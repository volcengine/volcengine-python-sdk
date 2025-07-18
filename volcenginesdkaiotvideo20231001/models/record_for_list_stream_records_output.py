# coding: utf-8

"""
    aiotvideo20231001

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class RecordForListStreamRecordsOutput(object):
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
        'duration': 'int',
        'end_time': 'int',
        'format': 'str',
        'start_time': 'int'
    }

    attribute_map = {
        'duration': 'Duration',
        'end_time': 'EndTime',
        'format': 'Format',
        'start_time': 'StartTime'
    }

    def __init__(self, duration=None, end_time=None, format=None, start_time=None, _configuration=None):  # noqa: E501
        """RecordForListStreamRecordsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._duration = None
        self._end_time = None
        self._format = None
        self._start_time = None
        self.discriminator = None

        if duration is not None:
            self.duration = duration
        if end_time is not None:
            self.end_time = end_time
        if format is not None:
            self.format = format
        if start_time is not None:
            self.start_time = start_time

    @property
    def duration(self):
        """Gets the duration of this RecordForListStreamRecordsOutput.  # noqa: E501


        :return: The duration of this RecordForListStreamRecordsOutput.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this RecordForListStreamRecordsOutput.


        :param duration: The duration of this RecordForListStreamRecordsOutput.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def end_time(self):
        """Gets the end_time of this RecordForListStreamRecordsOutput.  # noqa: E501


        :return: The end_time of this RecordForListStreamRecordsOutput.  # noqa: E501
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this RecordForListStreamRecordsOutput.


        :param end_time: The end_time of this RecordForListStreamRecordsOutput.  # noqa: E501
        :type: int
        """

        self._end_time = end_time

    @property
    def format(self):
        """Gets the format of this RecordForListStreamRecordsOutput.  # noqa: E501


        :return: The format of this RecordForListStreamRecordsOutput.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this RecordForListStreamRecordsOutput.


        :param format: The format of this RecordForListStreamRecordsOutput.  # noqa: E501
        :type: str
        """

        self._format = format

    @property
    def start_time(self):
        """Gets the start_time of this RecordForListStreamRecordsOutput.  # noqa: E501


        :return: The start_time of this RecordForListStreamRecordsOutput.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this RecordForListStreamRecordsOutput.


        :param start_time: The start_time of this RecordForListStreamRecordsOutput.  # noqa: E501
        :type: int
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
        if issubclass(RecordForListStreamRecordsOutput, dict):
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
        if not isinstance(other, RecordForListStreamRecordsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RecordForListStreamRecordsOutput):
            return True

        return self.to_dict() != other.to_dict()
