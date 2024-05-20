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


class DescribeDetachedBackupsRequest(object):
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
        'backup_status': 'str',
        'backup_type': 'str',
        'instance_id': 'str',
        'instance_name': 'str',
        'page_number': 'int',
        'page_size': 'int',
        'project_name': 'str'
    }

    attribute_map = {
        'backup_end_time': 'BackupEndTime',
        'backup_id': 'BackupId',
        'backup_start_time': 'BackupStartTime',
        'backup_status': 'BackupStatus',
        'backup_type': 'BackupType',
        'instance_id': 'InstanceId',
        'instance_name': 'InstanceName',
        'page_number': 'PageNumber',
        'page_size': 'PageSize',
        'project_name': 'ProjectName'
    }

    def __init__(self, backup_end_time=None, backup_id=None, backup_start_time=None, backup_status=None, backup_type=None, instance_id=None, instance_name=None, page_number=None, page_size=None, project_name=None, _configuration=None):  # noqa: E501
        """DescribeDetachedBackupsRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._backup_end_time = None
        self._backup_id = None
        self._backup_start_time = None
        self._backup_status = None
        self._backup_type = None
        self._instance_id = None
        self._instance_name = None
        self._page_number = None
        self._page_size = None
        self._project_name = None
        self.discriminator = None

        if backup_end_time is not None:
            self.backup_end_time = backup_end_time
        if backup_id is not None:
            self.backup_id = backup_id
        if backup_start_time is not None:
            self.backup_start_time = backup_start_time
        if backup_status is not None:
            self.backup_status = backup_status
        if backup_type is not None:
            self.backup_type = backup_type
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if project_name is not None:
            self.project_name = project_name

    @property
    def backup_end_time(self):
        """Gets the backup_end_time of this DescribeDetachedBackupsRequest.  # noqa: E501


        :return: The backup_end_time of this DescribeDetachedBackupsRequest.  # noqa: E501
        :rtype: str
        """
        return self._backup_end_time

    @backup_end_time.setter
    def backup_end_time(self, backup_end_time):
        """Sets the backup_end_time of this DescribeDetachedBackupsRequest.


        :param backup_end_time: The backup_end_time of this DescribeDetachedBackupsRequest.  # noqa: E501
        :type: str
        """

        self._backup_end_time = backup_end_time

    @property
    def backup_id(self):
        """Gets the backup_id of this DescribeDetachedBackupsRequest.  # noqa: E501


        :return: The backup_id of this DescribeDetachedBackupsRequest.  # noqa: E501
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        """Sets the backup_id of this DescribeDetachedBackupsRequest.


        :param backup_id: The backup_id of this DescribeDetachedBackupsRequest.  # noqa: E501
        :type: str
        """

        self._backup_id = backup_id

    @property
    def backup_start_time(self):
        """Gets the backup_start_time of this DescribeDetachedBackupsRequest.  # noqa: E501


        :return: The backup_start_time of this DescribeDetachedBackupsRequest.  # noqa: E501
        :rtype: str
        """
        return self._backup_start_time

    @backup_start_time.setter
    def backup_start_time(self, backup_start_time):
        """Sets the backup_start_time of this DescribeDetachedBackupsRequest.


        :param backup_start_time: The backup_start_time of this DescribeDetachedBackupsRequest.  # noqa: E501
        :type: str
        """

        self._backup_start_time = backup_start_time

    @property
    def backup_status(self):
        """Gets the backup_status of this DescribeDetachedBackupsRequest.  # noqa: E501


        :return: The backup_status of this DescribeDetachedBackupsRequest.  # noqa: E501
        :rtype: str
        """
        return self._backup_status

    @backup_status.setter
    def backup_status(self, backup_status):
        """Sets the backup_status of this DescribeDetachedBackupsRequest.


        :param backup_status: The backup_status of this DescribeDetachedBackupsRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["Success", "Failed", "Running"]  # noqa: E501
        if (self._configuration.client_side_validation and
                backup_status not in allowed_values):
            raise ValueError(
                "Invalid value for `backup_status` ({0}), must be one of {1}"  # noqa: E501
                .format(backup_status, allowed_values)
            )

        self._backup_status = backup_status

    @property
    def backup_type(self):
        """Gets the backup_type of this DescribeDetachedBackupsRequest.  # noqa: E501


        :return: The backup_type of this DescribeDetachedBackupsRequest.  # noqa: E501
        :rtype: str
        """
        return self._backup_type

    @backup_type.setter
    def backup_type(self, backup_type):
        """Sets the backup_type of this DescribeDetachedBackupsRequest.


        :param backup_type: The backup_type of this DescribeDetachedBackupsRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["Full", "Increment"]  # noqa: E501
        if (self._configuration.client_side_validation and
                backup_type not in allowed_values):
            raise ValueError(
                "Invalid value for `backup_type` ({0}), must be one of {1}"  # noqa: E501
                .format(backup_type, allowed_values)
            )

        self._backup_type = backup_type

    @property
    def instance_id(self):
        """Gets the instance_id of this DescribeDetachedBackupsRequest.  # noqa: E501


        :return: The instance_id of this DescribeDetachedBackupsRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this DescribeDetachedBackupsRequest.


        :param instance_id: The instance_id of this DescribeDetachedBackupsRequest.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def instance_name(self):
        """Gets the instance_name of this DescribeDetachedBackupsRequest.  # noqa: E501


        :return: The instance_name of this DescribeDetachedBackupsRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this DescribeDetachedBackupsRequest.


        :param instance_name: The instance_name of this DescribeDetachedBackupsRequest.  # noqa: E501
        :type: str
        """

        self._instance_name = instance_name

    @property
    def page_number(self):
        """Gets the page_number of this DescribeDetachedBackupsRequest.  # noqa: E501


        :return: The page_number of this DescribeDetachedBackupsRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this DescribeDetachedBackupsRequest.


        :param page_number: The page_number of this DescribeDetachedBackupsRequest.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this DescribeDetachedBackupsRequest.  # noqa: E501


        :return: The page_size of this DescribeDetachedBackupsRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this DescribeDetachedBackupsRequest.


        :param page_size: The page_size of this DescribeDetachedBackupsRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def project_name(self):
        """Gets the project_name of this DescribeDetachedBackupsRequest.  # noqa: E501


        :return: The project_name of this DescribeDetachedBackupsRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this DescribeDetachedBackupsRequest.


        :param project_name: The project_name of this DescribeDetachedBackupsRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

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
        if issubclass(DescribeDetachedBackupsRequest, dict):
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
        if not isinstance(other, DescribeDetachedBackupsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeDetachedBackupsRequest):
            return True

        return self.to_dict() != other.to_dict()