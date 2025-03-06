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


class UsageStatForDescribeBackupStatsOutput(object):
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
        'quantity': 'int',
        'stat_item': 'str',
        'stat_time': 'str'
    }

    attribute_map = {
        'quantity': 'Quantity',
        'stat_item': 'StatItem',
        'stat_time': 'StatTime'
    }

    def __init__(self, quantity=None, stat_item=None, stat_time=None, _configuration=None):  # noqa: E501
        """UsageStatForDescribeBackupStatsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._quantity = None
        self._stat_item = None
        self._stat_time = None
        self.discriminator = None

        if quantity is not None:
            self.quantity = quantity
        if stat_item is not None:
            self.stat_item = stat_item
        if stat_time is not None:
            self.stat_time = stat_time

    @property
    def quantity(self):
        """Gets the quantity of this UsageStatForDescribeBackupStatsOutput.  # noqa: E501


        :return: The quantity of this UsageStatForDescribeBackupStatsOutput.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this UsageStatForDescribeBackupStatsOutput.


        :param quantity: The quantity of this UsageStatForDescribeBackupStatsOutput.  # noqa: E501
        :type: int
        """

        self._quantity = quantity

    @property
    def stat_item(self):
        """Gets the stat_item of this UsageStatForDescribeBackupStatsOutput.  # noqa: E501


        :return: The stat_item of this UsageStatForDescribeBackupStatsOutput.  # noqa: E501
        :rtype: str
        """
        return self._stat_item

    @stat_item.setter
    def stat_item(self, stat_item):
        """Sets the stat_item of this UsageStatForDescribeBackupStatsOutput.


        :param stat_item: The stat_item of this UsageStatForDescribeBackupStatsOutput.  # noqa: E501
        :type: str
        """

        self._stat_item = stat_item

    @property
    def stat_time(self):
        """Gets the stat_time of this UsageStatForDescribeBackupStatsOutput.  # noqa: E501


        :return: The stat_time of this UsageStatForDescribeBackupStatsOutput.  # noqa: E501
        :rtype: str
        """
        return self._stat_time

    @stat_time.setter
    def stat_time(self, stat_time):
        """Sets the stat_time of this UsageStatForDescribeBackupStatsOutput.


        :param stat_time: The stat_time of this UsageStatForDescribeBackupStatsOutput.  # noqa: E501
        :type: str
        """

        self._stat_time = stat_time

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
        if issubclass(UsageStatForDescribeBackupStatsOutput, dict):
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
        if not isinstance(other, UsageStatForDescribeBackupStatsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UsageStatForDescribeBackupStatsOutput):
            return True

        return self.to_dict() != other.to_dict()
