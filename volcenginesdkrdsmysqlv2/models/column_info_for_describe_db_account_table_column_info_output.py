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


class ColumnInfoForDescribeDbAccountTableColumnInfoOutput(object):
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
        'account_privileges': 'list[str]',
        'column_name': 'str'
    }

    attribute_map = {
        'account_privileges': 'AccountPrivileges',
        'column_name': 'ColumnName'
    }

    def __init__(self, account_privileges=None, column_name=None, _configuration=None):  # noqa: E501
        """ColumnInfoForDescribeDbAccountTableColumnInfoOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_privileges = None
        self._column_name = None
        self.discriminator = None

        if account_privileges is not None:
            self.account_privileges = account_privileges
        if column_name is not None:
            self.column_name = column_name

    @property
    def account_privileges(self):
        """Gets the account_privileges of this ColumnInfoForDescribeDbAccountTableColumnInfoOutput.  # noqa: E501


        :return: The account_privileges of this ColumnInfoForDescribeDbAccountTableColumnInfoOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._account_privileges

    @account_privileges.setter
    def account_privileges(self, account_privileges):
        """Sets the account_privileges of this ColumnInfoForDescribeDbAccountTableColumnInfoOutput.


        :param account_privileges: The account_privileges of this ColumnInfoForDescribeDbAccountTableColumnInfoOutput.  # noqa: E501
        :type: list[str]
        """

        self._account_privileges = account_privileges

    @property
    def column_name(self):
        """Gets the column_name of this ColumnInfoForDescribeDbAccountTableColumnInfoOutput.  # noqa: E501


        :return: The column_name of this ColumnInfoForDescribeDbAccountTableColumnInfoOutput.  # noqa: E501
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        """Sets the column_name of this ColumnInfoForDescribeDbAccountTableColumnInfoOutput.


        :param column_name: The column_name of this ColumnInfoForDescribeDbAccountTableColumnInfoOutput.  # noqa: E501
        :type: str
        """

        self._column_name = column_name

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
        if issubclass(ColumnInfoForDescribeDbAccountTableColumnInfoOutput, dict):
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
        if not isinstance(other, ColumnInfoForDescribeDbAccountTableColumnInfoOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ColumnInfoForDescribeDbAccountTableColumnInfoOutput):
            return True

        return self.to_dict() != other.to_dict()
