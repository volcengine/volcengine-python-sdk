# coding: utf-8
"""直接 provider 入口与标准、默认、自定义寻址的离线回归。"""
import copy
import glob
import io
import os
import re
import tempfile
import threading
import unittest

from endpoint_security_support import EndpointSecurityTestCase, INVALID_LABELS, NON_STRING_LABELS
from volcenginesdkcore.endpoint.providers import default_provider, standard_provider
from volcenginesdkcore.endpoint.providers.default_provider import (
    DefaultEndpointProvider, HostEndpointProvider, ServiceEndpointInfo,
)
from volcenginesdkcore.endpoint.providers.standard_provider import (
    StandardEndpointResolver, ServiceInfo, StandProviderError,
)
from volcenginesdkcore.endpoint.validation import validate_region, validate_service
from volcenginesdkcore.feature.rds import connect_utils

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
_RESOURCE_PATH = re.compile(r"'/([^/']+)/([^/']+)/([^/']+)/(get|post)/[^']*'")


def builtin_services():
    """所有内置 service：两张寻址表的 key 与 service 字段、RDS 默认值、生成代码的 resource path。"""
    services = set(default_provider.default_endpoint)
    services.update(info.service for info in default_provider.default_endpoint.values())
    services.update(standard_provider.ServiceInfos)
    services.update(info.service for info in standard_provider.ServiceInfos.values())
    services.add(connect_utils.DEFAULT_SERVICE)
    services.update(generated_services())
    return services


def generated_services():
    services = set()
    for path in glob.glob(os.path.join(REPO_ROOT, 'volcenginesdk*', 'api', '*.py')):
        with io.open(path, encoding='utf-8') as source:
            services.update(m.group(3) for m in _RESOURCE_PATH.finditer(source.read()))
    return services


def builtin_regions():
    regions = set(default_provider.bootstrap_region)
    regions.update(getattr(default_provider, name) for name in dir(default_provider)
                   if name.startswith('region_code_'))
    regions.update(standard_provider.region_matcher.white_regions)
    for info in default_provider.default_endpoint.values():
        regions.update(info.region_endpoint_map)
    return regions


