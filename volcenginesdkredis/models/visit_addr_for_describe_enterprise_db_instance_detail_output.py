# coding: utf-8

"""
    redis

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class VisitAddrForDescribeEnterpriseDBInstanceDetailOutput(object):
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
        'addr_type': 'str',
        'eip_id': 'str',
        'ip_address': 'str',
        'port': 'str',
        'vip': 'str'
    }

    attribute_map = {
        'addr_type': 'AddrType',
        'eip_id': 'EipId',
        'ip_address': 'IPAddress',
        'port': 'Port',
        'vip': 'VIP'
    }

    def __init__(self, addr_type=None, eip_id=None, ip_address=None, port=None, vip=None, _configuration=None):  # noqa: E501
        """VisitAddrForDescribeEnterpriseDBInstanceDetailOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._addr_type = None
        self._eip_id = None
        self._ip_address = None
        self._port = None
        self._vip = None
        self.discriminator = None

        if addr_type is not None:
            self.addr_type = addr_type
        if eip_id is not None:
            self.eip_id = eip_id
        if ip_address is not None:
            self.ip_address = ip_address
        if port is not None:
            self.port = port
        if vip is not None:
            self.vip = vip

    @property
    def addr_type(self):
        """Gets the addr_type of this VisitAddrForDescribeEnterpriseDBInstanceDetailOutput.  # noqa: E501


        :return: The addr_type of this VisitAddrForDescribeEnterpriseDBInstanceDetailOutput.  # noqa: E501
        :rtype: str
        """
        return self._addr_type

    @addr_type.setter
    def addr_type(self, addr_type):
        """Sets the addr_type of this VisitAddrForDescribeEnterpriseDBInstanceDetailOutput.


        :param addr_type: The addr_type of this VisitAddrForDescribeEnterpriseDBInstanceDetailOutput.  # noqa: E501
        :type: str
        """

        self._addr_type = addr_type

    @property
    def eip_id(self):
        """Gets the eip_id of this VisitAddrForDescribeEnterpriseDBInstanceDetailOutput.  # noqa: E501


        :return: The eip_id of this VisitAddrForDescribeEnterpriseDBInstanceDetailOutput.  # noqa: E501
        :rtype: str
        """
        return self._eip_id

    @eip_id.setter
    def eip_id(self, eip_id):
        """Sets the eip_id of this VisitAddrForDescribeEnterpriseDBInstanceDetailOutput.


        :param eip_id: The eip_id of this VisitAddrForDescribeEnterpriseDBInstanceDetailOutput.  # noqa: E501
        :type: str
        """

        self._eip_id = eip_id

    @property
    def ip_address(self):
        """Gets the ip_address of this VisitAddrForDescribeEnterpriseDBInstanceDetailOutput.  # noqa: E501


        :return: The ip_address of this VisitAddrForDescribeEnterpriseDBInstanceDetailOutput.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this VisitAddrForDescribeEnterpriseDBInstanceDetailOutput.


        :param ip_address: The ip_address of this VisitAddrForDescribeEnterpriseDBInstanceDetailOutput.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

    @property
    def port(self):
        """Gets the port of this VisitAddrForDescribeEnterpriseDBInstanceDetailOutput.  # noqa: E501


        :return: The port of this VisitAddrForDescribeEnterpriseDBInstanceDetailOutput.  # noqa: E501
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this VisitAddrForDescribeEnterpriseDBInstanceDetailOutput.


        :param port: The port of this VisitAddrForDescribeEnterpriseDBInstanceDetailOutput.  # noqa: E501
        :type: str
        """

        self._port = port

    @property
    def vip(self):
        """Gets the vip of this VisitAddrForDescribeEnterpriseDBInstanceDetailOutput.  # noqa: E501


        :return: The vip of this VisitAddrForDescribeEnterpriseDBInstanceDetailOutput.  # noqa: E501
        :rtype: str
        """
        return self._vip

    @vip.setter
    def vip(self, vip):
        """Sets the vip of this VisitAddrForDescribeEnterpriseDBInstanceDetailOutput.


        :param vip: The vip of this VisitAddrForDescribeEnterpriseDBInstanceDetailOutput.  # noqa: E501
        :type: str
        """

        self._vip = vip

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
        if issubclass(VisitAddrForDescribeEnterpriseDBInstanceDetailOutput, dict):
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
        if not isinstance(other, VisitAddrForDescribeEnterpriseDBInstanceDetailOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VisitAddrForDescribeEnterpriseDBInstanceDetailOutput):
            return True

        return self.to_dict() != other.to_dict()
