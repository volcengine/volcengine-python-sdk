# coding: utf-8

"""
    rds_mysql

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class RecoveryDBInstanceRequest(object):
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
        'instance_id': 'str',
        'instance_name': 'str',
        'instance_spec_name': 'str',
        'prepaid_period': 'str',
        'recovery_type': 'str',
        'restore_time': 'str',
        'storage_space_gb': 'int',
        'storage_type': 'str',
        'used_time': 'int',
        'vpc_id': 'str'
    }

    attribute_map = {
        'auto_renew': 'AutoRenew',
        'backup_id': 'BackupId',
        'charge_type': 'ChargeType',
        'instance_id': 'InstanceId',
        'instance_name': 'InstanceName',
        'instance_spec_name': 'InstanceSpecName',
        'prepaid_period': 'PrepaidPeriod',
        'recovery_type': 'RecoveryType',
        'restore_time': 'RestoreTime',
        'storage_space_gb': 'StorageSpaceGB',
        'storage_type': 'StorageType',
        'used_time': 'UsedTime',
        'vpc_id': 'VpcID'
    }

    def __init__(self, auto_renew=None, backup_id=None, charge_type=None, instance_id=None, instance_name=None, instance_spec_name=None, prepaid_period=None, recovery_type=None, restore_time=None, storage_space_gb=None, storage_type=None, used_time=None, vpc_id=None, _configuration=None):  # noqa: E501
        """RecoveryDBInstanceRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._auto_renew = None
        self._backup_id = None
        self._charge_type = None
        self._instance_id = None
        self._instance_name = None
        self._instance_spec_name = None
        self._prepaid_period = None
        self._recovery_type = None
        self._restore_time = None
        self._storage_space_gb = None
        self._storage_type = None
        self._used_time = None
        self._vpc_id = None
        self.discriminator = None

        if auto_renew is not None:
            self.auto_renew = auto_renew
        if backup_id is not None:
            self.backup_id = backup_id
        if charge_type is not None:
            self.charge_type = charge_type
        self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if instance_spec_name is not None:
            self.instance_spec_name = instance_spec_name
        if prepaid_period is not None:
            self.prepaid_period = prepaid_period
        if recovery_type is not None:
            self.recovery_type = recovery_type
        if restore_time is not None:
            self.restore_time = restore_time
        if storage_space_gb is not None:
            self.storage_space_gb = storage_space_gb
        if storage_type is not None:
            self.storage_type = storage_type
        if used_time is not None:
            self.used_time = used_time
        if vpc_id is not None:
            self.vpc_id = vpc_id

    @property
    def auto_renew(self):
        """Gets the auto_renew of this RecoveryDBInstanceRequest.  # noqa: E501


        :return: The auto_renew of this RecoveryDBInstanceRequest.  # noqa: E501
        :rtype: bool
        """
        return self._auto_renew

    @auto_renew.setter
    def auto_renew(self, auto_renew):
        """Sets the auto_renew of this RecoveryDBInstanceRequest.


        :param auto_renew: The auto_renew of this RecoveryDBInstanceRequest.  # noqa: E501
        :type: bool
        """

        self._auto_renew = auto_renew

    @property
    def backup_id(self):
        """Gets the backup_id of this RecoveryDBInstanceRequest.  # noqa: E501


        :return: The backup_id of this RecoveryDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        """Sets the backup_id of this RecoveryDBInstanceRequest.


        :param backup_id: The backup_id of this RecoveryDBInstanceRequest.  # noqa: E501
        :type: str
        """

        self._backup_id = backup_id

    @property
    def charge_type(self):
        """Gets the charge_type of this RecoveryDBInstanceRequest.  # noqa: E501


        :return: The charge_type of this RecoveryDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._charge_type

    @charge_type.setter
    def charge_type(self, charge_type):
        """Sets the charge_type of this RecoveryDBInstanceRequest.


        :param charge_type: The charge_type of this RecoveryDBInstanceRequest.  # noqa: E501
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
    def instance_id(self):
        """Gets the instance_id of this RecoveryDBInstanceRequest.  # noqa: E501


        :return: The instance_id of this RecoveryDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this RecoveryDBInstanceRequest.


        :param instance_id: The instance_id of this RecoveryDBInstanceRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and instance_id is None:
            raise ValueError("Invalid value for `instance_id`, must not be `None`")  # noqa: E501

        self._instance_id = instance_id

    @property
    def instance_name(self):
        """Gets the instance_name of this RecoveryDBInstanceRequest.  # noqa: E501


        :return: The instance_name of this RecoveryDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this RecoveryDBInstanceRequest.


        :param instance_name: The instance_name of this RecoveryDBInstanceRequest.  # noqa: E501
        :type: str
        """

        self._instance_name = instance_name

    @property
    def instance_spec_name(self):
        """Gets the instance_spec_name of this RecoveryDBInstanceRequest.  # noqa: E501


        :return: The instance_spec_name of this RecoveryDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_spec_name

    @instance_spec_name.setter
    def instance_spec_name(self, instance_spec_name):
        """Sets the instance_spec_name of this RecoveryDBInstanceRequest.


        :param instance_spec_name: The instance_spec_name of this RecoveryDBInstanceRequest.  # noqa: E501
        :type: str
        """

        self._instance_spec_name = instance_spec_name

    @property
    def prepaid_period(self):
        """Gets the prepaid_period of this RecoveryDBInstanceRequest.  # noqa: E501


        :return: The prepaid_period of this RecoveryDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._prepaid_period

    @prepaid_period.setter
    def prepaid_period(self, prepaid_period):
        """Sets the prepaid_period of this RecoveryDBInstanceRequest.


        :param prepaid_period: The prepaid_period of this RecoveryDBInstanceRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["Month", "Year"]  # noqa: E501
        if (self._configuration.client_side_validation and
                prepaid_period not in allowed_values):
            raise ValueError(
                "Invalid value for `prepaid_period` ({0}), must be one of {1}"  # noqa: E501
                .format(prepaid_period, allowed_values)
            )

        self._prepaid_period = prepaid_period

    @property
    def recovery_type(self):
        """Gets the recovery_type of this RecoveryDBInstanceRequest.  # noqa: E501


        :return: The recovery_type of this RecoveryDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._recovery_type

    @recovery_type.setter
    def recovery_type(self, recovery_type):
        """Sets the recovery_type of this RecoveryDBInstanceRequest.


        :param recovery_type: The recovery_type of this RecoveryDBInstanceRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["Instance"]  # noqa: E501
        if (self._configuration.client_side_validation and
                recovery_type not in allowed_values):
            raise ValueError(
                "Invalid value for `recovery_type` ({0}), must be one of {1}"  # noqa: E501
                .format(recovery_type, allowed_values)
            )

        self._recovery_type = recovery_type

    @property
    def restore_time(self):
        """Gets the restore_time of this RecoveryDBInstanceRequest.  # noqa: E501


        :return: The restore_time of this RecoveryDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._restore_time

    @restore_time.setter
    def restore_time(self, restore_time):
        """Sets the restore_time of this RecoveryDBInstanceRequest.


        :param restore_time: The restore_time of this RecoveryDBInstanceRequest.  # noqa: E501
        :type: str
        """

        self._restore_time = restore_time

    @property
    def storage_space_gb(self):
        """Gets the storage_space_gb of this RecoveryDBInstanceRequest.  # noqa: E501


        :return: The storage_space_gb of this RecoveryDBInstanceRequest.  # noqa: E501
        :rtype: int
        """
        return self._storage_space_gb

    @storage_space_gb.setter
    def storage_space_gb(self, storage_space_gb):
        """Sets the storage_space_gb of this RecoveryDBInstanceRequest.


        :param storage_space_gb: The storage_space_gb of this RecoveryDBInstanceRequest.  # noqa: E501
        :type: int
        """

        self._storage_space_gb = storage_space_gb

    @property
    def storage_type(self):
        """Gets the storage_type of this RecoveryDBInstanceRequest.  # noqa: E501


        :return: The storage_type of this RecoveryDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._storage_type

    @storage_type.setter
    def storage_type(self, storage_type):
        """Sets the storage_type of this RecoveryDBInstanceRequest.


        :param storage_type: The storage_type of this RecoveryDBInstanceRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["CloudStorage", "ESSDPL1", "ESSDPL2", "LocalSSD"]  # noqa: E501
        if (self._configuration.client_side_validation and
                storage_type not in allowed_values):
            raise ValueError(
                "Invalid value for `storage_type` ({0}), must be one of {1}"  # noqa: E501
                .format(storage_type, allowed_values)
            )

        self._storage_type = storage_type

    @property
    def used_time(self):
        """Gets the used_time of this RecoveryDBInstanceRequest.  # noqa: E501


        :return: The used_time of this RecoveryDBInstanceRequest.  # noqa: E501
        :rtype: int
        """
        return self._used_time

    @used_time.setter
    def used_time(self, used_time):
        """Sets the used_time of this RecoveryDBInstanceRequest.


        :param used_time: The used_time of this RecoveryDBInstanceRequest.  # noqa: E501
        :type: int
        """

        self._used_time = used_time

    @property
    def vpc_id(self):
        """Gets the vpc_id of this RecoveryDBInstanceRequest.  # noqa: E501


        :return: The vpc_id of this RecoveryDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this RecoveryDBInstanceRequest.


        :param vpc_id: The vpc_id of this RecoveryDBInstanceRequest.  # noqa: E501
        :type: str
        """

        self._vpc_id = vpc_id

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
        if issubclass(RecoveryDBInstanceRequest, dict):
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
        if not isinstance(other, RecoveryDBInstanceRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RecoveryDBInstanceRequest):
            return True

        return self.to_dict() != other.to_dict()
