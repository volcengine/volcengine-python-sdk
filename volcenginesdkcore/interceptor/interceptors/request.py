class RuntimeOption(object):
    def __init__(self, client_side_validation, ak=None, sk=None, session_token=None, region=None, scheme=None,
                 endpoint_provider=None, connect_timeout=None, read_timeout=None):
        self.ak = ak
        self.sk = sk
        self.session_token = session_token
        self.region = region
        self.scheme = scheme
        self.endpoint_provider = endpoint_provider
        self.connect_timeout = connect_timeout
        self.read_timeout = read_timeout
        self.client_side_validation = client_side_validation


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

        self.runtime_options = None
        if hasattr(body, '_configuration') and isinstance(body._configuration, RuntimeOption):
            self.runtime_options = body._configuration
