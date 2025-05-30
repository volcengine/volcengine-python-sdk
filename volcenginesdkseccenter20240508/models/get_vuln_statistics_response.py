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


class GetVulnStatisticsResponse(object):
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
        'auto_update_time': 'int',
        'danger': 'int',
        'high': 'int',
        'if_auto_update': 'bool',
        'if_large_agent': 'bool',
        'ignore': 'int',
        'increase': 'int',
        'low': 'int',
        'mid': 'int',
        'processed': 'int',
        'unknown': 'int',
        'unprocessed': 'int',
        'vuln_lib_version': 'int',
        'vuln_type': 'VulnTypeForGetVulnStatisticsOutput'
    }

    attribute_map = {
        'auto_update_time': 'AutoUpdateTime',
        'danger': 'Danger',
        'high': 'High',
        'if_auto_update': 'IfAutoUpdate',
        'if_large_agent': 'IfLargeAgent',
        'ignore': 'Ignore',
        'increase': 'Increase',
        'low': 'Low',
        'mid': 'Mid',
        'processed': 'Processed',
        'unknown': 'Unknown',
        'unprocessed': 'Unprocessed',
        'vuln_lib_version': 'VulnLibVersion',
        'vuln_type': 'VulnType'
    }

    def __init__(self, auto_update_time=None, danger=None, high=None, if_auto_update=None, if_large_agent=None, ignore=None, increase=None, low=None, mid=None, processed=None, unknown=None, unprocessed=None, vuln_lib_version=None, vuln_type=None, _configuration=None):  # noqa: E501
        """GetVulnStatisticsResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._auto_update_time = None
        self._danger = None
        self._high = None
        self._if_auto_update = None
        self._if_large_agent = None
        self._ignore = None
        self._increase = None
        self._low = None
        self._mid = None
        self._processed = None
        self._unknown = None
        self._unprocessed = None
        self._vuln_lib_version = None
        self._vuln_type = None
        self.discriminator = None

        if auto_update_time is not None:
            self.auto_update_time = auto_update_time
        if danger is not None:
            self.danger = danger
        if high is not None:
            self.high = high
        if if_auto_update is not None:
            self.if_auto_update = if_auto_update
        if if_large_agent is not None:
            self.if_large_agent = if_large_agent
        if ignore is not None:
            self.ignore = ignore
        if increase is not None:
            self.increase = increase
        if low is not None:
            self.low = low
        if mid is not None:
            self.mid = mid
        if processed is not None:
            self.processed = processed
        if unknown is not None:
            self.unknown = unknown
        if unprocessed is not None:
            self.unprocessed = unprocessed
        if vuln_lib_version is not None:
            self.vuln_lib_version = vuln_lib_version
        if vuln_type is not None:
            self.vuln_type = vuln_type

    @property
    def auto_update_time(self):
        """Gets the auto_update_time of this GetVulnStatisticsResponse.  # noqa: E501


        :return: The auto_update_time of this GetVulnStatisticsResponse.  # noqa: E501
        :rtype: int
        """
        return self._auto_update_time

    @auto_update_time.setter
    def auto_update_time(self, auto_update_time):
        """Sets the auto_update_time of this GetVulnStatisticsResponse.


        :param auto_update_time: The auto_update_time of this GetVulnStatisticsResponse.  # noqa: E501
        :type: int
        """

        self._auto_update_time = auto_update_time

    @property
    def danger(self):
        """Gets the danger of this GetVulnStatisticsResponse.  # noqa: E501


        :return: The danger of this GetVulnStatisticsResponse.  # noqa: E501
        :rtype: int
        """
        return self._danger

    @danger.setter
    def danger(self, danger):
        """Sets the danger of this GetVulnStatisticsResponse.


        :param danger: The danger of this GetVulnStatisticsResponse.  # noqa: E501
        :type: int
        """

        self._danger = danger

    @property
    def high(self):
        """Gets the high of this GetVulnStatisticsResponse.  # noqa: E501


        :return: The high of this GetVulnStatisticsResponse.  # noqa: E501
        :rtype: int
        """
        return self._high

    @high.setter
    def high(self, high):
        """Sets the high of this GetVulnStatisticsResponse.


        :param high: The high of this GetVulnStatisticsResponse.  # noqa: E501
        :type: int
        """

        self._high = high

    @property
    def if_auto_update(self):
        """Gets the if_auto_update of this GetVulnStatisticsResponse.  # noqa: E501


        :return: The if_auto_update of this GetVulnStatisticsResponse.  # noqa: E501
        :rtype: bool
        """
        return self._if_auto_update

    @if_auto_update.setter
    def if_auto_update(self, if_auto_update):
        """Sets the if_auto_update of this GetVulnStatisticsResponse.


        :param if_auto_update: The if_auto_update of this GetVulnStatisticsResponse.  # noqa: E501
        :type: bool
        """

        self._if_auto_update = if_auto_update

    @property
    def if_large_agent(self):
        """Gets the if_large_agent of this GetVulnStatisticsResponse.  # noqa: E501


        :return: The if_large_agent of this GetVulnStatisticsResponse.  # noqa: E501
        :rtype: bool
        """
        return self._if_large_agent

    @if_large_agent.setter
    def if_large_agent(self, if_large_agent):
        """Sets the if_large_agent of this GetVulnStatisticsResponse.


        :param if_large_agent: The if_large_agent of this GetVulnStatisticsResponse.  # noqa: E501
        :type: bool
        """

        self._if_large_agent = if_large_agent

    @property
    def ignore(self):
        """Gets the ignore of this GetVulnStatisticsResponse.  # noqa: E501


        :return: The ignore of this GetVulnStatisticsResponse.  # noqa: E501
        :rtype: int
        """
        return self._ignore

    @ignore.setter
    def ignore(self, ignore):
        """Sets the ignore of this GetVulnStatisticsResponse.


        :param ignore: The ignore of this GetVulnStatisticsResponse.  # noqa: E501
        :type: int
        """

        self._ignore = ignore

    @property
    def increase(self):
        """Gets the increase of this GetVulnStatisticsResponse.  # noqa: E501


        :return: The increase of this GetVulnStatisticsResponse.  # noqa: E501
        :rtype: int
        """
        return self._increase

    @increase.setter
    def increase(self, increase):
        """Sets the increase of this GetVulnStatisticsResponse.


        :param increase: The increase of this GetVulnStatisticsResponse.  # noqa: E501
        :type: int
        """

        self._increase = increase

    @property
    def low(self):
        """Gets the low of this GetVulnStatisticsResponse.  # noqa: E501


        :return: The low of this GetVulnStatisticsResponse.  # noqa: E501
        :rtype: int
        """
        return self._low

    @low.setter
    def low(self, low):
        """Sets the low of this GetVulnStatisticsResponse.


        :param low: The low of this GetVulnStatisticsResponse.  # noqa: E501
        :type: int
        """

        self._low = low

    @property
    def mid(self):
        """Gets the mid of this GetVulnStatisticsResponse.  # noqa: E501


        :return: The mid of this GetVulnStatisticsResponse.  # noqa: E501
        :rtype: int
        """
        return self._mid

    @mid.setter
    def mid(self, mid):
        """Sets the mid of this GetVulnStatisticsResponse.


        :param mid: The mid of this GetVulnStatisticsResponse.  # noqa: E501
        :type: int
        """

        self._mid = mid

    @property
    def processed(self):
        """Gets the processed of this GetVulnStatisticsResponse.  # noqa: E501


        :return: The processed of this GetVulnStatisticsResponse.  # noqa: E501
        :rtype: int
        """
        return self._processed

    @processed.setter
    def processed(self, processed):
        """Sets the processed of this GetVulnStatisticsResponse.


        :param processed: The processed of this GetVulnStatisticsResponse.  # noqa: E501
        :type: int
        """

        self._processed = processed

    @property
    def unknown(self):
        """Gets the unknown of this GetVulnStatisticsResponse.  # noqa: E501


        :return: The unknown of this GetVulnStatisticsResponse.  # noqa: E501
        :rtype: int
        """
        return self._unknown

    @unknown.setter
    def unknown(self, unknown):
        """Sets the unknown of this GetVulnStatisticsResponse.


        :param unknown: The unknown of this GetVulnStatisticsResponse.  # noqa: E501
        :type: int
        """

        self._unknown = unknown

    @property
    def unprocessed(self):
        """Gets the unprocessed of this GetVulnStatisticsResponse.  # noqa: E501


        :return: The unprocessed of this GetVulnStatisticsResponse.  # noqa: E501
        :rtype: int
        """
        return self._unprocessed

    @unprocessed.setter
    def unprocessed(self, unprocessed):
        """Sets the unprocessed of this GetVulnStatisticsResponse.


        :param unprocessed: The unprocessed of this GetVulnStatisticsResponse.  # noqa: E501
        :type: int
        """

        self._unprocessed = unprocessed

    @property
    def vuln_lib_version(self):
        """Gets the vuln_lib_version of this GetVulnStatisticsResponse.  # noqa: E501


        :return: The vuln_lib_version of this GetVulnStatisticsResponse.  # noqa: E501
        :rtype: int
        """
        return self._vuln_lib_version

    @vuln_lib_version.setter
    def vuln_lib_version(self, vuln_lib_version):
        """Sets the vuln_lib_version of this GetVulnStatisticsResponse.


        :param vuln_lib_version: The vuln_lib_version of this GetVulnStatisticsResponse.  # noqa: E501
        :type: int
        """

        self._vuln_lib_version = vuln_lib_version

    @property
    def vuln_type(self):
        """Gets the vuln_type of this GetVulnStatisticsResponse.  # noqa: E501


        :return: The vuln_type of this GetVulnStatisticsResponse.  # noqa: E501
        :rtype: VulnTypeForGetVulnStatisticsOutput
        """
        return self._vuln_type

    @vuln_type.setter
    def vuln_type(self, vuln_type):
        """Sets the vuln_type of this GetVulnStatisticsResponse.


        :param vuln_type: The vuln_type of this GetVulnStatisticsResponse.  # noqa: E501
        :type: VulnTypeForGetVulnStatisticsOutput
        """

        self._vuln_type = vuln_type

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
        if issubclass(GetVulnStatisticsResponse, dict):
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
        if not isinstance(other, GetVulnStatisticsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetVulnStatisticsResponse):
            return True

        return self.to_dict() != other.to_dict()
