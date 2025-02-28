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


class CreateDomainResponse(object):
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
        'cname': 'str',
        'default_module_quick_conf': 'DefaultModuleQuickConfForCreateDomainOutput',
        'domain': 'str',
        'server_ips': 'str',
        'src_ips': 'str'
    }

    attribute_map = {
        'cname': 'Cname',
        'default_module_quick_conf': 'DefaultModuleQuickConf',
        'domain': 'Domain',
        'server_ips': 'ServerIps',
        'src_ips': 'SrcIps'
    }

    def __init__(self, cname=None, default_module_quick_conf=None, domain=None, server_ips=None, src_ips=None, _configuration=None):  # noqa: E501
        """CreateDomainResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cname = None
        self._default_module_quick_conf = None
        self._domain = None
        self._server_ips = None
        self._src_ips = None
        self.discriminator = None

        if cname is not None:
            self.cname = cname
        if default_module_quick_conf is not None:
            self.default_module_quick_conf = default_module_quick_conf
        if domain is not None:
            self.domain = domain
        if server_ips is not None:
            self.server_ips = server_ips
        if src_ips is not None:
            self.src_ips = src_ips

    @property
    def cname(self):
        """Gets the cname of this CreateDomainResponse.  # noqa: E501


        :return: The cname of this CreateDomainResponse.  # noqa: E501
        :rtype: str
        """
        return self._cname

    @cname.setter
    def cname(self, cname):
        """Sets the cname of this CreateDomainResponse.


        :param cname: The cname of this CreateDomainResponse.  # noqa: E501
        :type: str
        """

        self._cname = cname

    @property
    def default_module_quick_conf(self):
        """Gets the default_module_quick_conf of this CreateDomainResponse.  # noqa: E501


        :return: The default_module_quick_conf of this CreateDomainResponse.  # noqa: E501
        :rtype: DefaultModuleQuickConfForCreateDomainOutput
        """
        return self._default_module_quick_conf

    @default_module_quick_conf.setter
    def default_module_quick_conf(self, default_module_quick_conf):
        """Sets the default_module_quick_conf of this CreateDomainResponse.


        :param default_module_quick_conf: The default_module_quick_conf of this CreateDomainResponse.  # noqa: E501
        :type: DefaultModuleQuickConfForCreateDomainOutput
        """

        self._default_module_quick_conf = default_module_quick_conf

    @property
    def domain(self):
        """Gets the domain of this CreateDomainResponse.  # noqa: E501


        :return: The domain of this CreateDomainResponse.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this CreateDomainResponse.


        :param domain: The domain of this CreateDomainResponse.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def server_ips(self):
        """Gets the server_ips of this CreateDomainResponse.  # noqa: E501


        :return: The server_ips of this CreateDomainResponse.  # noqa: E501
        :rtype: str
        """
        return self._server_ips

    @server_ips.setter
    def server_ips(self, server_ips):
        """Sets the server_ips of this CreateDomainResponse.


        :param server_ips: The server_ips of this CreateDomainResponse.  # noqa: E501
        :type: str
        """

        self._server_ips = server_ips

    @property
    def src_ips(self):
        """Gets the src_ips of this CreateDomainResponse.  # noqa: E501


        :return: The src_ips of this CreateDomainResponse.  # noqa: E501
        :rtype: str
        """
        return self._src_ips

    @src_ips.setter
    def src_ips(self, src_ips):
        """Sets the src_ips of this CreateDomainResponse.


        :param src_ips: The src_ips of this CreateDomainResponse.  # noqa: E501
        :type: str
        """

        self._src_ips = src_ips

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
        if issubclass(CreateDomainResponse, dict):
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
        if not isinstance(other, CreateDomainResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateDomainResponse):
            return True

        return self.to_dict() != other.to_dict()
