# coding: utf-8

"""
    storage_ebs

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ModifyVolumeExtraPerformanceRequest(object):
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
        'extra_performance_iops': 'int',
        'extra_performance_throughput_mb': 'int',
        'extra_performance_type_id': 'str',
        'volume_id': 'str'
    }

    attribute_map = {
        'extra_performance_iops': 'ExtraPerformanceIOPS',
        'extra_performance_throughput_mb': 'ExtraPerformanceThroughputMB',
        'extra_performance_type_id': 'ExtraPerformanceTypeId',
        'volume_id': 'VolumeId'
    }

    def __init__(self, extra_performance_iops=None, extra_performance_throughput_mb=None, extra_performance_type_id=None, volume_id=None, _configuration=None):  # noqa: E501
        """ModifyVolumeExtraPerformanceRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._extra_performance_iops = None
        self._extra_performance_throughput_mb = None
        self._extra_performance_type_id = None
        self._volume_id = None
        self.discriminator = None

        if extra_performance_iops is not None:
            self.extra_performance_iops = extra_performance_iops
        if extra_performance_throughput_mb is not None:
            self.extra_performance_throughput_mb = extra_performance_throughput_mb
        self.extra_performance_type_id = extra_performance_type_id
        self.volume_id = volume_id

    @property
    def extra_performance_iops(self):
        """Gets the extra_performance_iops of this ModifyVolumeExtraPerformanceRequest.  # noqa: E501


        :return: The extra_performance_iops of this ModifyVolumeExtraPerformanceRequest.  # noqa: E501
        :rtype: int
        """
        return self._extra_performance_iops

    @extra_performance_iops.setter
    def extra_performance_iops(self, extra_performance_iops):
        """Sets the extra_performance_iops of this ModifyVolumeExtraPerformanceRequest.


        :param extra_performance_iops: The extra_performance_iops of this ModifyVolumeExtraPerformanceRequest.  # noqa: E501
        :type: int
        """

        self._extra_performance_iops = extra_performance_iops

    @property
    def extra_performance_throughput_mb(self):
        """Gets the extra_performance_throughput_mb of this ModifyVolumeExtraPerformanceRequest.  # noqa: E501


        :return: The extra_performance_throughput_mb of this ModifyVolumeExtraPerformanceRequest.  # noqa: E501
        :rtype: int
        """
        return self._extra_performance_throughput_mb

    @extra_performance_throughput_mb.setter
    def extra_performance_throughput_mb(self, extra_performance_throughput_mb):
        """Sets the extra_performance_throughput_mb of this ModifyVolumeExtraPerformanceRequest.


        :param extra_performance_throughput_mb: The extra_performance_throughput_mb of this ModifyVolumeExtraPerformanceRequest.  # noqa: E501
        :type: int
        """

        self._extra_performance_throughput_mb = extra_performance_throughput_mb

    @property
    def extra_performance_type_id(self):
        """Gets the extra_performance_type_id of this ModifyVolumeExtraPerformanceRequest.  # noqa: E501


        :return: The extra_performance_type_id of this ModifyVolumeExtraPerformanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._extra_performance_type_id

    @extra_performance_type_id.setter
    def extra_performance_type_id(self, extra_performance_type_id):
        """Sets the extra_performance_type_id of this ModifyVolumeExtraPerformanceRequest.


        :param extra_performance_type_id: The extra_performance_type_id of this ModifyVolumeExtraPerformanceRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and extra_performance_type_id is None:
            raise ValueError("Invalid value for `extra_performance_type_id`, must not be `None`")  # noqa: E501
        allowed_values = ["IOPS", "Balance", "Throughput"]  # noqa: E501
        if (self._configuration.client_side_validation and
                extra_performance_type_id not in allowed_values):
            raise ValueError(
                "Invalid value for `extra_performance_type_id` ({0}), must be one of {1}"  # noqa: E501
                .format(extra_performance_type_id, allowed_values)
            )

        self._extra_performance_type_id = extra_performance_type_id

    @property
    def volume_id(self):
        """Gets the volume_id of this ModifyVolumeExtraPerformanceRequest.  # noqa: E501


        :return: The volume_id of this ModifyVolumeExtraPerformanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """Sets the volume_id of this ModifyVolumeExtraPerformanceRequest.


        :param volume_id: The volume_id of this ModifyVolumeExtraPerformanceRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and volume_id is None:
            raise ValueError("Invalid value for `volume_id`, must not be `None`")  # noqa: E501

        self._volume_id = volume_id

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
        if issubclass(ModifyVolumeExtraPerformanceRequest, dict):
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
        if not isinstance(other, ModifyVolumeExtraPerformanceRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModifyVolumeExtraPerformanceRequest):
            return True

        return self.to_dict() != other.to_dict()
