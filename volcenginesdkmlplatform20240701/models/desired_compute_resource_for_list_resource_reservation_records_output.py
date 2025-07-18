# coding: utf-8

"""
    ml_platform20240701

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DesiredComputeResourceForListResourceReservationRecordsOutput(object):
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
        'count': 'int',
        'instance_type_id': 'str',
        'zone_ids': 'list[str]'
    }

    attribute_map = {
        'count': 'Count',
        'instance_type_id': 'InstanceTypeId',
        'zone_ids': 'ZoneIds'
    }

    def __init__(self, count=None, instance_type_id=None, zone_ids=None, _configuration=None):  # noqa: E501
        """DesiredComputeResourceForListResourceReservationRecordsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._count = None
        self._instance_type_id = None
        self._zone_ids = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if instance_type_id is not None:
            self.instance_type_id = instance_type_id
        if zone_ids is not None:
            self.zone_ids = zone_ids

    @property
    def count(self):
        """Gets the count of this DesiredComputeResourceForListResourceReservationRecordsOutput.  # noqa: E501


        :return: The count of this DesiredComputeResourceForListResourceReservationRecordsOutput.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this DesiredComputeResourceForListResourceReservationRecordsOutput.


        :param count: The count of this DesiredComputeResourceForListResourceReservationRecordsOutput.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def instance_type_id(self):
        """Gets the instance_type_id of this DesiredComputeResourceForListResourceReservationRecordsOutput.  # noqa: E501


        :return: The instance_type_id of this DesiredComputeResourceForListResourceReservationRecordsOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_type_id

    @instance_type_id.setter
    def instance_type_id(self, instance_type_id):
        """Sets the instance_type_id of this DesiredComputeResourceForListResourceReservationRecordsOutput.


        :param instance_type_id: The instance_type_id of this DesiredComputeResourceForListResourceReservationRecordsOutput.  # noqa: E501
        :type: str
        """

        self._instance_type_id = instance_type_id

    @property
    def zone_ids(self):
        """Gets the zone_ids of this DesiredComputeResourceForListResourceReservationRecordsOutput.  # noqa: E501


        :return: The zone_ids of this DesiredComputeResourceForListResourceReservationRecordsOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._zone_ids

    @zone_ids.setter
    def zone_ids(self, zone_ids):
        """Sets the zone_ids of this DesiredComputeResourceForListResourceReservationRecordsOutput.


        :param zone_ids: The zone_ids of this DesiredComputeResourceForListResourceReservationRecordsOutput.  # noqa: E501
        :type: list[str]
        """

        self._zone_ids = zone_ids

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
        if issubclass(DesiredComputeResourceForListResourceReservationRecordsOutput, dict):
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
        if not isinstance(other, DesiredComputeResourceForListResourceReservationRecordsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DesiredComputeResourceForListResourceReservationRecordsOutput):
            return True

        return self.to_dict() != other.to_dict()
