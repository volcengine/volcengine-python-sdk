# coding: utf-8
"""真实 SDK 调用链 + 本地传输桩：非法 region/service 在签名和发送之前失败。"""
import glob
import io
import os
import re
import threading
import unittest
from multiprocessing.pool import ThreadPool

from six.moves.urllib.parse import parse_qs, urlsplit

import volcenginesdkbilling
import volcenginesdkecs
from volcenginesdkcore import ApiClient, rest
from volcenginesdkcore.endpoint.endpoint_provider import ResolvedEndpoint
from volcenginesdkcore.endpoint.providers import default_provider
from volcenginesdkcore.endpoint.providers.default_provider import (
    DefaultEndpointProvider, HostEndpointProvider, ServiceEndpointInfo,
)
from volcenginesdkcore.endpoint.providers.standard_provider import StandardEndpointResolver
from volcenginesdkcore.feature.rds import build_auth_token
from volcenginesdkcore.interceptor import InterceptorContext
from volcenginesdkcore.interceptor.interceptors.request import RuntimeOption
from volcenginesdkcore.signv4 import SignerV4
from volcenginesdkcore.universal import UniversalApi, UniversalInfo
from endpoint_security_support import (
    EndpointSecurityTestCase, INVALID_LABELS, NON_STRING_LABELS, VALID_LABELS, expected_message,
)

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SIGNATURE_HEADERS = ('Authorization', 'X-Date', 'X-Content-Sha256', 'X-Security-Token')
ECS_PATH = '/DescribeInstances/2020-04-01/ecs/get/text_plain/'


class PlaceholderCredentials(object):
    ak = 'placeholder-ak'
    sk = 'placeholder-sk'
    session_token = 'placeholder-session'


class CountingCredentialProvider(object):
    def __init__(self):
        self.calls = 0

    def get_credentials(self):
        self.calls += 1
        return PlaceholderCredentials()


class CountingResolver(object):
    def __init__(self):
        self.calls = []

    def endpoint_for(self, service, region, **kwargs):
        self.calls.append((service, region))
        return ResolvedEndpoint('custom.internal')


class FakeUrllib3Response(object):
    status = 200
    reason = 'local stub'
    data = '{"ResponseMetadata":{"RequestId":"placeholder-request"},"Result":{}}'
    headers = {}


