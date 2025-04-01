# coding: utf-8

"""
    edx

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class GetDXPPortPriceRequest(object):
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
        'module_type': 'str'
    }

    attribute_map = {
        'module_type': 'ModuleType'
    }

    def __init__(self, module_type=None, _configuration=None):  # noqa: E501
        """GetDXPPortPriceRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._module_type = None
        self.discriminator = None

        self.module_type = module_type

    @property
    def module_type(self):
        """Gets the module_type of this GetDXPPortPriceRequest.  # noqa: E501


        :return: The module_type of this GetDXPPortPriceRequest.  # noqa: E501
        :rtype: str
        """
        return self._module_type

    @module_type.setter
    def module_type(self, module_type):
        """Sets the module_type of this GetDXPPortPriceRequest.


        :param module_type: The module_type of this GetDXPPortPriceRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and module_type is None:
            raise ValueError("Invalid value for `module_type`, must not be `None`")  # noqa: E501

        self._module_type = module_type

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
        if issubclass(GetDXPPortPriceRequest, dict):
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
        if not isinstance(other, GetDXPPortPriceRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetDXPPortPriceRequest):
            return True

        return self.to_dict() != other.to_dict()
