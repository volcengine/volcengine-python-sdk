__all__ = [
    "RepeatTimer",
    "WeakMethod",
    "weak_repeat_timer",
    "request_bytedance_gateway",
]

import hashlib
import hmac
import json
import os
import urllib.parse
import weakref
from datetime import datetime, timezone
from threading import Timer
from typing import Dict

import requests
import volcenginesdkcore
import volcenginesdksts
from typing_extensions import (
    Any,
    Callable,
    Concatenate,
    Generic,
    Iterable,
    Mapping,
    Optional,
    ParamSpec,
    Protocol,
    TypeVar,
)
from volcenginesdkcore.rest import ApiException

from . import error
from .log import logger


class RepeatTimer(Timer):
    """
    定时重复执行函数.
    """

    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)


T = TypeVar("T")
P = ParamSpec("P")
R = TypeVar("R")
R_co = TypeVar("R_co", covariant=True)


class MethodProtocol(Protocol[T, P, R]):
    __self__: T

    __func__: Callable[Concatenate[T, P], R]

    __call__: Callable[P, R]


class WeakMethod(Generic[T, P, R_co]):
    """
    对方法 (bound method) 的弱引用.
    """

    # instance: weakref.ReferenceType[T]
    # func: weakref.ReferenceType[Callable[Concatenate[T, P], R_co]]

    def __init__(self, method: Callable[P, R_co]):
        # Type checkers do not differentiate methods from callables, so
        # we have to ignore the casting error
        _method: MethodProtocol[T, P, R_co] = method  # pyright: ignore

        self.instance = weakref.ref(_method.__self__)
        self.func = weakref.ref(_method.__func__)

    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> Optional[R_co]:
        instance = self.instance()
        func = self.func()

        if instance is None or func is None:
            logger.info("Weak method called on freed object")
            return

        return func(instance, *args, **kwargs)


def weak_repeat_timer(
    interval: float,
    method: Callable[P, None],
    args: Optional[Iterable[Any]] = None,
    kwargs: Optional[Mapping[str, Any]] = None,
) -> RepeatTimer:
    """
    定时重复执行对象上的方法. 在对象被垃圾回收时自动结束线程.
    """
    # Due to limitations of 'ParamSpec', we cannot annotate 'args' and 'kwargs' precisely
    timer = RepeatTimer(interval, WeakMethod(method), args, kwargs)
    weakref.finalize(method.__self__, timer.cancel)  # pyright: ignore

    return timer


class TopRequester:
    def __init__(
        self,
        ak,
        sk,
        token=None,
        host="open.volcengineapi.com",
        region="cn-beijing",
        use_tls=True,
        service="pcc",
        version="2024-12-24",
        debug=False,
    ):
        volc_config = volcenginesdkcore.Configuration()
        volc_config.host = host
        volc_config.ak = ak
        volc_config.sk = sk
        volc_config.session_token = token
        volc_config.region = region
        volc_config.debug = debug
        if use_tls:
            volc_config.scheme = "https"
        else:
            volc_config.scheme = "http"
        self._api_client = volcenginesdkcore.ApiClient(configuration=volc_config)
        self._service = service
        self._version = version

    def _construct_resource_path(
        self,
        action: str,
        version: str,
        service: str,
        method: str = "post",
        content_type: str = "application_json",
    ) -> str:
        return f"/{action}/{version}/{service}/{method.lower()}/{content_type}/"

    def request(
        self,
        method,
        query,
        header,
        param,
        action,
        body,
        service=None,
        version=None,
        content_type="application/json",
    ):
        resp = self._api_client.call_api(
            self._construct_resource_path(
                action=action,
                version=self._version if not version else version,
                service=self._service if not service else service,
                method=method,
                content_type=content_type.replace("/", "_"),
            ),
            method,
            body=body,
            auth_settings=["volcengineSign"],
            header_params={
                "Accept": "application/json",
                "Content-Type": content_type,
                **header,
            },
            path_params=param,
            query_params=query,
            post_params=[],
            files={},
            response_type=bytes,
            collection_formats={},
            _return_http_data_only=False,
            _preload_content=True,
        )

        status, headers, data = resp[1], resp[2], resp[0]
        logger.info(f"Top request response,status={status}, headers: {headers}")

        return data

    def request_with_assume_role(
        self,
        method,
        query,
        header,
        param,
        service,
        action,
        body,
        version,
        target_uid,
        target_resource=None,
        region="cn-beijing",
        content_type="application/json",
        use_tls=True,
        host="open.volcengineapi.com",
    ):
        data = {
            "TargetAccount": target_uid,
            "TargetResource": os.getenv("PCC_SERVICE", "pcc")
            if not target_resource
            else target_resource,
        }
        access_info = self.request("POST", [], {}, {}, "UpdateUserAccessInfo", data)
        ak = access_info["Ak"]
        sk = access_info["Sk"]
        sts_token = access_info["StsToken"]

        customer_requester = TopRequester(
            ak=ak, sk=sk, token=sts_token, region=region, use_tls=use_tls, host=host
        )
        return customer_requester.request(
            method, query, header, param, action, body, service, version, content_type
        )


