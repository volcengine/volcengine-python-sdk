# coding: utf-8

"""
    rds_mysql_v2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ProxyResourceInfoForDescribeDBInstanceDetailOutput(object):
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
        'current_proxy_cpu_num': 'int',
        'max_proxy_cpu_num': 'int',
        'min_proxy_cpu_num': 'int'
    }

    attribute_map = {
        'current_proxy_cpu_num': 'CurrentProxyCpuNum',
        'max_proxy_cpu_num': 'MaxProxyCpuNum',
        'min_proxy_cpu_num': 'MinProxyCpuNum'
    }

    def __init__(self, current_proxy_cpu_num=None, max_proxy_cpu_num=None, min_proxy_cpu_num=None, _configuration=None):  # noqa: E501
        """ProxyResourceInfoForDescribeDBInstanceDetailOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._current_proxy_cpu_num = None
        self._max_proxy_cpu_num = None
        self._min_proxy_cpu_num = None
        self.discriminator = None

        if current_proxy_cpu_num is not None:
            self.current_proxy_cpu_num = current_proxy_cpu_num
        if max_proxy_cpu_num is not None:
            self.max_proxy_cpu_num = max_proxy_cpu_num
        if min_proxy_cpu_num is not None:
            self.min_proxy_cpu_num = min_proxy_cpu_num

    @property
    def current_proxy_cpu_num(self):
        """Gets the current_proxy_cpu_num of this ProxyResourceInfoForDescribeDBInstanceDetailOutput.  # noqa: E501


        :return: The current_proxy_cpu_num of this ProxyResourceInfoForDescribeDBInstanceDetailOutput.  # noqa: E501
        :rtype: int
        """
        return self._current_proxy_cpu_num

    @current_proxy_cpu_num.setter
    def current_proxy_cpu_num(self, current_proxy_cpu_num):
        """Sets the current_proxy_cpu_num of this ProxyResourceInfoForDescribeDBInstanceDetailOutput.


        :param current_proxy_cpu_num: The current_proxy_cpu_num of this ProxyResourceInfoForDescribeDBInstanceDetailOutput.  # noqa: E501
        :type: int
        """

        self._current_proxy_cpu_num = current_proxy_cpu_num

    @property
    def max_proxy_cpu_num(self):
        """Gets the max_proxy_cpu_num of this ProxyResourceInfoForDescribeDBInstanceDetailOutput.  # noqa: E501


        :return: The max_proxy_cpu_num of this ProxyResourceInfoForDescribeDBInstanceDetailOutput.  # noqa: E501
        :rtype: int
        """
        return self._max_proxy_cpu_num

    @max_proxy_cpu_num.setter
    def max_proxy_cpu_num(self, max_proxy_cpu_num):
        """Sets the max_proxy_cpu_num of this ProxyResourceInfoForDescribeDBInstanceDetailOutput.


        :param max_proxy_cpu_num: The max_proxy_cpu_num of this ProxyResourceInfoForDescribeDBInstanceDetailOutput.  # noqa: E501
        :type: int
        """

        self._max_proxy_cpu_num = max_proxy_cpu_num

    @property
    def min_proxy_cpu_num(self):
        """Gets the min_proxy_cpu_num of this ProxyResourceInfoForDescribeDBInstanceDetailOutput.  # noqa: E501


        :return: The min_proxy_cpu_num of this ProxyResourceInfoForDescribeDBInstanceDetailOutput.  # noqa: E501
        :rtype: int
        """
        return self._min_proxy_cpu_num

    @min_proxy_cpu_num.setter
    def min_proxy_cpu_num(self, min_proxy_cpu_num):
        """Sets the min_proxy_cpu_num of this ProxyResourceInfoForDescribeDBInstanceDetailOutput.


        :param min_proxy_cpu_num: The min_proxy_cpu_num of this ProxyResourceInfoForDescribeDBInstanceDetailOutput.  # noqa: E501
        :type: int
        """

        self._min_proxy_cpu_num = min_proxy_cpu_num

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
        if issubclass(ProxyResourceInfoForDescribeDBInstanceDetailOutput, dict):
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
        if not isinstance(other, ProxyResourceInfoForDescribeDBInstanceDetailOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProxyResourceInfoForDescribeDBInstanceDetailOutput):
            return True

        return self.to_dict() != other.to_dict()
