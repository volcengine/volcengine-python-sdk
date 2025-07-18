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


class ServerGroupForDescribeNLBServerGroupsOutput(object):
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
        'any_port_enabled': 'bool',
        'bypass_security_group_enabled': 'bool',
        'connection_drain_enabled': 'bool',
        'connection_drain_timeout': 'int',
        'create_time': 'str',
        'description': 'str',
        'health_check': 'HealthCheckForDescribeNLBServerGroupsOutput',
        'ip_address_version': 'str',
        'preserve_client_ip_enabled': 'bool',
        'project_name': 'str',
        'protocol': 'str',
        'proxy_protocol_type': 'str',
        'related_load_balancer_ids': 'list[str]',
        'scheduler': 'str',
        'server_count': 'int',
        'server_group_id': 'str',
        'server_group_name': 'str',
        'session_persistence_enabled': 'bool',
        'session_persistence_timeout': 'int',
        'status': 'str',
        'tags': 'list[TagForDescribeNLBServerGroupsOutput]',
        'type': 'str',
        'update_time': 'str',
        'vpc_id': 'str'
    }

    attribute_map = {
        'account_id': 'AccountId',
        'any_port_enabled': 'AnyPortEnabled',
        'bypass_security_group_enabled': 'BypassSecurityGroupEnabled',
        'connection_drain_enabled': 'ConnectionDrainEnabled',
        'connection_drain_timeout': 'ConnectionDrainTimeout',
        'create_time': 'CreateTime',
        'description': 'Description',
        'health_check': 'HealthCheck',
        'ip_address_version': 'IpAddressVersion',
        'preserve_client_ip_enabled': 'PreserveClientIpEnabled',
        'project_name': 'ProjectName',
        'protocol': 'Protocol',
        'proxy_protocol_type': 'ProxyProtocolType',
        'related_load_balancer_ids': 'RelatedLoadBalancerIds',
        'scheduler': 'Scheduler',
        'server_count': 'ServerCount',
        'server_group_id': 'ServerGroupId',
        'server_group_name': 'ServerGroupName',
        'session_persistence_enabled': 'SessionPersistenceEnabled',
        'session_persistence_timeout': 'SessionPersistenceTimeout',
        'status': 'Status',
        'tags': 'Tags',
        'type': 'Type',
        'update_time': 'UpdateTime',
        'vpc_id': 'VpcId'
    }

    def __init__(self, account_id=None, any_port_enabled=None, bypass_security_group_enabled=None, connection_drain_enabled=None, connection_drain_timeout=None, create_time=None, description=None, health_check=None, ip_address_version=None, preserve_client_ip_enabled=None, project_name=None, protocol=None, proxy_protocol_type=None, related_load_balancer_ids=None, scheduler=None, server_count=None, server_group_id=None, server_group_name=None, session_persistence_enabled=None, session_persistence_timeout=None, status=None, tags=None, type=None, update_time=None, vpc_id=None, _configuration=None):  # noqa: E501
        """ServerGroupForDescribeNLBServerGroupsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_id = None
        self._any_port_enabled = None
        self._bypass_security_group_enabled = None
        self._connection_drain_enabled = None
        self._connection_drain_timeout = None
        self._create_time = None
        self._description = None
        self._health_check = None
        self._ip_address_version = None
        self._preserve_client_ip_enabled = None
        self._project_name = None
        self._protocol = None
        self._proxy_protocol_type = None
        self._related_load_balancer_ids = None
        self._scheduler = None
        self._server_count = None
        self._server_group_id = None
        self._server_group_name = None
        self._session_persistence_enabled = None
        self._session_persistence_timeout = None
        self._status = None
        self._tags = None
        self._type = None
        self._update_time = None
        self._vpc_id = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if any_port_enabled is not None:
            self.any_port_enabled = any_port_enabled
        if bypass_security_group_enabled is not None:
            self.bypass_security_group_enabled = bypass_security_group_enabled
        if connection_drain_enabled is not None:
            self.connection_drain_enabled = connection_drain_enabled
        if connection_drain_timeout is not None:
            self.connection_drain_timeout = connection_drain_timeout
        if create_time is not None:
            self.create_time = create_time
        if description is not None:
            self.description = description
        if health_check is not None:
            self.health_check = health_check
        if ip_address_version is not None:
            self.ip_address_version = ip_address_version
        if preserve_client_ip_enabled is not None:
            self.preserve_client_ip_enabled = preserve_client_ip_enabled
        if project_name is not None:
            self.project_name = project_name
        if protocol is not None:
            self.protocol = protocol
        if proxy_protocol_type is not None:
            self.proxy_protocol_type = proxy_protocol_type
        if related_load_balancer_ids is not None:
            self.related_load_balancer_ids = related_load_balancer_ids
        if scheduler is not None:
            self.scheduler = scheduler
        if server_count is not None:
            self.server_count = server_count
        if server_group_id is not None:
            self.server_group_id = server_group_id
        if server_group_name is not None:
            self.server_group_name = server_group_name
        if session_persistence_enabled is not None:
            self.session_persistence_enabled = session_persistence_enabled
        if session_persistence_timeout is not None:
            self.session_persistence_timeout = session_persistence_timeout
        if status is not None:
            self.status = status
        if tags is not None:
            self.tags = tags
        if type is not None:
            self.type = type
        if update_time is not None:
            self.update_time = update_time
        if vpc_id is not None:
            self.vpc_id = vpc_id

    @property
    def account_id(self):
        """Gets the account_id of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501


        :return: The account_id of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this ServerGroupForDescribeNLBServerGroupsOutput.


        :param account_id: The account_id of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def any_port_enabled(self):
        """Gets the any_port_enabled of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501


        :return: The any_port_enabled of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501
        :rtype: bool
        """
        return self._any_port_enabled

    @any_port_enabled.setter
    def any_port_enabled(self, any_port_enabled):
        """Sets the any_port_enabled of this ServerGroupForDescribeNLBServerGroupsOutput.


        :param any_port_enabled: The any_port_enabled of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501
        :type: bool
        """

        self._any_port_enabled = any_port_enabled

    @property
    def bypass_security_group_enabled(self):
        """Gets the bypass_security_group_enabled of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501


        :return: The bypass_security_group_enabled of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501
        :rtype: bool
        """
        return self._bypass_security_group_enabled

    @bypass_security_group_enabled.setter
    def bypass_security_group_enabled(self, bypass_security_group_enabled):
        """Sets the bypass_security_group_enabled of this ServerGroupForDescribeNLBServerGroupsOutput.


        :param bypass_security_group_enabled: The bypass_security_group_enabled of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501
        :type: bool
        """

        self._bypass_security_group_enabled = bypass_security_group_enabled

    @property
    def connection_drain_enabled(self):
        """Gets the connection_drain_enabled of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501


        :return: The connection_drain_enabled of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501
        :rtype: bool
        """
        return self._connection_drain_enabled

    @connection_drain_enabled.setter
    def connection_drain_enabled(self, connection_drain_enabled):
        """Sets the connection_drain_enabled of this ServerGroupForDescribeNLBServerGroupsOutput.


        :param connection_drain_enabled: The connection_drain_enabled of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501
        :type: bool
        """

        self._connection_drain_enabled = connection_drain_enabled

    @property
    def connection_drain_timeout(self):
        """Gets the connection_drain_timeout of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501


        :return: The connection_drain_timeout of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501
        :rtype: int
        """
        return self._connection_drain_timeout

    @connection_drain_timeout.setter
    def connection_drain_timeout(self, connection_drain_timeout):
        """Sets the connection_drain_timeout of this ServerGroupForDescribeNLBServerGroupsOutput.


        :param connection_drain_timeout: The connection_drain_timeout of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501
        :type: int
        """

        self._connection_drain_timeout = connection_drain_timeout

    @property
    def create_time(self):
        """Gets the create_time of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501


        :return: The create_time of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ServerGroupForDescribeNLBServerGroupsOutput.


        :param create_time: The create_time of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501
        :type: str
        """

        self._create_time = create_time

    @property
    def description(self):
        """Gets the description of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501


        :return: The description of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ServerGroupForDescribeNLBServerGroupsOutput.


        :param description: The description of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def health_check(self):
        """Gets the health_check of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501


        :return: The health_check of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501
        :rtype: HealthCheckForDescribeNLBServerGroupsOutput
        """
        return self._health_check

    @health_check.setter
    def health_check(self, health_check):
        """Sets the health_check of this ServerGroupForDescribeNLBServerGroupsOutput.


        :param health_check: The health_check of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501
        :type: HealthCheckForDescribeNLBServerGroupsOutput
        """

        self._health_check = health_check

    @property
    def ip_address_version(self):
        """Gets the ip_address_version of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501


        :return: The ip_address_version of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._ip_address_version

    @ip_address_version.setter
    def ip_address_version(self, ip_address_version):
        """Sets the ip_address_version of this ServerGroupForDescribeNLBServerGroupsOutput.


        :param ip_address_version: The ip_address_version of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501
        :type: str
        """

        self._ip_address_version = ip_address_version

    @property
    def preserve_client_ip_enabled(self):
        """Gets the preserve_client_ip_enabled of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501


        :return: The preserve_client_ip_enabled of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501
        :rtype: bool
        """
        return self._preserve_client_ip_enabled

    @preserve_client_ip_enabled.setter
    def preserve_client_ip_enabled(self, preserve_client_ip_enabled):
        """Sets the preserve_client_ip_enabled of this ServerGroupForDescribeNLBServerGroupsOutput.


        :param preserve_client_ip_enabled: The preserve_client_ip_enabled of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501
        :type: bool
        """

        self._preserve_client_ip_enabled = preserve_client_ip_enabled

    @property
    def project_name(self):
        """Gets the project_name of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501


        :return: The project_name of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this ServerGroupForDescribeNLBServerGroupsOutput.


        :param project_name: The project_name of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def protocol(self):
        """Gets the protocol of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501


        :return: The protocol of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ServerGroupForDescribeNLBServerGroupsOutput.


        :param protocol: The protocol of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501
        :type: str
        """

        self._protocol = protocol

    @property
    def proxy_protocol_type(self):
        """Gets the proxy_protocol_type of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501


        :return: The proxy_protocol_type of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._proxy_protocol_type

    @proxy_protocol_type.setter
    def proxy_protocol_type(self, proxy_protocol_type):
        """Sets the proxy_protocol_type of this ServerGroupForDescribeNLBServerGroupsOutput.


        :param proxy_protocol_type: The proxy_protocol_type of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501
        :type: str
        """

        self._proxy_protocol_type = proxy_protocol_type

    @property
    def related_load_balancer_ids(self):
        """Gets the related_load_balancer_ids of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501


        :return: The related_load_balancer_ids of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._related_load_balancer_ids

    @related_load_balancer_ids.setter
    def related_load_balancer_ids(self, related_load_balancer_ids):
        """Sets the related_load_balancer_ids of this ServerGroupForDescribeNLBServerGroupsOutput.


        :param related_load_balancer_ids: The related_load_balancer_ids of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501
        :type: list[str]
        """

        self._related_load_balancer_ids = related_load_balancer_ids

    @property
    def scheduler(self):
        """Gets the scheduler of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501


        :return: The scheduler of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._scheduler

    @scheduler.setter
    def scheduler(self, scheduler):
        """Sets the scheduler of this ServerGroupForDescribeNLBServerGroupsOutput.


        :param scheduler: The scheduler of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501
        :type: str
        """

        self._scheduler = scheduler

    @property
    def server_count(self):
        """Gets the server_count of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501


        :return: The server_count of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501
        :rtype: int
        """
        return self._server_count

    @server_count.setter
    def server_count(self, server_count):
        """Sets the server_count of this ServerGroupForDescribeNLBServerGroupsOutput.


        :param server_count: The server_count of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501
        :type: int
        """

        self._server_count = server_count

    @property
    def server_group_id(self):
        """Gets the server_group_id of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501


        :return: The server_group_id of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._server_group_id

    @server_group_id.setter
    def server_group_id(self, server_group_id):
        """Sets the server_group_id of this ServerGroupForDescribeNLBServerGroupsOutput.


        :param server_group_id: The server_group_id of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501
        :type: str
        """

        self._server_group_id = server_group_id

    @property
    def server_group_name(self):
        """Gets the server_group_name of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501


        :return: The server_group_name of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._server_group_name

    @server_group_name.setter
    def server_group_name(self, server_group_name):
        """Sets the server_group_name of this ServerGroupForDescribeNLBServerGroupsOutput.


        :param server_group_name: The server_group_name of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501
        :type: str
        """

        self._server_group_name = server_group_name

    @property
    def session_persistence_enabled(self):
        """Gets the session_persistence_enabled of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501


        :return: The session_persistence_enabled of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501
        :rtype: bool
        """
        return self._session_persistence_enabled

    @session_persistence_enabled.setter
    def session_persistence_enabled(self, session_persistence_enabled):
        """Sets the session_persistence_enabled of this ServerGroupForDescribeNLBServerGroupsOutput.


        :param session_persistence_enabled: The session_persistence_enabled of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501
        :type: bool
        """

        self._session_persistence_enabled = session_persistence_enabled

    @property
    def session_persistence_timeout(self):
        """Gets the session_persistence_timeout of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501


        :return: The session_persistence_timeout of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501
        :rtype: int
        """
        return self._session_persistence_timeout

    @session_persistence_timeout.setter
    def session_persistence_timeout(self, session_persistence_timeout):
        """Sets the session_persistence_timeout of this ServerGroupForDescribeNLBServerGroupsOutput.


        :param session_persistence_timeout: The session_persistence_timeout of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501
        :type: int
        """

        self._session_persistence_timeout = session_persistence_timeout

    @property
    def status(self):
        """Gets the status of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501


        :return: The status of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ServerGroupForDescribeNLBServerGroupsOutput.


        :param status: The status of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def tags(self):
        """Gets the tags of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501


        :return: The tags of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501
        :rtype: list[TagForDescribeNLBServerGroupsOutput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ServerGroupForDescribeNLBServerGroupsOutput.


        :param tags: The tags of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501
        :type: list[TagForDescribeNLBServerGroupsOutput]
        """

        self._tags = tags

    @property
    def type(self):
        """Gets the type of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501


        :return: The type of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ServerGroupForDescribeNLBServerGroupsOutput.


        :param type: The type of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def update_time(self):
        """Gets the update_time of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501


        :return: The update_time of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ServerGroupForDescribeNLBServerGroupsOutput.


        :param update_time: The update_time of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501
        :type: str
        """

        self._update_time = update_time

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501


        :return: The vpc_id of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ServerGroupForDescribeNLBServerGroupsOutput.


        :param vpc_id: The vpc_id of this ServerGroupForDescribeNLBServerGroupsOutput.  # noqa: E501
        :type: str
        """

        self._vpc_id = vpc_id

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
        if issubclass(ServerGroupForDescribeNLBServerGroupsOutput, dict):
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
        if not isinstance(other, ServerGroupForDescribeNLBServerGroupsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ServerGroupForDescribeNLBServerGroupsOutput):
            return True

        return self.to_dict() != other.to_dict()