def _hmac_sha256(key: bytes, content: str):
    return hmac.new(key, content.encode(), hashlib.sha256).digest()


def _hash_sha256(content: str):
    return hashlib.sha256(content.encode()).hexdigest()


def _format_query(params: Dict[str, str]) -> str:
    return "&".join(
        urllib.parse.quote(key, safe="-_.~")
        + "="
        + urllib.parse.quote(value, safe="-_.~")
        for key, value in params.items()
    )


def top_request(
    ra_url: str,
    body: Any,
    additional_headers: Optional[Dict[str, str]],
    top_config: Dict[str, str],
) -> requests.Response:
    top_ak = top_config["ak"]
    top_sk = top_config["sk"]
    top_service = top_config["service"]
    top_region = top_config.get("region", "cn-beijing")
    top_method = top_config.get("method", "POST").upper()
    top_action = top_config.get("action", "GetAttestationBackend")
    top_version = top_config.get("version", "2024-12-24")
    use_tls: bool = top_config.get("use_tls", True)  # type: ignore
    sts_token = top_config.get("sts_token", None)
    target_uid = top_config.get("target_uid", None)
    target_resource = top_config.get("target_resource", "pcc")

    if ra_url:
        top_host = ra_url
    else:
        top_host = top_config.get("url", "open.volcengineapi.com")

    requester = TopRequester(
        ak=top_ak,
        sk=top_sk,
        token=sts_token,
        region=top_region,
        use_tls=use_tls,
        host=top_host,
        service=top_service,
        version=top_version,
    )

    resp = None
    if not target_uid:
        try:
            resp = requester.request(
                top_method, [], additional_headers, {}, top_action, body
            )
        except ApiException as e:
            logger.error(
                "status: {}, reason: {}, body: {}, headers: {}".format(
                    e.status, e.reason, e.body, e.headers
                )
            )
            raise e
        except Exception as e:
            logger.error("request error: {}".format(e))
            raise e
    else:
        try:
            resp = requester.request_with_assume_role(
                top_method,
                [],
                additional_headers,
                {},
                top_service,
                top_action,
                body,
                top_version,
                target_uid,
                target_resource,
                top_region,
                use_tls=use_tls,
                host=top_host
            )
        except ApiException as e:
            logger.error(
                "status: {}, reason: {}, body: {}, headers: {}".format(
                    e.status, e.reason, e.body, e.headers
                )
            )
            raise e
        except Exception as e:
            logger.error("request error: {}".format(e))
            raise e

    return resp


def get_top_access_key(top_config: Dict[str, str]) -> tuple:
    try:
        configuration = volcenginesdkcore.Configuration()
        configuration.ak = top_config.get("ak")
        configuration.sk = top_config.get("sk")
        configuration.region = top_config.get("region", "cn-beijing")

        duration_seconds = int(top_config.get("duration_seconds", "3600"))
        role_session_name = top_config.get("role_session_name", "temp_")
        role_trn = top_config.get("aicc_saas_trn")

        volcenginesdkcore.Configuration.set_default(configuration)

        api_instance = volcenginesdksts.STSApi()
        assume_role_request = volcenginesdksts.AssumeRoleRequest(
            duration_seconds=duration_seconds,
            role_session_name=role_session_name,
            role_trn=role_trn,
        )

        ret = api_instance.assume_role(assume_role_request)
        if ret and ret.credentials:
            ak = ret.credentials.access_key_id
            sk = ret.credentials.secret_access_key
            session_token = ret.credentials.session_token

            return ak, sk, session_token
        else:
            return None, None, None

    except Exception as e:
        logger.error("get_top_access_key: {}".format(e))
        raise e


