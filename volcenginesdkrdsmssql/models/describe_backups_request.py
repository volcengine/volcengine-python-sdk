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


class DescribeBackupsRequest(object):
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
        'backup_id': 'str',
        'backup_start_time': 'str',
        'backup_type': 'str',
        'instance_id': 'str',
        'page_number': 'int',
        'page_size': 'int'
    }

    attribute_map = {
        'backup_end_time': 'BackupEndTime',
        'backup_id': 'BackupId',
        'backup_start_time': 'BackupStartTime',
        'backup_type': 'BackupType',
        'instance_id': 'InstanceId',
        'page_number': 'PageNumber',
        'page_size': 'PageSize'
    }

    def __init__(self, backup_end_time=None, backup_id=None, backup_start_time=None, backup_type=None, instance_id=None, page_number=None, page_size=None, _configuration=None):  # noqa: E501
        """DescribeBackupsRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._backup_end_time = None
        self._backup_id = None
        self._backup_start_time = None
        self._backup_type = None
        self._instance_id = None
        self._page_number = None
        self._page_size = None
        self.discriminator = None

        if backup_end_time is not None:
            self.backup_end_time = backup_end_time
        if backup_id is not None:
            self.backup_id = backup_id
        if backup_start_time is not None:
            self.backup_start_time = backup_start_time
        if backup_type is not None:
            self.backup_type = backup_type
        self.instance_id = instance_id
        self.page_number = page_number
        self.page_size = page_size

    @property
    def backup_end_time(self):
        """Gets the backup_end_time of this DescribeBackupsRequest.  # noqa: E501


        :return: The backup_end_time of this DescribeBackupsRequest.  # noqa: E501
        :rtype: str
        """
        return self._backup_end_time

    @backup_end_time.setter
    def backup_end_time(self, backup_end_time):
        """Sets the backup_end_time of this DescribeBackupsRequest.


        :param backup_end_time: The backup_end_time of this DescribeBackupsRequest.  # noqa: E501
        :type: str
        """

        self._backup_end_time = backup_end_time

    @property
    def backup_id(self):
        """Gets the backup_id of this DescribeBackupsRequest.  # noqa: E501


        :return: The backup_id of this DescribeBackupsRequest.  # noqa: E501
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        """Sets the backup_id of this DescribeBackupsRequest.


        :param backup_id: The backup_id of this DescribeBackupsRequest.  # noqa: E501
        :type: str
        """

        self._backup_id = backup_id

    @property
    def backup_start_time(self):
        """Gets the backup_start_time of this DescribeBackupsRequest.  # noqa: E501


        :return: The backup_start_time of this DescribeBackupsRequest.  # noqa: E501
        :rtype: str
        """
        return self._backup_start_time

    @backup_start_time.setter
    def backup_start_time(self, backup_start_time):
        """Sets the backup_start_time of this DescribeBackupsRequest.


        :param backup_start_time: The backup_start_time of this DescribeBackupsRequest.  # noqa: E501
        :type: str
        """

        self._backup_start_time = backup_start_time

    @property
    def backup_type(self):
        """Gets the backup_type of this DescribeBackupsRequest.  # noqa: E501


        :return: The backup_type of this DescribeBackupsRequest.  # noqa: E501
        :rtype: str
        """
        return self._backup_type

    @backup_type.setter
    def backup_type(self, backup_type):
        """Sets the backup_type of this DescribeBackupsRequest.


        :param backup_type: The backup_type of this DescribeBackupsRequest.  # noqa: E501
        :type: str
        """

        self._backup_type = backup_type

    @property
    def instance_id(self):
        """Gets the instance_id of this DescribeBackupsRequest.  # noqa: E501


        :return: The instance_id of this DescribeBackupsRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this DescribeBackupsRequest.


        :param instance_id: The instance_id of this DescribeBackupsRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and instance_id is None:
            raise ValueError("Invalid value for `instance_id`, must not be `None`")  # noqa: E501

        self._instance_id = instance_id

    @property
    def page_number(self):
        """Gets the page_number of this DescribeBackupsRequest.  # noqa: E501


        :return: The page_number of this DescribeBackupsRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this DescribeBackupsRequest.


        :param page_number: The page_number of this DescribeBackupsRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and page_number is None:
            raise ValueError("Invalid value for `page_number`, must not be `None`")  # noqa: E501

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this DescribeBackupsRequest.  # noqa: E501


        :return: The page_size of this DescribeBackupsRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this DescribeBackupsRequest.


        :param page_size: The page_size of this DescribeBackupsRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and page_size is None:
            raise ValueError("Invalid value for `page_size`, must not be `None`")  # noqa: E501

        self._page_size = page_size

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
        if issubclass(DescribeBackupsRequest, dict):
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
        if not isinstance(other, DescribeBackupsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeBackupsRequest):
            return True

        return self.to_dict() != other.to_dict()
