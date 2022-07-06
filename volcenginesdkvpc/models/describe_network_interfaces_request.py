# coding: utf-8

"""
    vpc

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeNetworkInterfacesRequest(object):
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
        'instance_id': 'str',
        'network_interface_ids': 'list[str]',
        'network_interface_name': 'str',
        'page_number': 'int',
        'page_size': 'int',
        'primary_ip_addresses': 'list[str]',
        'private_ip_addresses': 'list[str]',
        'security_group_id': 'str',
        'status': 'str',
        'subnet_id': 'str',
        'type': 'str',
        'vpc_id': 'str',
        'zone_id': 'str'
    }

    attribute_map = {
        'instance_id': 'InstanceId',
        'network_interface_ids': 'NetworkInterfaceIds',
        'network_interface_name': 'NetworkInterfaceName',
        'page_number': 'PageNumber',
        'page_size': 'PageSize',
        'primary_ip_addresses': 'PrimaryIpAddresses',
        'private_ip_addresses': 'PrivateIpAddresses',
        'security_group_id': 'SecurityGroupId',
        'status': 'Status',
        'subnet_id': 'SubnetId',
        'type': 'Type',
        'vpc_id': 'VpcId',
        'zone_id': 'ZoneId'
    }

    def __init__(self, instance_id=None, network_interface_ids=None, network_interface_name=None, page_number=None, page_size=None, primary_ip_addresses=None, private_ip_addresses=None, security_group_id=None, status=None, subnet_id=None, type=None, vpc_id=None, zone_id=None, _configuration=None):  # noqa: E501
        """DescribeNetworkInterfacesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._instance_id = None
        self._network_interface_ids = None
        self._network_interface_name = None
        self._page_number = None
        self._page_size = None
        self._primary_ip_addresses = None
        self._private_ip_addresses = None
        self._security_group_id = None
        self._status = None
        self._subnet_id = None
        self._type = None
        self._vpc_id = None
        self._zone_id = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if network_interface_ids is not None:
            self.network_interface_ids = network_interface_ids
        if network_interface_name is not None:
            self.network_interface_name = network_interface_name
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if primary_ip_addresses is not None:
            self.primary_ip_addresses = primary_ip_addresses
        if private_ip_addresses is not None:
            self.private_ip_addresses = private_ip_addresses
        if security_group_id is not None:
            self.security_group_id = security_group_id
        if status is not None:
            self.status = status
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if type is not None:
            self.type = type
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if zone_id is not None:
            self.zone_id = zone_id

    @property
    def instance_id(self):
        """Gets the instance_id of this DescribeNetworkInterfacesRequest.  # noqa: E501


        :return: The instance_id of this DescribeNetworkInterfacesRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this DescribeNetworkInterfacesRequest.


        :param instance_id: The instance_id of this DescribeNetworkInterfacesRequest.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def network_interface_ids(self):
        """Gets the network_interface_ids of this DescribeNetworkInterfacesRequest.  # noqa: E501


        :return: The network_interface_ids of this DescribeNetworkInterfacesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._network_interface_ids

    @network_interface_ids.setter
    def network_interface_ids(self, network_interface_ids):
        """Sets the network_interface_ids of this DescribeNetworkInterfacesRequest.


        :param network_interface_ids: The network_interface_ids of this DescribeNetworkInterfacesRequest.  # noqa: E501
        :type: list[str]
        """

        self._network_interface_ids = network_interface_ids

    @property
    def network_interface_name(self):
        """Gets the network_interface_name of this DescribeNetworkInterfacesRequest.  # noqa: E501


        :return: The network_interface_name of this DescribeNetworkInterfacesRequest.  # noqa: E501
        :rtype: str
        """
        return self._network_interface_name

    @network_interface_name.setter
    def network_interface_name(self, network_interface_name):
        """Sets the network_interface_name of this DescribeNetworkInterfacesRequest.


        :param network_interface_name: The network_interface_name of this DescribeNetworkInterfacesRequest.  # noqa: E501
        :type: str
        """

        self._network_interface_name = network_interface_name

    @property
    def page_number(self):
        """Gets the page_number of this DescribeNetworkInterfacesRequest.  # noqa: E501


        :return: The page_number of this DescribeNetworkInterfacesRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this DescribeNetworkInterfacesRequest.


        :param page_number: The page_number of this DescribeNetworkInterfacesRequest.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this DescribeNetworkInterfacesRequest.  # noqa: E501


        :return: The page_size of this DescribeNetworkInterfacesRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this DescribeNetworkInterfacesRequest.


        :param page_size: The page_size of this DescribeNetworkInterfacesRequest.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                page_size is not None and page_size > 100):  # noqa: E501
            raise ValueError("Invalid value for `page_size`, must be a value less than or equal to `100`")  # noqa: E501

        self._page_size = page_size

    @property
    def primary_ip_addresses(self):
        """Gets the primary_ip_addresses of this DescribeNetworkInterfacesRequest.  # noqa: E501


        :return: The primary_ip_addresses of this DescribeNetworkInterfacesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._primary_ip_addresses

    @primary_ip_addresses.setter
    def primary_ip_addresses(self, primary_ip_addresses):
        """Sets the primary_ip_addresses of this DescribeNetworkInterfacesRequest.


        :param primary_ip_addresses: The primary_ip_addresses of this DescribeNetworkInterfacesRequest.  # noqa: E501
        :type: list[str]
        """

        self._primary_ip_addresses = primary_ip_addresses

    @property
    def private_ip_addresses(self):
        """Gets the private_ip_addresses of this DescribeNetworkInterfacesRequest.  # noqa: E501


        :return: The private_ip_addresses of this DescribeNetworkInterfacesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._private_ip_addresses

    @private_ip_addresses.setter
    def private_ip_addresses(self, private_ip_addresses):
        """Sets the private_ip_addresses of this DescribeNetworkInterfacesRequest.


        :param private_ip_addresses: The private_ip_addresses of this DescribeNetworkInterfacesRequest.  # noqa: E501
        :type: list[str]
        """

        self._private_ip_addresses = private_ip_addresses

    @property
    def security_group_id(self):
        """Gets the security_group_id of this DescribeNetworkInterfacesRequest.  # noqa: E501


        :return: The security_group_id of this DescribeNetworkInterfacesRequest.  # noqa: E501
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this DescribeNetworkInterfacesRequest.


        :param security_group_id: The security_group_id of this DescribeNetworkInterfacesRequest.  # noqa: E501
        :type: str
        """

        self._security_group_id = security_group_id

    @property
    def status(self):
        """Gets the status of this DescribeNetworkInterfacesRequest.  # noqa: E501


        :return: The status of this DescribeNetworkInterfacesRequest.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DescribeNetworkInterfacesRequest.


        :param status: The status of this DescribeNetworkInterfacesRequest.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def subnet_id(self):
        """Gets the subnet_id of this DescribeNetworkInterfacesRequest.  # noqa: E501


        :return: The subnet_id of this DescribeNetworkInterfacesRequest.  # noqa: E501
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this DescribeNetworkInterfacesRequest.


        :param subnet_id: The subnet_id of this DescribeNetworkInterfacesRequest.  # noqa: E501
        :type: str
        """

        self._subnet_id = subnet_id

    @property
    def type(self):
        """Gets the type of this DescribeNetworkInterfacesRequest.  # noqa: E501


        :return: The type of this DescribeNetworkInterfacesRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DescribeNetworkInterfacesRequest.


        :param type: The type of this DescribeNetworkInterfacesRequest.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def vpc_id(self):
        """Gets the vpc_id of this DescribeNetworkInterfacesRequest.  # noqa: E501


        :return: The vpc_id of this DescribeNetworkInterfacesRequest.  # noqa: E501
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this DescribeNetworkInterfacesRequest.


        :param vpc_id: The vpc_id of this DescribeNetworkInterfacesRequest.  # noqa: E501
        :type: str
        """

        self._vpc_id = vpc_id

    @property
    def zone_id(self):
        """Gets the zone_id of this DescribeNetworkInterfacesRequest.  # noqa: E501


        :return: The zone_id of this DescribeNetworkInterfacesRequest.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this DescribeNetworkInterfacesRequest.


        :param zone_id: The zone_id of this DescribeNetworkInterfacesRequest.  # noqa: E501
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
        if issubclass(DescribeNetworkInterfacesRequest, dict):
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
        if not isinstance(other, DescribeNetworkInterfacesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeNetworkInterfacesRequest):
            return True

        return self.to_dict() != other.to_dict()
