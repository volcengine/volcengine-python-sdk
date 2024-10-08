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


class WeightFailoverInfoForDescribeDnsScheduleOutput(object):
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
        'alarm_id': 'str',
        'vendor': 'str',
        'weight_failover_id': 'str'
    }

    attribute_map = {
        'alarm_id': 'AlarmId',
        'vendor': 'Vendor',
        'weight_failover_id': 'WeightFailoverId'
    }

    def __init__(self, alarm_id=None, vendor=None, weight_failover_id=None, _configuration=None):  # noqa: E501
        """WeightFailoverInfoForDescribeDnsScheduleOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._alarm_id = None
        self._vendor = None
        self._weight_failover_id = None
        self.discriminator = None

        if alarm_id is not None:
            self.alarm_id = alarm_id
        if vendor is not None:
            self.vendor = vendor
        if weight_failover_id is not None:
            self.weight_failover_id = weight_failover_id

    @property
    def alarm_id(self):
        """Gets the alarm_id of this WeightFailoverInfoForDescribeDnsScheduleOutput.  # noqa: E501


        :return: The alarm_id of this WeightFailoverInfoForDescribeDnsScheduleOutput.  # noqa: E501
        :rtype: str
        """
        return self._alarm_id

    @alarm_id.setter
    def alarm_id(self, alarm_id):
        """Sets the alarm_id of this WeightFailoverInfoForDescribeDnsScheduleOutput.


        :param alarm_id: The alarm_id of this WeightFailoverInfoForDescribeDnsScheduleOutput.  # noqa: E501
        :type: str
        """

        self._alarm_id = alarm_id

    @property
    def vendor(self):
        """Gets the vendor of this WeightFailoverInfoForDescribeDnsScheduleOutput.  # noqa: E501


        :return: The vendor of this WeightFailoverInfoForDescribeDnsScheduleOutput.  # noqa: E501
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this WeightFailoverInfoForDescribeDnsScheduleOutput.


        :param vendor: The vendor of this WeightFailoverInfoForDescribeDnsScheduleOutput.  # noqa: E501
        :type: str
        """

        self._vendor = vendor

    @property
    def weight_failover_id(self):
        """Gets the weight_failover_id of this WeightFailoverInfoForDescribeDnsScheduleOutput.  # noqa: E501


        :return: The weight_failover_id of this WeightFailoverInfoForDescribeDnsScheduleOutput.  # noqa: E501
        :rtype: str
        """
        return self._weight_failover_id

    @weight_failover_id.setter
    def weight_failover_id(self, weight_failover_id):
        """Sets the weight_failover_id of this WeightFailoverInfoForDescribeDnsScheduleOutput.


        :param weight_failover_id: The weight_failover_id of this WeightFailoverInfoForDescribeDnsScheduleOutput.  # noqa: E501
        :type: str
        """

        self._weight_failover_id = weight_failover_id

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
        if issubclass(WeightFailoverInfoForDescribeDnsScheduleOutput, dict):
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
        if not isinstance(other, WeightFailoverInfoForDescribeDnsScheduleOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WeightFailoverInfoForDescribeDnsScheduleOutput):
            return True

        return self.to_dict() != other.to_dict()
