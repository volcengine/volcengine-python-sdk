# coding: utf-8

"""
    ecs

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class AvailableSpotResourceForDescribeSpotAdviceOutput(object):
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
        'average_spot_discount': 'int',
        'instance_type': 'str',
        'interruption_rate': 'int',
        'interruption_rate_range': 'str',
        'zone_id': 'str'
    }

    attribute_map = {
        'average_spot_discount': 'AverageSpotDiscount',
        'instance_type': 'InstanceType',
        'interruption_rate': 'InterruptionRate',
        'interruption_rate_range': 'InterruptionRateRange',
        'zone_id': 'ZoneId'
    }

    def __init__(self, average_spot_discount=None, instance_type=None, interruption_rate=None, interruption_rate_range=None, zone_id=None, _configuration=None):  # noqa: E501
        """AvailableSpotResourceForDescribeSpotAdviceOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._average_spot_discount = None
        self._instance_type = None
        self._interruption_rate = None
        self._interruption_rate_range = None
        self._zone_id = None
        self.discriminator = None

        if average_spot_discount is not None:
            self.average_spot_discount = average_spot_discount
        if instance_type is not None:
            self.instance_type = instance_type
        if interruption_rate is not None:
            self.interruption_rate = interruption_rate
        if interruption_rate_range is not None:
            self.interruption_rate_range = interruption_rate_range
        if zone_id is not None:
            self.zone_id = zone_id

    @property
    def average_spot_discount(self):
        """Gets the average_spot_discount of this AvailableSpotResourceForDescribeSpotAdviceOutput.  # noqa: E501


        :return: The average_spot_discount of this AvailableSpotResourceForDescribeSpotAdviceOutput.  # noqa: E501
        :rtype: int
        """
        return self._average_spot_discount

    @average_spot_discount.setter
    def average_spot_discount(self, average_spot_discount):
        """Sets the average_spot_discount of this AvailableSpotResourceForDescribeSpotAdviceOutput.


        :param average_spot_discount: The average_spot_discount of this AvailableSpotResourceForDescribeSpotAdviceOutput.  # noqa: E501
        :type: int
        """

        self._average_spot_discount = average_spot_discount

    @property
    def instance_type(self):
        """Gets the instance_type of this AvailableSpotResourceForDescribeSpotAdviceOutput.  # noqa: E501


        :return: The instance_type of this AvailableSpotResourceForDescribeSpotAdviceOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this AvailableSpotResourceForDescribeSpotAdviceOutput.


        :param instance_type: The instance_type of this AvailableSpotResourceForDescribeSpotAdviceOutput.  # noqa: E501
        :type: str
        """

        self._instance_type = instance_type

    @property
    def interruption_rate(self):
        """Gets the interruption_rate of this AvailableSpotResourceForDescribeSpotAdviceOutput.  # noqa: E501


        :return: The interruption_rate of this AvailableSpotResourceForDescribeSpotAdviceOutput.  # noqa: E501
        :rtype: int
        """
        return self._interruption_rate

    @interruption_rate.setter
    def interruption_rate(self, interruption_rate):
        """Sets the interruption_rate of this AvailableSpotResourceForDescribeSpotAdviceOutput.


        :param interruption_rate: The interruption_rate of this AvailableSpotResourceForDescribeSpotAdviceOutput.  # noqa: E501
        :type: int
        """

        self._interruption_rate = interruption_rate

    @property
    def interruption_rate_range(self):
        """Gets the interruption_rate_range of this AvailableSpotResourceForDescribeSpotAdviceOutput.  # noqa: E501


        :return: The interruption_rate_range of this AvailableSpotResourceForDescribeSpotAdviceOutput.  # noqa: E501
        :rtype: str
        """
        return self._interruption_rate_range

    @interruption_rate_range.setter
    def interruption_rate_range(self, interruption_rate_range):
        """Sets the interruption_rate_range of this AvailableSpotResourceForDescribeSpotAdviceOutput.


        :param interruption_rate_range: The interruption_rate_range of this AvailableSpotResourceForDescribeSpotAdviceOutput.  # noqa: E501
        :type: str
        """

        self._interruption_rate_range = interruption_rate_range

    @property
    def zone_id(self):
        """Gets the zone_id of this AvailableSpotResourceForDescribeSpotAdviceOutput.  # noqa: E501


        :return: The zone_id of this AvailableSpotResourceForDescribeSpotAdviceOutput.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this AvailableSpotResourceForDescribeSpotAdviceOutput.


        :param zone_id: The zone_id of this AvailableSpotResourceForDescribeSpotAdviceOutput.  # noqa: E501
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
        if issubclass(AvailableSpotResourceForDescribeSpotAdviceOutput, dict):
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
        if not isinstance(other, AvailableSpotResourceForDescribeSpotAdviceOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AvailableSpotResourceForDescribeSpotAdviceOutput):
            return True

        return self.to_dict() != other.to_dict()
