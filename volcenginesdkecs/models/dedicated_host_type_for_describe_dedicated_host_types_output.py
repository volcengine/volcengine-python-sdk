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


class DedicatedHostTypeForDescribeDedicatedHostTypesOutput(object):
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
        'cores': 'int',
        'dedicated_host_type_id': 'str',
        'is_supported_cpu_overcommit_ratio': 'bool',
        'local_volumes': 'list[LocalVolumeForDescribeDedicatedHostTypesOutput]',
        'max_cpu_overcommit_ratio': 'float',
        'processor_model': 'str',
        'sockets': 'int',
        'support_instance_type_families': 'list[str]',
        'support_instance_types_list': 'list[str]',
        'total_memory': 'int',
        'total_vcpus': 'int'
    }

    attribute_map = {
        'cores': 'Cores',
        'dedicated_host_type_id': 'DedicatedHostTypeId',
        'is_supported_cpu_overcommit_ratio': 'IsSupportedCpuOvercommitRatio',
        'local_volumes': 'LocalVolumes',
        'max_cpu_overcommit_ratio': 'MaxCpuOvercommitRatio',
        'processor_model': 'ProcessorModel',
        'sockets': 'Sockets',
        'support_instance_type_families': 'SupportInstanceTypeFamilies',
        'support_instance_types_list': 'SupportInstanceTypesList',
        'total_memory': 'TotalMemory',
        'total_vcpus': 'TotalVcpus'
    }

    def __init__(self, cores=None, dedicated_host_type_id=None, is_supported_cpu_overcommit_ratio=None, local_volumes=None, max_cpu_overcommit_ratio=None, processor_model=None, sockets=None, support_instance_type_families=None, support_instance_types_list=None, total_memory=None, total_vcpus=None, _configuration=None):  # noqa: E501
        """DedicatedHostTypeForDescribeDedicatedHostTypesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cores = None
        self._dedicated_host_type_id = None
        self._is_supported_cpu_overcommit_ratio = None
        self._local_volumes = None
        self._max_cpu_overcommit_ratio = None
        self._processor_model = None
        self._sockets = None
        self._support_instance_type_families = None
        self._support_instance_types_list = None
        self._total_memory = None
        self._total_vcpus = None
        self.discriminator = None

        if cores is not None:
            self.cores = cores
        if dedicated_host_type_id is not None:
            self.dedicated_host_type_id = dedicated_host_type_id
        if is_supported_cpu_overcommit_ratio is not None:
            self.is_supported_cpu_overcommit_ratio = is_supported_cpu_overcommit_ratio
        if local_volumes is not None:
            self.local_volumes = local_volumes
        if max_cpu_overcommit_ratio is not None:
            self.max_cpu_overcommit_ratio = max_cpu_overcommit_ratio
        if processor_model is not None:
            self.processor_model = processor_model
        if sockets is not None:
            self.sockets = sockets
        if support_instance_type_families is not None:
            self.support_instance_type_families = support_instance_type_families
        if support_instance_types_list is not None:
            self.support_instance_types_list = support_instance_types_list
        if total_memory is not None:
            self.total_memory = total_memory
        if total_vcpus is not None:
            self.total_vcpus = total_vcpus

    @property
    def cores(self):
        """Gets the cores of this DedicatedHostTypeForDescribeDedicatedHostTypesOutput.  # noqa: E501


        :return: The cores of this DedicatedHostTypeForDescribeDedicatedHostTypesOutput.  # noqa: E501
        :rtype: int
        """
        return self._cores

    @cores.setter
    def cores(self, cores):
        """Sets the cores of this DedicatedHostTypeForDescribeDedicatedHostTypesOutput.


        :param cores: The cores of this DedicatedHostTypeForDescribeDedicatedHostTypesOutput.  # noqa: E501
        :type: int
        """

        self._cores = cores

    @property
    def dedicated_host_type_id(self):
        """Gets the dedicated_host_type_id of this DedicatedHostTypeForDescribeDedicatedHostTypesOutput.  # noqa: E501


        :return: The dedicated_host_type_id of this DedicatedHostTypeForDescribeDedicatedHostTypesOutput.  # noqa: E501
        :rtype: str
        """
        return self._dedicated_host_type_id

    @dedicated_host_type_id.setter
    def dedicated_host_type_id(self, dedicated_host_type_id):
        """Sets the dedicated_host_type_id of this DedicatedHostTypeForDescribeDedicatedHostTypesOutput.


        :param dedicated_host_type_id: The dedicated_host_type_id of this DedicatedHostTypeForDescribeDedicatedHostTypesOutput.  # noqa: E501
        :type: str
        """

        self._dedicated_host_type_id = dedicated_host_type_id

    @property
    def is_supported_cpu_overcommit_ratio(self):
        """Gets the is_supported_cpu_overcommit_ratio of this DedicatedHostTypeForDescribeDedicatedHostTypesOutput.  # noqa: E501


        :return: The is_supported_cpu_overcommit_ratio of this DedicatedHostTypeForDescribeDedicatedHostTypesOutput.  # noqa: E501
        :rtype: bool
        """
        return self._is_supported_cpu_overcommit_ratio

    @is_supported_cpu_overcommit_ratio.setter
    def is_supported_cpu_overcommit_ratio(self, is_supported_cpu_overcommit_ratio):
        """Sets the is_supported_cpu_overcommit_ratio of this DedicatedHostTypeForDescribeDedicatedHostTypesOutput.


        :param is_supported_cpu_overcommit_ratio: The is_supported_cpu_overcommit_ratio of this DedicatedHostTypeForDescribeDedicatedHostTypesOutput.  # noqa: E501
        :type: bool
        """

        self._is_supported_cpu_overcommit_ratio = is_supported_cpu_overcommit_ratio

    @property
    def local_volumes(self):
        """Gets the local_volumes of this DedicatedHostTypeForDescribeDedicatedHostTypesOutput.  # noqa: E501


        :return: The local_volumes of this DedicatedHostTypeForDescribeDedicatedHostTypesOutput.  # noqa: E501
        :rtype: list[LocalVolumeForDescribeDedicatedHostTypesOutput]
        """
        return self._local_volumes

    @local_volumes.setter
    def local_volumes(self, local_volumes):
        """Sets the local_volumes of this DedicatedHostTypeForDescribeDedicatedHostTypesOutput.


        :param local_volumes: The local_volumes of this DedicatedHostTypeForDescribeDedicatedHostTypesOutput.  # noqa: E501
        :type: list[LocalVolumeForDescribeDedicatedHostTypesOutput]
        """

        self._local_volumes = local_volumes

    @property
    def max_cpu_overcommit_ratio(self):
        """Gets the max_cpu_overcommit_ratio of this DedicatedHostTypeForDescribeDedicatedHostTypesOutput.  # noqa: E501


        :return: The max_cpu_overcommit_ratio of this DedicatedHostTypeForDescribeDedicatedHostTypesOutput.  # noqa: E501
        :rtype: float
        """
        return self._max_cpu_overcommit_ratio

    @max_cpu_overcommit_ratio.setter
    def max_cpu_overcommit_ratio(self, max_cpu_overcommit_ratio):
        """Sets the max_cpu_overcommit_ratio of this DedicatedHostTypeForDescribeDedicatedHostTypesOutput.


        :param max_cpu_overcommit_ratio: The max_cpu_overcommit_ratio of this DedicatedHostTypeForDescribeDedicatedHostTypesOutput.  # noqa: E501
        :type: float
        """

        self._max_cpu_overcommit_ratio = max_cpu_overcommit_ratio

    @property
    def processor_model(self):
        """Gets the processor_model of this DedicatedHostTypeForDescribeDedicatedHostTypesOutput.  # noqa: E501


        :return: The processor_model of this DedicatedHostTypeForDescribeDedicatedHostTypesOutput.  # noqa: E501
        :rtype: str
        """
        return self._processor_model

    @processor_model.setter
    def processor_model(self, processor_model):
        """Sets the processor_model of this DedicatedHostTypeForDescribeDedicatedHostTypesOutput.


        :param processor_model: The processor_model of this DedicatedHostTypeForDescribeDedicatedHostTypesOutput.  # noqa: E501
        :type: str
        """

        self._processor_model = processor_model

    @property
    def sockets(self):
        """Gets the sockets of this DedicatedHostTypeForDescribeDedicatedHostTypesOutput.  # noqa: E501


        :return: The sockets of this DedicatedHostTypeForDescribeDedicatedHostTypesOutput.  # noqa: E501
        :rtype: int
        """
        return self._sockets

    @sockets.setter
    def sockets(self, sockets):
        """Sets the sockets of this DedicatedHostTypeForDescribeDedicatedHostTypesOutput.


        :param sockets: The sockets of this DedicatedHostTypeForDescribeDedicatedHostTypesOutput.  # noqa: E501
        :type: int
        """

        self._sockets = sockets

    @property
    def support_instance_type_families(self):
        """Gets the support_instance_type_families of this DedicatedHostTypeForDescribeDedicatedHostTypesOutput.  # noqa: E501


        :return: The support_instance_type_families of this DedicatedHostTypeForDescribeDedicatedHostTypesOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._support_instance_type_families

    @support_instance_type_families.setter
    def support_instance_type_families(self, support_instance_type_families):
        """Sets the support_instance_type_families of this DedicatedHostTypeForDescribeDedicatedHostTypesOutput.


        :param support_instance_type_families: The support_instance_type_families of this DedicatedHostTypeForDescribeDedicatedHostTypesOutput.  # noqa: E501
        :type: list[str]
        """

        self._support_instance_type_families = support_instance_type_families

    @property
    def support_instance_types_list(self):
        """Gets the support_instance_types_list of this DedicatedHostTypeForDescribeDedicatedHostTypesOutput.  # noqa: E501


        :return: The support_instance_types_list of this DedicatedHostTypeForDescribeDedicatedHostTypesOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._support_instance_types_list

    @support_instance_types_list.setter
    def support_instance_types_list(self, support_instance_types_list):
        """Sets the support_instance_types_list of this DedicatedHostTypeForDescribeDedicatedHostTypesOutput.


        :param support_instance_types_list: The support_instance_types_list of this DedicatedHostTypeForDescribeDedicatedHostTypesOutput.  # noqa: E501
        :type: list[str]
        """

        self._support_instance_types_list = support_instance_types_list

    @property
    def total_memory(self):
        """Gets the total_memory of this DedicatedHostTypeForDescribeDedicatedHostTypesOutput.  # noqa: E501


        :return: The total_memory of this DedicatedHostTypeForDescribeDedicatedHostTypesOutput.  # noqa: E501
        :rtype: int
        """
        return self._total_memory

    @total_memory.setter
    def total_memory(self, total_memory):
        """Sets the total_memory of this DedicatedHostTypeForDescribeDedicatedHostTypesOutput.


        :param total_memory: The total_memory of this DedicatedHostTypeForDescribeDedicatedHostTypesOutput.  # noqa: E501
        :type: int
        """

        self._total_memory = total_memory

    @property
    def total_vcpus(self):
        """Gets the total_vcpus of this DedicatedHostTypeForDescribeDedicatedHostTypesOutput.  # noqa: E501


        :return: The total_vcpus of this DedicatedHostTypeForDescribeDedicatedHostTypesOutput.  # noqa: E501
        :rtype: int
        """
        return self._total_vcpus

    @total_vcpus.setter
    def total_vcpus(self, total_vcpus):
        """Sets the total_vcpus of this DedicatedHostTypeForDescribeDedicatedHostTypesOutput.


        :param total_vcpus: The total_vcpus of this DedicatedHostTypeForDescribeDedicatedHostTypesOutput.  # noqa: E501
        :type: int
        """

        self._total_vcpus = total_vcpus

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
        if issubclass(DedicatedHostTypeForDescribeDedicatedHostTypesOutput, dict):
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
        if not isinstance(other, DedicatedHostTypeForDescribeDedicatedHostTypesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DedicatedHostTypeForDescribeDedicatedHostTypesOutput):
            return True

        return self.to_dict() != other.to_dict()
