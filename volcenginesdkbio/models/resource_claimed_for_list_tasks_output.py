# coding: utf-8

"""
    bio

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ResourceClaimedForListTasksOutput(object):
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
        'cpu_core': 'float',
        'gpugi_b': 'float',
        'memory_gi_b': 'float',
        'storage_gi_b': 'float'
    }

    attribute_map = {
        'cpu_core': 'CPUCore',
        'gpugi_b': 'GPUGiB',
        'memory_gi_b': 'MemoryGiB',
        'storage_gi_b': 'StorageGiB'
    }

    def __init__(self, cpu_core=None, gpugi_b=None, memory_gi_b=None, storage_gi_b=None, _configuration=None):  # noqa: E501
        """ResourceClaimedForListTasksOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cpu_core = None
        self._gpugi_b = None
        self._memory_gi_b = None
        self._storage_gi_b = None
        self.discriminator = None

        if cpu_core is not None:
            self.cpu_core = cpu_core
        if gpugi_b is not None:
            self.gpugi_b = gpugi_b
        if memory_gi_b is not None:
            self.memory_gi_b = memory_gi_b
        if storage_gi_b is not None:
            self.storage_gi_b = storage_gi_b

    @property
    def cpu_core(self):
        """Gets the cpu_core of this ResourceClaimedForListTasksOutput.  # noqa: E501


        :return: The cpu_core of this ResourceClaimedForListTasksOutput.  # noqa: E501
        :rtype: float
        """
        return self._cpu_core

    @cpu_core.setter
    def cpu_core(self, cpu_core):
        """Sets the cpu_core of this ResourceClaimedForListTasksOutput.


        :param cpu_core: The cpu_core of this ResourceClaimedForListTasksOutput.  # noqa: E501
        :type: float
        """

        self._cpu_core = cpu_core

    @property
    def gpugi_b(self):
        """Gets the gpugi_b of this ResourceClaimedForListTasksOutput.  # noqa: E501


        :return: The gpugi_b of this ResourceClaimedForListTasksOutput.  # noqa: E501
        :rtype: float
        """
        return self._gpugi_b

    @gpugi_b.setter
    def gpugi_b(self, gpugi_b):
        """Sets the gpugi_b of this ResourceClaimedForListTasksOutput.


        :param gpugi_b: The gpugi_b of this ResourceClaimedForListTasksOutput.  # noqa: E501
        :type: float
        """

        self._gpugi_b = gpugi_b

    @property
    def memory_gi_b(self):
        """Gets the memory_gi_b of this ResourceClaimedForListTasksOutput.  # noqa: E501


        :return: The memory_gi_b of this ResourceClaimedForListTasksOutput.  # noqa: E501
        :rtype: float
        """
        return self._memory_gi_b

    @memory_gi_b.setter
    def memory_gi_b(self, memory_gi_b):
        """Sets the memory_gi_b of this ResourceClaimedForListTasksOutput.


        :param memory_gi_b: The memory_gi_b of this ResourceClaimedForListTasksOutput.  # noqa: E501
        :type: float
        """

        self._memory_gi_b = memory_gi_b

    @property
    def storage_gi_b(self):
        """Gets the storage_gi_b of this ResourceClaimedForListTasksOutput.  # noqa: E501


        :return: The storage_gi_b of this ResourceClaimedForListTasksOutput.  # noqa: E501
        :rtype: float
        """
        return self._storage_gi_b

    @storage_gi_b.setter
    def storage_gi_b(self, storage_gi_b):
        """Sets the storage_gi_b of this ResourceClaimedForListTasksOutput.


        :param storage_gi_b: The storage_gi_b of this ResourceClaimedForListTasksOutput.  # noqa: E501
        :type: float
        """

        self._storage_gi_b = storage_gi_b

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
        if issubclass(ResourceClaimedForListTasksOutput, dict):
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
        if not isinstance(other, ResourceClaimedForListTasksOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResourceClaimedForListTasksOutput):
            return True

        return self.to_dict() != other.to_dict()
