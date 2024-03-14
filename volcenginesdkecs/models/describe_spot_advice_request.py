# coding: utf-8

"""
    ecs

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeSpotAdviceRequest(object):
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
        'cpus': 'int',
        'gpu': 'GpuForDescribeSpotAdviceInput',
        'instance_type_family': 'str',
        'instance_type_ids': 'list[str]',
        'max_results': 'int',
        'memory_size': 'int',
        'min_cpus': 'int',
        'min_memory_size': 'int',
        'next_token': 'str',
        'zone_id': 'str'
    }

    attribute_map = {
        'cpus': 'Cpus',
        'gpu': 'Gpu',
        'instance_type_family': 'InstanceTypeFamily',
        'instance_type_ids': 'InstanceTypeIds',
        'max_results': 'MaxResults',
        'memory_size': 'MemorySize',
        'min_cpus': 'MinCpus',
        'min_memory_size': 'MinMemorySize',
        'next_token': 'NextToken',
        'zone_id': 'ZoneId'
    }

    def __init__(self, cpus=None, gpu=None, instance_type_family=None, instance_type_ids=None, max_results=None, memory_size=None, min_cpus=None, min_memory_size=None, next_token=None, zone_id=None, _configuration=None):  # noqa: E501
        """DescribeSpotAdviceRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cpus = None
        self._gpu = None
        self._instance_type_family = None
        self._instance_type_ids = None
        self._max_results = None
        self._memory_size = None
        self._min_cpus = None
        self._min_memory_size = None
        self._next_token = None
        self._zone_id = None
        self.discriminator = None

        if cpus is not None:
            self.cpus = cpus
        if gpu is not None:
            self.gpu = gpu
        if instance_type_family is not None:
            self.instance_type_family = instance_type_family
        if instance_type_ids is not None:
            self.instance_type_ids = instance_type_ids
        if max_results is not None:
            self.max_results = max_results
        if memory_size is not None:
            self.memory_size = memory_size
        if min_cpus is not None:
            self.min_cpus = min_cpus
        if min_memory_size is not None:
            self.min_memory_size = min_memory_size
        if next_token is not None:
            self.next_token = next_token
        if zone_id is not None:
            self.zone_id = zone_id

    @property
    def cpus(self):
        """Gets the cpus of this DescribeSpotAdviceRequest.  # noqa: E501


        :return: The cpus of this DescribeSpotAdviceRequest.  # noqa: E501
        :rtype: int
        """
        return self._cpus

    @cpus.setter
    def cpus(self, cpus):
        """Sets the cpus of this DescribeSpotAdviceRequest.


        :param cpus: The cpus of this DescribeSpotAdviceRequest.  # noqa: E501
        :type: int
        """

        self._cpus = cpus

    @property
    def gpu(self):
        """Gets the gpu of this DescribeSpotAdviceRequest.  # noqa: E501


        :return: The gpu of this DescribeSpotAdviceRequest.  # noqa: E501
        :rtype: GpuForDescribeSpotAdviceInput
        """
        return self._gpu

    @gpu.setter
    def gpu(self, gpu):
        """Sets the gpu of this DescribeSpotAdviceRequest.


        :param gpu: The gpu of this DescribeSpotAdviceRequest.  # noqa: E501
        :type: GpuForDescribeSpotAdviceInput
        """

        self._gpu = gpu

    @property
    def instance_type_family(self):
        """Gets the instance_type_family of this DescribeSpotAdviceRequest.  # noqa: E501


        :return: The instance_type_family of this DescribeSpotAdviceRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_type_family

    @instance_type_family.setter
    def instance_type_family(self, instance_type_family):
        """Sets the instance_type_family of this DescribeSpotAdviceRequest.


        :param instance_type_family: The instance_type_family of this DescribeSpotAdviceRequest.  # noqa: E501
        :type: str
        """

        self._instance_type_family = instance_type_family

    @property
    def instance_type_ids(self):
        """Gets the instance_type_ids of this DescribeSpotAdviceRequest.  # noqa: E501


        :return: The instance_type_ids of this DescribeSpotAdviceRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._instance_type_ids

    @instance_type_ids.setter
    def instance_type_ids(self, instance_type_ids):
        """Sets the instance_type_ids of this DescribeSpotAdviceRequest.


        :param instance_type_ids: The instance_type_ids of this DescribeSpotAdviceRequest.  # noqa: E501
        :type: list[str]
        """

        self._instance_type_ids = instance_type_ids

    @property
    def max_results(self):
        """Gets the max_results of this DescribeSpotAdviceRequest.  # noqa: E501


        :return: The max_results of this DescribeSpotAdviceRequest.  # noqa: E501
        :rtype: int
        """
        return self._max_results

    @max_results.setter
    def max_results(self, max_results):
        """Sets the max_results of this DescribeSpotAdviceRequest.


        :param max_results: The max_results of this DescribeSpotAdviceRequest.  # noqa: E501
        :type: int
        """

        self._max_results = max_results

    @property
    def memory_size(self):
        """Gets the memory_size of this DescribeSpotAdviceRequest.  # noqa: E501


        :return: The memory_size of this DescribeSpotAdviceRequest.  # noqa: E501
        :rtype: int
        """
        return self._memory_size

    @memory_size.setter
    def memory_size(self, memory_size):
        """Sets the memory_size of this DescribeSpotAdviceRequest.


        :param memory_size: The memory_size of this DescribeSpotAdviceRequest.  # noqa: E501
        :type: int
        """

        self._memory_size = memory_size

    @property
    def min_cpus(self):
        """Gets the min_cpus of this DescribeSpotAdviceRequest.  # noqa: E501


        :return: The min_cpus of this DescribeSpotAdviceRequest.  # noqa: E501
        :rtype: int
        """
        return self._min_cpus

    @min_cpus.setter
    def min_cpus(self, min_cpus):
        """Sets the min_cpus of this DescribeSpotAdviceRequest.


        :param min_cpus: The min_cpus of this DescribeSpotAdviceRequest.  # noqa: E501
        :type: int
        """

        self._min_cpus = min_cpus

    @property
    def min_memory_size(self):
        """Gets the min_memory_size of this DescribeSpotAdviceRequest.  # noqa: E501


        :return: The min_memory_size of this DescribeSpotAdviceRequest.  # noqa: E501
        :rtype: int
        """
        return self._min_memory_size

    @min_memory_size.setter
    def min_memory_size(self, min_memory_size):
        """Sets the min_memory_size of this DescribeSpotAdviceRequest.


        :param min_memory_size: The min_memory_size of this DescribeSpotAdviceRequest.  # noqa: E501
        :type: int
        """

        self._min_memory_size = min_memory_size

    @property
    def next_token(self):
        """Gets the next_token of this DescribeSpotAdviceRequest.  # noqa: E501


        :return: The next_token of this DescribeSpotAdviceRequest.  # noqa: E501
        :rtype: str
        """
        return self._next_token

    @next_token.setter
    def next_token(self, next_token):
        """Sets the next_token of this DescribeSpotAdviceRequest.


        :param next_token: The next_token of this DescribeSpotAdviceRequest.  # noqa: E501
        :type: str
        """

        self._next_token = next_token

    @property
    def zone_id(self):
        """Gets the zone_id of this DescribeSpotAdviceRequest.  # noqa: E501


        :return: The zone_id of this DescribeSpotAdviceRequest.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this DescribeSpotAdviceRequest.


        :param zone_id: The zone_id of this DescribeSpotAdviceRequest.  # noqa: E501
        :type: str
        """

        self._zone_id = zone_id

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
        if issubclass(DescribeSpotAdviceRequest, dict):
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
        if not isinstance(other, DescribeSpotAdviceRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeSpotAdviceRequest):
            return True

        return self.to_dict() != other.to_dict()
