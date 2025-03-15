# coding: utf-8

"""
    filenas

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DimensionForCreateDataFlowInput(object):
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
        'attr': 'str',
        'static_values': 'list[StaticValueForCreateDataFlowInput]'
    }

    attribute_map = {
        'attr': 'Attr',
        'static_values': 'StaticValues'
    }

    def __init__(self, attr=None, static_values=None, _configuration=None):  # noqa: E501
        """DimensionForCreateDataFlowInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._attr = None
        self._static_values = None
        self.discriminator = None

        if attr is not None:
            self.attr = attr
        if static_values is not None:
            self.static_values = static_values

    @property
    def attr(self):
        """Gets the attr of this DimensionForCreateDataFlowInput.  # noqa: E501


        :return: The attr of this DimensionForCreateDataFlowInput.  # noqa: E501
        :rtype: str
        """
        return self._attr

    @attr.setter
    def attr(self, attr):
        """Sets the attr of this DimensionForCreateDataFlowInput.


        :param attr: The attr of this DimensionForCreateDataFlowInput.  # noqa: E501
        :type: str
        """
        allowed_values = ["FileSize", "FileSuffix", "SubDirectory", "ModifyTime", "AccessTime"]  # noqa: E501
        if (self._configuration.client_side_validation and
                attr not in allowed_values):
            raise ValueError(
                "Invalid value for `attr` ({0}), must be one of {1}"  # noqa: E501
                .format(attr, allowed_values)
            )

        self._attr = attr

    @property
    def static_values(self):
        """Gets the static_values of this DimensionForCreateDataFlowInput.  # noqa: E501


        :return: The static_values of this DimensionForCreateDataFlowInput.  # noqa: E501
        :rtype: list[StaticValueForCreateDataFlowInput]
        """
        return self._static_values

    @static_values.setter
    def static_values(self, static_values):
        """Sets the static_values of this DimensionForCreateDataFlowInput.


        :param static_values: The static_values of this DimensionForCreateDataFlowInput.  # noqa: E501
        :type: list[StaticValueForCreateDataFlowInput]
        """

        self._static_values = static_values

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
        if issubclass(DimensionForCreateDataFlowInput, dict):
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
        if not isinstance(other, DimensionForCreateDataFlowInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DimensionForCreateDataFlowInput):
            return True

        return self.to_dict() != other.to_dict()
