# coding: utf-8

"""
    privatelink

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ZoneForDescribeVpcEndpointConnectionsOutput(object):
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
        'network_interface_ip': 'str',
        'network_interface_id': 'str',
        'network_interface_ipv6': 'str',
        'resource_id': 'str',
        'service_status': 'str',
        'subnet_id': 'str',
        'zone_domain': 'str',
        'zone_id': 'str',
        'zone_status': 'str'
    }

    attribute_map = {
        'network_interface_ip': 'NetworkInterfaceIP',
        'network_interface_id': 'NetworkInterfaceId',
        'network_interface_ipv6': 'NetworkInterfaceIpv6',
        'resource_id': 'ResourceId',
        'service_status': 'ServiceStatus',
        'subnet_id': 'SubnetId',
        'zone_domain': 'ZoneDomain',
        'zone_id': 'ZoneId',
        'zone_status': 'ZoneStatus'
    }

    def __init__(self, network_interface_ip=None, network_interface_id=None, network_interface_ipv6=None, resource_id=None, service_status=None, subnet_id=None, zone_domain=None, zone_id=None, zone_status=None, _configuration=None):  # noqa: E501
        """ZoneForDescribeVpcEndpointConnectionsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._network_interface_ip = None
        self._network_interface_id = None
        self._network_interface_ipv6 = None
        self._resource_id = None
        self._service_status = None
        self._subnet_id = None
        self._zone_domain = None
        self._zone_id = None
        self._zone_status = None
        self.discriminator = None

        if network_interface_ip is not None:
            self.network_interface_ip = network_interface_ip
        if network_interface_id is not None:
            self.network_interface_id = network_interface_id
        if network_interface_ipv6 is not None:
            self.network_interface_ipv6 = network_interface_ipv6
        if resource_id is not None:
            self.resource_id = resource_id
        if service_status is not None:
            self.service_status = service_status
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if zone_domain is not None:
            self.zone_domain = zone_domain
        if zone_id is not None:
            self.zone_id = zone_id
        if zone_status is not None:
            self.zone_status = zone_status

    @property
    def network_interface_ip(self):
        """Gets the network_interface_ip of this ZoneForDescribeVpcEndpointConnectionsOutput.  # noqa: E501


        :return: The network_interface_ip of this ZoneForDescribeVpcEndpointConnectionsOutput.  # noqa: E501
        :rtype: str
        """
        return self._network_interface_ip

    @network_interface_ip.setter
    def network_interface_ip(self, network_interface_ip):
        """Sets the network_interface_ip of this ZoneForDescribeVpcEndpointConnectionsOutput.


        :param network_interface_ip: The network_interface_ip of this ZoneForDescribeVpcEndpointConnectionsOutput.  # noqa: E501
        :type: str
        """

        self._network_interface_ip = network_interface_ip

    @property
    def network_interface_id(self):
        """Gets the network_interface_id of this ZoneForDescribeVpcEndpointConnectionsOutput.  # noqa: E501


        :return: The network_interface_id of this ZoneForDescribeVpcEndpointConnectionsOutput.  # noqa: E501
        :rtype: str
        """
        return self._network_interface_id

    @network_interface_id.setter
    def network_interface_id(self, network_interface_id):
        """Sets the network_interface_id of this ZoneForDescribeVpcEndpointConnectionsOutput.


        :param network_interface_id: The network_interface_id of this ZoneForDescribeVpcEndpointConnectionsOutput.  # noqa: E501
        :type: str
        """

        self._network_interface_id = network_interface_id

    @property
    def network_interface_ipv6(self):
        """Gets the network_interface_ipv6 of this ZoneForDescribeVpcEndpointConnectionsOutput.  # noqa: E501


        :return: The network_interface_ipv6 of this ZoneForDescribeVpcEndpointConnectionsOutput.  # noqa: E501
        :rtype: str
        """
        return self._network_interface_ipv6

    @network_interface_ipv6.setter
    def network_interface_ipv6(self, network_interface_ipv6):
        """Sets the network_interface_ipv6 of this ZoneForDescribeVpcEndpointConnectionsOutput.


        :param network_interface_ipv6: The network_interface_ipv6 of this ZoneForDescribeVpcEndpointConnectionsOutput.  # noqa: E501
        :type: str
        """

        self._network_interface_ipv6 = network_interface_ipv6

    @property
    def resource_id(self):
        """Gets the resource_id of this ZoneForDescribeVpcEndpointConnectionsOutput.  # noqa: E501


        :return: The resource_id of this ZoneForDescribeVpcEndpointConnectionsOutput.  # noqa: E501
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ZoneForDescribeVpcEndpointConnectionsOutput.


        :param resource_id: The resource_id of this ZoneForDescribeVpcEndpointConnectionsOutput.  # noqa: E501
        :type: str
        """

        self._resource_id = resource_id

    @property
    def service_status(self):
        """Gets the service_status of this ZoneForDescribeVpcEndpointConnectionsOutput.  # noqa: E501


        :return: The service_status of this ZoneForDescribeVpcEndpointConnectionsOutput.  # noqa: E501
        :rtype: str
        """
        return self._service_status

    @service_status.setter
    def service_status(self, service_status):
        """Sets the service_status of this ZoneForDescribeVpcEndpointConnectionsOutput.


        :param service_status: The service_status of this ZoneForDescribeVpcEndpointConnectionsOutput.  # noqa: E501
        :type: str
        """

        self._service_status = service_status

    @property
    def subnet_id(self):
        """Gets the subnet_id of this ZoneForDescribeVpcEndpointConnectionsOutput.  # noqa: E501


        :return: The subnet_id of this ZoneForDescribeVpcEndpointConnectionsOutput.  # noqa: E501
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this ZoneForDescribeVpcEndpointConnectionsOutput.


        :param subnet_id: The subnet_id of this ZoneForDescribeVpcEndpointConnectionsOutput.  # noqa: E501
        :type: str
        """

        self._subnet_id = subnet_id

    @property
    def zone_domain(self):
        """Gets the zone_domain of this ZoneForDescribeVpcEndpointConnectionsOutput.  # noqa: E501


        :return: The zone_domain of this ZoneForDescribeVpcEndpointConnectionsOutput.  # noqa: E501
        :rtype: str
        """
        return self._zone_domain

    @zone_domain.setter
    def zone_domain(self, zone_domain):
        """Sets the zone_domain of this ZoneForDescribeVpcEndpointConnectionsOutput.


        :param zone_domain: The zone_domain of this ZoneForDescribeVpcEndpointConnectionsOutput.  # noqa: E501
        :type: str
        """

        self._zone_domain = zone_domain

    @property
    def zone_id(self):
        """Gets the zone_id of this ZoneForDescribeVpcEndpointConnectionsOutput.  # noqa: E501


        :return: The zone_id of this ZoneForDescribeVpcEndpointConnectionsOutput.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this ZoneForDescribeVpcEndpointConnectionsOutput.


        :param zone_id: The zone_id of this ZoneForDescribeVpcEndpointConnectionsOutput.  # noqa: E501
        :type: str
        """

        self._zone_id = zone_id

    @property
    def zone_status(self):
        """Gets the zone_status of this ZoneForDescribeVpcEndpointConnectionsOutput.  # noqa: E501


        :return: The zone_status of this ZoneForDescribeVpcEndpointConnectionsOutput.  # noqa: E501
        :rtype: str
        """
        return self._zone_status

    @zone_status.setter
    def zone_status(self, zone_status):
        """Sets the zone_status of this ZoneForDescribeVpcEndpointConnectionsOutput.


        :param zone_status: The zone_status of this ZoneForDescribeVpcEndpointConnectionsOutput.  # noqa: E501
        :type: str
        """

        self._zone_status = zone_status

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
        if issubclass(ZoneForDescribeVpcEndpointConnectionsOutput, dict):
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
        if not isinstance(other, ZoneForDescribeVpcEndpointConnectionsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ZoneForDescribeVpcEndpointConnectionsOutput):
            return True

        return self.to_dict() != other.to_dict()
