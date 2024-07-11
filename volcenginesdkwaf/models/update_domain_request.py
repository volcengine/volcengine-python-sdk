# coding: utf-8

"""
    waf

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class UpdateDomainRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'access_mode': 'int',
        'backend_groups': 'list[BackendGroupForUpdateDomainInput]',
        'bot_dytoken_enable': 'int',
        'bot_frequency_enable': 'int',
        'bot_repeat_enable': 'int',
        'bot_sequence_default_action': 'int',
        'bot_sequence_enable': 'int',
        'certificate_id': 'int',
        'certificate_platform': 'str',
        'client_ip_location': 'int',
        'client_max_body_size': 'int',
        'cloud_access_config': 'list[CloudAccessConfigForUpdateDomainInput]',
        'custom_header': 'list[str]',
        'domain': 'str',
        'enable_http2': 'int',
        'enable_i_pv6': 'int',
        'keep_alive_request': 'int',
        'keep_alive_time_out': 'int',
        'lb_algorithm': 'str',
        'protocol_follow': 'int',
        'protocol_ports': 'ProtocolPortsForUpdateDomainInput',
        'protocols': 'list[str]',
        'proxy_config': 'int',
        'proxy_connect_time_out': 'int',
        'proxy_keep_alive': 'int',
        'proxy_keep_alive_time_out': 'int',
        'proxy_read_time_out': 'int',
        'proxy_retry': 'int',
        'proxy_write_time_out': 'int',
        'public_real_server': 'int',
        'redirect_https': 'bool',
        'region': 'str',
        'ssl_ciphers': 'list[str]',
        'ssl_protocols': 'list[str]',
        'tls_enable': 'int',
        'volc_certificate_id': 'str',
        'vpc_id': 'str'
    }

    attribute_map = {
        'access_mode': 'AccessMode',
        'backend_groups': 'BackendGroups',
        'bot_dytoken_enable': 'BotDytokenEnable',
        'bot_frequency_enable': 'BotFrequencyEnable',
        'bot_repeat_enable': 'BotRepeatEnable',
        'bot_sequence_default_action': 'BotSequenceDefaultAction',
        'bot_sequence_enable': 'BotSequenceEnable',
        'certificate_id': 'CertificateID',
        'certificate_platform': 'CertificatePlatform',
        'client_ip_location': 'ClientIPLocation',
        'client_max_body_size': 'ClientMaxBodySize',
        'cloud_access_config': 'CloudAccessConfig',
        'custom_header': 'CustomHeader',
        'domain': 'Domain',
        'enable_http2': 'EnableHTTP2',
        'enable_i_pv6': 'EnableIPv6',
        'keep_alive_request': 'KeepAliveRequest',
        'keep_alive_time_out': 'KeepAliveTimeOut',
        'lb_algorithm': 'LBAlgorithm',
        'protocol_follow': 'ProtocolFollow',
        'protocol_ports': 'ProtocolPorts',
        'protocols': 'Protocols',
        'proxy_config': 'ProxyConfig',
        'proxy_connect_time_out': 'ProxyConnectTimeOut',
        'proxy_keep_alive': 'ProxyKeepAlive',
        'proxy_keep_alive_time_out': 'ProxyKeepAliveTimeOut',
        'proxy_read_time_out': 'ProxyReadTimeOut',
        'proxy_retry': 'ProxyRetry',
        'proxy_write_time_out': 'ProxyWriteTimeOut',
        'public_real_server': 'PublicRealServer',
        'redirect_https': 'RedirectHTTPS',
        'region': 'Region',
        'ssl_ciphers': 'SSLCiphers',
        'ssl_protocols': 'SSLProtocols',
        'tls_enable': 'TLSEnable',
        'volc_certificate_id': 'VolcCertificateID',
        'vpc_id': 'VpcID'
    }

    def __init__(self, access_mode=None, backend_groups=None, bot_dytoken_enable=None, bot_frequency_enable=None, bot_repeat_enable=None, bot_sequence_default_action=None, bot_sequence_enable=None, certificate_id=None, certificate_platform=None, client_ip_location=None, client_max_body_size=None, cloud_access_config=None, custom_header=None, domain=None, enable_http2=None, enable_i_pv6=None, keep_alive_request=None, keep_alive_time_out=None, lb_algorithm=None, protocol_follow=None, protocol_ports=None, protocols=None, proxy_config=None, proxy_connect_time_out=None, proxy_keep_alive=None, proxy_keep_alive_time_out=None, proxy_read_time_out=None, proxy_retry=None, proxy_write_time_out=None, public_real_server=None, redirect_https=None, region=None, ssl_ciphers=None, ssl_protocols=None, tls_enable=None, volc_certificate_id=None, vpc_id=None, _configuration=None):  # noqa: E501
        """UpdateDomainRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._access_mode = None
        self._backend_groups = None
        self._bot_dytoken_enable = None
        self._bot_frequency_enable = None
        self._bot_repeat_enable = None
        self._bot_sequence_default_action = None
        self._bot_sequence_enable = None
        self._certificate_id = None
        self._certificate_platform = None
        self._client_ip_location = None
        self._client_max_body_size = None
        self._cloud_access_config = None
        self._custom_header = None
        self._domain = None
        self._enable_http2 = None
        self._enable_i_pv6 = None
        self._keep_alive_request = None
        self._keep_alive_time_out = None
        self._lb_algorithm = None
        self._protocol_follow = None
        self._protocol_ports = None
        self._protocols = None
        self._proxy_config = None
        self._proxy_connect_time_out = None
        self._proxy_keep_alive = None
        self._proxy_keep_alive_time_out = None
        self._proxy_read_time_out = None
        self._proxy_retry = None
        self._proxy_write_time_out = None
        self._public_real_server = None
        self._redirect_https = None
        self._region = None
        self._ssl_ciphers = None
        self._ssl_protocols = None
        self._tls_enable = None
        self._volc_certificate_id = None
        self._vpc_id = None
        self.discriminator = None

        self.access_mode = access_mode
        if backend_groups is not None:
            self.backend_groups = backend_groups
        if bot_dytoken_enable is not None:
            self.bot_dytoken_enable = bot_dytoken_enable
        if bot_frequency_enable is not None:
            self.bot_frequency_enable = bot_frequency_enable
        if bot_repeat_enable is not None:
            self.bot_repeat_enable = bot_repeat_enable
        if bot_sequence_default_action is not None:
            self.bot_sequence_default_action = bot_sequence_default_action
        if bot_sequence_enable is not None:
            self.bot_sequence_enable = bot_sequence_enable
        if certificate_id is not None:
            self.certificate_id = certificate_id
        if certificate_platform is not None:
            self.certificate_platform = certificate_platform
        if client_ip_location is not None:
            self.client_ip_location = client_ip_location
        if client_max_body_size is not None:
            self.client_max_body_size = client_max_body_size
        if cloud_access_config is not None:
            self.cloud_access_config = cloud_access_config
        if custom_header is not None:
            self.custom_header = custom_header
        self.domain = domain
        if enable_http2 is not None:
            self.enable_http2 = enable_http2
        if enable_i_pv6 is not None:
            self.enable_i_pv6 = enable_i_pv6
        if keep_alive_request is not None:
            self.keep_alive_request = keep_alive_request
        if keep_alive_time_out is not None:
            self.keep_alive_time_out = keep_alive_time_out
        if lb_algorithm is not None:
            self.lb_algorithm = lb_algorithm
        if protocol_follow is not None:
            self.protocol_follow = protocol_follow
        if protocol_ports is not None:
            self.protocol_ports = protocol_ports
        if protocols is not None:
            self.protocols = protocols
        if proxy_config is not None:
            self.proxy_config = proxy_config
        if proxy_connect_time_out is not None:
            self.proxy_connect_time_out = proxy_connect_time_out
        if proxy_keep_alive is not None:
            self.proxy_keep_alive = proxy_keep_alive
        if proxy_keep_alive_time_out is not None:
            self.proxy_keep_alive_time_out = proxy_keep_alive_time_out
        if proxy_read_time_out is not None:
            self.proxy_read_time_out = proxy_read_time_out
        if proxy_retry is not None:
            self.proxy_retry = proxy_retry
        if proxy_write_time_out is not None:
            self.proxy_write_time_out = proxy_write_time_out
        if public_real_server is not None:
            self.public_real_server = public_real_server
        if redirect_https is not None:
            self.redirect_https = redirect_https
        self.region = region
        if ssl_ciphers is not None:
            self.ssl_ciphers = ssl_ciphers
        if ssl_protocols is not None:
            self.ssl_protocols = ssl_protocols
        if tls_enable is not None:
            self.tls_enable = tls_enable
        if volc_certificate_id is not None:
            self.volc_certificate_id = volc_certificate_id
        if vpc_id is not None:
            self.vpc_id = vpc_id

    @property
    def access_mode(self):
        """Gets the access_mode of this UpdateDomainRequest.  # noqa: E501


        :return: The access_mode of this UpdateDomainRequest.  # noqa: E501
        :rtype: int
        """
        return self._access_mode

    @access_mode.setter
    def access_mode(self, access_mode):
        """Sets the access_mode of this UpdateDomainRequest.


        :param access_mode: The access_mode of this UpdateDomainRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and access_mode is None:
            raise ValueError("Invalid value for `access_mode`, must not be `None`")  # noqa: E501

        self._access_mode = access_mode

    @property
    def backend_groups(self):
        """Gets the backend_groups of this UpdateDomainRequest.  # noqa: E501


        :return: The backend_groups of this UpdateDomainRequest.  # noqa: E501
        :rtype: list[BackendGroupForUpdateDomainInput]
        """
        return self._backend_groups

    @backend_groups.setter
    def backend_groups(self, backend_groups):
        """Sets the backend_groups of this UpdateDomainRequest.


        :param backend_groups: The backend_groups of this UpdateDomainRequest.  # noqa: E501
        :type: list[BackendGroupForUpdateDomainInput]
        """

        self._backend_groups = backend_groups

    @property
    def bot_dytoken_enable(self):
        """Gets the bot_dytoken_enable of this UpdateDomainRequest.  # noqa: E501


        :return: The bot_dytoken_enable of this UpdateDomainRequest.  # noqa: E501
        :rtype: int
        """
        return self._bot_dytoken_enable

    @bot_dytoken_enable.setter
    def bot_dytoken_enable(self, bot_dytoken_enable):
        """Sets the bot_dytoken_enable of this UpdateDomainRequest.


        :param bot_dytoken_enable: The bot_dytoken_enable of this UpdateDomainRequest.  # noqa: E501
        :type: int
        """

        self._bot_dytoken_enable = bot_dytoken_enable

    @property
    def bot_frequency_enable(self):
        """Gets the bot_frequency_enable of this UpdateDomainRequest.  # noqa: E501


        :return: The bot_frequency_enable of this UpdateDomainRequest.  # noqa: E501
        :rtype: int
        """
        return self._bot_frequency_enable

    @bot_frequency_enable.setter
    def bot_frequency_enable(self, bot_frequency_enable):
        """Sets the bot_frequency_enable of this UpdateDomainRequest.


        :param bot_frequency_enable: The bot_frequency_enable of this UpdateDomainRequest.  # noqa: E501
        :type: int
        """

        self._bot_frequency_enable = bot_frequency_enable

    @property
    def bot_repeat_enable(self):
        """Gets the bot_repeat_enable of this UpdateDomainRequest.  # noqa: E501


        :return: The bot_repeat_enable of this UpdateDomainRequest.  # noqa: E501
        :rtype: int
        """
        return self._bot_repeat_enable

    @bot_repeat_enable.setter
    def bot_repeat_enable(self, bot_repeat_enable):
        """Sets the bot_repeat_enable of this UpdateDomainRequest.


        :param bot_repeat_enable: The bot_repeat_enable of this UpdateDomainRequest.  # noqa: E501
        :type: int
        """

        self._bot_repeat_enable = bot_repeat_enable

    @property
    def bot_sequence_default_action(self):
        """Gets the bot_sequence_default_action of this UpdateDomainRequest.  # noqa: E501


        :return: The bot_sequence_default_action of this UpdateDomainRequest.  # noqa: E501
        :rtype: int
        """
        return self._bot_sequence_default_action

    @bot_sequence_default_action.setter
    def bot_sequence_default_action(self, bot_sequence_default_action):
        """Sets the bot_sequence_default_action of this UpdateDomainRequest.


        :param bot_sequence_default_action: The bot_sequence_default_action of this UpdateDomainRequest.  # noqa: E501
        :type: int
        """

        self._bot_sequence_default_action = bot_sequence_default_action

    @property
    def bot_sequence_enable(self):
        """Gets the bot_sequence_enable of this UpdateDomainRequest.  # noqa: E501


        :return: The bot_sequence_enable of this UpdateDomainRequest.  # noqa: E501
        :rtype: int
        """
        return self._bot_sequence_enable

    @bot_sequence_enable.setter
    def bot_sequence_enable(self, bot_sequence_enable):
        """Sets the bot_sequence_enable of this UpdateDomainRequest.


        :param bot_sequence_enable: The bot_sequence_enable of this UpdateDomainRequest.  # noqa: E501
        :type: int
        """

        self._bot_sequence_enable = bot_sequence_enable

    @property
    def certificate_id(self):
        """Gets the certificate_id of this UpdateDomainRequest.  # noqa: E501


        :return: The certificate_id of this UpdateDomainRequest.  # noqa: E501
        :rtype: int
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        """Sets the certificate_id of this UpdateDomainRequest.


        :param certificate_id: The certificate_id of this UpdateDomainRequest.  # noqa: E501
        :type: int
        """

        self._certificate_id = certificate_id

    @property
    def certificate_platform(self):
        """Gets the certificate_platform of this UpdateDomainRequest.  # noqa: E501


        :return: The certificate_platform of this UpdateDomainRequest.  # noqa: E501
        :rtype: str
        """
        return self._certificate_platform

    @certificate_platform.setter
    def certificate_platform(self, certificate_platform):
        """Sets the certificate_platform of this UpdateDomainRequest.


        :param certificate_platform: The certificate_platform of this UpdateDomainRequest.  # noqa: E501
        :type: str
        """

        self._certificate_platform = certificate_platform

    @property
    def client_ip_location(self):
        """Gets the client_ip_location of this UpdateDomainRequest.  # noqa: E501


        :return: The client_ip_location of this UpdateDomainRequest.  # noqa: E501
        :rtype: int
        """
        return self._client_ip_location

    @client_ip_location.setter
    def client_ip_location(self, client_ip_location):
        """Sets the client_ip_location of this UpdateDomainRequest.


        :param client_ip_location: The client_ip_location of this UpdateDomainRequest.  # noqa: E501
        :type: int
        """

        self._client_ip_location = client_ip_location

    @property
    def client_max_body_size(self):
        """Gets the client_max_body_size of this UpdateDomainRequest.  # noqa: E501


        :return: The client_max_body_size of this UpdateDomainRequest.  # noqa: E501
        :rtype: int
        """
        return self._client_max_body_size

    @client_max_body_size.setter
    def client_max_body_size(self, client_max_body_size):
        """Sets the client_max_body_size of this UpdateDomainRequest.


        :param client_max_body_size: The client_max_body_size of this UpdateDomainRequest.  # noqa: E501
        :type: int
        """

        self._client_max_body_size = client_max_body_size

    @property
    def cloud_access_config(self):
        """Gets the cloud_access_config of this UpdateDomainRequest.  # noqa: E501


        :return: The cloud_access_config of this UpdateDomainRequest.  # noqa: E501
        :rtype: list[CloudAccessConfigForUpdateDomainInput]
        """
        return self._cloud_access_config

    @cloud_access_config.setter
    def cloud_access_config(self, cloud_access_config):
        """Sets the cloud_access_config of this UpdateDomainRequest.


        :param cloud_access_config: The cloud_access_config of this UpdateDomainRequest.  # noqa: E501
        :type: list[CloudAccessConfigForUpdateDomainInput]
        """

        self._cloud_access_config = cloud_access_config

    @property
    def custom_header(self):
        """Gets the custom_header of this UpdateDomainRequest.  # noqa: E501


        :return: The custom_header of this UpdateDomainRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._custom_header

    @custom_header.setter
    def custom_header(self, custom_header):
        """Sets the custom_header of this UpdateDomainRequest.


        :param custom_header: The custom_header of this UpdateDomainRequest.  # noqa: E501
        :type: list[str]
        """

        self._custom_header = custom_header

    @property
    def domain(self):
        """Gets the domain of this UpdateDomainRequest.  # noqa: E501


        :return: The domain of this UpdateDomainRequest.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this UpdateDomainRequest.


        :param domain: The domain of this UpdateDomainRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and domain is None:
            raise ValueError("Invalid value for `domain`, must not be `None`")  # noqa: E501

        self._domain = domain

    @property
    def enable_http2(self):
        """Gets the enable_http2 of this UpdateDomainRequest.  # noqa: E501


        :return: The enable_http2 of this UpdateDomainRequest.  # noqa: E501
        :rtype: int
        """
        return self._enable_http2

    @enable_http2.setter
    def enable_http2(self, enable_http2):
        """Sets the enable_http2 of this UpdateDomainRequest.


        :param enable_http2: The enable_http2 of this UpdateDomainRequest.  # noqa: E501
        :type: int
        """

        self._enable_http2 = enable_http2

    @property
    def enable_i_pv6(self):
        """Gets the enable_i_pv6 of this UpdateDomainRequest.  # noqa: E501


        :return: The enable_i_pv6 of this UpdateDomainRequest.  # noqa: E501
        :rtype: int
        """
        return self._enable_i_pv6

    @enable_i_pv6.setter
    def enable_i_pv6(self, enable_i_pv6):
        """Sets the enable_i_pv6 of this UpdateDomainRequest.


        :param enable_i_pv6: The enable_i_pv6 of this UpdateDomainRequest.  # noqa: E501
        :type: int
        """

        self._enable_i_pv6 = enable_i_pv6

    @property
    def keep_alive_request(self):
        """Gets the keep_alive_request of this UpdateDomainRequest.  # noqa: E501


        :return: The keep_alive_request of this UpdateDomainRequest.  # noqa: E501
        :rtype: int
        """
        return self._keep_alive_request

    @keep_alive_request.setter
    def keep_alive_request(self, keep_alive_request):
        """Sets the keep_alive_request of this UpdateDomainRequest.


        :param keep_alive_request: The keep_alive_request of this UpdateDomainRequest.  # noqa: E501
        :type: int
        """

        self._keep_alive_request = keep_alive_request

    @property
    def keep_alive_time_out(self):
        """Gets the keep_alive_time_out of this UpdateDomainRequest.  # noqa: E501


        :return: The keep_alive_time_out of this UpdateDomainRequest.  # noqa: E501
        :rtype: int
        """
        return self._keep_alive_time_out

    @keep_alive_time_out.setter
    def keep_alive_time_out(self, keep_alive_time_out):
        """Sets the keep_alive_time_out of this UpdateDomainRequest.


        :param keep_alive_time_out: The keep_alive_time_out of this UpdateDomainRequest.  # noqa: E501
        :type: int
        """

        self._keep_alive_time_out = keep_alive_time_out

    @property
    def lb_algorithm(self):
        """Gets the lb_algorithm of this UpdateDomainRequest.  # noqa: E501


        :return: The lb_algorithm of this UpdateDomainRequest.  # noqa: E501
        :rtype: str
        """
        return self._lb_algorithm

    @lb_algorithm.setter
    def lb_algorithm(self, lb_algorithm):
        """Sets the lb_algorithm of this UpdateDomainRequest.


        :param lb_algorithm: The lb_algorithm of this UpdateDomainRequest.  # noqa: E501
        :type: str
        """

        self._lb_algorithm = lb_algorithm

    @property
    def protocol_follow(self):
        """Gets the protocol_follow of this UpdateDomainRequest.  # noqa: E501


        :return: The protocol_follow of this UpdateDomainRequest.  # noqa: E501
        :rtype: int
        """
        return self._protocol_follow

    @protocol_follow.setter
    def protocol_follow(self, protocol_follow):
        """Sets the protocol_follow of this UpdateDomainRequest.


        :param protocol_follow: The protocol_follow of this UpdateDomainRequest.  # noqa: E501
        :type: int
        """

        self._protocol_follow = protocol_follow

    @property
    def protocol_ports(self):
        """Gets the protocol_ports of this UpdateDomainRequest.  # noqa: E501


        :return: The protocol_ports of this UpdateDomainRequest.  # noqa: E501
        :rtype: ProtocolPortsForUpdateDomainInput
        """
        return self._protocol_ports

    @protocol_ports.setter
    def protocol_ports(self, protocol_ports):
        """Sets the protocol_ports of this UpdateDomainRequest.


        :param protocol_ports: The protocol_ports of this UpdateDomainRequest.  # noqa: E501
        :type: ProtocolPortsForUpdateDomainInput
        """

        self._protocol_ports = protocol_ports

    @property
    def protocols(self):
        """Gets the protocols of this UpdateDomainRequest.  # noqa: E501


        :return: The protocols of this UpdateDomainRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._protocols

    @protocols.setter
    def protocols(self, protocols):
        """Sets the protocols of this UpdateDomainRequest.


        :param protocols: The protocols of this UpdateDomainRequest.  # noqa: E501
        :type: list[str]
        """

        self._protocols = protocols

    @property
    def proxy_config(self):
        """Gets the proxy_config of this UpdateDomainRequest.  # noqa: E501


        :return: The proxy_config of this UpdateDomainRequest.  # noqa: E501
        :rtype: int
        """
        return self._proxy_config

    @proxy_config.setter
    def proxy_config(self, proxy_config):
        """Sets the proxy_config of this UpdateDomainRequest.


        :param proxy_config: The proxy_config of this UpdateDomainRequest.  # noqa: E501
        :type: int
        """

        self._proxy_config = proxy_config

    @property
    def proxy_connect_time_out(self):
        """Gets the proxy_connect_time_out of this UpdateDomainRequest.  # noqa: E501


        :return: The proxy_connect_time_out of this UpdateDomainRequest.  # noqa: E501
        :rtype: int
        """
        return self._proxy_connect_time_out

    @proxy_connect_time_out.setter
    def proxy_connect_time_out(self, proxy_connect_time_out):
        """Sets the proxy_connect_time_out of this UpdateDomainRequest.


        :param proxy_connect_time_out: The proxy_connect_time_out of this UpdateDomainRequest.  # noqa: E501
        :type: int
        """

        self._proxy_connect_time_out = proxy_connect_time_out

    @property
    def proxy_keep_alive(self):
        """Gets the proxy_keep_alive of this UpdateDomainRequest.  # noqa: E501


        :return: The proxy_keep_alive of this UpdateDomainRequest.  # noqa: E501
        :rtype: int
        """
        return self._proxy_keep_alive

    @proxy_keep_alive.setter
    def proxy_keep_alive(self, proxy_keep_alive):
        """Sets the proxy_keep_alive of this UpdateDomainRequest.


        :param proxy_keep_alive: The proxy_keep_alive of this UpdateDomainRequest.  # noqa: E501
        :type: int
        """

        self._proxy_keep_alive = proxy_keep_alive

    @property
    def proxy_keep_alive_time_out(self):
        """Gets the proxy_keep_alive_time_out of this UpdateDomainRequest.  # noqa: E501


        :return: The proxy_keep_alive_time_out of this UpdateDomainRequest.  # noqa: E501
        :rtype: int
        """
        return self._proxy_keep_alive_time_out

    @proxy_keep_alive_time_out.setter
    def proxy_keep_alive_time_out(self, proxy_keep_alive_time_out):
        """Sets the proxy_keep_alive_time_out of this UpdateDomainRequest.


        :param proxy_keep_alive_time_out: The proxy_keep_alive_time_out of this UpdateDomainRequest.  # noqa: E501
        :type: int
        """

        self._proxy_keep_alive_time_out = proxy_keep_alive_time_out

    @property
    def proxy_read_time_out(self):
        """Gets the proxy_read_time_out of this UpdateDomainRequest.  # noqa: E501


        :return: The proxy_read_time_out of this UpdateDomainRequest.  # noqa: E501
        :rtype: int
        """
        return self._proxy_read_time_out

    @proxy_read_time_out.setter
    def proxy_read_time_out(self, proxy_read_time_out):
        """Sets the proxy_read_time_out of this UpdateDomainRequest.


        :param proxy_read_time_out: The proxy_read_time_out of this UpdateDomainRequest.  # noqa: E501
        :type: int
        """

        self._proxy_read_time_out = proxy_read_time_out

    @property
    def proxy_retry(self):
        """Gets the proxy_retry of this UpdateDomainRequest.  # noqa: E501


        :return: The proxy_retry of this UpdateDomainRequest.  # noqa: E501
        :rtype: int
        """
        return self._proxy_retry

    @proxy_retry.setter
    def proxy_retry(self, proxy_retry):
        """Sets the proxy_retry of this UpdateDomainRequest.


        :param proxy_retry: The proxy_retry of this UpdateDomainRequest.  # noqa: E501
        :type: int
        """

        self._proxy_retry = proxy_retry

    @property
    def proxy_write_time_out(self):
        """Gets the proxy_write_time_out of this UpdateDomainRequest.  # noqa: E501


        :return: The proxy_write_time_out of this UpdateDomainRequest.  # noqa: E501
        :rtype: int
        """
        return self._proxy_write_time_out

    @proxy_write_time_out.setter
    def proxy_write_time_out(self, proxy_write_time_out):
        """Sets the proxy_write_time_out of this UpdateDomainRequest.


        :param proxy_write_time_out: The proxy_write_time_out of this UpdateDomainRequest.  # noqa: E501
        :type: int
        """

        self._proxy_write_time_out = proxy_write_time_out

    @property
    def public_real_server(self):
        """Gets the public_real_server of this UpdateDomainRequest.  # noqa: E501


        :return: The public_real_server of this UpdateDomainRequest.  # noqa: E501
        :rtype: int
        """
        return self._public_real_server

    @public_real_server.setter
    def public_real_server(self, public_real_server):
        """Sets the public_real_server of this UpdateDomainRequest.


        :param public_real_server: The public_real_server of this UpdateDomainRequest.  # noqa: E501
        :type: int
        """

        self._public_real_server = public_real_server

    @property
    def redirect_https(self):
        """Gets the redirect_https of this UpdateDomainRequest.  # noqa: E501


        :return: The redirect_https of this UpdateDomainRequest.  # noqa: E501
        :rtype: bool
        """
        return self._redirect_https

    @redirect_https.setter
    def redirect_https(self, redirect_https):
        """Sets the redirect_https of this UpdateDomainRequest.


        :param redirect_https: The redirect_https of this UpdateDomainRequest.  # noqa: E501
        :type: bool
        """

        self._redirect_https = redirect_https

    @property
    def region(self):
        """Gets the region of this UpdateDomainRequest.  # noqa: E501


        :return: The region of this UpdateDomainRequest.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this UpdateDomainRequest.


        :param region: The region of this UpdateDomainRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and region is None:
            raise ValueError("Invalid value for `region`, must not be `None`")  # noqa: E501

        self._region = region

    @property
    def ssl_ciphers(self):
        """Gets the ssl_ciphers of this UpdateDomainRequest.  # noqa: E501


        :return: The ssl_ciphers of this UpdateDomainRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._ssl_ciphers

    @ssl_ciphers.setter
    def ssl_ciphers(self, ssl_ciphers):
        """Sets the ssl_ciphers of this UpdateDomainRequest.


        :param ssl_ciphers: The ssl_ciphers of this UpdateDomainRequest.  # noqa: E501
        :type: list[str]
        """

        self._ssl_ciphers = ssl_ciphers

    @property
    def ssl_protocols(self):
        """Gets the ssl_protocols of this UpdateDomainRequest.  # noqa: E501


        :return: The ssl_protocols of this UpdateDomainRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._ssl_protocols

    @ssl_protocols.setter
    def ssl_protocols(self, ssl_protocols):
        """Sets the ssl_protocols of this UpdateDomainRequest.


        :param ssl_protocols: The ssl_protocols of this UpdateDomainRequest.  # noqa: E501
        :type: list[str]
        """

        self._ssl_protocols = ssl_protocols

    @property
    def tls_enable(self):
        """Gets the tls_enable of this UpdateDomainRequest.  # noqa: E501


        :return: The tls_enable of this UpdateDomainRequest.  # noqa: E501
        :rtype: int
        """
        return self._tls_enable

    @tls_enable.setter
    def tls_enable(self, tls_enable):
        """Sets the tls_enable of this UpdateDomainRequest.


        :param tls_enable: The tls_enable of this UpdateDomainRequest.  # noqa: E501
        :type: int
        """

        self._tls_enable = tls_enable

    @property
    def volc_certificate_id(self):
        """Gets the volc_certificate_id of this UpdateDomainRequest.  # noqa: E501


        :return: The volc_certificate_id of this UpdateDomainRequest.  # noqa: E501
        :rtype: str
        """
        return self._volc_certificate_id

    @volc_certificate_id.setter
    def volc_certificate_id(self, volc_certificate_id):
        """Sets the volc_certificate_id of this UpdateDomainRequest.


        :param volc_certificate_id: The volc_certificate_id of this UpdateDomainRequest.  # noqa: E501
        :type: str
        """

        self._volc_certificate_id = volc_certificate_id

    @property
    def vpc_id(self):
        """Gets the vpc_id of this UpdateDomainRequest.  # noqa: E501


        :return: The vpc_id of this UpdateDomainRequest.  # noqa: E501
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this UpdateDomainRequest.


        :param vpc_id: The vpc_id of this UpdateDomainRequest.  # noqa: E501
        :type: str
        """

        self._vpc_id = vpc_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(UpdateDomainRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateDomainRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateDomainRequest):
            return True

        return self.to_dict() != other.to_dict()
