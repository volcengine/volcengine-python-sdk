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


class TopDataDetailForDescribeDistrictRankingOutput(object):
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
        'metric': 'str',
        'value_details': 'list[ValueDetailForDescribeDistrictRankingOutput]'
    }

    attribute_map = {
        'metric': 'Metric',
        'value_details': 'ValueDetails'
    }

    def __init__(self, metric=None, value_details=None, _configuration=None):  # noqa: E501
        """TopDataDetailForDescribeDistrictRankingOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._metric = None
        self._value_details = None
        self.discriminator = None

        if metric is not None:
            self.metric = metric
        if value_details is not None:
            self.value_details = value_details

    @property
    def metric(self):
        """Gets the metric of this TopDataDetailForDescribeDistrictRankingOutput.  # noqa: E501


        :return: The metric of this TopDataDetailForDescribeDistrictRankingOutput.  # noqa: E501
        :rtype: str
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this TopDataDetailForDescribeDistrictRankingOutput.


        :param metric: The metric of this TopDataDetailForDescribeDistrictRankingOutput.  # noqa: E501
        :type: str
        """

        self._metric = metric

    @property
    def value_details(self):
        """Gets the value_details of this TopDataDetailForDescribeDistrictRankingOutput.  # noqa: E501


        :return: The value_details of this TopDataDetailForDescribeDistrictRankingOutput.  # noqa: E501
        :rtype: list[ValueDetailForDescribeDistrictRankingOutput]
        """
        return self._value_details

    @value_details.setter
    def value_details(self, value_details):
        """Sets the value_details of this TopDataDetailForDescribeDistrictRankingOutput.


        :param value_details: The value_details of this TopDataDetailForDescribeDistrictRankingOutput.  # noqa: E501
        :type: list[ValueDetailForDescribeDistrictRankingOutput]
        """

        self._value_details = value_details

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
        if issubclass(TopDataDetailForDescribeDistrictRankingOutput, dict):
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
        if not isinstance(other, TopDataDetailForDescribeDistrictRankingOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TopDataDetailForDescribeDistrictRankingOutput):
            return True

        return self.to_dict() != other.to_dict()