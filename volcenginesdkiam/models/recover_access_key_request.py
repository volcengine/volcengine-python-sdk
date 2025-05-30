# coding: utf-8

"""
    iam

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class RecoverAccessKeyRequest(object):
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
        'access_key_id': 'str',
        'owner_type': 'str',
        'user_name': 'str'
    }

    attribute_map = {
        'access_key_id': 'AccessKeyId',
        'owner_type': 'OwnerType',
        'user_name': 'UserName'
    }

    def __init__(self, access_key_id=None, owner_type=None, user_name=None, _configuration=None):  # noqa: E501
        """RecoverAccessKeyRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._access_key_id = None
        self._owner_type = None
        self._user_name = None
        self.discriminator = None

        self.access_key_id = access_key_id
        self.owner_type = owner_type
        self.user_name = user_name

    @property
    def access_key_id(self):
        """Gets the access_key_id of this RecoverAccessKeyRequest.  # noqa: E501


        :return: The access_key_id of this RecoverAccessKeyRequest.  # noqa: E501
        :rtype: str
        """
        return self._access_key_id

    @access_key_id.setter
    def access_key_id(self, access_key_id):
        """Sets the access_key_id of this RecoverAccessKeyRequest.


        :param access_key_id: The access_key_id of this RecoverAccessKeyRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and access_key_id is None:
            raise ValueError("Invalid value for `access_key_id`, must not be `None`")  # noqa: E501

        self._access_key_id = access_key_id

    @property
    def owner_type(self):
        """Gets the owner_type of this RecoverAccessKeyRequest.  # noqa: E501


        :return: The owner_type of this RecoverAccessKeyRequest.  # noqa: E501
        :rtype: str
        """
        return self._owner_type

    @owner_type.setter
    def owner_type(self, owner_type):
        """Sets the owner_type of this RecoverAccessKeyRequest.


        :param owner_type: The owner_type of this RecoverAccessKeyRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and owner_type is None:
            raise ValueError("Invalid value for `owner_type`, must not be `None`")  # noqa: E501
        allowed_values = ["User", "Root"]  # noqa: E501
        if (self._configuration.client_side_validation and
                owner_type not in allowed_values):
            raise ValueError(
                "Invalid value for `owner_type` ({0}), must be one of {1}"  # noqa: E501
                .format(owner_type, allowed_values)
            )

        self._owner_type = owner_type

    @property
    def user_name(self):
        """Gets the user_name of this RecoverAccessKeyRequest.  # noqa: E501


        :return: The user_name of this RecoverAccessKeyRequest.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this RecoverAccessKeyRequest.


        :param user_name: The user_name of this RecoverAccessKeyRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and user_name is None:
            raise ValueError("Invalid value for `user_name`, must not be `None`")  # noqa: E501

        self._user_name = user_name

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
        if issubclass(RecoverAccessKeyRequest, dict):
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
        if not isinstance(other, RecoverAccessKeyRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RecoverAccessKeyRequest):
            return True

        return self.to_dict() != other.to_dict()
