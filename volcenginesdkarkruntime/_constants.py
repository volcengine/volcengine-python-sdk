# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import httpx

VERSION = ""
BASE_URL = "https://ark.cn-beijing.volces.com/api/v3"

RAW_RESPONSE_HEADER = "X-Stainless-Raw-Response"
CLIENT_REQUEST_HEADER = "X-Client-Request-Id"
SERVER_REQUEST_HEADER = "X-Request-Id"

# default timeout is 1 minutes
DEFAULT_TIMEOUT = httpx.Timeout(timeout=60.0, connect=60.0)
DEFAULT_MAX_RETRIES = 1
DEFAULT_CONNECTION_LIMITS = httpx.Limits(
    max_connections=1000, max_keepalive_connections=100
)

INITIAL_RETRY_DELAY = 0.5
MAX_RETRY_DELAY = 8.0
