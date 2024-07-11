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


class DescribeTransitRouterDirectConnectGatewayAttachmentsRequest(object):
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
        'direct_connect_gateway_id': 'str',
        'page_number': 'int',
        'page_size': 'int',
        'tag_filters': 'list[TagFilterForDescribeTransitRouterDirectConnectGatewayAttachmentsInput]',
        'transit_router_attachment_ids': 'list[str]',
        'transit_router_id': 'str'
    }

    attribute_map = {
        'direct_connect_gateway_id': 'DirectConnectGatewayId',
        'page_number': 'PageNumber',
        'page_size': 'PageSize',
        'tag_filters': 'TagFilters',
        'transit_router_attachment_ids': 'TransitRouterAttachmentIds',
        'transit_router_id': 'TransitRouterId'
    }

    def __init__(self, direct_connect_gateway_id=None, page_number=None, page_size=None, tag_filters=None, transit_router_attachment_ids=None, transit_router_id=None, _configuration=None):  # noqa: E501
        """DescribeTransitRouterDirectConnectGatewayAttachmentsRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._direct_connect_gateway_id = None
        self._page_number = None
        self._page_size = None
        self._tag_filters = None
        self._transit_router_attachment_ids = None
        self._transit_router_id = None
        self.discriminator = None

        if direct_connect_gateway_id is not None:
            self.direct_connect_gateway_id = direct_connect_gateway_id
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if tag_filters is not None:
            self.tag_filters = tag_filters
        if transit_router_attachment_ids is not None:
            self.transit_router_attachment_ids = transit_router_attachment_ids
        self.transit_router_id = transit_router_id

    @property
    def direct_connect_gateway_id(self):
        """Gets the direct_connect_gateway_id of this DescribeTransitRouterDirectConnectGatewayAttachmentsRequest.  # noqa: E501


        :return: The direct_connect_gateway_id of this DescribeTransitRouterDirectConnectGatewayAttachmentsRequest.  # noqa: E501
        :rtype: str
        """
        return self._direct_connect_gateway_id

    @direct_connect_gateway_id.setter
    def direct_connect_gateway_id(self, direct_connect_gateway_id):
        """Sets the direct_connect_gateway_id of this DescribeTransitRouterDirectConnectGatewayAttachmentsRequest.


        :param direct_connect_gateway_id: The direct_connect_gateway_id of this DescribeTransitRouterDirectConnectGatewayAttachmentsRequest.  # noqa: E501
        :type: str
        """

        self._direct_connect_gateway_id = direct_connect_gateway_id

    @property
    def page_number(self):
        """Gets the page_number of this DescribeTransitRouterDirectConnectGatewayAttachmentsRequest.  # noqa: E501


        :return: The page_number of this DescribeTransitRouterDirectConnectGatewayAttachmentsRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this DescribeTransitRouterDirectConnectGatewayAttachmentsRequest.


        :param page_number: The page_number of this DescribeTransitRouterDirectConnectGatewayAttachmentsRequest.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this DescribeTransitRouterDirectConnectGatewayAttachmentsRequest.  # noqa: E501


        :return: The page_size of this DescribeTransitRouterDirectConnectGatewayAttachmentsRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this DescribeTransitRouterDirectConnectGatewayAttachmentsRequest.


        :param page_size: The page_size of this DescribeTransitRouterDirectConnectGatewayAttachmentsRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def tag_filters(self):
        """Gets the tag_filters of this DescribeTransitRouterDirectConnectGatewayAttachmentsRequest.  # noqa: E501


        :return: The tag_filters of this DescribeTransitRouterDirectConnectGatewayAttachmentsRequest.  # noqa: E501
        :rtype: list[TagFilterForDescribeTransitRouterDirectConnectGatewayAttachmentsInput]
        """
        return self._tag_filters

    @tag_filters.setter
    def tag_filters(self, tag_filters):
        """Sets the tag_filters of this DescribeTransitRouterDirectConnectGatewayAttachmentsRequest.


        :param tag_filters: The tag_filters of this DescribeTransitRouterDirectConnectGatewayAttachmentsRequest.  # noqa: E501
        :type: list[TagFilterForDescribeTransitRouterDirectConnectGatewayAttachmentsInput]
        """

        self._tag_filters = tag_filters

    @property
    def transit_router_attachment_ids(self):
        """Gets the transit_router_attachment_ids of this DescribeTransitRouterDirectConnectGatewayAttachmentsRequest.  # noqa: E501


        :return: The transit_router_attachment_ids of this DescribeTransitRouterDirectConnectGatewayAttachmentsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._transit_router_attachment_ids

    @transit_router_attachment_ids.setter
    def transit_router_attachment_ids(self, transit_router_attachment_ids):
        """Sets the transit_router_attachment_ids of this DescribeTransitRouterDirectConnectGatewayAttachmentsRequest.


        :param transit_router_attachment_ids: The transit_router_attachment_ids of this DescribeTransitRouterDirectConnectGatewayAttachmentsRequest.  # noqa: E501
        :type: list[str]
        """

        self._transit_router_attachment_ids = transit_router_attachment_ids

    @property
    def transit_router_id(self):
        """Gets the transit_router_id of this DescribeTransitRouterDirectConnectGatewayAttachmentsRequest.  # noqa: E501


        :return: The transit_router_id of this DescribeTransitRouterDirectConnectGatewayAttachmentsRequest.  # noqa: E501
        :rtype: str
        """
        return self._transit_router_id

    @transit_router_id.setter
    def transit_router_id(self, transit_router_id):
        """Sets the transit_router_id of this DescribeTransitRouterDirectConnectGatewayAttachmentsRequest.


        :param transit_router_id: The transit_router_id of this DescribeTransitRouterDirectConnectGatewayAttachmentsRequest.  # noqa: E501
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
        if issubclass(DescribeTransitRouterDirectConnectGatewayAttachmentsRequest, dict):
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
        if not isinstance(other, DescribeTransitRouterDirectConnectGatewayAttachmentsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeTransitRouterDirectConnectGatewayAttachmentsRequest):
            return True

        return self.to_dict() != other.to_dict()