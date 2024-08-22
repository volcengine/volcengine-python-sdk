# coding: utf-8

"""
    vedbm

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class AccountPrivilegeForDescribeDBAccountsOutput(object):
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
        'account_privilege': 'str',
        'account_privilege_detail': 'str',
        'db_name': 'str'
    }

    attribute_map = {
        'account_privilege': 'AccountPrivilege',
        'account_privilege_detail': 'AccountPrivilegeDetail',
        'db_name': 'DBName'
    }

    def __init__(self, account_privilege=None, account_privilege_detail=None, db_name=None, _configuration=None):  # noqa: E501
        """AccountPrivilegeForDescribeDBAccountsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_privilege = None
        self._account_privilege_detail = None
        self._db_name = None
        self.discriminator = None

        if account_privilege is not None:
            self.account_privilege = account_privilege
        if account_privilege_detail is not None:
            self.account_privilege_detail = account_privilege_detail
        if db_name is not None:
            self.db_name = db_name

    @property
    def account_privilege(self):
        """Gets the account_privilege of this AccountPrivilegeForDescribeDBAccountsOutput.  # noqa: E501


        :return: The account_privilege of this AccountPrivilegeForDescribeDBAccountsOutput.  # noqa: E501
        :rtype: str
        """
        return self._account_privilege

    @account_privilege.setter
    def account_privilege(self, account_privilege):
        """Sets the account_privilege of this AccountPrivilegeForDescribeDBAccountsOutput.


        :param account_privilege: The account_privilege of this AccountPrivilegeForDescribeDBAccountsOutput.  # noqa: E501
        :type: str
        """

        self._account_privilege = account_privilege

    @property
    def account_privilege_detail(self):
        """Gets the account_privilege_detail of this AccountPrivilegeForDescribeDBAccountsOutput.  # noqa: E501


        :return: The account_privilege_detail of this AccountPrivilegeForDescribeDBAccountsOutput.  # noqa: E501
        :rtype: str
        """
        return self._account_privilege_detail

    @account_privilege_detail.setter
    def account_privilege_detail(self, account_privilege_detail):
        """Sets the account_privilege_detail of this AccountPrivilegeForDescribeDBAccountsOutput.


        :param account_privilege_detail: The account_privilege_detail of this AccountPrivilegeForDescribeDBAccountsOutput.  # noqa: E501
        :type: str
        """

        self._account_privilege_detail = account_privilege_detail

    @property
    def db_name(self):
        """Gets the db_name of this AccountPrivilegeForDescribeDBAccountsOutput.  # noqa: E501


        :return: The db_name of this AccountPrivilegeForDescribeDBAccountsOutput.  # noqa: E501
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """Sets the db_name of this AccountPrivilegeForDescribeDBAccountsOutput.


        :param db_name: The db_name of this AccountPrivilegeForDescribeDBAccountsOutput.  # noqa: E501
        :type: str
        """

        self._db_name = db_name

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
        if issubclass(AccountPrivilegeForDescribeDBAccountsOutput, dict):
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
        if not isinstance(other, AccountPrivilegeForDescribeDBAccountsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountPrivilegeForDescribeDBAccountsOutput):
            return True

        return self.to_dict() != other.to_dict()
