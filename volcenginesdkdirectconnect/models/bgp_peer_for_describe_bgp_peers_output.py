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


class BgpPeerForDescribeBgpPeersOutput(object):
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
        'account_id': 'str',
        'auth_key': 'str',
        'bgp_peer_id': 'str',
        'bgp_peer_name': 'str',
        'creation_time': 'str',
        'description': 'str',
        'ip_version': 'str',
        'local_asn': 'int',
        'remote_asn': 'int',
        'session_status': 'str',
        'status': 'str',
        'update_time': 'str',
        'virtual_interface_id': 'str'
    }

    attribute_map = {
        'account_id': 'AccountId',
        'auth_key': 'AuthKey',
        'bgp_peer_id': 'BgpPeerId',
        'bgp_peer_name': 'BgpPeerName',
        'creation_time': 'CreationTime',
        'description': 'Description',
        'ip_version': 'IpVersion',
        'local_asn': 'LocalAsn',
        'remote_asn': 'RemoteAsn',
        'session_status': 'SessionStatus',
        'status': 'Status',
        'update_time': 'UpdateTime',
        'virtual_interface_id': 'VirtualInterfaceId'
    }

    def __init__(self, account_id=None, auth_key=None, bgp_peer_id=None, bgp_peer_name=None, creation_time=None, description=None, ip_version=None, local_asn=None, remote_asn=None, session_status=None, status=None, update_time=None, virtual_interface_id=None, _configuration=None):  # noqa: E501
        """BgpPeerForDescribeBgpPeersOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_id = None
        self._auth_key = None
        self._bgp_peer_id = None
        self._bgp_peer_name = None
        self._creation_time = None
        self._description = None
        self._ip_version = None
        self._local_asn = None
        self._remote_asn = None
        self._session_status = None
        self._status = None
        self._update_time = None
        self._virtual_interface_id = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if auth_key is not None:
            self.auth_key = auth_key
        if bgp_peer_id is not None:
            self.bgp_peer_id = bgp_peer_id
        if bgp_peer_name is not None:
            self.bgp_peer_name = bgp_peer_name
        if creation_time is not None:
            self.creation_time = creation_time
        if description is not None:
            self.description = description
        if ip_version is not None:
            self.ip_version = ip_version
        if local_asn is not None:
            self.local_asn = local_asn
        if remote_asn is not None:
            self.remote_asn = remote_asn
        if session_status is not None:
            self.session_status = session_status
        if status is not None:
            self.status = status
        if update_time is not None:
            self.update_time = update_time
        if virtual_interface_id is not None:
            self.virtual_interface_id = virtual_interface_id

    @property
    def account_id(self):
        """Gets the account_id of this BgpPeerForDescribeBgpPeersOutput.  # noqa: E501


        :return: The account_id of this BgpPeerForDescribeBgpPeersOutput.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this BgpPeerForDescribeBgpPeersOutput.


        :param account_id: The account_id of this BgpPeerForDescribeBgpPeersOutput.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def auth_key(self):
        """Gets the auth_key of this BgpPeerForDescribeBgpPeersOutput.  # noqa: E501


        :return: The auth_key of this BgpPeerForDescribeBgpPeersOutput.  # noqa: E501
        :rtype: str
        """
        return self._auth_key

    @auth_key.setter
    def auth_key(self, auth_key):
        """Sets the auth_key of this BgpPeerForDescribeBgpPeersOutput.


        :param auth_key: The auth_key of this BgpPeerForDescribeBgpPeersOutput.  # noqa: E501
        :type: str
        """

        self._auth_key = auth_key

    @property
    def bgp_peer_id(self):
        """Gets the bgp_peer_id of this BgpPeerForDescribeBgpPeersOutput.  # noqa: E501


        :return: The bgp_peer_id of this BgpPeerForDescribeBgpPeersOutput.  # noqa: E501
        :rtype: str
        """
        return self._bgp_peer_id

    @bgp_peer_id.setter
    def bgp_peer_id(self, bgp_peer_id):
        """Sets the bgp_peer_id of this BgpPeerForDescribeBgpPeersOutput.


        :param bgp_peer_id: The bgp_peer_id of this BgpPeerForDescribeBgpPeersOutput.  # noqa: E501
        :type: str
        """

        self._bgp_peer_id = bgp_peer_id

    @property
    def bgp_peer_name(self):
        """Gets the bgp_peer_name of this BgpPeerForDescribeBgpPeersOutput.  # noqa: E501


        :return: The bgp_peer_name of this BgpPeerForDescribeBgpPeersOutput.  # noqa: E501
        :rtype: str
        """
        return self._bgp_peer_name

    @bgp_peer_name.setter
    def bgp_peer_name(self, bgp_peer_name):
        """Sets the bgp_peer_name of this BgpPeerForDescribeBgpPeersOutput.


        :param bgp_peer_name: The bgp_peer_name of this BgpPeerForDescribeBgpPeersOutput.  # noqa: E501
        :type: str
        """

        self._bgp_peer_name = bgp_peer_name

    @property
    def creation_time(self):
        """Gets the creation_time of this BgpPeerForDescribeBgpPeersOutput.  # noqa: E501


        :return: The creation_time of this BgpPeerForDescribeBgpPeersOutput.  # noqa: E501
        :rtype: str
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this BgpPeerForDescribeBgpPeersOutput.


        :param creation_time: The creation_time of this BgpPeerForDescribeBgpPeersOutput.  # noqa: E501
        :type: str
        """

        self._creation_time = creation_time

    @property
    def description(self):
        """Gets the description of this BgpPeerForDescribeBgpPeersOutput.  # noqa: E501


        :return: The description of this BgpPeerForDescribeBgpPeersOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BgpPeerForDescribeBgpPeersOutput.


        :param description: The description of this BgpPeerForDescribeBgpPeersOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def ip_version(self):
        """Gets the ip_version of this BgpPeerForDescribeBgpPeersOutput.  # noqa: E501


        :return: The ip_version of this BgpPeerForDescribeBgpPeersOutput.  # noqa: E501
        :rtype: str
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this BgpPeerForDescribeBgpPeersOutput.


        :param ip_version: The ip_version of this BgpPeerForDescribeBgpPeersOutput.  # noqa: E501
        :type: str
        """

        self._ip_version = ip_version

    @property
    def local_asn(self):
        """Gets the local_asn of this BgpPeerForDescribeBgpPeersOutput.  # noqa: E501


        :return: The local_asn of this BgpPeerForDescribeBgpPeersOutput.  # noqa: E501
        :rtype: int
        """
        return self._local_asn

    @local_asn.setter
    def local_asn(self, local_asn):
        """Sets the local_asn of this BgpPeerForDescribeBgpPeersOutput.


        :param local_asn: The local_asn of this BgpPeerForDescribeBgpPeersOutput.  # noqa: E501
        :type: int
        """

        self._local_asn = local_asn

    @property
    def remote_asn(self):
        """Gets the remote_asn of this BgpPeerForDescribeBgpPeersOutput.  # noqa: E501


        :return: The remote_asn of this BgpPeerForDescribeBgpPeersOutput.  # noqa: E501
        :rtype: int
        """
        return self._remote_asn

    @remote_asn.setter
    def remote_asn(self, remote_asn):
        """Sets the remote_asn of this BgpPeerForDescribeBgpPeersOutput.


        :param remote_asn: The remote_asn of this BgpPeerForDescribeBgpPeersOutput.  # noqa: E501
        :type: int
        """

        self._remote_asn = remote_asn

    @property
    def session_status(self):
        """Gets the session_status of this BgpPeerForDescribeBgpPeersOutput.  # noqa: E501


        :return: The session_status of this BgpPeerForDescribeBgpPeersOutput.  # noqa: E501
        :rtype: str
        """
        return self._session_status

    @session_status.setter
    def session_status(self, session_status):
        """Sets the session_status of this BgpPeerForDescribeBgpPeersOutput.


        :param session_status: The session_status of this BgpPeerForDescribeBgpPeersOutput.  # noqa: E501
        :type: str
        """

        self._session_status = session_status

    @property
    def status(self):
        """Gets the status of this BgpPeerForDescribeBgpPeersOutput.  # noqa: E501


        :return: The status of this BgpPeerForDescribeBgpPeersOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BgpPeerForDescribeBgpPeersOutput.


        :param status: The status of this BgpPeerForDescribeBgpPeersOutput.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def update_time(self):
        """Gets the update_time of this BgpPeerForDescribeBgpPeersOutput.  # noqa: E501


        :return: The update_time of this BgpPeerForDescribeBgpPeersOutput.  # noqa: E501
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this BgpPeerForDescribeBgpPeersOutput.


        :param update_time: The update_time of this BgpPeerForDescribeBgpPeersOutput.  # noqa: E501
        :type: str
        """

        self._update_time = update_time

    @property
    def virtual_interface_id(self):
        """Gets the virtual_interface_id of this BgpPeerForDescribeBgpPeersOutput.  # noqa: E501


        :return: The virtual_interface_id of this BgpPeerForDescribeBgpPeersOutput.  # noqa: E501
        :rtype: str
        """
        return self._virtual_interface_id

    @virtual_interface_id.setter
    def virtual_interface_id(self, virtual_interface_id):
        """Sets the virtual_interface_id of this BgpPeerForDescribeBgpPeersOutput.


        :param virtual_interface_id: The virtual_interface_id of this BgpPeerForDescribeBgpPeersOutput.  # noqa: E501
        :type: str
        """

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
        if issubclass(BgpPeerForDescribeBgpPeersOutput, dict):
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
        if not isinstance(other, BgpPeerForDescribeBgpPeersOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BgpPeerForDescribeBgpPeersOutput):
            return True

        return self.to_dict() != other.to_dict()
