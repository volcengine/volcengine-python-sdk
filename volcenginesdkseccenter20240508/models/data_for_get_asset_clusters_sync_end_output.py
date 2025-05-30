# coding: utf-8

"""
    seccenter20240508

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DataForGetAssetClustersSyncEndOutput(object):
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
        'latest_sync_time': 'int',
        'sync_processing': 'bool'
    }

    attribute_map = {
        'latest_sync_time': 'LatestSyncTime',
        'sync_processing': 'SyncProcessing'
    }

    def __init__(self, latest_sync_time=None, sync_processing=None, _configuration=None):  # noqa: E501
        """DataForGetAssetClustersSyncEndOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._latest_sync_time = None
        self._sync_processing = None
        self.discriminator = None

        if latest_sync_time is not None:
            self.latest_sync_time = latest_sync_time
        if sync_processing is not None:
            self.sync_processing = sync_processing

    @property
    def latest_sync_time(self):
        """Gets the latest_sync_time of this DataForGetAssetClustersSyncEndOutput.  # noqa: E501


        :return: The latest_sync_time of this DataForGetAssetClustersSyncEndOutput.  # noqa: E501
        :rtype: int
        """
        return self._latest_sync_time

    @latest_sync_time.setter
    def latest_sync_time(self, latest_sync_time):
        """Sets the latest_sync_time of this DataForGetAssetClustersSyncEndOutput.


        :param latest_sync_time: The latest_sync_time of this DataForGetAssetClustersSyncEndOutput.  # noqa: E501
        :type: int
        """

        self._latest_sync_time = latest_sync_time

    @property
    def sync_processing(self):
        """Gets the sync_processing of this DataForGetAssetClustersSyncEndOutput.  # noqa: E501


        :return: The sync_processing of this DataForGetAssetClustersSyncEndOutput.  # noqa: E501
        :rtype: bool
        """
        return self._sync_processing

    @sync_processing.setter
    def sync_processing(self, sync_processing):
        """Sets the sync_processing of this DataForGetAssetClustersSyncEndOutput.


        :param sync_processing: The sync_processing of this DataForGetAssetClustersSyncEndOutput.  # noqa: E501
        :type: bool
        """

        self._sync_processing = sync_processing

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
        if issubclass(DataForGetAssetClustersSyncEndOutput, dict):
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
        if not isinstance(other, DataForGetAssetClustersSyncEndOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataForGetAssetClustersSyncEndOutput):
            return True

        return self.to_dict() != other.to_dict()
