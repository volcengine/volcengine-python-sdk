import json

from volcenginesdkcore.signv4 import SignerV4
from .interceptor import RequestInterceptor


class SignRequestInterceptor(RequestInterceptor):

    def name(self):
        return 'volcengine-sign-request-interceptor'

    def intercept(self, context):
        self.update_params_for_auth(host=context.request.host, path=context.request.true_path,
                                    method=context.request.method,
                                    headers=context.request.header_params,
                                    querys=context.request.query_params,
                                    auth_settings=context.request.auth_settings,
                                    body=context.request.body,
                                    post_params=context.request.post_params,
                                    service=context.request.service,
                                    ak=context.request.ak,
                                    sk=context.request.sk,
                                    session_token=context.request.session_token,
                                    region=context.request.region)
        return context

    @staticmethod
    def update_params_for_auth(host, path, method, headers, querys, auth_settings, body, post_params, service, ak,
                               sk, session_token, region):
        if not auth_settings:
            return

        for auth in auth_settings:
            headers["Host"] = host
            if method in ["POST", "PUT", "DELETE", "PATCH"]:
                body = json.dumps(body)
            else:
                body = ""
            SignerV4.sign(path, method, headers, body, post_params, querys,
                          ak, sk,
                          region, service, session_token)
