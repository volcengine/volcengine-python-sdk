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


class PlusAlarmInfo49ForGetHidsAlarmInfoOutput(object):
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
        'pid_tree': 'str',
        'sip': 'str',
        'sport': 'str'
    }

    attribute_map = {
        'pid_tree': 'PidTree',
        'sip': 'Sip',
        'sport': 'Sport'
    }

    def __init__(self, pid_tree=None, sip=None, sport=None, _configuration=None):  # noqa: E501
        """PlusAlarmInfo49ForGetHidsAlarmInfoOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._pid_tree = None
        self._sip = None
        self._sport = None
        self.discriminator = None

        if pid_tree is not None:
            self.pid_tree = pid_tree
        if sip is not None:
            self.sip = sip
        if sport is not None:
            self.sport = sport

    @property
    def pid_tree(self):
        """Gets the pid_tree of this PlusAlarmInfo49ForGetHidsAlarmInfoOutput.  # noqa: E501


        :return: The pid_tree of this PlusAlarmInfo49ForGetHidsAlarmInfoOutput.  # noqa: E501
        :rtype: str
        """
        return self._pid_tree

    @pid_tree.setter
    def pid_tree(self, pid_tree):
        """Sets the pid_tree of this PlusAlarmInfo49ForGetHidsAlarmInfoOutput.


        :param pid_tree: The pid_tree of this PlusAlarmInfo49ForGetHidsAlarmInfoOutput.  # noqa: E501
        :type: str
        """

        self._pid_tree = pid_tree

    @property
    def sip(self):
        """Gets the sip of this PlusAlarmInfo49ForGetHidsAlarmInfoOutput.  # noqa: E501


        :return: The sip of this PlusAlarmInfo49ForGetHidsAlarmInfoOutput.  # noqa: E501
        :rtype: str
        """
        return self._sip

    @sip.setter
    def sip(self, sip):
        """Sets the sip of this PlusAlarmInfo49ForGetHidsAlarmInfoOutput.


        :param sip: The sip of this PlusAlarmInfo49ForGetHidsAlarmInfoOutput.  # noqa: E501
        :type: str
        """

        self._sip = sip

    @property
    def sport(self):
        """Gets the sport of this PlusAlarmInfo49ForGetHidsAlarmInfoOutput.  # noqa: E501


        :return: The sport of this PlusAlarmInfo49ForGetHidsAlarmInfoOutput.  # noqa: E501
        :rtype: str
        """
        return self._sport

    @sport.setter
    def sport(self, sport):
        """Sets the sport of this PlusAlarmInfo49ForGetHidsAlarmInfoOutput.


        :param sport: The sport of this PlusAlarmInfo49ForGetHidsAlarmInfoOutput.  # noqa: E501
        :type: str
        """

        self._sport = sport

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
        if issubclass(PlusAlarmInfo49ForGetHidsAlarmInfoOutput, dict):
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
        if not isinstance(other, PlusAlarmInfo49ForGetHidsAlarmInfoOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PlusAlarmInfo49ForGetHidsAlarmInfoOutput):
            return True

        return self.to_dict() != other.to_dict()
