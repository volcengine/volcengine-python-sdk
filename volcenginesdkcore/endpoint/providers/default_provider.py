# coding=utf-8
import os

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

    @property
    def __standardize_domain_service_code(self):
        return self.service.lower().replace('_', '-')

    def get_endpoint_for(self, region, enable_dualstack=False):
        suffix = '.volcengine-api.com' if enable_dualstack else '.volcengineapi.com'

        if self.is_global:
            if self.global_endpoint:
                return self.global_endpoint
            return self.__standardize_domain_service_code + suffix
        if region in self.region_endpoint_map:
            return self.region_endpoint_map[region]

        return self.__standardize_domain_service_code + '.' + region + suffix


class DefaultEndpointProvider(EndpointProvider):
    region_code_cn_beijing_auto_driving = "cn-beijing-autodriving"
    region_code_ap_southeast3 = "ap-southeast-3"

    default_endpoint = {
        'ecs': ServiceEndpointInfo(
            service='ecs',
            is_global=False,
            global_endpoint='',
            region_endpoint_map={},
        ),
    }

    bootstrap_region = {
        region_code_cn_beijing_auto_driving: {},
        region_code_ap_southeast3: {},
    }

    def __init__(self, custom_endpoints=None):
        self.custom_endpoints = custom_endpoints or {}

    def get_default_endpoint(self, service, region):
        if service in self.default_endpoint:
            e = self.default_endpoint[service]
            return e.get_endpoint_for(region, self.__has_enabled_dualstack())
        return fallback_endpoint

    def __in_bootstrap_region_list(self, region, custom_bootstrap_region):
        region_code = region.strip()
        bs_region_list_path = os.getenv('VOLC_BOOTSTRAP_REGION_LIST_CONF')
        if bs_region_list_path:
            try:
                with open(bs_region_list_path, 'r') as f:
                    content = f.read()
                    lines = content.split('\n')
                    for line in lines:
                        line = line.strip()
                        if not line:
                            continue
                        if line == region_code:
                            return True
            except Exception:
                pass

        if self.bootstrap_region:
            if region_code in self.bootstrap_region:
                return True

        if custom_bootstrap_region:
            return region_code in custom_bootstrap_region

        return False

    @staticmethod
    def __has_enabled_dualstack():
        return os.getenv("VOLC_ENABLE_DUALSTACK") == 'true'

    def endpoint_for(self, service, region, custom_bootstrap_region=None):
        if service in self.custom_endpoints:
            conf = self.custom_endpoints[service]
            host = conf.get_endpoint_for(region)
        else:
            if custom_bootstrap_region is None:
                custom_bootstrap_region = {}
            if not self.__in_bootstrap_region_list(region, custom_bootstrap_region):
                return fallback_endpoint

            host = self.get_default_endpoint(service=service, region=region)

        return ResolvedEndpoint(host)


class HostEndpointProvider(EndpointProvider):
    def __init__(self, host):
        self.host = host

    def endpoint_for(self, service, region):
        return ResolvedEndpoint(self.host)
