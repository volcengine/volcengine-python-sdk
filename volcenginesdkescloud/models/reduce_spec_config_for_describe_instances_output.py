# coding: utf-8

"""
    escloud

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ReduceSpecConfigForDescribeInstancesOutput(object):
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
        'cold_node_num': 'int',
        'data_node_num': 'int',
        'enable_pure_master': 'bool',
        'master_node_num': 'int',
        'warm_node_num': 'int'
    }

    attribute_map = {
        'cold_node_num': 'ColdNodeNum',
        'data_node_num': 'DataNodeNum',
        'enable_pure_master': 'EnablePureMaster',
        'master_node_num': 'MasterNodeNum',
        'warm_node_num': 'WarmNodeNum'
    }

    def __init__(self, cold_node_num=None, data_node_num=None, enable_pure_master=None, master_node_num=None, warm_node_num=None, _configuration=None):  # noqa: E501
        """ReduceSpecConfigForDescribeInstancesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cold_node_num = None
        self._data_node_num = None
        self._enable_pure_master = None
        self._master_node_num = None
        self._warm_node_num = None
        self.discriminator = None

        if cold_node_num is not None:
            self.cold_node_num = cold_node_num
        if data_node_num is not None:
            self.data_node_num = data_node_num
        if enable_pure_master is not None:
            self.enable_pure_master = enable_pure_master
        if master_node_num is not None:
            self.master_node_num = master_node_num
        if warm_node_num is not None:
            self.warm_node_num = warm_node_num

    @property
    def cold_node_num(self):
        """Gets the cold_node_num of this ReduceSpecConfigForDescribeInstancesOutput.  # noqa: E501


        :return: The cold_node_num of this ReduceSpecConfigForDescribeInstancesOutput.  # noqa: E501
        :rtype: int
        """
        return self._cold_node_num

    @cold_node_num.setter
    def cold_node_num(self, cold_node_num):
        """Sets the cold_node_num of this ReduceSpecConfigForDescribeInstancesOutput.


        :param cold_node_num: The cold_node_num of this ReduceSpecConfigForDescribeInstancesOutput.  # noqa: E501
        :type: int
        """

        self._cold_node_num = cold_node_num

    @property
    def data_node_num(self):
        """Gets the data_node_num of this ReduceSpecConfigForDescribeInstancesOutput.  # noqa: E501


        :return: The data_node_num of this ReduceSpecConfigForDescribeInstancesOutput.  # noqa: E501
        :rtype: int
        """
        return self._data_node_num

    @data_node_num.setter
    def data_node_num(self, data_node_num):
        """Sets the data_node_num of this ReduceSpecConfigForDescribeInstancesOutput.


        :param data_node_num: The data_node_num of this ReduceSpecConfigForDescribeInstancesOutput.  # noqa: E501
        :type: int
        """

        self._data_node_num = data_node_num

    @property
    def enable_pure_master(self):
        """Gets the enable_pure_master of this ReduceSpecConfigForDescribeInstancesOutput.  # noqa: E501


        :return: The enable_pure_master of this ReduceSpecConfigForDescribeInstancesOutput.  # noqa: E501
        :rtype: bool
        """
        return self._enable_pure_master

    @enable_pure_master.setter
    def enable_pure_master(self, enable_pure_master):
        """Sets the enable_pure_master of this ReduceSpecConfigForDescribeInstancesOutput.


        :param enable_pure_master: The enable_pure_master of this ReduceSpecConfigForDescribeInstancesOutput.  # noqa: E501
        :type: bool
        """

        self._enable_pure_master = enable_pure_master

    @property
    def master_node_num(self):
        """Gets the master_node_num of this ReduceSpecConfigForDescribeInstancesOutput.  # noqa: E501


        :return: The master_node_num of this ReduceSpecConfigForDescribeInstancesOutput.  # noqa: E501
        :rtype: int
        """
        return self._master_node_num

    @master_node_num.setter
    def master_node_num(self, master_node_num):
        """Sets the master_node_num of this ReduceSpecConfigForDescribeInstancesOutput.


        :param master_node_num: The master_node_num of this ReduceSpecConfigForDescribeInstancesOutput.  # noqa: E501
        :type: int
        """

        self._master_node_num = master_node_num

    @property
    def warm_node_num(self):
        """Gets the warm_node_num of this ReduceSpecConfigForDescribeInstancesOutput.  # noqa: E501


        :return: The warm_node_num of this ReduceSpecConfigForDescribeInstancesOutput.  # noqa: E501
        :rtype: int
        """
        return self._warm_node_num

    @warm_node_num.setter
    def warm_node_num(self, warm_node_num):
        """Sets the warm_node_num of this ReduceSpecConfigForDescribeInstancesOutput.


        :param warm_node_num: The warm_node_num of this ReduceSpecConfigForDescribeInstancesOutput.  # noqa: E501
        :type: int
        """

        self._warm_node_num = warm_node_num

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
        if issubclass(ReduceSpecConfigForDescribeInstancesOutput, dict):
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
        if not isinstance(other, ReduceSpecConfigForDescribeInstancesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReduceSpecConfigForDescribeInstancesOutput):
            return True

        return self.to_dict() != other.to_dict()