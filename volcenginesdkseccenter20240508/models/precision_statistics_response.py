# coding: utf-8

"""
    seccenter20240508

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class PrecisionStatisticsResponse(object):
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
        'distribution': 'list[DistributionForPrecisionStatisticsOutput]',
        'today_new_count': 'int',
        'total_count': 'int'
    }

    attribute_map = {
        'distribution': 'Distribution',
        'today_new_count': 'TodayNewCount',
        'total_count': 'TotalCount'
    }

    def __init__(self, distribution=None, today_new_count=None, total_count=None, _configuration=None):  # noqa: E501
        """PrecisionStatisticsResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._distribution = None
        self._today_new_count = None
        self._total_count = None
        self.discriminator = None

        if distribution is not None:
            self.distribution = distribution
        if today_new_count is not None:
            self.today_new_count = today_new_count
        if total_count is not None:
            self.total_count = total_count

    @property
    def distribution(self):
        """Gets the distribution of this PrecisionStatisticsResponse.  # noqa: E501


        :return: The distribution of this PrecisionStatisticsResponse.  # noqa: E501
        :rtype: list[DistributionForPrecisionStatisticsOutput]
        """
        return self._distribution

    @distribution.setter
    def distribution(self, distribution):
        """Sets the distribution of this PrecisionStatisticsResponse.


        :param distribution: The distribution of this PrecisionStatisticsResponse.  # noqa: E501
        :type: list[DistributionForPrecisionStatisticsOutput]
        """

        self._distribution = distribution

    @property
    def today_new_count(self):
        """Gets the today_new_count of this PrecisionStatisticsResponse.  # noqa: E501


        :return: The today_new_count of this PrecisionStatisticsResponse.  # noqa: E501
        :rtype: int
        """
        return self._today_new_count

    @today_new_count.setter
    def today_new_count(self, today_new_count):
        """Sets the today_new_count of this PrecisionStatisticsResponse.


        :param today_new_count: The today_new_count of this PrecisionStatisticsResponse.  # noqa: E501
        :type: int
        """

        self._today_new_count = today_new_count

    @property
    def total_count(self):
        """Gets the total_count of this PrecisionStatisticsResponse.  # noqa: E501


        :return: The total_count of this PrecisionStatisticsResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this PrecisionStatisticsResponse.


        :param total_count: The total_count of this PrecisionStatisticsResponse.  # noqa: E501
        :type: int
        """

        self._total_count = total_count

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
        if issubclass(PrecisionStatisticsResponse, dict):
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
        if not isinstance(other, PrecisionStatisticsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PrecisionStatisticsResponse):
            return True

        return self.to_dict() != other.to_dict()
