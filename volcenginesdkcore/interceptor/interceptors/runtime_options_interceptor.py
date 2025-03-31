# coding=utf-8

from urllib3 import Timeout

from .interceptor import RequestInterceptor


class RuntimeOptionsInterceptor(RequestInterceptor):

    def name(self):
        return 'volcengine-runtime-options-interceptor'

    def intercept(self, context):
        opt = context.request.runtime_options
        if not opt:
            return context

        context.request.ak = opt.ak if opt.ak is not None else context.request.ak
        context.request.sk = opt.sk if opt.sk is not None else context.request.sk
        context.request.session_token = opt.session_token \
            if opt.session_token is not None else context.request.session_token
        context.request.region = opt.region if opt.region is not None else context.request.region
        context.request.scheme = opt.scheme if opt.scheme is not None else context.request.scheme

        if opt.connect_timeout is not None or opt.read_timeout is not None:
            context.request.request_timeout = Timeout(
                connect=opt.connect_timeout if opt.connect_timeout is not None else -1,
                read=opt.read_timeout if opt.read_timeout is not None else -1,
            )

        if opt.endpoint_provider is not None:
            context.request.endpoint_provider = opt.endpoint_provider
            context.request.host = None

        return context
