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


class UpdateAccessKeyRequest(object):
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
        'status': 'str',
        'user_name': 'str'
    }

    attribute_map = {
        'access_key_id': 'AccessKeyId',
        'status': 'Status',
        'user_name': 'UserName'
    }

    def __init__(self, access_key_id=None, status=None, user_name=None, _configuration=None):  # noqa: E501
        """UpdateAccessKeyRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._access_key_id = None
        self._status = None
        self._user_name = None
        self.discriminator = None

        self.access_key_id = access_key_id
        self.status = status
        if user_name is not None:
            self.user_name = user_name

    @property
    def access_key_id(self):
        """Gets the access_key_id of this UpdateAccessKeyRequest.  # noqa: E501


        :return: The access_key_id of this UpdateAccessKeyRequest.  # noqa: E501
        :rtype: str
        """
        return self._access_key_id

    @access_key_id.setter
    def access_key_id(self, access_key_id):
        """Sets the access_key_id of this UpdateAccessKeyRequest.


        :param access_key_id: The access_key_id of this UpdateAccessKeyRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and access_key_id is None:
            raise ValueError("Invalid value for `access_key_id`, must not be `None`")  # noqa: E501

        self._access_key_id = access_key_id

    @property
    def status(self):
        """Gets the status of this UpdateAccessKeyRequest.  # noqa: E501


        :return: The status of this UpdateAccessKeyRequest.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateAccessKeyRequest.


        :param status: The status of this UpdateAccessKeyRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def user_name(self):
        """Gets the user_name of this UpdateAccessKeyRequest.  # noqa: E501


        :return: The user_name of this UpdateAccessKeyRequest.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this UpdateAccessKeyRequest.


        :param user_name: The user_name of this UpdateAccessKeyRequest.  # noqa: E501
        :type: str
        """

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
        if issubclass(UpdateAccessKeyRequest, dict):
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
        if not isinstance(other, UpdateAccessKeyRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateAccessKeyRequest):
            return True

        return self.to_dict() != other.to_dict()
