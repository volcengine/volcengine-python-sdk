# coding: utf-8

"""
    vpn

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class BgpConfigForCreateVpnConnectionInput(object):
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
        'enable_bgp': 'bool',
        'local_bgp_ip': 'str',
        'tunnel_cidr': 'str'
    }

    attribute_map = {
        'enable_bgp': 'EnableBgp',
        'local_bgp_ip': 'LocalBgpIp',
        'tunnel_cidr': 'TunnelCidr'
    }

    def __init__(self, enable_bgp=None, local_bgp_ip=None, tunnel_cidr=None, _configuration=None):  # noqa: E501
        """BgpConfigForCreateVpnConnectionInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._enable_bgp = None
        self._local_bgp_ip = None
        self._tunnel_cidr = None
        self.discriminator = None

        self.enable_bgp = enable_bgp
        if local_bgp_ip is not None:
            self.local_bgp_ip = local_bgp_ip
        if tunnel_cidr is not None:
            self.tunnel_cidr = tunnel_cidr

    @property
    def enable_bgp(self):
        """Gets the enable_bgp of this BgpConfigForCreateVpnConnectionInput.  # noqa: E501


        :return: The enable_bgp of this BgpConfigForCreateVpnConnectionInput.  # noqa: E501
        :rtype: bool
        """
        return self._enable_bgp

    @enable_bgp.setter
    def enable_bgp(self, enable_bgp):
        """Sets the enable_bgp of this BgpConfigForCreateVpnConnectionInput.


        :param enable_bgp: The enable_bgp of this BgpConfigForCreateVpnConnectionInput.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and enable_bgp is None:
            raise ValueError("Invalid value for `enable_bgp`, must not be `None`")  # noqa: E501

        self._enable_bgp = enable_bgp

    @property
    def local_bgp_ip(self):
        """Gets the local_bgp_ip of this BgpConfigForCreateVpnConnectionInput.  # noqa: E501


        :return: The local_bgp_ip of this BgpConfigForCreateVpnConnectionInput.  # noqa: E501
        :rtype: str
        """
        return self._local_bgp_ip

    @local_bgp_ip.setter
    def local_bgp_ip(self, local_bgp_ip):
        """Sets the local_bgp_ip of this BgpConfigForCreateVpnConnectionInput.


        :param local_bgp_ip: The local_bgp_ip of this BgpConfigForCreateVpnConnectionInput.  # noqa: E501
        :type: str
        """

        self._local_bgp_ip = local_bgp_ip

    @property
    def tunnel_cidr(self):
        """Gets the tunnel_cidr of this BgpConfigForCreateVpnConnectionInput.  # noqa: E501


        :return: The tunnel_cidr of this BgpConfigForCreateVpnConnectionInput.  # noqa: E501
        :rtype: str
        """
        return self._tunnel_cidr

    @tunnel_cidr.setter
    def tunnel_cidr(self, tunnel_cidr):
        """Sets the tunnel_cidr of this BgpConfigForCreateVpnConnectionInput.


        :param tunnel_cidr: The tunnel_cidr of this BgpConfigForCreateVpnConnectionInput.  # noqa: E501
        :type: str
        """

        self._tunnel_cidr = tunnel_cidr

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
        if issubclass(BgpConfigForCreateVpnConnectionInput, dict):
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
        if not isinstance(other, BgpConfigForCreateVpnConnectionInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BgpConfigForCreateVpnConnectionInput):
            return True

        return self.to_dict() != other.to_dict()