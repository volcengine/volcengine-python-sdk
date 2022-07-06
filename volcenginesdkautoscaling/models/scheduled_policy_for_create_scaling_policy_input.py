# coding: utf-8

"""
    auto_scaling

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ScheduledPolicyForCreateScalingPolicyInput(object):
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
        'launch_time': 'str',
        'recurrence_end_time': 'str',
        'recurrence_type': 'str',
        'recurrence_value': 'str'
    }

    attribute_map = {
        'launch_time': 'LaunchTime',
        'recurrence_end_time': 'RecurrenceEndTime',
        'recurrence_type': 'RecurrenceType',
        'recurrence_value': 'RecurrenceValue'
    }

    def __init__(self, launch_time=None, recurrence_end_time=None, recurrence_type=None, recurrence_value=None, _configuration=None):  # noqa: E501
        """ScheduledPolicyForCreateScalingPolicyInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._launch_time = None
        self._recurrence_end_time = None
        self._recurrence_type = None
        self._recurrence_value = None
        self.discriminator = None

        if launch_time is not None:
            self.launch_time = launch_time
        if recurrence_end_time is not None:
            self.recurrence_end_time = recurrence_end_time
        if recurrence_type is not None:
            self.recurrence_type = recurrence_type
        if recurrence_value is not None:
            self.recurrence_value = recurrence_value

    @property
    def launch_time(self):
        """Gets the launch_time of this ScheduledPolicyForCreateScalingPolicyInput.  # noqa: E501


        :return: The launch_time of this ScheduledPolicyForCreateScalingPolicyInput.  # noqa: E501
        :rtype: str
        """
        return self._launch_time

    @launch_time.setter
    def launch_time(self, launch_time):
        """Sets the launch_time of this ScheduledPolicyForCreateScalingPolicyInput.


        :param launch_time: The launch_time of this ScheduledPolicyForCreateScalingPolicyInput.  # noqa: E501
        :type: str
        """

        self._launch_time = launch_time

    @property
    def recurrence_end_time(self):
        """Gets the recurrence_end_time of this ScheduledPolicyForCreateScalingPolicyInput.  # noqa: E501


        :return: The recurrence_end_time of this ScheduledPolicyForCreateScalingPolicyInput.  # noqa: E501
        :rtype: str
        """
        return self._recurrence_end_time

    @recurrence_end_time.setter
    def recurrence_end_time(self, recurrence_end_time):
        """Sets the recurrence_end_time of this ScheduledPolicyForCreateScalingPolicyInput.


        :param recurrence_end_time: The recurrence_end_time of this ScheduledPolicyForCreateScalingPolicyInput.  # noqa: E501
        :type: str
        """

        self._recurrence_end_time = recurrence_end_time

    @property
    def recurrence_type(self):
        """Gets the recurrence_type of this ScheduledPolicyForCreateScalingPolicyInput.  # noqa: E501


        :return: The recurrence_type of this ScheduledPolicyForCreateScalingPolicyInput.  # noqa: E501
        :rtype: str
        """
        return self._recurrence_type

    @recurrence_type.setter
    def recurrence_type(self, recurrence_type):
        """Sets the recurrence_type of this ScheduledPolicyForCreateScalingPolicyInput.


        :param recurrence_type: The recurrence_type of this ScheduledPolicyForCreateScalingPolicyInput.  # noqa: E501
        :type: str
        """

        self._recurrence_type = recurrence_type

    @property
    def recurrence_value(self):
        """Gets the recurrence_value of this ScheduledPolicyForCreateScalingPolicyInput.  # noqa: E501


        :return: The recurrence_value of this ScheduledPolicyForCreateScalingPolicyInput.  # noqa: E501
        :rtype: str
        """
        return self._recurrence_value

    @recurrence_value.setter
    def recurrence_value(self, recurrence_value):
        """Sets the recurrence_value of this ScheduledPolicyForCreateScalingPolicyInput.


        :param recurrence_value: The recurrence_value of this ScheduledPolicyForCreateScalingPolicyInput.  # noqa: E501
        :type: str
        """

        self._recurrence_value = recurrence_value

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
        if issubclass(ScheduledPolicyForCreateScalingPolicyInput, dict):
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
        if not isinstance(other, ScheduledPolicyForCreateScalingPolicyInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ScheduledPolicyForCreateScalingPolicyInput):
            return True

        return self.to_dict() != other.to_dict()
