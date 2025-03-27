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


class DescribeBackupDetailRequest(object):
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
        'backup_id': 'str',
        'instance_id': 'str'
    }

    attribute_map = {
        'backup_id': 'BackupId',
        'instance_id': 'InstanceId'
    }

    def __init__(self, backup_id=None, instance_id=None, _configuration=None):  # noqa: E501
        """DescribeBackupDetailRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._backup_id = None
        self._instance_id = None
        self.discriminator = None

        self.backup_id = backup_id
        self.instance_id = instance_id

    @property
    def backup_id(self):
        """Gets the backup_id of this DescribeBackupDetailRequest.  # noqa: E501


        :return: The backup_id of this DescribeBackupDetailRequest.  # noqa: E501
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        """Sets the backup_id of this DescribeBackupDetailRequest.


        :param backup_id: The backup_id of this DescribeBackupDetailRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and backup_id is None:
            raise ValueError("Invalid value for `backup_id`, must not be `None`")  # noqa: E501

        self._backup_id = backup_id

    @property
    def instance_id(self):
        """Gets the instance_id of this DescribeBackupDetailRequest.  # noqa: E501


        :return: The instance_id of this DescribeBackupDetailRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this DescribeBackupDetailRequest.


        :param instance_id: The instance_id of this DescribeBackupDetailRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and instance_id is None:
            raise ValueError("Invalid value for `instance_id`, must not be `None`")  # noqa: E501

        self._instance_id = instance_id

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
        if issubclass(DescribeBackupDetailRequest, dict):
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
        if not isinstance(other, DescribeBackupDetailRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeBackupDetailRequest):
            return True

        return self.to_dict() != other.to_dict()
