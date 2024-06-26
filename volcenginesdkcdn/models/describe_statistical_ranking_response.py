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


class DescribeStatisticalRankingResponse(object):
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
        'item': 'str',
        'metric': 'str',
        'ranking_data_list': 'list[RankingDataListForDescribeStatisticalRankingOutput]',
        'ua_type': 'str'
    }

    attribute_map = {
        'item': 'Item',
        'metric': 'Metric',
        'ranking_data_list': 'RankingDataList',
        'ua_type': 'UaType'
    }

    def __init__(self, item=None, metric=None, ranking_data_list=None, ua_type=None, _configuration=None):  # noqa: E501
        """DescribeStatisticalRankingResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._item = None
        self._metric = None
        self._ranking_data_list = None
        self._ua_type = None
        self.discriminator = None

        if item is not None:
            self.item = item
        if metric is not None:
            self.metric = metric
        if ranking_data_list is not None:
            self.ranking_data_list = ranking_data_list
        if ua_type is not None:
            self.ua_type = ua_type

    @property
    def item(self):
        """Gets the item of this DescribeStatisticalRankingResponse.  # noqa: E501


        :return: The item of this DescribeStatisticalRankingResponse.  # noqa: E501
        :rtype: str
        """
        return self._item

    @item.setter
    def item(self, item):
        """Sets the item of this DescribeStatisticalRankingResponse.


        :param item: The item of this DescribeStatisticalRankingResponse.  # noqa: E501
        :type: str
        """

        self._item = item

    @property
    def metric(self):
        """Gets the metric of this DescribeStatisticalRankingResponse.  # noqa: E501


        :return: The metric of this DescribeStatisticalRankingResponse.  # noqa: E501
        :rtype: str
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this DescribeStatisticalRankingResponse.


        :param metric: The metric of this DescribeStatisticalRankingResponse.  # noqa: E501
        :type: str
        """

        self._metric = metric

    @property
    def ranking_data_list(self):
        """Gets the ranking_data_list of this DescribeStatisticalRankingResponse.  # noqa: E501


        :return: The ranking_data_list of this DescribeStatisticalRankingResponse.  # noqa: E501
        :rtype: list[RankingDataListForDescribeStatisticalRankingOutput]
        """
        return self._ranking_data_list

    @ranking_data_list.setter
    def ranking_data_list(self, ranking_data_list):
        """Sets the ranking_data_list of this DescribeStatisticalRankingResponse.


        :param ranking_data_list: The ranking_data_list of this DescribeStatisticalRankingResponse.  # noqa: E501
        :type: list[RankingDataListForDescribeStatisticalRankingOutput]
        """

        self._ranking_data_list = ranking_data_list

    @property
    def ua_type(self):
        """Gets the ua_type of this DescribeStatisticalRankingResponse.  # noqa: E501


        :return: The ua_type of this DescribeStatisticalRankingResponse.  # noqa: E501
        :rtype: str
        """
        return self._ua_type

    @ua_type.setter
    def ua_type(self, ua_type):
        """Sets the ua_type of this DescribeStatisticalRankingResponse.


        :param ua_type: The ua_type of this DescribeStatisticalRankingResponse.  # noqa: E501
        :type: str
        """

        self._ua_type = ua_type

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
        if issubclass(DescribeStatisticalRankingResponse, dict):
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
        if not isinstance(other, DescribeStatisticalRankingResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeStatisticalRankingResponse):
            return True

        return self.to_dict() != other.to_dict()
