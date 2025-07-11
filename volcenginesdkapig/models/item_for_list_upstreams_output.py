# coding: utf-8

"""
    apig

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ItemForListUpstreamsOutput(object):
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
        'backend_target_list': 'list[BackendTargetListForListUpstreamsOutput]',
        'circuit_breaking_settings': 'CircuitBreakingSettingsForListUpstreamsOutput',
        'comments': 'str',
        'create_time': 'str',
        'gateway_id': 'str',
        'id': 'str',
        'load_balancer_settings': 'LoadBalancerSettingsForListUpstreamsOutput',
        'name': 'str',
        'protocol': 'str',
        'resource_type': 'str',
        'source_type': 'str',
        'tags': 'list[TagForListUpstreamsOutput]',
        'tls_settings': 'TlsSettingsForListUpstreamsOutput',
        'update_time': 'str',
        'upstream_spec': 'UpstreamSpecForListUpstreamsOutput',
        'version_details': 'list[VersionDetailForListUpstreamsOutput]'
    }

    attribute_map = {
        'backend_target_list': 'BackendTargetList',
        'circuit_breaking_settings': 'CircuitBreakingSettings',
        'comments': 'Comments',
        'create_time': 'CreateTime',
        'gateway_id': 'GatewayId',
        'id': 'Id',
        'load_balancer_settings': 'LoadBalancerSettings',
        'name': 'Name',
        'protocol': 'Protocol',
        'resource_type': 'ResourceType',
        'source_type': 'SourceType',
        'tags': 'Tags',
        'tls_settings': 'TlsSettings',
        'update_time': 'UpdateTime',
        'upstream_spec': 'UpstreamSpec',
        'version_details': 'VersionDetails'
    }

    def __init__(self, backend_target_list=None, circuit_breaking_settings=None, comments=None, create_time=None, gateway_id=None, id=None, load_balancer_settings=None, name=None, protocol=None, resource_type=None, source_type=None, tags=None, tls_settings=None, update_time=None, upstream_spec=None, version_details=None, _configuration=None):  # noqa: E501
        """ItemForListUpstreamsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._backend_target_list = None
        self._circuit_breaking_settings = None
        self._comments = None
        self._create_time = None
        self._gateway_id = None
        self._id = None
        self._load_balancer_settings = None
        self._name = None
        self._protocol = None
        self._resource_type = None
        self._source_type = None
        self._tags = None
        self._tls_settings = None
        self._update_time = None
        self._upstream_spec = None
        self._version_details = None
        self.discriminator = None

        if backend_target_list is not None:
            self.backend_target_list = backend_target_list
        if circuit_breaking_settings is not None:
            self.circuit_breaking_settings = circuit_breaking_settings
        if comments is not None:
            self.comments = comments
        if create_time is not None:
            self.create_time = create_time
        if gateway_id is not None:
            self.gateway_id = gateway_id
        if id is not None:
            self.id = id
        if load_balancer_settings is not None:
            self.load_balancer_settings = load_balancer_settings
        if name is not None:
            self.name = name
        if protocol is not None:
            self.protocol = protocol
        if resource_type is not None:
            self.resource_type = resource_type
        if source_type is not None:
            self.source_type = source_type
        if tags is not None:
            self.tags = tags
        if tls_settings is not None:
            self.tls_settings = tls_settings
        if update_time is not None:
            self.update_time = update_time
        if upstream_spec is not None:
            self.upstream_spec = upstream_spec
        if version_details is not None:
            self.version_details = version_details

    @property
    def backend_target_list(self):
        """Gets the backend_target_list of this ItemForListUpstreamsOutput.  # noqa: E501


        :return: The backend_target_list of this ItemForListUpstreamsOutput.  # noqa: E501
        :rtype: list[BackendTargetListForListUpstreamsOutput]
        """
        return self._backend_target_list

    @backend_target_list.setter
    def backend_target_list(self, backend_target_list):
        """Sets the backend_target_list of this ItemForListUpstreamsOutput.


        :param backend_target_list: The backend_target_list of this ItemForListUpstreamsOutput.  # noqa: E501
        :type: list[BackendTargetListForListUpstreamsOutput]
        """

        self._backend_target_list = backend_target_list

    @property
    def circuit_breaking_settings(self):
        """Gets the circuit_breaking_settings of this ItemForListUpstreamsOutput.  # noqa: E501


        :return: The circuit_breaking_settings of this ItemForListUpstreamsOutput.  # noqa: E501
        :rtype: CircuitBreakingSettingsForListUpstreamsOutput
        """
        return self._circuit_breaking_settings

    @circuit_breaking_settings.setter
    def circuit_breaking_settings(self, circuit_breaking_settings):
        """Sets the circuit_breaking_settings of this ItemForListUpstreamsOutput.


        :param circuit_breaking_settings: The circuit_breaking_settings of this ItemForListUpstreamsOutput.  # noqa: E501
        :type: CircuitBreakingSettingsForListUpstreamsOutput
        """

        self._circuit_breaking_settings = circuit_breaking_settings

    @property
    def comments(self):
        """Gets the comments of this ItemForListUpstreamsOutput.  # noqa: E501


        :return: The comments of this ItemForListUpstreamsOutput.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this ItemForListUpstreamsOutput.


        :param comments: The comments of this ItemForListUpstreamsOutput.  # noqa: E501
        :type: str
        """

        self._comments = comments

    @property
    def create_time(self):
        """Gets the create_time of this ItemForListUpstreamsOutput.  # noqa: E501


        :return: The create_time of this ItemForListUpstreamsOutput.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ItemForListUpstreamsOutput.


        :param create_time: The create_time of this ItemForListUpstreamsOutput.  # noqa: E501
        :type: str
        """

        self._create_time = create_time

    @property
    def gateway_id(self):
        """Gets the gateway_id of this ItemForListUpstreamsOutput.  # noqa: E501


        :return: The gateway_id of this ItemForListUpstreamsOutput.  # noqa: E501
        :rtype: str
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, gateway_id):
        """Sets the gateway_id of this ItemForListUpstreamsOutput.


        :param gateway_id: The gateway_id of this ItemForListUpstreamsOutput.  # noqa: E501
        :type: str
        """

        self._gateway_id = gateway_id

    @property
    def id(self):
        """Gets the id of this ItemForListUpstreamsOutput.  # noqa: E501


        :return: The id of this ItemForListUpstreamsOutput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ItemForListUpstreamsOutput.


        :param id: The id of this ItemForListUpstreamsOutput.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def load_balancer_settings(self):
        """Gets the load_balancer_settings of this ItemForListUpstreamsOutput.  # noqa: E501


        :return: The load_balancer_settings of this ItemForListUpstreamsOutput.  # noqa: E501
        :rtype: LoadBalancerSettingsForListUpstreamsOutput
        """
        return self._load_balancer_settings

    @load_balancer_settings.setter
    def load_balancer_settings(self, load_balancer_settings):
        """Sets the load_balancer_settings of this ItemForListUpstreamsOutput.


        :param load_balancer_settings: The load_balancer_settings of this ItemForListUpstreamsOutput.  # noqa: E501
        :type: LoadBalancerSettingsForListUpstreamsOutput
        """

        self._load_balancer_settings = load_balancer_settings

    @property
    def name(self):
        """Gets the name of this ItemForListUpstreamsOutput.  # noqa: E501


        :return: The name of this ItemForListUpstreamsOutput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ItemForListUpstreamsOutput.


        :param name: The name of this ItemForListUpstreamsOutput.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def protocol(self):
        """Gets the protocol of this ItemForListUpstreamsOutput.  # noqa: E501


        :return: The protocol of this ItemForListUpstreamsOutput.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ItemForListUpstreamsOutput.


        :param protocol: The protocol of this ItemForListUpstreamsOutput.  # noqa: E501
        :type: str
        """

        self._protocol = protocol

    @property
    def resource_type(self):
        """Gets the resource_type of this ItemForListUpstreamsOutput.  # noqa: E501


        :return: The resource_type of this ItemForListUpstreamsOutput.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ItemForListUpstreamsOutput.


        :param resource_type: The resource_type of this ItemForListUpstreamsOutput.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def source_type(self):
        """Gets the source_type of this ItemForListUpstreamsOutput.  # noqa: E501


        :return: The source_type of this ItemForListUpstreamsOutput.  # noqa: E501
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this ItemForListUpstreamsOutput.


        :param source_type: The source_type of this ItemForListUpstreamsOutput.  # noqa: E501
        :type: str
        """

        self._source_type = source_type

    @property
    def tags(self):
        """Gets the tags of this ItemForListUpstreamsOutput.  # noqa: E501


        :return: The tags of this ItemForListUpstreamsOutput.  # noqa: E501
        :rtype: list[TagForListUpstreamsOutput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ItemForListUpstreamsOutput.


        :param tags: The tags of this ItemForListUpstreamsOutput.  # noqa: E501
        :type: list[TagForListUpstreamsOutput]
        """

        self._tags = tags

    @property
    def tls_settings(self):
        """Gets the tls_settings of this ItemForListUpstreamsOutput.  # noqa: E501


        :return: The tls_settings of this ItemForListUpstreamsOutput.  # noqa: E501
        :rtype: TlsSettingsForListUpstreamsOutput
        """
        return self._tls_settings

    @tls_settings.setter
    def tls_settings(self, tls_settings):
        """Sets the tls_settings of this ItemForListUpstreamsOutput.


        :param tls_settings: The tls_settings of this ItemForListUpstreamsOutput.  # noqa: E501
        :type: TlsSettingsForListUpstreamsOutput
        """

        self._tls_settings = tls_settings

    @property
    def update_time(self):
        """Gets the update_time of this ItemForListUpstreamsOutput.  # noqa: E501


        :return: The update_time of this ItemForListUpstreamsOutput.  # noqa: E501
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ItemForListUpstreamsOutput.


        :param update_time: The update_time of this ItemForListUpstreamsOutput.  # noqa: E501
        :type: str
        """

        self._update_time = update_time

    @property
    def upstream_spec(self):
        """Gets the upstream_spec of this ItemForListUpstreamsOutput.  # noqa: E501


        :return: The upstream_spec of this ItemForListUpstreamsOutput.  # noqa: E501
        :rtype: UpstreamSpecForListUpstreamsOutput
        """
        return self._upstream_spec

    @upstream_spec.setter
    def upstream_spec(self, upstream_spec):
        """Sets the upstream_spec of this ItemForListUpstreamsOutput.


        :param upstream_spec: The upstream_spec of this ItemForListUpstreamsOutput.  # noqa: E501
        :type: UpstreamSpecForListUpstreamsOutput
        """

        self._upstream_spec = upstream_spec

    @property
    def version_details(self):
        """Gets the version_details of this ItemForListUpstreamsOutput.  # noqa: E501


        :return: The version_details of this ItemForListUpstreamsOutput.  # noqa: E501
        :rtype: list[VersionDetailForListUpstreamsOutput]
        """
        return self._version_details

    @version_details.setter
    def version_details(self, version_details):
        """Sets the version_details of this ItemForListUpstreamsOutput.


        :param version_details: The version_details of this ItemForListUpstreamsOutput.  # noqa: E501
        :type: list[VersionDetailForListUpstreamsOutput]
        """

        self._version_details = version_details

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
        if issubclass(ItemForListUpstreamsOutput, dict):
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
        if not isinstance(other, ItemForListUpstreamsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ItemForListUpstreamsOutput):
            return True

        return self.to_dict() != other.to_dict()
