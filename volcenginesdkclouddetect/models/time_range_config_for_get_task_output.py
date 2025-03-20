# coding: utf-8

"""
    cloud_detect

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class TimeRangeConfigForGetTaskOutput(object):
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
        'end_time': 'EndTimeForGetTaskOutput',
        'interval': 'int',
        'start_time': 'StartTimeForGetTaskOutput'
    }

    attribute_map = {
        'end_time': 'EndTime',
        'interval': 'Interval',
        'start_time': 'StartTime'
    }

    def __init__(self, end_time=None, interval=None, start_time=None, _configuration=None):  # noqa: E501
        """TimeRangeConfigForGetTaskOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._end_time = None
        self._interval = None
        self._start_time = None
        self.discriminator = None

        if end_time is not None:
            self.end_time = end_time
        if interval is not None:
            self.interval = interval
        if start_time is not None:
            self.start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this TimeRangeConfigForGetTaskOutput.  # noqa: E501


        :return: The end_time of this TimeRangeConfigForGetTaskOutput.  # noqa: E501
        :rtype: EndTimeForGetTaskOutput
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this TimeRangeConfigForGetTaskOutput.


        :param end_time: The end_time of this TimeRangeConfigForGetTaskOutput.  # noqa: E501
        :type: EndTimeForGetTaskOutput
        """

        self._end_time = end_time

    @property
    def interval(self):
        """Gets the interval of this TimeRangeConfigForGetTaskOutput.  # noqa: E501


        :return: The interval of this TimeRangeConfigForGetTaskOutput.  # noqa: E501
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this TimeRangeConfigForGetTaskOutput.


        :param interval: The interval of this TimeRangeConfigForGetTaskOutput.  # noqa: E501
        :type: int
        """

        self._interval = interval

    @property
    def start_time(self):
        """Gets the start_time of this TimeRangeConfigForGetTaskOutput.  # noqa: E501


        :return: The start_time of this TimeRangeConfigForGetTaskOutput.  # noqa: E501
        :rtype: StartTimeForGetTaskOutput
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this TimeRangeConfigForGetTaskOutput.


        :param start_time: The start_time of this TimeRangeConfigForGetTaskOutput.  # noqa: E501
        :type: StartTimeForGetTaskOutput
        """

        self._start_time = start_time

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
        if issubclass(TimeRangeConfigForGetTaskOutput, dict):
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
        if not isinstance(other, TimeRangeConfigForGetTaskOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TimeRangeConfigForGetTaskOutput):
            return True

        return self.to_dict() != other.to_dict()
