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
        'db_minor_version': 'str',
        'deletion_protection': 'str',
        'instance_name': 'str',
        'node_number': 'int',
        'node_spec': 'str',
        'period': 'int',
        'period_unit': 'str',
        'port': 'int',
        'pre_paid_storage_in_gb': 'int',
        'project_name': 'str',
        'restore_time': 'str',
        'src_instance_id': 'str',
        'src_project_name': 'str',
        'storage_charge_type': 'str',
        'subnet_id': 'str',
        'tags': 'list[TagForRestoreToNewInstanceInput]',
        'template_id': 'str',
        'vpc_id': 'str',
        'zone_ids': 'str'
    }

    attribute_map = {
        'auto_renew': 'AutoRenew',
        'backup_id': 'BackupId',
        'charge_type': 'ChargeType',
        'db_minor_version': 'DBMinorVersion',
        'deletion_protection': 'DeletionProtection',
        'instance_name': 'InstanceName',
        'node_number': 'NodeNumber',
        'node_spec': 'NodeSpec',
        'period': 'Period',
        'period_unit': 'PeriodUnit',
        'port': 'Port',
        'pre_paid_storage_in_gb': 'PrePaidStorageInGB',
        'project_name': 'ProjectName',
        'restore_time': 'RestoreTime',
        'src_instance_id': 'SrcInstanceId',
        'src_project_name': 'SrcProjectName',
        'storage_charge_type': 'StorageChargeType',
        'subnet_id': 'SubnetId',
        'tags': 'Tags',
        'template_id': 'TemplateId',
        'vpc_id': 'VpcId',
        'zone_ids': 'ZoneIds'
    }

    def __init__(self, auto_renew=None, backup_id=None, charge_type=None, db_minor_version=None, deletion_protection=None, instance_name=None, node_number=None, node_spec=None, period=None, period_unit=None, port=None, pre_paid_storage_in_gb=None, project_name=None, restore_time=None, src_instance_id=None, src_project_name=None, storage_charge_type=None, subnet_id=None, tags=None, template_id=None, vpc_id=None, zone_ids=None, _configuration=None):  # noqa: E501
        """RestoreToNewInstanceRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._auto_renew = None
        self._backup_id = None
        self._charge_type = None
        self._db_minor_version = None
        self._deletion_protection = None
        self._instance_name = None
        self._node_number = None
        self._node_spec = None
        self._period = None
        self._period_unit = None
        self._port = None
        self._pre_paid_storage_in_gb = None
        self._project_name = None
        self._restore_time = None
        self._src_instance_id = None
        self._src_project_name = None
        self._storage_charge_type = None
        self._subnet_id = None
        self._tags = None
        self._template_id = None
        self._vpc_id = None
        self._zone_ids = None
        self.discriminator = None

        if auto_renew is not None:
            self.auto_renew = auto_renew
        if backup_id is not None:
            self.backup_id = backup_id
        self.charge_type = charge_type
        if db_minor_version is not None:
            self.db_minor_version = db_minor_version
        if deletion_protection is not None:
            self.deletion_protection = deletion_protection
        if instance_name is not None:
            self.instance_name = instance_name
        self.node_number = node_number
        self.node_spec = node_spec
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
        if restore_time is not None:
            self.restore_time = restore_time
        self.src_instance_id = src_instance_id
        if src_project_name is not None:
            self.src_project_name = src_project_name
        if storage_charge_type is not None:
            self.storage_charge_type = storage_charge_type
        self.subnet_id = subnet_id
        if tags is not None:
            self.tags = tags
        if template_id is not None:
            self.template_id = template_id
        self.vpc_id = vpc_id
        self.zone_ids = zone_ids

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
        if self._configuration.client_side_validation and charge_type is None:
            raise ValueError("Invalid value for `charge_type`, must not be `None`")  # noqa: E501

        self._charge_type = charge_type

    @property
    def db_minor_version(self):
        """Gets the db_minor_version of this RestoreToNewInstanceRequest.  # noqa: E501


        :return: The db_minor_version of this RestoreToNewInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._db_minor_version

    @db_minor_version.setter
    def db_minor_version(self, db_minor_version):
        """Sets the db_minor_version of this RestoreToNewInstanceRequest.


        :param db_minor_version: The db_minor_version of this RestoreToNewInstanceRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["2.0", "3.0", "3.1", "3.2"]  # noqa: E501
        if (self._configuration.client_side_validation and
                db_minor_version not in allowed_values):
            raise ValueError(
                "Invalid value for `db_minor_version` ({0}), must be one of {1}"  # noqa: E501
                .format(db_minor_version, allowed_values)
            )

        self._db_minor_version = db_minor_version

    @property
    def deletion_protection(self):
        """Gets the deletion_protection of this RestoreToNewInstanceRequest.  # noqa: E501


        :return: The deletion_protection of this RestoreToNewInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._deletion_protection

    @deletion_protection.setter
    def deletion_protection(self, deletion_protection):
        """Sets the deletion_protection of this RestoreToNewInstanceRequest.


        :param deletion_protection: The deletion_protection of this RestoreToNewInstanceRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["disabled", "enabled"]  # noqa: E501
        if (self._configuration.client_side_validation and
                deletion_protection not in allowed_values):
            raise ValueError(
                "Invalid value for `deletion_protection` ({0}), must be one of {1}"  # noqa: E501
                .format(deletion_protection, allowed_values)
            )

        self._deletion_protection = deletion_protection

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
        if self._configuration.client_side_validation and node_number is None:
            raise ValueError("Invalid value for `node_number`, must not be `None`")  # noqa: E501

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
        """Gets the port of this RestoreToNewInstanceRequest.  # noqa: E501


        :return: The port of this RestoreToNewInstanceRequest.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this RestoreToNewInstanceRequest.


        :param port: The port of this RestoreToNewInstanceRequest.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def pre_paid_storage_in_gb(self):
        """Gets the pre_paid_storage_in_gb of this RestoreToNewInstanceRequest.  # noqa: E501


        :return: The pre_paid_storage_in_gb of this RestoreToNewInstanceRequest.  # noqa: E501
        :rtype: int
        """
        return self._pre_paid_storage_in_gb

    @pre_paid_storage_in_gb.setter
    def pre_paid_storage_in_gb(self, pre_paid_storage_in_gb):
        """Sets the pre_paid_storage_in_gb of this RestoreToNewInstanceRequest.


        :param pre_paid_storage_in_gb: The pre_paid_storage_in_gb of this RestoreToNewInstanceRequest.  # noqa: E501
        :type: int
        """

        self._pre_paid_storage_in_gb = pre_paid_storage_in_gb

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
    def src_instance_id(self):
        """Gets the src_instance_id of this RestoreToNewInstanceRequest.  # noqa: E501


        :return: The src_instance_id of this RestoreToNewInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._src_instance_id

    @src_instance_id.setter
    def src_instance_id(self, src_instance_id):
        """Sets the src_instance_id of this RestoreToNewInstanceRequest.


        :param src_instance_id: The src_instance_id of this RestoreToNewInstanceRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and src_instance_id is None:
            raise ValueError("Invalid value for `src_instance_id`, must not be `None`")  # noqa: E501

        self._src_instance_id = src_instance_id

    @property
    def src_project_name(self):
        """Gets the src_project_name of this RestoreToNewInstanceRequest.  # noqa: E501


        :return: The src_project_name of this RestoreToNewInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._src_project_name

    @src_project_name.setter
    def src_project_name(self, src_project_name):
        """Sets the src_project_name of this RestoreToNewInstanceRequest.


        :param src_project_name: The src_project_name of this RestoreToNewInstanceRequest.  # noqa: E501
        :type: str
        """

        self._src_project_name = src_project_name

    @property
    def storage_charge_type(self):
        """Gets the storage_charge_type of this RestoreToNewInstanceRequest.  # noqa: E501


        :return: The storage_charge_type of this RestoreToNewInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._storage_charge_type

    @storage_charge_type.setter
    def storage_charge_type(self, storage_charge_type):
        """Sets the storage_charge_type of this RestoreToNewInstanceRequest.


        :param storage_charge_type: The storage_charge_type of this RestoreToNewInstanceRequest.  # noqa: E501
        :type: str
        """

        self._storage_charge_type = storage_charge_type

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
    def tags(self):
        """Gets the tags of this RestoreToNewInstanceRequest.  # noqa: E501


        :return: The tags of this RestoreToNewInstanceRequest.  # noqa: E501
        :rtype: list[TagForRestoreToNewInstanceInput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this RestoreToNewInstanceRequest.


        :param tags: The tags of this RestoreToNewInstanceRequest.  # noqa: E501
        :type: list[TagForRestoreToNewInstanceInput]
        """

        self._tags = tags

    @property
    def template_id(self):
        """Gets the template_id of this RestoreToNewInstanceRequest.  # noqa: E501


        :return: The template_id of this RestoreToNewInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this RestoreToNewInstanceRequest.


        :param template_id: The template_id of this RestoreToNewInstanceRequest.  # noqa: E501
        :type: str
        """

        self._template_id = template_id

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
    def zone_ids(self):
        """Gets the zone_ids of this RestoreToNewInstanceRequest.  # noqa: E501


        :return: The zone_ids of this RestoreToNewInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._zone_ids

    @zone_ids.setter
    def zone_ids(self, zone_ids):
        """Sets the zone_ids of this RestoreToNewInstanceRequest.


        :param zone_ids: The zone_ids of this RestoreToNewInstanceRequest.  # noqa: E501
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
