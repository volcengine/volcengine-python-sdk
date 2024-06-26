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


class GetSecurityConfigResponse(object):
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
        'safe_auth_close': 'int',
        'safe_auth_exempt_duration': 'int',
        'safe_auth_type': 'str',
        'user_id': 'int'
    }

    attribute_map = {
        'safe_auth_close': 'SafeAuthClose',
        'safe_auth_exempt_duration': 'SafeAuthExemptDuration',
        'safe_auth_type': 'SafeAuthType',
        'user_id': 'UserID'
    }

    def __init__(self, safe_auth_close=None, safe_auth_exempt_duration=None, safe_auth_type=None, user_id=None, _configuration=None):  # noqa: E501
        """GetSecurityConfigResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._safe_auth_close = None
        self._safe_auth_exempt_duration = None
        self._safe_auth_type = None
        self._user_id = None
        self.discriminator = None

        if safe_auth_close is not None:
            self.safe_auth_close = safe_auth_close
        if safe_auth_exempt_duration is not None:
            self.safe_auth_exempt_duration = safe_auth_exempt_duration
        if safe_auth_type is not None:
            self.safe_auth_type = safe_auth_type
        if user_id is not None:
            self.user_id = user_id

    @property
    def safe_auth_close(self):
        """Gets the safe_auth_close of this GetSecurityConfigResponse.  # noqa: E501


        :return: The safe_auth_close of this GetSecurityConfigResponse.  # noqa: E501
        :rtype: int
        """
        return self._safe_auth_close

    @safe_auth_close.setter
    def safe_auth_close(self, safe_auth_close):
        """Sets the safe_auth_close of this GetSecurityConfigResponse.


        :param safe_auth_close: The safe_auth_close of this GetSecurityConfigResponse.  # noqa: E501
        :type: int
        """

        self._safe_auth_close = safe_auth_close

    @property
    def safe_auth_exempt_duration(self):
        """Gets the safe_auth_exempt_duration of this GetSecurityConfigResponse.  # noqa: E501


        :return: The safe_auth_exempt_duration of this GetSecurityConfigResponse.  # noqa: E501
        :rtype: int
        """
        return self._safe_auth_exempt_duration

    @safe_auth_exempt_duration.setter
    def safe_auth_exempt_duration(self, safe_auth_exempt_duration):
        """Sets the safe_auth_exempt_duration of this GetSecurityConfigResponse.


        :param safe_auth_exempt_duration: The safe_auth_exempt_duration of this GetSecurityConfigResponse.  # noqa: E501
        :type: int
        """

        self._safe_auth_exempt_duration = safe_auth_exempt_duration

    @property
    def safe_auth_type(self):
        """Gets the safe_auth_type of this GetSecurityConfigResponse.  # noqa: E501


        :return: The safe_auth_type of this GetSecurityConfigResponse.  # noqa: E501
        :rtype: str
        """
        return self._safe_auth_type

    @safe_auth_type.setter
    def safe_auth_type(self, safe_auth_type):
        """Sets the safe_auth_type of this GetSecurityConfigResponse.


        :param safe_auth_type: The safe_auth_type of this GetSecurityConfigResponse.  # noqa: E501
        :type: str
        """

        self._safe_auth_type = safe_auth_type

    @property
    def user_id(self):
        """Gets the user_id of this GetSecurityConfigResponse.  # noqa: E501


        :return: The user_id of this GetSecurityConfigResponse.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this GetSecurityConfigResponse.


        :param user_id: The user_id of this GetSecurityConfigResponse.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

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
        if issubclass(GetSecurityConfigResponse, dict):
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
        if not isinstance(other, GetSecurityConfigResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetSecurityConfigResponse):
            return True

        return self.to_dict() != other.to_dict()