class EndpointClientSecurityTest(EndpointSecurityTestCase):
    def setUp(self):
        super(EndpointClientSecurityTest, self).setUp()
        self.sign_calls = []
        self.presign_calls = []
        self.sent = []
        self.credential_http = []
        self.default_credential_calls = []
        original_sign = SignerV4.sign
        original_presign = SignerV4.sign_url

        def sign(*args, **kwargs):
            self.sign_calls.append(True)
            return original_sign(*args, **kwargs)

        def presign(*args, **kwargs):
            self.presign_calls.append(True)
            return original_presign(*args, **kwargs)

        # 传输桩放在 SDK 最底层的 RESTClientObject.request，计数即真实发送次数。
        def transport(rest_client, method, url, **kwargs):
            self.sent.append({'url': url, 'method': method, 'headers': dict(kwargs.get('headers') or {}),
                              'query': kwargs.get('query_params')})
            return rest.RESTResponse(FakeUrllib3Response())

        def credential_http(*args, **kwargs):
            self.credential_http.append(True)
            raise AssertionError('禁止凭证 HTTP 请求')

        from volcenginesdkcore.auth.providers.default_provider import DefaultCredentialProvider

        def default_credentials(*args, **kwargs):
            self.default_credential_calls.append(True)
            raise AssertionError('非法输入不应获取默认凭证')

        self.replace(SignerV4, 'sign', staticmethod(sign))
        self.replace(SignerV4, 'sign_url', staticmethod(presign))
        self.replace(rest.RESTClientObject, 'request', transport)
        self.replace(ApiClient, '_do_http_request', credential_http)
        self.replace(DefaultCredentialProvider, 'get_credentials', default_credentials)

    # ---------------------------------------------------------------- helpers
    def client(self, conf=None):
        return ApiClient(conf if conf is not None else self.configuration())

    def call(self, client, service='ecs', async_req=False):
        info = UniversalInfo(method='GET', service=service, version='2020-04-01', action='DescribeInstances')
        return UniversalApi(client).do_call(info, {}, async_req=async_req)

    def generated_call(self, client, kind='ecs', option=None, async_req=False):
        if kind == 'billing':
            return volcenginesdkbilling.BILLINGApi(client).query_balance_acct(
                volcenginesdkbilling.QueryBalanceAcctRequest(_configuration=option), async_req=async_req)
        return volcenginesdkecs.ECSApi(client).describe_instances(
            volcenginesdkecs.DescribeInstancesRequest(_configuration=option), async_req=async_req)

    def run_pipeline(self, client, resource_path=ECS_PATH, method='GET'):
        """直接执行内部请求流水线（解析 endpoint + 签名），传入构造好的请求对象。"""
        headers = {'Content-Type': 'text/plain' if method == 'GET' else 'application/json'}
        request = client._create_request(resource_path, method, {}, [], headers, {}, [], {}, object,
                                         ['volcengineSign'])
        request.auto_retry = False
        request.retryer = client._base_retryer
        context = InterceptorContext(request=request)
        error = None
        try:
            client.interceptor_chain.execute_request(context)
        except Exception as caught:
            error = caught
        return request, error

    def assert_no_side_effect(self):
        self.assertEqual([], self.sign_calls)
        self.assertEqual([], self.presign_calls)
        self.assertEqual([], self.sent)
        self.assertEqual([], self.credential_http)
        self.assertEqual([], self.default_credential_calls)
        self.assertEqual([], self.network_attempts)

    # ---------------------------------------------------- signing is not run
    def test_invalid_region_request_object_is_not_signed(self):
        for value in [u'cn-beijing@127.0.0.1', u'1cn', u'cn-beijing-']:
            request, error = self.run_pipeline(self.client(self.configuration(value)))
            self.assertEqual('InvalidRegion', getattr(error, 'code', None))
            for header in SIGNATURE_HEADERS:
                self.assertNotIn(header, request.header_params)
            self.assertNotIn('Host', request.header_params)
            self.assertEqual('', request.url)
            self.assertFalse(request.host)
        self.assert_no_side_effect()

    def test_valid_region_request_object_is_signed(self):
        request, error = self.run_pipeline(self.client(self.configuration('ap-southeast-2')))
        self.assertIsNone(error)
        self.assertIn('Authorization', request.header_params)
        self.assertIn('X-Date', request.header_params)
        self.assertIn('/ap-southeast-2/ecs/request', request.header_params['Authorization'])
        self.assertEqual('ecs.ap-southeast-2.volcengineapi.com', request.header_params['Host'])
        self.assertEqual('https://ecs.ap-southeast-2.volcengineapi.com/', request.url)
        self.assertEqual(1, len(self.sign_calls))
        self.assertEqual([], self.sent)

    # ------------------------------------------------ end to end, both paths
    def test_generated_and_universal_valid_requests_are_sent_and_signed(self):
        client = self.client()
        self.generated_call(client, 'ecs')
        self.generated_call(client, 'billing')
        self.call(client, 'ecs')
        self.assertEqual(3, len(self.sent))
        self.assertEqual(['https://open.volcengineapi.com/'] * 3, [r['url'] for r in self.sent])
        for sent in self.sent:
            self.assertIn('Authorization', sent['headers'])
            self.assertIn('X-Date', sent['headers'])
        self.assertEqual(3, len(self.sign_calls))

    def test_universal_error_message_and_code(self):
        error = self.assert_rejected('InvalidService', self.call, self.client(), u'evil.com#')
        self.assertEqual(expected_message('service', u'"evil.com#"', u'illegal character at index 4'),
                         error.message)
        error = self.assert_rejected('InvalidRegion', self.call, self.client(self.configuration(u'cn-beijing-')))
        self.assertEqual(expected_message('region', u'"cn-beijing-"', u"must not end with '-' or '_'"),
                         error.message)
        self.assert_no_side_effect()

    def test_construction_never_fails_with_invalid_region(self):
        for _, value in INVALID_LABELS + NON_STRING_LABELS:
            conf = self.configuration(value)
            provider = CountingCredentialProvider()
            conf.credential_provider = provider
            client = self.client(conf)
            UniversalApi(client)
            volcenginesdkbilling.BILLINGApi(client)
            volcenginesdkecs.ECSApi(client)
            self.assertIsNone(client._pool)
            self.assertEqual(0, provider.calls)
        self.assert_no_side_effect()

    def test_invalid_region_never_initializes_default_credentials(self):
        conf = self.configuration(u'cn-beijing@127.0.0.1')
        conf.ak = conf.sk = ''
        client = self.client(conf)
        self.assert_rejected('InvalidRegion', self.call, client)
        self.assert_rejected('InvalidRegion', self.generated_call, client)
        self.assertFalse(hasattr(client.sign_request_interceptor, '_default_credential_provider'))
        self.assert_no_side_effect()

    # ---------------------------------------------------- deferred failures
    def test_set_invalid_after_construction_then_recover(self):
        conf = self.configuration()
        client = self.client(conf)
        api = volcenginesdkecs.ECSApi(client)
        self.generated_call(client)
        self.assertEqual(1, len(self.sent))
        for value in [u'cn-beijing@127.0.0.1', u'1cn-beijing', u'rds_mysql_']:
            conf.region = value
            self.assert_rejected('InvalidRegion', api.describe_instances, volcenginesdkecs.DescribeInstancesRequest())
            self.assert_rejected('InvalidRegion', self.call, client)
        self.assertEqual(1, len(self.sent))
        self.assertEqual(1, len(self.sign_calls))
        conf.region = 'ap-southeast-2'
        self.generated_call(client)
        self.call(client)
        self.assertEqual(['https://open.volcengineapi.com/', 'https://ecs.ap-southeast-2.volcengineapi.com/',
                          'https://ecs.ap-southeast-2.volcengineapi.com/'], [r['url'] for r in self.sent])

    def test_runtime_option_region_and_provider_overrides(self):
        conf = self.configuration()
        conf.host = 'fixed.internal'
        client = self.client(conf)
        resolver = CountingResolver()
        invalid = RuntimeOption(False, region=u'cn-beijing\n', endpoint_provider=resolver)
        self.assert_rejected('InvalidRegion', self.generated_call, client, 'ecs', invalid)
        self.assertEqual([], resolver.calls)
        self.assert_no_side_effect()
        valid = RuntimeOption(False, region='cn-shanghai', endpoint_provider=resolver)
        self.generated_call(client, 'ecs', valid)
        self.assertEqual([('ecs', 'cn-shanghai')], resolver.calls)
        self.assertEqual('https://custom.internal/', self.sent[-1]['url'])
        fixed = RuntimeOption(False, region=u'cn-beijing@127.0.0.1',
                              endpoint_provider=HostEndpointProvider('override.internal'))
        self.generated_call(client, 'billing', fixed)
        self.assertEqual('https://override.internal/', self.sent[-1]['url'])
        self.assertEqual('fixed.internal', conf.host)
        self.assertEqual('cn-beijing', conf.region)

    def test_async_rejects_then_recovers(self):
        client = self.client()
        pool = ThreadPool(processes=1)
        client._pool = pool
        try:
            pending = self.generated_call(client, 'ecs', RuntimeOption(False, region=u'cn-beijing\n'), True)
            self.assert_rejected('InvalidRegion', pending.get, 10)
            self.assert_no_side_effect()
            pending = self.generated_call(client, 'ecs', None, True)
            self.assertIsInstance(pending.get(10), volcenginesdkecs.DescribeInstancesResponse)
            self.assertEqual(1, len(self.sent))
        finally:
            pool.close()
            pool.join()
            client._pool = None

    # ----------------------------------------------------- resolver entries
    def test_custom_resolver_is_never_called_for_invalid_input(self):
        class FailingResolver(object):
            def endpoint_for(inner, service, region, **kwargs):
                self.fail('自定义解析器不应收到非法输入: %r %r' % (service, region))

        for field in ['region', 'service']:
            for _, value in INVALID_LABELS + NON_STRING_LABELS:
                conf = self.configuration(value if field == 'region' else 'cn-beijing')
                provider = CountingCredentialProvider()
                conf.endpoint_provider = FailingResolver()
                conf.credential_provider = provider
                client = self.client(conf)
                code = 'InvalidRegion' if field == 'region' else 'InvalidService'
                self.assert_rejected(code, self.call, client, value if field == 'service' else 'ecs')
                if field == 'region':
                    self.assert_rejected(code, self.generated_call, client)
                    request, error = self.run_pipeline(client)
                    self.assertEqual(code, error.code)
                self.assertEqual(0, provider.calls)
        self.assert_no_side_effect()

    def test_valid_custom_resolver(self):
        conf = self.configuration()
        resolver = CountingResolver()
        conf.endpoint_provider = resolver
        client = self.client(conf)
        self.call(client)
        self.assertEqual([('ecs', 'cn-beijing')], resolver.calls)
        self.assertEqual('https://custom.internal/', self.sent[-1]['url'])
        self.assertIn('Authorization', self.sent[-1]['headers'])

    def test_unknown_service_custom_endpoint_is_rejected(self):
        # Python 中与 Go ResolveUnknownService 等价的入口：按名字拼接的自定义服务。
        for provider in [DefaultEndpointProvider({u'evil.com#': ServiceEndpointInfo(u'evil.com#', False, '', {})}),
                         StandardEndpointResolver()]:
            conf = self.configuration()
            conf.endpoint_provider = provider
            self.assert_rejected('InvalidService', self.call, self.client(conf), u'evil.com#')
        self.assert_no_side_effect()

    def test_host_provider_subclass_cannot_bypass_validation(self):
        class DynamicHostProvider(HostEndpointProvider):
            def endpoint_for(inner, service, region, **kwargs):
                self.fail('可重写的动态 resolver 不得收到非法输入')
        conf = self.configuration(u'cn-beijing@127.0.0.1')
        conf.endpoint_provider = DynamicHostProvider('unused.internal')
        self.assert_rejected('InvalidRegion', self.call, self.client(conf))
        self.assert_no_side_effect()

    # ----------------------------------------------------- explicit endpoint
    def test_explicit_host_is_kept_and_not_validated(self):
        for host in ['private.internal', 'http://localhost:8080', 'https://service.internal:9443']:
            conf = self.configuration(u'cn-beijing@127.0.0.1')
            conf.host = host
            client = self.client(conf)
            self.call(client, 'ecs')
            self.generated_call(client)
            expected = host if '://' in host else 'https://' + host
            for sent in self.sent[-2:]:
                self.assertEqual(expected + '/', sent['url'])
                self.assertEqual(urlsplit(expected).netloc, sent['headers']['Host'])
        self.assertEqual(6, len(self.sign_calls))
        self.assertEqual([], self.network_attempts)

    def test_fixed_host_provider_is_explicit_endpoint(self):
        conf = self.configuration(u'cn-beijing@127.0.0.1')
        conf.endpoint_provider = HostEndpointProvider('private.internal:8080')
        self.call(self.client(conf), 'ecs')
        self.assertEqual('https://private.internal:8080/', self.sent[-1]['url'])
        self.assertEqual(1, len(self.sign_calls))

    # ------------------------------------------------------------- presign
    def test_rds_presign_rejects_without_signed_url(self):
        for _, value in INVALID_LABELS + NON_STRING_LABELS:
            conf = self.configuration(value)
            provider = CountingCredentialProvider()
            conf.credential_provider = provider
            client = self.client(conf)
            token = None
            if value is False or value == [] or value == {}:
                # 空值沿用原有的 "region must not be empty" 处理。
                with self.assertRaises(ValueError):
                    token = build_auth_token(client, 'placeholder-db-user', 'placeholder-instance')
            else:
                error = self.assert_rejected('InvalidRegion', build_auth_token, client,
                                             'placeholder-db-user', 'placeholder-instance')
                self.assertTrue(error.message.startswith(u'invalid region '))
            self.assertIsNone(token)
            self.assertEqual(0, provider.calls)
        self.assert_no_side_effect()

    def test_rds_presign_fails_before_building_request(self):
        created = []
        original = ApiClient._create_request

        def create_request(client, *args, **kwargs):
            created.append(args)
            return original(client, *args, **kwargs)

        self.replace(ApiClient, '_create_request', create_request)
        client = self.client(self.configuration(u'cn-beijing@127.0.0.1'))
        error = self.assert_rejected('InvalidRegion', build_auth_token, client, 'u', 'i')
        self.assertEqual(expected_message('region', u'"cn-beijing@127.0.0.1"', u'illegal character at index 10'),
                         error.message)
        self.assertEqual([], created)
        self.assert_no_side_effect()
        build_auth_token(self.client(), 'u', 'i')
        self.assertEqual(1, len(created))

    def test_rds_presign_deferred_then_recover(self):
        conf = self.configuration()
        client = self.client(conf)
        conf.region = u'cn-beijing@127.0.0.1'
        self.assert_rejected('InvalidRegion', build_auth_token, client, 'u', 'i')
        self.assertEqual([], self.presign_calls)
        conf.region = 'cn-beijing'
        token = build_auth_token(client, 'u', 'i')
        self.assertEqual(['https://rds-mysql.cn-beijing.volcengineapi.com'], parse_qs(token)['X-HOST'])
        self.assertEqual(1, len(self.presign_calls))

    def test_rds_presign_success_and_explicit_host(self):
        for host, region in [(None, 'cn-beijing'), ('db.private.internal', u'cn-beijing@127.0.0.1')]:
            conf = self.configuration(region)
            conf.host = host
            client = self.client(conf)
            token = build_auth_token(client, 'placeholder-db-user', 'placeholder-instance', 600)
            query = parse_qs(token, keep_blank_values=True)
            self.assertEqual(['https://' + (host or 'rds-mysql.cn-beijing.volcengineapi.com')], query['X-HOST'])
            self.assertEqual(['placeholder-db-user'], query['DBUser'])
            self.assertEqual(['600'], query['X-Expires'])
            self.assertEqual(64, len(query['X-Signature'][0]))
            self.assertEqual(host, conf.host)
        self.assertEqual(2, len(self.presign_calls))
        self.assertEqual([], self.sent)

    # ------------------------------------------------- built-in fallbacks
    def test_every_generated_service_resolves_to_original_host(self):
        pattern = re.compile(r"'(/[^/']+/[^/']+/([^/']+)/(get|post)/[^']*)'")
        paths = {}
        for path in glob.glob(os.path.join(REPO_ROOT, 'volcenginesdk*', 'api', '*.py')):
            with io.open(path, encoding='utf-8') as source:
                for match in pattern.finditer(source.read()):
                    paths.setdefault(match.group(2), (match.group(1), match.group(3).upper()))
        self.assertGreater(len(paths), 100)
        resolver = DefaultEndpointProvider()
        for region in ['cn-beijing'] + sorted(default_provider.bootstrap_region):
            client = self.client(self.configuration(region))
            for service, (resource_path, method) in sorted(paths.items()):
                request, error = self.run_pipeline(client, resource_path, method)
                self.assertIsNone(error, '%s %s: %r' % (service, region, error))
                self.assertEqual(resolver.endpoint_for(service, region, use_dual_stack=False).host, request.host)
                self.assertIn('Authorization', request.header_params)
        self.assertEqual([], self.sent)

    def test_valid_labels_accepted_end_to_end(self):
        for value in VALID_LABELS:
            conf = self.configuration(value)
            conf.endpoint_provider = CountingResolver()
            self.call(self.client(conf), value or 'ecs')
        self.assertEqual(len(VALID_LABELS), len(self.sent))

    def test_two_threads_shared_configuration_failure_isolation(self):
        conf = self.configuration()
        conf.endpoint_provider = StandardEndpointResolver()
        bad_client, good_client = self.client(conf), self.client(conf)
        start = threading.Event()
        results, errors = [], []

        def invalid():
            start.wait(5)
            try:
                for _ in range(20):
                    self.assert_rejected('InvalidRegion', self.generated_call, bad_client, 'billing',
                                         RuntimeOption(False, region=u'cn-beijing\n'))
                results.append('rejected')
            except BaseException as error:
                errors.append(error)

        def valid():
            start.wait(5)
            try:
                for _ in range(20):
                    self.generated_call(good_client, 'ecs')
                results.append('accepted')
            except BaseException as error:
                errors.append(error)

        threads = [threading.Thread(target=invalid), threading.Thread(target=valid)]
        for thread in threads:
            thread.daemon = True
            thread.start()
        start.set()
        for thread in threads:
            thread.join(10)
            self.assertFalse(thread.is_alive())
        self.assertEqual([], errors)
        self.assertEqual(['accepted', 'rejected'], sorted(results))
        self.assertEqual({'https://ecs.cn-beijing.volcengineapi.com/'}, set(r['url'] for r in self.sent))
        self.assertEqual(20, len(self.sign_calls))


def _generated_rejection(kind, value):
    def test(self):
        conf = self.configuration(value)
        conf.client_side_validation = False
        provider = CountingCredentialProvider()
        conf.credential_provider = provider
        self.assert_rejected('InvalidRegion', self.generated_call, self.client(conf), kind)
        self.assertEqual(0, provider.calls)
        self.assert_no_side_effect()
    return test


def _universal_rejection(field, value):
    def test(self):
        conf = self.configuration(value if field == 'region' else 'cn-beijing')
        conf.client_side_validation = False
        code = 'InvalidRegion' if field == 'region' else 'InvalidService'
        self.assert_rejected(code, self.call, self.client(conf), value if field == 'service' else 'ecs')
        self.assert_no_side_effect()
    return test


for _name, _value in INVALID_LABELS + NON_STRING_LABELS:
    for _kind in ['billing', 'ecs']:
        setattr(EndpointClientSecurityTest, 'test_generated_%s_region_rejects_%s' % (_kind, _name),
                _generated_rejection(_kind, _value))
    for _field in ['region', 'service']:
        setattr(EndpointClientSecurityTest, 'test_universal_%s_rejects_%s' % (_field, _name),
                _universal_rejection(_field, _value))


if __name__ == '__main__':
    unittest.main()
