# coding: utf-8

"""
    rocketmq

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class CreateInstanceRequest(object):
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
        'allow_list_ids': 'list[str]',
        'charge_info': 'ChargeInfoForCreateInstanceInput',
        'client_token': 'str',
        'compute_spec': 'str',
        'eip_id': 'str',
        'enable_ssl': 'bool',
        'file_reserved_time': 'int',
        'ip_version_type': 'str',
        'instance_description': 'str',
        'instance_name': 'str',
        'network_types': 'str',
        'project_name': 'str',
        'ssl_mode': 'str',
        'storage_space': 'int',
        'subnet_id': 'str',
        'tags': 'dict(str, str)',
        'version': 'str',
        'vpc_id': 'str',
        'zone_id': 'str'
    }

    attribute_map = {
        'allow_list_ids': 'AllowListIds',
        'charge_info': 'ChargeInfo',
        'client_token': 'ClientToken',
        'compute_spec': 'ComputeSpec',
        'eip_id': 'EipId',
        'enable_ssl': 'EnableSSL',
        'file_reserved_time': 'FileReservedTime',
        'ip_version_type': 'IPVersionType',
        'instance_description': 'InstanceDescription',
        'instance_name': 'InstanceName',
        'network_types': 'NetworkTypes',
        'project_name': 'ProjectName',
        'ssl_mode': 'SSLMode',
        'storage_space': 'StorageSpace',
        'subnet_id': 'SubnetId',
        'tags': 'Tags',
        'version': 'Version',
        'vpc_id': 'VpcId',
        'zone_id': 'ZoneId'
    }

    def __init__(self, allow_list_ids=None, charge_info=None, client_token=None, compute_spec=None, eip_id=None, enable_ssl=None, file_reserved_time=None, ip_version_type=None, instance_description=None, instance_name=None, network_types=None, project_name=None, ssl_mode=None, storage_space=None, subnet_id=None, tags=None, version=None, vpc_id=None, zone_id=None, _configuration=None):  # noqa: E501
        """CreateInstanceRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._allow_list_ids = None
        self._charge_info = None
        self._client_token = None
        self._compute_spec = None
        self._eip_id = None
        self._enable_ssl = None
        self._file_reserved_time = None
        self._ip_version_type = None
        self._instance_description = None
        self._instance_name = None
        self._network_types = None
        self._project_name = None
        self._ssl_mode = None
        self._storage_space = None
        self._subnet_id = None
        self._tags = None
        self._version = None
        self._vpc_id = None
        self._zone_id = None
        self.discriminator = None

        if allow_list_ids is not None:
            self.allow_list_ids = allow_list_ids
        if charge_info is not None:
            self.charge_info = charge_info
        if client_token is not None:
            self.client_token = client_token
        self.compute_spec = compute_spec
        if eip_id is not None:
            self.eip_id = eip_id
        if enable_ssl is not None:
            self.enable_ssl = enable_ssl
        self.file_reserved_time = file_reserved_time
        if ip_version_type is not None:
            self.ip_version_type = ip_version_type
        if instance_description is not None:
            self.instance_description = instance_description
        if instance_name is not None:
            self.instance_name = instance_name
        self.network_types = network_types
        if project_name is not None:
            self.project_name = project_name
        if ssl_mode is not None:
            self.ssl_mode = ssl_mode
        self.storage_space = storage_space
        self.subnet_id = subnet_id
        if tags is not None:
            self.tags = tags
        self.version = version
        self.vpc_id = vpc_id
        self.zone_id = zone_id

    @property
    def allow_list_ids(self):
        """Gets the allow_list_ids of this CreateInstanceRequest.  # noqa: E501


        :return: The allow_list_ids of this CreateInstanceRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._allow_list_ids

    @allow_list_ids.setter
    def allow_list_ids(self, allow_list_ids):
        """Sets the allow_list_ids of this CreateInstanceRequest.


        :param allow_list_ids: The allow_list_ids of this CreateInstanceRequest.  # noqa: E501
        :type: list[str]
        """

        self._allow_list_ids = allow_list_ids

    @property
    def charge_info(self):
        """Gets the charge_info of this CreateInstanceRequest.  # noqa: E501


        :return: The charge_info of this CreateInstanceRequest.  # noqa: E501
        :rtype: ChargeInfoForCreateInstanceInput
        """
        return self._charge_info

    @charge_info.setter
    def charge_info(self, charge_info):
        """Sets the charge_info of this CreateInstanceRequest.


        :param charge_info: The charge_info of this CreateInstanceRequest.  # noqa: E501
        :type: ChargeInfoForCreateInstanceInput
        """

        self._charge_info = charge_info

    @property
    def client_token(self):
        """Gets the client_token of this CreateInstanceRequest.  # noqa: E501


        :return: The client_token of this CreateInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_token

    @client_token.setter
    def client_token(self, client_token):
        """Sets the client_token of this CreateInstanceRequest.


        :param client_token: The client_token of this CreateInstanceRequest.  # noqa: E501
        :type: str
        """

        self._client_token = client_token

    @property
    def compute_spec(self):
        """Gets the compute_spec of this CreateInstanceRequest.  # noqa: E501


        :return: The compute_spec of this CreateInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._compute_spec

    @compute_spec.setter
    def compute_spec(self, compute_spec):
        """Sets the compute_spec of this CreateInstanceRequest.


        :param compute_spec: The compute_spec of this CreateInstanceRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and compute_spec is None:
            raise ValueError("Invalid value for `compute_spec`, must not be `None`")  # noqa: E501

        self._compute_spec = compute_spec

    @property
    def eip_id(self):
        """Gets the eip_id of this CreateInstanceRequest.  # noqa: E501


        :return: The eip_id of this CreateInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._eip_id

    @eip_id.setter
    def eip_id(self, eip_id):
        """Sets the eip_id of this CreateInstanceRequest.


        :param eip_id: The eip_id of this CreateInstanceRequest.  # noqa: E501
        :type: str
        """

        self._eip_id = eip_id

    @property
    def enable_ssl(self):
        """Gets the enable_ssl of this CreateInstanceRequest.  # noqa: E501


        :return: The enable_ssl of this CreateInstanceRequest.  # noqa: E501
        :rtype: bool
        """
        return self._enable_ssl

    @enable_ssl.setter
    def enable_ssl(self, enable_ssl):
        """Sets the enable_ssl of this CreateInstanceRequest.


        :param enable_ssl: The enable_ssl of this CreateInstanceRequest.  # noqa: E501
        :type: bool
        """

        self._enable_ssl = enable_ssl

    @property
    def file_reserved_time(self):
        """Gets the file_reserved_time of this CreateInstanceRequest.  # noqa: E501


        :return: The file_reserved_time of this CreateInstanceRequest.  # noqa: E501
        :rtype: int
        """
        return self._file_reserved_time

    @file_reserved_time.setter
    def file_reserved_time(self, file_reserved_time):
        """Sets the file_reserved_time of this CreateInstanceRequest.


        :param file_reserved_time: The file_reserved_time of this CreateInstanceRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and file_reserved_time is None:
            raise ValueError("Invalid value for `file_reserved_time`, must not be `None`")  # noqa: E501

        self._file_reserved_time = file_reserved_time

    @property
    def ip_version_type(self):
        """Gets the ip_version_type of this CreateInstanceRequest.  # noqa: E501


        :return: The ip_version_type of this CreateInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._ip_version_type

    @ip_version_type.setter
    def ip_version_type(self, ip_version_type):
        """Sets the ip_version_type of this CreateInstanceRequest.


        :param ip_version_type: The ip_version_type of this CreateInstanceRequest.  # noqa: E501
        :type: str
        """

        self._ip_version_type = ip_version_type

    @property
    def instance_description(self):
        """Gets the instance_description of this CreateInstanceRequest.  # noqa: E501


        :return: The instance_description of this CreateInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_description

    @instance_description.setter
    def instance_description(self, instance_description):
        """Sets the instance_description of this CreateInstanceRequest.


        :param instance_description: The instance_description of this CreateInstanceRequest.  # noqa: E501
        :type: str
        """

        self._instance_description = instance_description

    @property
    def instance_name(self):
        """Gets the instance_name of this CreateInstanceRequest.  # noqa: E501


        :return: The instance_name of this CreateInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this CreateInstanceRequest.


        :param instance_name: The instance_name of this CreateInstanceRequest.  # noqa: E501
        :type: str
        """

        self._instance_name = instance_name

    @property
    def network_types(self):
        """Gets the network_types of this CreateInstanceRequest.  # noqa: E501


        :return: The network_types of this CreateInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._network_types

    @network_types.setter
    def network_types(self, network_types):
        """Sets the network_types of this CreateInstanceRequest.


        :param network_types: The network_types of this CreateInstanceRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and network_types is None:
            raise ValueError("Invalid value for `network_types`, must not be `None`")  # noqa: E501

        self._network_types = network_types

    @property
    def project_name(self):
        """Gets the project_name of this CreateInstanceRequest.  # noqa: E501


        :return: The project_name of this CreateInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this CreateInstanceRequest.


        :param project_name: The project_name of this CreateInstanceRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def ssl_mode(self):
        """Gets the ssl_mode of this CreateInstanceRequest.  # noqa: E501


        :return: The ssl_mode of this CreateInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._ssl_mode

    @ssl_mode.setter
    def ssl_mode(self, ssl_mode):
        """Sets the ssl_mode of this CreateInstanceRequest.


        :param ssl_mode: The ssl_mode of this CreateInstanceRequest.  # noqa: E501
        :type: str
        """

        self._ssl_mode = ssl_mode

    @property
    def storage_space(self):
        """Gets the storage_space of this CreateInstanceRequest.  # noqa: E501


        :return: The storage_space of this CreateInstanceRequest.  # noqa: E501
        :rtype: int
        """
        return self._storage_space

    @storage_space.setter
    def storage_space(self, storage_space):
        """Sets the storage_space of this CreateInstanceRequest.


        :param storage_space: The storage_space of this CreateInstanceRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and storage_space is None:
            raise ValueError("Invalid value for `storage_space`, must not be `None`")  # noqa: E501

        self._storage_space = storage_space

    @property
    def subnet_id(self):
        """Gets the subnet_id of this CreateInstanceRequest.  # noqa: E501


        :return: The subnet_id of this CreateInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this CreateInstanceRequest.


        :param subnet_id: The subnet_id of this CreateInstanceRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and subnet_id is None:
            raise ValueError("Invalid value for `subnet_id`, must not be `None`")  # noqa: E501

        self._subnet_id = subnet_id

    @property
    def tags(self):
        """Gets the tags of this CreateInstanceRequest.  # noqa: E501


        :return: The tags of this CreateInstanceRequest.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateInstanceRequest.


        :param tags: The tags of this CreateInstanceRequest.  # noqa: E501
        :type: dict(str, str)
        """

        self._tags = tags

    @property
    def version(self):
        """Gets the version of this CreateInstanceRequest.  # noqa: E501


        :return: The version of this CreateInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CreateInstanceRequest.


        :param version: The version of this CreateInstanceRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def vpc_id(self):
        """Gets the vpc_id of this CreateInstanceRequest.  # noqa: E501


        :return: The vpc_id of this CreateInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this CreateInstanceRequest.


        :param vpc_id: The vpc_id of this CreateInstanceRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and vpc_id is None:
            raise ValueError("Invalid value for `vpc_id`, must not be `None`")  # noqa: E501

        self._vpc_id = vpc_id

    @property
    def zone_id(self):
        """Gets the zone_id of this CreateInstanceRequest.  # noqa: E501


        :return: The zone_id of this CreateInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this CreateInstanceRequest.


        :param zone_id: The zone_id of this CreateInstanceRequest.  # noqa: E501
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
        if issubclass(CreateInstanceRequest, dict):
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
        if not isinstance(other, CreateInstanceRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateInstanceRequest):
            return True

        return self.to_dict() != other.to_dict()
