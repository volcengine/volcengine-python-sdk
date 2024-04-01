# coding: utf-8

"""
    privatelink

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class CreateUniqueResourceTypeVpcEndpointServiceRequest(object):
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
        'auto_accept_enabled': 'bool',
        'client_token': 'str',
        'description': 'str',
        'project_name': 'str',
        'resource': 'ResourceForCreateUniqueResourceTypeVpcEndpointServiceInput',
        'service_resource_type': 'str',
        'tags': 'TagsForCreateUniqueResourceTypeVpcEndpointServiceInput',
        'zone_ids': 'list[str]'
    }

    attribute_map = {
        'auto_accept_enabled': 'AutoAcceptEnabled',
        'client_token': 'ClientToken',
        'description': 'Description',
        'project_name': 'ProjectName',
        'resource': 'Resource',
        'service_resource_type': 'ServiceResourceType',
        'tags': 'Tags',
        'zone_ids': 'ZoneIds'
    }

    def __init__(self, auto_accept_enabled=None, client_token=None, description=None, project_name=None, resource=None, service_resource_type=None, tags=None, zone_ids=None, _configuration=None):  # noqa: E501
        """CreateUniqueResourceTypeVpcEndpointServiceRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._auto_accept_enabled = None
        self._client_token = None
        self._description = None
        self._project_name = None
        self._resource = None
        self._service_resource_type = None
        self._tags = None
        self._zone_ids = None
        self.discriminator = None

        if auto_accept_enabled is not None:
            self.auto_accept_enabled = auto_accept_enabled
        if client_token is not None:
            self.client_token = client_token
        if description is not None:
            self.description = description
        if project_name is not None:
            self.project_name = project_name
        if resource is not None:
            self.resource = resource
        if service_resource_type is not None:
            self.service_resource_type = service_resource_type
        if tags is not None:
            self.tags = tags
        if zone_ids is not None:
            self.zone_ids = zone_ids

    @property
    def auto_accept_enabled(self):
        """Gets the auto_accept_enabled of this CreateUniqueResourceTypeVpcEndpointServiceRequest.  # noqa: E501


        :return: The auto_accept_enabled of this CreateUniqueResourceTypeVpcEndpointServiceRequest.  # noqa: E501
        :rtype: bool
        """
        return self._auto_accept_enabled

    @auto_accept_enabled.setter
    def auto_accept_enabled(self, auto_accept_enabled):
        """Sets the auto_accept_enabled of this CreateUniqueResourceTypeVpcEndpointServiceRequest.


        :param auto_accept_enabled: The auto_accept_enabled of this CreateUniqueResourceTypeVpcEndpointServiceRequest.  # noqa: E501
        :type: bool
        """

        self._auto_accept_enabled = auto_accept_enabled

    @property
    def client_token(self):
        """Gets the client_token of this CreateUniqueResourceTypeVpcEndpointServiceRequest.  # noqa: E501


        :return: The client_token of this CreateUniqueResourceTypeVpcEndpointServiceRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_token

    @client_token.setter
    def client_token(self, client_token):
        """Sets the client_token of this CreateUniqueResourceTypeVpcEndpointServiceRequest.


        :param client_token: The client_token of this CreateUniqueResourceTypeVpcEndpointServiceRequest.  # noqa: E501
        :type: str
        """

        self._client_token = client_token

    @property
    def description(self):
        """Gets the description of this CreateUniqueResourceTypeVpcEndpointServiceRequest.  # noqa: E501


        :return: The description of this CreateUniqueResourceTypeVpcEndpointServiceRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateUniqueResourceTypeVpcEndpointServiceRequest.


        :param description: The description of this CreateUniqueResourceTypeVpcEndpointServiceRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def project_name(self):
        """Gets the project_name of this CreateUniqueResourceTypeVpcEndpointServiceRequest.  # noqa: E501


        :return: The project_name of this CreateUniqueResourceTypeVpcEndpointServiceRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this CreateUniqueResourceTypeVpcEndpointServiceRequest.


        :param project_name: The project_name of this CreateUniqueResourceTypeVpcEndpointServiceRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def resource(self):
        """Gets the resource of this CreateUniqueResourceTypeVpcEndpointServiceRequest.  # noqa: E501


        :return: The resource of this CreateUniqueResourceTypeVpcEndpointServiceRequest.  # noqa: E501
        :rtype: ResourceForCreateUniqueResourceTypeVpcEndpointServiceInput
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this CreateUniqueResourceTypeVpcEndpointServiceRequest.


        :param resource: The resource of this CreateUniqueResourceTypeVpcEndpointServiceRequest.  # noqa: E501
        :type: ResourceForCreateUniqueResourceTypeVpcEndpointServiceInput
        """

        self._resource = resource

    @property
    def service_resource_type(self):
        """Gets the service_resource_type of this CreateUniqueResourceTypeVpcEndpointServiceRequest.  # noqa: E501


        :return: The service_resource_type of this CreateUniqueResourceTypeVpcEndpointServiceRequest.  # noqa: E501
        :rtype: str
        """
        return self._service_resource_type

    @service_resource_type.setter
    def service_resource_type(self, service_resource_type):
        """Sets the service_resource_type of this CreateUniqueResourceTypeVpcEndpointServiceRequest.


        :param service_resource_type: The service_resource_type of this CreateUniqueResourceTypeVpcEndpointServiceRequest.  # noqa: E501
        :type: str
        """

        self._service_resource_type = service_resource_type

    @property
    def tags(self):
        """Gets the tags of this CreateUniqueResourceTypeVpcEndpointServiceRequest.  # noqa: E501


        :return: The tags of this CreateUniqueResourceTypeVpcEndpointServiceRequest.  # noqa: E501
        :rtype: TagsForCreateUniqueResourceTypeVpcEndpointServiceInput
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateUniqueResourceTypeVpcEndpointServiceRequest.


        :param tags: The tags of this CreateUniqueResourceTypeVpcEndpointServiceRequest.  # noqa: E501
        :type: TagsForCreateUniqueResourceTypeVpcEndpointServiceInput
        """

        self._tags = tags

    @property
    def zone_ids(self):
        """Gets the zone_ids of this CreateUniqueResourceTypeVpcEndpointServiceRequest.  # noqa: E501


        :return: The zone_ids of this CreateUniqueResourceTypeVpcEndpointServiceRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._zone_ids

    @zone_ids.setter
    def zone_ids(self, zone_ids):
        """Sets the zone_ids of this CreateUniqueResourceTypeVpcEndpointServiceRequest.


        :param zone_ids: The zone_ids of this CreateUniqueResourceTypeVpcEndpointServiceRequest.  # noqa: E501
        :type: list[str]
        """

        self._zone_ids = zone_ids

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
        if issubclass(CreateUniqueResourceTypeVpcEndpointServiceRequest, dict):
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
        if not isinstance(other, CreateUniqueResourceTypeVpcEndpointServiceRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateUniqueResourceTypeVpcEndpointServiceRequest):
            return True

        return self.to_dict() != other.to_dict()
