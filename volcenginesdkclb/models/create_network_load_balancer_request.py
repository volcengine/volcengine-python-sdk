# coding: utf-8

"""
    clb

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class CreateNetworkLoadBalancerRequest(object):
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
        'client_token': 'str',
        'cross_zone_enabled': 'bool',
        'description': 'str',
        'ip_address_version': 'str',
        'ipv4_bandwidth_package_id': 'str',
        'load_balancer_name': 'str',
        'modification_protection_status': 'str',
        'network_type': 'str',
        'project_name': 'str',
        'region_id': 'str',
        'security_group_ids': 'list[str]',
        'tags': 'list[TagForCreateNetworkLoadBalancerInput]',
        'vpc_id': 'str',
        'zone_mappings': 'list[ZoneMappingForCreateNetworkLoadBalancerInput]'
    }

    attribute_map = {
        'client_token': 'ClientToken',
        'cross_zone_enabled': 'CrossZoneEnabled',
        'description': 'Description',
        'ip_address_version': 'IpAddressVersion',
        'ipv4_bandwidth_package_id': 'Ipv4BandwidthPackageId',
        'load_balancer_name': 'LoadBalancerName',
        'modification_protection_status': 'ModificationProtectionStatus',
        'network_type': 'NetworkType',
        'project_name': 'ProjectName',
        'region_id': 'RegionId',
        'security_group_ids': 'SecurityGroupIds',
        'tags': 'Tags',
        'vpc_id': 'VpcId',
        'zone_mappings': 'ZoneMappings'
    }

    def __init__(self, client_token=None, cross_zone_enabled=None, description=None, ip_address_version=None, ipv4_bandwidth_package_id=None, load_balancer_name=None, modification_protection_status=None, network_type=None, project_name=None, region_id=None, security_group_ids=None, tags=None, vpc_id=None, zone_mappings=None, _configuration=None):  # noqa: E501
        """CreateNetworkLoadBalancerRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._client_token = None
        self._cross_zone_enabled = None
        self._description = None
        self._ip_address_version = None
        self._ipv4_bandwidth_package_id = None
        self._load_balancer_name = None
        self._modification_protection_status = None
        self._network_type = None
        self._project_name = None
        self._region_id = None
        self._security_group_ids = None
        self._tags = None
        self._vpc_id = None
        self._zone_mappings = None
        self.discriminator = None

        if client_token is not None:
            self.client_token = client_token
        if cross_zone_enabled is not None:
            self.cross_zone_enabled = cross_zone_enabled
        if description is not None:
            self.description = description
        if ip_address_version is not None:
            self.ip_address_version = ip_address_version
        if ipv4_bandwidth_package_id is not None:
            self.ipv4_bandwidth_package_id = ipv4_bandwidth_package_id
        if load_balancer_name is not None:
            self.load_balancer_name = load_balancer_name
        if modification_protection_status is not None:
            self.modification_protection_status = modification_protection_status
        self.network_type = network_type
        if project_name is not None:
            self.project_name = project_name
        self.region_id = region_id
        if security_group_ids is not None:
            self.security_group_ids = security_group_ids
        if tags is not None:
            self.tags = tags
        self.vpc_id = vpc_id
        if zone_mappings is not None:
            self.zone_mappings = zone_mappings

    @property
    def client_token(self):
        """Gets the client_token of this CreateNetworkLoadBalancerRequest.  # noqa: E501


        :return: The client_token of this CreateNetworkLoadBalancerRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_token

    @client_token.setter
    def client_token(self, client_token):
        """Sets the client_token of this CreateNetworkLoadBalancerRequest.


        :param client_token: The client_token of this CreateNetworkLoadBalancerRequest.  # noqa: E501
        :type: str
        """

        self._client_token = client_token

    @property
    def cross_zone_enabled(self):
        """Gets the cross_zone_enabled of this CreateNetworkLoadBalancerRequest.  # noqa: E501


        :return: The cross_zone_enabled of this CreateNetworkLoadBalancerRequest.  # noqa: E501
        :rtype: bool
        """
        return self._cross_zone_enabled

    @cross_zone_enabled.setter
    def cross_zone_enabled(self, cross_zone_enabled):
        """Sets the cross_zone_enabled of this CreateNetworkLoadBalancerRequest.


        :param cross_zone_enabled: The cross_zone_enabled of this CreateNetworkLoadBalancerRequest.  # noqa: E501
        :type: bool
        """

        self._cross_zone_enabled = cross_zone_enabled

    @property
    def description(self):
        """Gets the description of this CreateNetworkLoadBalancerRequest.  # noqa: E501


        :return: The description of this CreateNetworkLoadBalancerRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateNetworkLoadBalancerRequest.


        :param description: The description of this CreateNetworkLoadBalancerRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def ip_address_version(self):
        """Gets the ip_address_version of this CreateNetworkLoadBalancerRequest.  # noqa: E501


        :return: The ip_address_version of this CreateNetworkLoadBalancerRequest.  # noqa: E501
        :rtype: str
        """
        return self._ip_address_version

    @ip_address_version.setter
    def ip_address_version(self, ip_address_version):
        """Sets the ip_address_version of this CreateNetworkLoadBalancerRequest.


        :param ip_address_version: The ip_address_version of this CreateNetworkLoadBalancerRequest.  # noqa: E501
        :type: str
        """

        self._ip_address_version = ip_address_version

    @property
    def ipv4_bandwidth_package_id(self):
        """Gets the ipv4_bandwidth_package_id of this CreateNetworkLoadBalancerRequest.  # noqa: E501


        :return: The ipv4_bandwidth_package_id of this CreateNetworkLoadBalancerRequest.  # noqa: E501
        :rtype: str
        """
        return self._ipv4_bandwidth_package_id

    @ipv4_bandwidth_package_id.setter
    def ipv4_bandwidth_package_id(self, ipv4_bandwidth_package_id):
        """Sets the ipv4_bandwidth_package_id of this CreateNetworkLoadBalancerRequest.


        :param ipv4_bandwidth_package_id: The ipv4_bandwidth_package_id of this CreateNetworkLoadBalancerRequest.  # noqa: E501
        :type: str
        """

        self._ipv4_bandwidth_package_id = ipv4_bandwidth_package_id

    @property
    def load_balancer_name(self):
        """Gets the load_balancer_name of this CreateNetworkLoadBalancerRequest.  # noqa: E501


        :return: The load_balancer_name of this CreateNetworkLoadBalancerRequest.  # noqa: E501
        :rtype: str
        """
        return self._load_balancer_name

    @load_balancer_name.setter
    def load_balancer_name(self, load_balancer_name):
        """Sets the load_balancer_name of this CreateNetworkLoadBalancerRequest.


        :param load_balancer_name: The load_balancer_name of this CreateNetworkLoadBalancerRequest.  # noqa: E501
        :type: str
        """

        self._load_balancer_name = load_balancer_name

    @property
    def modification_protection_status(self):
        """Gets the modification_protection_status of this CreateNetworkLoadBalancerRequest.  # noqa: E501


        :return: The modification_protection_status of this CreateNetworkLoadBalancerRequest.  # noqa: E501
        :rtype: str
        """
        return self._modification_protection_status

    @modification_protection_status.setter
    def modification_protection_status(self, modification_protection_status):
        """Sets the modification_protection_status of this CreateNetworkLoadBalancerRequest.


        :param modification_protection_status: The modification_protection_status of this CreateNetworkLoadBalancerRequest.  # noqa: E501
        :type: str
        """

        self._modification_protection_status = modification_protection_status

    @property
    def network_type(self):
        """Gets the network_type of this CreateNetworkLoadBalancerRequest.  # noqa: E501


        :return: The network_type of this CreateNetworkLoadBalancerRequest.  # noqa: E501
        :rtype: str
        """
        return self._network_type

    @network_type.setter
    def network_type(self, network_type):
        """Sets the network_type of this CreateNetworkLoadBalancerRequest.


        :param network_type: The network_type of this CreateNetworkLoadBalancerRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and network_type is None:
            raise ValueError("Invalid value for `network_type`, must not be `None`")  # noqa: E501

        self._network_type = network_type

    @property
    def project_name(self):
        """Gets the project_name of this CreateNetworkLoadBalancerRequest.  # noqa: E501


        :return: The project_name of this CreateNetworkLoadBalancerRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this CreateNetworkLoadBalancerRequest.


        :param project_name: The project_name of this CreateNetworkLoadBalancerRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def region_id(self):
        """Gets the region_id of this CreateNetworkLoadBalancerRequest.  # noqa: E501


        :return: The region_id of this CreateNetworkLoadBalancerRequest.  # noqa: E501
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this CreateNetworkLoadBalancerRequest.


        :param region_id: The region_id of this CreateNetworkLoadBalancerRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and region_id is None:
            raise ValueError("Invalid value for `region_id`, must not be `None`")  # noqa: E501

        self._region_id = region_id

    @property
    def security_group_ids(self):
        """Gets the security_group_ids of this CreateNetworkLoadBalancerRequest.  # noqa: E501


        :return: The security_group_ids of this CreateNetworkLoadBalancerRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._security_group_ids

    @security_group_ids.setter
    def security_group_ids(self, security_group_ids):
        """Sets the security_group_ids of this CreateNetworkLoadBalancerRequest.


        :param security_group_ids: The security_group_ids of this CreateNetworkLoadBalancerRequest.  # noqa: E501
        :type: list[str]
        """

        self._security_group_ids = security_group_ids

    @property
    def tags(self):
        """Gets the tags of this CreateNetworkLoadBalancerRequest.  # noqa: E501


        :return: The tags of this CreateNetworkLoadBalancerRequest.  # noqa: E501
        :rtype: list[TagForCreateNetworkLoadBalancerInput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateNetworkLoadBalancerRequest.


        :param tags: The tags of this CreateNetworkLoadBalancerRequest.  # noqa: E501
        :type: list[TagForCreateNetworkLoadBalancerInput]
        """

        self._tags = tags

    @property
    def vpc_id(self):
        """Gets the vpc_id of this CreateNetworkLoadBalancerRequest.  # noqa: E501


        :return: The vpc_id of this CreateNetworkLoadBalancerRequest.  # noqa: E501
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this CreateNetworkLoadBalancerRequest.


        :param vpc_id: The vpc_id of this CreateNetworkLoadBalancerRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and vpc_id is None:
            raise ValueError("Invalid value for `vpc_id`, must not be `None`")  # noqa: E501

        self._vpc_id = vpc_id

    @property
    def zone_mappings(self):
        """Gets the zone_mappings of this CreateNetworkLoadBalancerRequest.  # noqa: E501


        :return: The zone_mappings of this CreateNetworkLoadBalancerRequest.  # noqa: E501
        :rtype: list[ZoneMappingForCreateNetworkLoadBalancerInput]
        """
        return self._zone_mappings

    @zone_mappings.setter
    def zone_mappings(self, zone_mappings):
        """Sets the zone_mappings of this CreateNetworkLoadBalancerRequest.


        :param zone_mappings: The zone_mappings of this CreateNetworkLoadBalancerRequest.  # noqa: E501
        :type: list[ZoneMappingForCreateNetworkLoadBalancerInput]
        """

        self._zone_mappings = zone_mappings

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
        if issubclass(CreateNetworkLoadBalancerRequest, dict):
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
        if not isinstance(other, CreateNetworkLoadBalancerRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateNetworkLoadBalancerRequest):
            return True

        return self.to_dict() != other.to_dict()
