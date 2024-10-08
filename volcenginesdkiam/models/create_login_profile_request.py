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


class CreateLoginProfileRequest(object):
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
        'login_allowed': 'bool',
        'password': 'str',
        'password_reset_required': 'bool',
        'safe_auth_exempt_duration': 'int',
        'safe_auth_exempt_required': 'int',
        'safe_auth_exempt_unit': 'int',
        'safe_auth_flag': 'bool',
        'safe_auth_type': 'str',
        'user_name': 'str'
    }

    attribute_map = {
        'login_allowed': 'LoginAllowed',
        'password': 'Password',
        'password_reset_required': 'PasswordResetRequired',
        'safe_auth_exempt_duration': 'SafeAuthExemptDuration',
        'safe_auth_exempt_required': 'SafeAuthExemptRequired',
        'safe_auth_exempt_unit': 'SafeAuthExemptUnit',
        'safe_auth_flag': 'SafeAuthFlag',
        'safe_auth_type': 'SafeAuthType',
        'user_name': 'UserName'
    }

    def __init__(self, login_allowed=None, password=None, password_reset_required=None, safe_auth_exempt_duration=None, safe_auth_exempt_required=None, safe_auth_exempt_unit=None, safe_auth_flag=None, safe_auth_type=None, user_name=None, _configuration=None):  # noqa: E501
        """CreateLoginProfileRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._login_allowed = None
        self._password = None
        self._password_reset_required = None
        self._safe_auth_exempt_duration = None
        self._safe_auth_exempt_required = None
        self._safe_auth_exempt_unit = None
        self._safe_auth_flag = None
        self._safe_auth_type = None
        self._user_name = None
        self.discriminator = None

        if login_allowed is not None:
            self.login_allowed = login_allowed
        self.password = password
        if password_reset_required is not None:
            self.password_reset_required = password_reset_required
        if safe_auth_exempt_duration is not None:
            self.safe_auth_exempt_duration = safe_auth_exempt_duration
        if safe_auth_exempt_required is not None:
            self.safe_auth_exempt_required = safe_auth_exempt_required
        if safe_auth_exempt_unit is not None:
            self.safe_auth_exempt_unit = safe_auth_exempt_unit
        if safe_auth_flag is not None:
            self.safe_auth_flag = safe_auth_flag
        if safe_auth_type is not None:
            self.safe_auth_type = safe_auth_type
        self.user_name = user_name

    @property
    def login_allowed(self):
        """Gets the login_allowed of this CreateLoginProfileRequest.  # noqa: E501


        :return: The login_allowed of this CreateLoginProfileRequest.  # noqa: E501
        :rtype: bool
        """
        return self._login_allowed

    @login_allowed.setter
    def login_allowed(self, login_allowed):
        """Sets the login_allowed of this CreateLoginProfileRequest.


        :param login_allowed: The login_allowed of this CreateLoginProfileRequest.  # noqa: E501
        :type: bool
        """

        self._login_allowed = login_allowed

    @property
    def password(self):
        """Gets the password of this CreateLoginProfileRequest.  # noqa: E501


        :return: The password of this CreateLoginProfileRequest.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this CreateLoginProfileRequest.


        :param password: The password of this CreateLoginProfileRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def password_reset_required(self):
        """Gets the password_reset_required of this CreateLoginProfileRequest.  # noqa: E501


        :return: The password_reset_required of this CreateLoginProfileRequest.  # noqa: E501
        :rtype: bool
        """
        return self._password_reset_required

    @password_reset_required.setter
    def password_reset_required(self, password_reset_required):
        """Sets the password_reset_required of this CreateLoginProfileRequest.


        :param password_reset_required: The password_reset_required of this CreateLoginProfileRequest.  # noqa: E501
        :type: bool
        """

        self._password_reset_required = password_reset_required

    @property
    def safe_auth_exempt_duration(self):
        """Gets the safe_auth_exempt_duration of this CreateLoginProfileRequest.  # noqa: E501


        :return: The safe_auth_exempt_duration of this CreateLoginProfileRequest.  # noqa: E501
        :rtype: int
        """
        return self._safe_auth_exempt_duration

    @safe_auth_exempt_duration.setter
    def safe_auth_exempt_duration(self, safe_auth_exempt_duration):
        """Sets the safe_auth_exempt_duration of this CreateLoginProfileRequest.


        :param safe_auth_exempt_duration: The safe_auth_exempt_duration of this CreateLoginProfileRequest.  # noqa: E501
        :type: int
        """

        self._safe_auth_exempt_duration = safe_auth_exempt_duration

    @property
    def safe_auth_exempt_required(self):
        """Gets the safe_auth_exempt_required of this CreateLoginProfileRequest.  # noqa: E501


        :return: The safe_auth_exempt_required of this CreateLoginProfileRequest.  # noqa: E501
        :rtype: int
        """
        return self._safe_auth_exempt_required

    @safe_auth_exempt_required.setter
    def safe_auth_exempt_required(self, safe_auth_exempt_required):
        """Sets the safe_auth_exempt_required of this CreateLoginProfileRequest.


        :param safe_auth_exempt_required: The safe_auth_exempt_required of this CreateLoginProfileRequest.  # noqa: E501
        :type: int
        """

        self._safe_auth_exempt_required = safe_auth_exempt_required

    @property
    def safe_auth_exempt_unit(self):
        """Gets the safe_auth_exempt_unit of this CreateLoginProfileRequest.  # noqa: E501


        :return: The safe_auth_exempt_unit of this CreateLoginProfileRequest.  # noqa: E501
        :rtype: int
        """
        return self._safe_auth_exempt_unit

    @safe_auth_exempt_unit.setter
    def safe_auth_exempt_unit(self, safe_auth_exempt_unit):
        """Sets the safe_auth_exempt_unit of this CreateLoginProfileRequest.


        :param safe_auth_exempt_unit: The safe_auth_exempt_unit of this CreateLoginProfileRequest.  # noqa: E501
        :type: int
        """

        self._safe_auth_exempt_unit = safe_auth_exempt_unit

    @property
    def safe_auth_flag(self):
        """Gets the safe_auth_flag of this CreateLoginProfileRequest.  # noqa: E501


        :return: The safe_auth_flag of this CreateLoginProfileRequest.  # noqa: E501
        :rtype: bool
        """
        return self._safe_auth_flag

    @safe_auth_flag.setter
    def safe_auth_flag(self, safe_auth_flag):
        """Sets the safe_auth_flag of this CreateLoginProfileRequest.


        :param safe_auth_flag: The safe_auth_flag of this CreateLoginProfileRequest.  # noqa: E501
        :type: bool
        """

        self._safe_auth_flag = safe_auth_flag

    @property
    def safe_auth_type(self):
        """Gets the safe_auth_type of this CreateLoginProfileRequest.  # noqa: E501


        :return: The safe_auth_type of this CreateLoginProfileRequest.  # noqa: E501
        :rtype: str
        """
        return self._safe_auth_type

    @safe_auth_type.setter
    def safe_auth_type(self, safe_auth_type):
        """Sets the safe_auth_type of this CreateLoginProfileRequest.


        :param safe_auth_type: The safe_auth_type of this CreateLoginProfileRequest.  # noqa: E501
        :type: str
        """

        self._safe_auth_type = safe_auth_type

    @property
    def user_name(self):
        """Gets the user_name of this CreateLoginProfileRequest.  # noqa: E501


        :return: The user_name of this CreateLoginProfileRequest.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this CreateLoginProfileRequest.


        :param user_name: The user_name of this CreateLoginProfileRequest.  # noqa: E501
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
        if issubclass(CreateLoginProfileRequest, dict):
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
        if not isinstance(other, CreateLoginProfileRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateLoginProfileRequest):
            return True

        return self.to_dict() != other.to_dict()
