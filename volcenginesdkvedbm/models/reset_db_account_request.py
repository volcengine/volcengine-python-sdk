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


class ResetDBAccountRequest(object):
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
        'account_password': 'str',
        'instance_id': 'str'
    }

    attribute_map = {
        'account_name': 'AccountName',
        'account_password': 'AccountPassword',
        'instance_id': 'InstanceId'
    }

    def __init__(self, account_name=None, account_password=None, instance_id=None, _configuration=None):  # noqa: E501
        """ResetDBAccountRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_name = None
        self._account_password = None
        self._instance_id = None
        self.discriminator = None

        self.account_name = account_name
        self.account_password = account_password
        self.instance_id = instance_id

    @property
    def account_name(self):
        """Gets the account_name of this ResetDBAccountRequest.  # noqa: E501


        :return: The account_name of this ResetDBAccountRequest.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this ResetDBAccountRequest.


        :param account_name: The account_name of this ResetDBAccountRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and account_name is None:
            raise ValueError("Invalid value for `account_name`, must not be `None`")  # noqa: E501

        self._account_name = account_name

    @property
    def account_password(self):
        """Gets the account_password of this ResetDBAccountRequest.  # noqa: E501


        :return: The account_password of this ResetDBAccountRequest.  # noqa: E501
        :rtype: str
        """
        return self._account_password

    @account_password.setter
    def account_password(self, account_password):
        """Sets the account_password of this ResetDBAccountRequest.


        :param account_password: The account_password of this ResetDBAccountRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and account_password is None:
            raise ValueError("Invalid value for `account_password`, must not be `None`")  # noqa: E501

        self._account_password = account_password

    @property
    def instance_id(self):
        """Gets the instance_id of this ResetDBAccountRequest.  # noqa: E501


        :return: The instance_id of this ResetDBAccountRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ResetDBAccountRequest.


        :param instance_id: The instance_id of this ResetDBAccountRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and instance_id is None:
            raise ValueError("Invalid value for `instance_id`, must not be `None`")  # noqa: E501

        self._instance_id = instance_id

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
        if issubclass(ResetDBAccountRequest, dict):
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
        if not isinstance(other, ResetDBAccountRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResetDBAccountRequest):
            return True

        return self.to_dict() != other.to_dict()
