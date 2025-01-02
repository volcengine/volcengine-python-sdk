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


class LoginProfileForGetLoginProfileOutput(object):
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
        'create_date': 'str',
        'last_login_date': 'str',
        'last_login_ip': 'str',
        'last_reset_password_time': 'int',
        'login_allowed': 'bool',
        'login_locked': 'bool',
        'password_expire_at': 'int',
        'password_reset_required': 'bool',
        'safe_auth_exempt_duration': 'int',
        'safe_auth_exempt_required': 'int',
        'safe_auth_exempt_unit': 'int',
        'safe_auth_flag': 'bool',
        'safe_auth_type': 'str',
        'update_date': 'str',
        'user_id': 'int',
        'user_name': 'str'
    }

    attribute_map = {
        'create_date': 'CreateDate',
        'last_login_date': 'LastLoginDate',
        'last_login_ip': 'LastLoginIp',
        'last_reset_password_time': 'LastResetPasswordTime',
        'login_allowed': 'LoginAllowed',
        'login_locked': 'LoginLocked',
        'password_expire_at': 'PasswordExpireAt',
        'password_reset_required': 'PasswordResetRequired',
        'safe_auth_exempt_duration': 'SafeAuthExemptDuration',
        'safe_auth_exempt_required': 'SafeAuthExemptRequired',
        'safe_auth_exempt_unit': 'SafeAuthExemptUnit',
        'safe_auth_flag': 'SafeAuthFlag',
        'safe_auth_type': 'SafeAuthType',
        'update_date': 'UpdateDate',
        'user_id': 'UserId',
        'user_name': 'UserName'
    }

    def __init__(self, create_date=None, last_login_date=None, last_login_ip=None, last_reset_password_time=None, login_allowed=None, login_locked=None, password_expire_at=None, password_reset_required=None, safe_auth_exempt_duration=None, safe_auth_exempt_required=None, safe_auth_exempt_unit=None, safe_auth_flag=None, safe_auth_type=None, update_date=None, user_id=None, user_name=None, _configuration=None):  # noqa: E501
        """LoginProfileForGetLoginProfileOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._create_date = None
        self._last_login_date = None
        self._last_login_ip = None
        self._last_reset_password_time = None
        self._login_allowed = None
        self._login_locked = None
        self._password_expire_at = None
        self._password_reset_required = None
        self._safe_auth_exempt_duration = None
        self._safe_auth_exempt_required = None
        self._safe_auth_exempt_unit = None
        self._safe_auth_flag = None
        self._safe_auth_type = None
        self._update_date = None
        self._user_id = None
        self._user_name = None
        self.discriminator = None

        if create_date is not None:
            self.create_date = create_date
        if last_login_date is not None:
            self.last_login_date = last_login_date
        if last_login_ip is not None:
            self.last_login_ip = last_login_ip
        if last_reset_password_time is not None:
            self.last_reset_password_time = last_reset_password_time
        if login_allowed is not None:
            self.login_allowed = login_allowed
        if login_locked is not None:
            self.login_locked = login_locked
        if password_expire_at is not None:
            self.password_expire_at = password_expire_at
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
        if update_date is not None:
            self.update_date = update_date
        if user_id is not None:
            self.user_id = user_id
        if user_name is not None:
            self.user_name = user_name

    @property
    def create_date(self):
        """Gets the create_date of this LoginProfileForGetLoginProfileOutput.  # noqa: E501


        :return: The create_date of this LoginProfileForGetLoginProfileOutput.  # noqa: E501
        :rtype: str
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this LoginProfileForGetLoginProfileOutput.


        :param create_date: The create_date of this LoginProfileForGetLoginProfileOutput.  # noqa: E501
        :type: str
        """

        self._create_date = create_date

    @property
    def last_login_date(self):
        """Gets the last_login_date of this LoginProfileForGetLoginProfileOutput.  # noqa: E501


        :return: The last_login_date of this LoginProfileForGetLoginProfileOutput.  # noqa: E501
        :rtype: str
        """
        return self._last_login_date

    @last_login_date.setter
    def last_login_date(self, last_login_date):
        """Sets the last_login_date of this LoginProfileForGetLoginProfileOutput.


        :param last_login_date: The last_login_date of this LoginProfileForGetLoginProfileOutput.  # noqa: E501
        :type: str
        """

        self._last_login_date = last_login_date

    @property
    def last_login_ip(self):
        """Gets the last_login_ip of this LoginProfileForGetLoginProfileOutput.  # noqa: E501


        :return: The last_login_ip of this LoginProfileForGetLoginProfileOutput.  # noqa: E501
        :rtype: str
        """
        return self._last_login_ip

    @last_login_ip.setter
    def last_login_ip(self, last_login_ip):
        """Sets the last_login_ip of this LoginProfileForGetLoginProfileOutput.


        :param last_login_ip: The last_login_ip of this LoginProfileForGetLoginProfileOutput.  # noqa: E501
        :type: str
        """

        self._last_login_ip = last_login_ip

    @property
    def last_reset_password_time(self):
        """Gets the last_reset_password_time of this LoginProfileForGetLoginProfileOutput.  # noqa: E501


        :return: The last_reset_password_time of this LoginProfileForGetLoginProfileOutput.  # noqa: E501
        :rtype: int
        """
        return self._last_reset_password_time

    @last_reset_password_time.setter
    def last_reset_password_time(self, last_reset_password_time):
        """Sets the last_reset_password_time of this LoginProfileForGetLoginProfileOutput.


        :param last_reset_password_time: The last_reset_password_time of this LoginProfileForGetLoginProfileOutput.  # noqa: E501
        :type: int
        """

        self._last_reset_password_time = last_reset_password_time

    @property
    def login_allowed(self):
        """Gets the login_allowed of this LoginProfileForGetLoginProfileOutput.  # noqa: E501


        :return: The login_allowed of this LoginProfileForGetLoginProfileOutput.  # noqa: E501
        :rtype: bool
        """
        return self._login_allowed

    @login_allowed.setter
    def login_allowed(self, login_allowed):
        """Sets the login_allowed of this LoginProfileForGetLoginProfileOutput.


        :param login_allowed: The login_allowed of this LoginProfileForGetLoginProfileOutput.  # noqa: E501
        :type: bool
        """

        self._login_allowed = login_allowed

    @property
    def login_locked(self):
        """Gets the login_locked of this LoginProfileForGetLoginProfileOutput.  # noqa: E501


        :return: The login_locked of this LoginProfileForGetLoginProfileOutput.  # noqa: E501
        :rtype: bool
        """
        return self._login_locked

    @login_locked.setter
    def login_locked(self, login_locked):
        """Sets the login_locked of this LoginProfileForGetLoginProfileOutput.


        :param login_locked: The login_locked of this LoginProfileForGetLoginProfileOutput.  # noqa: E501
        :type: bool
        """

        self._login_locked = login_locked

    @property
    def password_expire_at(self):
        """Gets the password_expire_at of this LoginProfileForGetLoginProfileOutput.  # noqa: E501


        :return: The password_expire_at of this LoginProfileForGetLoginProfileOutput.  # noqa: E501
        :rtype: int
        """
        return self._password_expire_at

    @password_expire_at.setter
    def password_expire_at(self, password_expire_at):
        """Sets the password_expire_at of this LoginProfileForGetLoginProfileOutput.


        :param password_expire_at: The password_expire_at of this LoginProfileForGetLoginProfileOutput.  # noqa: E501
        :type: int
        """

        self._password_expire_at = password_expire_at

    @property
    def password_reset_required(self):
        """Gets the password_reset_required of this LoginProfileForGetLoginProfileOutput.  # noqa: E501


        :return: The password_reset_required of this LoginProfileForGetLoginProfileOutput.  # noqa: E501
        :rtype: bool
        """
        return self._password_reset_required

    @password_reset_required.setter
    def password_reset_required(self, password_reset_required):
        """Sets the password_reset_required of this LoginProfileForGetLoginProfileOutput.


        :param password_reset_required: The password_reset_required of this LoginProfileForGetLoginProfileOutput.  # noqa: E501
        :type: bool
        """

        self._password_reset_required = password_reset_required

    @property
    def safe_auth_exempt_duration(self):
        """Gets the safe_auth_exempt_duration of this LoginProfileForGetLoginProfileOutput.  # noqa: E501


        :return: The safe_auth_exempt_duration of this LoginProfileForGetLoginProfileOutput.  # noqa: E501
        :rtype: int
        """
        return self._safe_auth_exempt_duration

    @safe_auth_exempt_duration.setter
    def safe_auth_exempt_duration(self, safe_auth_exempt_duration):
        """Sets the safe_auth_exempt_duration of this LoginProfileForGetLoginProfileOutput.


        :param safe_auth_exempt_duration: The safe_auth_exempt_duration of this LoginProfileForGetLoginProfileOutput.  # noqa: E501
        :type: int
        """

        self._safe_auth_exempt_duration = safe_auth_exempt_duration

    @property
    def safe_auth_exempt_required(self):
        """Gets the safe_auth_exempt_required of this LoginProfileForGetLoginProfileOutput.  # noqa: E501


        :return: The safe_auth_exempt_required of this LoginProfileForGetLoginProfileOutput.  # noqa: E501
        :rtype: int
        """
        return self._safe_auth_exempt_required

    @safe_auth_exempt_required.setter
    def safe_auth_exempt_required(self, safe_auth_exempt_required):
        """Sets the safe_auth_exempt_required of this LoginProfileForGetLoginProfileOutput.


        :param safe_auth_exempt_required: The safe_auth_exempt_required of this LoginProfileForGetLoginProfileOutput.  # noqa: E501
        :type: int
        """

        self._safe_auth_exempt_required = safe_auth_exempt_required

    @property
    def safe_auth_exempt_unit(self):
        """Gets the safe_auth_exempt_unit of this LoginProfileForGetLoginProfileOutput.  # noqa: E501


        :return: The safe_auth_exempt_unit of this LoginProfileForGetLoginProfileOutput.  # noqa: E501
        :rtype: int
        """
        return self._safe_auth_exempt_unit

    @safe_auth_exempt_unit.setter
    def safe_auth_exempt_unit(self, safe_auth_exempt_unit):
        """Sets the safe_auth_exempt_unit of this LoginProfileForGetLoginProfileOutput.


        :param safe_auth_exempt_unit: The safe_auth_exempt_unit of this LoginProfileForGetLoginProfileOutput.  # noqa: E501
        :type: int
        """

        self._safe_auth_exempt_unit = safe_auth_exempt_unit

    @property
    def safe_auth_flag(self):
        """Gets the safe_auth_flag of this LoginProfileForGetLoginProfileOutput.  # noqa: E501


        :return: The safe_auth_flag of this LoginProfileForGetLoginProfileOutput.  # noqa: E501
        :rtype: bool
        """
        return self._safe_auth_flag

    @safe_auth_flag.setter
    def safe_auth_flag(self, safe_auth_flag):
        """Sets the safe_auth_flag of this LoginProfileForGetLoginProfileOutput.


        :param safe_auth_flag: The safe_auth_flag of this LoginProfileForGetLoginProfileOutput.  # noqa: E501
        :type: bool
        """

        self._safe_auth_flag = safe_auth_flag

    @property
    def safe_auth_type(self):
        """Gets the safe_auth_type of this LoginProfileForGetLoginProfileOutput.  # noqa: E501


        :return: The safe_auth_type of this LoginProfileForGetLoginProfileOutput.  # noqa: E501
        :rtype: str
        """
        return self._safe_auth_type

    @safe_auth_type.setter
    def safe_auth_type(self, safe_auth_type):
        """Sets the safe_auth_type of this LoginProfileForGetLoginProfileOutput.


        :param safe_auth_type: The safe_auth_type of this LoginProfileForGetLoginProfileOutput.  # noqa: E501
        :type: str
        """

        self._safe_auth_type = safe_auth_type

    @property
    def update_date(self):
        """Gets the update_date of this LoginProfileForGetLoginProfileOutput.  # noqa: E501


        :return: The update_date of this LoginProfileForGetLoginProfileOutput.  # noqa: E501
        :rtype: str
        """
        return self._update_date

    @update_date.setter
    def update_date(self, update_date):
        """Sets the update_date of this LoginProfileForGetLoginProfileOutput.


        :param update_date: The update_date of this LoginProfileForGetLoginProfileOutput.  # noqa: E501
        :type: str
        """

        self._update_date = update_date

    @property
    def user_id(self):
        """Gets the user_id of this LoginProfileForGetLoginProfileOutput.  # noqa: E501


        :return: The user_id of this LoginProfileForGetLoginProfileOutput.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this LoginProfileForGetLoginProfileOutput.


        :param user_id: The user_id of this LoginProfileForGetLoginProfileOutput.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def user_name(self):
        """Gets the user_name of this LoginProfileForGetLoginProfileOutput.  # noqa: E501


        :return: The user_name of this LoginProfileForGetLoginProfileOutput.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this LoginProfileForGetLoginProfileOutput.


        :param user_name: The user_name of this LoginProfileForGetLoginProfileOutput.  # noqa: E501
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
        if issubclass(LoginProfileForGetLoginProfileOutput, dict):
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
        if not isinstance(other, LoginProfileForGetLoginProfileOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LoginProfileForGetLoginProfileOutput):
            return True

        return self.to_dict() != other.to_dict()