class EndpointProviderSecurityTest(EndpointSecurityTestCase):
    def test_builtin_services_and_regions_pass_validation(self):
        services, regions = builtin_services(), builtin_regions()
        # 生成代码目录缺失时宁可失败，也不让兜底测试空转。
        self.assertGreater(len(generated_services()), 100)
        self.assertGreaterEqual(len(services), 140)
        self.assertGreaterEqual(len(regions), 52)
        for service in sorted(services):
            validate_service(service)
        for region in sorted(regions):
            validate_region(region)

    def test_builtin_hosts_unchanged_for_valid_values(self):
        # 合法值的解析结果与改动前的拼接公式逐一相同。
        provider = DefaultEndpointProvider()
        bootstrap = sorted(default_provider.bootstrap_region)
        for service, info in sorted(default_provider.default_endpoint.items()):
            code = info.service.lower().replace('_', '-')
            for region in bootstrap:
                for dual, suffix in [(False, '.volcengineapi.com'), (True, '.volcengine-api.com')]:
                    if info.is_global:
                        expected = info.global_endpoint or code + suffix
                    else:
                        expected = info.region_endpoint_map.get(region) or code + '.' + region + suffix
                    self.assertEqual(expected, provider.endpoint_for(service, region, use_dual_stack=dual).host)
            self.assertEqual('open.volcengineapi.com', provider.endpoint_for(service, 'cn-beijing').host)
        resolver = StandardEndpointResolver()
        for service, info in sorted(standard_provider.ServiceInfos.items()):
            code = service.lower().replace('_', '-')
            for region in sorted(standard_provider.region_matcher.white_regions):
                for dual, stack in [(False, 'volcengineapi'), (True, 'volcengine-api')]:
                    middle = '' if info.IsGlobal else '.' + region
                    self.assertEqual(code + middle + '.' + stack + '.com',
                                     resolver.endpoint_for(service, region, use_dual_stack=dual).host)

    def test_default_fallback_and_bootstrap_compatibility(self):
        provider = DefaultEndpointProvider()
        for service in ['ecs', 'billing', 'unknown', '']:
            self.assertEqual('open.volcengineapi.com', provider.endpoint_for(service, 'cn-beijing').host)
        self.assertEqual('open.volcengineapi.com', provider.endpoint_for('ecs', '').host)
        self.assertEqual('ecs.ap-southeast-2.volcengineapi.com',
                         provider.endpoint_for('ecs', 'ap-southeast-2').host)
        self.assertEqual('ecs.cn-beijing.volcengineapi.com',
                         provider.endpoint_for('ecs', 'cn-beijing', custom_bootstrap_region={'cn-beijing': {}}).host)
        self.assertEqual('billing.volcengineapi.com', provider.get_default_endpoint('billing', 'cn-beijing'))
        self.assertEqual('open.volcengineapi.com', provider.get_default_endpoint('unknown', 'cn-beijing'))

    def test_dualstack_explicit_and_environment(self):
        provider = DefaultEndpointProvider()
        os.environ['VOLC_ENABLE_DUALSTACK'] = 'true'
        self.assertEqual('ecs.ap-southeast-2.volcengine-api.com',
                         provider.endpoint_for('ecs', 'ap-southeast-2').host)
        self.assertEqual('ecs.ap-southeast-2.volcengineapi.com',
                         provider.endpoint_for('ecs', 'ap-southeast-2', use_dual_stack=False).host)
        self.assertEqual('ecs.ap-southeast-2.volcengine-api.com',
                         provider.endpoint_for('ecs', 'ap-southeast-2', use_dual_stack=True).host)

    def test_environment_bootstrap_file(self):
        provider = DefaultEndpointProvider()
        bad = 'cn-beijing@127.0.0.1/'
        # 先关闭文件再交给被测代码读取：Windows 上已打开的 NamedTemporaryFile 不能被再次打开。
        fd, path = tempfile.mkstemp(suffix='.conf')
        self.addCleanup(os.remove, path)
        with os.fdopen(fd, 'w') as config:
            config.write('cn-beijing\n' + bad + '\n')
        os.environ['VOLC_BOOTSTRAP_REGION_LIST_CONF'] = path
        self.assertEqual('ecs.cn-beijing.volcengineapi.com', provider.endpoint_for('ecs', 'cn-beijing').host)
        self.assert_rejected('InvalidRegion', provider.endpoint_for, 'ecs', bad)

    def test_service_info_all_compatible_branches(self):
        info = ServiceEndpointInfo('Cloud_Detect', False, '', {'cn-beijing': 'private.internal'})
        self.assertEqual('private.internal', info.get_endpoint_for('cn-beijing'))
        self.assertEqual('cloud-detect.CN_Beijing-2.volcengineapi.com', info.get_endpoint_for('CN_Beijing-2'))
        self.assertEqual('cloud-detect.cn-shanghai.internal', info.get_endpoint_for('cn-shanghai', '.internal'))
        self.assertEqual('cloud-detect.volcengineapi.com',
                         ServiceEndpointInfo('Cloud_Detect', True, '', {}).get_endpoint_for('cn-beijing'))
        self.assertEqual('fixed.internal',
                         ServiceEndpointInfo('ecs', True, 'fixed.internal', {}).get_endpoint_for('cn-beijing'))
        provider = DefaultEndpointProvider({'custom': info})
        self.assertEqual('private.internal', provider.endpoint_for('custom', 'cn-beijing').host)
        self.assertEqual('cloud-detect.cn-shanghai.volcengineapi.com',
                         provider.endpoint_for('custom', 'cn-shanghai').host)

    def test_custom_service_info_cannot_hide_invalid_service(self):
        info = ServiceEndpointInfo('ecs@127.0.0.1/', False, '', {})
        self.assert_rejected('InvalidService', DefaultEndpointProvider({'ecs': info}).endpoint_for,
                             'ecs', 'cn-beijing')

    def test_fixed_host_ignores_nonparticipating_inputs(self):
        for host in ['private.internal', '127.0.0.1:8080', 'localhost']:
            provider = HostEndpointProvider(host)
            for _, value in INVALID_LABELS + NON_STRING_LABELS:
                self.assertEqual(host, provider.endpoint_for(value, value).host)

    def test_standard_compatibility_and_business_errors(self):
        malicious = 'ecs@127.0.0.1/'
        custom = StandardEndpointResolver(custom_services={malicious: ServiceInfo(malicious, False)})
        self.assert_rejected('InvalidService', custom.endpoint_for, malicious, 'cn-beijing')
        provider = StandardEndpointResolver(custom_services={'Cloud_Detect': ServiceInfo('Cloud_Detect', False)})
        self.assertEqual('ecs.cn-beijing.volcengineapi.com', provider.endpoint_for('ecs', 'cn-beijing').host)
        self.assertEqual('billing.volcengineapi.com', provider.endpoint_for('billing', 'cn-beijing').host)
        self.assertEqual('cloud-detect.cn-beijing.volcengine-api.com',
                         provider.endpoint_for('Cloud_Detect', 'cn-beijing', use_dual_stack=True).host)
        for service, region, code in [('ecs', '', 'InvalidRegion'), ('missing', 'cn-beijing', 'ServiceNotFound')]:
            with self.assertRaises(StandProviderError) as caught:
                provider.endpoint_for(service, region)
            self.assertEqual(code, caught.exception.code)

    def test_standard_custom_format_and_internal_domain(self):
        provider = StandardEndpointResolver(fmt='{Service}{Region}.{Extension[domain]}',
                                            extension={'domain': 'private.internal'})
        self.assertEqual('ecs.cn-beijing.private.internal', provider.endpoint_for('ecs', 'cn-beijing').host)
        provider = StandardEndpointResolver(fmt='{Missing}')
        with self.assertRaises(StandProviderError) as caught:
            provider.endpoint_for('ecs', 'cn-beijing')
        self.assertEqual('TemplateExecuteError', caught.exception.code)

    def test_standard_failure_preserves_variables_then_success(self):
        provider = StandardEndpointResolver()
        provider.endpoint_for('ecs', 'cn-beijing')
        before = copy.deepcopy(provider.variables.to_dict())
        for _, value in INVALID_LABELS:
            self.assert_rejected('InvalidRegion', provider.endpoint_for, 'billing', value)
            self.assert_rejected('InvalidService', provider.endpoint_for, value, 'cn-beijing')
            self.assertEqual(before, provider.variables.to_dict())
        self.assertEqual('billing.volcengine-api.com',
                         provider.endpoint_for('billing', 'cn-shanghai', use_dual_stack=True).host)

    def test_shared_resolver_two_threads_invalid_does_not_pollute_valid(self):
        provider = StandardEndpointResolver()
        start = threading.Event()
        failures = []
        completed = []

        def run_invalid():
            start.wait(5)
            try:
                for _ in range(100):
                    self.assert_rejected('InvalidRegion', provider.endpoint_for, 'billing', 'cn-beijing\n')
                completed.append('invalid')
            except BaseException as error:
                failures.append(error)

        def run_valid():
            start.wait(5)
            try:
                for _ in range(100):
                    self.assertEqual('ecs.cn-beijing.volcengineapi.com',
                                     provider.endpoint_for('ecs', 'cn-beijing').host)
                completed.append('valid')
            except BaseException as error:
                failures.append(error)

        threads = [threading.Thread(target=run_invalid), threading.Thread(target=run_valid)]
        for thread in threads:
            thread.daemon = True
            thread.start()
        start.set()
        for thread in threads:
            thread.join(10)
            self.assertFalse(thread.is_alive())
        self.assertEqual([], failures)
        self.assertEqual(['invalid', 'valid'], sorted(completed))


