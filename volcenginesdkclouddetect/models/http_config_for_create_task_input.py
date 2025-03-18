# coding: utf-8

"""
    cloud_detect

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class HTTPConfigForCreateTaskInput(object):
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
        'body_type': 'int',
        'custom_host_config': 'CustomHostConfigForCreateTaskInput',
        'dns_server': 'str',
        'dns_type': 'str',
        'http_headers': 'list[HTTPHeaderForCreateTaskInput]',
        'http_method': 'int',
        'http_version': 'str',
        'ignore_certificate': 'bool',
        'max_body_size': 'int',
        'proxy_url': 'str',
        'redirect': 'bool',
        'request_body': 'str',
        'timeout': 'int'
    }

    attribute_map = {
        'body_type': 'BodyType',
        'custom_host_config': 'CustomHostConfig',
        'dns_server': 'DNSServer',
        'dns_type': 'DNSType',
        'http_headers': 'HTTPHeaders',
        'http_method': 'HTTPMethod',
        'http_version': 'HTTPVersion',
        'ignore_certificate': 'IgnoreCertificate',
        'max_body_size': 'MaxBodySize',
        'proxy_url': 'ProxyURL',
        'redirect': 'Redirect',
        'request_body': 'RequestBody',
        'timeout': 'Timeout'
    }

    def __init__(self, body_type=None, custom_host_config=None, dns_server=None, dns_type=None, http_headers=None, http_method=None, http_version=None, ignore_certificate=None, max_body_size=None, proxy_url=None, redirect=None, request_body=None, timeout=None, _configuration=None):  # noqa: E501
        """HTTPConfigForCreateTaskInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._body_type = None
        self._custom_host_config = None
        self._dns_server = None
        self._dns_type = None
        self._http_headers = None
        self._http_method = None
        self._http_version = None
        self._ignore_certificate = None
        self._max_body_size = None
        self._proxy_url = None
        self._redirect = None
        self._request_body = None
        self._timeout = None
        self.discriminator = None

        if body_type is not None:
            self.body_type = body_type
        if custom_host_config is not None:
            self.custom_host_config = custom_host_config
        if dns_server is not None:
            self.dns_server = dns_server
        if dns_type is not None:
            self.dns_type = dns_type
        if http_headers is not None:
            self.http_headers = http_headers
        if http_method is not None:
            self.http_method = http_method
        if http_version is not None:
            self.http_version = http_version
        if ignore_certificate is not None:
            self.ignore_certificate = ignore_certificate
        if max_body_size is not None:
            self.max_body_size = max_body_size
        if proxy_url is not None:
            self.proxy_url = proxy_url
        if redirect is not None:
            self.redirect = redirect
        if request_body is not None:
            self.request_body = request_body
        if timeout is not None:
            self.timeout = timeout

    @property
    def body_type(self):
        """Gets the body_type of this HTTPConfigForCreateTaskInput.  # noqa: E501


        :return: The body_type of this HTTPConfigForCreateTaskInput.  # noqa: E501
        :rtype: int
        """
        return self._body_type

    @body_type.setter
    def body_type(self, body_type):
        """Sets the body_type of this HTTPConfigForCreateTaskInput.


        :param body_type: The body_type of this HTTPConfigForCreateTaskInput.  # noqa: E501
        :type: int
        """

        self._body_type = body_type

    @property
    def custom_host_config(self):
        """Gets the custom_host_config of this HTTPConfigForCreateTaskInput.  # noqa: E501


        :return: The custom_host_config of this HTTPConfigForCreateTaskInput.  # noqa: E501
        :rtype: CustomHostConfigForCreateTaskInput
        """
        return self._custom_host_config

    @custom_host_config.setter
    def custom_host_config(self, custom_host_config):
        """Sets the custom_host_config of this HTTPConfigForCreateTaskInput.


        :param custom_host_config: The custom_host_config of this HTTPConfigForCreateTaskInput.  # noqa: E501
        :type: CustomHostConfigForCreateTaskInput
        """

        self._custom_host_config = custom_host_config

    @property
    def dns_server(self):
        """Gets the dns_server of this HTTPConfigForCreateTaskInput.  # noqa: E501


        :return: The dns_server of this HTTPConfigForCreateTaskInput.  # noqa: E501
        :rtype: str
        """
        return self._dns_server

    @dns_server.setter
    def dns_server(self, dns_server):
        """Sets the dns_server of this HTTPConfigForCreateTaskInput.


        :param dns_server: The dns_server of this HTTPConfigForCreateTaskInput.  # noqa: E501
        :type: str
        """

        self._dns_server = dns_server

    @property
    def dns_type(self):
        """Gets the dns_type of this HTTPConfigForCreateTaskInput.  # noqa: E501


        :return: The dns_type of this HTTPConfigForCreateTaskInput.  # noqa: E501
        :rtype: str
        """
        return self._dns_type

    @dns_type.setter
    def dns_type(self, dns_type):
        """Sets the dns_type of this HTTPConfigForCreateTaskInput.


        :param dns_type: The dns_type of this HTTPConfigForCreateTaskInput.  # noqa: E501
        :type: str
        """

        self._dns_type = dns_type

    @property
    def http_headers(self):
        """Gets the http_headers of this HTTPConfigForCreateTaskInput.  # noqa: E501


        :return: The http_headers of this HTTPConfigForCreateTaskInput.  # noqa: E501
        :rtype: list[HTTPHeaderForCreateTaskInput]
        """
        return self._http_headers

    @http_headers.setter
    def http_headers(self, http_headers):
        """Sets the http_headers of this HTTPConfigForCreateTaskInput.


        :param http_headers: The http_headers of this HTTPConfigForCreateTaskInput.  # noqa: E501
        :type: list[HTTPHeaderForCreateTaskInput]
        """

        self._http_headers = http_headers

    @property
    def http_method(self):
        """Gets the http_method of this HTTPConfigForCreateTaskInput.  # noqa: E501


        :return: The http_method of this HTTPConfigForCreateTaskInput.  # noqa: E501
        :rtype: int
        """
        return self._http_method

    @http_method.setter
    def http_method(self, http_method):
        """Sets the http_method of this HTTPConfigForCreateTaskInput.


        :param http_method: The http_method of this HTTPConfigForCreateTaskInput.  # noqa: E501
        :type: int
        """

        self._http_method = http_method

    @property
    def http_version(self):
        """Gets the http_version of this HTTPConfigForCreateTaskInput.  # noqa: E501


        :return: The http_version of this HTTPConfigForCreateTaskInput.  # noqa: E501
        :rtype: str
        """
        return self._http_version

    @http_version.setter
    def http_version(self, http_version):
        """Sets the http_version of this HTTPConfigForCreateTaskInput.


        :param http_version: The http_version of this HTTPConfigForCreateTaskInput.  # noqa: E501
        :type: str
        """

        self._http_version = http_version

    @property
    def ignore_certificate(self):
        """Gets the ignore_certificate of this HTTPConfigForCreateTaskInput.  # noqa: E501


        :return: The ignore_certificate of this HTTPConfigForCreateTaskInput.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_certificate

    @ignore_certificate.setter
    def ignore_certificate(self, ignore_certificate):
        """Sets the ignore_certificate of this HTTPConfigForCreateTaskInput.


        :param ignore_certificate: The ignore_certificate of this HTTPConfigForCreateTaskInput.  # noqa: E501
        :type: bool
        """

        self._ignore_certificate = ignore_certificate

    @property
    def max_body_size(self):
        """Gets the max_body_size of this HTTPConfigForCreateTaskInput.  # noqa: E501


        :return: The max_body_size of this HTTPConfigForCreateTaskInput.  # noqa: E501
        :rtype: int
        """
        return self._max_body_size

    @max_body_size.setter
    def max_body_size(self, max_body_size):
        """Sets the max_body_size of this HTTPConfigForCreateTaskInput.


        :param max_body_size: The max_body_size of this HTTPConfigForCreateTaskInput.  # noqa: E501
        :type: int
        """

        self._max_body_size = max_body_size

    @property
    def proxy_url(self):
        """Gets the proxy_url of this HTTPConfigForCreateTaskInput.  # noqa: E501


        :return: The proxy_url of this HTTPConfigForCreateTaskInput.  # noqa: E501
        :rtype: str
        """
        return self._proxy_url

    @proxy_url.setter
    def proxy_url(self, proxy_url):
        """Sets the proxy_url of this HTTPConfigForCreateTaskInput.


        :param proxy_url: The proxy_url of this HTTPConfigForCreateTaskInput.  # noqa: E501
        :type: str
        """

        self._proxy_url = proxy_url

    @property
    def redirect(self):
        """Gets the redirect of this HTTPConfigForCreateTaskInput.  # noqa: E501


        :return: The redirect of this HTTPConfigForCreateTaskInput.  # noqa: E501
        :rtype: bool
        """
        return self._redirect

    @redirect.setter
    def redirect(self, redirect):
        """Sets the redirect of this HTTPConfigForCreateTaskInput.


        :param redirect: The redirect of this HTTPConfigForCreateTaskInput.  # noqa: E501
        :type: bool
        """

        self._redirect = redirect

    @property
    def request_body(self):
        """Gets the request_body of this HTTPConfigForCreateTaskInput.  # noqa: E501


        :return: The request_body of this HTTPConfigForCreateTaskInput.  # noqa: E501
        :rtype: str
        """
        return self._request_body

    @request_body.setter
    def request_body(self, request_body):
        """Sets the request_body of this HTTPConfigForCreateTaskInput.


        :param request_body: The request_body of this HTTPConfigForCreateTaskInput.  # noqa: E501
        :type: str
        """

        self._request_body = request_body

    @property
    def timeout(self):
        """Gets the timeout of this HTTPConfigForCreateTaskInput.  # noqa: E501


        :return: The timeout of this HTTPConfigForCreateTaskInput.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this HTTPConfigForCreateTaskInput.


        :param timeout: The timeout of this HTTPConfigForCreateTaskInput.  # noqa: E501
        :type: int
        """

        self._timeout = timeout

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
        if issubclass(HTTPConfigForCreateTaskInput, dict):
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
        if not isinstance(other, HTTPConfigForCreateTaskInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HTTPConfigForCreateTaskInput):
            return True

        return self.to_dict() != other.to_dict()
