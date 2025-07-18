# coding: utf-8

from __future__ import absolute_import

import copy
import logging
import multiprocessing
import sys
import warnings

import six
from six.moves import http_client as httplib

from volcenginesdkcore.endpoint import DefaultEndpointProvider
from volcenginesdkcore.retryer.retryer import DEFAULT_RETRYER


class TypeWithDefault(type):
    def __init__(cls, name, bases, dct):
        super(TypeWithDefault, cls).__init__(name, bases, dct)
        cls._default = None

    def __call__(cls):
        if cls._default is None:
            cls._default = type.__call__(cls)
        return copy.copy(cls._default)

    def set_default(cls, default):
        cls._default = copy.copy(default)


class Configuration(six.with_metaclass(TypeWithDefault, object)):
    """NOTE: This class is auto generated by the swagger code generator program.

    Ref: https://github.com/swagger-api/swagger-codegen
    Do not edit the class manually.
    """

    @property
    def schema(self):
        warnings.warn(
            "The field 'schema' is deprecated and will be removed in future versions. Use 'scheme' instead.",
            DeprecationWarning,
            stacklevel=2
        )
        return self.scheme

    @schema.setter
    def schema(self, value):
        warnings.warn(
            "The field 'schema' is deprecated and will be removed in future versions. Use 'scheme' instead.",
            DeprecationWarning,
            stacklevel=2
        )
        self.scheme = value

    def __init__(self):
        """Constructor"""

        # Default Base url
        self.host = None

        # Custom bootstrap region dict
        self.custom_bootstrap_region = None

        # use dual stack endpoint rule
        self.use_dual_stack = None

        # Scheme Support http or https
        self.scheme = "https"
        # Temp file folder for downloading files
        self.temp_folder_path = None

        # Authentication Settings
        # dict to store API key(s)
        self.api_key = {}
        # dict to store API prefix (e.g. Bearer)
        self.api_key_prefix = {}
        # function to refresh API key if expired
        self.refresh_api_key_hook = None

        # 自定义适配
        self.ak = ""
        self.sk = ""
        self.session_token = ""
        self.region = ""

        # Logging Settings
        self.logger = {}
        self.logger["package_logger"] = logging.getLogger("volcenginesdkcore")
        self.logger["urllib3_logger"] = logging.getLogger("urllib3")
        # Log format
        self.logger_format = '%(asctime)s %(levelname)s %(message)s'
        # Log stream handler
        self.logger_stream_handler = None
        # Log file handler
        self.logger_file_handler = None
        # Debug file location
        self.logger_file = None
        # Debug switch
        self.debug = False

        # SSL/TLS verification
        # Set this to false to skip verifying SSL certificate when calling API
        # from https server.
        self.verify_ssl = True
        # Set this to customize the certificate file to verify the peer.
        self.ssl_ca_cert = None
        # client certificate file
        self.cert_file = None
        # client key file
        self.key_file = None
        # Set this to True/False to enable/disable SSL hostname verification.
        self.assert_hostname = None

        self.num_pools = 4

        self.connect_timeout = 30.0
        self.read_timeout = 30.0

        # urllib3 connection pool's maximum number of connections saved
        # per pool. urllib3 uses 1 connection as default value, but this is
        # not the best value when you are making a lot of possibly parallel
        # requests to the same host, which is often the case here.
        # cpu_count * 5 is used as default value to increase performance.
        self.connection_pool_maxsize = multiprocessing.cpu_count() * 5

        # Proxy URL
        self.proxy = None
        # Safe chars for path_param
        self.safe_chars_for_path_param = ''

        # Disable client side validation
        self.client_side_validation = True

        self.endpoint_provider = DefaultEndpointProvider()

        self.auto_retry = True
        self.__retryer = DEFAULT_RETRYER
        self.__retry_error_codes = None
        self.__min_retry_delay_ms = None
        self.__max_retry_delay_ms = None

    @property
    def logger_file(self):
        """The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str
        """
        return self.__logger_file

    @logger_file.setter
    def logger_file(self, value):
        """The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str
        """
        self.__logger_file = value
        if self.__logger_file:
            # If set logging file,
            # then add file handler and remove stream handler.
            self.logger_file_handler = logging.FileHandler(self.__logger_file)
            self.logger_file_handler.setFormatter(self.logger_formatter)
            for _, logger in six.iteritems(self.logger):
                logger.addHandler(self.logger_file_handler)
                if self.logger_stream_handler:
                    logger.removeHandler(self.logger_stream_handler)
        else:
            # If not set logging file,
            # then add stream handler and remove file handler.
            self.logger_stream_handler = logging.StreamHandler()
            self.logger_stream_handler.setFormatter(self.logger_formatter)
            for _, logger in six.iteritems(self.logger):
                logger.addHandler(self.logger_stream_handler)
                if self.logger_file_handler:
                    logger.removeHandler(self.logger_file_handler)

    @property
    def debug(self):
        """Debug status

        :param value: The debug status, True or False.
        :type: bool
        """
        return self.__debug

    @debug.setter
    def debug(self, value):
        """Debug status

        :param value: The debug status, True or False.
        :type: bool
        """
        self.__debug = value
        if self.__debug:
            # if debug status is True, turn on debug logging
            for _, logger in six.iteritems(self.logger):
                logger.setLevel(logging.DEBUG)
            # turn on httplib debug
            httplib.HTTPConnection.debuglevel = 1
        else:
            # if debug status is False, turn off debug logging,
            # setting log level to default `logging.WARNING`
            for _, logger in six.iteritems(self.logger):
                logger.setLevel(logging.WARNING)
            # turn off httplib debug
            httplib.HTTPConnection.debuglevel = 0

    @property
    def logger_format(self):
        """The logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str
        """
        return self.__logger_format

    @logger_format.setter
    def logger_format(self, value):
        """The logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str
        """
        self.__logger_format = value
        self.logger_formatter = logging.Formatter(self.__logger_format)

    def get_api_key_with_prefix(self, identifier):
        """Gets API key (with prefix if set).

        :param identifier: The identifier of apiKey.
        :return: The token for api key authentication.
        """

        if self.refresh_api_key_hook:
            self.refresh_api_key_hook(self)

        key = self.api_key.get(identifier)
        if key:
            prefix = self.api_key_prefix.get(identifier)
            if prefix:
                return "%s %s" % (prefix, key)
            else:
                return key

    def to_debug_report(self):
        """Gets the essential information for debugging.

        :return: The report for debugging.
        """
        return "Python SDK Debug Report:\n" \
               "OS: {env}\n" \
               "Python Version: {pyversion}\n" \
               "Version of the API: 0.1.0\n" \
               "SDK Package Version: 4.0.6".\
            format(env=sys.platform, pyversion=sys.version)

    @property
    def num_max_retries(self):
        return self.__retryer.num_max_retries

    @num_max_retries.setter
    def num_max_retries(self, num_max_retries):
        if num_max_retries is None:
            raise ValueError("num_max_retries cannot be None")
        if num_max_retries < 0:
            raise ValueError("num_max_retries must be greater than or equal to 0")
        self.__retryer.num_max_retries = num_max_retries

    @property
    def backoff_strategy(self):
        return self.__retryer.backoff_strategy

    @backoff_strategy.setter
    def backoff_strategy(self, value):
        self.__retryer.backoff_strategy = value
        if self.min_retry_delay_ms is not None:
            self.__retryer.backoff_strategy.min_retry_delay_ms = self.min_retry_delay_ms
        if self.max_retry_delay_ms is not None:
            self.__retryer.backoff_strategy.max_retry_delay_ms = self.max_retry_delay_ms

    @property
    def retry_condition(self):
        return self.__retryer.retry_condition

    @retry_condition.setter
    def retry_condition(self, value):
        self.__retryer.retry_condition = value
        if self.retry_error_codes is not None:
            self.__retryer.retry_condition.retry_error_codes = self.retry_error_codes

    @property
    def retry_error_codes(self):
        return self.__retry_error_codes

    @retry_error_codes.setter
    def retry_error_codes(self, value):
        self.__retry_error_codes = value
        self.__retryer.retry_condition.retry_error_codes = value

    @property
    def min_retry_delay_ms(self):
        return self.__min_retry_delay_ms

    @min_retry_delay_ms.setter
    def min_retry_delay_ms(self, value):
        self.__min_retry_delay_ms = value
        self.__retryer.backoff_strategy.min_retry_delay_ms = value

    @property
    def max_retry_delay_ms(self):
        return self.__max_retry_delay_ms

    @max_retry_delay_ms.setter
    def max_retry_delay_ms(self, value):
        self.__max_retry_delay_ms = value
        self.__retryer.backoff_strategy.max_retry_delay_ms = value

    @property
    def retryer(self):
        return self.__retryer
