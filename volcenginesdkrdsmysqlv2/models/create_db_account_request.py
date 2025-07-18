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


class CreateDBAccountRequest(object):
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
        'account_desc': 'str',
        'account_name': 'str',
        'account_password': 'str',
        'account_privileges': 'list[AccountPrivilegeForCreateDBAccountInput]',
        'account_type': 'str',
        'dry_run': 'bool',
        'host': 'str',
        'instance_id': 'str',
        'table_column_privileges': 'list[TableColumnPrivilegeForCreateDBAccountInput]'
    }

    attribute_map = {
        'account_desc': 'AccountDesc',
        'account_name': 'AccountName',
        'account_password': 'AccountPassword',
        'account_privileges': 'AccountPrivileges',
        'account_type': 'AccountType',
        'dry_run': 'DryRun',
        'host': 'Host',
        'instance_id': 'InstanceId',
        'table_column_privileges': 'TableColumnPrivileges'
    }

    def __init__(self, account_desc=None, account_name=None, account_password=None, account_privileges=None, account_type=None, dry_run=None, host=None, instance_id=None, table_column_privileges=None, _configuration=None):  # noqa: E501
        """CreateDBAccountRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_desc = None
        self._account_name = None
        self._account_password = None
        self._account_privileges = None
        self._account_type = None
        self._dry_run = None
        self._host = None
        self._instance_id = None
        self._table_column_privileges = None
        self.discriminator = None

        if account_desc is not None:
            self.account_desc = account_desc
        self.account_name = account_name
        self.account_password = account_password
        if account_privileges is not None:
            self.account_privileges = account_privileges
        self.account_type = account_type
        if dry_run is not None:
            self.dry_run = dry_run
        if host is not None:
            self.host = host
        self.instance_id = instance_id
        if table_column_privileges is not None:
            self.table_column_privileges = table_column_privileges

    @property
    def account_desc(self):
        """Gets the account_desc of this CreateDBAccountRequest.  # noqa: E501


        :return: The account_desc of this CreateDBAccountRequest.  # noqa: E501
        :rtype: str
        """
        return self._account_desc

    @account_desc.setter
    def account_desc(self, account_desc):
        """Sets the account_desc of this CreateDBAccountRequest.


        :param account_desc: The account_desc of this CreateDBAccountRequest.  # noqa: E501
        :type: str
        """

        self._account_desc = account_desc

    @property
    def account_name(self):
        """Gets the account_name of this CreateDBAccountRequest.  # noqa: E501


        :return: The account_name of this CreateDBAccountRequest.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this CreateDBAccountRequest.


        :param account_name: The account_name of this CreateDBAccountRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and account_name is None:
            raise ValueError("Invalid value for `account_name`, must not be `None`")  # noqa: E501

        self._account_name = account_name

    @property
    def account_password(self):
        """Gets the account_password of this CreateDBAccountRequest.  # noqa: E501


        :return: The account_password of this CreateDBAccountRequest.  # noqa: E501
        :rtype: str
        """
        return self._account_password

    @account_password.setter
    def account_password(self, account_password):
        """Sets the account_password of this CreateDBAccountRequest.


        :param account_password: The account_password of this CreateDBAccountRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and account_password is None:
            raise ValueError("Invalid value for `account_password`, must not be `None`")  # noqa: E501

        self._account_password = account_password

    @property
    def account_privileges(self):
        """Gets the account_privileges of this CreateDBAccountRequest.  # noqa: E501


        :return: The account_privileges of this CreateDBAccountRequest.  # noqa: E501
        :rtype: list[AccountPrivilegeForCreateDBAccountInput]
        """
        return self._account_privileges

    @account_privileges.setter
    def account_privileges(self, account_privileges):
        """Sets the account_privileges of this CreateDBAccountRequest.


        :param account_privileges: The account_privileges of this CreateDBAccountRequest.  # noqa: E501
        :type: list[AccountPrivilegeForCreateDBAccountInput]
        """

        self._account_privileges = account_privileges

    @property
    def account_type(self):
        """Gets the account_type of this CreateDBAccountRequest.  # noqa: E501


        :return: The account_type of this CreateDBAccountRequest.  # noqa: E501
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """Sets the account_type of this CreateDBAccountRequest.


        :param account_type: The account_type of this CreateDBAccountRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and account_type is None:
            raise ValueError("Invalid value for `account_type`, must not be `None`")  # noqa: E501

        self._account_type = account_type

    @property
    def dry_run(self):
        """Gets the dry_run of this CreateDBAccountRequest.  # noqa: E501


        :return: The dry_run of this CreateDBAccountRequest.  # noqa: E501
        :rtype: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        """Sets the dry_run of this CreateDBAccountRequest.


        :param dry_run: The dry_run of this CreateDBAccountRequest.  # noqa: E501
        :type: bool
        """

        self._dry_run = dry_run

    @property
    def host(self):
        """Gets the host of this CreateDBAccountRequest.  # noqa: E501


        :return: The host of this CreateDBAccountRequest.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this CreateDBAccountRequest.


        :param host: The host of this CreateDBAccountRequest.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def instance_id(self):
        """Gets the instance_id of this CreateDBAccountRequest.  # noqa: E501


        :return: The instance_id of this CreateDBAccountRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this CreateDBAccountRequest.


        :param instance_id: The instance_id of this CreateDBAccountRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and instance_id is None:
            raise ValueError("Invalid value for `instance_id`, must not be `None`")  # noqa: E501

        self._instance_id = instance_id

    @property
    def table_column_privileges(self):
        """Gets the table_column_privileges of this CreateDBAccountRequest.  # noqa: E501


        :return: The table_column_privileges of this CreateDBAccountRequest.  # noqa: E501
        :rtype: list[TableColumnPrivilegeForCreateDBAccountInput]
        """
        return self._table_column_privileges

    @table_column_privileges.setter
    def table_column_privileges(self, table_column_privileges):
        """Sets the table_column_privileges of this CreateDBAccountRequest.


        :param table_column_privileges: The table_column_privileges of this CreateDBAccountRequest.  # noqa: E501
        :type: list[TableColumnPrivilegeForCreateDBAccountInput]
        """

        self._table_column_privileges = table_column_privileges

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
        if issubclass(CreateDBAccountRequest, dict):
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
        if not isinstance(other, CreateDBAccountRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateDBAccountRequest):
            return True

        return self.to_dict() != other.to_dict()
