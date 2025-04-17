# coding: utf-8

"""
    edx

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class BGPPeerForDescribeVirtualInterfaceBGPPeerOutput(object):
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
        'create_time': 'str',
        'enabled': 'bool',
        'local_ip': 'str',
        'md5': 'str',
        'peer_asn': 'int',
        'peer_ip': 'str',
        'vif_instance_id': 'str'
    }

    attribute_map = {
        'create_time': 'CreateTime',
        'enabled': 'Enabled',
        'local_ip': 'LocalIP',
        'md5': 'MD5',
        'peer_asn': 'PeerASN',
        'peer_ip': 'PeerIP',
        'vif_instance_id': 'VIFInstanceId'
    }

    def __init__(self, create_time=None, enabled=None, local_ip=None, md5=None, peer_asn=None, peer_ip=None, vif_instance_id=None, _configuration=None):  # noqa: E501
        """BGPPeerForDescribeVirtualInterfaceBGPPeerOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._create_time = None
        self._enabled = None
        self._local_ip = None
        self._md5 = None
        self._peer_asn = None
        self._peer_ip = None
        self._vif_instance_id = None
        self.discriminator = None

        if create_time is not None:
            self.create_time = create_time
        if enabled is not None:
            self.enabled = enabled
        if local_ip is not None:
            self.local_ip = local_ip
        if md5 is not None:
            self.md5 = md5
        if peer_asn is not None:
            self.peer_asn = peer_asn
        if peer_ip is not None:
            self.peer_ip = peer_ip
        if vif_instance_id is not None:
            self.vif_instance_id = vif_instance_id

    @property
    def create_time(self):
        """Gets the create_time of this BGPPeerForDescribeVirtualInterfaceBGPPeerOutput.  # noqa: E501


        :return: The create_time of this BGPPeerForDescribeVirtualInterfaceBGPPeerOutput.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this BGPPeerForDescribeVirtualInterfaceBGPPeerOutput.


        :param create_time: The create_time of this BGPPeerForDescribeVirtualInterfaceBGPPeerOutput.  # noqa: E501
        :type: str
        """

        self._create_time = create_time

    @property
    def enabled(self):
        """Gets the enabled of this BGPPeerForDescribeVirtualInterfaceBGPPeerOutput.  # noqa: E501


        :return: The enabled of this BGPPeerForDescribeVirtualInterfaceBGPPeerOutput.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this BGPPeerForDescribeVirtualInterfaceBGPPeerOutput.


        :param enabled: The enabled of this BGPPeerForDescribeVirtualInterfaceBGPPeerOutput.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def local_ip(self):
        """Gets the local_ip of this BGPPeerForDescribeVirtualInterfaceBGPPeerOutput.  # noqa: E501


        :return: The local_ip of this BGPPeerForDescribeVirtualInterfaceBGPPeerOutput.  # noqa: E501
        :rtype: str
        """
        return self._local_ip

    @local_ip.setter
    def local_ip(self, local_ip):
        """Sets the local_ip of this BGPPeerForDescribeVirtualInterfaceBGPPeerOutput.


        :param local_ip: The local_ip of this BGPPeerForDescribeVirtualInterfaceBGPPeerOutput.  # noqa: E501
        :type: str
        """

        self._local_ip = local_ip

    @property
    def md5(self):
        """Gets the md5 of this BGPPeerForDescribeVirtualInterfaceBGPPeerOutput.  # noqa: E501


        :return: The md5 of this BGPPeerForDescribeVirtualInterfaceBGPPeerOutput.  # noqa: E501
        :rtype: str
        """
        return self._md5

    @md5.setter
    def md5(self, md5):
        """Sets the md5 of this BGPPeerForDescribeVirtualInterfaceBGPPeerOutput.


        :param md5: The md5 of this BGPPeerForDescribeVirtualInterfaceBGPPeerOutput.  # noqa: E501
        :type: str
        """

        self._md5 = md5

    @property
    def peer_asn(self):
        """Gets the peer_asn of this BGPPeerForDescribeVirtualInterfaceBGPPeerOutput.  # noqa: E501


        :return: The peer_asn of this BGPPeerForDescribeVirtualInterfaceBGPPeerOutput.  # noqa: E501
        :rtype: int
        """
        return self._peer_asn

    @peer_asn.setter
    def peer_asn(self, peer_asn):
        """Sets the peer_asn of this BGPPeerForDescribeVirtualInterfaceBGPPeerOutput.


        :param peer_asn: The peer_asn of this BGPPeerForDescribeVirtualInterfaceBGPPeerOutput.  # noqa: E501
        :type: int
        """

        self._peer_asn = peer_asn

    @property
    def peer_ip(self):
        """Gets the peer_ip of this BGPPeerForDescribeVirtualInterfaceBGPPeerOutput.  # noqa: E501


        :return: The peer_ip of this BGPPeerForDescribeVirtualInterfaceBGPPeerOutput.  # noqa: E501
        :rtype: str
        """
        return self._peer_ip

    @peer_ip.setter
    def peer_ip(self, peer_ip):
        """Sets the peer_ip of this BGPPeerForDescribeVirtualInterfaceBGPPeerOutput.


        :param peer_ip: The peer_ip of this BGPPeerForDescribeVirtualInterfaceBGPPeerOutput.  # noqa: E501
        :type: str
        """

        self._peer_ip = peer_ip

    @property
    def vif_instance_id(self):
        """Gets the vif_instance_id of this BGPPeerForDescribeVirtualInterfaceBGPPeerOutput.  # noqa: E501


        :return: The vif_instance_id of this BGPPeerForDescribeVirtualInterfaceBGPPeerOutput.  # noqa: E501
        :rtype: str
        """
        return self._vif_instance_id

    @vif_instance_id.setter
    def vif_instance_id(self, vif_instance_id):
        """Sets the vif_instance_id of this BGPPeerForDescribeVirtualInterfaceBGPPeerOutput.


        :param vif_instance_id: The vif_instance_id of this BGPPeerForDescribeVirtualInterfaceBGPPeerOutput.  # noqa: E501
        :type: str
        """

        self._vif_instance_id = vif_instance_id

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
        if issubclass(BGPPeerForDescribeVirtualInterfaceBGPPeerOutput, dict):
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
        if not isinstance(other, BGPPeerForDescribeVirtualInterfaceBGPPeerOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BGPPeerForDescribeVirtualInterfaceBGPPeerOutput):
            return True

        return self.to_dict() != other.to_dict()
