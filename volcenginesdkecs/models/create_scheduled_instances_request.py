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


class CreateScheduledInstancesRequest(object):
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
        'auto_release_at': 'str',
        'client_token': 'str',
        'count': 'int',
        'cpu_max_frequency': 'float',
        'delivery_type': 'str',
        'description': 'str',
        'dry_run': 'bool',
        'eip_address': 'EipAddressForCreateScheduledInstancesInput',
        'elastic_scheduled_instance_type': 'str',
        'end_delivery_at': 'str',
        'hostname': 'str',
        'hpc_cluster_id': 'str',
        'image_id': 'str',
        'install_run_command_agent': 'bool',
        'instance_name': 'str',
        'instance_type_id': 'str',
        'keep_image_credential': 'bool',
        'key_pair_name': 'str',
        'min_count': 'int',
        'network_interfaces': 'list[NetworkInterfaceForCreateScheduledInstancesInput]',
        'password': 'str',
        'project_name': 'str',
        'scheduled_instance_description': 'str',
        'scheduled_instance_name': 'str',
        'security_enhancement_strategy': 'str',
        'start_delivery_at': 'str',
        'suffix_index': 'int',
        'tags': 'list[TagForCreateScheduledInstancesInput]',
        'unique_suffix': 'bool',
        'user_data': 'str',
        'volumes': 'list[VolumeForCreateScheduledInstancesInput]',
        'zone_id': 'str'
    }

    attribute_map = {
        'auto_release_at': 'AutoReleaseAt',
        'client_token': 'ClientToken',
        'count': 'Count',
        'cpu_max_frequency': 'CpuMaxFrequency',
        'delivery_type': 'DeliveryType',
        'description': 'Description',
        'dry_run': 'DryRun',
        'eip_address': 'EipAddress',
        'elastic_scheduled_instance_type': 'ElasticScheduledInstanceType',
        'end_delivery_at': 'EndDeliveryAt',
        'hostname': 'Hostname',
        'hpc_cluster_id': 'HpcClusterId',
        'image_id': 'ImageId',
        'install_run_command_agent': 'InstallRunCommandAgent',
        'instance_name': 'InstanceName',
        'instance_type_id': 'InstanceTypeId',
        'keep_image_credential': 'KeepImageCredential',
        'key_pair_name': 'KeyPairName',
        'min_count': 'MinCount',
        'network_interfaces': 'NetworkInterfaces',
        'password': 'Password',
        'project_name': 'ProjectName',
        'scheduled_instance_description': 'ScheduledInstanceDescription',
        'scheduled_instance_name': 'ScheduledInstanceName',
        'security_enhancement_strategy': 'SecurityEnhancementStrategy',
        'start_delivery_at': 'StartDeliveryAt',
        'suffix_index': 'SuffixIndex',
        'tags': 'Tags',
        'unique_suffix': 'UniqueSuffix',
        'user_data': 'UserData',
        'volumes': 'Volumes',
        'zone_id': 'ZoneId'
    }

    def __init__(self, auto_release_at=None, client_token=None, count=None, cpu_max_frequency=None, delivery_type=None, description=None, dry_run=None, eip_address=None, elastic_scheduled_instance_type=None, end_delivery_at=None, hostname=None, hpc_cluster_id=None, image_id=None, install_run_command_agent=None, instance_name=None, instance_type_id=None, keep_image_credential=None, key_pair_name=None, min_count=None, network_interfaces=None, password=None, project_name=None, scheduled_instance_description=None, scheduled_instance_name=None, security_enhancement_strategy=None, start_delivery_at=None, suffix_index=None, tags=None, unique_suffix=None, user_data=None, volumes=None, zone_id=None, _configuration=None):  # noqa: E501
        """CreateScheduledInstancesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._auto_release_at = None
        self._client_token = None
        self._count = None
        self._cpu_max_frequency = None
        self._delivery_type = None
        self._description = None
        self._dry_run = None
        self._eip_address = None
        self._elastic_scheduled_instance_type = None
        self._end_delivery_at = None
        self._hostname = None
        self._hpc_cluster_id = None
        self._image_id = None
        self._install_run_command_agent = None
        self._instance_name = None
        self._instance_type_id = None
        self._keep_image_credential = None
        self._key_pair_name = None
        self._min_count = None
        self._network_interfaces = None
        self._password = None
        self._project_name = None
        self._scheduled_instance_description = None
        self._scheduled_instance_name = None
        self._security_enhancement_strategy = None
        self._start_delivery_at = None
        self._suffix_index = None
        self._tags = None
        self._unique_suffix = None
        self._user_data = None
        self._volumes = None
        self._zone_id = None
        self.discriminator = None

        if auto_release_at is not None:
            self.auto_release_at = auto_release_at
        if client_token is not None:
            self.client_token = client_token
        if count is not None:
            self.count = count
        if cpu_max_frequency is not None:
            self.cpu_max_frequency = cpu_max_frequency
        if delivery_type is not None:
            self.delivery_type = delivery_type
        if description is not None:
            self.description = description
        if dry_run is not None:
            self.dry_run = dry_run
        if eip_address is not None:
            self.eip_address = eip_address
        if elastic_scheduled_instance_type is not None:
            self.elastic_scheduled_instance_type = elastic_scheduled_instance_type
        if end_delivery_at is not None:
            self.end_delivery_at = end_delivery_at
        if hostname is not None:
            self.hostname = hostname
        if hpc_cluster_id is not None:
            self.hpc_cluster_id = hpc_cluster_id
        self.image_id = image_id
        if install_run_command_agent is not None:
            self.install_run_command_agent = install_run_command_agent
        self.instance_name = instance_name
        self.instance_type_id = instance_type_id
        if keep_image_credential is not None:
            self.keep_image_credential = keep_image_credential
        if key_pair_name is not None:
            self.key_pair_name = key_pair_name
        if min_count is not None:
            self.min_count = min_count
        if network_interfaces is not None:
            self.network_interfaces = network_interfaces
        if password is not None:
            self.password = password
        if project_name is not None:
            self.project_name = project_name
        if scheduled_instance_description is not None:
            self.scheduled_instance_description = scheduled_instance_description
        self.scheduled_instance_name = scheduled_instance_name
        if security_enhancement_strategy is not None:
            self.security_enhancement_strategy = security_enhancement_strategy
        if start_delivery_at is not None:
            self.start_delivery_at = start_delivery_at
        if suffix_index is not None:
            self.suffix_index = suffix_index
        if tags is not None:
            self.tags = tags
        if unique_suffix is not None:
            self.unique_suffix = unique_suffix
        if user_data is not None:
            self.user_data = user_data
        if volumes is not None:
            self.volumes = volumes
        self.zone_id = zone_id

    @property
    def auto_release_at(self):
        """Gets the auto_release_at of this CreateScheduledInstancesRequest.  # noqa: E501


        :return: The auto_release_at of this CreateScheduledInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._auto_release_at

    @auto_release_at.setter
    def auto_release_at(self, auto_release_at):
        """Sets the auto_release_at of this CreateScheduledInstancesRequest.


        :param auto_release_at: The auto_release_at of this CreateScheduledInstancesRequest.  # noqa: E501
        :type: str
        """

        self._auto_release_at = auto_release_at

    @property
    def client_token(self):
        """Gets the client_token of this CreateScheduledInstancesRequest.  # noqa: E501


        :return: The client_token of this CreateScheduledInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_token

    @client_token.setter
    def client_token(self, client_token):
        """Sets the client_token of this CreateScheduledInstancesRequest.


        :param client_token: The client_token of this CreateScheduledInstancesRequest.  # noqa: E501
        :type: str
        """

        self._client_token = client_token

    @property
    def count(self):
        """Gets the count of this CreateScheduledInstancesRequest.  # noqa: E501


        :return: The count of this CreateScheduledInstancesRequest.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this CreateScheduledInstancesRequest.


        :param count: The count of this CreateScheduledInstancesRequest.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def cpu_max_frequency(self):
        """Gets the cpu_max_frequency of this CreateScheduledInstancesRequest.  # noqa: E501


        :return: The cpu_max_frequency of this CreateScheduledInstancesRequest.  # noqa: E501
        :rtype: float
        """
        return self._cpu_max_frequency

    @cpu_max_frequency.setter
    def cpu_max_frequency(self, cpu_max_frequency):
        """Sets the cpu_max_frequency of this CreateScheduledInstancesRequest.


        :param cpu_max_frequency: The cpu_max_frequency of this CreateScheduledInstancesRequest.  # noqa: E501
        :type: float
        """

        self._cpu_max_frequency = cpu_max_frequency

    @property
    def delivery_type(self):
        """Gets the delivery_type of this CreateScheduledInstancesRequest.  # noqa: E501


        :return: The delivery_type of this CreateScheduledInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._delivery_type

    @delivery_type.setter
    def delivery_type(self, delivery_type):
        """Sets the delivery_type of this CreateScheduledInstancesRequest.


        :param delivery_type: The delivery_type of this CreateScheduledInstancesRequest.  # noqa: E501
        :type: str
        """

        self._delivery_type = delivery_type

    @property
    def description(self):
        """Gets the description of this CreateScheduledInstancesRequest.  # noqa: E501


        :return: The description of this CreateScheduledInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateScheduledInstancesRequest.


        :param description: The description of this CreateScheduledInstancesRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def dry_run(self):
        """Gets the dry_run of this CreateScheduledInstancesRequest.  # noqa: E501


        :return: The dry_run of this CreateScheduledInstancesRequest.  # noqa: E501
        :rtype: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        """Sets the dry_run of this CreateScheduledInstancesRequest.


        :param dry_run: The dry_run of this CreateScheduledInstancesRequest.  # noqa: E501
        :type: bool
        """

        self._dry_run = dry_run

    @property
    def eip_address(self):
        """Gets the eip_address of this CreateScheduledInstancesRequest.  # noqa: E501


        :return: The eip_address of this CreateScheduledInstancesRequest.  # noqa: E501
        :rtype: EipAddressForCreateScheduledInstancesInput
        """
        return self._eip_address

    @eip_address.setter
    def eip_address(self, eip_address):
        """Sets the eip_address of this CreateScheduledInstancesRequest.


        :param eip_address: The eip_address of this CreateScheduledInstancesRequest.  # noqa: E501
        :type: EipAddressForCreateScheduledInstancesInput
        """

        self._eip_address = eip_address

    @property
    def elastic_scheduled_instance_type(self):
        """Gets the elastic_scheduled_instance_type of this CreateScheduledInstancesRequest.  # noqa: E501


        :return: The elastic_scheduled_instance_type of this CreateScheduledInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._elastic_scheduled_instance_type

    @elastic_scheduled_instance_type.setter
    def elastic_scheduled_instance_type(self, elastic_scheduled_instance_type):
        """Sets the elastic_scheduled_instance_type of this CreateScheduledInstancesRequest.


        :param elastic_scheduled_instance_type: The elastic_scheduled_instance_type of this CreateScheduledInstancesRequest.  # noqa: E501
        :type: str
        """

        self._elastic_scheduled_instance_type = elastic_scheduled_instance_type

    @property
    def end_delivery_at(self):
        """Gets the end_delivery_at of this CreateScheduledInstancesRequest.  # noqa: E501


        :return: The end_delivery_at of this CreateScheduledInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._end_delivery_at

    @end_delivery_at.setter
    def end_delivery_at(self, end_delivery_at):
        """Sets the end_delivery_at of this CreateScheduledInstancesRequest.


        :param end_delivery_at: The end_delivery_at of this CreateScheduledInstancesRequest.  # noqa: E501
        :type: str
        """

        self._end_delivery_at = end_delivery_at

    @property
    def hostname(self):
        """Gets the hostname of this CreateScheduledInstancesRequest.  # noqa: E501


        :return: The hostname of this CreateScheduledInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this CreateScheduledInstancesRequest.


        :param hostname: The hostname of this CreateScheduledInstancesRequest.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def hpc_cluster_id(self):
        """Gets the hpc_cluster_id of this CreateScheduledInstancesRequest.  # noqa: E501


        :return: The hpc_cluster_id of this CreateScheduledInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._hpc_cluster_id

    @hpc_cluster_id.setter
    def hpc_cluster_id(self, hpc_cluster_id):
        """Sets the hpc_cluster_id of this CreateScheduledInstancesRequest.


        :param hpc_cluster_id: The hpc_cluster_id of this CreateScheduledInstancesRequest.  # noqa: E501
        :type: str
        """

        self._hpc_cluster_id = hpc_cluster_id

    @property
    def image_id(self):
        """Gets the image_id of this CreateScheduledInstancesRequest.  # noqa: E501


        :return: The image_id of this CreateScheduledInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this CreateScheduledInstancesRequest.


        :param image_id: The image_id of this CreateScheduledInstancesRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and image_id is None:
            raise ValueError("Invalid value for `image_id`, must not be `None`")  # noqa: E501

        self._image_id = image_id

    @property
    def install_run_command_agent(self):
        """Gets the install_run_command_agent of this CreateScheduledInstancesRequest.  # noqa: E501


        :return: The install_run_command_agent of this CreateScheduledInstancesRequest.  # noqa: E501
        :rtype: bool
        """
        return self._install_run_command_agent

    @install_run_command_agent.setter
    def install_run_command_agent(self, install_run_command_agent):
        """Sets the install_run_command_agent of this CreateScheduledInstancesRequest.


        :param install_run_command_agent: The install_run_command_agent of this CreateScheduledInstancesRequest.  # noqa: E501
        :type: bool
        """

        self._install_run_command_agent = install_run_command_agent

    @property
    def instance_name(self):
        """Gets the instance_name of this CreateScheduledInstancesRequest.  # noqa: E501


        :return: The instance_name of this CreateScheduledInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this CreateScheduledInstancesRequest.


        :param instance_name: The instance_name of this CreateScheduledInstancesRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and instance_name is None:
            raise ValueError("Invalid value for `instance_name`, must not be `None`")  # noqa: E501

        self._instance_name = instance_name

    @property
    def instance_type_id(self):
        """Gets the instance_type_id of this CreateScheduledInstancesRequest.  # noqa: E501


        :return: The instance_type_id of this CreateScheduledInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_type_id

    @instance_type_id.setter
    def instance_type_id(self, instance_type_id):
        """Sets the instance_type_id of this CreateScheduledInstancesRequest.


        :param instance_type_id: The instance_type_id of this CreateScheduledInstancesRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and instance_type_id is None:
            raise ValueError("Invalid value for `instance_type_id`, must not be `None`")  # noqa: E501

        self._instance_type_id = instance_type_id

    @property
    def keep_image_credential(self):
        """Gets the keep_image_credential of this CreateScheduledInstancesRequest.  # noqa: E501


        :return: The keep_image_credential of this CreateScheduledInstancesRequest.  # noqa: E501
        :rtype: bool
        """
        return self._keep_image_credential

    @keep_image_credential.setter
    def keep_image_credential(self, keep_image_credential):
        """Sets the keep_image_credential of this CreateScheduledInstancesRequest.


        :param keep_image_credential: The keep_image_credential of this CreateScheduledInstancesRequest.  # noqa: E501
        :type: bool
        """

        self._keep_image_credential = keep_image_credential

    @property
    def key_pair_name(self):
        """Gets the key_pair_name of this CreateScheduledInstancesRequest.  # noqa: E501


        :return: The key_pair_name of this CreateScheduledInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._key_pair_name

    @key_pair_name.setter
    def key_pair_name(self, key_pair_name):
        """Sets the key_pair_name of this CreateScheduledInstancesRequest.


        :param key_pair_name: The key_pair_name of this CreateScheduledInstancesRequest.  # noqa: E501
        :type: str
        """

        self._key_pair_name = key_pair_name

    @property
    def min_count(self):
        """Gets the min_count of this CreateScheduledInstancesRequest.  # noqa: E501


        :return: The min_count of this CreateScheduledInstancesRequest.  # noqa: E501
        :rtype: int
        """
        return self._min_count

    @min_count.setter
    def min_count(self, min_count):
        """Sets the min_count of this CreateScheduledInstancesRequest.


        :param min_count: The min_count of this CreateScheduledInstancesRequest.  # noqa: E501
        :type: int
        """

        self._min_count = min_count

    @property
    def network_interfaces(self):
        """Gets the network_interfaces of this CreateScheduledInstancesRequest.  # noqa: E501


        :return: The network_interfaces of this CreateScheduledInstancesRequest.  # noqa: E501
        :rtype: list[NetworkInterfaceForCreateScheduledInstancesInput]
        """
        return self._network_interfaces

    @network_interfaces.setter
    def network_interfaces(self, network_interfaces):
        """Sets the network_interfaces of this CreateScheduledInstancesRequest.


        :param network_interfaces: The network_interfaces of this CreateScheduledInstancesRequest.  # noqa: E501
        :type: list[NetworkInterfaceForCreateScheduledInstancesInput]
        """

        self._network_interfaces = network_interfaces

    @property
    def password(self):
        """Gets the password of this CreateScheduledInstancesRequest.  # noqa: E501


        :return: The password of this CreateScheduledInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this CreateScheduledInstancesRequest.


        :param password: The password of this CreateScheduledInstancesRequest.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def project_name(self):
        """Gets the project_name of this CreateScheduledInstancesRequest.  # noqa: E501


        :return: The project_name of this CreateScheduledInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this CreateScheduledInstancesRequest.


        :param project_name: The project_name of this CreateScheduledInstancesRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def scheduled_instance_description(self):
        """Gets the scheduled_instance_description of this CreateScheduledInstancesRequest.  # noqa: E501


        :return: The scheduled_instance_description of this CreateScheduledInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._scheduled_instance_description

    @scheduled_instance_description.setter
    def scheduled_instance_description(self, scheduled_instance_description):
        """Sets the scheduled_instance_description of this CreateScheduledInstancesRequest.


        :param scheduled_instance_description: The scheduled_instance_description of this CreateScheduledInstancesRequest.  # noqa: E501
        :type: str
        """

        self._scheduled_instance_description = scheduled_instance_description

    @property
    def scheduled_instance_name(self):
        """Gets the scheduled_instance_name of this CreateScheduledInstancesRequest.  # noqa: E501


        :return: The scheduled_instance_name of this CreateScheduledInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._scheduled_instance_name

    @scheduled_instance_name.setter
    def scheduled_instance_name(self, scheduled_instance_name):
        """Sets the scheduled_instance_name of this CreateScheduledInstancesRequest.


        :param scheduled_instance_name: The scheduled_instance_name of this CreateScheduledInstancesRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and scheduled_instance_name is None:
            raise ValueError("Invalid value for `scheduled_instance_name`, must not be `None`")  # noqa: E501

        self._scheduled_instance_name = scheduled_instance_name

    @property
    def security_enhancement_strategy(self):
        """Gets the security_enhancement_strategy of this CreateScheduledInstancesRequest.  # noqa: E501


        :return: The security_enhancement_strategy of this CreateScheduledInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._security_enhancement_strategy

    @security_enhancement_strategy.setter
    def security_enhancement_strategy(self, security_enhancement_strategy):
        """Sets the security_enhancement_strategy of this CreateScheduledInstancesRequest.


        :param security_enhancement_strategy: The security_enhancement_strategy of this CreateScheduledInstancesRequest.  # noqa: E501
        :type: str
        """

        self._security_enhancement_strategy = security_enhancement_strategy

    @property
    def start_delivery_at(self):
        """Gets the start_delivery_at of this CreateScheduledInstancesRequest.  # noqa: E501


        :return: The start_delivery_at of this CreateScheduledInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._start_delivery_at

    @start_delivery_at.setter
    def start_delivery_at(self, start_delivery_at):
        """Sets the start_delivery_at of this CreateScheduledInstancesRequest.


        :param start_delivery_at: The start_delivery_at of this CreateScheduledInstancesRequest.  # noqa: E501
        :type: str
        """

        self._start_delivery_at = start_delivery_at

    @property
    def suffix_index(self):
        """Gets the suffix_index of this CreateScheduledInstancesRequest.  # noqa: E501


        :return: The suffix_index of this CreateScheduledInstancesRequest.  # noqa: E501
        :rtype: int
        """
        return self._suffix_index

    @suffix_index.setter
    def suffix_index(self, suffix_index):
        """Sets the suffix_index of this CreateScheduledInstancesRequest.


        :param suffix_index: The suffix_index of this CreateScheduledInstancesRequest.  # noqa: E501
        :type: int
        """

        self._suffix_index = suffix_index

    @property
    def tags(self):
        """Gets the tags of this CreateScheduledInstancesRequest.  # noqa: E501


        :return: The tags of this CreateScheduledInstancesRequest.  # noqa: E501
        :rtype: list[TagForCreateScheduledInstancesInput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateScheduledInstancesRequest.


        :param tags: The tags of this CreateScheduledInstancesRequest.  # noqa: E501
        :type: list[TagForCreateScheduledInstancesInput]
        """

        self._tags = tags

    @property
    def unique_suffix(self):
        """Gets the unique_suffix of this CreateScheduledInstancesRequest.  # noqa: E501


        :return: The unique_suffix of this CreateScheduledInstancesRequest.  # noqa: E501
        :rtype: bool
        """
        return self._unique_suffix

    @unique_suffix.setter
    def unique_suffix(self, unique_suffix):
        """Sets the unique_suffix of this CreateScheduledInstancesRequest.


        :param unique_suffix: The unique_suffix of this CreateScheduledInstancesRequest.  # noqa: E501
        :type: bool
        """

        self._unique_suffix = unique_suffix

    @property
    def user_data(self):
        """Gets the user_data of this CreateScheduledInstancesRequest.  # noqa: E501


        :return: The user_data of this CreateScheduledInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this CreateScheduledInstancesRequest.


        :param user_data: The user_data of this CreateScheduledInstancesRequest.  # noqa: E501
        :type: str
        """

        self._user_data = user_data

    @property
    def volumes(self):
        """Gets the volumes of this CreateScheduledInstancesRequest.  # noqa: E501


        :return: The volumes of this CreateScheduledInstancesRequest.  # noqa: E501
        :rtype: list[VolumeForCreateScheduledInstancesInput]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this CreateScheduledInstancesRequest.


        :param volumes: The volumes of this CreateScheduledInstancesRequest.  # noqa: E501
        :type: list[VolumeForCreateScheduledInstancesInput]
        """

        self._volumes = volumes

    @property
    def zone_id(self):
        """Gets the zone_id of this CreateScheduledInstancesRequest.  # noqa: E501


        :return: The zone_id of this CreateScheduledInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this CreateScheduledInstancesRequest.


        :param zone_id: The zone_id of this CreateScheduledInstancesRequest.  # noqa: E501
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
        if issubclass(CreateScheduledInstancesRequest, dict):
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
        if not isinstance(other, CreateScheduledInstancesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateScheduledInstancesRequest):
            return True

        return self.to_dict() != other.to_dict()
