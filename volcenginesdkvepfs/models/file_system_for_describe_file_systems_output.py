# coding: utf-8

"""
    vepfs

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class FileSystemForDescribeFileSystemsOutput(object):
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
        'account_id': 'str',
        'attach_status': 'str',
        'auto_renew': 'bool',
        'bandwidth': 'int',
        'capacity_info': 'CapacityInfoForDescribeFileSystemsOutput',
        'charge_status': 'str',
        'charge_type': 'str',
        'create_time': 'str',
        'description': 'str',
        'ece_code': 'str',
        'expire_time': 'str',
        'file_system_id': 'str',
        'file_system_name': 'str',
        'file_system_type': 'str',
        'free_time': 'str',
        'last_modify_time': 'str',
        'month': 'int',
        'mount_points': 'list[MountPointForDescribeFileSystemsOutput]',
        'project': 'str',
        'protocol_type': 'str',
        'region_id': 'str',
        'replicas_num': 'int',
        'security_group_id': 'str',
        'status': 'str',
        'stop_service_time': 'str',
        'storage': 'StorageForDescribeFileSystemsOutput',
        'store_type': 'str',
        'subnet_id': 'str',
        'subnet_name': 'str',
        'tags': 'list[TagForDescribeFileSystemsOutput]',
        'trade_info': 'TradeInfoForDescribeFileSystemsOutput',
        'upgrade_end_time': 'str',
        'upgrade_error': 'str',
        'upgrade_start_time': 'str',
        'user_id': 'str',
        'version': 'str',
        'vpc_id': 'str',
        'vpc_name': 'str',
        'zone_id': 'str',
        'zone_name': 'str'
    }

    attribute_map = {
        'account_id': 'AccountId',
        'attach_status': 'AttachStatus',
        'auto_renew': 'AutoRenew',
        'bandwidth': 'Bandwidth',
        'capacity_info': 'CapacityInfo',
        'charge_status': 'ChargeStatus',
        'charge_type': 'ChargeType',
        'create_time': 'CreateTime',
        'description': 'Description',
        'ece_code': 'EceCode',
        'expire_time': 'ExpireTime',
        'file_system_id': 'FileSystemId',
        'file_system_name': 'FileSystemName',
        'file_system_type': 'FileSystemType',
        'free_time': 'FreeTime',
        'last_modify_time': 'LastModifyTime',
        'month': 'Month',
        'mount_points': 'MountPoints',
        'project': 'Project',
        'protocol_type': 'ProtocolType',
        'region_id': 'RegionId',
        'replicas_num': 'ReplicasNum',
        'security_group_id': 'SecurityGroupId',
        'status': 'Status',
        'stop_service_time': 'StopServiceTime',
        'storage': 'Storage',
        'store_type': 'StoreType',
        'subnet_id': 'SubnetId',
        'subnet_name': 'SubnetName',
        'tags': 'Tags',
        'trade_info': 'TradeInfo',
        'upgrade_end_time': 'UpgradeEndTime',
        'upgrade_error': 'UpgradeError',
        'upgrade_start_time': 'UpgradeStartTime',
        'user_id': 'UserId',
        'version': 'Version',
        'vpc_id': 'VpcId',
        'vpc_name': 'VpcName',
        'zone_id': 'ZoneId',
        'zone_name': 'ZoneName'
    }

    def __init__(self, account_id=None, attach_status=None, auto_renew=None, bandwidth=None, capacity_info=None, charge_status=None, charge_type=None, create_time=None, description=None, ece_code=None, expire_time=None, file_system_id=None, file_system_name=None, file_system_type=None, free_time=None, last_modify_time=None, month=None, mount_points=None, project=None, protocol_type=None, region_id=None, replicas_num=None, security_group_id=None, status=None, stop_service_time=None, storage=None, store_type=None, subnet_id=None, subnet_name=None, tags=None, trade_info=None, upgrade_end_time=None, upgrade_error=None, upgrade_start_time=None, user_id=None, version=None, vpc_id=None, vpc_name=None, zone_id=None, zone_name=None, _configuration=None):  # noqa: E501
        """FileSystemForDescribeFileSystemsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_id = None
        self._attach_status = None
        self._auto_renew = None
        self._bandwidth = None
        self._capacity_info = None
        self._charge_status = None
        self._charge_type = None
        self._create_time = None
        self._description = None
        self._ece_code = None
        self._expire_time = None
        self._file_system_id = None
        self._file_system_name = None
        self._file_system_type = None
        self._free_time = None
        self._last_modify_time = None
        self._month = None
        self._mount_points = None
        self._project = None
        self._protocol_type = None
        self._region_id = None
        self._replicas_num = None
        self._security_group_id = None
        self._status = None
        self._stop_service_time = None
        self._storage = None
        self._store_type = None
        self._subnet_id = None
        self._subnet_name = None
        self._tags = None
        self._trade_info = None
        self._upgrade_end_time = None
        self._upgrade_error = None
        self._upgrade_start_time = None
        self._user_id = None
        self._version = None
        self._vpc_id = None
        self._vpc_name = None
        self._zone_id = None
        self._zone_name = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if attach_status is not None:
            self.attach_status = attach_status
        if auto_renew is not None:
            self.auto_renew = auto_renew
        if bandwidth is not None:
            self.bandwidth = bandwidth
        if capacity_info is not None:
            self.capacity_info = capacity_info
        if charge_status is not None:
            self.charge_status = charge_status
        if charge_type is not None:
            self.charge_type = charge_type
        if create_time is not None:
            self.create_time = create_time
        if description is not None:
            self.description = description
        if ece_code is not None:
            self.ece_code = ece_code
        if expire_time is not None:
            self.expire_time = expire_time
        if file_system_id is not None:
            self.file_system_id = file_system_id
        if file_system_name is not None:
            self.file_system_name = file_system_name
        if file_system_type is not None:
            self.file_system_type = file_system_type
        if free_time is not None:
            self.free_time = free_time
        if last_modify_time is not None:
            self.last_modify_time = last_modify_time
        if month is not None:
            self.month = month
        if mount_points is not None:
            self.mount_points = mount_points
        if project is not None:
            self.project = project
        if protocol_type is not None:
            self.protocol_type = protocol_type
        if region_id is not None:
            self.region_id = region_id
        if replicas_num is not None:
            self.replicas_num = replicas_num
        if security_group_id is not None:
            self.security_group_id = security_group_id
        if status is not None:
            self.status = status
        if stop_service_time is not None:
            self.stop_service_time = stop_service_time
        if storage is not None:
            self.storage = storage
        if store_type is not None:
            self.store_type = store_type
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if subnet_name is not None:
            self.subnet_name = subnet_name
        if tags is not None:
            self.tags = tags
        if trade_info is not None:
            self.trade_info = trade_info
        if upgrade_end_time is not None:
            self.upgrade_end_time = upgrade_end_time
        if upgrade_error is not None:
            self.upgrade_error = upgrade_error
        if upgrade_start_time is not None:
            self.upgrade_start_time = upgrade_start_time
        if user_id is not None:
            self.user_id = user_id
        if version is not None:
            self.version = version
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if vpc_name is not None:
            self.vpc_name = vpc_name
        if zone_id is not None:
            self.zone_id = zone_id
        if zone_name is not None:
            self.zone_name = zone_name

    @property
    def account_id(self):
        """Gets the account_id of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The account_id of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this FileSystemForDescribeFileSystemsOutput.


        :param account_id: The account_id of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def attach_status(self):
        """Gets the attach_status of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The attach_status of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: str
        """
        return self._attach_status

    @attach_status.setter
    def attach_status(self, attach_status):
        """Sets the attach_status of this FileSystemForDescribeFileSystemsOutput.


        :param attach_status: The attach_status of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: str
        """

        self._attach_status = attach_status

    @property
    def auto_renew(self):
        """Gets the auto_renew of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The auto_renew of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: bool
        """
        return self._auto_renew

    @auto_renew.setter
    def auto_renew(self, auto_renew):
        """Sets the auto_renew of this FileSystemForDescribeFileSystemsOutput.


        :param auto_renew: The auto_renew of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: bool
        """

        self._auto_renew = auto_renew

    @property
    def bandwidth(self):
        """Gets the bandwidth of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The bandwidth of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: int
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this FileSystemForDescribeFileSystemsOutput.


        :param bandwidth: The bandwidth of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: int
        """

        self._bandwidth = bandwidth

    @property
    def capacity_info(self):
        """Gets the capacity_info of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The capacity_info of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: CapacityInfoForDescribeFileSystemsOutput
        """
        return self._capacity_info

    @capacity_info.setter
    def capacity_info(self, capacity_info):
        """Sets the capacity_info of this FileSystemForDescribeFileSystemsOutput.


        :param capacity_info: The capacity_info of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: CapacityInfoForDescribeFileSystemsOutput
        """

        self._capacity_info = capacity_info

    @property
    def charge_status(self):
        """Gets the charge_status of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The charge_status of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: str
        """
        return self._charge_status

    @charge_status.setter
    def charge_status(self, charge_status):
        """Sets the charge_status of this FileSystemForDescribeFileSystemsOutput.


        :param charge_status: The charge_status of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: str
        """

        self._charge_status = charge_status

    @property
    def charge_type(self):
        """Gets the charge_type of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The charge_type of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: str
        """
        return self._charge_type

    @charge_type.setter
    def charge_type(self, charge_type):
        """Sets the charge_type of this FileSystemForDescribeFileSystemsOutput.


        :param charge_type: The charge_type of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: str
        """

        self._charge_type = charge_type

    @property
    def create_time(self):
        """Gets the create_time of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The create_time of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this FileSystemForDescribeFileSystemsOutput.


        :param create_time: The create_time of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: str
        """

        self._create_time = create_time

    @property
    def description(self):
        """Gets the description of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The description of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FileSystemForDescribeFileSystemsOutput.


        :param description: The description of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def ece_code(self):
        """Gets the ece_code of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The ece_code of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: str
        """
        return self._ece_code

    @ece_code.setter
    def ece_code(self, ece_code):
        """Sets the ece_code of this FileSystemForDescribeFileSystemsOutput.


        :param ece_code: The ece_code of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: str
        """

        self._ece_code = ece_code

    @property
    def expire_time(self):
        """Gets the expire_time of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The expire_time of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this FileSystemForDescribeFileSystemsOutput.


        :param expire_time: The expire_time of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: str
        """

        self._expire_time = expire_time

    @property
    def file_system_id(self):
        """Gets the file_system_id of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The file_system_id of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: str
        """
        return self._file_system_id

    @file_system_id.setter
    def file_system_id(self, file_system_id):
        """Sets the file_system_id of this FileSystemForDescribeFileSystemsOutput.


        :param file_system_id: The file_system_id of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: str
        """

        self._file_system_id = file_system_id

    @property
    def file_system_name(self):
        """Gets the file_system_name of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The file_system_name of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: str
        """
        return self._file_system_name

    @file_system_name.setter
    def file_system_name(self, file_system_name):
        """Sets the file_system_name of this FileSystemForDescribeFileSystemsOutput.


        :param file_system_name: The file_system_name of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: str
        """

        self._file_system_name = file_system_name

    @property
    def file_system_type(self):
        """Gets the file_system_type of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The file_system_type of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: str
        """
        return self._file_system_type

    @file_system_type.setter
    def file_system_type(self, file_system_type):
        """Sets the file_system_type of this FileSystemForDescribeFileSystemsOutput.


        :param file_system_type: The file_system_type of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: str
        """

        self._file_system_type = file_system_type

    @property
    def free_time(self):
        """Gets the free_time of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The free_time of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: str
        """
        return self._free_time

    @free_time.setter
    def free_time(self, free_time):
        """Sets the free_time of this FileSystemForDescribeFileSystemsOutput.


        :param free_time: The free_time of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: str
        """

        self._free_time = free_time

    @property
    def last_modify_time(self):
        """Gets the last_modify_time of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The last_modify_time of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: str
        """
        return self._last_modify_time

    @last_modify_time.setter
    def last_modify_time(self, last_modify_time):
        """Sets the last_modify_time of this FileSystemForDescribeFileSystemsOutput.


        :param last_modify_time: The last_modify_time of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: str
        """

        self._last_modify_time = last_modify_time

    @property
    def month(self):
        """Gets the month of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The month of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: int
        """
        return self._month

    @month.setter
    def month(self, month):
        """Sets the month of this FileSystemForDescribeFileSystemsOutput.


        :param month: The month of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: int
        """

        self._month = month

    @property
    def mount_points(self):
        """Gets the mount_points of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The mount_points of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: list[MountPointForDescribeFileSystemsOutput]
        """
        return self._mount_points

    @mount_points.setter
    def mount_points(self, mount_points):
        """Sets the mount_points of this FileSystemForDescribeFileSystemsOutput.


        :param mount_points: The mount_points of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: list[MountPointForDescribeFileSystemsOutput]
        """

        self._mount_points = mount_points

    @property
    def project(self):
        """Gets the project of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The project of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this FileSystemForDescribeFileSystemsOutput.


        :param project: The project of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: str
        """

        self._project = project

    @property
    def protocol_type(self):
        """Gets the protocol_type of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The protocol_type of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: str
        """
        return self._protocol_type

    @protocol_type.setter
    def protocol_type(self, protocol_type):
        """Sets the protocol_type of this FileSystemForDescribeFileSystemsOutput.


        :param protocol_type: The protocol_type of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: str
        """

        self._protocol_type = protocol_type

    @property
    def region_id(self):
        """Gets the region_id of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The region_id of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this FileSystemForDescribeFileSystemsOutput.


        :param region_id: The region_id of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: str
        """

        self._region_id = region_id

    @property
    def replicas_num(self):
        """Gets the replicas_num of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The replicas_num of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: int
        """
        return self._replicas_num

    @replicas_num.setter
    def replicas_num(self, replicas_num):
        """Sets the replicas_num of this FileSystemForDescribeFileSystemsOutput.


        :param replicas_num: The replicas_num of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: int
        """

        self._replicas_num = replicas_num

    @property
    def security_group_id(self):
        """Gets the security_group_id of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The security_group_id of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this FileSystemForDescribeFileSystemsOutput.


        :param security_group_id: The security_group_id of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: str
        """

        self._security_group_id = security_group_id

    @property
    def status(self):
        """Gets the status of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The status of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this FileSystemForDescribeFileSystemsOutput.


        :param status: The status of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def stop_service_time(self):
        """Gets the stop_service_time of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The stop_service_time of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: str
        """
        return self._stop_service_time

    @stop_service_time.setter
    def stop_service_time(self, stop_service_time):
        """Sets the stop_service_time of this FileSystemForDescribeFileSystemsOutput.


        :param stop_service_time: The stop_service_time of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: str
        """

        self._stop_service_time = stop_service_time

    @property
    def storage(self):
        """Gets the storage of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The storage of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: StorageForDescribeFileSystemsOutput
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        """Sets the storage of this FileSystemForDescribeFileSystemsOutput.


        :param storage: The storage of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: StorageForDescribeFileSystemsOutput
        """

        self._storage = storage

    @property
    def store_type(self):
        """Gets the store_type of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The store_type of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: str
        """
        return self._store_type

    @store_type.setter
    def store_type(self, store_type):
        """Sets the store_type of this FileSystemForDescribeFileSystemsOutput.


        :param store_type: The store_type of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: str
        """

        self._store_type = store_type

    @property
    def subnet_id(self):
        """Gets the subnet_id of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The subnet_id of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this FileSystemForDescribeFileSystemsOutput.


        :param subnet_id: The subnet_id of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: str
        """

        self._subnet_id = subnet_id

    @property
    def subnet_name(self):
        """Gets the subnet_name of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The subnet_name of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: str
        """
        return self._subnet_name

    @subnet_name.setter
    def subnet_name(self, subnet_name):
        """Sets the subnet_name of this FileSystemForDescribeFileSystemsOutput.


        :param subnet_name: The subnet_name of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: str
        """

        self._subnet_name = subnet_name

    @property
    def tags(self):
        """Gets the tags of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The tags of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: list[TagForDescribeFileSystemsOutput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this FileSystemForDescribeFileSystemsOutput.


        :param tags: The tags of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: list[TagForDescribeFileSystemsOutput]
        """

        self._tags = tags

    @property
    def trade_info(self):
        """Gets the trade_info of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The trade_info of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: TradeInfoForDescribeFileSystemsOutput
        """
        return self._trade_info

    @trade_info.setter
    def trade_info(self, trade_info):
        """Sets the trade_info of this FileSystemForDescribeFileSystemsOutput.


        :param trade_info: The trade_info of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: TradeInfoForDescribeFileSystemsOutput
        """

        self._trade_info = trade_info

    @property
    def upgrade_end_time(self):
        """Gets the upgrade_end_time of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The upgrade_end_time of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: str
        """
        return self._upgrade_end_time

    @upgrade_end_time.setter
    def upgrade_end_time(self, upgrade_end_time):
        """Sets the upgrade_end_time of this FileSystemForDescribeFileSystemsOutput.


        :param upgrade_end_time: The upgrade_end_time of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: str
        """

        self._upgrade_end_time = upgrade_end_time

    @property
    def upgrade_error(self):
        """Gets the upgrade_error of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The upgrade_error of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: str
        """
        return self._upgrade_error

    @upgrade_error.setter
    def upgrade_error(self, upgrade_error):
        """Sets the upgrade_error of this FileSystemForDescribeFileSystemsOutput.


        :param upgrade_error: The upgrade_error of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: str
        """

        self._upgrade_error = upgrade_error

    @property
    def upgrade_start_time(self):
        """Gets the upgrade_start_time of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The upgrade_start_time of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: str
        """
        return self._upgrade_start_time

    @upgrade_start_time.setter
    def upgrade_start_time(self, upgrade_start_time):
        """Sets the upgrade_start_time of this FileSystemForDescribeFileSystemsOutput.


        :param upgrade_start_time: The upgrade_start_time of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: str
        """

        self._upgrade_start_time = upgrade_start_time

    @property
    def user_id(self):
        """Gets the user_id of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The user_id of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this FileSystemForDescribeFileSystemsOutput.


        :param user_id: The user_id of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def version(self):
        """Gets the version of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The version of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this FileSystemForDescribeFileSystemsOutput.


        :param version: The version of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def vpc_id(self):
        """Gets the vpc_id of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The vpc_id of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this FileSystemForDescribeFileSystemsOutput.


        :param vpc_id: The vpc_id of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: str
        """

        self._vpc_id = vpc_id

    @property
    def vpc_name(self):
        """Gets the vpc_name of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The vpc_name of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: str
        """
        return self._vpc_name

    @vpc_name.setter
    def vpc_name(self, vpc_name):
        """Sets the vpc_name of this FileSystemForDescribeFileSystemsOutput.


        :param vpc_name: The vpc_name of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: str
        """

        self._vpc_name = vpc_name

    @property
    def zone_id(self):
        """Gets the zone_id of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The zone_id of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this FileSystemForDescribeFileSystemsOutput.


        :param zone_id: The zone_id of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: str
        """

        self._zone_id = zone_id

    @property
    def zone_name(self):
        """Gets the zone_name of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The zone_name of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: str
        """
        return self._zone_name

    @zone_name.setter
    def zone_name(self, zone_name):
        """Sets the zone_name of this FileSystemForDescribeFileSystemsOutput.


        :param zone_name: The zone_name of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: str
        """

        self._zone_name = zone_name

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
        if issubclass(FileSystemForDescribeFileSystemsOutput, dict):
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
        if not isinstance(other, FileSystemForDescribeFileSystemsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileSystemForDescribeFileSystemsOutput):
            return True

        return self.to_dict() != other.to_dict()
