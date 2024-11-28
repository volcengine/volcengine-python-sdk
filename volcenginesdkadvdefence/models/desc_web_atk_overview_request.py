# coding: utf-8

"""
    advdefence

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescWebAtkOverviewRequest(object):
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
        'begin_time': 'int',
        'end_time': 'int',
        'hosts': 'list[str]'
    }

    attribute_map = {
        'begin_time': 'BeginTime',
        'end_time': 'EndTime',
        'hosts': 'Hosts'
    }

    def __init__(self, begin_time=None, end_time=None, hosts=None, _configuration=None):  # noqa: E501
        """DescWebAtkOverviewRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._begin_time = None
        self._end_time = None
        self._hosts = None
        self.discriminator = None

        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if hosts is not None:
            self.hosts = hosts

    @property
    def begin_time(self):
        """Gets the begin_time of this DescWebAtkOverviewRequest.  # noqa: E501


        :return: The begin_time of this DescWebAtkOverviewRequest.  # noqa: E501
        :rtype: int
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this DescWebAtkOverviewRequest.


        :param begin_time: The begin_time of this DescWebAtkOverviewRequest.  # noqa: E501
        :type: int
        """

        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this DescWebAtkOverviewRequest.  # noqa: E501


        :return: The end_time of this DescWebAtkOverviewRequest.  # noqa: E501
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this DescWebAtkOverviewRequest.


        :param end_time: The end_time of this DescWebAtkOverviewRequest.  # noqa: E501
        :type: int
        """

        self._end_time = end_time

    @property
    def hosts(self):
        """Gets the hosts of this DescWebAtkOverviewRequest.  # noqa: E501


        :return: The hosts of this DescWebAtkOverviewRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this DescWebAtkOverviewRequest.


        :param hosts: The hosts of this DescWebAtkOverviewRequest.  # noqa: E501
        :type: list[str]
        """

        self._hosts = hosts

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
        if issubclass(DescWebAtkOverviewRequest, dict):
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
        if not isinstance(other, DescWebAtkOverviewRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescWebAtkOverviewRequest):
            return True

        return self.to_dict() != other.to_dict()
