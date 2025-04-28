from .interceptor import RequestInterceptor


class ResolveEndpointInterceptor(RequestInterceptor):

    def name(self):
        return 'volcengine-resolve-endpoint-interceptor'

    def intercept(self, context):
        host = context.request.host
        scheme = context.request.scheme
        if not host:
            service = context.request.resource_path.split('/')[3]
            endpoint_resolver = context.request.endpoint_provider.endpoint_for(
                service, context.request.region,
                custom_bootstrap_region=context.request.custom_bootstrap_region,
                use_dual_stack=context.request.use_dual_stack)
            context.request.host = endpoint_resolver.host
            prefix = endpoint_resolver.url_for(scheme)
        else:
            prefix = scheme + '://' + host
        context.request.url = prefix + context.request.true_path

        return context
