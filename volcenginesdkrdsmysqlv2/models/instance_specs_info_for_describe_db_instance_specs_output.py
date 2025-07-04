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


class InstanceSpecsInfoForDescribeDBInstanceSpecsOutput(object):
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
        'connection': 'int',
        'db_engine_version': 'str',
        'iops': 'int',
        'instance_type': 'str',
        'memory': 'int',
        'qps': 'int',
        'region_id': 'str',
        'spec_code': 'str',
        'spec_family': 'str',
        'spec_status': 'str',
        'storage_max': 'int',
        'storage_min': 'int',
        'storage_step': 'int',
        'storage_type': 'str',
        'vcpu': 'int',
        'zone_id': 'str'
    }

    attribute_map = {
        'connection': 'Connection',
        'db_engine_version': 'DBEngineVersion',
        'iops': 'IOPS',
        'instance_type': 'InstanceType',
        'memory': 'Memory',
        'qps': 'QPS',
        'region_id': 'RegionId',
        'spec_code': 'SpecCode',
        'spec_family': 'SpecFamily',
        'spec_status': 'SpecStatus',
        'storage_max': 'StorageMax',
        'storage_min': 'StorageMin',
        'storage_step': 'StorageStep',
        'storage_type': 'StorageType',
        'vcpu': 'VCPU',
        'zone_id': 'ZoneId'
    }

    def __init__(self, connection=None, db_engine_version=None, iops=None, instance_type=None, memory=None, qps=None, region_id=None, spec_code=None, spec_family=None, spec_status=None, storage_max=None, storage_min=None, storage_step=None, storage_type=None, vcpu=None, zone_id=None, _configuration=None):  # noqa: E501
        """InstanceSpecsInfoForDescribeDBInstanceSpecsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._connection = None
        self._db_engine_version = None
        self._iops = None
        self._instance_type = None
        self._memory = None
        self._qps = None
        self._region_id = None
        self._spec_code = None
        self._spec_family = None
        self._spec_status = None
        self._storage_max = None
        self._storage_min = None
        self._storage_step = None
        self._storage_type = None
        self._vcpu = None
        self._zone_id = None
        self.discriminator = None

        if connection is not None:
            self.connection = connection
        if db_engine_version is not None:
            self.db_engine_version = db_engine_version
        if iops is not None:
            self.iops = iops
        if instance_type is not None:
            self.instance_type = instance_type
        if memory is not None:
            self.memory = memory
        if qps is not None:
            self.qps = qps
        if region_id is not None:
            self.region_id = region_id
        if spec_code is not None:
            self.spec_code = spec_code
        if spec_family is not None:
            self.spec_family = spec_family
        if spec_status is not None:
            self.spec_status = spec_status
        if storage_max is not None:
            self.storage_max = storage_max
        if storage_min is not None:
            self.storage_min = storage_min
        if storage_step is not None:
            self.storage_step = storage_step
        if storage_type is not None:
            self.storage_type = storage_type
        if vcpu is not None:
            self.vcpu = vcpu
        if zone_id is not None:
            self.zone_id = zone_id

    @property
    def connection(self):
        """Gets the connection of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.  # noqa: E501


        :return: The connection of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.  # noqa: E501
        :rtype: int
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        """Sets the connection of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.


        :param connection: The connection of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.  # noqa: E501
        :type: int
        """

        self._connection = connection

    @property
    def db_engine_version(self):
        """Gets the db_engine_version of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.  # noqa: E501


        :return: The db_engine_version of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.  # noqa: E501
        :rtype: str
        """
        return self._db_engine_version

    @db_engine_version.setter
    def db_engine_version(self, db_engine_version):
        """Sets the db_engine_version of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.


        :param db_engine_version: The db_engine_version of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.  # noqa: E501
        :type: str
        """

        self._db_engine_version = db_engine_version

    @property
    def iops(self):
        """Gets the iops of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.  # noqa: E501


        :return: The iops of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.  # noqa: E501
        :rtype: int
        """
        return self._iops

    @iops.setter
    def iops(self, iops):
        """Sets the iops of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.


        :param iops: The iops of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.  # noqa: E501
        :type: int
        """

        self._iops = iops

    @property
    def instance_type(self):
        """Gets the instance_type of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.  # noqa: E501


        :return: The instance_type of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.


        :param instance_type: The instance_type of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.  # noqa: E501
        :type: str
        """

        self._instance_type = instance_type

    @property
    def memory(self):
        """Gets the memory of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.  # noqa: E501


        :return: The memory of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.  # noqa: E501
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.


        :param memory: The memory of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.  # noqa: E501
        :type: int
        """

        self._memory = memory

    @property
    def qps(self):
        """Gets the qps of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.  # noqa: E501


        :return: The qps of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.  # noqa: E501
        :rtype: int
        """
        return self._qps

    @qps.setter
    def qps(self, qps):
        """Sets the qps of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.


        :param qps: The qps of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.  # noqa: E501
        :type: int
        """

        self._qps = qps

    @property
    def region_id(self):
        """Gets the region_id of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.  # noqa: E501


        :return: The region_id of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.  # noqa: E501
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.


        :param region_id: The region_id of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.  # noqa: E501
        :type: str
        """

        self._region_id = region_id

    @property
    def spec_code(self):
        """Gets the spec_code of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.  # noqa: E501


        :return: The spec_code of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.  # noqa: E501
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        """Sets the spec_code of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.


        :param spec_code: The spec_code of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.  # noqa: E501
        :type: str
        """

        self._spec_code = spec_code

    @property
    def spec_family(self):
        """Gets the spec_family of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.  # noqa: E501


        :return: The spec_family of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.  # noqa: E501
        :rtype: str
        """
        return self._spec_family

    @spec_family.setter
    def spec_family(self, spec_family):
        """Sets the spec_family of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.


        :param spec_family: The spec_family of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.  # noqa: E501
        :type: str
        """

        self._spec_family = spec_family

    @property
    def spec_status(self):
        """Gets the spec_status of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.  # noqa: E501


        :return: The spec_status of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.  # noqa: E501
        :rtype: str
        """
        return self._spec_status

    @spec_status.setter
    def spec_status(self, spec_status):
        """Sets the spec_status of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.


        :param spec_status: The spec_status of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.  # noqa: E501
        :type: str
        """

        self._spec_status = spec_status

    @property
    def storage_max(self):
        """Gets the storage_max of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.  # noqa: E501


        :return: The storage_max of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.  # noqa: E501
        :rtype: int
        """
        return self._storage_max

    @storage_max.setter
    def storage_max(self, storage_max):
        """Sets the storage_max of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.


        :param storage_max: The storage_max of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.  # noqa: E501
        :type: int
        """

        self._storage_max = storage_max

    @property
    def storage_min(self):
        """Gets the storage_min of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.  # noqa: E501


        :return: The storage_min of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.  # noqa: E501
        :rtype: int
        """
        return self._storage_min

    @storage_min.setter
    def storage_min(self, storage_min):
        """Sets the storage_min of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.


        :param storage_min: The storage_min of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.  # noqa: E501
        :type: int
        """

        self._storage_min = storage_min

    @property
    def storage_step(self):
        """Gets the storage_step of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.  # noqa: E501


        :return: The storage_step of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.  # noqa: E501
        :rtype: int
        """
        return self._storage_step

    @storage_step.setter
    def storage_step(self, storage_step):
        """Sets the storage_step of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.


        :param storage_step: The storage_step of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.  # noqa: E501
        :type: int
        """

        self._storage_step = storage_step

    @property
    def storage_type(self):
        """Gets the storage_type of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.  # noqa: E501


        :return: The storage_type of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.  # noqa: E501
        :rtype: str
        """
        return self._storage_type

    @storage_type.setter
    def storage_type(self, storage_type):
        """Sets the storage_type of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.


        :param storage_type: The storage_type of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.  # noqa: E501
        :type: str
        """

        self._storage_type = storage_type

    @property
    def vcpu(self):
        """Gets the vcpu of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.  # noqa: E501


        :return: The vcpu of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.  # noqa: E501
        :rtype: int
        """
        return self._vcpu

    @vcpu.setter
    def vcpu(self, vcpu):
        """Sets the vcpu of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.


        :param vcpu: The vcpu of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.  # noqa: E501
        :type: int
        """

        self._vcpu = vcpu

    @property
    def zone_id(self):
        """Gets the zone_id of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.  # noqa: E501


        :return: The zone_id of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.


        :param zone_id: The zone_id of this InstanceSpecsInfoForDescribeDBInstanceSpecsOutput.  # noqa: E501
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
        if issubclass(InstanceSpecsInfoForDescribeDBInstanceSpecsOutput, dict):
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
        if not isinstance(other, InstanceSpecsInfoForDescribeDBInstanceSpecsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InstanceSpecsInfoForDescribeDBInstanceSpecsOutput):
            return True

        return self.to_dict() != other.to_dict()
