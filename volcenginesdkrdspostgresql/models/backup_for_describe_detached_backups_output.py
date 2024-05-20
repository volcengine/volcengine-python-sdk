# coding: utf-8

"""
    rds_postgresql

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class BackupForDescribeDetachedBackupsOutput(object):
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
        'backup_end_time': 'str',
        'backup_file_name': 'str',
        'backup_file_size': 'int',
        'backup_id': 'str',
        'backup_progress': 'int',
        'backup_start_time': 'str',
        'backup_status': 'str',
        'backup_type': 'str',
        'create_type': 'str',
        'instance_info': 'InstanceInfoForDescribeDetachedBackupsOutput'
    }

    attribute_map = {
        'backup_end_time': 'BackupEndTime',
        'backup_file_name': 'BackupFileName',
        'backup_file_size': 'BackupFileSize',
        'backup_id': 'BackupId',
        'backup_progress': 'BackupProgress',
        'backup_start_time': 'BackupStartTime',
        'backup_status': 'BackupStatus',
        'backup_type': 'BackupType',
        'create_type': 'CreateType',
        'instance_info': 'InstanceInfo'
    }

    def __init__(self, backup_end_time=None, backup_file_name=None, backup_file_size=None, backup_id=None, backup_progress=None, backup_start_time=None, backup_status=None, backup_type=None, create_type=None, instance_info=None, _configuration=None):  # noqa: E501
        """BackupForDescribeDetachedBackupsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._backup_end_time = None
        self._backup_file_name = None
        self._backup_file_size = None
        self._backup_id = None
        self._backup_progress = None
        self._backup_start_time = None
        self._backup_status = None
        self._backup_type = None
        self._create_type = None
        self._instance_info = None
        self.discriminator = None

        if backup_end_time is not None:
            self.backup_end_time = backup_end_time
        if backup_file_name is not None:
            self.backup_file_name = backup_file_name
        if backup_file_size is not None:
            self.backup_file_size = backup_file_size
        if backup_id is not None:
            self.backup_id = backup_id
        if backup_progress is not None:
            self.backup_progress = backup_progress
        if backup_start_time is not None:
            self.backup_start_time = backup_start_time
        if backup_status is not None:
            self.backup_status = backup_status
        if backup_type is not None:
            self.backup_type = backup_type
        if create_type is not None:
            self.create_type = create_type
        if instance_info is not None:
            self.instance_info = instance_info

    @property
    def backup_end_time(self):
        """Gets the backup_end_time of this BackupForDescribeDetachedBackupsOutput.  # noqa: E501


        :return: The backup_end_time of this BackupForDescribeDetachedBackupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._backup_end_time

    @backup_end_time.setter
    def backup_end_time(self, backup_end_time):
        """Sets the backup_end_time of this BackupForDescribeDetachedBackupsOutput.


        :param backup_end_time: The backup_end_time of this BackupForDescribeDetachedBackupsOutput.  # noqa: E501
        :type: str
        """

        self._backup_end_time = backup_end_time

    @property
    def backup_file_name(self):
        """Gets the backup_file_name of this BackupForDescribeDetachedBackupsOutput.  # noqa: E501


        :return: The backup_file_name of this BackupForDescribeDetachedBackupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._backup_file_name

    @backup_file_name.setter
    def backup_file_name(self, backup_file_name):
        """Sets the backup_file_name of this BackupForDescribeDetachedBackupsOutput.


        :param backup_file_name: The backup_file_name of this BackupForDescribeDetachedBackupsOutput.  # noqa: E501
        :type: str
        """

        self._backup_file_name = backup_file_name

    @property
    def backup_file_size(self):
        """Gets the backup_file_size of this BackupForDescribeDetachedBackupsOutput.  # noqa: E501


        :return: The backup_file_size of this BackupForDescribeDetachedBackupsOutput.  # noqa: E501
        :rtype: int
        """
        return self._backup_file_size

    @backup_file_size.setter
    def backup_file_size(self, backup_file_size):
        """Sets the backup_file_size of this BackupForDescribeDetachedBackupsOutput.


        :param backup_file_size: The backup_file_size of this BackupForDescribeDetachedBackupsOutput.  # noqa: E501
        :type: int
        """

        self._backup_file_size = backup_file_size

    @property
    def backup_id(self):
        """Gets the backup_id of this BackupForDescribeDetachedBackupsOutput.  # noqa: E501


        :return: The backup_id of this BackupForDescribeDetachedBackupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        """Sets the backup_id of this BackupForDescribeDetachedBackupsOutput.


        :param backup_id: The backup_id of this BackupForDescribeDetachedBackupsOutput.  # noqa: E501
        :type: str
        """

        self._backup_id = backup_id

    @property
    def backup_progress(self):
        """Gets the backup_progress of this BackupForDescribeDetachedBackupsOutput.  # noqa: E501


        :return: The backup_progress of this BackupForDescribeDetachedBackupsOutput.  # noqa: E501
        :rtype: int
        """
        return self._backup_progress

    @backup_progress.setter
    def backup_progress(self, backup_progress):
        """Sets the backup_progress of this BackupForDescribeDetachedBackupsOutput.


        :param backup_progress: The backup_progress of this BackupForDescribeDetachedBackupsOutput.  # noqa: E501
        :type: int
        """

        self._backup_progress = backup_progress

    @property
    def backup_start_time(self):
        """Gets the backup_start_time of this BackupForDescribeDetachedBackupsOutput.  # noqa: E501


        :return: The backup_start_time of this BackupForDescribeDetachedBackupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._backup_start_time

    @backup_start_time.setter
    def backup_start_time(self, backup_start_time):
        """Sets the backup_start_time of this BackupForDescribeDetachedBackupsOutput.


        :param backup_start_time: The backup_start_time of this BackupForDescribeDetachedBackupsOutput.  # noqa: E501
        :type: str
        """

        self._backup_start_time = backup_start_time

    @property
    def backup_status(self):
        """Gets the backup_status of this BackupForDescribeDetachedBackupsOutput.  # noqa: E501


        :return: The backup_status of this BackupForDescribeDetachedBackupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._backup_status

    @backup_status.setter
    def backup_status(self, backup_status):
        """Sets the backup_status of this BackupForDescribeDetachedBackupsOutput.


        :param backup_status: The backup_status of this BackupForDescribeDetachedBackupsOutput.  # noqa: E501
        :type: str
        """

        self._backup_status = backup_status

    @property
    def backup_type(self):
        """Gets the backup_type of this BackupForDescribeDetachedBackupsOutput.  # noqa: E501


        :return: The backup_type of this BackupForDescribeDetachedBackupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._backup_type

    @backup_type.setter
    def backup_type(self, backup_type):
        """Sets the backup_type of this BackupForDescribeDetachedBackupsOutput.


        :param backup_type: The backup_type of this BackupForDescribeDetachedBackupsOutput.  # noqa: E501
        :type: str
        """

        self._backup_type = backup_type

    @property
    def create_type(self):
        """Gets the create_type of this BackupForDescribeDetachedBackupsOutput.  # noqa: E501


        :return: The create_type of this BackupForDescribeDetachedBackupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._create_type

    @create_type.setter
    def create_type(self, create_type):
        """Sets the create_type of this BackupForDescribeDetachedBackupsOutput.


        :param create_type: The create_type of this BackupForDescribeDetachedBackupsOutput.  # noqa: E501
        :type: str
        """

        self._create_type = create_type

    @property
    def instance_info(self):
        """Gets the instance_info of this BackupForDescribeDetachedBackupsOutput.  # noqa: E501


        :return: The instance_info of this BackupForDescribeDetachedBackupsOutput.  # noqa: E501
        :rtype: InstanceInfoForDescribeDetachedBackupsOutput
        """
        return self._instance_info

    @instance_info.setter
    def instance_info(self, instance_info):
        """Sets the instance_info of this BackupForDescribeDetachedBackupsOutput.


        :param instance_info: The instance_info of this BackupForDescribeDetachedBackupsOutput.  # noqa: E501
        :type: InstanceInfoForDescribeDetachedBackupsOutput
        """

        self._instance_info = instance_info

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
        if issubclass(BackupForDescribeDetachedBackupsOutput, dict):
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
        if not isinstance(other, BackupForDescribeDetachedBackupsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BackupForDescribeDetachedBackupsOutput):
            return True

        return self.to_dict() != other.to_dict()