# coding: utf-8

"""
    transitrouter

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class CreateTransitRouterDirectConnectGatewayAttachmentRequest(object):
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
        'client_token': 'str',
        'description': 'str',
        'direct_connect_gateway_id': 'str',
        'tags': 'list[TagForCreateTransitRouterDirectConnectGatewayAttachmentInput]',
        'transit_router_attachment_name': 'str',
        'transit_router_id': 'str'
    }

    attribute_map = {
        'client_token': 'ClientToken',
        'description': 'Description',
        'direct_connect_gateway_id': 'DirectConnectGatewayId',
        'tags': 'Tags',
        'transit_router_attachment_name': 'TransitRouterAttachmentName',
        'transit_router_id': 'TransitRouterId'
    }

    def __init__(self, client_token=None, description=None, direct_connect_gateway_id=None, tags=None, transit_router_attachment_name=None, transit_router_id=None, _configuration=None):  # noqa: E501
        """CreateTransitRouterDirectConnectGatewayAttachmentRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._client_token = None
        self._description = None
        self._direct_connect_gateway_id = None
        self._tags = None
        self._transit_router_attachment_name = None
        self._transit_router_id = None
        self.discriminator = None

        if client_token is not None:
            self.client_token = client_token
        if description is not None:
            self.description = description
        self.direct_connect_gateway_id = direct_connect_gateway_id
        if tags is not None:
            self.tags = tags
        if transit_router_attachment_name is not None:
            self.transit_router_attachment_name = transit_router_attachment_name
        self.transit_router_id = transit_router_id

    @property
    def client_token(self):
        """Gets the client_token of this CreateTransitRouterDirectConnectGatewayAttachmentRequest.  # noqa: E501


        :return: The client_token of this CreateTransitRouterDirectConnectGatewayAttachmentRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_token

    @client_token.setter
    def client_token(self, client_token):
        """Sets the client_token of this CreateTransitRouterDirectConnectGatewayAttachmentRequest.


        :param client_token: The client_token of this CreateTransitRouterDirectConnectGatewayAttachmentRequest.  # noqa: E501
        :type: str
        """

        self._client_token = client_token

    @property
    def description(self):
        """Gets the description of this CreateTransitRouterDirectConnectGatewayAttachmentRequest.  # noqa: E501


        :return: The description of this CreateTransitRouterDirectConnectGatewayAttachmentRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateTransitRouterDirectConnectGatewayAttachmentRequest.


        :param description: The description of this CreateTransitRouterDirectConnectGatewayAttachmentRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def direct_connect_gateway_id(self):
        """Gets the direct_connect_gateway_id of this CreateTransitRouterDirectConnectGatewayAttachmentRequest.  # noqa: E501


        :return: The direct_connect_gateway_id of this CreateTransitRouterDirectConnectGatewayAttachmentRequest.  # noqa: E501
        :rtype: str
        """
        return self._direct_connect_gateway_id

    @direct_connect_gateway_id.setter
    def direct_connect_gateway_id(self, direct_connect_gateway_id):
        """Sets the direct_connect_gateway_id of this CreateTransitRouterDirectConnectGatewayAttachmentRequest.


        :param direct_connect_gateway_id: The direct_connect_gateway_id of this CreateTransitRouterDirectConnectGatewayAttachmentRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and direct_connect_gateway_id is None:
            raise ValueError("Invalid value for `direct_connect_gateway_id`, must not be `None`")  # noqa: E501

        self._direct_connect_gateway_id = direct_connect_gateway_id

    @property
    def tags(self):
        """Gets the tags of this CreateTransitRouterDirectConnectGatewayAttachmentRequest.  # noqa: E501


        :return: The tags of this CreateTransitRouterDirectConnectGatewayAttachmentRequest.  # noqa: E501
        :rtype: list[TagForCreateTransitRouterDirectConnectGatewayAttachmentInput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateTransitRouterDirectConnectGatewayAttachmentRequest.


        :param tags: The tags of this CreateTransitRouterDirectConnectGatewayAttachmentRequest.  # noqa: E501
        :type: list[TagForCreateTransitRouterDirectConnectGatewayAttachmentInput]
        """

        self._tags = tags

    @property
    def transit_router_attachment_name(self):
        """Gets the transit_router_attachment_name of this CreateTransitRouterDirectConnectGatewayAttachmentRequest.  # noqa: E501


        :return: The transit_router_attachment_name of this CreateTransitRouterDirectConnectGatewayAttachmentRequest.  # noqa: E501
        :rtype: str
        """
        return self._transit_router_attachment_name

    @transit_router_attachment_name.setter
    def transit_router_attachment_name(self, transit_router_attachment_name):
        """Sets the transit_router_attachment_name of this CreateTransitRouterDirectConnectGatewayAttachmentRequest.


        :param transit_router_attachment_name: The transit_router_attachment_name of this CreateTransitRouterDirectConnectGatewayAttachmentRequest.  # noqa: E501
        :type: str
        """

        self._transit_router_attachment_name = transit_router_attachment_name

    @property
    def transit_router_id(self):
        """Gets the transit_router_id of this CreateTransitRouterDirectConnectGatewayAttachmentRequest.  # noqa: E501


        :return: The transit_router_id of this CreateTransitRouterDirectConnectGatewayAttachmentRequest.  # noqa: E501
        :rtype: str
        """
        return self._transit_router_id

    @transit_router_id.setter
    def transit_router_id(self, transit_router_id):
        """Sets the transit_router_id of this CreateTransitRouterDirectConnectGatewayAttachmentRequest.


        :param transit_router_id: The transit_router_id of this CreateTransitRouterDirectConnectGatewayAttachmentRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and transit_router_id is None:
            raise ValueError("Invalid value for `transit_router_id`, must not be `None`")  # noqa: E501

        self._transit_router_id = transit_router_id

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
        if issubclass(CreateTransitRouterDirectConnectGatewayAttachmentRequest, dict):
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
        if not isinstance(other, CreateTransitRouterDirectConnectGatewayAttachmentRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateTransitRouterDirectConnectGatewayAttachmentRequest):
            return True

        return self.to_dict() != other.to_dict()
