# coding: utf-8

"""
    cdn

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class SignCapRuleForDescribeCdnConfigOutput(object):
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
        'cap_mode': 'str',
        'param_name': 'str',
        'uri_level': 'int'
    }

    attribute_map = {
        'cap_mode': 'CapMode',
        'param_name': 'ParamName',
        'uri_level': 'UriLevel'
    }

    def __init__(self, cap_mode=None, param_name=None, uri_level=None, _configuration=None):  # noqa: E501
        """SignCapRuleForDescribeCdnConfigOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cap_mode = None
        self._param_name = None
        self._uri_level = None
        self.discriminator = None

        if cap_mode is not None:
            self.cap_mode = cap_mode
        if param_name is not None:
            self.param_name = param_name
        if uri_level is not None:
            self.uri_level = uri_level

    @property
    def cap_mode(self):
        """Gets the cap_mode of this SignCapRuleForDescribeCdnConfigOutput.  # noqa: E501


        :return: The cap_mode of this SignCapRuleForDescribeCdnConfigOutput.  # noqa: E501
        :rtype: str
        """
        return self._cap_mode

    @cap_mode.setter
    def cap_mode(self, cap_mode):
        """Sets the cap_mode of this SignCapRuleForDescribeCdnConfigOutput.


        :param cap_mode: The cap_mode of this SignCapRuleForDescribeCdnConfigOutput.  # noqa: E501
        :type: str
        """

        self._cap_mode = cap_mode

    @property
    def param_name(self):
        """Gets the param_name of this SignCapRuleForDescribeCdnConfigOutput.  # noqa: E501


        :return: The param_name of this SignCapRuleForDescribeCdnConfigOutput.  # noqa: E501
        :rtype: str
        """
        return self._param_name

    @param_name.setter
    def param_name(self, param_name):
        """Sets the param_name of this SignCapRuleForDescribeCdnConfigOutput.


        :param param_name: The param_name of this SignCapRuleForDescribeCdnConfigOutput.  # noqa: E501
        :type: str
        """

        self._param_name = param_name

    @property
    def uri_level(self):
        """Gets the uri_level of this SignCapRuleForDescribeCdnConfigOutput.  # noqa: E501


        :return: The uri_level of this SignCapRuleForDescribeCdnConfigOutput.  # noqa: E501
        :rtype: int
        """
        return self._uri_level

    @uri_level.setter
    def uri_level(self, uri_level):
        """Sets the uri_level of this SignCapRuleForDescribeCdnConfigOutput.


        :param uri_level: The uri_level of this SignCapRuleForDescribeCdnConfigOutput.  # noqa: E501
        :type: int
        """

        self._uri_level = uri_level

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
        if issubclass(SignCapRuleForDescribeCdnConfigOutput, dict):
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
        if not isinstance(other, SignCapRuleForDescribeCdnConfigOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SignCapRuleForDescribeCdnConfigOutput):
            return True

        return self.to_dict() != other.to_dict()
