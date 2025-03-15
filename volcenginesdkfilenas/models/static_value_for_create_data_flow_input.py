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


class StaticValueForCreateDataFlowInput(object):
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
        'relationship': 'str',
        'unit': 'str',
        'value': 'str'
    }

    attribute_map = {
        'relationship': 'Relationship',
        'unit': 'Unit',
        'value': 'Value'
    }

    def __init__(self, relationship=None, unit=None, value=None, _configuration=None):  # noqa: E501
        """StaticValueForCreateDataFlowInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._relationship = None
        self._unit = None
        self._value = None
        self.discriminator = None

        if relationship is not None:
            self.relationship = relationship
        if unit is not None:
            self.unit = unit
        if value is not None:
            self.value = value

    @property
    def relationship(self):
        """Gets the relationship of this StaticValueForCreateDataFlowInput.  # noqa: E501


        :return: The relationship of this StaticValueForCreateDataFlowInput.  # noqa: E501
        :rtype: str
        """
        return self._relationship

    @relationship.setter
    def relationship(self, relationship):
        """Sets the relationship of this StaticValueForCreateDataFlowInput.


        :param relationship: The relationship of this StaticValueForCreateDataFlowInput.  # noqa: E501
        :type: str
        """
        allowed_values = ["GE", "CT", "NC"]  # noqa: E501
        if (self._configuration.client_side_validation and
                relationship not in allowed_values):
            raise ValueError(
                "Invalid value for `relationship` ({0}), must be one of {1}"  # noqa: E501
                .format(relationship, allowed_values)
            )

        self._relationship = relationship

    @property
    def unit(self):
        """Gets the unit of this StaticValueForCreateDataFlowInput.  # noqa: E501


        :return: The unit of this StaticValueForCreateDataFlowInput.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this StaticValueForCreateDataFlowInput.


        :param unit: The unit of this StaticValueForCreateDataFlowInput.  # noqa: E501
        :type: str
        """
        allowed_values = ["Hour", "Day", "Week", "Month", "Year"]  # noqa: E501
        if (self._configuration.client_side_validation and
                unit not in allowed_values):
            raise ValueError(
                "Invalid value for `unit` ({0}), must be one of {1}"  # noqa: E501
                .format(unit, allowed_values)
            )

        self._unit = unit

    @property
    def value(self):
        """Gets the value of this StaticValueForCreateDataFlowInput.  # noqa: E501


        :return: The value of this StaticValueForCreateDataFlowInput.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this StaticValueForCreateDataFlowInput.


        :param value: The value of this StaticValueForCreateDataFlowInput.  # noqa: E501
        :type: str
        """

        self._value = value

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
        if issubclass(StaticValueForCreateDataFlowInput, dict):
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
        if not isinstance(other, StaticValueForCreateDataFlowInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StaticValueForCreateDataFlowInput):
            return True

        return self.to_dict() != other.to_dict()
