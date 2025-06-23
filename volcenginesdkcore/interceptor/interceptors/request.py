class RuntimeOption(object):
    def __init__(self, client_side_validation, ak=None, sk=None, session_token=None, region=None, scheme=None,
                 endpoint_provider=None, connect_timeout=None, read_timeout=None, auto_retry=None, num_max_retries=None,
                 backoff_strategy=None, retry_condition=None,
                 retry_error_codes=None, min_retry_delay_ms=None, max_retry_delay_ms=None):
        self.ak = ak
        self.sk = sk
        self.session_token = session_token
        self.region = region
        self.scheme = scheme
        self.endpoint_provider = endpoint_provider
        self.connect_timeout = connect_timeout
        self.read_timeout = read_timeout
        self.client_side_validation = client_side_validation
        self.auto_retry = auto_retry
        self.num_max_retries = num_max_retries
        self.backoff_strategy = backoff_strategy
        self.retry_condition = retry_condition
        self.retry_error_codes = retry_error_codes
        self.min_retry_delay_ms = min_retry_delay_ms
        self.max_retry_delay_ms = max_retry_delay_ms


class Request(object):
    def __init__(
            self, configuration, resource_path, method, path_params=None,
            query_params=None, header_params=None, body=None, post_params=None,
            files=None, response_type=None, auth_settings=None,
            _return_http_data_only=None, collection_formats=None,
            _preload_content=True, _request_timeout=None):
        self.resource_path = resource_path
        self.method = method
        self.path_params = path_params
        self.query_params = query_params
        self.header_params = header_params
        self.body = body
        self.post_params = post_params
        self.files = files
        self.response_type = response_type
        self.auth_settings = auth_settings
        self._return_http_data_only = _return_http_data_only
        self.collection_formats = collection_formats
        self.preload_content = _preload_content
        self.request_timeout = _request_timeout
        self.host = configuration.host

        self.url = ''
        self.true_path = '/'
        self.service = ''
        self.md = ''

        self.ak = configuration.ak
        self.sk = configuration.sk
        self.session_token = configuration.session_token
        self.region = configuration.region
        self.scheme = configuration.scheme
        self.endpoint_provider = configuration.endpoint_provider
        self.custom_bootstrap_region = configuration.custom_bootstrap_region
        self.use_dual_stack = configuration.use_dual_stack

        # retryer setting, default use global configration if value not set
        self.auto_retry = configuration.auto_retry
        self.retryer = configuration.retryer

        self.runtime_options = None
        if hasattr(body, '_configuration') and isinstance(body._configuration, RuntimeOption):
            self.runtime_options = body._configuration
