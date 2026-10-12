# coding: utf-8
"""SSO 两个自动域名入口均拒绝非法区域，保留正常刷新和缓存流程。"""
import copy
import json
import unittest

from six.moves.urllib.parse import urlsplit, parse_qs

from endpoint_security_support import EndpointSecurityTestCase, INVALID_LABELS
from volcenginesdkcore import ApiClient
from volcenginesdkcore.auth.providers.cli_config_provider import SsoCredentialProvider


class EndpointSsoSecurityTest(EndpointSecurityTestCase):
    def setUp(self):
        super(EndpointSsoSecurityTest, self).setUp()
        self.http_calls = []

        def request(client, url, **kwargs):
            self.http_calls.append((url, kwargs))
            if '/token' in url:
                return json.dumps({'access_token': 'placeholder-new-access',
                                   'refresh_token': 'placeholder-new-refresh', 'expires_in': 3600})
            return json.dumps({'Result': {'RoleCredentials': {
                'AccessKeyId': 'placeholder-ak', 'SecretAccessKey': 'placeholder-sk',
                'SessionToken': 'placeholder-session', 'Expiration': 4102444800,
            }}})

        self.replace(ApiClient, '_do_http_request', request)

    def provider(self, region='cn-beijing', expired=False):
        provider = SsoCredentialProvider({}, 'https://placeholder.invalid', 'placeholder-session', region,
                                         'placeholder-account', 'placeholder-role', '/tmp/endpoint-ssrf-tests')
        provider._cache = {'access_token': 'placeholder-access', 'refresh_token': 'placeholder-refresh',
                           'client_id': 'placeholder-client', 'client_secret': 'placeholder-secret',
                           'expires_at': '2000-01-01T00:00:00Z' if expired else '2100-01-01T00:00:00Z'}
        return provider

    def test_oauth_success_then_portal_success(self):
        provider = self.provider(expired=True)
        credential = provider.get_credentials()
        self.assertEqual('placeholder-ak', credential.ak)
        self.assertEqual('placeholder-sk', credential.sk)
        self.assertEqual('placeholder-session', credential.session_token)
        self.assertEqual('placeholder-new-refresh', provider._cache['refresh_token'])
        self.assertEqual('https://cloudidentity-oauth.cn-beijing.volces.com/token', self.http_calls[0][0])
        self.assertEqual('POST', self.http_calls[0][1]['method'])
        self.assertFalse(self.http_calls[0][1]['retry_on_5xx'])
        self.assertEqual('refresh_token', self.http_calls[0][1]['data']['grant_type'])
        portal = urlsplit(self.http_calls[1][0])
        self.assertEqual('cloudidentity-portal.cn-beijing.volces.com', portal.netloc)
        self.assertEqual('/federation/credentials', portal.path)
        self.assertEqual({'account_id': ['placeholder-account'], 'role_name': ['placeholder-role']},
                         parse_qs(portal.query))
        self.assertEqual('placeholder-new-access', self.http_calls[1][1]['headers']['x-bd-cloudidentity-bearer-token'])
        self.assertIs(credential, provider.get_credentials())
        self.assertEqual(2, len(self.http_calls))
        self.assertEqual([], self.network_attempts)

    def test_unexpired_access_token_only_calls_portal(self):
        provider = self.provider()
        credential = provider.get_credentials()
        self.assertEqual('placeholder-ak', credential.ak)
        self.assertEqual(1, len(self.http_calls))
        self.assertEqual('cloudidentity-portal.cn-beijing.volces.com', urlsplit(self.http_calls[0][0]).netloc)

    def test_rejected_region_does_not_modify_cache_or_later_provider(self):
        for expired in [False, True]:
            provider = self.provider('cn-beijing\n', expired)
            before = copy.deepcopy(provider._cache)
            self.assert_rejected('InvalidRegion', provider.get_credentials)
            self.assertEqual(before, provider._cache)
            self.assertIsNone(provider._credentials)
            self.assertIsNone(provider._expiration)
            provider._region = 'cn-beijing'
            self.assertEqual('placeholder-ak', provider.get_credentials().ak)
        self.assertEqual('placeholder-ak', self.provider().get_credentials().ak)
        self.assertEqual(4, len(self.http_calls))


def _sso_invalid_test(entry, value):
    def test(self):
        provider = self.provider(value, expired=True)
        before = copy.deepcopy(provider._cache)
        if entry == 'oauth':
            self.assert_rejected('InvalidRegion', provider._refresh_access_token,
                                 '/tmp/endpoint-ssrf-tests/placeholder-cache')
        else:
            self.assert_rejected('InvalidRegion', provider._fetch_role_credentials, 'placeholder-access')
        self.assertEqual(before, provider._cache)
        self.assertIsNone(provider._credentials)
        self.assertIsNone(provider._expiration)
        self.assertEqual([], self.http_calls)
    return test


for _entry in ['oauth', 'portal']:
    for _name, _value in INVALID_LABELS:
        setattr(EndpointSsoSecurityTest, 'test_%s_region_rejects_%s' % (_entry, _name),
                _sso_invalid_test(_entry, _value))


if __name__ == '__main__':
    unittest.main()
