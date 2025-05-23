# coding: utf-8

"""
    redis

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class AccountForListDBAccountOutput(object):
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
        'account_status': 'str',
        'description': 'str',
        'instance_id': 'str',
        'role_name': 'str'
    }

    attribute_map = {
        'account_name': 'AccountName',
        'account_status': 'AccountStatus',
        'description': 'Description',
        'instance_id': 'InstanceId',
        'role_name': 'RoleName'
    }

    def __init__(self, account_name=None, account_status=None, description=None, instance_id=None, role_name=None, _configuration=None):  # noqa: E501
        """AccountForListDBAccountOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_name = None
        self._account_status = None
        self._description = None
        self._instance_id = None
        self._role_name = None
        self.discriminator = None

        if account_name is not None:
            self.account_name = account_name
        if account_status is not None:
            self.account_status = account_status
        if description is not None:
            self.description = description
        if instance_id is not None:
            self.instance_id = instance_id
        if role_name is not None:
            self.role_name = role_name

    @property
    def account_name(self):
        """Gets the account_name of this AccountForListDBAccountOutput.  # noqa: E501


        :return: The account_name of this AccountForListDBAccountOutput.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this AccountForListDBAccountOutput.


        :param account_name: The account_name of this AccountForListDBAccountOutput.  # noqa: E501
        :type: str
        """

        self._account_name = account_name

    @property
    def account_status(self):
        """Gets the account_status of this AccountForListDBAccountOutput.  # noqa: E501


        :return: The account_status of this AccountForListDBAccountOutput.  # noqa: E501
        :rtype: str
        """
        return self._account_status

    @account_status.setter
    def account_status(self, account_status):
        """Sets the account_status of this AccountForListDBAccountOutput.


        :param account_status: The account_status of this AccountForListDBAccountOutput.  # noqa: E501
        :type: str
        """

        self._account_status = account_status

    @property
    def description(self):
        """Gets the description of this AccountForListDBAccountOutput.  # noqa: E501


        :return: The description of this AccountForListDBAccountOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AccountForListDBAccountOutput.


        :param description: The description of this AccountForListDBAccountOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def instance_id(self):
        """Gets the instance_id of this AccountForListDBAccountOutput.  # noqa: E501


        :return: The instance_id of this AccountForListDBAccountOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this AccountForListDBAccountOutput.


        :param instance_id: The instance_id of this AccountForListDBAccountOutput.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def role_name(self):
        """Gets the role_name of this AccountForListDBAccountOutput.  # noqa: E501


        :return: The role_name of this AccountForListDBAccountOutput.  # noqa: E501
        :rtype: str
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        """Sets the role_name of this AccountForListDBAccountOutput.


        :param role_name: The role_name of this AccountForListDBAccountOutput.  # noqa: E501
        :type: str
        """

        self._role_name = role_name

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
        if issubclass(AccountForListDBAccountOutput, dict):
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
        if not isinstance(other, AccountForListDBAccountOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountForListDBAccountOutput):
            return True

        return self.to_dict() != other.to_dict()
