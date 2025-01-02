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


class BgpInfoForDescribeVpnConnectionAttributesOutput(object):
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
        'local_asn': 'int',
        'local_bgp_ip': 'str',
        'peer_asn': 'str',
        'peer_bgp_ip': 'str',
        'session_status': 'str',
        'tunnel_cidr': 'str'
    }

    attribute_map = {
        'enable_bgp': 'EnableBgp',
        'local_asn': 'LocalAsn',
        'local_bgp_ip': 'LocalBgpIp',
        'peer_asn': 'PeerAsn',
        'peer_bgp_ip': 'PeerBgpIp',
        'session_status': 'SessionStatus',
        'tunnel_cidr': 'TunnelCidr'
    }

    def __init__(self, enable_bgp=None, local_asn=None, local_bgp_ip=None, peer_asn=None, peer_bgp_ip=None, session_status=None, tunnel_cidr=None, _configuration=None):  # noqa: E501
        """BgpInfoForDescribeVpnConnectionAttributesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._enable_bgp = None
        self._local_asn = None
        self._local_bgp_ip = None
        self._peer_asn = None
        self._peer_bgp_ip = None
        self._session_status = None
        self._tunnel_cidr = None
        self.discriminator = None

        if enable_bgp is not None:
            self.enable_bgp = enable_bgp
        if local_asn is not None:
            self.local_asn = local_asn
        if local_bgp_ip is not None:
            self.local_bgp_ip = local_bgp_ip
        if peer_asn is not None:
            self.peer_asn = peer_asn
        if peer_bgp_ip is not None:
            self.peer_bgp_ip = peer_bgp_ip
        if session_status is not None:
            self.session_status = session_status
        if tunnel_cidr is not None:
            self.tunnel_cidr = tunnel_cidr

    @property
    def enable_bgp(self):
        """Gets the enable_bgp of this BgpInfoForDescribeVpnConnectionAttributesOutput.  # noqa: E501


        :return: The enable_bgp of this BgpInfoForDescribeVpnConnectionAttributesOutput.  # noqa: E501
        :rtype: bool
        """
        return self._enable_bgp

    @enable_bgp.setter
    def enable_bgp(self, enable_bgp):
        """Sets the enable_bgp of this BgpInfoForDescribeVpnConnectionAttributesOutput.


        :param enable_bgp: The enable_bgp of this BgpInfoForDescribeVpnConnectionAttributesOutput.  # noqa: E501
        :type: bool
        """

        self._enable_bgp = enable_bgp

    @property
    def local_asn(self):
        """Gets the local_asn of this BgpInfoForDescribeVpnConnectionAttributesOutput.  # noqa: E501


        :return: The local_asn of this BgpInfoForDescribeVpnConnectionAttributesOutput.  # noqa: E501
        :rtype: int
        """
        return self._local_asn

    @local_asn.setter
    def local_asn(self, local_asn):
        """Sets the local_asn of this BgpInfoForDescribeVpnConnectionAttributesOutput.


        :param local_asn: The local_asn of this BgpInfoForDescribeVpnConnectionAttributesOutput.  # noqa: E501
        :type: int
        """

        self._local_asn = local_asn

    @property
    def local_bgp_ip(self):
        """Gets the local_bgp_ip of this BgpInfoForDescribeVpnConnectionAttributesOutput.  # noqa: E501


        :return: The local_bgp_ip of this BgpInfoForDescribeVpnConnectionAttributesOutput.  # noqa: E501
        :rtype: str
        """
        return self._local_bgp_ip

    @local_bgp_ip.setter
    def local_bgp_ip(self, local_bgp_ip):
        """Sets the local_bgp_ip of this BgpInfoForDescribeVpnConnectionAttributesOutput.


        :param local_bgp_ip: The local_bgp_ip of this BgpInfoForDescribeVpnConnectionAttributesOutput.  # noqa: E501
        :type: str
        """

        self._local_bgp_ip = local_bgp_ip

    @property
    def peer_asn(self):
        """Gets the peer_asn of this BgpInfoForDescribeVpnConnectionAttributesOutput.  # noqa: E501


        :return: The peer_asn of this BgpInfoForDescribeVpnConnectionAttributesOutput.  # noqa: E501
        :rtype: str
        """
        return self._peer_asn

    @peer_asn.setter
    def peer_asn(self, peer_asn):
        """Sets the peer_asn of this BgpInfoForDescribeVpnConnectionAttributesOutput.


        :param peer_asn: The peer_asn of this BgpInfoForDescribeVpnConnectionAttributesOutput.  # noqa: E501
        :type: str
        """

        self._peer_asn = peer_asn

    @property
    def peer_bgp_ip(self):
        """Gets the peer_bgp_ip of this BgpInfoForDescribeVpnConnectionAttributesOutput.  # noqa: E501


        :return: The peer_bgp_ip of this BgpInfoForDescribeVpnConnectionAttributesOutput.  # noqa: E501
        :rtype: str
        """
        return self._peer_bgp_ip

    @peer_bgp_ip.setter
    def peer_bgp_ip(self, peer_bgp_ip):
        """Sets the peer_bgp_ip of this BgpInfoForDescribeVpnConnectionAttributesOutput.


        :param peer_bgp_ip: The peer_bgp_ip of this BgpInfoForDescribeVpnConnectionAttributesOutput.  # noqa: E501
        :type: str
        """

        self._peer_bgp_ip = peer_bgp_ip

    @property
    def session_status(self):
        """Gets the session_status of this BgpInfoForDescribeVpnConnectionAttributesOutput.  # noqa: E501


        :return: The session_status of this BgpInfoForDescribeVpnConnectionAttributesOutput.  # noqa: E501
        :rtype: str
        """
        return self._session_status

    @session_status.setter
    def session_status(self, session_status):
        """Sets the session_status of this BgpInfoForDescribeVpnConnectionAttributesOutput.


        :param session_status: The session_status of this BgpInfoForDescribeVpnConnectionAttributesOutput.  # noqa: E501
        :type: str
        """

        self._session_status = session_status

    @property
    def tunnel_cidr(self):
        """Gets the tunnel_cidr of this BgpInfoForDescribeVpnConnectionAttributesOutput.  # noqa: E501


        :return: The tunnel_cidr of this BgpInfoForDescribeVpnConnectionAttributesOutput.  # noqa: E501
        :rtype: str
        """
        return self._tunnel_cidr

    @tunnel_cidr.setter
    def tunnel_cidr(self, tunnel_cidr):
        """Sets the tunnel_cidr of this BgpInfoForDescribeVpnConnectionAttributesOutput.


        :param tunnel_cidr: The tunnel_cidr of this BgpInfoForDescribeVpnConnectionAttributesOutput.  # noqa: E501
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
        if issubclass(BgpInfoForDescribeVpnConnectionAttributesOutput, dict):
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
        if not isinstance(other, BgpInfoForDescribeVpnConnectionAttributesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BgpInfoForDescribeVpnConnectionAttributesOutput):
            return True

        return self.to_dict() != other.to_dict()