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


class DataForDescribeCrossRegionBackupDBInstancesOutput(object):
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
        'backup_enabled': 'bool',
        'db_engine_version': 'str',
        'instance_id': 'str',
        'instance_name': 'str',
        'instance_status': 'str',
        'log_backup_enabled': 'bool',
        'project_name': 'str',
        'region_id': 'str',
        'retention': 'int',
        'service_enable_time': 'str'
    }

    attribute_map = {
        'backup_enabled': 'BackupEnabled',
        'db_engine_version': 'DBEngineVersion',
        'instance_id': 'InstanceId',
        'instance_name': 'InstanceName',
        'instance_status': 'InstanceStatus',
        'log_backup_enabled': 'LogBackupEnabled',
        'project_name': 'ProjectName',
        'region_id': 'RegionId',
        'retention': 'Retention',
        'service_enable_time': 'ServiceEnableTime'
    }

    def __init__(self, backup_enabled=None, db_engine_version=None, instance_id=None, instance_name=None, instance_status=None, log_backup_enabled=None, project_name=None, region_id=None, retention=None, service_enable_time=None, _configuration=None):  # noqa: E501
        """DataForDescribeCrossRegionBackupDBInstancesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._backup_enabled = None
        self._db_engine_version = None
        self._instance_id = None
        self._instance_name = None
        self._instance_status = None
        self._log_backup_enabled = None
        self._project_name = None
        self._region_id = None
        self._retention = None
        self._service_enable_time = None
        self.discriminator = None

        if backup_enabled is not None:
            self.backup_enabled = backup_enabled
        if db_engine_version is not None:
            self.db_engine_version = db_engine_version
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if instance_status is not None:
            self.instance_status = instance_status
        if log_backup_enabled is not None:
            self.log_backup_enabled = log_backup_enabled
        if project_name is not None:
            self.project_name = project_name
        if region_id is not None:
            self.region_id = region_id
        if retention is not None:
            self.retention = retention
        if service_enable_time is not None:
            self.service_enable_time = service_enable_time

    @property
    def backup_enabled(self):
        """Gets the backup_enabled of this DataForDescribeCrossRegionBackupDBInstancesOutput.  # noqa: E501


        :return: The backup_enabled of this DataForDescribeCrossRegionBackupDBInstancesOutput.  # noqa: E501
        :rtype: bool
        """
        return self._backup_enabled

    @backup_enabled.setter
    def backup_enabled(self, backup_enabled):
        """Sets the backup_enabled of this DataForDescribeCrossRegionBackupDBInstancesOutput.


        :param backup_enabled: The backup_enabled of this DataForDescribeCrossRegionBackupDBInstancesOutput.  # noqa: E501
        :type: bool
        """

        self._backup_enabled = backup_enabled

    @property
    def db_engine_version(self):
        """Gets the db_engine_version of this DataForDescribeCrossRegionBackupDBInstancesOutput.  # noqa: E501


        :return: The db_engine_version of this DataForDescribeCrossRegionBackupDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._db_engine_version

    @db_engine_version.setter
    def db_engine_version(self, db_engine_version):
        """Sets the db_engine_version of this DataForDescribeCrossRegionBackupDBInstancesOutput.


        :param db_engine_version: The db_engine_version of this DataForDescribeCrossRegionBackupDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._db_engine_version = db_engine_version

    @property
    def instance_id(self):
        """Gets the instance_id of this DataForDescribeCrossRegionBackupDBInstancesOutput.  # noqa: E501


        :return: The instance_id of this DataForDescribeCrossRegionBackupDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this DataForDescribeCrossRegionBackupDBInstancesOutput.


        :param instance_id: The instance_id of this DataForDescribeCrossRegionBackupDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def instance_name(self):
        """Gets the instance_name of this DataForDescribeCrossRegionBackupDBInstancesOutput.  # noqa: E501


        :return: The instance_name of this DataForDescribeCrossRegionBackupDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this DataForDescribeCrossRegionBackupDBInstancesOutput.


        :param instance_name: The instance_name of this DataForDescribeCrossRegionBackupDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._instance_name = instance_name

    @property
    def instance_status(self):
        """Gets the instance_status of this DataForDescribeCrossRegionBackupDBInstancesOutput.  # noqa: E501


        :return: The instance_status of this DataForDescribeCrossRegionBackupDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_status

    @instance_status.setter
    def instance_status(self, instance_status):
        """Sets the instance_status of this DataForDescribeCrossRegionBackupDBInstancesOutput.


        :param instance_status: The instance_status of this DataForDescribeCrossRegionBackupDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._instance_status = instance_status

    @property
    def log_backup_enabled(self):
        """Gets the log_backup_enabled of this DataForDescribeCrossRegionBackupDBInstancesOutput.  # noqa: E501


        :return: The log_backup_enabled of this DataForDescribeCrossRegionBackupDBInstancesOutput.  # noqa: E501
        :rtype: bool
        """
        return self._log_backup_enabled

    @log_backup_enabled.setter
    def log_backup_enabled(self, log_backup_enabled):
        """Sets the log_backup_enabled of this DataForDescribeCrossRegionBackupDBInstancesOutput.


        :param log_backup_enabled: The log_backup_enabled of this DataForDescribeCrossRegionBackupDBInstancesOutput.  # noqa: E501
        :type: bool
        """

        self._log_backup_enabled = log_backup_enabled

    @property
    def project_name(self):
        """Gets the project_name of this DataForDescribeCrossRegionBackupDBInstancesOutput.  # noqa: E501


        :return: The project_name of this DataForDescribeCrossRegionBackupDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this DataForDescribeCrossRegionBackupDBInstancesOutput.


        :param project_name: The project_name of this DataForDescribeCrossRegionBackupDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def region_id(self):
        """Gets the region_id of this DataForDescribeCrossRegionBackupDBInstancesOutput.  # noqa: E501


        :return: The region_id of this DataForDescribeCrossRegionBackupDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this DataForDescribeCrossRegionBackupDBInstancesOutput.


        :param region_id: The region_id of this DataForDescribeCrossRegionBackupDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._region_id = region_id

    @property
    def retention(self):
        """Gets the retention of this DataForDescribeCrossRegionBackupDBInstancesOutput.  # noqa: E501


        :return: The retention of this DataForDescribeCrossRegionBackupDBInstancesOutput.  # noqa: E501
        :rtype: int
        """
        return self._retention

    @retention.setter
    def retention(self, retention):
        """Sets the retention of this DataForDescribeCrossRegionBackupDBInstancesOutput.


        :param retention: The retention of this DataForDescribeCrossRegionBackupDBInstancesOutput.  # noqa: E501
        :type: int
        """

        self._retention = retention

    @property
    def service_enable_time(self):
        """Gets the service_enable_time of this DataForDescribeCrossRegionBackupDBInstancesOutput.  # noqa: E501


        :return: The service_enable_time of this DataForDescribeCrossRegionBackupDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._service_enable_time

    @service_enable_time.setter
    def service_enable_time(self, service_enable_time):
        """Sets the service_enable_time of this DataForDescribeCrossRegionBackupDBInstancesOutput.


        :param service_enable_time: The service_enable_time of this DataForDescribeCrossRegionBackupDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._service_enable_time = service_enable_time

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
        if issubclass(DataForDescribeCrossRegionBackupDBInstancesOutput, dict):
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
        if not isinstance(other, DataForDescribeCrossRegionBackupDBInstancesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataForDescribeCrossRegionBackupDBInstancesOutput):
            return True

        return self.to_dict() != other.to_dict()
