# coding: utf-8

"""
    dms

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class IncreaseSettingForCreateDataMigrateTaskInput(object):
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
        'interval': 'int',
        'times': 'int'
    }

    attribute_map = {
        'interval': 'Interval',
        'times': 'Times'
    }

    def __init__(self, interval=None, times=None, _configuration=None):  # noqa: E501
        """IncreaseSettingForCreateDataMigrateTaskInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._interval = None
        self._times = None
        self.discriminator = None

        if interval is not None:
            self.interval = interval
        if times is not None:
            self.times = times

    @property
    def interval(self):
        """Gets the interval of this IncreaseSettingForCreateDataMigrateTaskInput.  # noqa: E501


        :return: The interval of this IncreaseSettingForCreateDataMigrateTaskInput.  # noqa: E501
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this IncreaseSettingForCreateDataMigrateTaskInput.


        :param interval: The interval of this IncreaseSettingForCreateDataMigrateTaskInput.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                interval is not None and interval > 86400):  # noqa: E501
            raise ValueError("Invalid value for `interval`, must be a value less than or equal to `86400`")  # noqa: E501
        if (self._configuration.client_side_validation and
                interval is not None and interval < 3600):  # noqa: E501
            raise ValueError("Invalid value for `interval`, must be a value greater than or equal to `3600`")  # noqa: E501

        self._interval = interval

    @property
    def times(self):
        """Gets the times of this IncreaseSettingForCreateDataMigrateTaskInput.  # noqa: E501


        :return: The times of this IncreaseSettingForCreateDataMigrateTaskInput.  # noqa: E501
        :rtype: int
        """
        return self._times

    @times.setter
    def times(self, times):
        """Sets the times of this IncreaseSettingForCreateDataMigrateTaskInput.


        :param times: The times of this IncreaseSettingForCreateDataMigrateTaskInput.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                times is not None and times > 30):  # noqa: E501
            raise ValueError("Invalid value for `times`, must be a value less than or equal to `30`")  # noqa: E501
        if (self._configuration.client_side_validation and
                times is not None and times < 1):  # noqa: E501
            raise ValueError("Invalid value for `times`, must be a value greater than or equal to `1`")  # noqa: E501

        self._times = times

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
        if issubclass(IncreaseSettingForCreateDataMigrateTaskInput, dict):
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
        if not isinstance(other, IncreaseSettingForCreateDataMigrateTaskInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IncreaseSettingForCreateDataMigrateTaskInput):
            return True

        return self.to_dict() != other.to_dict()