# coding: utf-8

"""
    mongodb

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class RestoreToNewInstanceRequest(object):
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
        'auto_renew': 'bool',
        'backup_id': 'str',
        'charge_type': 'str',
        'db_engine': 'str',
        'db_engine_version': 'str',
        'instance_name': 'str',
        'instance_type': 'str',
        'mongos_node_number': 'int',
        'mongos_node_spec': 'str',
        'node_number': 'int',
        'node_spec': 'str',
        'number': 'int',
        'period': 'int',
        'period_unit': 'str',
        'project_name': 'str',
        'restore_time': 'str',
        'shard_number': 'int',
        'src_db_instance_id': 'str',
        'storage_space_gb': 'int',
        'subnet_id': 'str',
        'super_account_name': 'str',
        'super_account_password': 'str',
        'vpc_id': 'str',
        'zone_id': 'str'
    }

    attribute_map = {
        'auto_renew': 'AutoRenew',
        'backup_id': 'BackupId',
        'charge_type': 'ChargeType',
        'db_engine': 'DBEngine',
        'db_engine_version': 'DBEngineVersion',
        'instance_name': 'InstanceName',
        'instance_type': 'InstanceType',
        'mongos_node_number': 'MongosNodeNumber',
        'mongos_node_spec': 'MongosNodeSpec',
        'node_number': 'NodeNumber',
        'node_spec': 'NodeSpec',
        'number': 'Number',
        'period': 'Period',
        'period_unit': 'PeriodUnit',
        'project_name': 'ProjectName',
        'restore_time': 'RestoreTime',
        'shard_number': 'ShardNumber',
        'src_db_instance_id': 'SrcDBInstanceId',
        'storage_space_gb': 'StorageSpaceGB',
        'subnet_id': 'SubnetId',
        'super_account_name': 'SuperAccountName',
        'super_account_password': 'SuperAccountPassword',
        'vpc_id': 'VpcId',
        'zone_id': 'ZoneId'
    }

    def __init__(self, auto_renew=None, backup_id=None, charge_type=None, db_engine=None, db_engine_version=None, instance_name=None, instance_type=None, mongos_node_number=None, mongos_node_spec=None, node_number=None, node_spec=None, number=None, period=None, period_unit=None, project_name=None, restore_time=None, shard_number=None, src_db_instance_id=None, storage_space_gb=None, subnet_id=None, super_account_name=None, super_account_password=None, vpc_id=None, zone_id=None, _configuration=None):  # noqa: E501
        """RestoreToNewInstanceRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._auto_renew = None
        self._backup_id = None
        self._charge_type = None
        self._db_engine = None
        self._db_engine_version = None
        self._instance_name = None
        self._instance_type = None
        self._mongos_node_number = None
        self._mongos_node_spec = None
        self._node_number = None
        self._node_spec = None
        self._number = None
        self._period = None
        self._period_unit = None
        self._project_name = None
        self._restore_time = None
        self._shard_number = None
        self._src_db_instance_id = None
        self._storage_space_gb = None
        self._subnet_id = None
        self._super_account_name = None
        self._super_account_password = None
        self._vpc_id = None
        self._zone_id = None
        self.discriminator = None

        if auto_renew is not None:
            self.auto_renew = auto_renew
        if backup_id is not None:
            self.backup_id = backup_id
        if charge_type is not None:
            self.charge_type = charge_type
        if db_engine is not None:
            self.db_engine = db_engine
        if db_engine_version is not None:
            self.db_engine_version = db_engine_version
        if instance_name is not None:
            self.instance_name = instance_name
        if instance_type is not None:
            self.instance_type = instance_type
        if mongos_node_number is not None:
            self.mongos_node_number = mongos_node_number
        if mongos_node_spec is not None:
            self.mongos_node_spec = mongos_node_spec
        if node_number is not None:
            self.node_number = node_number
        self.node_spec = node_spec
        if number is not None:
            self.number = number
        if period is not None:
            self.period = period
        if period_unit is not None:
            self.period_unit = period_unit
        if project_name is not None:
            self.project_name = project_name
        if restore_time is not None:
            self.restore_time = restore_time
        if shard_number is not None:
            self.shard_number = shard_number
        self.src_db_instance_id = src_db_instance_id
        self.storage_space_gb = storage_space_gb
        self.subnet_id = subnet_id
        if super_account_name is not None:
            self.super_account_name = super_account_name
        if super_account_password is not None:
            self.super_account_password = super_account_password
        self.vpc_id = vpc_id
        self.zone_id = zone_id

    @property
    def auto_renew(self):
        """Gets the auto_renew of this RestoreToNewInstanceRequest.  # noqa: E501


        :return: The auto_renew of this RestoreToNewInstanceRequest.  # noqa: E501
        :rtype: bool
        """
        return self._auto_renew

    @auto_renew.setter
    def auto_renew(self, auto_renew):
        """Sets the auto_renew of this RestoreToNewInstanceRequest.


        :param auto_renew: The auto_renew of this RestoreToNewInstanceRequest.  # noqa: E501
        :type: bool
        """

        self._auto_renew = auto_renew

    @property
    def backup_id(self):
        """Gets the backup_id of this RestoreToNewInstanceRequest.  # noqa: E501


        :return: The backup_id of this RestoreToNewInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        """Sets the backup_id of this RestoreToNewInstanceRequest.


        :param backup_id: The backup_id of this RestoreToNewInstanceRequest.  # noqa: E501
        :type: str
        """

        self._backup_id = backup_id

    @property
    def charge_type(self):
        """Gets the charge_type of this RestoreToNewInstanceRequest.  # noqa: E501


        :return: The charge_type of this RestoreToNewInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._charge_type

    @charge_type.setter
    def charge_type(self, charge_type):
        """Sets the charge_type of this RestoreToNewInstanceRequest.


        :param charge_type: The charge_type of this RestoreToNewInstanceRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["NotEnabled", "PostPaid", "Prepaid"]  # noqa: E501
        if (self._configuration.client_side_validation and
                charge_type not in allowed_values):
            raise ValueError(
                "Invalid value for `charge_type` ({0}), must be one of {1}"  # noqa: E501
                .format(charge_type, allowed_values)
            )

        self._charge_type = charge_type

    @property
    def db_engine(self):
        """Gets the db_engine of this RestoreToNewInstanceRequest.  # noqa: E501


        :return: The db_engine of this RestoreToNewInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._db_engine

    @db_engine.setter
    def db_engine(self, db_engine):
        """Sets the db_engine of this RestoreToNewInstanceRequest.


        :param db_engine: The db_engine of this RestoreToNewInstanceRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["MongoDB"]  # noqa: E501
        if (self._configuration.client_side_validation and
                db_engine not in allowed_values):
            raise ValueError(
                "Invalid value for `db_engine` ({0}), must be one of {1}"  # noqa: E501
                .format(db_engine, allowed_values)
            )

        self._db_engine = db_engine

    @property
    def db_engine_version(self):
        """Gets the db_engine_version of this RestoreToNewInstanceRequest.  # noqa: E501


        :return: The db_engine_version of this RestoreToNewInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._db_engine_version

    @db_engine_version.setter
    def db_engine_version(self, db_engine_version):
        """Sets the db_engine_version of this RestoreToNewInstanceRequest.


        :param db_engine_version: The db_engine_version of this RestoreToNewInstanceRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["MongoDB_4_0", "MongoDB_4_2", "MongoDB_4_4", "MongoDB_5_0", "MongoDB_6_0"]  # noqa: E501
        if (self._configuration.client_side_validation and
                db_engine_version not in allowed_values):
            raise ValueError(
                "Invalid value for `db_engine_version` ({0}), must be one of {1}"  # noqa: E501
                .format(db_engine_version, allowed_values)
            )

        self._db_engine_version = db_engine_version

    @property
    def instance_name(self):
        """Gets the instance_name of this RestoreToNewInstanceRequest.  # noqa: E501


        :return: The instance_name of this RestoreToNewInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this RestoreToNewInstanceRequest.


        :param instance_name: The instance_name of this RestoreToNewInstanceRequest.  # noqa: E501
        :type: str
        """

        self._instance_name = instance_name

    @property
    def instance_type(self):
        """Gets the instance_type of this RestoreToNewInstanceRequest.  # noqa: E501


        :return: The instance_type of this RestoreToNewInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this RestoreToNewInstanceRequest.


        :param instance_type: The instance_type of this RestoreToNewInstanceRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["ReplicaSet", "ShardedCluster"]  # noqa: E501
        if (self._configuration.client_side_validation and
                instance_type not in allowed_values):
            raise ValueError(
                "Invalid value for `instance_type` ({0}), must be one of {1}"  # noqa: E501
                .format(instance_type, allowed_values)
            )

        self._instance_type = instance_type

    @property
    def mongos_node_number(self):
        """Gets the mongos_node_number of this RestoreToNewInstanceRequest.  # noqa: E501


        :return: The mongos_node_number of this RestoreToNewInstanceRequest.  # noqa: E501
        :rtype: int
        """
        return self._mongos_node_number

    @mongos_node_number.setter
    def mongos_node_number(self, mongos_node_number):
        """Sets the mongos_node_number of this RestoreToNewInstanceRequest.


        :param mongos_node_number: The mongos_node_number of this RestoreToNewInstanceRequest.  # noqa: E501
        :type: int
        """

        self._mongos_node_number = mongos_node_number

    @property
    def mongos_node_spec(self):
        """Gets the mongos_node_spec of this RestoreToNewInstanceRequest.  # noqa: E501


        :return: The mongos_node_spec of this RestoreToNewInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._mongos_node_spec

    @mongos_node_spec.setter
    def mongos_node_spec(self, mongos_node_spec):
        """Sets the mongos_node_spec of this RestoreToNewInstanceRequest.


        :param mongos_node_spec: The mongos_node_spec of this RestoreToNewInstanceRequest.  # noqa: E501
        :type: str
        """

        self._mongos_node_spec = mongos_node_spec

    @property
    def node_number(self):
        """Gets the node_number of this RestoreToNewInstanceRequest.  # noqa: E501


        :return: The node_number of this RestoreToNewInstanceRequest.  # noqa: E501
        :rtype: int
        """
        return self._node_number

    @node_number.setter
    def node_number(self, node_number):
        """Sets the node_number of this RestoreToNewInstanceRequest.


        :param node_number: The node_number of this RestoreToNewInstanceRequest.  # noqa: E501
        :type: int
        """

        self._node_number = node_number

    @property
    def node_spec(self):
        """Gets the node_spec of this RestoreToNewInstanceRequest.  # noqa: E501


        :return: The node_spec of this RestoreToNewInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._node_spec

    @node_spec.setter
    def node_spec(self, node_spec):
        """Sets the node_spec of this RestoreToNewInstanceRequest.


        :param node_spec: The node_spec of this RestoreToNewInstanceRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and node_spec is None:
            raise ValueError("Invalid value for `node_spec`, must not be `None`")  # noqa: E501

        self._node_spec = node_spec

    @property
    def number(self):
        """Gets the number of this RestoreToNewInstanceRequest.  # noqa: E501


        :return: The number of this RestoreToNewInstanceRequest.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this RestoreToNewInstanceRequest.


        :param number: The number of this RestoreToNewInstanceRequest.  # noqa: E501
        :type: int
        """

        self._number = number

    @property
    def period(self):
        """Gets the period of this RestoreToNewInstanceRequest.  # noqa: E501


        :return: The period of this RestoreToNewInstanceRequest.  # noqa: E501
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this RestoreToNewInstanceRequest.


        :param period: The period of this RestoreToNewInstanceRequest.  # noqa: E501
        :type: int
        """

        self._period = period

    @property
    def period_unit(self):
        """Gets the period_unit of this RestoreToNewInstanceRequest.  # noqa: E501


        :return: The period_unit of this RestoreToNewInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._period_unit

    @period_unit.setter
    def period_unit(self, period_unit):
        """Sets the period_unit of this RestoreToNewInstanceRequest.


        :param period_unit: The period_unit of this RestoreToNewInstanceRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["Year", "Month"]  # noqa: E501
        if (self._configuration.client_side_validation and
                period_unit not in allowed_values):
            raise ValueError(
                "Invalid value for `period_unit` ({0}), must be one of {1}"  # noqa: E501
                .format(period_unit, allowed_values)
            )

        self._period_unit = period_unit

    @property
    def project_name(self):
        """Gets the project_name of this RestoreToNewInstanceRequest.  # noqa: E501


        :return: The project_name of this RestoreToNewInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this RestoreToNewInstanceRequest.


        :param project_name: The project_name of this RestoreToNewInstanceRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def restore_time(self):
        """Gets the restore_time of this RestoreToNewInstanceRequest.  # noqa: E501


        :return: The restore_time of this RestoreToNewInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._restore_time

    @restore_time.setter
    def restore_time(self, restore_time):
        """Sets the restore_time of this RestoreToNewInstanceRequest.


        :param restore_time: The restore_time of this RestoreToNewInstanceRequest.  # noqa: E501
        :type: str
        """

        self._restore_time = restore_time

    @property
    def shard_number(self):
        """Gets the shard_number of this RestoreToNewInstanceRequest.  # noqa: E501


        :return: The shard_number of this RestoreToNewInstanceRequest.  # noqa: E501
        :rtype: int
        """
        return self._shard_number

    @shard_number.setter
    def shard_number(self, shard_number):
        """Sets the shard_number of this RestoreToNewInstanceRequest.


        :param shard_number: The shard_number of this RestoreToNewInstanceRequest.  # noqa: E501
        :type: int
        """

        self._shard_number = shard_number

    @property
    def src_db_instance_id(self):
        """Gets the src_db_instance_id of this RestoreToNewInstanceRequest.  # noqa: E501


        :return: The src_db_instance_id of this RestoreToNewInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._src_db_instance_id

    @src_db_instance_id.setter
    def src_db_instance_id(self, src_db_instance_id):
        """Sets the src_db_instance_id of this RestoreToNewInstanceRequest.


        :param src_db_instance_id: The src_db_instance_id of this RestoreToNewInstanceRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and src_db_instance_id is None:
            raise ValueError("Invalid value for `src_db_instance_id`, must not be `None`")  # noqa: E501

        self._src_db_instance_id = src_db_instance_id

    @property
    def storage_space_gb(self):
        """Gets the storage_space_gb of this RestoreToNewInstanceRequest.  # noqa: E501


        :return: The storage_space_gb of this RestoreToNewInstanceRequest.  # noqa: E501
        :rtype: int
        """
        return self._storage_space_gb

    @storage_space_gb.setter
    def storage_space_gb(self, storage_space_gb):
        """Sets the storage_space_gb of this RestoreToNewInstanceRequest.


        :param storage_space_gb: The storage_space_gb of this RestoreToNewInstanceRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and storage_space_gb is None:
            raise ValueError("Invalid value for `storage_space_gb`, must not be `None`")  # noqa: E501

        self._storage_space_gb = storage_space_gb

    @property
    def subnet_id(self):
        """Gets the subnet_id of this RestoreToNewInstanceRequest.  # noqa: E501


        :return: The subnet_id of this RestoreToNewInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this RestoreToNewInstanceRequest.


        :param subnet_id: The subnet_id of this RestoreToNewInstanceRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and subnet_id is None:
            raise ValueError("Invalid value for `subnet_id`, must not be `None`")  # noqa: E501

        self._subnet_id = subnet_id

    @property
    def super_account_name(self):
        """Gets the super_account_name of this RestoreToNewInstanceRequest.  # noqa: E501


        :return: The super_account_name of this RestoreToNewInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._super_account_name

    @super_account_name.setter
    def super_account_name(self, super_account_name):
        """Sets the super_account_name of this RestoreToNewInstanceRequest.


        :param super_account_name: The super_account_name of this RestoreToNewInstanceRequest.  # noqa: E501
        :type: str
        """

        self._super_account_name = super_account_name

    @property
    def super_account_password(self):
        """Gets the super_account_password of this RestoreToNewInstanceRequest.  # noqa: E501


        :return: The super_account_password of this RestoreToNewInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._super_account_password

    @super_account_password.setter
    def super_account_password(self, super_account_password):
        """Sets the super_account_password of this RestoreToNewInstanceRequest.


        :param super_account_password: The super_account_password of this RestoreToNewInstanceRequest.  # noqa: E501
        :type: str
        """

        self._super_account_password = super_account_password

    @property
    def vpc_id(self):
        """Gets the vpc_id of this RestoreToNewInstanceRequest.  # noqa: E501


        :return: The vpc_id of this RestoreToNewInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this RestoreToNewInstanceRequest.


        :param vpc_id: The vpc_id of this RestoreToNewInstanceRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and vpc_id is None:
            raise ValueError("Invalid value for `vpc_id`, must not be `None`")  # noqa: E501

        self._vpc_id = vpc_id

    @property
    def zone_id(self):
        """Gets the zone_id of this RestoreToNewInstanceRequest.  # noqa: E501


        :return: The zone_id of this RestoreToNewInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this RestoreToNewInstanceRequest.


        :param zone_id: The zone_id of this RestoreToNewInstanceRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and zone_id is None:
            raise ValueError("Invalid value for `zone_id`, must not be `None`")  # noqa: E501

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
        if issubclass(RestoreToNewInstanceRequest, dict):
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
        if not isinstance(other, RestoreToNewInstanceRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RestoreToNewInstanceRequest):
            return True

        return self.to_dict() != other.to_dict()