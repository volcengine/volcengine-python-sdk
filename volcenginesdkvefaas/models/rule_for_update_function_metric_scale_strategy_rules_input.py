# coding: utf-8

"""
    vefaas

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class RuleForUpdateFunctionMetricScaleStrategyRulesInput(object):
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
        'metric_type': 'str',
        'target': 'int'
    }

    attribute_map = {
        'metric_type': 'MetricType',
        'target': 'Target'
    }

    def __init__(self, metric_type=None, target=None, _configuration=None):  # noqa: E501
        """RuleForUpdateFunctionMetricScaleStrategyRulesInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._metric_type = None
        self._target = None
        self.discriminator = None

        if metric_type is not None:
            self.metric_type = metric_type
        if target is not None:
            self.target = target

    @property
    def metric_type(self):
        """Gets the metric_type of this RuleForUpdateFunctionMetricScaleStrategyRulesInput.  # noqa: E501


        :return: The metric_type of this RuleForUpdateFunctionMetricScaleStrategyRulesInput.  # noqa: E501
        :rtype: str
        """
        return self._metric_type

    @metric_type.setter
    def metric_type(self, metric_type):
        """Sets the metric_type of this RuleForUpdateFunctionMetricScaleStrategyRulesInput.


        :param metric_type: The metric_type of this RuleForUpdateFunctionMetricScaleStrategyRulesInput.  # noqa: E501
        :type: str
        """

        self._metric_type = metric_type

    @property
    def target(self):
        """Gets the target of this RuleForUpdateFunctionMetricScaleStrategyRulesInput.  # noqa: E501


        :return: The target of this RuleForUpdateFunctionMetricScaleStrategyRulesInput.  # noqa: E501
        :rtype: int
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this RuleForUpdateFunctionMetricScaleStrategyRulesInput.


        :param target: The target of this RuleForUpdateFunctionMetricScaleStrategyRulesInput.  # noqa: E501
        :type: int
        """

        self._target = target

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
        if issubclass(RuleForUpdateFunctionMetricScaleStrategyRulesInput, dict):
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
        if not isinstance(other, RuleForUpdateFunctionMetricScaleStrategyRulesInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RuleForUpdateFunctionMetricScaleStrategyRulesInput):
            return True

        return self.to_dict() != other.to_dict()
