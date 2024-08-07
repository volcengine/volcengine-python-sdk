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


class DescribeTransitRouterForwardPolicyEntriesRequest(object):
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
        'source_cidr_block': 'str',
        'transit_router_forward_policy_entry_ids': 'list[str]',
        'transit_router_forward_policy_table_id': 'str',
        'transit_router_route_table_id': 'str'
    }

    attribute_map = {
        'page_number': 'PageNumber',
        'page_size': 'PageSize',
        'source_cidr_block': 'SourceCidrBlock',
        'transit_router_forward_policy_entry_ids': 'TransitRouterForwardPolicyEntryIds',
        'transit_router_forward_policy_table_id': 'TransitRouterForwardPolicyTableId',
        'transit_router_route_table_id': 'TransitRouterRouteTableId'
    }

    def __init__(self, page_number=None, page_size=None, source_cidr_block=None, transit_router_forward_policy_entry_ids=None, transit_router_forward_policy_table_id=None, transit_router_route_table_id=None, _configuration=None):  # noqa: E501
        """DescribeTransitRouterForwardPolicyEntriesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._page_number = None
        self._page_size = None
        self._source_cidr_block = None
        self._transit_router_forward_policy_entry_ids = None
        self._transit_router_forward_policy_table_id = None
        self._transit_router_route_table_id = None
        self.discriminator = None

        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if source_cidr_block is not None:
            self.source_cidr_block = source_cidr_block
        if transit_router_forward_policy_entry_ids is not None:
            self.transit_router_forward_policy_entry_ids = transit_router_forward_policy_entry_ids
        self.transit_router_forward_policy_table_id = transit_router_forward_policy_table_id
        if transit_router_route_table_id is not None:
            self.transit_router_route_table_id = transit_router_route_table_id

    @property
    def page_number(self):
        """Gets the page_number of this DescribeTransitRouterForwardPolicyEntriesRequest.  # noqa: E501


        :return: The page_number of this DescribeTransitRouterForwardPolicyEntriesRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this DescribeTransitRouterForwardPolicyEntriesRequest.


        :param page_number: The page_number of this DescribeTransitRouterForwardPolicyEntriesRequest.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this DescribeTransitRouterForwardPolicyEntriesRequest.  # noqa: E501


        :return: The page_size of this DescribeTransitRouterForwardPolicyEntriesRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this DescribeTransitRouterForwardPolicyEntriesRequest.


        :param page_size: The page_size of this DescribeTransitRouterForwardPolicyEntriesRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def source_cidr_block(self):
        """Gets the source_cidr_block of this DescribeTransitRouterForwardPolicyEntriesRequest.  # noqa: E501


        :return: The source_cidr_block of this DescribeTransitRouterForwardPolicyEntriesRequest.  # noqa: E501
        :rtype: str
        """
        return self._source_cidr_block

    @source_cidr_block.setter
    def source_cidr_block(self, source_cidr_block):
        """Sets the source_cidr_block of this DescribeTransitRouterForwardPolicyEntriesRequest.


        :param source_cidr_block: The source_cidr_block of this DescribeTransitRouterForwardPolicyEntriesRequest.  # noqa: E501
        :type: str
        """

        self._source_cidr_block = source_cidr_block

    @property
    def transit_router_forward_policy_entry_ids(self):
        """Gets the transit_router_forward_policy_entry_ids of this DescribeTransitRouterForwardPolicyEntriesRequest.  # noqa: E501


        :return: The transit_router_forward_policy_entry_ids of this DescribeTransitRouterForwardPolicyEntriesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._transit_router_forward_policy_entry_ids

    @transit_router_forward_policy_entry_ids.setter
    def transit_router_forward_policy_entry_ids(self, transit_router_forward_policy_entry_ids):
        """Sets the transit_router_forward_policy_entry_ids of this DescribeTransitRouterForwardPolicyEntriesRequest.


        :param transit_router_forward_policy_entry_ids: The transit_router_forward_policy_entry_ids of this DescribeTransitRouterForwardPolicyEntriesRequest.  # noqa: E501
        :type: list[str]
        """

        self._transit_router_forward_policy_entry_ids = transit_router_forward_policy_entry_ids

    @property
    def transit_router_forward_policy_table_id(self):
        """Gets the transit_router_forward_policy_table_id of this DescribeTransitRouterForwardPolicyEntriesRequest.  # noqa: E501


        :return: The transit_router_forward_policy_table_id of this DescribeTransitRouterForwardPolicyEntriesRequest.  # noqa: E501
        :rtype: str
        """
        return self._transit_router_forward_policy_table_id

    @transit_router_forward_policy_table_id.setter
    def transit_router_forward_policy_table_id(self, transit_router_forward_policy_table_id):
        """Sets the transit_router_forward_policy_table_id of this DescribeTransitRouterForwardPolicyEntriesRequest.


        :param transit_router_forward_policy_table_id: The transit_router_forward_policy_table_id of this DescribeTransitRouterForwardPolicyEntriesRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and transit_router_forward_policy_table_id is None:
            raise ValueError("Invalid value for `transit_router_forward_policy_table_id`, must not be `None`")  # noqa: E501

        self._transit_router_forward_policy_table_id = transit_router_forward_policy_table_id

    @property
    def transit_router_route_table_id(self):
        """Gets the transit_router_route_table_id of this DescribeTransitRouterForwardPolicyEntriesRequest.  # noqa: E501


        :return: The transit_router_route_table_id of this DescribeTransitRouterForwardPolicyEntriesRequest.  # noqa: E501
        :rtype: str
        """
        return self._transit_router_route_table_id

    @transit_router_route_table_id.setter
    def transit_router_route_table_id(self, transit_router_route_table_id):
        """Sets the transit_router_route_table_id of this DescribeTransitRouterForwardPolicyEntriesRequest.


        :param transit_router_route_table_id: The transit_router_route_table_id of this DescribeTransitRouterForwardPolicyEntriesRequest.  # noqa: E501
        :type: str
        """

        self._transit_router_route_table_id = transit_router_route_table_id

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
        if issubclass(DescribeTransitRouterForwardPolicyEntriesRequest, dict):
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
        if not isinstance(other, DescribeTransitRouterForwardPolicyEntriesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeTransitRouterForwardPolicyEntriesRequest):
            return True

        return self.to_dict() != other.to_dict()
