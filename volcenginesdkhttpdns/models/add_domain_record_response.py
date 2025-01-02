# coding: utf-8

"""
    httpdns

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class AddDomainRecordResponse(object):
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
        'domain': 'str',
        'enable': 'bool',
        'line': 'str',
        'target': 'list[str]',
        'ttl': 'int',
        'type': 'str',
        'weights': 'list[WeightForAddDomainRecordOutput]'
    }

    attribute_map = {
        'domain': 'Domain',
        'enable': 'Enable',
        'line': 'Line',
        'target': 'Target',
        'ttl': 'Ttl',
        'type': 'Type',
        'weights': 'Weights'
    }

    def __init__(self, domain=None, enable=None, line=None, target=None, ttl=None, type=None, weights=None, _configuration=None):  # noqa: E501
        """AddDomainRecordResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._domain = None
        self._enable = None
        self._line = None
        self._target = None
        self._ttl = None
        self._type = None
        self._weights = None
        self.discriminator = None

        if domain is not None:
            self.domain = domain
        if enable is not None:
            self.enable = enable
        if line is not None:
            self.line = line
        if target is not None:
            self.target = target
        if ttl is not None:
            self.ttl = ttl
        if type is not None:
            self.type = type
        if weights is not None:
            self.weights = weights

    @property
    def domain(self):
        """Gets the domain of this AddDomainRecordResponse.  # noqa: E501


        :return: The domain of this AddDomainRecordResponse.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this AddDomainRecordResponse.


        :param domain: The domain of this AddDomainRecordResponse.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def enable(self):
        """Gets the enable of this AddDomainRecordResponse.  # noqa: E501


        :return: The enable of this AddDomainRecordResponse.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this AddDomainRecordResponse.


        :param enable: The enable of this AddDomainRecordResponse.  # noqa: E501
        :type: bool
        """

        self._enable = enable

    @property
    def line(self):
        """Gets the line of this AddDomainRecordResponse.  # noqa: E501


        :return: The line of this AddDomainRecordResponse.  # noqa: E501
        :rtype: str
        """
        return self._line

    @line.setter
    def line(self, line):
        """Sets the line of this AddDomainRecordResponse.


        :param line: The line of this AddDomainRecordResponse.  # noqa: E501
        :type: str
        """

        self._line = line

    @property
    def target(self):
        """Gets the target of this AddDomainRecordResponse.  # noqa: E501


        :return: The target of this AddDomainRecordResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this AddDomainRecordResponse.


        :param target: The target of this AddDomainRecordResponse.  # noqa: E501
        :type: list[str]
        """

        self._target = target

    @property
    def ttl(self):
        """Gets the ttl of this AddDomainRecordResponse.  # noqa: E501


        :return: The ttl of this AddDomainRecordResponse.  # noqa: E501
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this AddDomainRecordResponse.


        :param ttl: The ttl of this AddDomainRecordResponse.  # noqa: E501
        :type: int
        """

        self._ttl = ttl

    @property
    def type(self):
        """Gets the type of this AddDomainRecordResponse.  # noqa: E501


        :return: The type of this AddDomainRecordResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AddDomainRecordResponse.


        :param type: The type of this AddDomainRecordResponse.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def weights(self):
        """Gets the weights of this AddDomainRecordResponse.  # noqa: E501


        :return: The weights of this AddDomainRecordResponse.  # noqa: E501
        :rtype: list[WeightForAddDomainRecordOutput]
        """
        return self._weights

    @weights.setter
    def weights(self, weights):
        """Sets the weights of this AddDomainRecordResponse.


        :param weights: The weights of this AddDomainRecordResponse.  # noqa: E501
        :type: list[WeightForAddDomainRecordOutput]
        """

        self._weights = weights

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
        if issubclass(AddDomainRecordResponse, dict):
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
        if not isinstance(other, AddDomainRecordResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddDomainRecordResponse):
            return True

        return self.to_dict() != other.to_dict()