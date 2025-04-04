# coding: utf-8

"""
    rds_mssql

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class RestoreTaskDetailForDescribeTosRestoreTaskDetailOutput(object):
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
        'backup_type': 'str',
        'db_name': 'str',
        'new_db_name': 'str',
        'restore_desc': 'str',
        'restore_end_time': 'str',
        'restore_file_name': 'str',
        'restore_file_size': 'str',
        'restore_start_time': 'str'
    }

    attribute_map = {
        'backup_type': 'BackupType',
        'db_name': 'DBName',
        'new_db_name': 'NewDBName',
        'restore_desc': 'RestoreDesc',
        'restore_end_time': 'RestoreEndTime',
        'restore_file_name': 'RestoreFileName',
        'restore_file_size': 'RestoreFileSize',
        'restore_start_time': 'RestoreStartTime'
    }

    def __init__(self, backup_type=None, db_name=None, new_db_name=None, restore_desc=None, restore_end_time=None, restore_file_name=None, restore_file_size=None, restore_start_time=None, _configuration=None):  # noqa: E501
        """RestoreTaskDetailForDescribeTosRestoreTaskDetailOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._backup_type = None
        self._db_name = None
        self._new_db_name = None
        self._restore_desc = None
        self._restore_end_time = None
        self._restore_file_name = None
        self._restore_file_size = None
        self._restore_start_time = None
        self.discriminator = None

        if backup_type is not None:
            self.backup_type = backup_type
        if db_name is not None:
            self.db_name = db_name
        if new_db_name is not None:
            self.new_db_name = new_db_name
        if restore_desc is not None:
            self.restore_desc = restore_desc
        if restore_end_time is not None:
            self.restore_end_time = restore_end_time
        if restore_file_name is not None:
            self.restore_file_name = restore_file_name
        if restore_file_size is not None:
            self.restore_file_size = restore_file_size
        if restore_start_time is not None:
            self.restore_start_time = restore_start_time

    @property
    def backup_type(self):
        """Gets the backup_type of this RestoreTaskDetailForDescribeTosRestoreTaskDetailOutput.  # noqa: E501


        :return: The backup_type of this RestoreTaskDetailForDescribeTosRestoreTaskDetailOutput.  # noqa: E501
        :rtype: str
        """
        return self._backup_type

    @backup_type.setter
    def backup_type(self, backup_type):
        """Sets the backup_type of this RestoreTaskDetailForDescribeTosRestoreTaskDetailOutput.


        :param backup_type: The backup_type of this RestoreTaskDetailForDescribeTosRestoreTaskDetailOutput.  # noqa: E501
        :type: str
        """

        self._backup_type = backup_type

    @property
    def db_name(self):
        """Gets the db_name of this RestoreTaskDetailForDescribeTosRestoreTaskDetailOutput.  # noqa: E501


        :return: The db_name of this RestoreTaskDetailForDescribeTosRestoreTaskDetailOutput.  # noqa: E501
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """Sets the db_name of this RestoreTaskDetailForDescribeTosRestoreTaskDetailOutput.


        :param db_name: The db_name of this RestoreTaskDetailForDescribeTosRestoreTaskDetailOutput.  # noqa: E501
        :type: str
        """

        self._db_name = db_name

    @property
    def new_db_name(self):
        """Gets the new_db_name of this RestoreTaskDetailForDescribeTosRestoreTaskDetailOutput.  # noqa: E501


        :return: The new_db_name of this RestoreTaskDetailForDescribeTosRestoreTaskDetailOutput.  # noqa: E501
        :rtype: str
        """
        return self._new_db_name

    @new_db_name.setter
    def new_db_name(self, new_db_name):
        """Sets the new_db_name of this RestoreTaskDetailForDescribeTosRestoreTaskDetailOutput.


        :param new_db_name: The new_db_name of this RestoreTaskDetailForDescribeTosRestoreTaskDetailOutput.  # noqa: E501
        :type: str
        """

        self._new_db_name = new_db_name

    @property
    def restore_desc(self):
        """Gets the restore_desc of this RestoreTaskDetailForDescribeTosRestoreTaskDetailOutput.  # noqa: E501


        :return: The restore_desc of this RestoreTaskDetailForDescribeTosRestoreTaskDetailOutput.  # noqa: E501
        :rtype: str
        """
        return self._restore_desc

    @restore_desc.setter
    def restore_desc(self, restore_desc):
        """Sets the restore_desc of this RestoreTaskDetailForDescribeTosRestoreTaskDetailOutput.


        :param restore_desc: The restore_desc of this RestoreTaskDetailForDescribeTosRestoreTaskDetailOutput.  # noqa: E501
        :type: str
        """

        self._restore_desc = restore_desc

    @property
    def restore_end_time(self):
        """Gets the restore_end_time of this RestoreTaskDetailForDescribeTosRestoreTaskDetailOutput.  # noqa: E501


        :return: The restore_end_time of this RestoreTaskDetailForDescribeTosRestoreTaskDetailOutput.  # noqa: E501
        :rtype: str
        """
        return self._restore_end_time

    @restore_end_time.setter
    def restore_end_time(self, restore_end_time):
        """Sets the restore_end_time of this RestoreTaskDetailForDescribeTosRestoreTaskDetailOutput.


        :param restore_end_time: The restore_end_time of this RestoreTaskDetailForDescribeTosRestoreTaskDetailOutput.  # noqa: E501
        :type: str
        """

        self._restore_end_time = restore_end_time

    @property
    def restore_file_name(self):
        """Gets the restore_file_name of this RestoreTaskDetailForDescribeTosRestoreTaskDetailOutput.  # noqa: E501


        :return: The restore_file_name of this RestoreTaskDetailForDescribeTosRestoreTaskDetailOutput.  # noqa: E501
        :rtype: str
        """
        return self._restore_file_name

    @restore_file_name.setter
    def restore_file_name(self, restore_file_name):
        """Sets the restore_file_name of this RestoreTaskDetailForDescribeTosRestoreTaskDetailOutput.


        :param restore_file_name: The restore_file_name of this RestoreTaskDetailForDescribeTosRestoreTaskDetailOutput.  # noqa: E501
        :type: str
        """

        self._restore_file_name = restore_file_name

    @property
    def restore_file_size(self):
        """Gets the restore_file_size of this RestoreTaskDetailForDescribeTosRestoreTaskDetailOutput.  # noqa: E501


        :return: The restore_file_size of this RestoreTaskDetailForDescribeTosRestoreTaskDetailOutput.  # noqa: E501
        :rtype: str
        """
        return self._restore_file_size

    @restore_file_size.setter
    def restore_file_size(self, restore_file_size):
        """Sets the restore_file_size of this RestoreTaskDetailForDescribeTosRestoreTaskDetailOutput.


        :param restore_file_size: The restore_file_size of this RestoreTaskDetailForDescribeTosRestoreTaskDetailOutput.  # noqa: E501
        :type: str
        """

        self._restore_file_size = restore_file_size

    @property
    def restore_start_time(self):
        """Gets the restore_start_time of this RestoreTaskDetailForDescribeTosRestoreTaskDetailOutput.  # noqa: E501


        :return: The restore_start_time of this RestoreTaskDetailForDescribeTosRestoreTaskDetailOutput.  # noqa: E501
        :rtype: str
        """
        return self._restore_start_time

    @restore_start_time.setter
    def restore_start_time(self, restore_start_time):
        """Sets the restore_start_time of this RestoreTaskDetailForDescribeTosRestoreTaskDetailOutput.


        :param restore_start_time: The restore_start_time of this RestoreTaskDetailForDescribeTosRestoreTaskDetailOutput.  # noqa: E501
        :type: str
        """

        self._restore_start_time = restore_start_time

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
        if issubclass(RestoreTaskDetailForDescribeTosRestoreTaskDetailOutput, dict):
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
        if not isinstance(other, RestoreTaskDetailForDescribeTosRestoreTaskDetailOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RestoreTaskDetailForDescribeTosRestoreTaskDetailOutput):
            return True

        return self.to_dict() != other.to_dict()
