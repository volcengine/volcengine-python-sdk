# coding: utf-8

"""
    cdn

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class BandwidthLimitRuleForDescribeCdnConfigOutput(object):
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
        'bandwidth_limit_action': 'BandwidthLimitActionForDescribeCdnConfigOutput',
        'condition': 'ConditionForDescribeCdnConfigOutput'
    }

    attribute_map = {
        'bandwidth_limit_action': 'BandwidthLimitAction',
        'condition': 'Condition'
    }

    def __init__(self, bandwidth_limit_action=None, condition=None, _configuration=None):  # noqa: E501
        """BandwidthLimitRuleForDescribeCdnConfigOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bandwidth_limit_action = None
        self._condition = None
        self.discriminator = None

        if bandwidth_limit_action is not None:
            self.bandwidth_limit_action = bandwidth_limit_action
        if condition is not None:
            self.condition = condition

    @property
    def bandwidth_limit_action(self):
        """Gets the bandwidth_limit_action of this BandwidthLimitRuleForDescribeCdnConfigOutput.  # noqa: E501


        :return: The bandwidth_limit_action of this BandwidthLimitRuleForDescribeCdnConfigOutput.  # noqa: E501
        :rtype: BandwidthLimitActionForDescribeCdnConfigOutput
        """
        return self._bandwidth_limit_action

    @bandwidth_limit_action.setter
    def bandwidth_limit_action(self, bandwidth_limit_action):
        """Sets the bandwidth_limit_action of this BandwidthLimitRuleForDescribeCdnConfigOutput.


        :param bandwidth_limit_action: The bandwidth_limit_action of this BandwidthLimitRuleForDescribeCdnConfigOutput.  # noqa: E501
        :type: BandwidthLimitActionForDescribeCdnConfigOutput
        """

        self._bandwidth_limit_action = bandwidth_limit_action

    @property
    def condition(self):
        """Gets the condition of this BandwidthLimitRuleForDescribeCdnConfigOutput.  # noqa: E501


        :return: The condition of this BandwidthLimitRuleForDescribeCdnConfigOutput.  # noqa: E501
        :rtype: ConditionForDescribeCdnConfigOutput
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this BandwidthLimitRuleForDescribeCdnConfigOutput.


        :param condition: The condition of this BandwidthLimitRuleForDescribeCdnConfigOutput.  # noqa: E501
        :type: ConditionForDescribeCdnConfigOutput
        """

        self._condition = condition

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
        if issubclass(BandwidthLimitRuleForDescribeCdnConfigOutput, dict):
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
        if not isinstance(other, BandwidthLimitRuleForDescribeCdnConfigOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BandwidthLimitRuleForDescribeCdnConfigOutput):
            return True

        return self.to_dict() != other.to_dict()