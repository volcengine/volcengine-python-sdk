# coding: utf-8

"""
    dbw

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeSlowLogsResponse(object):
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
        'slow_logs': 'list[SlowLogForDescribeSlowLogsOutput]',
        'total': 'int'
    }

    attribute_map = {
        'slow_logs': 'SlowLogs',
        'total': 'Total'
    }

    def __init__(self, slow_logs=None, total=None, _configuration=None):  # noqa: E501
        """DescribeSlowLogsResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._slow_logs = None
        self._total = None
        self.discriminator = None

        if slow_logs is not None:
            self.slow_logs = slow_logs
        if total is not None:
            self.total = total

    @property
    def slow_logs(self):
        """Gets the slow_logs of this DescribeSlowLogsResponse.  # noqa: E501


        :return: The slow_logs of this DescribeSlowLogsResponse.  # noqa: E501
        :rtype: list[SlowLogForDescribeSlowLogsOutput]
        """
        return self._slow_logs

    @slow_logs.setter
    def slow_logs(self, slow_logs):
        """Sets the slow_logs of this DescribeSlowLogsResponse.


        :param slow_logs: The slow_logs of this DescribeSlowLogsResponse.  # noqa: E501
        :type: list[SlowLogForDescribeSlowLogsOutput]
        """

        self._slow_logs = slow_logs

    @property
    def total(self):
        """Gets the total of this DescribeSlowLogsResponse.  # noqa: E501


        :return: The total of this DescribeSlowLogsResponse.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this DescribeSlowLogsResponse.


        :param total: The total of this DescribeSlowLogsResponse.  # noqa: E501
        :type: int
        """

        self._total = total

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
        if issubclass(DescribeSlowLogsResponse, dict):
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
        if not isinstance(other, DescribeSlowLogsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeSlowLogsResponse):
            return True

        return self.to_dict() != other.to_dict()
