# coding: utf-8

"""
    seccenter

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class AddCloudEnvRequest(object):
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
        'access_key': 'str',
        'cloud_platform': 'str',
        'comment': 'str',
        'key_type': 'str',
        'secret_key': 'str',
        'sync_period': 'int'
    }

    attribute_map = {
        'access_key': 'AccessKey',
        'cloud_platform': 'CloudPlatform',
        'comment': 'Comment',
        'key_type': 'KeyType',
        'secret_key': 'SecretKey',
        'sync_period': 'SyncPeriod'
    }

    def __init__(self, access_key=None, cloud_platform=None, comment=None, key_type=None, secret_key=None, sync_period=None, _configuration=None):  # noqa: E501
        """AddCloudEnvRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._access_key = None
        self._cloud_platform = None
        self._comment = None
        self._key_type = None
        self._secret_key = None
        self._sync_period = None
        self.discriminator = None

        self.access_key = access_key
        self.cloud_platform = cloud_platform
        self.comment = comment
        self.key_type = key_type
        self.secret_key = secret_key
        self.sync_period = sync_period

    @property
    def access_key(self):
        """Gets the access_key of this AddCloudEnvRequest.  # noqa: E501


        :return: The access_key of this AddCloudEnvRequest.  # noqa: E501
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        """Sets the access_key of this AddCloudEnvRequest.


        :param access_key: The access_key of this AddCloudEnvRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and access_key is None:
            raise ValueError("Invalid value for `access_key`, must not be `None`")  # noqa: E501

        self._access_key = access_key

    @property
    def cloud_platform(self):
        """Gets the cloud_platform of this AddCloudEnvRequest.  # noqa: E501


        :return: The cloud_platform of this AddCloudEnvRequest.  # noqa: E501
        :rtype: str
        """
        return self._cloud_platform

    @cloud_platform.setter
    def cloud_platform(self, cloud_platform):
        """Sets the cloud_platform of this AddCloudEnvRequest.


        :param cloud_platform: The cloud_platform of this AddCloudEnvRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and cloud_platform is None:
            raise ValueError("Invalid value for `cloud_platform`, must not be `None`")  # noqa: E501

        self._cloud_platform = cloud_platform

    @property
    def comment(self):
        """Gets the comment of this AddCloudEnvRequest.  # noqa: E501


        :return: The comment of this AddCloudEnvRequest.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this AddCloudEnvRequest.


        :param comment: The comment of this AddCloudEnvRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and comment is None:
            raise ValueError("Invalid value for `comment`, must not be `None`")  # noqa: E501

        self._comment = comment

    @property
    def key_type(self):
        """Gets the key_type of this AddCloudEnvRequest.  # noqa: E501


        :return: The key_type of this AddCloudEnvRequest.  # noqa: E501
        :rtype: str
        """
        return self._key_type

    @key_type.setter
    def key_type(self, key_type):
        """Sets the key_type of this AddCloudEnvRequest.


        :param key_type: The key_type of this AddCloudEnvRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and key_type is None:
            raise ValueError("Invalid value for `key_type`, must not be `None`")  # noqa: E501

        self._key_type = key_type

    @property
    def secret_key(self):
        """Gets the secret_key of this AddCloudEnvRequest.  # noqa: E501


        :return: The secret_key of this AddCloudEnvRequest.  # noqa: E501
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """Sets the secret_key of this AddCloudEnvRequest.


        :param secret_key: The secret_key of this AddCloudEnvRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and secret_key is None:
            raise ValueError("Invalid value for `secret_key`, must not be `None`")  # noqa: E501

        self._secret_key = secret_key

    @property
    def sync_period(self):
        """Gets the sync_period of this AddCloudEnvRequest.  # noqa: E501


        :return: The sync_period of this AddCloudEnvRequest.  # noqa: E501
        :rtype: int
        """
        return self._sync_period

    @sync_period.setter
    def sync_period(self, sync_period):
        """Sets the sync_period of this AddCloudEnvRequest.


        :param sync_period: The sync_period of this AddCloudEnvRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and sync_period is None:
            raise ValueError("Invalid value for `sync_period`, must not be `None`")  # noqa: E501

        self._sync_period = sync_period

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
        if issubclass(AddCloudEnvRequest, dict):
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
        if not isinstance(other, AddCloudEnvRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddCloudEnvRequest):
            return True

        return self.to_dict() != other.to_dict()
