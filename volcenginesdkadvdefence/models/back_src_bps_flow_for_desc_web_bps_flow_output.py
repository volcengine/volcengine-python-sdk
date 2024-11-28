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


class BackSrcBpsFlowForDescWebBpsFlowOutput(object):
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
        'avg_bps': 'float',
        'max_bps': 'float',
        'time_stamp': 'int'
    }

    attribute_map = {
        'avg_bps': 'AvgBps',
        'max_bps': 'MaxBps',
        'time_stamp': 'TimeStamp'
    }

    def __init__(self, avg_bps=None, max_bps=None, time_stamp=None, _configuration=None):  # noqa: E501
        """BackSrcBpsFlowForDescWebBpsFlowOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._avg_bps = None
        self._max_bps = None
        self._time_stamp = None
        self.discriminator = None

        if avg_bps is not None:
            self.avg_bps = avg_bps
        if max_bps is not None:
            self.max_bps = max_bps
        if time_stamp is not None:
            self.time_stamp = time_stamp

    @property
    def avg_bps(self):
        """Gets the avg_bps of this BackSrcBpsFlowForDescWebBpsFlowOutput.  # noqa: E501


        :return: The avg_bps of this BackSrcBpsFlowForDescWebBpsFlowOutput.  # noqa: E501
        :rtype: float
        """
        return self._avg_bps

    @avg_bps.setter
    def avg_bps(self, avg_bps):
        """Sets the avg_bps of this BackSrcBpsFlowForDescWebBpsFlowOutput.


        :param avg_bps: The avg_bps of this BackSrcBpsFlowForDescWebBpsFlowOutput.  # noqa: E501
        :type: float
        """

        self._avg_bps = avg_bps

    @property
    def max_bps(self):
        """Gets the max_bps of this BackSrcBpsFlowForDescWebBpsFlowOutput.  # noqa: E501


        :return: The max_bps of this BackSrcBpsFlowForDescWebBpsFlowOutput.  # noqa: E501
        :rtype: float
        """
        return self._max_bps

    @max_bps.setter
    def max_bps(self, max_bps):
        """Sets the max_bps of this BackSrcBpsFlowForDescWebBpsFlowOutput.


        :param max_bps: The max_bps of this BackSrcBpsFlowForDescWebBpsFlowOutput.  # noqa: E501
        :type: float
        """

        self._max_bps = max_bps

    @property
    def time_stamp(self):
        """Gets the time_stamp of this BackSrcBpsFlowForDescWebBpsFlowOutput.  # noqa: E501


        :return: The time_stamp of this BackSrcBpsFlowForDescWebBpsFlowOutput.  # noqa: E501
        :rtype: int
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp):
        """Sets the time_stamp of this BackSrcBpsFlowForDescWebBpsFlowOutput.


        :param time_stamp: The time_stamp of this BackSrcBpsFlowForDescWebBpsFlowOutput.  # noqa: E501
        :type: int
        """

        self._time_stamp = time_stamp

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
        if issubclass(BackSrcBpsFlowForDescWebBpsFlowOutput, dict):
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
        if not isinstance(other, BackSrcBpsFlowForDescWebBpsFlowOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BackSrcBpsFlowForDescWebBpsFlowOutput):
            return True

        return self.to_dict() != other.to_dict()