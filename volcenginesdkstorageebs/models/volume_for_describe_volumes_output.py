# coding: utf-8

"""
    storage_ebs

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class VolumeForDescribeVolumesOutput(object):
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
        'auto_snapshot_policy_id': 'str',
        'auto_snapshot_policy_name': 'str',
        'billing_type': 'int',
        'created_at': 'str',
        'delete_with_instance': 'bool',
        'description': 'str',
        'device_name': 'str',
        'error_detail': 'str',
        'expired_time': 'str',
        'image_id': 'str',
        'instance_id': 'str',
        'kind': 'str',
        'overdue_reclaim_time': 'str',
        'overdue_time': 'str',
        'pay_type': 'str',
        'project_name': 'str',
        'renew_type': 'int',
        'size': 'str',
        'snapshot_count': 'int',
        'source_snapshot_id': 'str',
        'status': 'str',
        'tags': 'list[TagForDescribeVolumesOutput]',
        'trade_status': 'int',
        'updated_at': 'str',
        'volume_id': 'str',
        'volume_name': 'str',
        'volume_type': 'str',
        'zone_id': 'str'
    }

    attribute_map = {
        'auto_snapshot_policy_id': 'AutoSnapshotPolicyId',
        'auto_snapshot_policy_name': 'AutoSnapshotPolicyName',
        'billing_type': 'BillingType',
        'created_at': 'CreatedAt',
        'delete_with_instance': 'DeleteWithInstance',
        'description': 'Description',
        'device_name': 'DeviceName',
        'error_detail': 'ErrorDetail',
        'expired_time': 'ExpiredTime',
        'image_id': 'ImageId',
        'instance_id': 'InstanceId',
        'kind': 'Kind',
        'overdue_reclaim_time': 'OverdueReclaimTime',
        'overdue_time': 'OverdueTime',
        'pay_type': 'PayType',
        'project_name': 'ProjectName',
        'renew_type': 'RenewType',
        'size': 'Size',
        'snapshot_count': 'SnapshotCount',
        'source_snapshot_id': 'SourceSnapshotId',
        'status': 'Status',
        'tags': 'Tags',
        'trade_status': 'TradeStatus',
        'updated_at': 'UpdatedAt',
        'volume_id': 'VolumeId',
        'volume_name': 'VolumeName',
        'volume_type': 'VolumeType',
        'zone_id': 'ZoneId'
    }

    def __init__(self, auto_snapshot_policy_id=None, auto_snapshot_policy_name=None, billing_type=None, created_at=None, delete_with_instance=None, description=None, device_name=None, error_detail=None, expired_time=None, image_id=None, instance_id=None, kind=None, overdue_reclaim_time=None, overdue_time=None, pay_type=None, project_name=None, renew_type=None, size=None, snapshot_count=None, source_snapshot_id=None, status=None, tags=None, trade_status=None, updated_at=None, volume_id=None, volume_name=None, volume_type=None, zone_id=None, _configuration=None):  # noqa: E501
        """VolumeForDescribeVolumesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._auto_snapshot_policy_id = None
        self._auto_snapshot_policy_name = None
        self._billing_type = None
        self._created_at = None
        self._delete_with_instance = None
        self._description = None
        self._device_name = None
        self._error_detail = None
        self._expired_time = None
        self._image_id = None
        self._instance_id = None
        self._kind = None
        self._overdue_reclaim_time = None
        self._overdue_time = None
        self._pay_type = None
        self._project_name = None
        self._renew_type = None
        self._size = None
        self._snapshot_count = None
        self._source_snapshot_id = None
        self._status = None
        self._tags = None
        self._trade_status = None
        self._updated_at = None
        self._volume_id = None
        self._volume_name = None
        self._volume_type = None
        self._zone_id = None
        self.discriminator = None

        if auto_snapshot_policy_id is not None:
            self.auto_snapshot_policy_id = auto_snapshot_policy_id
        if auto_snapshot_policy_name is not None:
            self.auto_snapshot_policy_name = auto_snapshot_policy_name
        if billing_type is not None:
            self.billing_type = billing_type
        if created_at is not None:
            self.created_at = created_at
        if delete_with_instance is not None:
            self.delete_with_instance = delete_with_instance
        if description is not None:
            self.description = description
        if device_name is not None:
            self.device_name = device_name
        if error_detail is not None:
            self.error_detail = error_detail
        if expired_time is not None:
            self.expired_time = expired_time
        if image_id is not None:
            self.image_id = image_id
        if instance_id is not None:
            self.instance_id = instance_id
        if kind is not None:
            self.kind = kind
        if overdue_reclaim_time is not None:
            self.overdue_reclaim_time = overdue_reclaim_time
        if overdue_time is not None:
            self.overdue_time = overdue_time
        if pay_type is not None:
            self.pay_type = pay_type
        if project_name is not None:
            self.project_name = project_name
        if renew_type is not None:
            self.renew_type = renew_type
        if size is not None:
            self.size = size
        if snapshot_count is not None:
            self.snapshot_count = snapshot_count
        if source_snapshot_id is not None:
            self.source_snapshot_id = source_snapshot_id
        if status is not None:
            self.status = status
        if tags is not None:
            self.tags = tags
        if trade_status is not None:
            self.trade_status = trade_status
        if updated_at is not None:
            self.updated_at = updated_at
        if volume_id is not None:
            self.volume_id = volume_id
        if volume_name is not None:
            self.volume_name = volume_name
        if volume_type is not None:
            self.volume_type = volume_type
        if zone_id is not None:
            self.zone_id = zone_id

    @property
    def auto_snapshot_policy_id(self):
        """Gets the auto_snapshot_policy_id of this VolumeForDescribeVolumesOutput.  # noqa: E501


        :return: The auto_snapshot_policy_id of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :rtype: str
        """
        return self._auto_snapshot_policy_id

    @auto_snapshot_policy_id.setter
    def auto_snapshot_policy_id(self, auto_snapshot_policy_id):
        """Sets the auto_snapshot_policy_id of this VolumeForDescribeVolumesOutput.


        :param auto_snapshot_policy_id: The auto_snapshot_policy_id of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :type: str
        """

        self._auto_snapshot_policy_id = auto_snapshot_policy_id

    @property
    def auto_snapshot_policy_name(self):
        """Gets the auto_snapshot_policy_name of this VolumeForDescribeVolumesOutput.  # noqa: E501


        :return: The auto_snapshot_policy_name of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :rtype: str
        """
        return self._auto_snapshot_policy_name

    @auto_snapshot_policy_name.setter
    def auto_snapshot_policy_name(self, auto_snapshot_policy_name):
        """Sets the auto_snapshot_policy_name of this VolumeForDescribeVolumesOutput.


        :param auto_snapshot_policy_name: The auto_snapshot_policy_name of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :type: str
        """

        self._auto_snapshot_policy_name = auto_snapshot_policy_name

    @property
    def billing_type(self):
        """Gets the billing_type of this VolumeForDescribeVolumesOutput.  # noqa: E501


        :return: The billing_type of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :rtype: int
        """
        return self._billing_type

    @billing_type.setter
    def billing_type(self, billing_type):
        """Sets the billing_type of this VolumeForDescribeVolumesOutput.


        :param billing_type: The billing_type of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :type: int
        """

        self._billing_type = billing_type

    @property
    def created_at(self):
        """Gets the created_at of this VolumeForDescribeVolumesOutput.  # noqa: E501


        :return: The created_at of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this VolumeForDescribeVolumesOutput.


        :param created_at: The created_at of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def delete_with_instance(self):
        """Gets the delete_with_instance of this VolumeForDescribeVolumesOutput.  # noqa: E501


        :return: The delete_with_instance of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :rtype: bool
        """
        return self._delete_with_instance

    @delete_with_instance.setter
    def delete_with_instance(self, delete_with_instance):
        """Sets the delete_with_instance of this VolumeForDescribeVolumesOutput.


        :param delete_with_instance: The delete_with_instance of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :type: bool
        """

        self._delete_with_instance = delete_with_instance

    @property
    def description(self):
        """Gets the description of this VolumeForDescribeVolumesOutput.  # noqa: E501


        :return: The description of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VolumeForDescribeVolumesOutput.


        :param description: The description of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def device_name(self):
        """Gets the device_name of this VolumeForDescribeVolumesOutput.  # noqa: E501


        :return: The device_name of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this VolumeForDescribeVolumesOutput.


        :param device_name: The device_name of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :type: str
        """

        self._device_name = device_name

    @property
    def error_detail(self):
        """Gets the error_detail of this VolumeForDescribeVolumesOutput.  # noqa: E501


        :return: The error_detail of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :rtype: str
        """
        return self._error_detail

    @error_detail.setter
    def error_detail(self, error_detail):
        """Sets the error_detail of this VolumeForDescribeVolumesOutput.


        :param error_detail: The error_detail of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :type: str
        """

        self._error_detail = error_detail

    @property
    def expired_time(self):
        """Gets the expired_time of this VolumeForDescribeVolumesOutput.  # noqa: E501


        :return: The expired_time of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :rtype: str
        """
        return self._expired_time

    @expired_time.setter
    def expired_time(self, expired_time):
        """Sets the expired_time of this VolumeForDescribeVolumesOutput.


        :param expired_time: The expired_time of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :type: str
        """

        self._expired_time = expired_time

    @property
    def image_id(self):
        """Gets the image_id of this VolumeForDescribeVolumesOutput.  # noqa: E501


        :return: The image_id of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this VolumeForDescribeVolumesOutput.


        :param image_id: The image_id of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :type: str
        """

        self._image_id = image_id

    @property
    def instance_id(self):
        """Gets the instance_id of this VolumeForDescribeVolumesOutput.  # noqa: E501


        :return: The instance_id of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this VolumeForDescribeVolumesOutput.


        :param instance_id: The instance_id of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def kind(self):
        """Gets the kind of this VolumeForDescribeVolumesOutput.  # noqa: E501


        :return: The kind of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this VolumeForDescribeVolumesOutput.


        :param kind: The kind of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def overdue_reclaim_time(self):
        """Gets the overdue_reclaim_time of this VolumeForDescribeVolumesOutput.  # noqa: E501


        :return: The overdue_reclaim_time of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :rtype: str
        """
        return self._overdue_reclaim_time

    @overdue_reclaim_time.setter
    def overdue_reclaim_time(self, overdue_reclaim_time):
        """Sets the overdue_reclaim_time of this VolumeForDescribeVolumesOutput.


        :param overdue_reclaim_time: The overdue_reclaim_time of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :type: str
        """

        self._overdue_reclaim_time = overdue_reclaim_time

    @property
    def overdue_time(self):
        """Gets the overdue_time of this VolumeForDescribeVolumesOutput.  # noqa: E501


        :return: The overdue_time of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :rtype: str
        """
        return self._overdue_time

    @overdue_time.setter
    def overdue_time(self, overdue_time):
        """Sets the overdue_time of this VolumeForDescribeVolumesOutput.


        :param overdue_time: The overdue_time of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :type: str
        """

        self._overdue_time = overdue_time

    @property
    def pay_type(self):
        """Gets the pay_type of this VolumeForDescribeVolumesOutput.  # noqa: E501


        :return: The pay_type of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :rtype: str
        """
        return self._pay_type

    @pay_type.setter
    def pay_type(self, pay_type):
        """Sets the pay_type of this VolumeForDescribeVolumesOutput.


        :param pay_type: The pay_type of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :type: str
        """

        self._pay_type = pay_type

    @property
    def project_name(self):
        """Gets the project_name of this VolumeForDescribeVolumesOutput.  # noqa: E501


        :return: The project_name of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this VolumeForDescribeVolumesOutput.


        :param project_name: The project_name of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def renew_type(self):
        """Gets the renew_type of this VolumeForDescribeVolumesOutput.  # noqa: E501


        :return: The renew_type of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :rtype: int
        """
        return self._renew_type

    @renew_type.setter
    def renew_type(self, renew_type):
        """Sets the renew_type of this VolumeForDescribeVolumesOutput.


        :param renew_type: The renew_type of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :type: int
        """

        self._renew_type = renew_type

    @property
    def size(self):
        """Gets the size of this VolumeForDescribeVolumesOutput.  # noqa: E501


        :return: The size of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this VolumeForDescribeVolumesOutput.


        :param size: The size of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :type: str
        """

        self._size = size

    @property
    def snapshot_count(self):
        """Gets the snapshot_count of this VolumeForDescribeVolumesOutput.  # noqa: E501


        :return: The snapshot_count of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :rtype: int
        """
        return self._snapshot_count

    @snapshot_count.setter
    def snapshot_count(self, snapshot_count):
        """Sets the snapshot_count of this VolumeForDescribeVolumesOutput.


        :param snapshot_count: The snapshot_count of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :type: int
        """

        self._snapshot_count = snapshot_count

    @property
    def source_snapshot_id(self):
        """Gets the source_snapshot_id of this VolumeForDescribeVolumesOutput.  # noqa: E501


        :return: The source_snapshot_id of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :rtype: str
        """
        return self._source_snapshot_id

    @source_snapshot_id.setter
    def source_snapshot_id(self, source_snapshot_id):
        """Sets the source_snapshot_id of this VolumeForDescribeVolumesOutput.


        :param source_snapshot_id: The source_snapshot_id of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :type: str
        """

        self._source_snapshot_id = source_snapshot_id

    @property
    def status(self):
        """Gets the status of this VolumeForDescribeVolumesOutput.  # noqa: E501


        :return: The status of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this VolumeForDescribeVolumesOutput.


        :param status: The status of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def tags(self):
        """Gets the tags of this VolumeForDescribeVolumesOutput.  # noqa: E501


        :return: The tags of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :rtype: list[TagForDescribeVolumesOutput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this VolumeForDescribeVolumesOutput.


        :param tags: The tags of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :type: list[TagForDescribeVolumesOutput]
        """

        self._tags = tags

    @property
    def trade_status(self):
        """Gets the trade_status of this VolumeForDescribeVolumesOutput.  # noqa: E501


        :return: The trade_status of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :rtype: int
        """
        return self._trade_status

    @trade_status.setter
    def trade_status(self, trade_status):
        """Sets the trade_status of this VolumeForDescribeVolumesOutput.


        :param trade_status: The trade_status of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :type: int
        """

        self._trade_status = trade_status

    @property
    def updated_at(self):
        """Gets the updated_at of this VolumeForDescribeVolumesOutput.  # noqa: E501


        :return: The updated_at of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this VolumeForDescribeVolumesOutput.


        :param updated_at: The updated_at of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

    @property
    def volume_id(self):
        """Gets the volume_id of this VolumeForDescribeVolumesOutput.  # noqa: E501


        :return: The volume_id of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """Sets the volume_id of this VolumeForDescribeVolumesOutput.


        :param volume_id: The volume_id of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :type: str
        """

        self._volume_id = volume_id

    @property
    def volume_name(self):
        """Gets the volume_name of this VolumeForDescribeVolumesOutput.  # noqa: E501


        :return: The volume_name of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :rtype: str
        """
        return self._volume_name

    @volume_name.setter
    def volume_name(self, volume_name):
        """Sets the volume_name of this VolumeForDescribeVolumesOutput.


        :param volume_name: The volume_name of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :type: str
        """

        self._volume_name = volume_name

    @property
    def volume_type(self):
        """Gets the volume_type of this VolumeForDescribeVolumesOutput.  # noqa: E501


        :return: The volume_type of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        """Sets the volume_type of this VolumeForDescribeVolumesOutput.


        :param volume_type: The volume_type of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :type: str
        """

        self._volume_type = volume_type

    @property
    def zone_id(self):
        """Gets the zone_id of this VolumeForDescribeVolumesOutput.  # noqa: E501


        :return: The zone_id of this VolumeForDescribeVolumesOutput.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this VolumeForDescribeVolumesOutput.


        :param zone_id: The zone_id of this VolumeForDescribeVolumesOutput.  # noqa: E501
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
        if issubclass(VolumeForDescribeVolumesOutput, dict):
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
        if not isinstance(other, VolumeForDescribeVolumesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VolumeForDescribeVolumesOutput):
            return True

        return self.to_dict() != other.to_dict()
