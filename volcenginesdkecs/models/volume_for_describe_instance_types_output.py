# coding: utf-8

"""
    ecs

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class VolumeForDescribeInstanceTypesOutput(object):
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
        'supported_volume_types': 'list[str]'
    }

    attribute_map = {
        'supported_volume_types': 'SupportedVolumeTypes'
    }

    def __init__(self, supported_volume_types=None, _configuration=None):  # noqa: E501
        """VolumeForDescribeInstanceTypesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._supported_volume_types = None
        self.discriminator = None

        if supported_volume_types is not None:
            self.supported_volume_types = supported_volume_types

    @property
    def supported_volume_types(self):
        """Gets the supported_volume_types of this VolumeForDescribeInstanceTypesOutput.  # noqa: E501


        :return: The supported_volume_types of this VolumeForDescribeInstanceTypesOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._supported_volume_types

    @supported_volume_types.setter
    def supported_volume_types(self, supported_volume_types):
        """Sets the supported_volume_types of this VolumeForDescribeInstanceTypesOutput.


        :param supported_volume_types: The supported_volume_types of this VolumeForDescribeInstanceTypesOutput.  # noqa: E501
        :type: list[str]
        """

        self._supported_volume_types = supported_volume_types

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
        if issubclass(VolumeForDescribeInstanceTypesOutput, dict):
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
        if not isinstance(other, VolumeForDescribeInstanceTypesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VolumeForDescribeInstanceTypesOutput):
            return True

        return self.to_dict() != other.to_dict()
