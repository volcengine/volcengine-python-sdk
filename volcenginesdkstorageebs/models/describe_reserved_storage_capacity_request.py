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


class DescribeReservedStorageCapacityRequest(object):
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
        'page_number': 'str',
        'page_size': 'str',
        'reserved_storage_capacity_ids': 'list[str]',
        'reserved_storage_capacity_name': 'str',
        'status': 'str',
        'volume_type': 'str',
        'zone_id': 'str'
    }

    attribute_map = {
        'page_number': 'PageNumber',
        'page_size': 'PageSize',
        'reserved_storage_capacity_ids': 'ReservedStorageCapacityIds',
        'reserved_storage_capacity_name': 'ReservedStorageCapacityName',
        'status': 'Status',
        'volume_type': 'VolumeType',
        'zone_id': 'ZoneId'
    }

    def __init__(self, page_number=None, page_size=None, reserved_storage_capacity_ids=None, reserved_storage_capacity_name=None, status=None, volume_type=None, zone_id=None, _configuration=None):  # noqa: E501
        """DescribeReservedStorageCapacityRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._page_number = None
        self._page_size = None
        self._reserved_storage_capacity_ids = None
        self._reserved_storage_capacity_name = None
        self._status = None
        self._volume_type = None
        self._zone_id = None
        self.discriminator = None

        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if reserved_storage_capacity_ids is not None:
            self.reserved_storage_capacity_ids = reserved_storage_capacity_ids
        if reserved_storage_capacity_name is not None:
            self.reserved_storage_capacity_name = reserved_storage_capacity_name
        if status is not None:
            self.status = status
        if volume_type is not None:
            self.volume_type = volume_type
        if zone_id is not None:
            self.zone_id = zone_id

    @property
    def page_number(self):
        """Gets the page_number of this DescribeReservedStorageCapacityRequest.  # noqa: E501


        :return: The page_number of this DescribeReservedStorageCapacityRequest.  # noqa: E501
        :rtype: str
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this DescribeReservedStorageCapacityRequest.


        :param page_number: The page_number of this DescribeReservedStorageCapacityRequest.  # noqa: E501
        :type: str
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this DescribeReservedStorageCapacityRequest.  # noqa: E501


        :return: The page_size of this DescribeReservedStorageCapacityRequest.  # noqa: E501
        :rtype: str
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this DescribeReservedStorageCapacityRequest.


        :param page_size: The page_size of this DescribeReservedStorageCapacityRequest.  # noqa: E501
        :type: str
        """

        self._page_size = page_size

    @property
    def reserved_storage_capacity_ids(self):
        """Gets the reserved_storage_capacity_ids of this DescribeReservedStorageCapacityRequest.  # noqa: E501


        :return: The reserved_storage_capacity_ids of this DescribeReservedStorageCapacityRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._reserved_storage_capacity_ids

    @reserved_storage_capacity_ids.setter
    def reserved_storage_capacity_ids(self, reserved_storage_capacity_ids):
        """Sets the reserved_storage_capacity_ids of this DescribeReservedStorageCapacityRequest.


        :param reserved_storage_capacity_ids: The reserved_storage_capacity_ids of this DescribeReservedStorageCapacityRequest.  # noqa: E501
        :type: list[str]
        """

        self._reserved_storage_capacity_ids = reserved_storage_capacity_ids

    @property
    def reserved_storage_capacity_name(self):
        """Gets the reserved_storage_capacity_name of this DescribeReservedStorageCapacityRequest.  # noqa: E501


        :return: The reserved_storage_capacity_name of this DescribeReservedStorageCapacityRequest.  # noqa: E501
        :rtype: str
        """
        return self._reserved_storage_capacity_name

    @reserved_storage_capacity_name.setter
    def reserved_storage_capacity_name(self, reserved_storage_capacity_name):
        """Sets the reserved_storage_capacity_name of this DescribeReservedStorageCapacityRequest.


        :param reserved_storage_capacity_name: The reserved_storage_capacity_name of this DescribeReservedStorageCapacityRequest.  # noqa: E501
        :type: str
        """

        self._reserved_storage_capacity_name = reserved_storage_capacity_name

    @property
    def status(self):
        """Gets the status of this DescribeReservedStorageCapacityRequest.  # noqa: E501


        :return: The status of this DescribeReservedStorageCapacityRequest.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DescribeReservedStorageCapacityRequest.


        :param status: The status of this DescribeReservedStorageCapacityRequest.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def volume_type(self):
        """Gets the volume_type of this DescribeReservedStorageCapacityRequest.  # noqa: E501


        :return: The volume_type of this DescribeReservedStorageCapacityRequest.  # noqa: E501
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        """Sets the volume_type of this DescribeReservedStorageCapacityRequest.


        :param volume_type: The volume_type of this DescribeReservedStorageCapacityRequest.  # noqa: E501
        :type: str
        """

        self._volume_type = volume_type

    @property
    def zone_id(self):
        """Gets the zone_id of this DescribeReservedStorageCapacityRequest.  # noqa: E501


        :return: The zone_id of this DescribeReservedStorageCapacityRequest.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this DescribeReservedStorageCapacityRequest.


        :param zone_id: The zone_id of this DescribeReservedStorageCapacityRequest.  # noqa: E501
        :type: str
        """

        self._zone_id = zone_id

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
        if issubclass(DescribeReservedStorageCapacityRequest, dict):
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
        if not isinstance(other, DescribeReservedStorageCapacityRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeReservedStorageCapacityRequest):
            return True

        return self.to_dict() != other.to_dict()