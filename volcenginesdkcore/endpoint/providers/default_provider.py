# coding=utf-8
from volcenginesdkcore.endpoint.endpoint_provider import EndpointProvider, ResolvedEndpoint

fallback_endpoint = 'open.volcengineapi.com'


class DefaultEndpointConfig:
    def __init__(self, service, is_global, global_endpoint,
                 region_endpoint_map, fallback_endpoint=fallback_endpoint):
        self.service = service
        self.is_global = is_global
        self.global_endpoint = global_endpoint
        self.region_endpoint_map = region_endpoint_map
        self.fallback_endpoint = fallback_endpoint


def get_default_endpoint(service, region):
    if service in default_endpoint:
        e = default_endpoint[service]
        if e.is_global:
            return e.global_endpoint
        if region in e.region_endpoint_map:
            return e.region_endpoint_map[region]
        return e.fallback_endpoint
    return fallback_endpoint


default_endpoint = {
    'ecs': DefaultEndpointConfig(
        service='ecs',
        is_global=False,
        global_endpoint='',
        region_endpoint_map={
            'cn-beijing-autodriving': 'ecs' + '.' + 'cn-beijing-autodriving' + '.volcengineapi.com'
        }
    ),
}


class DefaultEndpointProvider(EndpointProvider):

    def __init__(self, custom_endpoints=None):
        self.scheme = 'https'
        self.custom_endpoints = custom_endpoints or {}

    def endpoint_for(self, service, region):
        # 检查自定义终端节点配置
        if service in self.custom_endpoints:
            url = self.custom_endpoints[service]
        else:
            url = get_default_endpoint(service=service, region=region)

        return ResolvedEndpoint(url, self.scheme)


class HostEndpointProvider(EndpointProvider):
    def __init__(self, host):
        self.host = host
        self.scheme = 'https'

    def endpoint_for(self, service, region):
        return ResolvedEndpoint(self.host, self.scheme)
