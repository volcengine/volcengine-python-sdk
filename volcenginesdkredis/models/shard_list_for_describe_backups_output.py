# coding: utf-8

"""
    redis

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ShardListForDescribeBackupsOutput(object):
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
        'shard_index': 'int',
        'slot_map': 'list[str]',
        'slots_number': 'int'
    }

    attribute_map = {
        'shard_index': 'ShardIndex',
        'slot_map': 'SlotMap',
        'slots_number': 'SlotsNumber'
    }

    def __init__(self, shard_index=None, slot_map=None, slots_number=None, _configuration=None):  # noqa: E501
        """ShardListForDescribeBackupsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._shard_index = None
        self._slot_map = None
        self._slots_number = None
        self.discriminator = None

        if shard_index is not None:
            self.shard_index = shard_index
        if slot_map is not None:
            self.slot_map = slot_map
        if slots_number is not None:
            self.slots_number = slots_number

    @property
    def shard_index(self):
        """Gets the shard_index of this ShardListForDescribeBackupsOutput.  # noqa: E501


        :return: The shard_index of this ShardListForDescribeBackupsOutput.  # noqa: E501
        :rtype: int
        """
        return self._shard_index

    @shard_index.setter
    def shard_index(self, shard_index):
        """Sets the shard_index of this ShardListForDescribeBackupsOutput.


        :param shard_index: The shard_index of this ShardListForDescribeBackupsOutput.  # noqa: E501
        :type: int
        """

        self._shard_index = shard_index

    @property
    def slot_map(self):
        """Gets the slot_map of this ShardListForDescribeBackupsOutput.  # noqa: E501


        :return: The slot_map of this ShardListForDescribeBackupsOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._slot_map

    @slot_map.setter
    def slot_map(self, slot_map):
        """Sets the slot_map of this ShardListForDescribeBackupsOutput.


        :param slot_map: The slot_map of this ShardListForDescribeBackupsOutput.  # noqa: E501
        :type: list[str]
        """

        self._slot_map = slot_map

    @property
    def slots_number(self):
        """Gets the slots_number of this ShardListForDescribeBackupsOutput.  # noqa: E501


        :return: The slots_number of this ShardListForDescribeBackupsOutput.  # noqa: E501
        :rtype: int
        """
        return self._slots_number

    @slots_number.setter
    def slots_number(self, slots_number):
        """Sets the slots_number of this ShardListForDescribeBackupsOutput.


        :param slots_number: The slots_number of this ShardListForDescribeBackupsOutput.  # noqa: E501
        :type: int
        """

        self._slots_number = slots_number

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
        if issubclass(ShardListForDescribeBackupsOutput, dict):
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
        if not isinstance(other, ShardListForDescribeBackupsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ShardListForDescribeBackupsOutput):
            return True

        return self.to_dict() != other.to_dict()
