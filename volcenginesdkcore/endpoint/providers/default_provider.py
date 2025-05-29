# coding=utf-8
import os
import warnings

from volcenginesdkcore.endpoint.endpoint_provider import EndpointProvider, ResolvedEndpoint

open_prefix = 'open'
endpoint_suffix = '.volcengineapi.com'
dualstack_endpoint_suffix = '.volcengine-api.com'
fallback_endpoint = open_prefix + endpoint_suffix
region_code_cn_beijing_auto_driving = "cn-beijing-autodriving"
region_code_cn_shanghai_auto_driving = "cn-shanghai-autodriving"
region_code_ap_southeast2 = "ap-southeast-2"
region_code_ap_southeast3 = "ap-southeast-3"


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

    def get_endpoint_for(self, region, suffix=endpoint_suffix):
        if self.is_global:
            if self.global_endpoint:
                return self.global_endpoint
            return self.__standardize_domain_service_code + suffix
        if region in self.region_endpoint_map:
            return self.region_endpoint_map[region]

        return self.__standardize_domain_service_code + '.' + region + suffix


default_endpoint = {
    'ecs': ServiceEndpointInfo(
        service='ecs',
        is_global=False,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'billing': ServiceEndpointInfo(
        service='billing',
        is_global=True,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'advdefence': ServiceEndpointInfo(
        service='advdefence',
        is_global=True,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'alb': ServiceEndpointInfo(
        service='alb',
        is_global=False,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'auto_scaling': ServiceEndpointInfo(
        service='auto_scaling',
        is_global=False,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'bio': ServiceEndpointInfo(
        service='bio',
        is_global=False,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'vedbm': ServiceEndpointInfo(
        service='vedbm',
        is_global=False,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'pca': ServiceEndpointInfo(
        service='pca',
        is_global=True,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'cloud_trail': ServiceEndpointInfo(
        service='cloud_trail',
        is_global=False,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'nta': ServiceEndpointInfo(
        service='nta',
        is_global=True,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'kms': ServiceEndpointInfo(
        service='kms',
        is_global=False,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'tis': ServiceEndpointInfo(
        service='tis',
        is_global=True,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'vei_api': ServiceEndpointInfo(
        service='vei_api',
        is_global=True,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'rocketmq': ServiceEndpointInfo(
        service='rocketmq',
        is_global=False,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'emr': ServiceEndpointInfo(
        service='emr',
        is_global=False,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'iam': ServiceEndpointInfo(
        service='iam',
        is_global=True,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'volc_observe': ServiceEndpointInfo(
        service='volc_observe',
        is_global=False,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'vmp': ServiceEndpointInfo(
        service='vmp',
        is_global=False,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'cen': ServiceEndpointInfo(
        service='cen',
        is_global=True,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'escloud': ServiceEndpointInfo(
        service='escloud',
        is_global=False,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'ml_platform': ServiceEndpointInfo(
        service='ml_platform',
        is_global=False,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'vepfs': ServiceEndpointInfo(
        service='vepfs',
        is_global=False,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'redis': ServiceEndpointInfo(
        service='redis',
        is_global=False,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'filenas': ServiceEndpointInfo(
        service='filenas',
        is_global=False,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'vefaas': ServiceEndpointInfo(
        service='vefaas',
        is_global=False,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'vpn': ServiceEndpointInfo(
        service='vpn',
        is_global=False,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'vod': ServiceEndpointInfo(
        service='vod',
        is_global=False,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'fw_center': ServiceEndpointInfo(
        service='fw_center',
        is_global=True,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'privatelink': ServiceEndpointInfo(
        service='privatelink',
        is_global=False,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'rds_mssql': ServiceEndpointInfo(
        service='rds_mssql',
        is_global=False,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'waf': ServiceEndpointInfo(
        service='waf',
        is_global=True,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'mongodb': ServiceEndpointInfo(
        service='mongodb',
        is_global=False,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'smc': ServiceEndpointInfo(
        service='smc',
        is_global=True,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'rds_mysql': ServiceEndpointInfo(
        service='rds_mysql',
        is_global=False,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'seccenter': ServiceEndpointInfo(
        service='seccenter',
        is_global=True,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'mcdn': ServiceEndpointInfo(
        service='mcdn',
        is_global=True,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'dataleap': ServiceEndpointInfo(
        service='dataleap',
        is_global=False,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'edx': ServiceEndpointInfo(
        service='edx',
        is_global=True,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'natgateway': ServiceEndpointInfo(
        service='natgateway',
        is_global=False,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'rabbitmq': ServiceEndpointInfo(
        service='rabbitmq',
        is_global=False,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'httpdns': ServiceEndpointInfo(
        service='httpdns',
        is_global=True,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'translate': ServiceEndpointInfo(
        service='translate',
        is_global=True,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'cr': ServiceEndpointInfo(
        service='cr',
        is_global=False,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'spark': ServiceEndpointInfo(
        service='spark',
        is_global=True,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'cdn': ServiceEndpointInfo(
        service='cdn',
        is_global=True,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'clb': ServiceEndpointInfo(
        service='clb',
        is_global=False,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'cv': ServiceEndpointInfo(
        service='cv',
        is_global=True,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'tag': ServiceEndpointInfo(
        service='tag',
        is_global=True,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'vke': ServiceEndpointInfo(
        service='vke',
        is_global=False,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'mcs': ServiceEndpointInfo(
        service='mcs',
        is_global=False,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'flink': ServiceEndpointInfo(
        service='flink',
        is_global=False,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'kafka': ServiceEndpointInfo(
        service='kafka',
        is_global=False,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'rds_postgresql': ServiceEndpointInfo(
        service='rds_postgresql',
        is_global=False,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'sts': ServiceEndpointInfo(
        service='sts',
        is_global=False,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'ark': ServiceEndpointInfo(
        service='ark',
        is_global=False,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'transitrouter': ServiceEndpointInfo(
        service='transitrouter',
        is_global=False,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'cloud_detect': ServiceEndpointInfo(
        service='cloud_detect',
        is_global=True,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'vpc': ServiceEndpointInfo(
        service='vpc',
        is_global=False,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'certificate_service': ServiceEndpointInfo(
        service='certificate_service',
        is_global=True,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'dms': ServiceEndpointInfo(
        service='dms',
        is_global=False,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'dns': ServiceEndpointInfo(
        service='dns',
        is_global=True,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'directconnect': ServiceEndpointInfo(
        service='directconnect',
        is_global=False,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'storage_ebs': ServiceEndpointInfo(
        service='storage_ebs',
        is_global=False,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'quota': ServiceEndpointInfo(
        service='quota',
        is_global=True,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'fasttrack': ServiceEndpointInfo(
        service='fasttrack',
        is_global=False,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'acep': ServiceEndpointInfo(
        service='acep',
        is_global=True,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'private_zone': ServiceEndpointInfo(
        service='private_zone',
        is_global=True,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'sqs': ServiceEndpointInfo(
        service='sqs',
        is_global=False,
        global_endpoint='',
        region_endpoint_map={},
    ),
    'resourcecenter': ServiceEndpointInfo(
        service='resourcecenter',
        is_global=True,
        global_endpoint='',
        region_endpoint_map={},
    ),
}

bootstrap_region = {
    region_code_cn_beijing_auto_driving: {},
    region_code_ap_southeast2: {},
    region_code_ap_southeast3: {},
    region_code_cn_shanghai_auto_driving: {},
}


class DefaultEndpointProvider(EndpointProvider):

    def __init__(self, custom_endpoints=None):
        self.custom_endpoints = custom_endpoints or {}

    def get_default_endpoint(self, service, region, suffix=endpoint_suffix):
        if service in default_endpoint:
            e = default_endpoint[service]
            return e.get_endpoint_for(region, suffix)
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
            except Exception as e:
                warnings.warn(
                    'failed to read bootstrap region list from file ' + bs_region_list_path + ': ' + str(e),
                    Warning,
                    stacklevel=2
                )

        if bootstrap_region:
            if region_code in bootstrap_region:
                return True

        if custom_bootstrap_region:
            return region_code in custom_bootstrap_region

        return False

    @staticmethod
    def __has_enabled_dualstack(use_dual_stack):
        if use_dual_stack is None:
            return os.getenv("VOLC_ENABLE_DUALSTACK") == 'true'
        return use_dual_stack

    def endpoint_for(self, service, region, custom_bootstrap_region=None, use_dual_stack=None, **kwargs):
        if service in self.custom_endpoints:
            conf = self.custom_endpoints[service]
            host = conf.get_endpoint_for(region)
            return ResolvedEndpoint(host)

        if custom_bootstrap_region is None:
            custom_bootstrap_region = {}

        if not self.__in_bootstrap_region_list(region, custom_bootstrap_region):
            return ResolvedEndpoint(fallback_endpoint)

        suffix = dualstack_endpoint_suffix if self.__has_enabled_dualstack(use_dual_stack) else endpoint_suffix
        host = self.get_default_endpoint(service=service, region=region, suffix=suffix)

        return ResolvedEndpoint(host)


class HostEndpointProvider(EndpointProvider):
    def __init__(self, host):
        self.host = host

    def endpoint_for(self, service, region, **kwargs):
        return ResolvedEndpoint(self.host)
