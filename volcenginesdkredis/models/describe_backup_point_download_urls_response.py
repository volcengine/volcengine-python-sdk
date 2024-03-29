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


class DescribeBackupPointDownloadUrlsResponse(object):
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
        'backup_point_download_urls': 'list[BackupPointDownloadUrlForDescribeBackupPointDownloadUrlsOutput]',
        'instance_id': 'str',
        'shard_number': 'int'
    }

    attribute_map = {
        'backup_point_download_urls': 'BackupPointDownloadUrls',
        'instance_id': 'InstanceId',
        'shard_number': 'ShardNumber'
    }

    def __init__(self, backup_point_download_urls=None, instance_id=None, shard_number=None, _configuration=None):  # noqa: E501
        """DescribeBackupPointDownloadUrlsResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._backup_point_download_urls = None
        self._instance_id = None
        self._shard_number = None
        self.discriminator = None

        if backup_point_download_urls is not None:
            self.backup_point_download_urls = backup_point_download_urls
        if instance_id is not None:
            self.instance_id = instance_id
        if shard_number is not None:
            self.shard_number = shard_number

    @property
    def backup_point_download_urls(self):
        """Gets the backup_point_download_urls of this DescribeBackupPointDownloadUrlsResponse.  # noqa: E501


        :return: The backup_point_download_urls of this DescribeBackupPointDownloadUrlsResponse.  # noqa: E501
        :rtype: list[BackupPointDownloadUrlForDescribeBackupPointDownloadUrlsOutput]
        """
        return self._backup_point_download_urls

    @backup_point_download_urls.setter
    def backup_point_download_urls(self, backup_point_download_urls):
        """Sets the backup_point_download_urls of this DescribeBackupPointDownloadUrlsResponse.


        :param backup_point_download_urls: The backup_point_download_urls of this DescribeBackupPointDownloadUrlsResponse.  # noqa: E501
        :type: list[BackupPointDownloadUrlForDescribeBackupPointDownloadUrlsOutput]
        """

        self._backup_point_download_urls = backup_point_download_urls

    @property
    def instance_id(self):
        """Gets the instance_id of this DescribeBackupPointDownloadUrlsResponse.  # noqa: E501


        :return: The instance_id of this DescribeBackupPointDownloadUrlsResponse.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this DescribeBackupPointDownloadUrlsResponse.


        :param instance_id: The instance_id of this DescribeBackupPointDownloadUrlsResponse.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def shard_number(self):
        """Gets the shard_number of this DescribeBackupPointDownloadUrlsResponse.  # noqa: E501


        :return: The shard_number of this DescribeBackupPointDownloadUrlsResponse.  # noqa: E501
        :rtype: int
        """
        return self._shard_number

    @shard_number.setter
    def shard_number(self, shard_number):
        """Sets the shard_number of this DescribeBackupPointDownloadUrlsResponse.


        :param shard_number: The shard_number of this DescribeBackupPointDownloadUrlsResponse.  # noqa: E501
        :type: int
        """

        self._shard_number = shard_number

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
        if issubclass(DescribeBackupPointDownloadUrlsResponse, dict):
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
        if not isinstance(other, DescribeBackupPointDownloadUrlsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeBackupPointDownloadUrlsResponse):
            return True

        return self.to_dict() != other.to_dict()
