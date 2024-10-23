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


class DescribeTransitRouterAttachmentsRequest(object):
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
        'resource_id': 'str',
        'resource_type': 'str',
        'tag_filters': 'list[TagFilterForDescribeTransitRouterAttachmentsInput]',
        'transit_router_attachment_ids': 'list[str]',
        'transit_router_forward_policy_table_id': 'str',
        'transit_router_id': 'str',
        'transit_router_traffic_qos_marking_policy_id': 'str',
        'transit_router_traffic_qos_queue_policy_id': 'str'
    }

    attribute_map = {
        'page_number': 'PageNumber',
        'page_size': 'PageSize',
        'resource_id': 'ResourceId',
        'resource_type': 'ResourceType',
        'tag_filters': 'TagFilters',
        'transit_router_attachment_ids': 'TransitRouterAttachmentIds',
        'transit_router_forward_policy_table_id': 'TransitRouterForwardPolicyTableId',
        'transit_router_id': 'TransitRouterId',
        'transit_router_traffic_qos_marking_policy_id': 'TransitRouterTrafficQosMarkingPolicyId',
        'transit_router_traffic_qos_queue_policy_id': 'TransitRouterTrafficQosQueuePolicyId'
    }

    def __init__(self, page_number=None, page_size=None, resource_id=None, resource_type=None, tag_filters=None, transit_router_attachment_ids=None, transit_router_forward_policy_table_id=None, transit_router_id=None, transit_router_traffic_qos_marking_policy_id=None, transit_router_traffic_qos_queue_policy_id=None, _configuration=None):  # noqa: E501
        """DescribeTransitRouterAttachmentsRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._page_number = None
        self._page_size = None
        self._resource_id = None
        self._resource_type = None
        self._tag_filters = None
        self._transit_router_attachment_ids = None
        self._transit_router_forward_policy_table_id = None
        self._transit_router_id = None
        self._transit_router_traffic_qos_marking_policy_id = None
        self._transit_router_traffic_qos_queue_policy_id = None
        self.discriminator = None

        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_type is not None:
            self.resource_type = resource_type
        if tag_filters is not None:
            self.tag_filters = tag_filters
        if transit_router_attachment_ids is not None:
            self.transit_router_attachment_ids = transit_router_attachment_ids
        if transit_router_forward_policy_table_id is not None:
            self.transit_router_forward_policy_table_id = transit_router_forward_policy_table_id
        if transit_router_id is not None:
            self.transit_router_id = transit_router_id
        if transit_router_traffic_qos_marking_policy_id is not None:
            self.transit_router_traffic_qos_marking_policy_id = transit_router_traffic_qos_marking_policy_id
        if transit_router_traffic_qos_queue_policy_id is not None:
            self.transit_router_traffic_qos_queue_policy_id = transit_router_traffic_qos_queue_policy_id

    @property
    def page_number(self):
        """Gets the page_number of this DescribeTransitRouterAttachmentsRequest.  # noqa: E501


        :return: The page_number of this DescribeTransitRouterAttachmentsRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this DescribeTransitRouterAttachmentsRequest.


        :param page_number: The page_number of this DescribeTransitRouterAttachmentsRequest.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this DescribeTransitRouterAttachmentsRequest.  # noqa: E501


        :return: The page_size of this DescribeTransitRouterAttachmentsRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this DescribeTransitRouterAttachmentsRequest.


        :param page_size: The page_size of this DescribeTransitRouterAttachmentsRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def resource_id(self):
        """Gets the resource_id of this DescribeTransitRouterAttachmentsRequest.  # noqa: E501


        :return: The resource_id of this DescribeTransitRouterAttachmentsRequest.  # noqa: E501
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this DescribeTransitRouterAttachmentsRequest.


        :param resource_id: The resource_id of this DescribeTransitRouterAttachmentsRequest.  # noqa: E501
        :type: str
        """

        self._resource_id = resource_id

    @property
    def resource_type(self):
        """Gets the resource_type of this DescribeTransitRouterAttachmentsRequest.  # noqa: E501


        :return: The resource_type of this DescribeTransitRouterAttachmentsRequest.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this DescribeTransitRouterAttachmentsRequest.


        :param resource_type: The resource_type of this DescribeTransitRouterAttachmentsRequest.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def tag_filters(self):
        """Gets the tag_filters of this DescribeTransitRouterAttachmentsRequest.  # noqa: E501


        :return: The tag_filters of this DescribeTransitRouterAttachmentsRequest.  # noqa: E501
        :rtype: list[TagFilterForDescribeTransitRouterAttachmentsInput]
        """
        return self._tag_filters

    @tag_filters.setter
    def tag_filters(self, tag_filters):
        """Sets the tag_filters of this DescribeTransitRouterAttachmentsRequest.


        :param tag_filters: The tag_filters of this DescribeTransitRouterAttachmentsRequest.  # noqa: E501
        :type: list[TagFilterForDescribeTransitRouterAttachmentsInput]
        """

        self._tag_filters = tag_filters

    @property
    def transit_router_attachment_ids(self):
        """Gets the transit_router_attachment_ids of this DescribeTransitRouterAttachmentsRequest.  # noqa: E501


        :return: The transit_router_attachment_ids of this DescribeTransitRouterAttachmentsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._transit_router_attachment_ids

    @transit_router_attachment_ids.setter
    def transit_router_attachment_ids(self, transit_router_attachment_ids):
        """Sets the transit_router_attachment_ids of this DescribeTransitRouterAttachmentsRequest.


        :param transit_router_attachment_ids: The transit_router_attachment_ids of this DescribeTransitRouterAttachmentsRequest.  # noqa: E501
        :type: list[str]
        """

        self._transit_router_attachment_ids = transit_router_attachment_ids

    @property
    def transit_router_forward_policy_table_id(self):
        """Gets the transit_router_forward_policy_table_id of this DescribeTransitRouterAttachmentsRequest.  # noqa: E501


        :return: The transit_router_forward_policy_table_id of this DescribeTransitRouterAttachmentsRequest.  # noqa: E501
        :rtype: str
        """
        return self._transit_router_forward_policy_table_id

    @transit_router_forward_policy_table_id.setter
    def transit_router_forward_policy_table_id(self, transit_router_forward_policy_table_id):
        """Sets the transit_router_forward_policy_table_id of this DescribeTransitRouterAttachmentsRequest.


        :param transit_router_forward_policy_table_id: The transit_router_forward_policy_table_id of this DescribeTransitRouterAttachmentsRequest.  # noqa: E501
        :type: str
        """

        self._transit_router_forward_policy_table_id = transit_router_forward_policy_table_id

    @property
    def transit_router_id(self):
        """Gets the transit_router_id of this DescribeTransitRouterAttachmentsRequest.  # noqa: E501


        :return: The transit_router_id of this DescribeTransitRouterAttachmentsRequest.  # noqa: E501
        :rtype: str
        """
        return self._transit_router_id

    @transit_router_id.setter
    def transit_router_id(self, transit_router_id):
        """Sets the transit_router_id of this DescribeTransitRouterAttachmentsRequest.


        :param transit_router_id: The transit_router_id of this DescribeTransitRouterAttachmentsRequest.  # noqa: E501
        :type: str
        """

        self._transit_router_id = transit_router_id

    @property
    def transit_router_traffic_qos_marking_policy_id(self):
        """Gets the transit_router_traffic_qos_marking_policy_id of this DescribeTransitRouterAttachmentsRequest.  # noqa: E501


        :return: The transit_router_traffic_qos_marking_policy_id of this DescribeTransitRouterAttachmentsRequest.  # noqa: E501
        :rtype: str
        """
        return self._transit_router_traffic_qos_marking_policy_id

    @transit_router_traffic_qos_marking_policy_id.setter
    def transit_router_traffic_qos_marking_policy_id(self, transit_router_traffic_qos_marking_policy_id):
        """Sets the transit_router_traffic_qos_marking_policy_id of this DescribeTransitRouterAttachmentsRequest.


        :param transit_router_traffic_qos_marking_policy_id: The transit_router_traffic_qos_marking_policy_id of this DescribeTransitRouterAttachmentsRequest.  # noqa: E501
        :type: str
        """

        self._transit_router_traffic_qos_marking_policy_id = transit_router_traffic_qos_marking_policy_id

    @property
    def transit_router_traffic_qos_queue_policy_id(self):
        """Gets the transit_router_traffic_qos_queue_policy_id of this DescribeTransitRouterAttachmentsRequest.  # noqa: E501


        :return: The transit_router_traffic_qos_queue_policy_id of this DescribeTransitRouterAttachmentsRequest.  # noqa: E501
        :rtype: str
        """
        return self._transit_router_traffic_qos_queue_policy_id

    @transit_router_traffic_qos_queue_policy_id.setter
    def transit_router_traffic_qos_queue_policy_id(self, transit_router_traffic_qos_queue_policy_id):
        """Sets the transit_router_traffic_qos_queue_policy_id of this DescribeTransitRouterAttachmentsRequest.


        :param transit_router_traffic_qos_queue_policy_id: The transit_router_traffic_qos_queue_policy_id of this DescribeTransitRouterAttachmentsRequest.  # noqa: E501
        :type: str
        """

        self._transit_router_traffic_qos_queue_policy_id = transit_router_traffic_qos_queue_policy_id

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
        if issubclass(DescribeTransitRouterAttachmentsRequest, dict):
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
        if not isinstance(other, DescribeTransitRouterAttachmentsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeTransitRouterAttachmentsRequest):
            return True

        return self.to_dict() != other.to_dict()
