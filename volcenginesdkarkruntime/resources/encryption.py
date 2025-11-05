from __future__ import annotations
from .._constants import ARK_E2E_ENCRYPTION_HEADER
from .._streaming import Stream, AsyncStream
from ..types.chat import (
    ChatCompletion,
    ChatCompletionChunk,
)

import os
import json
import warnings
from copy import deepcopy
from urllib.parse import urlparse
from typing import (
    Union,
    Iterable,
    Callable,
    Iterator,
    AsyncIterator,
)

from .._utils._key_agreement import (
    aes_gcm_decrypt_base64_string,
    aes_gcm_decrypt_base64_list,
    decrypt_validate,
)


def _decrypt_chunk(
    key: bytes, nonce: bytes, resp: Stream[ChatCompletionChunk]
) -> Iterator[ChatCompletionChunk]:
    for chunk in resp:
        if chunk.choices is not None:
            for index, choice in enumerate(chunk.choices):
                if (
                    choice.delta is not None
                    and choice.delta.content is not None
                    and choice.finish_reason != "content_filter"
                ):
                    choice.delta.content = aes_gcm_decrypt_base64_string(
                        key, nonce, choice.delta.content
                    )
                chunk.choices[index] = choice
        yield chunk


async def _async_decrypt_chunk(
    key: bytes, nonce: bytes, resp: AsyncStream[ChatCompletionChunk]
) -> AsyncIterator[ChatCompletionChunk]:
    async for chunk in resp:
        if chunk.choices is not None:
            for index, choice in enumerate(chunk.choices):
                if (
                    choice.delta is not None
                    and choice.delta.content is not None
                    and choice.finish_reason != "content_filter"
                ):
                    choice.delta.content = aes_gcm_decrypt_base64_string(
                        key, nonce, choice.delta.content
                    )
                chunk.choices[index] = choice
        yield chunk


def _decrypt(
    key: bytes, nonce: bytes, resp: Union[ChatCompletion, Stream[ChatCompletionChunk]]
) -> ChatCompletion | Stream[ChatCompletionChunk]:
    if isinstance(resp, ChatCompletion):
        if resp.choices is not None:
            for index, choice in enumerate(resp.choices):
                if (
                    choice.message is not None
                    and choice.finish_reason != "content_filter"
                    and choice.message.content is not None
                ):
                    try:
                        content = aes_gcm_decrypt_base64_string(
                            key, nonce, choice.message.content
                        )
                    except Exception:
                        content = ""
                    if content == "" or not decrypt_validate(choice.message.content):
                        content = aes_gcm_decrypt_base64_list(
                            key, nonce, choice.message.content
                        )
                    choice.message.content = content
                resp.choices[index] = choice
        return resp
    else:
        return Stream._make_stream_from_iterator(_decrypt_chunk(key, nonce, resp))


async def _async_decrypt(
    key: bytes,
    nonce: bytes,
    resp: ChatCompletion | AsyncStream[ChatCompletionChunk],
) -> ChatCompletion | AsyncStream[ChatCompletionChunk]:
    if isinstance(resp, ChatCompletion):
        if resp.choices is not None:
            for index, choice in enumerate(resp.choices):
                if (
                    choice.message is not None
                    and choice.finish_reason != "content_filter"
                    and choice.message.content is not None
                ):
                    try:
                        content = aes_gcm_decrypt_base64_string(
                            key, nonce, choice.message.content
                        )
                    except Exception:
                        content = ""
                    if content == "" or not decrypt_validate(choice.message.content):
                        content = aes_gcm_decrypt_base64_list(
                            key, nonce, choice.message.content
                        )
                    choice.message.content = content
                resp.choices[index] = choice
        return resp
    else:
        return AsyncStream._make_stream_from_iterator(
            _async_decrypt_chunk(key, nonce, resp)
        )


def with_e2e_encryption(func):
    def wrapper(*args, **kwargs):
        is_encrypt, _crypto_key, _crypto_nonce = _content_encryption(args, kwargs)
        resp = func(*args, **kwargs)
        if is_encrypt:
            resp = _decrypt(_crypto_key, _crypto_nonce, resp)
        return resp

    return wrapper


def async_with_e2e_encryption(func):
    async def wrapper(*args, **kwargs):
        is_encrypt, _crypto_key, _crypto_nonce = _content_encryption(args, kwargs)
        resp = await func(*args, **kwargs)
        if is_encrypt:
            resp = await _async_decrypt(_crypto_key, _crypto_nonce, resp)
        return resp

    return wrapper


def _content_encryption(args, kwargs):
    assert len(args) > 0
    extra_headers = kwargs.get("extra_headers") if kwargs.get("extra_headers") else {}
    if (
        extra_headers is not None
        and extra_headers.get(ARK_E2E_ENCRYPTION_HEADER, None) == "true"
    ):
        model: str = kwargs.get("model", "")
        messages = deepcopy(kwargs["messages"])
        ark_client = args[0]._client
        client, ring_id, key_id, exp_time = ark_client._get_endpoint_certificate(model)
        _crypto_key, _crypto_nonce, session_token = client.generate_ecies_key_pair()
        extra_headers["X-Session-Token"] = session_token
        _process_messages(
            messages,
            lambda x: client.encrypt_string_with_key(_crypto_key, _crypto_nonce, x),
        )
        info = {"ExpireTime": exp_time}
        if os.environ.get("VOLC_ARK_ENCRYPTION") == "AICC":
            info["Version"] = "AICCv0.1"
            info["KeyID"] = key_id
            info["RingID"] = ring_id
        extra_headers["X-Encrypt-Info"] = json.dumps(info)
        kwargs["extra_headers"] = {**extra_headers}
        kwargs["messages"] = messages
        return True, _crypto_key, _crypto_nonce
    return False, None, None


def _process_messages(messages, f: Callable[[str], str]):
    for message in messages:
        if message.get("content", None) is not None:
            current_content = message.get("content")
            if isinstance(current_content, str):
                message["content"] = f(current_content)
            elif isinstance(current_content, Iterable):
                for part in current_content:
                    if part.get("type", None) == "text":
                        part["text"] = f(part["text"])
                    elif part.get("type", None) == "image_url":
                        parse_result = urlparse(part["image_url"]["url"])
                        if parse_result.scheme == "data":
                            part["image_url"]["url"] = f(part["image_url"]["url"])
                        elif (
                            parse_result.scheme == "http"
                            or parse_result.scheme == "https"
                        ):
                            warnings.warn(
                                "encryption is not supported for image url, "
                                "please use base64 image if you want encryption"
                            )
                        else:
                            raise TypeError(
                                "encryption is not supported for image url scheme {}".format(
                                    parse_result
                                )
                            )
                    else:
                        raise TypeError(
                            "encryption is not supported for content type {}".format(
                                type(part)
                            )
                        )
            else:
                raise TypeError(
                    "encryption is not supported for content type {}".format(
                        type(message.get("content"))
                    )
                )
