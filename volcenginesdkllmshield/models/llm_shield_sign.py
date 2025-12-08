# coding:utf-8
"""
Copyright (year) Beijing Volcano Engine Technology Ltd.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import datetime
import hashlib
import hmac
from urllib.parse import quote, urlparse
import requests

# 以下参数视服务不同而不同，一个服务内通常是一致的
Version = "2025-08-31"
ContentType = "application/json"
Method = "POST"

ServiceCodeDev = "llmshield_dev"
ServiceCodeOnline = "llmshield"
Service = ServiceCodeOnline


def SetServiceDev(IsDev: bool):
    global Service, ServiceCodeDev, ServiceCodeOnline
    if IsDev:
        Service = ServiceCodeDev
    else:
        Service = ServiceCodeOnline


def GetServiceCode():
    global Service
    return Service


def norm_query(params):
    query = ""
    for key in sorted(params.keys()):
        if type(params[key]) == list:
            for k in params[key]:
                query = (
                        query + quote(key, safe="-_.~") + "=" + quote(k, safe="-_.~") + "&"
                )
        else:
            query = (query + quote(key, safe="-_.~") + "=" + quote(params[key], safe="-_.~") + "&")
    query = query[:-1]
    return query.replace("+", "%20")


# 第一步：准备辅助函数。
# sha256 非对称加密
def hmac_sha256(key: bytes, content: str):
    return hmac.new(key, content.encode("utf-8"), hashlib.sha256).digest()


# sha256 hash算法
def hash_sha256(content: bytes):
    return hashlib.sha256(content).hexdigest()


# 第二步：签名请求函数
def request_sign(header, ak, sk, region, url, path, action, body):
    host = urlparse(url).netloc
    date = utc_now()
    # 第三步：创建身份证明。其中的 Service 和 Region 字段是固定的。ak 和 sk 分别代表
    # AccessKeyID 和 SecretAccessKey。同时需要初始化签名结构体。一些签名计算时需要的属性也在这里处理。
    # 初始化身份证明结构体
    credential = {
        "access_key_id": ak,
        "secret_access_key": sk,
        "service": Service,
        "region": region,
    }
    # 初始化签名结构体
    request_param = {
        "body": body,
        "host": host,
        "path": path,
        "method": Method,
        "content_type": ContentType,
        "date": date,
        "query": {"Action": action, "Version": Version},
    }
    if body is None:
        request_param["body"] = ""
    # 第四步：接下来开始计算签名。在计算签名前，先准备好用于接收签算结果的 signResult 变量，并设置一些参数。
    # 初始化签名结果的结构体
    x_date = request_param["date"].strftime("%Y%m%dT%H%M%SZ")
    short_x_date = x_date[:8]
    x_content_sha256 = hash_sha256(request_param["body"])
    sign_result = {
        "Host": request_param["host"],
        "X-Content-Sha256": x_content_sha256,
        "X-Date": x_date,
        "Content-Type": request_param["content_type"],
    }
    # 第五步：计算 Signature 签名。
    signed_headers_str = ";".join(
        ["content-type", "host", "x-content-sha256", "x-date"]
    )
    # signed_headers_str = signed_headers_str + ";x-security-token"
    canonical_request_str = "\n".join(
        [request_param["method"].upper(),
         request_param["path"],
         norm_query(request_param["query"]),
         "\n".join(
             [
                 "content-type:" + request_param["content_type"],
                 "host:" + request_param["host"],
                 "x-content-sha256:" + x_content_sha256,
                 "x-date:" + x_date,
             ]
         ),
         "",
         signed_headers_str,
         x_content_sha256,
         ]
    )

    # 打印正规化的请求用于调试比对
    # print(canonical_request_str)
    hashed_canonical_request = hash_sha256(canonical_request_str.encode("utf-8"))

    # 打印hash值用于调试比对
    # print(hashed_canonical_request)
    credential_scope = "/".join([short_x_date, credential["region"], credential["service"], "request"])
    string_to_sign = "\n".join(["HMAC-SHA256", x_date, credential_scope, hashed_canonical_request])

    # 打印最终计算的签名字符串用于调试比对
    # print(string_to_sign)
    k_date = hmac_sha256(credential["secret_access_key"].encode("utf-8"), short_x_date)
    k_region = hmac_sha256(k_date, credential["region"])
    k_service = hmac_sha256(k_region, credential["service"])
    k_signing = hmac_sha256(k_service, "request")
    signature = hmac_sha256(k_signing, string_to_sign).hex()

    sign_result["Authorization"] = "HMAC-SHA256 Credential={}, SignedHeaders={}, Signature={}".format(
        credential["access_key_id"] + "/" + credential_scope,
        signed_headers_str,
        signature,
    )
    header = {**header, **sign_result, "X-Top-Service": Service, "X-Top-Region": region}
    # header = {**header, **{"X-Security-Token": SessionToken}}
    # 第六步：将 Signature 签名写入 HTTP Header 中，并发送 HTTP 请求。
    return header


# datetime.utcnow() 在 3.12+ 已经过期，使用如下方法兼容
def utc_now():
    try:
        from datetime import timezone
        return datetime.datetime.now(timezone.utc)
    except ImportError:
        class UTC(datetime.tzinfo):
            def utcoffset(self, dt):
                return datetime.timedelta(0)

            def tzname(self, dt):
                return "UTC"

            def dst(self, dt):
                return datetime.timedelta(0)

        return datetime.datetime.now(UTC())
