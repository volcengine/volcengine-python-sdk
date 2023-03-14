# coding: utf-8

"""
    directconnect

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class CreateBgpPeerRequest(object):
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
        'auth_key': 'str',
        'bgp_peer_name': 'str',
        'description': 'str',
        'remote_asn': 'int',
        'virtual_interface_id': 'str'
    }

    attribute_map = {
        'auth_key': 'AuthKey',
        'bgp_peer_name': 'BgpPeerName',
        'description': 'Description',
        'remote_asn': 'RemoteAsn',
        'virtual_interface_id': 'VirtualInterfaceId'
    }

    def __init__(self, auth_key=None, bgp_peer_name=None, description=None, remote_asn=None, virtual_interface_id=None, _configuration=None):  # noqa: E501
        """CreateBgpPeerRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._auth_key = None
        self._bgp_peer_name = None
        self._description = None
        self._remote_asn = None
        self._virtual_interface_id = None
        self.discriminator = None

        if auth_key is not None:
            self.auth_key = auth_key
        if bgp_peer_name is not None:
            self.bgp_peer_name = bgp_peer_name
        if description is not None:
            self.description = description
        self.remote_asn = remote_asn
        self.virtual_interface_id = virtual_interface_id

    @property
    def auth_key(self):
        """Gets the auth_key of this CreateBgpPeerRequest.  # noqa: E501


        :return: The auth_key of this CreateBgpPeerRequest.  # noqa: E501
        :rtype: str
        """
        return self._auth_key

    @auth_key.setter
    def auth_key(self, auth_key):
        """Sets the auth_key of this CreateBgpPeerRequest.


        :param auth_key: The auth_key of this CreateBgpPeerRequest.  # noqa: E501
        :type: str
        """

        self._auth_key = auth_key

    @property
    def bgp_peer_name(self):
        """Gets the bgp_peer_name of this CreateBgpPeerRequest.  # noqa: E501


        :return: The bgp_peer_name of this CreateBgpPeerRequest.  # noqa: E501
        :rtype: str
        """
        return self._bgp_peer_name

    @bgp_peer_name.setter
    def bgp_peer_name(self, bgp_peer_name):
        """Sets the bgp_peer_name of this CreateBgpPeerRequest.


        :param bgp_peer_name: The bgp_peer_name of this CreateBgpPeerRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                bgp_peer_name is not None and len(bgp_peer_name) > 128):
            raise ValueError("Invalid value for `bgp_peer_name`, length must be less than or equal to `128`")  # noqa: E501
        if (self._configuration.client_side_validation and
                bgp_peer_name is not None and len(bgp_peer_name) < 1):
            raise ValueError("Invalid value for `bgp_peer_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._bgp_peer_name = bgp_peer_name

    @property
    def description(self):
        """Gets the description of this CreateBgpPeerRequest.  # noqa: E501


        :return: The description of this CreateBgpPeerRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateBgpPeerRequest.


        :param description: The description of this CreateBgpPeerRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                description is not None and len(description) > 255):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                description is not None and len(description) < 1):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `1`")  # noqa: E501

        self._description = description

    @property
    def remote_asn(self):
        """Gets the remote_asn of this CreateBgpPeerRequest.  # noqa: E501


        :return: The remote_asn of this CreateBgpPeerRequest.  # noqa: E501
        :rtype: int
        """
        return self._remote_asn

    @remote_asn.setter
    def remote_asn(self, remote_asn):
        """Sets the remote_asn of this CreateBgpPeerRequest.


        :param remote_asn: The remote_asn of this CreateBgpPeerRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and remote_asn is None:
            raise ValueError("Invalid value for `remote_asn`, must not be `None`")  # noqa: E501

        self._remote_asn = remote_asn

    @property
    def virtual_interface_id(self):
        """Gets the virtual_interface_id of this CreateBgpPeerRequest.  # noqa: E501


        :return: The virtual_interface_id of this CreateBgpPeerRequest.  # noqa: E501
        :rtype: str
        """
        return self._virtual_interface_id

    @virtual_interface_id.setter
    def virtual_interface_id(self, virtual_interface_id):
        """Sets the virtual_interface_id of this CreateBgpPeerRequest.


        :param virtual_interface_id: The virtual_interface_id of this CreateBgpPeerRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and virtual_interface_id is None:
            raise ValueError("Invalid value for `virtual_interface_id`, must not be `None`")  # noqa: E501

        self._virtual_interface_id = virtual_interface_id

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
        if issubclass(CreateBgpPeerRequest, dict):
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
        if not isinstance(other, CreateBgpPeerRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateBgpPeerRequest):
            return True

        return self.to_dict() != other.to_dict()