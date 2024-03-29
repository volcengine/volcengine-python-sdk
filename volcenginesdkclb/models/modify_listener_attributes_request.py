# coding: utf-8

"""
    clb

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ModifyListenerAttributesRequest(object):
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
        'acl_ids': 'list[str]',
        'acl_status': 'str',
        'acl_type': 'str',
        'bandwidth': 'int',
        'certificate_id': 'str',
        'connection_drain_enabled': 'str',
        'connection_drain_timeout': 'int',
        'description': 'str',
        'enabled': 'str',
        'established_timeout': 'int',
        'health_check': 'HealthCheckForModifyListenerAttributesInput',
        'listener_id': 'str',
        'listener_name': 'str',
        'persistence_timeout': 'int',
        'persistence_type': 'str',
        'proxy_protocol_type': 'str',
        'scheduler': 'str',
        'server_group_id': 'str'
    }

    attribute_map = {
        'acl_ids': 'AclIds',
        'acl_status': 'AclStatus',
        'acl_type': 'AclType',
        'bandwidth': 'Bandwidth',
        'certificate_id': 'CertificateId',
        'connection_drain_enabled': 'ConnectionDrainEnabled',
        'connection_drain_timeout': 'ConnectionDrainTimeout',
        'description': 'Description',
        'enabled': 'Enabled',
        'established_timeout': 'EstablishedTimeout',
        'health_check': 'HealthCheck',
        'listener_id': 'ListenerId',
        'listener_name': 'ListenerName',
        'persistence_timeout': 'PersistenceTimeout',
        'persistence_type': 'PersistenceType',
        'proxy_protocol_type': 'ProxyProtocolType',
        'scheduler': 'Scheduler',
        'server_group_id': 'ServerGroupId'
    }

    def __init__(self, acl_ids=None, acl_status=None, acl_type=None, bandwidth=None, certificate_id=None, connection_drain_enabled=None, connection_drain_timeout=None, description=None, enabled=None, established_timeout=None, health_check=None, listener_id=None, listener_name=None, persistence_timeout=None, persistence_type=None, proxy_protocol_type=None, scheduler=None, server_group_id=None, _configuration=None):  # noqa: E501
        """ModifyListenerAttributesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._acl_ids = None
        self._acl_status = None
        self._acl_type = None
        self._bandwidth = None
        self._certificate_id = None
        self._connection_drain_enabled = None
        self._connection_drain_timeout = None
        self._description = None
        self._enabled = None
        self._established_timeout = None
        self._health_check = None
        self._listener_id = None
        self._listener_name = None
        self._persistence_timeout = None
        self._persistence_type = None
        self._proxy_protocol_type = None
        self._scheduler = None
        self._server_group_id = None
        self.discriminator = None

        if acl_ids is not None:
            self.acl_ids = acl_ids
        if acl_status is not None:
            self.acl_status = acl_status
        if acl_type is not None:
            self.acl_type = acl_type
        if bandwidth is not None:
            self.bandwidth = bandwidth
        if certificate_id is not None:
            self.certificate_id = certificate_id
        if connection_drain_enabled is not None:
            self.connection_drain_enabled = connection_drain_enabled
        if connection_drain_timeout is not None:
            self.connection_drain_timeout = connection_drain_timeout
        if description is not None:
            self.description = description
        if enabled is not None:
            self.enabled = enabled
        if established_timeout is not None:
            self.established_timeout = established_timeout
        if health_check is not None:
            self.health_check = health_check
        self.listener_id = listener_id
        if listener_name is not None:
            self.listener_name = listener_name
        if persistence_timeout is not None:
            self.persistence_timeout = persistence_timeout
        if persistence_type is not None:
            self.persistence_type = persistence_type
        if proxy_protocol_type is not None:
            self.proxy_protocol_type = proxy_protocol_type
        if scheduler is not None:
            self.scheduler = scheduler
        if server_group_id is not None:
            self.server_group_id = server_group_id

    @property
    def acl_ids(self):
        """Gets the acl_ids of this ModifyListenerAttributesRequest.  # noqa: E501


        :return: The acl_ids of this ModifyListenerAttributesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._acl_ids

    @acl_ids.setter
    def acl_ids(self, acl_ids):
        """Sets the acl_ids of this ModifyListenerAttributesRequest.


        :param acl_ids: The acl_ids of this ModifyListenerAttributesRequest.  # noqa: E501
        :type: list[str]
        """

        self._acl_ids = acl_ids

    @property
    def acl_status(self):
        """Gets the acl_status of this ModifyListenerAttributesRequest.  # noqa: E501


        :return: The acl_status of this ModifyListenerAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._acl_status

    @acl_status.setter
    def acl_status(self, acl_status):
        """Sets the acl_status of this ModifyListenerAttributesRequest.


        :param acl_status: The acl_status of this ModifyListenerAttributesRequest.  # noqa: E501
        :type: str
        """

        self._acl_status = acl_status

    @property
    def acl_type(self):
        """Gets the acl_type of this ModifyListenerAttributesRequest.  # noqa: E501


        :return: The acl_type of this ModifyListenerAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._acl_type

    @acl_type.setter
    def acl_type(self, acl_type):
        """Sets the acl_type of this ModifyListenerAttributesRequest.


        :param acl_type: The acl_type of this ModifyListenerAttributesRequest.  # noqa: E501
        :type: str
        """

        self._acl_type = acl_type

    @property
    def bandwidth(self):
        """Gets the bandwidth of this ModifyListenerAttributesRequest.  # noqa: E501


        :return: The bandwidth of this ModifyListenerAttributesRequest.  # noqa: E501
        :rtype: int
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this ModifyListenerAttributesRequest.


        :param bandwidth: The bandwidth of this ModifyListenerAttributesRequest.  # noqa: E501
        :type: int
        """

        self._bandwidth = bandwidth

    @property
    def certificate_id(self):
        """Gets the certificate_id of this ModifyListenerAttributesRequest.  # noqa: E501


        :return: The certificate_id of this ModifyListenerAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        """Sets the certificate_id of this ModifyListenerAttributesRequest.


        :param certificate_id: The certificate_id of this ModifyListenerAttributesRequest.  # noqa: E501
        :type: str
        """

        self._certificate_id = certificate_id

    @property
    def connection_drain_enabled(self):
        """Gets the connection_drain_enabled of this ModifyListenerAttributesRequest.  # noqa: E501


        :return: The connection_drain_enabled of this ModifyListenerAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._connection_drain_enabled

    @connection_drain_enabled.setter
    def connection_drain_enabled(self, connection_drain_enabled):
        """Sets the connection_drain_enabled of this ModifyListenerAttributesRequest.


        :param connection_drain_enabled: The connection_drain_enabled of this ModifyListenerAttributesRequest.  # noqa: E501
        :type: str
        """

        self._connection_drain_enabled = connection_drain_enabled

    @property
    def connection_drain_timeout(self):
        """Gets the connection_drain_timeout of this ModifyListenerAttributesRequest.  # noqa: E501


        :return: The connection_drain_timeout of this ModifyListenerAttributesRequest.  # noqa: E501
        :rtype: int
        """
        return self._connection_drain_timeout

    @connection_drain_timeout.setter
    def connection_drain_timeout(self, connection_drain_timeout):
        """Sets the connection_drain_timeout of this ModifyListenerAttributesRequest.


        :param connection_drain_timeout: The connection_drain_timeout of this ModifyListenerAttributesRequest.  # noqa: E501
        :type: int
        """

        self._connection_drain_timeout = connection_drain_timeout

    @property
    def description(self):
        """Gets the description of this ModifyListenerAttributesRequest.  # noqa: E501


        :return: The description of this ModifyListenerAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ModifyListenerAttributesRequest.


        :param description: The description of this ModifyListenerAttributesRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def enabled(self):
        """Gets the enabled of this ModifyListenerAttributesRequest.  # noqa: E501


        :return: The enabled of this ModifyListenerAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ModifyListenerAttributesRequest.


        :param enabled: The enabled of this ModifyListenerAttributesRequest.  # noqa: E501
        :type: str
        """

        self._enabled = enabled

    @property
    def established_timeout(self):
        """Gets the established_timeout of this ModifyListenerAttributesRequest.  # noqa: E501


        :return: The established_timeout of this ModifyListenerAttributesRequest.  # noqa: E501
        :rtype: int
        """
        return self._established_timeout

    @established_timeout.setter
    def established_timeout(self, established_timeout):
        """Sets the established_timeout of this ModifyListenerAttributesRequest.


        :param established_timeout: The established_timeout of this ModifyListenerAttributesRequest.  # noqa: E501
        :type: int
        """

        self._established_timeout = established_timeout

    @property
    def health_check(self):
        """Gets the health_check of this ModifyListenerAttributesRequest.  # noqa: E501


        :return: The health_check of this ModifyListenerAttributesRequest.  # noqa: E501
        :rtype: HealthCheckForModifyListenerAttributesInput
        """
        return self._health_check

    @health_check.setter
    def health_check(self, health_check):
        """Sets the health_check of this ModifyListenerAttributesRequest.


        :param health_check: The health_check of this ModifyListenerAttributesRequest.  # noqa: E501
        :type: HealthCheckForModifyListenerAttributesInput
        """

        self._health_check = health_check

    @property
    def listener_id(self):
        """Gets the listener_id of this ModifyListenerAttributesRequest.  # noqa: E501


        :return: The listener_id of this ModifyListenerAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._listener_id

    @listener_id.setter
    def listener_id(self, listener_id):
        """Sets the listener_id of this ModifyListenerAttributesRequest.


        :param listener_id: The listener_id of this ModifyListenerAttributesRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and listener_id is None:
            raise ValueError("Invalid value for `listener_id`, must not be `None`")  # noqa: E501

        self._listener_id = listener_id

    @property
    def listener_name(self):
        """Gets the listener_name of this ModifyListenerAttributesRequest.  # noqa: E501


        :return: The listener_name of this ModifyListenerAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._listener_name

    @listener_name.setter
    def listener_name(self, listener_name):
        """Sets the listener_name of this ModifyListenerAttributesRequest.


        :param listener_name: The listener_name of this ModifyListenerAttributesRequest.  # noqa: E501
        :type: str
        """

        self._listener_name = listener_name

    @property
    def persistence_timeout(self):
        """Gets the persistence_timeout of this ModifyListenerAttributesRequest.  # noqa: E501


        :return: The persistence_timeout of this ModifyListenerAttributesRequest.  # noqa: E501
        :rtype: int
        """
        return self._persistence_timeout

    @persistence_timeout.setter
    def persistence_timeout(self, persistence_timeout):
        """Sets the persistence_timeout of this ModifyListenerAttributesRequest.


        :param persistence_timeout: The persistence_timeout of this ModifyListenerAttributesRequest.  # noqa: E501
        :type: int
        """

        self._persistence_timeout = persistence_timeout

    @property
    def persistence_type(self):
        """Gets the persistence_type of this ModifyListenerAttributesRequest.  # noqa: E501


        :return: The persistence_type of this ModifyListenerAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._persistence_type

    @persistence_type.setter
    def persistence_type(self, persistence_type):
        """Sets the persistence_type of this ModifyListenerAttributesRequest.


        :param persistence_type: The persistence_type of this ModifyListenerAttributesRequest.  # noqa: E501
        :type: str
        """

        self._persistence_type = persistence_type

    @property
    def proxy_protocol_type(self):
        """Gets the proxy_protocol_type of this ModifyListenerAttributesRequest.  # noqa: E501


        :return: The proxy_protocol_type of this ModifyListenerAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._proxy_protocol_type

    @proxy_protocol_type.setter
    def proxy_protocol_type(self, proxy_protocol_type):
        """Sets the proxy_protocol_type of this ModifyListenerAttributesRequest.


        :param proxy_protocol_type: The proxy_protocol_type of this ModifyListenerAttributesRequest.  # noqa: E501
        :type: str
        """

        self._proxy_protocol_type = proxy_protocol_type

    @property
    def scheduler(self):
        """Gets the scheduler of this ModifyListenerAttributesRequest.  # noqa: E501


        :return: The scheduler of this ModifyListenerAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._scheduler

    @scheduler.setter
    def scheduler(self, scheduler):
        """Sets the scheduler of this ModifyListenerAttributesRequest.


        :param scheduler: The scheduler of this ModifyListenerAttributesRequest.  # noqa: E501
        :type: str
        """

        self._scheduler = scheduler

    @property
    def server_group_id(self):
        """Gets the server_group_id of this ModifyListenerAttributesRequest.  # noqa: E501


        :return: The server_group_id of this ModifyListenerAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._server_group_id

    @server_group_id.setter
    def server_group_id(self, server_group_id):
        """Sets the server_group_id of this ModifyListenerAttributesRequest.


        :param server_group_id: The server_group_id of this ModifyListenerAttributesRequest.  # noqa: E501
        :type: str
        """

        self._server_group_id = server_group_id

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
        if issubclass(ModifyListenerAttributesRequest, dict):
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
        if not isinstance(other, ModifyListenerAttributesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModifyListenerAttributesRequest):
            return True

        return self.to_dict() != other.to_dict()
