# coding: utf-8
import json

from volcenginesdkcore.signv4 import SignerV4
from .interceptor import RequestInterceptor


class SignRequestInterceptor(RequestInterceptor):

    def name(self):
        return 'volcengine-sign-request-interceptor'

    def intercept(self, context):
        # 新增代码。处理assume_role和assume_role_oidc和assume_role_saml
        if context.request.credential_provider is None and not context.request.ak and not context.request.sk:
            # No explicit credentials or provider set — use default credential chain.
            # Cache on the interceptor instance so subsequent requests reuse the same
            # DefaultCredentialProvider (preserving reuseLastProviderEnabled behavior).
            from volcenginesdkcore.auth.providers.default_provider import DefaultCredentialProvider
            if not hasattr(self, '_default_credential_provider') or self._default_credential_provider is None:
                self._default_credential_provider = DefaultCredentialProvider()
            context.request.credential_provider = self._default_credential_provider

        if context.request.credential_provider is not None:
            credentials = context.request.credential_provider.get_credentials()
            context.request.ak = credentials.ak
            context.request.sk = credentials.sk
            context.request.session_token = credentials.session_token

        if context.request.is_presign:
            context.request.signed_query = SignerV4.sign_url(
                path=context.request.true_path,
                method=context.request.method,
                query=context.request.query_params,
                ak=context.request.ak,
                sk=context.request.sk,
                region=context.request.region,
                service=context.request.service,
                session_token=context.request.session_token,
                host=context.request.host,
            )
        else:
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
            if method in ["POST", "PUT", "DELETE", "PATCH"] and body is not None:
                body = json.dumps(body)
            else:
                body = ""
            SignerV4.sign(path, method, headers, body, post_params, querys,
                          ak, sk,
                          region, service, session_token)
