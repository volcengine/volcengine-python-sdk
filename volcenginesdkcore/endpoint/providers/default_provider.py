# coding=utf-8
from volcenginesdkcore.endpoint.endpoint_provider import EndpointProvider, ResolvedEndpoint

fallback_endpoint = 'open.volcengineapi.com'


class ServiceEndpointInfo:
    def __init__(self, service, is_global, global_endpoint,
                 region_endpoint_map, fallback_endpoint=fallback_endpoint):
        self.service = service
        self.is_global = is_global
        self.global_endpoint = global_endpoint
        self.region_endpoint_map = region_endpoint_map
        self.fallback_endpoint = fallback_endpoint

    def get_endpoint_for(self, region):
        if self.is_global:
            return self.global_endpoint
        if region in self.region_endpoint_map:
            return self.region_endpoint_map[region]
        return self.fallback_endpoint


class DefaultEndpointProvider(EndpointProvider):
    default_endpoint = {
        'ecs': ServiceEndpointInfo(
            service='ecs',
            is_global=False,
            global_endpoint='',
            region_endpoint_map={
                'cn-beijing-autodriving': 'ecs' + '.' + 'cn-beijing-autodriving' + '.volcengineapi.com'
            }
        ),
    }

    def __init__(self, custom_endpoints=None):
        self.custom_endpoints = custom_endpoints or {}

    def get_default_endpoint(self, service, region):
        if service in self.default_endpoint:
            e = self.default_endpoint[service]
            return e.get_endpoint_for(region)
        return fallback_endpoint

    def endpoint_for(self, service, region):
        if service in self.custom_endpoints:
            conf = self.custom_endpoints[service]
            host = conf.get_endpoint_for(region)
        else:
            host = self.get_default_endpoint(service=service, region=region)

        return ResolvedEndpoint(host)


class HostEndpointProvider(EndpointProvider):
    def __init__(self, host):
        self.host = host

    def endpoint_for(self, service, region):
        return ResolvedEndpoint(self.host)
