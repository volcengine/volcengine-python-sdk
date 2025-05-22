# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import httpx

VERSION = "1.0.0"
BASE_URL = "https://ark.cn-beijing.volces.com/api/v3"

RAW_RESPONSE_HEADER = "X-Stainless-Raw-Response"
CLIENT_REQUEST_HEADER = "X-Client-Request-Id"
SERVER_REQUEST_HEADER = "X-Request-Id"
ARK_E2E_ENCRYPTION_HEADER = "x-is-encrypted"

DEFAULT_TIMEOUT_SECONDS = 600.0
DEFAULT_CONNECT_TIMEOUT_SECONDS = 60.0
# default timeout is 1 minutes
DEFAULT_TIMEOUT = httpx.Timeout(
    timeout=DEFAULT_TIMEOUT_SECONDS, connect=DEFAULT_CONNECT_TIMEOUT_SECONDS
)

DEFAULT_MAX_RETRIES = 2
DEFAULT_CONNECTION_LIMITS = httpx.Limits(
    max_connections=1000, max_keepalive_connections=100
)

INITIAL_RETRY_DELAY = 0.5
MAX_RETRY_DELAY = 8.0

_DEFAULT_MANDATORY_REFRESH_TIMEOUT = 10 * 60  # 10 min
_DEFAULT_ADVISORY_REFRESH_TIMEOUT = 30 * 60  # 30 min
_DEFAULT_STS_TIMEOUT = 7 * 24 * 60 * 60  # 7 days

_DEFAULT_RESOURCE_TYPE = "endpoint"
