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


class CreateScalingPolicyRequest(object):
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
        'adjustment_type': 'str',
        'adjustment_value': 'int',
        'alarm_policy': 'AlarmPolicyForCreateScalingPolicyInput',
        'cooldown': 'int',
        'scaling_group_id': 'str',
        'scaling_policy_name': 'str',
        'scaling_policy_type': 'str',
        'scheduled_policy': 'ScheduledPolicyForCreateScalingPolicyInput'
    }

    attribute_map = {
        'adjustment_type': 'AdjustmentType',
        'adjustment_value': 'AdjustmentValue',
        'alarm_policy': 'AlarmPolicy',
        'cooldown': 'Cooldown',
        'scaling_group_id': 'ScalingGroupId',
        'scaling_policy_name': 'ScalingPolicyName',
        'scaling_policy_type': 'ScalingPolicyType',
        'scheduled_policy': 'ScheduledPolicy'
    }

    def __init__(self, adjustment_type=None, adjustment_value=None, alarm_policy=None, cooldown=None, scaling_group_id=None, scaling_policy_name=None, scaling_policy_type=None, scheduled_policy=None, _configuration=None):  # noqa: E501
        """CreateScalingPolicyRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._adjustment_type = None
        self._adjustment_value = None
        self._alarm_policy = None
        self._cooldown = None
        self._scaling_group_id = None
        self._scaling_policy_name = None
        self._scaling_policy_type = None
        self._scheduled_policy = None
        self.discriminator = None

        if adjustment_type is not None:
            self.adjustment_type = adjustment_type
        if adjustment_value is not None:
            self.adjustment_value = adjustment_value
        if alarm_policy is not None:
            self.alarm_policy = alarm_policy
        if cooldown is not None:
            self.cooldown = cooldown
        self.scaling_group_id = scaling_group_id
        self.scaling_policy_name = scaling_policy_name
        self.scaling_policy_type = scaling_policy_type
        if scheduled_policy is not None:
            self.scheduled_policy = scheduled_policy

    @property
    def adjustment_type(self):
        """Gets the adjustment_type of this CreateScalingPolicyRequest.  # noqa: E501


        :return: The adjustment_type of this CreateScalingPolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._adjustment_type

    @adjustment_type.setter
    def adjustment_type(self, adjustment_type):
        """Sets the adjustment_type of this CreateScalingPolicyRequest.


        :param adjustment_type: The adjustment_type of this CreateScalingPolicyRequest.  # noqa: E501
        :type: str
        """

        self._adjustment_type = adjustment_type

    @property
    def adjustment_value(self):
        """Gets the adjustment_value of this CreateScalingPolicyRequest.  # noqa: E501


        :return: The adjustment_value of this CreateScalingPolicyRequest.  # noqa: E501
        :rtype: int
        """
        return self._adjustment_value

    @adjustment_value.setter
    def adjustment_value(self, adjustment_value):
        """Sets the adjustment_value of this CreateScalingPolicyRequest.


        :param adjustment_value: The adjustment_value of this CreateScalingPolicyRequest.  # noqa: E501
        :type: int
        """

        self._adjustment_value = adjustment_value

    @property
    def alarm_policy(self):
        """Gets the alarm_policy of this CreateScalingPolicyRequest.  # noqa: E501


        :return: The alarm_policy of this CreateScalingPolicyRequest.  # noqa: E501
        :rtype: AlarmPolicyForCreateScalingPolicyInput
        """
        return self._alarm_policy

    @alarm_policy.setter
    def alarm_policy(self, alarm_policy):
        """Sets the alarm_policy of this CreateScalingPolicyRequest.


        :param alarm_policy: The alarm_policy of this CreateScalingPolicyRequest.  # noqa: E501
        :type: AlarmPolicyForCreateScalingPolicyInput
        """

        self._alarm_policy = alarm_policy

    @property
    def cooldown(self):
        """Gets the cooldown of this CreateScalingPolicyRequest.  # noqa: E501


        :return: The cooldown of this CreateScalingPolicyRequest.  # noqa: E501
        :rtype: int
        """
        return self._cooldown

    @cooldown.setter
    def cooldown(self, cooldown):
        """Sets the cooldown of this CreateScalingPolicyRequest.


        :param cooldown: The cooldown of this CreateScalingPolicyRequest.  # noqa: E501
        :type: int
        """

        self._cooldown = cooldown

    @property
    def scaling_group_id(self):
        """Gets the scaling_group_id of this CreateScalingPolicyRequest.  # noqa: E501


        :return: The scaling_group_id of this CreateScalingPolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._scaling_group_id

    @scaling_group_id.setter
    def scaling_group_id(self, scaling_group_id):
        """Sets the scaling_group_id of this CreateScalingPolicyRequest.


        :param scaling_group_id: The scaling_group_id of this CreateScalingPolicyRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and scaling_group_id is None:
            raise ValueError("Invalid value for `scaling_group_id`, must not be `None`")  # noqa: E501

        self._scaling_group_id = scaling_group_id

    @property
    def scaling_policy_name(self):
        """Gets the scaling_policy_name of this CreateScalingPolicyRequest.  # noqa: E501


        :return: The scaling_policy_name of this CreateScalingPolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._scaling_policy_name

    @scaling_policy_name.setter
    def scaling_policy_name(self, scaling_policy_name):
        """Sets the scaling_policy_name of this CreateScalingPolicyRequest.


        :param scaling_policy_name: The scaling_policy_name of this CreateScalingPolicyRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and scaling_policy_name is None:
            raise ValueError("Invalid value for `scaling_policy_name`, must not be `None`")  # noqa: E501

        self._scaling_policy_name = scaling_policy_name

    @property
    def scaling_policy_type(self):
        """Gets the scaling_policy_type of this CreateScalingPolicyRequest.  # noqa: E501


        :return: The scaling_policy_type of this CreateScalingPolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._scaling_policy_type

    @scaling_policy_type.setter
    def scaling_policy_type(self, scaling_policy_type):
        """Sets the scaling_policy_type of this CreateScalingPolicyRequest.


        :param scaling_policy_type: The scaling_policy_type of this CreateScalingPolicyRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and scaling_policy_type is None:
            raise ValueError("Invalid value for `scaling_policy_type`, must not be `None`")  # noqa: E501

        self._scaling_policy_type = scaling_policy_type

    @property
    def scheduled_policy(self):
        """Gets the scheduled_policy of this CreateScalingPolicyRequest.  # noqa: E501


        :return: The scheduled_policy of this CreateScalingPolicyRequest.  # noqa: E501
        :rtype: ScheduledPolicyForCreateScalingPolicyInput
        """
        return self._scheduled_policy

    @scheduled_policy.setter
    def scheduled_policy(self, scheduled_policy):
        """Sets the scheduled_policy of this CreateScalingPolicyRequest.


        :param scheduled_policy: The scheduled_policy of this CreateScalingPolicyRequest.  # noqa: E501
        :type: ScheduledPolicyForCreateScalingPolicyInput
        """

        self._scheduled_policy = scheduled_policy

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
        if issubclass(CreateScalingPolicyRequest, dict):
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
        if not isinstance(other, CreateScalingPolicyRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateScalingPolicyRequest):
            return True

        return self.to_dict() != other.to_dict()
