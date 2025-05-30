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


class GetBaselineGroupStatisticsResponse(object):
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
        'checklist_num': 'int',
        'high_risk_num': 'int',
        'host_num': 'int',
        'last_check_time': 'int',
        'low_risk_num': 'int',
        'mid_risk_num': 'int',
        'pass_host_num': 'int',
        'pass_num': 'int',
        'pass_rate': 'int',
        'risk_host_num': 'int',
        'risk_num': 'int',
        'status': 'str'
    }

    attribute_map = {
        'checklist_num': 'ChecklistNum',
        'high_risk_num': 'HighRiskNum',
        'host_num': 'HostNum',
        'last_check_time': 'LastCheckTime',
        'low_risk_num': 'LowRiskNum',
        'mid_risk_num': 'MidRiskNum',
        'pass_host_num': 'PassHostNum',
        'pass_num': 'PassNum',
        'pass_rate': 'PassRate',
        'risk_host_num': 'RiskHostNum',
        'risk_num': 'RiskNum',
        'status': 'Status'
    }

    def __init__(self, checklist_num=None, high_risk_num=None, host_num=None, last_check_time=None, low_risk_num=None, mid_risk_num=None, pass_host_num=None, pass_num=None, pass_rate=None, risk_host_num=None, risk_num=None, status=None, _configuration=None):  # noqa: E501
        """GetBaselineGroupStatisticsResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._checklist_num = None
        self._high_risk_num = None
        self._host_num = None
        self._last_check_time = None
        self._low_risk_num = None
        self._mid_risk_num = None
        self._pass_host_num = None
        self._pass_num = None
        self._pass_rate = None
        self._risk_host_num = None
        self._risk_num = None
        self._status = None
        self.discriminator = None

        if checklist_num is not None:
            self.checklist_num = checklist_num
        if high_risk_num is not None:
            self.high_risk_num = high_risk_num
        if host_num is not None:
            self.host_num = host_num
        if last_check_time is not None:
            self.last_check_time = last_check_time
        if low_risk_num is not None:
            self.low_risk_num = low_risk_num
        if mid_risk_num is not None:
            self.mid_risk_num = mid_risk_num
        if pass_host_num is not None:
            self.pass_host_num = pass_host_num
        if pass_num is not None:
            self.pass_num = pass_num
        if pass_rate is not None:
            self.pass_rate = pass_rate
        if risk_host_num is not None:
            self.risk_host_num = risk_host_num
        if risk_num is not None:
            self.risk_num = risk_num
        if status is not None:
            self.status = status

    @property
    def checklist_num(self):
        """Gets the checklist_num of this GetBaselineGroupStatisticsResponse.  # noqa: E501


        :return: The checklist_num of this GetBaselineGroupStatisticsResponse.  # noqa: E501
        :rtype: int
        """
        return self._checklist_num

    @checklist_num.setter
    def checklist_num(self, checklist_num):
        """Sets the checklist_num of this GetBaselineGroupStatisticsResponse.


        :param checklist_num: The checklist_num of this GetBaselineGroupStatisticsResponse.  # noqa: E501
        :type: int
        """

        self._checklist_num = checklist_num

    @property
    def high_risk_num(self):
        """Gets the high_risk_num of this GetBaselineGroupStatisticsResponse.  # noqa: E501


        :return: The high_risk_num of this GetBaselineGroupStatisticsResponse.  # noqa: E501
        :rtype: int
        """
        return self._high_risk_num

    @high_risk_num.setter
    def high_risk_num(self, high_risk_num):
        """Sets the high_risk_num of this GetBaselineGroupStatisticsResponse.


        :param high_risk_num: The high_risk_num of this GetBaselineGroupStatisticsResponse.  # noqa: E501
        :type: int
        """

        self._high_risk_num = high_risk_num

    @property
    def host_num(self):
        """Gets the host_num of this GetBaselineGroupStatisticsResponse.  # noqa: E501


        :return: The host_num of this GetBaselineGroupStatisticsResponse.  # noqa: E501
        :rtype: int
        """
        return self._host_num

    @host_num.setter
    def host_num(self, host_num):
        """Sets the host_num of this GetBaselineGroupStatisticsResponse.


        :param host_num: The host_num of this GetBaselineGroupStatisticsResponse.  # noqa: E501
        :type: int
        """

        self._host_num = host_num

    @property
    def last_check_time(self):
        """Gets the last_check_time of this GetBaselineGroupStatisticsResponse.  # noqa: E501


        :return: The last_check_time of this GetBaselineGroupStatisticsResponse.  # noqa: E501
        :rtype: int
        """
        return self._last_check_time

    @last_check_time.setter
    def last_check_time(self, last_check_time):
        """Sets the last_check_time of this GetBaselineGroupStatisticsResponse.


        :param last_check_time: The last_check_time of this GetBaselineGroupStatisticsResponse.  # noqa: E501
        :type: int
        """

        self._last_check_time = last_check_time

    @property
    def low_risk_num(self):
        """Gets the low_risk_num of this GetBaselineGroupStatisticsResponse.  # noqa: E501


        :return: The low_risk_num of this GetBaselineGroupStatisticsResponse.  # noqa: E501
        :rtype: int
        """
        return self._low_risk_num

    @low_risk_num.setter
    def low_risk_num(self, low_risk_num):
        """Sets the low_risk_num of this GetBaselineGroupStatisticsResponse.


        :param low_risk_num: The low_risk_num of this GetBaselineGroupStatisticsResponse.  # noqa: E501
        :type: int
        """

        self._low_risk_num = low_risk_num

    @property
    def mid_risk_num(self):
        """Gets the mid_risk_num of this GetBaselineGroupStatisticsResponse.  # noqa: E501


        :return: The mid_risk_num of this GetBaselineGroupStatisticsResponse.  # noqa: E501
        :rtype: int
        """
        return self._mid_risk_num

    @mid_risk_num.setter
    def mid_risk_num(self, mid_risk_num):
        """Sets the mid_risk_num of this GetBaselineGroupStatisticsResponse.


        :param mid_risk_num: The mid_risk_num of this GetBaselineGroupStatisticsResponse.  # noqa: E501
        :type: int
        """

        self._mid_risk_num = mid_risk_num

    @property
    def pass_host_num(self):
        """Gets the pass_host_num of this GetBaselineGroupStatisticsResponse.  # noqa: E501


        :return: The pass_host_num of this GetBaselineGroupStatisticsResponse.  # noqa: E501
        :rtype: int
        """
        return self._pass_host_num

    @pass_host_num.setter
    def pass_host_num(self, pass_host_num):
        """Sets the pass_host_num of this GetBaselineGroupStatisticsResponse.


        :param pass_host_num: The pass_host_num of this GetBaselineGroupStatisticsResponse.  # noqa: E501
        :type: int
        """

        self._pass_host_num = pass_host_num

    @property
    def pass_num(self):
        """Gets the pass_num of this GetBaselineGroupStatisticsResponse.  # noqa: E501


        :return: The pass_num of this GetBaselineGroupStatisticsResponse.  # noqa: E501
        :rtype: int
        """
        return self._pass_num

    @pass_num.setter
    def pass_num(self, pass_num):
        """Sets the pass_num of this GetBaselineGroupStatisticsResponse.


        :param pass_num: The pass_num of this GetBaselineGroupStatisticsResponse.  # noqa: E501
        :type: int
        """

        self._pass_num = pass_num

    @property
    def pass_rate(self):
        """Gets the pass_rate of this GetBaselineGroupStatisticsResponse.  # noqa: E501


        :return: The pass_rate of this GetBaselineGroupStatisticsResponse.  # noqa: E501
        :rtype: int
        """
        return self._pass_rate

    @pass_rate.setter
    def pass_rate(self, pass_rate):
        """Sets the pass_rate of this GetBaselineGroupStatisticsResponse.


        :param pass_rate: The pass_rate of this GetBaselineGroupStatisticsResponse.  # noqa: E501
        :type: int
        """

        self._pass_rate = pass_rate

    @property
    def risk_host_num(self):
        """Gets the risk_host_num of this GetBaselineGroupStatisticsResponse.  # noqa: E501


        :return: The risk_host_num of this GetBaselineGroupStatisticsResponse.  # noqa: E501
        :rtype: int
        """
        return self._risk_host_num

    @risk_host_num.setter
    def risk_host_num(self, risk_host_num):
        """Sets the risk_host_num of this GetBaselineGroupStatisticsResponse.


        :param risk_host_num: The risk_host_num of this GetBaselineGroupStatisticsResponse.  # noqa: E501
        :type: int
        """

        self._risk_host_num = risk_host_num

    @property
    def risk_num(self):
        """Gets the risk_num of this GetBaselineGroupStatisticsResponse.  # noqa: E501


        :return: The risk_num of this GetBaselineGroupStatisticsResponse.  # noqa: E501
        :rtype: int
        """
        return self._risk_num

    @risk_num.setter
    def risk_num(self, risk_num):
        """Sets the risk_num of this GetBaselineGroupStatisticsResponse.


        :param risk_num: The risk_num of this GetBaselineGroupStatisticsResponse.  # noqa: E501
        :type: int
        """

        self._risk_num = risk_num

    @property
    def status(self):
        """Gets the status of this GetBaselineGroupStatisticsResponse.  # noqa: E501


        :return: The status of this GetBaselineGroupStatisticsResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GetBaselineGroupStatisticsResponse.


        :param status: The status of this GetBaselineGroupStatisticsResponse.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(GetBaselineGroupStatisticsResponse, dict):
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
        if not isinstance(other, GetBaselineGroupStatisticsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetBaselineGroupStatisticsResponse):
            return True

        return self.to_dict() != other.to_dict()
