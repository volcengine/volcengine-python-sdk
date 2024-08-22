# coding: utf-8

"""
    mcdn

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DomainSyncStatusStateForListCloudAccountsOutput(object):
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
        'last_sync_at': 'int',
        'sync_status': 'str'
    }

    attribute_map = {
        'last_sync_at': 'LastSyncAt',
        'sync_status': 'SyncStatus'
    }

    def __init__(self, last_sync_at=None, sync_status=None, _configuration=None):  # noqa: E501
        """DomainSyncStatusStateForListCloudAccountsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._last_sync_at = None
        self._sync_status = None
        self.discriminator = None

        if last_sync_at is not None:
            self.last_sync_at = last_sync_at
        if sync_status is not None:
            self.sync_status = sync_status

    @property
    def last_sync_at(self):
        """Gets the last_sync_at of this DomainSyncStatusStateForListCloudAccountsOutput.  # noqa: E501


        :return: The last_sync_at of this DomainSyncStatusStateForListCloudAccountsOutput.  # noqa: E501
        :rtype: int
        """
        return self._last_sync_at

    @last_sync_at.setter
    def last_sync_at(self, last_sync_at):
        """Sets the last_sync_at of this DomainSyncStatusStateForListCloudAccountsOutput.


        :param last_sync_at: The last_sync_at of this DomainSyncStatusStateForListCloudAccountsOutput.  # noqa: E501
        :type: int
        """

        self._last_sync_at = last_sync_at

    @property
    def sync_status(self):
        """Gets the sync_status of this DomainSyncStatusStateForListCloudAccountsOutput.  # noqa: E501


        :return: The sync_status of this DomainSyncStatusStateForListCloudAccountsOutput.  # noqa: E501
        :rtype: str
        """
        return self._sync_status

    @sync_status.setter
    def sync_status(self, sync_status):
        """Sets the sync_status of this DomainSyncStatusStateForListCloudAccountsOutput.


        :param sync_status: The sync_status of this DomainSyncStatusStateForListCloudAccountsOutput.  # noqa: E501
        :type: str
        """

        self._sync_status = sync_status

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
        if issubclass(DomainSyncStatusStateForListCloudAccountsOutput, dict):
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
        if not isinstance(other, DomainSyncStatusStateForListCloudAccountsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DomainSyncStatusStateForListCloudAccountsOutput):
            return True

        return self.to_dict() != other.to_dict()
