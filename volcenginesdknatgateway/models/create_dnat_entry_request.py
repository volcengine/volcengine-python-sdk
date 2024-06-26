# coding: utf-8

"""
    natgateway

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class CreateDnatEntryRequest(object):
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
        'dnat_entry_name': 'str',
        'external_ip': 'str',
        'external_port': 'str',
        'internal_ip': 'str',
        'internal_port': 'str',
        'nat_gateway_id': 'str',
        'port_type': 'str',
        'protocol': 'str'
    }

    attribute_map = {
        'dnat_entry_name': 'DnatEntryName',
        'external_ip': 'ExternalIp',
        'external_port': 'ExternalPort',
        'internal_ip': 'InternalIp',
        'internal_port': 'InternalPort',
        'nat_gateway_id': 'NatGatewayId',
        'port_type': 'PortType',
        'protocol': 'Protocol'
    }

    def __init__(self, dnat_entry_name=None, external_ip=None, external_port=None, internal_ip=None, internal_port=None, nat_gateway_id=None, port_type=None, protocol=None, _configuration=None):  # noqa: E501
        """CreateDnatEntryRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._dnat_entry_name = None
        self._external_ip = None
        self._external_port = None
        self._internal_ip = None
        self._internal_port = None
        self._nat_gateway_id = None
        self._port_type = None
        self._protocol = None
        self.discriminator = None

        if dnat_entry_name is not None:
            self.dnat_entry_name = dnat_entry_name
        self.external_ip = external_ip
        self.external_port = external_port
        self.internal_ip = internal_ip
        self.internal_port = internal_port
        self.nat_gateway_id = nat_gateway_id
        if port_type is not None:
            self.port_type = port_type
        self.protocol = protocol

    @property
    def dnat_entry_name(self):
        """Gets the dnat_entry_name of this CreateDnatEntryRequest.  # noqa: E501


        :return: The dnat_entry_name of this CreateDnatEntryRequest.  # noqa: E501
        :rtype: str
        """
        return self._dnat_entry_name

    @dnat_entry_name.setter
    def dnat_entry_name(self, dnat_entry_name):
        """Sets the dnat_entry_name of this CreateDnatEntryRequest.


        :param dnat_entry_name: The dnat_entry_name of this CreateDnatEntryRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                dnat_entry_name is not None and len(dnat_entry_name) > 128):
            raise ValueError("Invalid value for `dnat_entry_name`, length must be less than or equal to `128`")  # noqa: E501
        if (self._configuration.client_side_validation and
                dnat_entry_name is not None and len(dnat_entry_name) < 1):
            raise ValueError("Invalid value for `dnat_entry_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._dnat_entry_name = dnat_entry_name

    @property
    def external_ip(self):
        """Gets the external_ip of this CreateDnatEntryRequest.  # noqa: E501


        :return: The external_ip of this CreateDnatEntryRequest.  # noqa: E501
        :rtype: str
        """
        return self._external_ip

    @external_ip.setter
    def external_ip(self, external_ip):
        """Sets the external_ip of this CreateDnatEntryRequest.


        :param external_ip: The external_ip of this CreateDnatEntryRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and external_ip is None:
            raise ValueError("Invalid value for `external_ip`, must not be `None`")  # noqa: E501

        self._external_ip = external_ip

    @property
    def external_port(self):
        """Gets the external_port of this CreateDnatEntryRequest.  # noqa: E501


        :return: The external_port of this CreateDnatEntryRequest.  # noqa: E501
        :rtype: str
        """
        return self._external_port

    @external_port.setter
    def external_port(self, external_port):
        """Sets the external_port of this CreateDnatEntryRequest.


        :param external_port: The external_port of this CreateDnatEntryRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and external_port is None:
            raise ValueError("Invalid value for `external_port`, must not be `None`")  # noqa: E501

        self._external_port = external_port

    @property
    def internal_ip(self):
        """Gets the internal_ip of this CreateDnatEntryRequest.  # noqa: E501


        :return: The internal_ip of this CreateDnatEntryRequest.  # noqa: E501
        :rtype: str
        """
        return self._internal_ip

    @internal_ip.setter
    def internal_ip(self, internal_ip):
        """Sets the internal_ip of this CreateDnatEntryRequest.


        :param internal_ip: The internal_ip of this CreateDnatEntryRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and internal_ip is None:
            raise ValueError("Invalid value for `internal_ip`, must not be `None`")  # noqa: E501

        self._internal_ip = internal_ip

    @property
    def internal_port(self):
        """Gets the internal_port of this CreateDnatEntryRequest.  # noqa: E501


        :return: The internal_port of this CreateDnatEntryRequest.  # noqa: E501
        :rtype: str
        """
        return self._internal_port

    @internal_port.setter
    def internal_port(self, internal_port):
        """Sets the internal_port of this CreateDnatEntryRequest.


        :param internal_port: The internal_port of this CreateDnatEntryRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and internal_port is None:
            raise ValueError("Invalid value for `internal_port`, must not be `None`")  # noqa: E501

        self._internal_port = internal_port

    @property
    def nat_gateway_id(self):
        """Gets the nat_gateway_id of this CreateDnatEntryRequest.  # noqa: E501


        :return: The nat_gateway_id of this CreateDnatEntryRequest.  # noqa: E501
        :rtype: str
        """
        return self._nat_gateway_id

    @nat_gateway_id.setter
    def nat_gateway_id(self, nat_gateway_id):
        """Sets the nat_gateway_id of this CreateDnatEntryRequest.


        :param nat_gateway_id: The nat_gateway_id of this CreateDnatEntryRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and nat_gateway_id is None:
            raise ValueError("Invalid value for `nat_gateway_id`, must not be `None`")  # noqa: E501

        self._nat_gateway_id = nat_gateway_id

    @property
    def port_type(self):
        """Gets the port_type of this CreateDnatEntryRequest.  # noqa: E501


        :return: The port_type of this CreateDnatEntryRequest.  # noqa: E501
        :rtype: str
        """
        return self._port_type

    @port_type.setter
    def port_type(self, port_type):
        """Sets the port_type of this CreateDnatEntryRequest.


        :param port_type: The port_type of this CreateDnatEntryRequest.  # noqa: E501
        :type: str
        """

        self._port_type = port_type

    @property
    def protocol(self):
        """Gets the protocol of this CreateDnatEntryRequest.  # noqa: E501


        :return: The protocol of this CreateDnatEntryRequest.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this CreateDnatEntryRequest.


        :param protocol: The protocol of this CreateDnatEntryRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and protocol is None:
            raise ValueError("Invalid value for `protocol`, must not be `None`")  # noqa: E501

        self._protocol = protocol

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
        if issubclass(CreateDnatEntryRequest, dict):
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
        if not isinstance(other, CreateDnatEntryRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateDnatEntryRequest):
            return True

        return self.to_dict() != other.to_dict()
