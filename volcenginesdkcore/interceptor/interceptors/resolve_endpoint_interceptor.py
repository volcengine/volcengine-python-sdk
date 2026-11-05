# coding: utf-8
from .interceptor import RequestInterceptor
from ...endpoint.providers.default_provider import HostEndpointProvider
from ...endpoint.validation import validate_service_and_region
from ...observability.debugger import sdk_core_logger


class ResolveEndpointInterceptor(RequestInterceptor):

    run_on_retry = False

    def name(self):
        return 'volcengine-resolve-endpoint-interceptor'

    def intercept(self, context):
        host = context.request.host
        scheme = context.request.scheme
        if not host:
            service = context.request.resource_path.split('/')[3]
            # 显式固定 Host 不依赖输入；其他解析器必须在收到输入前完成校验。
            if type(context.request.endpoint_provider) is not HostEndpointProvider:
                validate_service_and_region(service, context.request.region)
            endpoint_resolver = context.request.endpoint_provider.endpoint_for(
                service, context.request.region,
                custom_bootstrap_region=context.request.custom_bootstrap_region,
                use_dual_stack=context.request.use_dual_stack)
            context.request.host = endpoint_resolver.host
            prefix = endpoint_resolver.url_for(scheme)
        else:
            if host.startswith('https://'):
                prefix = host
                context.request.host = host[len('https://'):]
            elif host.startswith('http://'):
                prefix = host
                context.request.host = host[len('http://'):]
            else:
                prefix = scheme + '://' + host
        context.request.url = prefix + context.request.true_path
        sdk_core_logger.debug_endpoint(
            "Using endpoint: %s", context.request.host
        )
        return context