# The first parameter was url, and is now unused
def request_bytedance_gateway(
    url: str,
    body: Any,
    additional_headers: Optional[Dict[str, str]],
    top_config: Dict[str, str],
) -> requests.Response:
    top_ak = top_config["ak"]
    top_sk = top_config["sk"]

    if not additional_headers:
        additional_headers = dict()

    if top_config.get("aicc_saas_trn"):
        ak, sk, session_token = get_top_access_key(top_config)
        if ak and sk and session_token:
            top_ak = ak
            top_sk = sk
            additional_headers["X-Security-Token"] = session_token
            additional_headers["sts_token"] = session_token
        if top_config.get("target_uid"):
            additional_headers["UID"] = top_config.get("target_uid")

    top_service = top_config["service"]
    top_region = top_config.get("region", "cn-beijing")
    top_method = top_config.get("method", "POST").upper()
    top_action = top_config.get("action", "GetAttestationBackend")
    top_version = top_config.get("version", "2024-12-24")
    url_rewrite = top_config.get("url_rewrite", "")
    http_scheme = top_config.get("http_scheme", "https")

    top_url = top_config.get("url", "") if top_config.get("url", "") else url
    if not top_url:
        top_url = url_rewrite
    if not top_url:
        logger.error("ra request error url=None")
        raise error.ParamError("top_url", "top_url is None")

    if top_url.startswith("http"):
        url_parsed = urllib.parse.urlparse(top_url)
        top_host = url_parsed.hostname
    else:
        top_host = top_url

    params = {"Action": top_action, "Version": top_version}
    query_str = _format_query(params)

    date_now = datetime.now(timezone.utc)
    body_str = json.dumps(body, separators=(",", ":"))

    x_date = date_now.strftime("%Y%m%dT%H%M%SZ")
    short_x_date = x_date[:8]
    x_content_sha256 = _hash_sha256(body_str)

    headers = {
        "Content-Type": "application/json",
        "Host": top_host,
        "X-Content-Sha256": x_content_sha256,
        "X-Date": x_date,
    }

    signed_headers = ";".join(key.lower() for key in headers.keys())

    canonical_request = "\n".join(
        [
            top_method,
            "/",
            query_str,
            *[key.lower() + ":" + value for key, value in headers.items()],
            "",
            signed_headers,
            x_content_sha256,
        ]
    )

    canonical_request_hash = _hash_sha256(canonical_request)
    credential_scope = "/".join([short_x_date, top_region, top_service, "request"])
    string_to_sign = "\n".join(
        ["HMAC-SHA256", x_date, credential_scope, canonical_request_hash]
    )

    logger.debug(
        f"ra request={canonical_request}, hash={canonical_request_hash}, sign={string_to_sign}"
    )

    k_date = _hmac_sha256(top_sk.encode(), short_x_date)
    k_region = _hmac_sha256(k_date, top_region)
    k_service = _hmac_sha256(k_region, top_service)
    k_signing = _hmac_sha256(k_service, "request")
    signature = _hmac_sha256(k_signing, string_to_sign).hex()

    headers["Authorization"] = (
        f"HMAC-SHA256 Credential={top_ak}/{credential_scope}, SignedHeaders={signed_headers}, Signature={signature}"
    )

    if url_rewrite:
        url_parsed = urllib.parse.urlparse(url_rewrite)
        headers["Host"] = url_parsed.hostname or ""
        url_final = url_rewrite + "?" + query_str
    else:
        if top_url.startswith("http"):
            url_final = top_url + "?" + query_str
        else:
            url_final = f"{http_scheme}://{top_url}/?{query_str}"

    if additional_headers:
        headers = {**headers, **additional_headers}

    r = requests.request(
        method=top_method, url=url_final, headers=headers, data=body_str, timeout=30
    )
    logger.debug(f"call ra: url={url_final}, header={headers}, body={body_str}, res={json.loads(r.text).get('Result')}")
    logger.info(f"ra response headers: X-Tt-Logid={r.headers.get('X-Tt-Logid')}")
    return r
