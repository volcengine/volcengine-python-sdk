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


class ItemForListGatewayServicesOutput(object):
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
        'auth_spec': 'AuthSpecForListGatewayServicesOutput',
        'comments': 'str',
        'create_time': 'str',
        'custom_domains': 'list[CustomDomainForListGatewayServicesOutput]',
        'domains': 'list[DomainForListGatewayServicesOutput]',
        'gateway_id': 'str',
        'gateway_name': 'str',
        'id': 'str',
        'message': 'str',
        'name': 'str',
        'protocol': 'list[str]',
        'status': 'str',
        'tags': 'list[TagForListGatewayServicesOutput]'
    }

    attribute_map = {
        'auth_spec': 'AuthSpec',
        'comments': 'Comments',
        'create_time': 'CreateTime',
        'custom_domains': 'CustomDomains',
        'domains': 'Domains',
        'gateway_id': 'GatewayId',
        'gateway_name': 'GatewayName',
        'id': 'Id',
        'message': 'Message',
        'name': 'Name',
        'protocol': 'Protocol',
        'status': 'Status',
        'tags': 'Tags'
    }

    def __init__(self, auth_spec=None, comments=None, create_time=None, custom_domains=None, domains=None, gateway_id=None, gateway_name=None, id=None, message=None, name=None, protocol=None, status=None, tags=None, _configuration=None):  # noqa: E501
        """ItemForListGatewayServicesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._auth_spec = None
        self._comments = None
        self._create_time = None
        self._custom_domains = None
        self._domains = None
        self._gateway_id = None
        self._gateway_name = None
        self._id = None
        self._message = None
        self._name = None
        self._protocol = None
        self._status = None
        self._tags = None
        self.discriminator = None

        if auth_spec is not None:
            self.auth_spec = auth_spec
        if comments is not None:
            self.comments = comments
        if create_time is not None:
            self.create_time = create_time
        if custom_domains is not None:
            self.custom_domains = custom_domains
        if domains is not None:
            self.domains = domains
        if gateway_id is not None:
            self.gateway_id = gateway_id
        if gateway_name is not None:
            self.gateway_name = gateway_name
        if id is not None:
            self.id = id
        if message is not None:
            self.message = message
        if name is not None:
            self.name = name
        if protocol is not None:
            self.protocol = protocol
        if status is not None:
            self.status = status
        if tags is not None:
            self.tags = tags

    @property
    def auth_spec(self):
        """Gets the auth_spec of this ItemForListGatewayServicesOutput.  # noqa: E501


        :return: The auth_spec of this ItemForListGatewayServicesOutput.  # noqa: E501
        :rtype: AuthSpecForListGatewayServicesOutput
        """
        return self._auth_spec

    @auth_spec.setter
    def auth_spec(self, auth_spec):
        """Sets the auth_spec of this ItemForListGatewayServicesOutput.


        :param auth_spec: The auth_spec of this ItemForListGatewayServicesOutput.  # noqa: E501
        :type: AuthSpecForListGatewayServicesOutput
        """

        self._auth_spec = auth_spec

    @property
    def comments(self):
        """Gets the comments of this ItemForListGatewayServicesOutput.  # noqa: E501


        :return: The comments of this ItemForListGatewayServicesOutput.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this ItemForListGatewayServicesOutput.


        :param comments: The comments of this ItemForListGatewayServicesOutput.  # noqa: E501
        :type: str
        """

        self._comments = comments

    @property
    def create_time(self):
        """Gets the create_time of this ItemForListGatewayServicesOutput.  # noqa: E501


        :return: The create_time of this ItemForListGatewayServicesOutput.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ItemForListGatewayServicesOutput.


        :param create_time: The create_time of this ItemForListGatewayServicesOutput.  # noqa: E501
        :type: str
        """

        self._create_time = create_time

    @property
    def custom_domains(self):
        """Gets the custom_domains of this ItemForListGatewayServicesOutput.  # noqa: E501


        :return: The custom_domains of this ItemForListGatewayServicesOutput.  # noqa: E501
        :rtype: list[CustomDomainForListGatewayServicesOutput]
        """
        return self._custom_domains

    @custom_domains.setter
    def custom_domains(self, custom_domains):
        """Sets the custom_domains of this ItemForListGatewayServicesOutput.


        :param custom_domains: The custom_domains of this ItemForListGatewayServicesOutput.  # noqa: E501
        :type: list[CustomDomainForListGatewayServicesOutput]
        """

        self._custom_domains = custom_domains

    @property
    def domains(self):
        """Gets the domains of this ItemForListGatewayServicesOutput.  # noqa: E501


        :return: The domains of this ItemForListGatewayServicesOutput.  # noqa: E501
        :rtype: list[DomainForListGatewayServicesOutput]
        """
        return self._domains

    @domains.setter
    def domains(self, domains):
        """Sets the domains of this ItemForListGatewayServicesOutput.


        :param domains: The domains of this ItemForListGatewayServicesOutput.  # noqa: E501
        :type: list[DomainForListGatewayServicesOutput]
        """

        self._domains = domains

    @property
    def gateway_id(self):
        """Gets the gateway_id of this ItemForListGatewayServicesOutput.  # noqa: E501


        :return: The gateway_id of this ItemForListGatewayServicesOutput.  # noqa: E501
        :rtype: str
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, gateway_id):
        """Sets the gateway_id of this ItemForListGatewayServicesOutput.


        :param gateway_id: The gateway_id of this ItemForListGatewayServicesOutput.  # noqa: E501
        :type: str
        """

        self._gateway_id = gateway_id

    @property
    def gateway_name(self):
        """Gets the gateway_name of this ItemForListGatewayServicesOutput.  # noqa: E501


        :return: The gateway_name of this ItemForListGatewayServicesOutput.  # noqa: E501
        :rtype: str
        """
        return self._gateway_name

    @gateway_name.setter
    def gateway_name(self, gateway_name):
        """Sets the gateway_name of this ItemForListGatewayServicesOutput.


        :param gateway_name: The gateway_name of this ItemForListGatewayServicesOutput.  # noqa: E501
        :type: str
        """

        self._gateway_name = gateway_name

    @property
    def id(self):
        """Gets the id of this ItemForListGatewayServicesOutput.  # noqa: E501


        :return: The id of this ItemForListGatewayServicesOutput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ItemForListGatewayServicesOutput.


        :param id: The id of this ItemForListGatewayServicesOutput.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def message(self):
        """Gets the message of this ItemForListGatewayServicesOutput.  # noqa: E501


        :return: The message of this ItemForListGatewayServicesOutput.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ItemForListGatewayServicesOutput.


        :param message: The message of this ItemForListGatewayServicesOutput.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def name(self):
        """Gets the name of this ItemForListGatewayServicesOutput.  # noqa: E501


        :return: The name of this ItemForListGatewayServicesOutput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ItemForListGatewayServicesOutput.


        :param name: The name of this ItemForListGatewayServicesOutput.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def protocol(self):
        """Gets the protocol of this ItemForListGatewayServicesOutput.  # noqa: E501


        :return: The protocol of this ItemForListGatewayServicesOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ItemForListGatewayServicesOutput.


        :param protocol: The protocol of this ItemForListGatewayServicesOutput.  # noqa: E501
        :type: list[str]
        """

        self._protocol = protocol

    @property
    def status(self):
        """Gets the status of this ItemForListGatewayServicesOutput.  # noqa: E501


        :return: The status of this ItemForListGatewayServicesOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ItemForListGatewayServicesOutput.


        :param status: The status of this ItemForListGatewayServicesOutput.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def tags(self):
        """Gets the tags of this ItemForListGatewayServicesOutput.  # noqa: E501


        :return: The tags of this ItemForListGatewayServicesOutput.  # noqa: E501
        :rtype: list[TagForListGatewayServicesOutput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ItemForListGatewayServicesOutput.


        :param tags: The tags of this ItemForListGatewayServicesOutput.  # noqa: E501
        :type: list[TagForListGatewayServicesOutput]
        """

        self._tags = tags

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
        if issubclass(ItemForListGatewayServicesOutput, dict):
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
        if not isinstance(other, ItemForListGatewayServicesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ItemForListGatewayServicesOutput):
            return True

        return self.to_dict() != other.to_dict()
