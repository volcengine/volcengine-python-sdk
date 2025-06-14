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


class DatabasesPrivilegeForCreateDatabaseInput(object):
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
        'account_name': 'str',
        'account_privilege': 'str',
        'account_privilege_detail': 'str'
    }

    attribute_map = {
        'account_name': 'AccountName',
        'account_privilege': 'AccountPrivilege',
        'account_privilege_detail': 'AccountPrivilegeDetail'
    }

    def __init__(self, account_name=None, account_privilege=None, account_privilege_detail=None, _configuration=None):  # noqa: E501
        """DatabasesPrivilegeForCreateDatabaseInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_name = None
        self._account_privilege = None
        self._account_privilege_detail = None
        self.discriminator = None

        if account_name is not None:
            self.account_name = account_name
        if account_privilege is not None:
            self.account_privilege = account_privilege
        if account_privilege_detail is not None:
            self.account_privilege_detail = account_privilege_detail

    @property
    def account_name(self):
        """Gets the account_name of this DatabasesPrivilegeForCreateDatabaseInput.  # noqa: E501


        :return: The account_name of this DatabasesPrivilegeForCreateDatabaseInput.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this DatabasesPrivilegeForCreateDatabaseInput.


        :param account_name: The account_name of this DatabasesPrivilegeForCreateDatabaseInput.  # noqa: E501
        :type: str
        """

        self._account_name = account_name

    @property
    def account_privilege(self):
        """Gets the account_privilege of this DatabasesPrivilegeForCreateDatabaseInput.  # noqa: E501


        :return: The account_privilege of this DatabasesPrivilegeForCreateDatabaseInput.  # noqa: E501
        :rtype: str
        """
        return self._account_privilege

    @account_privilege.setter
    def account_privilege(self, account_privilege):
        """Sets the account_privilege of this DatabasesPrivilegeForCreateDatabaseInput.


        :param account_privilege: The account_privilege of this DatabasesPrivilegeForCreateDatabaseInput.  # noqa: E501
        :type: str
        """
        allowed_values = ["Custom", "DDLOnly", "DMLOnly", "ReadOnly", "ReadWrite"]  # noqa: E501
        if (self._configuration.client_side_validation and
                account_privilege not in allowed_values):
            raise ValueError(
                "Invalid value for `account_privilege` ({0}), must be one of {1}"  # noqa: E501
                .format(account_privilege, allowed_values)
            )

        self._account_privilege = account_privilege

    @property
    def account_privilege_detail(self):
        """Gets the account_privilege_detail of this DatabasesPrivilegeForCreateDatabaseInput.  # noqa: E501


        :return: The account_privilege_detail of this DatabasesPrivilegeForCreateDatabaseInput.  # noqa: E501
        :rtype: str
        """
        return self._account_privilege_detail

    @account_privilege_detail.setter
    def account_privilege_detail(self, account_privilege_detail):
        """Sets the account_privilege_detail of this DatabasesPrivilegeForCreateDatabaseInput.


        :param account_privilege_detail: The account_privilege_detail of this DatabasesPrivilegeForCreateDatabaseInput.  # noqa: E501
        :type: str
        """

        self._account_privilege_detail = account_privilege_detail

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
        if issubclass(DatabasesPrivilegeForCreateDatabaseInput, dict):
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
        if not isinstance(other, DatabasesPrivilegeForCreateDatabaseInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DatabasesPrivilegeForCreateDatabaseInput):
            return True

        return self.to_dict() != other.to_dict()
