# coding: utf-8

"""
    vedbm

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class CreateDBInstanceRequest(object):
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
        'charge_type': 'str',
        'db_engine_version': 'str',
        'db_minor_version': 'str',
        'db_time_zone': 'str',
        'instance_name': 'str',
        'lower_case_table_names': 'str',
        'node_number': 'int',
        'node_spec': 'str',
        'number': 'int',
        'period': 'int',
        'period_unit': 'str',
        'port': 'int',
        'pre_paid_storage_in_gb': 'int',
        'project_name': 'str',
        'storage_charge_type': 'str',
        'subnet_id': 'str',
        'super_account_name': 'str',
        'super_account_password': 'str',
        'tags': 'list[TagForCreateDBInstanceInput]',
        'vpc_id': 'str',
        'zone_ids': 'str'
    }

    attribute_map = {
        'auto_renew': 'AutoRenew',
        'charge_type': 'ChargeType',
        'db_engine_version': 'DBEngineVersion',
        'db_minor_version': 'DBMinorVersion',
        'db_time_zone': 'DBTimeZone',
        'instance_name': 'InstanceName',
        'lower_case_table_names': 'LowerCaseTableNames',
        'node_number': 'NodeNumber',
        'node_spec': 'NodeSpec',
        'number': 'Number',
        'period': 'Period',
        'period_unit': 'PeriodUnit',
        'port': 'Port',
        'pre_paid_storage_in_gb': 'PrePaidStorageInGB',
        'project_name': 'ProjectName',
        'storage_charge_type': 'StorageChargeType',
        'subnet_id': 'SubnetId',
        'super_account_name': 'SuperAccountName',
        'super_account_password': 'SuperAccountPassword',
        'tags': 'Tags',
        'vpc_id': 'VpcId',
        'zone_ids': 'ZoneIds'
    }

    def __init__(self, auto_renew=None, charge_type=None, db_engine_version=None, db_minor_version=None, db_time_zone=None, instance_name=None, lower_case_table_names=None, node_number=None, node_spec=None, number=None, period=None, period_unit=None, port=None, pre_paid_storage_in_gb=None, project_name=None, storage_charge_type=None, subnet_id=None, super_account_name=None, super_account_password=None, tags=None, vpc_id=None, zone_ids=None, _configuration=None):  # noqa: E501
        """CreateDBInstanceRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._auto_renew = None
        self._charge_type = None
        self._db_engine_version = None
        self._db_minor_version = None
        self._db_time_zone = None
        self._instance_name = None
        self._lower_case_table_names = None
        self._node_number = None
        self._node_spec = None
        self._number = None
        self._period = None
        self._period_unit = None
        self._port = None
        self._pre_paid_storage_in_gb = None
        self._project_name = None
        self._storage_charge_type = None
        self._subnet_id = None
        self._super_account_name = None
        self._super_account_password = None
        self._tags = None
        self._vpc_id = None
        self._zone_ids = None
        self.discriminator = None

        if auto_renew is not None:
            self.auto_renew = auto_renew
        self.charge_type = charge_type
        self.db_engine_version = db_engine_version
        if db_minor_version is not None:
            self.db_minor_version = db_minor_version
        if db_time_zone is not None:
            self.db_time_zone = db_time_zone
        if instance_name is not None:
            self.instance_name = instance_name
        if lower_case_table_names is not None:
            self.lower_case_table_names = lower_case_table_names
        self.node_number = node_number
        self.node_spec = node_spec
        if number is not None:
            self.number = number
        if period is not None:
            self.period = period
        if period_unit is not None:
            self.period_unit = period_unit
        if port is not None:
            self.port = port
        if pre_paid_storage_in_gb is not None:
            self.pre_paid_storage_in_gb = pre_paid_storage_in_gb
        if project_name is not None:
            self.project_name = project_name
        if storage_charge_type is not None:
            self.storage_charge_type = storage_charge_type
        self.subnet_id = subnet_id
        if super_account_name is not None:
            self.super_account_name = super_account_name
        if super_account_password is not None:
            self.super_account_password = super_account_password
        if tags is not None:
            self.tags = tags
        self.vpc_id = vpc_id
        self.zone_ids = zone_ids

    @property
    def auto_renew(self):
        """Gets the auto_renew of this CreateDBInstanceRequest.  # noqa: E501


        :return: The auto_renew of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: bool
        """
        return self._auto_renew

    @auto_renew.setter
    def auto_renew(self, auto_renew):
        """Sets the auto_renew of this CreateDBInstanceRequest.


        :param auto_renew: The auto_renew of this CreateDBInstanceRequest.  # noqa: E501
        :type: bool
        """

        self._auto_renew = auto_renew

    @property
    def charge_type(self):
        """Gets the charge_type of this CreateDBInstanceRequest.  # noqa: E501


        :return: The charge_type of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._charge_type

    @charge_type.setter
    def charge_type(self, charge_type):
        """Sets the charge_type of this CreateDBInstanceRequest.


        :param charge_type: The charge_type of this CreateDBInstanceRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and charge_type is None:
            raise ValueError("Invalid value for `charge_type`, must not be `None`")  # noqa: E501
        allowed_values = ["PostPaid", "PrePaid"]  # noqa: E501
        if (self._configuration.client_side_validation and
                charge_type not in allowed_values):
            raise ValueError(
                "Invalid value for `charge_type` ({0}), must be one of {1}"  # noqa: E501
                .format(charge_type, allowed_values)
            )

        self._charge_type = charge_type

    @property
    def db_engine_version(self):
        """Gets the db_engine_version of this CreateDBInstanceRequest.  # noqa: E501


        :return: The db_engine_version of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._db_engine_version

    @db_engine_version.setter
    def db_engine_version(self, db_engine_version):
        """Sets the db_engine_version of this CreateDBInstanceRequest.


        :param db_engine_version: The db_engine_version of this CreateDBInstanceRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and db_engine_version is None:
            raise ValueError("Invalid value for `db_engine_version`, must not be `None`")  # noqa: E501
        allowed_values = ["MySQL_8_0"]  # noqa: E501
        if (self._configuration.client_side_validation and
                db_engine_version not in allowed_values):
            raise ValueError(
                "Invalid value for `db_engine_version` ({0}), must be one of {1}"  # noqa: E501
                .format(db_engine_version, allowed_values)
            )

        self._db_engine_version = db_engine_version

    @property
    def db_minor_version(self):
        """Gets the db_minor_version of this CreateDBInstanceRequest.  # noqa: E501


        :return: The db_minor_version of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._db_minor_version

    @db_minor_version.setter
    def db_minor_version(self, db_minor_version):
        """Sets the db_minor_version of this CreateDBInstanceRequest.


        :param db_minor_version: The db_minor_version of this CreateDBInstanceRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["3.0", "3.1", "3.2"]  # noqa: E501
        if (self._configuration.client_side_validation and
                db_minor_version not in allowed_values):
            raise ValueError(
                "Invalid value for `db_minor_version` ({0}), must be one of {1}"  # noqa: E501
                .format(db_minor_version, allowed_values)
            )

        self._db_minor_version = db_minor_version

    @property
    def db_time_zone(self):
        """Gets the db_time_zone of this CreateDBInstanceRequest.  # noqa: E501


        :return: The db_time_zone of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._db_time_zone

    @db_time_zone.setter
    def db_time_zone(self, db_time_zone):
        """Sets the db_time_zone of this CreateDBInstanceRequest.


        :param db_time_zone: The db_time_zone of this CreateDBInstanceRequest.  # noqa: E501
        :type: str
        """

        self._db_time_zone = db_time_zone

    @property
    def instance_name(self):
        """Gets the instance_name of this CreateDBInstanceRequest.  # noqa: E501


        :return: The instance_name of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this CreateDBInstanceRequest.


        :param instance_name: The instance_name of this CreateDBInstanceRequest.  # noqa: E501
        :type: str
        """

        self._instance_name = instance_name

    @property
    def lower_case_table_names(self):
        """Gets the lower_case_table_names of this CreateDBInstanceRequest.  # noqa: E501


        :return: The lower_case_table_names of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._lower_case_table_names

    @lower_case_table_names.setter
    def lower_case_table_names(self, lower_case_table_names):
        """Sets the lower_case_table_names of this CreateDBInstanceRequest.


        :param lower_case_table_names: The lower_case_table_names of this CreateDBInstanceRequest.  # noqa: E501
        :type: str
        """

        self._lower_case_table_names = lower_case_table_names

    @property
    def node_number(self):
        """Gets the node_number of this CreateDBInstanceRequest.  # noqa: E501


        :return: The node_number of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: int
        """
        return self._node_number

    @node_number.setter
    def node_number(self, node_number):
        """Sets the node_number of this CreateDBInstanceRequest.


        :param node_number: The node_number of this CreateDBInstanceRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and node_number is None:
            raise ValueError("Invalid value for `node_number`, must not be `None`")  # noqa: E501

        self._node_number = node_number

    @property
    def node_spec(self):
        """Gets the node_spec of this CreateDBInstanceRequest.  # noqa: E501


        :return: The node_spec of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._node_spec

    @node_spec.setter
    def node_spec(self, node_spec):
        """Sets the node_spec of this CreateDBInstanceRequest.


        :param node_spec: The node_spec of this CreateDBInstanceRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and node_spec is None:
            raise ValueError("Invalid value for `node_spec`, must not be `None`")  # noqa: E501
        allowed_values = ["vedb.mysql.x4.large", "vedb.mysql.x8.large", "vedb.mysql.x4.xlarge", "vedb.mysql.x8.xlarge", "vedb.mysql.x4.2xlarge", "vedb.mysql.x8.2xlarge", "vedb.mysql.x4.4xlarge", "vedb.mysql.x8.4xlarge", "vedb.mysql.x8.6xlarge", "vedb.mysql.x4.8xlarge", "vedb.mysql.x8.8xlarge", "vedb.mysql.g4.large", "vedb.mysql.g4.xlarge", "vedb.mysql.g4.2xlarge", "vedb.mysql.g8.2xlarge", "vedb.mysql.g4.4xlarge"]  # noqa: E501
        if (self._configuration.client_side_validation and
                node_spec not in allowed_values):
            raise ValueError(
                "Invalid value for `node_spec` ({0}), must be one of {1}"  # noqa: E501
                .format(node_spec, allowed_values)
            )

        self._node_spec = node_spec

    @property
    def number(self):
        """Gets the number of this CreateDBInstanceRequest.  # noqa: E501


        :return: The number of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this CreateDBInstanceRequest.


        :param number: The number of this CreateDBInstanceRequest.  # noqa: E501
        :type: int
        """

        self._number = number

    @property
    def period(self):
        """Gets the period of this CreateDBInstanceRequest.  # noqa: E501


        :return: The period of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this CreateDBInstanceRequest.


        :param period: The period of this CreateDBInstanceRequest.  # noqa: E501
        :type: int
        """

        self._period = period

    @property
    def period_unit(self):
        """Gets the period_unit of this CreateDBInstanceRequest.  # noqa: E501


        :return: The period_unit of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._period_unit

    @period_unit.setter
    def period_unit(self, period_unit):
        """Sets the period_unit of this CreateDBInstanceRequest.


        :param period_unit: The period_unit of this CreateDBInstanceRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["Month", "Year"]  # noqa: E501
        if (self._configuration.client_side_validation and
                period_unit not in allowed_values):
            raise ValueError(
                "Invalid value for `period_unit` ({0}), must be one of {1}"  # noqa: E501
                .format(period_unit, allowed_values)
            )

        self._period_unit = period_unit

    @property
    def port(self):
        """Gets the port of this CreateDBInstanceRequest.  # noqa: E501


        :return: The port of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this CreateDBInstanceRequest.


        :param port: The port of this CreateDBInstanceRequest.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def pre_paid_storage_in_gb(self):
        """Gets the pre_paid_storage_in_gb of this CreateDBInstanceRequest.  # noqa: E501


        :return: The pre_paid_storage_in_gb of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: int
        """
        return self._pre_paid_storage_in_gb

    @pre_paid_storage_in_gb.setter
    def pre_paid_storage_in_gb(self, pre_paid_storage_in_gb):
        """Sets the pre_paid_storage_in_gb of this CreateDBInstanceRequest.


        :param pre_paid_storage_in_gb: The pre_paid_storage_in_gb of this CreateDBInstanceRequest.  # noqa: E501
        :type: int
        """

        self._pre_paid_storage_in_gb = pre_paid_storage_in_gb

    @property
    def project_name(self):
        """Gets the project_name of this CreateDBInstanceRequest.  # noqa: E501


        :return: The project_name of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this CreateDBInstanceRequest.


        :param project_name: The project_name of this CreateDBInstanceRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def storage_charge_type(self):
        """Gets the storage_charge_type of this CreateDBInstanceRequest.  # noqa: E501


        :return: The storage_charge_type of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._storage_charge_type

    @storage_charge_type.setter
    def storage_charge_type(self, storage_charge_type):
        """Sets the storage_charge_type of this CreateDBInstanceRequest.


        :param storage_charge_type: The storage_charge_type of this CreateDBInstanceRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["PostPaid", "PrePaid"]  # noqa: E501
        if (self._configuration.client_side_validation and
                storage_charge_type not in allowed_values):
            raise ValueError(
                "Invalid value for `storage_charge_type` ({0}), must be one of {1}"  # noqa: E501
                .format(storage_charge_type, allowed_values)
            )

        self._storage_charge_type = storage_charge_type

    @property
    def subnet_id(self):
        """Gets the subnet_id of this CreateDBInstanceRequest.  # noqa: E501


        :return: The subnet_id of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this CreateDBInstanceRequest.


        :param subnet_id: The subnet_id of this CreateDBInstanceRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and subnet_id is None:
            raise ValueError("Invalid value for `subnet_id`, must not be `None`")  # noqa: E501

        self._subnet_id = subnet_id

    @property
    def super_account_name(self):
        """Gets the super_account_name of this CreateDBInstanceRequest.  # noqa: E501


        :return: The super_account_name of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._super_account_name

    @super_account_name.setter
    def super_account_name(self, super_account_name):
        """Sets the super_account_name of this CreateDBInstanceRequest.


        :param super_account_name: The super_account_name of this CreateDBInstanceRequest.  # noqa: E501
        :type: str
        """

        self._super_account_name = super_account_name

    @property
    def super_account_password(self):
        """Gets the super_account_password of this CreateDBInstanceRequest.  # noqa: E501


        :return: The super_account_password of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._super_account_password

    @super_account_password.setter
    def super_account_password(self, super_account_password):
        """Sets the super_account_password of this CreateDBInstanceRequest.


        :param super_account_password: The super_account_password of this CreateDBInstanceRequest.  # noqa: E501
        :type: str
        """

        self._super_account_password = super_account_password

    @property
    def tags(self):
        """Gets the tags of this CreateDBInstanceRequest.  # noqa: E501


        :return: The tags of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: list[TagForCreateDBInstanceInput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateDBInstanceRequest.


        :param tags: The tags of this CreateDBInstanceRequest.  # noqa: E501
        :type: list[TagForCreateDBInstanceInput]
        """

        self._tags = tags

    @property
    def vpc_id(self):
        """Gets the vpc_id of this CreateDBInstanceRequest.  # noqa: E501


        :return: The vpc_id of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this CreateDBInstanceRequest.


        :param vpc_id: The vpc_id of this CreateDBInstanceRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and vpc_id is None:
            raise ValueError("Invalid value for `vpc_id`, must not be `None`")  # noqa: E501

        self._vpc_id = vpc_id

    @property
    def zone_ids(self):
        """Gets the zone_ids of this CreateDBInstanceRequest.  # noqa: E501


        :return: The zone_ids of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._zone_ids

    @zone_ids.setter
    def zone_ids(self, zone_ids):
        """Sets the zone_ids of this CreateDBInstanceRequest.


        :param zone_ids: The zone_ids of this CreateDBInstanceRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and zone_ids is None:
            raise ValueError("Invalid value for `zone_ids`, must not be `None`")  # noqa: E501

        self._zone_ids = zone_ids

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
        if issubclass(CreateDBInstanceRequest, dict):
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
        if not isinstance(other, CreateDBInstanceRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateDBInstanceRequest):
            return True

        return self.to_dict() != other.to_dict()
