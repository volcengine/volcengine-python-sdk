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


class APIForCreateDomainOutput(object):
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
        'api_enable': 'int',
        'enable_auto_learning': 'int'
    }

    attribute_map = {
        'api_enable': 'ApiEnable',
        'enable_auto_learning': 'EnableAutoLearning'
    }

    def __init__(self, api_enable=None, enable_auto_learning=None, _configuration=None):  # noqa: E501
        """APIForCreateDomainOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._api_enable = None
        self._enable_auto_learning = None
        self.discriminator = None

        if api_enable is not None:
            self.api_enable = api_enable
        if enable_auto_learning is not None:
            self.enable_auto_learning = enable_auto_learning

    @property
    def api_enable(self):
        """Gets the api_enable of this APIForCreateDomainOutput.  # noqa: E501


        :return: The api_enable of this APIForCreateDomainOutput.  # noqa: E501
        :rtype: int
        """
        return self._api_enable

    @api_enable.setter
    def api_enable(self, api_enable):
        """Sets the api_enable of this APIForCreateDomainOutput.


        :param api_enable: The api_enable of this APIForCreateDomainOutput.  # noqa: E501
        :type: int
        """

        self._api_enable = api_enable

    @property
    def enable_auto_learning(self):
        """Gets the enable_auto_learning of this APIForCreateDomainOutput.  # noqa: E501


        :return: The enable_auto_learning of this APIForCreateDomainOutput.  # noqa: E501
        :rtype: int
        """
        return self._enable_auto_learning

    @enable_auto_learning.setter
    def enable_auto_learning(self, enable_auto_learning):
        """Sets the enable_auto_learning of this APIForCreateDomainOutput.


        :param enable_auto_learning: The enable_auto_learning of this APIForCreateDomainOutput.  # noqa: E501
        :type: int
        """

        self._enable_auto_learning = enable_auto_learning

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
        if issubclass(APIForCreateDomainOutput, dict):
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
        if not isinstance(other, APIForCreateDomainOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, APIForCreateDomainOutput):
            return True

        return self.to_dict() != other.to_dict()
