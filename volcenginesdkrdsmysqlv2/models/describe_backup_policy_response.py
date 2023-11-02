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


class DescribeBackupPolicyResponse(object):
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
        'binlog_file_counts_enable': 'bool',
        'binlog_limit_count': 'int',
        'binlog_local_retention_hour': 'int',
        'binlog_space_limit_enable': 'bool',
        'binlog_storage_percentage': 'int',
        'data_backup_retention_day': 'int',
        'data_full_backup_periods': 'list[str]',
        'data_full_backup_time': 'str',
        'instance_id': 'str',
        'log_backup_retention_day': 'int'
    }

    attribute_map = {
        'binlog_file_counts_enable': 'BinlogFileCountsEnable',
        'binlog_limit_count': 'BinlogLimitCount',
        'binlog_local_retention_hour': 'BinlogLocalRetentionHour',
        'binlog_space_limit_enable': 'BinlogSpaceLimitEnable',
        'binlog_storage_percentage': 'BinlogStoragePercentage',
        'data_backup_retention_day': 'DataBackupRetentionDay',
        'data_full_backup_periods': 'DataFullBackupPeriods',
        'data_full_backup_time': 'DataFullBackupTime',
        'instance_id': 'InstanceId',
        'log_backup_retention_day': 'LogBackupRetentionDay'
    }

    def __init__(self, binlog_file_counts_enable=None, binlog_limit_count=None, binlog_local_retention_hour=None, binlog_space_limit_enable=None, binlog_storage_percentage=None, data_backup_retention_day=None, data_full_backup_periods=None, data_full_backup_time=None, instance_id=None, log_backup_retention_day=None, _configuration=None):  # noqa: E501
        """DescribeBackupPolicyResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._binlog_file_counts_enable = None
        self._binlog_limit_count = None
        self._binlog_local_retention_hour = None
        self._binlog_space_limit_enable = None
        self._binlog_storage_percentage = None
        self._data_backup_retention_day = None
        self._data_full_backup_periods = None
        self._data_full_backup_time = None
        self._instance_id = None
        self._log_backup_retention_day = None
        self.discriminator = None

        if binlog_file_counts_enable is not None:
            self.binlog_file_counts_enable = binlog_file_counts_enable
        if binlog_limit_count is not None:
            self.binlog_limit_count = binlog_limit_count
        if binlog_local_retention_hour is not None:
            self.binlog_local_retention_hour = binlog_local_retention_hour
        if binlog_space_limit_enable is not None:
            self.binlog_space_limit_enable = binlog_space_limit_enable
        if binlog_storage_percentage is not None:
            self.binlog_storage_percentage = binlog_storage_percentage
        if data_backup_retention_day is not None:
            self.data_backup_retention_day = data_backup_retention_day
        if data_full_backup_periods is not None:
            self.data_full_backup_periods = data_full_backup_periods
        if data_full_backup_time is not None:
            self.data_full_backup_time = data_full_backup_time
        if instance_id is not None:
            self.instance_id = instance_id
        if log_backup_retention_day is not None:
            self.log_backup_retention_day = log_backup_retention_day

    @property
    def binlog_file_counts_enable(self):
        """Gets the binlog_file_counts_enable of this DescribeBackupPolicyResponse.  # noqa: E501


        :return: The binlog_file_counts_enable of this DescribeBackupPolicyResponse.  # noqa: E501
        :rtype: bool
        """
        return self._binlog_file_counts_enable

    @binlog_file_counts_enable.setter
    def binlog_file_counts_enable(self, binlog_file_counts_enable):
        """Sets the binlog_file_counts_enable of this DescribeBackupPolicyResponse.


        :param binlog_file_counts_enable: The binlog_file_counts_enable of this DescribeBackupPolicyResponse.  # noqa: E501
        :type: bool
        """

        self._binlog_file_counts_enable = binlog_file_counts_enable

    @property
    def binlog_limit_count(self):
        """Gets the binlog_limit_count of this DescribeBackupPolicyResponse.  # noqa: E501


        :return: The binlog_limit_count of this DescribeBackupPolicyResponse.  # noqa: E501
        :rtype: int
        """
        return self._binlog_limit_count

    @binlog_limit_count.setter
    def binlog_limit_count(self, binlog_limit_count):
        """Sets the binlog_limit_count of this DescribeBackupPolicyResponse.


        :param binlog_limit_count: The binlog_limit_count of this DescribeBackupPolicyResponse.  # noqa: E501
        :type: int
        """

        self._binlog_limit_count = binlog_limit_count

    @property
    def binlog_local_retention_hour(self):
        """Gets the binlog_local_retention_hour of this DescribeBackupPolicyResponse.  # noqa: E501


        :return: The binlog_local_retention_hour of this DescribeBackupPolicyResponse.  # noqa: E501
        :rtype: int
        """
        return self._binlog_local_retention_hour

    @binlog_local_retention_hour.setter
    def binlog_local_retention_hour(self, binlog_local_retention_hour):
        """Sets the binlog_local_retention_hour of this DescribeBackupPolicyResponse.


        :param binlog_local_retention_hour: The binlog_local_retention_hour of this DescribeBackupPolicyResponse.  # noqa: E501
        :type: int
        """

        self._binlog_local_retention_hour = binlog_local_retention_hour

    @property
    def binlog_space_limit_enable(self):
        """Gets the binlog_space_limit_enable of this DescribeBackupPolicyResponse.  # noqa: E501


        :return: The binlog_space_limit_enable of this DescribeBackupPolicyResponse.  # noqa: E501
        :rtype: bool
        """
        return self._binlog_space_limit_enable

    @binlog_space_limit_enable.setter
    def binlog_space_limit_enable(self, binlog_space_limit_enable):
        """Sets the binlog_space_limit_enable of this DescribeBackupPolicyResponse.


        :param binlog_space_limit_enable: The binlog_space_limit_enable of this DescribeBackupPolicyResponse.  # noqa: E501
        :type: bool
        """

        self._binlog_space_limit_enable = binlog_space_limit_enable

    @property
    def binlog_storage_percentage(self):
        """Gets the binlog_storage_percentage of this DescribeBackupPolicyResponse.  # noqa: E501


        :return: The binlog_storage_percentage of this DescribeBackupPolicyResponse.  # noqa: E501
        :rtype: int
        """
        return self._binlog_storage_percentage

    @binlog_storage_percentage.setter
    def binlog_storage_percentage(self, binlog_storage_percentage):
        """Sets the binlog_storage_percentage of this DescribeBackupPolicyResponse.


        :param binlog_storage_percentage: The binlog_storage_percentage of this DescribeBackupPolicyResponse.  # noqa: E501
        :type: int
        """

        self._binlog_storage_percentage = binlog_storage_percentage

    @property
    def data_backup_retention_day(self):
        """Gets the data_backup_retention_day of this DescribeBackupPolicyResponse.  # noqa: E501


        :return: The data_backup_retention_day of this DescribeBackupPolicyResponse.  # noqa: E501
        :rtype: int
        """
        return self._data_backup_retention_day

    @data_backup_retention_day.setter
    def data_backup_retention_day(self, data_backup_retention_day):
        """Sets the data_backup_retention_day of this DescribeBackupPolicyResponse.


        :param data_backup_retention_day: The data_backup_retention_day of this DescribeBackupPolicyResponse.  # noqa: E501
        :type: int
        """

        self._data_backup_retention_day = data_backup_retention_day

    @property
    def data_full_backup_periods(self):
        """Gets the data_full_backup_periods of this DescribeBackupPolicyResponse.  # noqa: E501


        :return: The data_full_backup_periods of this DescribeBackupPolicyResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._data_full_backup_periods

    @data_full_backup_periods.setter
    def data_full_backup_periods(self, data_full_backup_periods):
        """Sets the data_full_backup_periods of this DescribeBackupPolicyResponse.


        :param data_full_backup_periods: The data_full_backup_periods of this DescribeBackupPolicyResponse.  # noqa: E501
        :type: list[str]
        """

        self._data_full_backup_periods = data_full_backup_periods

    @property
    def data_full_backup_time(self):
        """Gets the data_full_backup_time of this DescribeBackupPolicyResponse.  # noqa: E501


        :return: The data_full_backup_time of this DescribeBackupPolicyResponse.  # noqa: E501
        :rtype: str
        """
        return self._data_full_backup_time

    @data_full_backup_time.setter
    def data_full_backup_time(self, data_full_backup_time):
        """Sets the data_full_backup_time of this DescribeBackupPolicyResponse.


        :param data_full_backup_time: The data_full_backup_time of this DescribeBackupPolicyResponse.  # noqa: E501
        :type: str
        """

        self._data_full_backup_time = data_full_backup_time

    @property
    def instance_id(self):
        """Gets the instance_id of this DescribeBackupPolicyResponse.  # noqa: E501


        :return: The instance_id of this DescribeBackupPolicyResponse.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this DescribeBackupPolicyResponse.


        :param instance_id: The instance_id of this DescribeBackupPolicyResponse.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def log_backup_retention_day(self):
        """Gets the log_backup_retention_day of this DescribeBackupPolicyResponse.  # noqa: E501


        :return: The log_backup_retention_day of this DescribeBackupPolicyResponse.  # noqa: E501
        :rtype: int
        """
        return self._log_backup_retention_day

    @log_backup_retention_day.setter
    def log_backup_retention_day(self, log_backup_retention_day):
        """Sets the log_backup_retention_day of this DescribeBackupPolicyResponse.


        :param log_backup_retention_day: The log_backup_retention_day of this DescribeBackupPolicyResponse.  # noqa: E501
        :type: int
        """

        self._log_backup_retention_day = log_backup_retention_day

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
        if issubclass(DescribeBackupPolicyResponse, dict):
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
        if not isinstance(other, DescribeBackupPolicyResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeBackupPolicyResponse):
            return True

        return self.to_dict() != other.to_dict()