def _provider_invalid_test(entry, field, value):
    def test(self):
        service = value if field == 'service' else 'ecs'
        region = value if field == 'region' else 'cn-beijing'
        if entry == 'default':
            fn = DefaultEndpointProvider().endpoint_for
        elif entry == 'default_direct':
            fn = DefaultEndpointProvider().get_default_endpoint
        elif entry == 'custom_bootstrap':
            def fn(service, region):
                return DefaultEndpointProvider().endpoint_for(service, region, custom_bootstrap_region=[region])
        elif entry == 'custom_endpoint':
            def fn(service, region):
                custom = {'ecs': ServiceEndpointInfo('ecs', False, '', {})}
                return DefaultEndpointProvider(custom).endpoint_for(service, region)
        elif entry == 'service_info':
            def fn(service, region):
                return ServiceEndpointInfo(service, False, '', {}).get_endpoint_for(region)
        else:
            fn = StandardEndpointResolver().endpoint_for
        self.assert_rejected('InvalidService' if field == 'service' else 'InvalidRegion', fn, service, region)
    return test


for _entry in ['default', 'default_direct', 'custom_bootstrap', 'custom_endpoint', 'service_info', 'standard']:
    for _field in ['service', 'region']:
        for _name, _value in INVALID_LABELS + NON_STRING_LABELS:
            setattr(EndpointProviderSecurityTest, 'test_%s_%s_rejects_%s' % (_entry, _field, _name),
                    _provider_invalid_test(_entry, _field, _value))


if __name__ == '__main__':
    unittest.main()
