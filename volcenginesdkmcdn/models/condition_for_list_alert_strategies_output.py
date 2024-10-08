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


class ConditionForListAlertStrategiesOutput(object):
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
        'format': 'str',
        'metric_id': 'str',
        'operator': 'str',
        'period': 'int',
        'sensitivity': 'str',
        'threshold_type': 'str',
        'value': 'float'
    }

    attribute_map = {
        'format': 'Format',
        'metric_id': 'MetricId',
        'operator': 'Operator',
        'period': 'Period',
        'sensitivity': 'Sensitivity',
        'threshold_type': 'ThresholdType',
        'value': 'Value'
    }

    def __init__(self, format=None, metric_id=None, operator=None, period=None, sensitivity=None, threshold_type=None, value=None, _configuration=None):  # noqa: E501
        """ConditionForListAlertStrategiesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._format = None
        self._metric_id = None
        self._operator = None
        self._period = None
        self._sensitivity = None
        self._threshold_type = None
        self._value = None
        self.discriminator = None

        if format is not None:
            self.format = format
        if metric_id is not None:
            self.metric_id = metric_id
        if operator is not None:
            self.operator = operator
        if period is not None:
            self.period = period
        if sensitivity is not None:
            self.sensitivity = sensitivity
        if threshold_type is not None:
            self.threshold_type = threshold_type
        if value is not None:
            self.value = value

    @property
    def format(self):
        """Gets the format of this ConditionForListAlertStrategiesOutput.  # noqa: E501


        :return: The format of this ConditionForListAlertStrategiesOutput.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this ConditionForListAlertStrategiesOutput.


        :param format: The format of this ConditionForListAlertStrategiesOutput.  # noqa: E501
        :type: str
        """

        self._format = format

    @property
    def metric_id(self):
        """Gets the metric_id of this ConditionForListAlertStrategiesOutput.  # noqa: E501


        :return: The metric_id of this ConditionForListAlertStrategiesOutput.  # noqa: E501
        :rtype: str
        """
        return self._metric_id

    @metric_id.setter
    def metric_id(self, metric_id):
        """Sets the metric_id of this ConditionForListAlertStrategiesOutput.


        :param metric_id: The metric_id of this ConditionForListAlertStrategiesOutput.  # noqa: E501
        :type: str
        """

        self._metric_id = metric_id

    @property
    def operator(self):
        """Gets the operator of this ConditionForListAlertStrategiesOutput.  # noqa: E501


        :return: The operator of this ConditionForListAlertStrategiesOutput.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this ConditionForListAlertStrategiesOutput.


        :param operator: The operator of this ConditionForListAlertStrategiesOutput.  # noqa: E501
        :type: str
        """

        self._operator = operator

    @property
    def period(self):
        """Gets the period of this ConditionForListAlertStrategiesOutput.  # noqa: E501


        :return: The period of this ConditionForListAlertStrategiesOutput.  # noqa: E501
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this ConditionForListAlertStrategiesOutput.


        :param period: The period of this ConditionForListAlertStrategiesOutput.  # noqa: E501
        :type: int
        """

        self._period = period

    @property
    def sensitivity(self):
        """Gets the sensitivity of this ConditionForListAlertStrategiesOutput.  # noqa: E501


        :return: The sensitivity of this ConditionForListAlertStrategiesOutput.  # noqa: E501
        :rtype: str
        """
        return self._sensitivity

    @sensitivity.setter
    def sensitivity(self, sensitivity):
        """Sets the sensitivity of this ConditionForListAlertStrategiesOutput.


        :param sensitivity: The sensitivity of this ConditionForListAlertStrategiesOutput.  # noqa: E501
        :type: str
        """

        self._sensitivity = sensitivity

    @property
    def threshold_type(self):
        """Gets the threshold_type of this ConditionForListAlertStrategiesOutput.  # noqa: E501


        :return: The threshold_type of this ConditionForListAlertStrategiesOutput.  # noqa: E501
        :rtype: str
        """
        return self._threshold_type

    @threshold_type.setter
    def threshold_type(self, threshold_type):
        """Sets the threshold_type of this ConditionForListAlertStrategiesOutput.


        :param threshold_type: The threshold_type of this ConditionForListAlertStrategiesOutput.  # noqa: E501
        :type: str
        """

        self._threshold_type = threshold_type

    @property
    def value(self):
        """Gets the value of this ConditionForListAlertStrategiesOutput.  # noqa: E501


        :return: The value of this ConditionForListAlertStrategiesOutput.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ConditionForListAlertStrategiesOutput.


        :param value: The value of this ConditionForListAlertStrategiesOutput.  # noqa: E501
        :type: float
        """

        self._value = value

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
        if issubclass(ConditionForListAlertStrategiesOutput, dict):
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
        if not isinstance(other, ConditionForListAlertStrategiesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConditionForListAlertStrategiesOutput):
            return True

        return self.to_dict() != other.to_dict()
