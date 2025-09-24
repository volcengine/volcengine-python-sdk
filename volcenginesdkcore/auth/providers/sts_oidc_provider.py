import threading
import time
import uuid
from datetime import datetime

import dateutil.parser

from volcenginesdkcore import UniversalApi, UniversalInfo, ApiClient, Configuration
from .provider import Provider, CredentialValue


class AssumeRoleOidcCredentials:
    def __init__(self, ak, sk, session_token, current_time, expired_time):
        self.ak = ak
        self.sk = sk
        self.session_token = session_token
        self.current_time = current_time
        self.expired_time = expired_time


class StsOidcCredentialProvider(Provider):
    def __init__(self, role_name, account_id, oidc_token, duration_seconds=3600, scheme='https',
                 host='sts.volcengineapi.com', region='cn-beijing', timeout=30, expired_buffer_seconds=60, policy=None):

        self.role_name = role_name
        self.account_id = account_id
        self.oidc_token = oidc_token

        self.timeout = timeout
        self.duration_seconds = duration_seconds

        self.host = host
        self.region = region
        self.scheme = scheme
        self.policy = policy
        self.expired_time = None
        if expired_buffer_seconds > 600:
            raise ValueError('expired_buffer_seconds must be less than or equal to 600')
        self.expired_buffer_seconds = expired_buffer_seconds

        self.credentials = None

        self._lock = threading.Lock()

    def retrieve(self):
        return self.credentials

    def is_expired(self):
        return (self.credentials is None or
                (self.expired_time and self.expired_time < time.time() + self.expired_buffer_seconds))

    def refresh(self):
        with self._lock:
            if self.is_expired():
                self._assume_role_oidc()

    def get_credentials(self):
        self.refresh()
        return self.credentials

    def _assume_role_oidc(self):
        params = {
            'DurationSeconds': self.duration_seconds,
            'RoleSessionName': uuid.uuid4().hex,
            'RoleTrn': 'trn:iam::' + self.account_id + ':role/' + self.role_name,
            'OIDCToken': self.oidc_token,
        }
        if self.policy is not None:
            params['Policy'] = self.policy
        configuration = type.__call__(Configuration)

        # configuration.ak = self.ak
        # configuration.sk = self.sk
        configuration.host = self.host
        configuration.region = self.region
        configuration.scheme = self.scheme
        configuration.read_timeout = self.timeout
        c = UniversalApi(ApiClient(configuration))
        info = UniversalInfo(method='POST', service='sts', version='2018-01-01', action='AssumeRoleWithOIDC',
                             content_type='application/x-www-form-urlencoded')

        resp, status_code, resp_header = c.do_call_with_http_info(info=info, body=params)
        if 'Credentials' not in resp:
            raise RuntimeError('failed to retrieve credentials from sts' + str(resp_header))
        resp_cred = resp['Credentials']

        # Parse the ISO string
        dt = dateutil.parser.parse(resp_cred['Expiration'])

        # Convert to timestamp (seconds since epoch)
        self.expired_time = (dt - datetime(1970, 1, 1, tzinfo=dateutil.tz.tzutc())).total_seconds()

        self.credentials = CredentialValue(ak=resp_cred['AccessKeyId'],
                                           sk=resp_cred['SecretAccessKey'],
                                           session_token=resp_cred['SessionToken'],
                                           provider_name='StsOidcCredentialProvider')
