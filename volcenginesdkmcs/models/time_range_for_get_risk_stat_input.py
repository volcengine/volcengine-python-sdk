# coding: utf-8

"""
    mcs

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class TimeRangeForGetRiskStatInput(object):
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
        'end_time_milli': 'int',
        'start_time_milli': 'int'
    }

    attribute_map = {
        'end_time_milli': 'EndTimeMilli',
        'start_time_milli': 'StartTimeMilli'
    }

    def __init__(self, end_time_milli=None, start_time_milli=None, _configuration=None):  # noqa: E501
        """TimeRangeForGetRiskStatInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._end_time_milli = None
        self._start_time_milli = None
        self.discriminator = None

        if end_time_milli is not None:
            self.end_time_milli = end_time_milli
        if start_time_milli is not None:
            self.start_time_milli = start_time_milli

    @property
    def end_time_milli(self):
        """Gets the end_time_milli of this TimeRangeForGetRiskStatInput.  # noqa: E501


        :return: The end_time_milli of this TimeRangeForGetRiskStatInput.  # noqa: E501
        :rtype: int
        """
        return self._end_time_milli

    @end_time_milli.setter
    def end_time_milli(self, end_time_milli):
        """Sets the end_time_milli of this TimeRangeForGetRiskStatInput.


        :param end_time_milli: The end_time_milli of this TimeRangeForGetRiskStatInput.  # noqa: E501
        :type: int
        """

        self._end_time_milli = end_time_milli

    @property
    def start_time_milli(self):
        """Gets the start_time_milli of this TimeRangeForGetRiskStatInput.  # noqa: E501


        :return: The start_time_milli of this TimeRangeForGetRiskStatInput.  # noqa: E501
        :rtype: int
        """
        return self._start_time_milli

    @start_time_milli.setter
    def start_time_milli(self, start_time_milli):
        """Sets the start_time_milli of this TimeRangeForGetRiskStatInput.


        :param start_time_milli: The start_time_milli of this TimeRangeForGetRiskStatInput.  # noqa: E501
        :type: int
        """

        self._start_time_milli = start_time_milli

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
        if issubclass(TimeRangeForGetRiskStatInput, dict):
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
        if not isinstance(other, TimeRangeForGetRiskStatInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TimeRangeForGetRiskStatInput):
            return True

        return self.to_dict() != other.to_dict()