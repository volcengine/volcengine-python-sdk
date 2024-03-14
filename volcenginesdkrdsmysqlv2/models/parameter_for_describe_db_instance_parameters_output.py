# coding: utf-8

"""
    rds_mysql_v2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ParameterForDescribeDBInstanceParametersOutput(object):
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
        'checking_code': 'str',
        'expression': 'str',
        'force_restart': 'bool',
        'parameter_default_value': 'str',
        'parameter_description': 'str',
        'parameter_name': 'str',
        'parameter_value': 'str'
    }

    attribute_map = {
        'checking_code': 'CheckingCode',
        'expression': 'Expression',
        'force_restart': 'ForceRestart',
        'parameter_default_value': 'ParameterDefaultValue',
        'parameter_description': 'ParameterDescription',
        'parameter_name': 'ParameterName',
        'parameter_value': 'ParameterValue'
    }

    def __init__(self, checking_code=None, expression=None, force_restart=None, parameter_default_value=None, parameter_description=None, parameter_name=None, parameter_value=None, _configuration=None):  # noqa: E501
        """ParameterForDescribeDBInstanceParametersOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._checking_code = None
        self._expression = None
        self._force_restart = None
        self._parameter_default_value = None
        self._parameter_description = None
        self._parameter_name = None
        self._parameter_value = None
        self.discriminator = None

        if checking_code is not None:
            self.checking_code = checking_code
        if expression is not None:
            self.expression = expression
        if force_restart is not None:
            self.force_restart = force_restart
        if parameter_default_value is not None:
            self.parameter_default_value = parameter_default_value
        if parameter_description is not None:
            self.parameter_description = parameter_description
        if parameter_name is not None:
            self.parameter_name = parameter_name
        if parameter_value is not None:
            self.parameter_value = parameter_value

    @property
    def checking_code(self):
        """Gets the checking_code of this ParameterForDescribeDBInstanceParametersOutput.  # noqa: E501


        :return: The checking_code of this ParameterForDescribeDBInstanceParametersOutput.  # noqa: E501
        :rtype: str
        """
        return self._checking_code

    @checking_code.setter
    def checking_code(self, checking_code):
        """Sets the checking_code of this ParameterForDescribeDBInstanceParametersOutput.


        :param checking_code: The checking_code of this ParameterForDescribeDBInstanceParametersOutput.  # noqa: E501
        :type: str
        """

        self._checking_code = checking_code

    @property
    def expression(self):
        """Gets the expression of this ParameterForDescribeDBInstanceParametersOutput.  # noqa: E501


        :return: The expression of this ParameterForDescribeDBInstanceParametersOutput.  # noqa: E501
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """Sets the expression of this ParameterForDescribeDBInstanceParametersOutput.


        :param expression: The expression of this ParameterForDescribeDBInstanceParametersOutput.  # noqa: E501
        :type: str
        """

        self._expression = expression

    @property
    def force_restart(self):
        """Gets the force_restart of this ParameterForDescribeDBInstanceParametersOutput.  # noqa: E501


        :return: The force_restart of this ParameterForDescribeDBInstanceParametersOutput.  # noqa: E501
        :rtype: bool
        """
        return self._force_restart

    @force_restart.setter
    def force_restart(self, force_restart):
        """Sets the force_restart of this ParameterForDescribeDBInstanceParametersOutput.


        :param force_restart: The force_restart of this ParameterForDescribeDBInstanceParametersOutput.  # noqa: E501
        :type: bool
        """

        self._force_restart = force_restart

    @property
    def parameter_default_value(self):
        """Gets the parameter_default_value of this ParameterForDescribeDBInstanceParametersOutput.  # noqa: E501


        :return: The parameter_default_value of this ParameterForDescribeDBInstanceParametersOutput.  # noqa: E501
        :rtype: str
        """
        return self._parameter_default_value

    @parameter_default_value.setter
    def parameter_default_value(self, parameter_default_value):
        """Sets the parameter_default_value of this ParameterForDescribeDBInstanceParametersOutput.


        :param parameter_default_value: The parameter_default_value of this ParameterForDescribeDBInstanceParametersOutput.  # noqa: E501
        :type: str
        """

        self._parameter_default_value = parameter_default_value

    @property
    def parameter_description(self):
        """Gets the parameter_description of this ParameterForDescribeDBInstanceParametersOutput.  # noqa: E501


        :return: The parameter_description of this ParameterForDescribeDBInstanceParametersOutput.  # noqa: E501
        :rtype: str
        """
        return self._parameter_description

    @parameter_description.setter
    def parameter_description(self, parameter_description):
        """Sets the parameter_description of this ParameterForDescribeDBInstanceParametersOutput.


        :param parameter_description: The parameter_description of this ParameterForDescribeDBInstanceParametersOutput.  # noqa: E501
        :type: str
        """

        self._parameter_description = parameter_description

    @property
    def parameter_name(self):
        """Gets the parameter_name of this ParameterForDescribeDBInstanceParametersOutput.  # noqa: E501


        :return: The parameter_name of this ParameterForDescribeDBInstanceParametersOutput.  # noqa: E501
        :rtype: str
        """
        return self._parameter_name

    @parameter_name.setter
    def parameter_name(self, parameter_name):
        """Sets the parameter_name of this ParameterForDescribeDBInstanceParametersOutput.


        :param parameter_name: The parameter_name of this ParameterForDescribeDBInstanceParametersOutput.  # noqa: E501
        :type: str
        """

        self._parameter_name = parameter_name

    @property
    def parameter_value(self):
        """Gets the parameter_value of this ParameterForDescribeDBInstanceParametersOutput.  # noqa: E501


        :return: The parameter_value of this ParameterForDescribeDBInstanceParametersOutput.  # noqa: E501
        :rtype: str
        """
        return self._parameter_value

    @parameter_value.setter
    def parameter_value(self, parameter_value):
        """Sets the parameter_value of this ParameterForDescribeDBInstanceParametersOutput.


        :param parameter_value: The parameter_value of this ParameterForDescribeDBInstanceParametersOutput.  # noqa: E501
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
        if issubclass(ParameterForDescribeDBInstanceParametersOutput, dict):
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
        if not isinstance(other, ParameterForDescribeDBInstanceParametersOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ParameterForDescribeDBInstanceParametersOutput):
            return True

        return self.to_dict() != other.to_dict()
