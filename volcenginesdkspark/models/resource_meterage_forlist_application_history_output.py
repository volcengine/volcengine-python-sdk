# coding: utf-8

"""
    spark

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ResourceMeterageForlistApplicationHistoryOutput(object):
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
        'cpu': 'str',
        'memory': 'str'
    }

    attribute_map = {
        'cpu': 'cpu',
        'memory': 'memory'
    }

    def __init__(self, cpu=None, memory=None, _configuration=None):  # noqa: E501
        """ResourceMeterageForlistApplicationHistoryOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cpu = None
        self._memory = None
        self.discriminator = None

        if cpu is not None:
            self.cpu = cpu
        if memory is not None:
            self.memory = memory

    @property
    def cpu(self):
        """Gets the cpu of this ResourceMeterageForlistApplicationHistoryOutput.  # noqa: E501


        :return: The cpu of this ResourceMeterageForlistApplicationHistoryOutput.  # noqa: E501
        :rtype: str
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this ResourceMeterageForlistApplicationHistoryOutput.


        :param cpu: The cpu of this ResourceMeterageForlistApplicationHistoryOutput.  # noqa: E501
        :type: str
        """

        self._cpu = cpu

    @property
    def memory(self):
        """Gets the memory of this ResourceMeterageForlistApplicationHistoryOutput.  # noqa: E501


        :return: The memory of this ResourceMeterageForlistApplicationHistoryOutput.  # noqa: E501
        :rtype: str
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this ResourceMeterageForlistApplicationHistoryOutput.


        :param memory: The memory of this ResourceMeterageForlistApplicationHistoryOutput.  # noqa: E501
        :type: str
        """

        self._memory = memory

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
        if issubclass(ResourceMeterageForlistApplicationHistoryOutput, dict):
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
        if not isinstance(other, ResourceMeterageForlistApplicationHistoryOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResourceMeterageForlistApplicationHistoryOutput):
            return True

        return self.to_dict() != other.to_dict()
