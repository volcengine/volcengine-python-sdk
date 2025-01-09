from __future__ import annotations

import datetime
import functools
import random
import string
from typing import (
    Any,
    Mapping,
    Callable,
    cast,
    TypeVar,
)

from typing_extensions import TypeGuard

from .._types import NotGiven

CallableT = TypeVar("CallableT", bound=Callable[..., Any])


def _gen_request_id():
    time_str = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    chars = string.ascii_letters + string.digits
    rand_str = "".join(random.choice(chars) for i in range(20))
    return f"{time_str}{rand_str}"


def is_mapping(obj: object) -> TypeGuard[Mapping[str, object]]:
    return isinstance(obj, Mapping)


def is_list(obj: object) -> TypeGuard[list[object]]:
    return isinstance(obj, list)


def coerce_boolean(val: str) -> bool:
    return val == "true" or val == "1" or val == "on"


def lru_cache(*, maxsize: int | None = 128) -> Callable[[CallableT], CallableT]:
    """A version of functools.lru_cache that retains the type signature
    for the wrapped function arguments.
    """
    wrapper = functools.lru_cache(  # noqa: TID251
        maxsize=maxsize,
    )
    return cast(Any, wrapper)  # type: ignore[no-any-return]


def strip_not_given(obj: object | None) -> object:
    """Remove all top-level keys where their values are instances of `NotGiven`"""
    if obj is None:
        return None

    if not is_mapping(obj):
        return obj

    return {key: value for key, value in obj.items() if not isinstance(value, NotGiven)}


def with_sts_token(func):
    def wrapper(*args, **kwargs):
        _insert_sts_token(args, kwargs)
        return func(*args, **kwargs)

    return wrapper


def async_with_sts_token(func):
    async def wrapper(*args, **kwargs):
        _insert_sts_token(args, kwargs)
        return await func(*args, **kwargs)

    return wrapper


def _insert_sts_token(args, kwargs):
    assert len(args) > 0
    assert "model" in kwargs, "you need to support model"

    ark_client = args[0]._client
    model = kwargs.get("model", "")
    if ark_client.api_key is None and model and model.startswith("ep-") and ark_client.ak and ark_client.sk:
        default_auth_header = {"Authorization": "Bearer " + ark_client._get_endpoint_sts_token(model)}
        extra_headers = kwargs.get("extra_headers") if kwargs.get("extra_headers") else {}
        kwargs["extra_headers"] = {**default_auth_header, **extra_headers}
    elif ark_client.api_key is None and model and model.startswith("bot-") and ark_client.ak and ark_client.sk:
        default_auth_header = {"Authorization": "Bearer " + ark_client._get_bot_sts_token(model)}
        extra_headers = kwargs.get("extra_headers") if kwargs.get("extra_headers") else {}
        kwargs["extra_headers"] = {**default_auth_header, **extra_headers}


def apikey_required(func):
    def wrapper(*args, **kwargs):
        _assert_apikey(args, kwargs)
        return func(*args, **kwargs)

    return wrapper


def async_apikey_required(func):
    async def wrapper(*args, **kwargs):
        _assert_apikey(args, kwargs)
        return await func(*args, **kwargs)

    return wrapper


def _assert_apikey(args, kwargs):
    assert len(args) > 0

    ark_client = args[0]._client
    assert ark_client.api_key is not None, \
        "ak&sk authentication is currently not supported for this method, please use api key instead"
