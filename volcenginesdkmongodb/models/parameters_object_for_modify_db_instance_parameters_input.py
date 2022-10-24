# coding: utf-8

"""
    mongodb

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ParametersObjectForModifyDBInstanceParametersInput(object):
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
        'parameter_name': 'str',
        'parameter_role': 'str',
        'parameter_value': 'str'
    }

    attribute_map = {
        'parameter_name': 'ParameterName',
        'parameter_role': 'ParameterRole',
        'parameter_value': 'ParameterValue'
    }

    def __init__(self, parameter_name=None, parameter_role=None, parameter_value=None, _configuration=None):  # noqa: E501
        """ParametersObjectForModifyDBInstanceParametersInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._parameter_name = None
        self._parameter_role = None
        self._parameter_value = None
        self.discriminator = None

        if parameter_name is not None:
            self.parameter_name = parameter_name
        if parameter_role is not None:
            self.parameter_role = parameter_role
        if parameter_value is not None:
            self.parameter_value = parameter_value

    @property
    def parameter_name(self):
        """Gets the parameter_name of this ParametersObjectForModifyDBInstanceParametersInput.  # noqa: E501


        :return: The parameter_name of this ParametersObjectForModifyDBInstanceParametersInput.  # noqa: E501
        :rtype: str
        """
        return self._parameter_name

    @parameter_name.setter
    def parameter_name(self, parameter_name):
        """Sets the parameter_name of this ParametersObjectForModifyDBInstanceParametersInput.


        :param parameter_name: The parameter_name of this ParametersObjectForModifyDBInstanceParametersInput.  # noqa: E501
        :type: str
        """

        self._parameter_name = parameter_name

    @property
    def parameter_role(self):
        """Gets the parameter_role of this ParametersObjectForModifyDBInstanceParametersInput.  # noqa: E501


        :return: The parameter_role of this ParametersObjectForModifyDBInstanceParametersInput.  # noqa: E501
        :rtype: str
        """
        return self._parameter_role

    @parameter_role.setter
    def parameter_role(self, parameter_role):
        """Sets the parameter_role of this ParametersObjectForModifyDBInstanceParametersInput.


        :param parameter_role: The parameter_role of this ParametersObjectForModifyDBInstanceParametersInput.  # noqa: E501
        :type: str
        """
        allowed_values = ["ConfigServer", "Mongos", "Node", "Shard", "Unknown"]  # noqa: E501
        if (self._configuration.client_side_validation and
                parameter_role not in allowed_values):
            raise ValueError(
                "Invalid value for `parameter_role` ({0}), must be one of {1}"  # noqa: E501
                .format(parameter_role, allowed_values)
            )

        self._parameter_role = parameter_role

    @property
    def parameter_value(self):
        """Gets the parameter_value of this ParametersObjectForModifyDBInstanceParametersInput.  # noqa: E501


        :return: The parameter_value of this ParametersObjectForModifyDBInstanceParametersInput.  # noqa: E501
        :rtype: str
        """
        return self._parameter_value

    @parameter_value.setter
    def parameter_value(self, parameter_value):
        """Sets the parameter_value of this ParametersObjectForModifyDBInstanceParametersInput.


        :param parameter_value: The parameter_value of this ParametersObjectForModifyDBInstanceParametersInput.  # noqa: E501
        :type: str
        """

        self._parameter_value = parameter_value

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
        if issubclass(ParametersObjectForModifyDBInstanceParametersInput, dict):
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
        if not isinstance(other, ParametersObjectForModifyDBInstanceParametersInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ParametersObjectForModifyDBInstanceParametersInput):
            return True

        return self.to_dict() != other.to_dict()