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


class DescribeBackupPlanResponse(object):
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
        'active': 'bool',
        'backup_hour': 'int',
        'backup_type': 'str',
        'expect_next_backup_time': 'str',
        'instance_id': 'str',
        'last_update_time': 'str',
        'period': 'list[int]',
        'ttl': 'int'
    }

    attribute_map = {
        'active': 'Active',
        'backup_hour': 'BackupHour',
        'backup_type': 'BackupType',
        'expect_next_backup_time': 'ExpectNextBackupTime',
        'instance_id': 'InstanceId',
        'last_update_time': 'LastUpdateTime',
        'period': 'Period',
        'ttl': 'TTL'
    }

    def __init__(self, active=None, backup_hour=None, backup_type=None, expect_next_backup_time=None, instance_id=None, last_update_time=None, period=None, ttl=None, _configuration=None):  # noqa: E501
        """DescribeBackupPlanResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._active = None
        self._backup_hour = None
        self._backup_type = None
        self._expect_next_backup_time = None
        self._instance_id = None
        self._last_update_time = None
        self._period = None
        self._ttl = None
        self.discriminator = None

        if active is not None:
            self.active = active
        if backup_hour is not None:
            self.backup_hour = backup_hour
        if backup_type is not None:
            self.backup_type = backup_type
        if expect_next_backup_time is not None:
            self.expect_next_backup_time = expect_next_backup_time
        if instance_id is not None:
            self.instance_id = instance_id
        if last_update_time is not None:
            self.last_update_time = last_update_time
        if period is not None:
            self.period = period
        if ttl is not None:
            self.ttl = ttl

    @property
    def active(self):
        """Gets the active of this DescribeBackupPlanResponse.  # noqa: E501


        :return: The active of this DescribeBackupPlanResponse.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this DescribeBackupPlanResponse.


        :param active: The active of this DescribeBackupPlanResponse.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def backup_hour(self):
        """Gets the backup_hour of this DescribeBackupPlanResponse.  # noqa: E501


        :return: The backup_hour of this DescribeBackupPlanResponse.  # noqa: E501
        :rtype: int
        """
        return self._backup_hour

    @backup_hour.setter
    def backup_hour(self, backup_hour):
        """Sets the backup_hour of this DescribeBackupPlanResponse.


        :param backup_hour: The backup_hour of this DescribeBackupPlanResponse.  # noqa: E501
        :type: int
        """

        self._backup_hour = backup_hour

    @property
    def backup_type(self):
        """Gets the backup_type of this DescribeBackupPlanResponse.  # noqa: E501


        :return: The backup_type of this DescribeBackupPlanResponse.  # noqa: E501
        :rtype: str
        """
        return self._backup_type

    @backup_type.setter
    def backup_type(self, backup_type):
        """Sets the backup_type of this DescribeBackupPlanResponse.


        :param backup_type: The backup_type of this DescribeBackupPlanResponse.  # noqa: E501
        :type: str
        """

        self._backup_type = backup_type

    @property
    def expect_next_backup_time(self):
        """Gets the expect_next_backup_time of this DescribeBackupPlanResponse.  # noqa: E501


        :return: The expect_next_backup_time of this DescribeBackupPlanResponse.  # noqa: E501
        :rtype: str
        """
        return self._expect_next_backup_time

    @expect_next_backup_time.setter
    def expect_next_backup_time(self, expect_next_backup_time):
        """Sets the expect_next_backup_time of this DescribeBackupPlanResponse.


        :param expect_next_backup_time: The expect_next_backup_time of this DescribeBackupPlanResponse.  # noqa: E501
        :type: str
        """

        self._expect_next_backup_time = expect_next_backup_time

    @property
    def instance_id(self):
        """Gets the instance_id of this DescribeBackupPlanResponse.  # noqa: E501


        :return: The instance_id of this DescribeBackupPlanResponse.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this DescribeBackupPlanResponse.


        :param instance_id: The instance_id of this DescribeBackupPlanResponse.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def last_update_time(self):
        """Gets the last_update_time of this DescribeBackupPlanResponse.  # noqa: E501


        :return: The last_update_time of this DescribeBackupPlanResponse.  # noqa: E501
        :rtype: str
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        """Sets the last_update_time of this DescribeBackupPlanResponse.


        :param last_update_time: The last_update_time of this DescribeBackupPlanResponse.  # noqa: E501
        :type: str
        """

        self._last_update_time = last_update_time

    @property
    def period(self):
        """Gets the period of this DescribeBackupPlanResponse.  # noqa: E501


        :return: The period of this DescribeBackupPlanResponse.  # noqa: E501
        :rtype: list[int]
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this DescribeBackupPlanResponse.


        :param period: The period of this DescribeBackupPlanResponse.  # noqa: E501
        :type: list[int]
        """

        self._period = period

    @property
    def ttl(self):
        """Gets the ttl of this DescribeBackupPlanResponse.  # noqa: E501


        :return: The ttl of this DescribeBackupPlanResponse.  # noqa: E501
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this DescribeBackupPlanResponse.


        :param ttl: The ttl of this DescribeBackupPlanResponse.  # noqa: E501
        :type: int
        """

        self._ttl = ttl

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
        if issubclass(DescribeBackupPlanResponse, dict):
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
        if not isinstance(other, DescribeBackupPlanResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeBackupPlanResponse):
            return True

        return self.to_dict() != other.to_dict()
