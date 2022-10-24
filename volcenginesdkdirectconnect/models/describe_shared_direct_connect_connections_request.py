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


class DescribeSharedDirectConnectConnectionsRequest(object):
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
        'page_number': 'int',
        'page_size': 'int',
        'parent_connection_id': 'str',
        'shared_direct_connect_connection_ids': 'list[str]',
        'shared_direct_connect_connection_name': 'str',
        'status': 'str',
        'user_account_id': 'str',
        'vlan_id': 'int'
    }

    attribute_map = {
        'page_number': 'PageNumber',
        'page_size': 'PageSize',
        'parent_connection_id': 'ParentConnectionId',
        'shared_direct_connect_connection_ids': 'SharedDirectConnectConnectionIds',
        'shared_direct_connect_connection_name': 'SharedDirectConnectConnectionName',
        'status': 'Status',
        'user_account_id': 'UserAccountId',
        'vlan_id': 'VlanId'
    }

    def __init__(self, page_number=None, page_size=None, parent_connection_id=None, shared_direct_connect_connection_ids=None, shared_direct_connect_connection_name=None, status=None, user_account_id=None, vlan_id=None, _configuration=None):  # noqa: E501
        """DescribeSharedDirectConnectConnectionsRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._page_number = None
        self._page_size = None
        self._parent_connection_id = None
        self._shared_direct_connect_connection_ids = None
        self._shared_direct_connect_connection_name = None
        self._status = None
        self._user_account_id = None
        self._vlan_id = None
        self.discriminator = None

        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if parent_connection_id is not None:
            self.parent_connection_id = parent_connection_id
        if shared_direct_connect_connection_ids is not None:
            self.shared_direct_connect_connection_ids = shared_direct_connect_connection_ids
        if shared_direct_connect_connection_name is not None:
            self.shared_direct_connect_connection_name = shared_direct_connect_connection_name
        if status is not None:
            self.status = status
        if user_account_id is not None:
            self.user_account_id = user_account_id
        if vlan_id is not None:
            self.vlan_id = vlan_id

    @property
    def page_number(self):
        """Gets the page_number of this DescribeSharedDirectConnectConnectionsRequest.  # noqa: E501


        :return: The page_number of this DescribeSharedDirectConnectConnectionsRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this DescribeSharedDirectConnectConnectionsRequest.


        :param page_number: The page_number of this DescribeSharedDirectConnectConnectionsRequest.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this DescribeSharedDirectConnectConnectionsRequest.  # noqa: E501


        :return: The page_size of this DescribeSharedDirectConnectConnectionsRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this DescribeSharedDirectConnectConnectionsRequest.


        :param page_size: The page_size of this DescribeSharedDirectConnectConnectionsRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def parent_connection_id(self):
        """Gets the parent_connection_id of this DescribeSharedDirectConnectConnectionsRequest.  # noqa: E501


        :return: The parent_connection_id of this DescribeSharedDirectConnectConnectionsRequest.  # noqa: E501
        :rtype: str
        """
        return self._parent_connection_id

    @parent_connection_id.setter
    def parent_connection_id(self, parent_connection_id):
        """Sets the parent_connection_id of this DescribeSharedDirectConnectConnectionsRequest.


        :param parent_connection_id: The parent_connection_id of this DescribeSharedDirectConnectConnectionsRequest.  # noqa: E501
        :type: str
        """

        self._parent_connection_id = parent_connection_id

    @property
    def shared_direct_connect_connection_ids(self):
        """Gets the shared_direct_connect_connection_ids of this DescribeSharedDirectConnectConnectionsRequest.  # noqa: E501


        :return: The shared_direct_connect_connection_ids of this DescribeSharedDirectConnectConnectionsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._shared_direct_connect_connection_ids

    @shared_direct_connect_connection_ids.setter
    def shared_direct_connect_connection_ids(self, shared_direct_connect_connection_ids):
        """Sets the shared_direct_connect_connection_ids of this DescribeSharedDirectConnectConnectionsRequest.


        :param shared_direct_connect_connection_ids: The shared_direct_connect_connection_ids of this DescribeSharedDirectConnectConnectionsRequest.  # noqa: E501
        :type: list[str]
        """

        self._shared_direct_connect_connection_ids = shared_direct_connect_connection_ids

    @property
    def shared_direct_connect_connection_name(self):
        """Gets the shared_direct_connect_connection_name of this DescribeSharedDirectConnectConnectionsRequest.  # noqa: E501


        :return: The shared_direct_connect_connection_name of this DescribeSharedDirectConnectConnectionsRequest.  # noqa: E501
        :rtype: str
        """
        return self._shared_direct_connect_connection_name

    @shared_direct_connect_connection_name.setter
    def shared_direct_connect_connection_name(self, shared_direct_connect_connection_name):
        """Sets the shared_direct_connect_connection_name of this DescribeSharedDirectConnectConnectionsRequest.


        :param shared_direct_connect_connection_name: The shared_direct_connect_connection_name of this DescribeSharedDirectConnectConnectionsRequest.  # noqa: E501
        :type: str
        """

        self._shared_direct_connect_connection_name = shared_direct_connect_connection_name

    @property
    def status(self):
        """Gets the status of this DescribeSharedDirectConnectConnectionsRequest.  # noqa: E501


        :return: The status of this DescribeSharedDirectConnectConnectionsRequest.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DescribeSharedDirectConnectConnectionsRequest.


        :param status: The status of this DescribeSharedDirectConnectConnectionsRequest.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def user_account_id(self):
        """Gets the user_account_id of this DescribeSharedDirectConnectConnectionsRequest.  # noqa: E501


        :return: The user_account_id of this DescribeSharedDirectConnectConnectionsRequest.  # noqa: E501
        :rtype: str
        """
        return self._user_account_id

    @user_account_id.setter
    def user_account_id(self, user_account_id):
        """Sets the user_account_id of this DescribeSharedDirectConnectConnectionsRequest.


        :param user_account_id: The user_account_id of this DescribeSharedDirectConnectConnectionsRequest.  # noqa: E501
        :type: str
        """

        self._user_account_id = user_account_id

    @property
    def vlan_id(self):
        """Gets the vlan_id of this DescribeSharedDirectConnectConnectionsRequest.  # noqa: E501


        :return: The vlan_id of this DescribeSharedDirectConnectConnectionsRequest.  # noqa: E501
        :rtype: int
        """
        return self._vlan_id

    @vlan_id.setter
    def vlan_id(self, vlan_id):
        """Sets the vlan_id of this DescribeSharedDirectConnectConnectionsRequest.


        :param vlan_id: The vlan_id of this DescribeSharedDirectConnectConnectionsRequest.  # noqa: E501
        :type: int
        """

        self._vlan_id = vlan_id

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
        if issubclass(DescribeSharedDirectConnectConnectionsRequest, dict):
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
        if not isinstance(other, DescribeSharedDirectConnectConnectionsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeSharedDirectConnectConnectionsRequest):
            return True

        return self.to_dict() != other.to_dict()