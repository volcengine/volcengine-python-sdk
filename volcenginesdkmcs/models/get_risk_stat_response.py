# coding: utf-8

"""
    mcs

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class GetRiskStatResponse(object):
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
        'not_fixed': 'NotFixedForGetRiskStatOutput',
        'stat_by_status': 'StatByStatusForGetRiskStatOutput',
        'trend': 'TrendForGetRiskStatOutput'
    }

    attribute_map = {
        'not_fixed': 'NotFixed',
        'stat_by_status': 'StatByStatus',
        'trend': 'Trend'
    }

    def __init__(self, not_fixed=None, stat_by_status=None, trend=None, _configuration=None):  # noqa: E501
        """GetRiskStatResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._not_fixed = None
        self._stat_by_status = None
        self._trend = None
        self.discriminator = None

        if not_fixed is not None:
            self.not_fixed = not_fixed
        if stat_by_status is not None:
            self.stat_by_status = stat_by_status
        if trend is not None:
            self.trend = trend

    @property
    def not_fixed(self):
        """Gets the not_fixed of this GetRiskStatResponse.  # noqa: E501


        :return: The not_fixed of this GetRiskStatResponse.  # noqa: E501
        :rtype: NotFixedForGetRiskStatOutput
        """
        return self._not_fixed

    @not_fixed.setter
    def not_fixed(self, not_fixed):
        """Sets the not_fixed of this GetRiskStatResponse.


        :param not_fixed: The not_fixed of this GetRiskStatResponse.  # noqa: E501
        :type: NotFixedForGetRiskStatOutput
        """

        self._not_fixed = not_fixed

    @property
    def stat_by_status(self):
        """Gets the stat_by_status of this GetRiskStatResponse.  # noqa: E501


        :return: The stat_by_status of this GetRiskStatResponse.  # noqa: E501
        :rtype: StatByStatusForGetRiskStatOutput
        """
        return self._stat_by_status

    @stat_by_status.setter
    def stat_by_status(self, stat_by_status):
        """Sets the stat_by_status of this GetRiskStatResponse.


        :param stat_by_status: The stat_by_status of this GetRiskStatResponse.  # noqa: E501
        :type: StatByStatusForGetRiskStatOutput
        """

        self._stat_by_status = stat_by_status

    @property
    def trend(self):
        """Gets the trend of this GetRiskStatResponse.  # noqa: E501


        :return: The trend of this GetRiskStatResponse.  # noqa: E501
        :rtype: TrendForGetRiskStatOutput
        """
        return self._trend

    @trend.setter
    def trend(self, trend):
        """Sets the trend of this GetRiskStatResponse.


        :param trend: The trend of this GetRiskStatResponse.  # noqa: E501
        :type: TrendForGetRiskStatOutput
        """

        self._trend = trend

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
        if issubclass(GetRiskStatResponse, dict):
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
        if not isinstance(other, GetRiskStatResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetRiskStatResponse):
            return True

        return self.to_dict() != other.to_dict()
