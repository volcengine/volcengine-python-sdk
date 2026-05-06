import threading
import time
import uuid
from datetime import datetime

import dateutil.parser, dateutil.tz

from volcenginesdkcore import UniversalApi, UniversalInfo, ApiClient, Configuration
from .provider import Provider, CredentialValue

class AssumeRoleCredentials:
    def __init__(self, ak, sk, session_token, current_time, expired_time):
        self.ak = ak
        self.sk = sk
        self.session_token = session_token
        self.current_time = current_time
        self.expired_time = expired_time


class StsCredentialProvider(Provider):
    def __init__(self, ak, sk, role_name, account_id, duration_seconds=3600, scheme='https',
                 host='sts.volcengineapi.com', region='cn-beijing', timeout=30, expired_buffer_seconds=60, policy=None,
                 max_retries=3, retry_interval=1):
        self.ak = ak
        self.sk = sk
        self.role_name = role_name
        self.account_id = account_id

        self.timeout = timeout
        self.max_retries = max(max_retries, 1)
        self.retry_interval = retry_interval
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
                self._assume_role()

    def get_credentials(self):
        self.refresh()
        return self.credentials

    def _assume_role(self):
        params = {
            'DurationSeconds': self.duration_seconds,
            'RoleSessionName': uuid.uuid4().hex,
            'RoleTrn': 'trn:iam::' + self.account_id + ':role/' + self.role_name,
        }
        if self.policy is not None:
            params['Policy'] = self.policy
        configuration = type.__call__(Configuration)
        configuration.ak = self.ak
        configuration.sk = self.sk
        configuration.host = self.host
        configuration.region = self.region
        configuration.scheme = self.scheme
        configuration.read_timeout = self.timeout

        # Retry: apply provider-level retry semantics to this STS call only.
        # Deep-copy the retryer so we don't mutate DEFAULT_RETRYER (module-level
        # singleton shared across Configurations). Configuration exposes retryer
        # via a getter-only property; swap the underlying __retryer via name
        # mangling.
        import copy
        configuration._Configuration__retryer = copy.deepcopy(configuration.retryer)
        # Provider semantics: max_retries = TOTAL attempts. Configuration
        # semantics: num_max_retries = retries AFTER the initial attempt.
        configuration.num_max_retries = max(self.max_retries - 1, 0)
        # Provider retry_interval is seconds; Configuration uses ms.
        # Collapse the exponential-backoff range to a fixed delay.
        delay_ms = int(self.retry_interval * 1000)
        configuration.min_retry_delay_ms = delay_ms
        configuration.max_retry_delay_ms = delay_ms

        c = UniversalApi(ApiClient(configuration))
        info = UniversalInfo(method='GET', service='sts', version='2018-01-01', action='AssumeRole',
                             content_type='text/plain')

        resp, status_code, resp_header = c.do_call_with_http_info(info=info, body=params)
        if 'Credentials' not in resp:
            raise RuntimeError('failed to retrieve credentials from sts' + str(resp_header))
        resp_cred = resp['Credentials']

        # Parse the ISO string
        dt = dateutil.parser.parse(resp_cred['ExpiredTime'])

        # Convert to timestamp (seconds since epoch)
        self.expired_time = (dt - datetime(1970, 1, 1, tzinfo=dateutil.tz.tzutc())).total_seconds()

        self.credentials = CredentialValue(ak=resp_cred['AccessKeyId'],
                                           sk=resp_cred['SecretAccessKey'],
                                           session_token=resp_cred['SessionToken'],
                                           provider_name='StsCredentialProvider')
