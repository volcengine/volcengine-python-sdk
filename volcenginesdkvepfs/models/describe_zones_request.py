# coding: utf-8

"""
    vepfs

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeZonesRequest(object):
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
        'file_system_type': 'str',
        'region_id': 'str'
    }

    attribute_map = {
        'file_system_type': 'FileSystemType',
        'region_id': 'RegionId'
    }

    def __init__(self, file_system_type=None, region_id=None, _configuration=None):  # noqa: E501
        """DescribeZonesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._file_system_type = None
        self._region_id = None
        self.discriminator = None

        if file_system_type is not None:
            self.file_system_type = file_system_type
        if region_id is not None:
            self.region_id = region_id

    @property
    def file_system_type(self):
        """Gets the file_system_type of this DescribeZonesRequest.  # noqa: E501


        :return: The file_system_type of this DescribeZonesRequest.  # noqa: E501
        :rtype: str
        """
        return self._file_system_type

    @file_system_type.setter
    def file_system_type(self, file_system_type):
        """Sets the file_system_type of this DescribeZonesRequest.


        :param file_system_type: The file_system_type of this DescribeZonesRequest.  # noqa: E501
        :type: str
        """

        self._file_system_type = file_system_type

    @property
    def region_id(self):
        """Gets the region_id of this DescribeZonesRequest.  # noqa: E501


        :return: The region_id of this DescribeZonesRequest.  # noqa: E501
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this DescribeZonesRequest.


        :param region_id: The region_id of this DescribeZonesRequest.  # noqa: E501
        :type: str
        """

        self._region_id = region_id

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
        if issubclass(DescribeZonesRequest, dict):
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
        if not isinstance(other, DescribeZonesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeZonesRequest):
            return True

        return self.to_dict() != other.to_dict()
