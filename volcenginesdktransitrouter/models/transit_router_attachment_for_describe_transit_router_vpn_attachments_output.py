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


class TransitRouterAttachmentForDescribeTransitRouterVpnAttachmentsOutput(object):
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
        'auto_publish_route_enabled': 'bool',
        'creation_time': 'str',
        'description': 'str',
        'status': 'str',
        'tags': 'list[TagForDescribeTransitRouterVpnAttachmentsOutput]',
        'transit_router_attachment_id': 'str',
        'transit_router_attachment_name': 'str',
        'transit_router_id': 'str',
        'update_time': 'str',
        'vpn_connection_id': 'str',
        'zone_id': 'str'
    }

    attribute_map = {
        'auto_publish_route_enabled': 'AutoPublishRouteEnabled',
        'creation_time': 'CreationTime',
        'description': 'Description',
        'status': 'Status',
        'tags': 'Tags',
        'transit_router_attachment_id': 'TransitRouterAttachmentId',
        'transit_router_attachment_name': 'TransitRouterAttachmentName',
        'transit_router_id': 'TransitRouterId',
        'update_time': 'UpdateTime',
        'vpn_connection_id': 'VpnConnectionId',
        'zone_id': 'ZoneId'
    }

    def __init__(self, auto_publish_route_enabled=None, creation_time=None, description=None, status=None, tags=None, transit_router_attachment_id=None, transit_router_attachment_name=None, transit_router_id=None, update_time=None, vpn_connection_id=None, zone_id=None, _configuration=None):  # noqa: E501
        """TransitRouterAttachmentForDescribeTransitRouterVpnAttachmentsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._auto_publish_route_enabled = None
        self._creation_time = None
        self._description = None
        self._status = None
        self._tags = None
        self._transit_router_attachment_id = None
        self._transit_router_attachment_name = None
        self._transit_router_id = None
        self._update_time = None
        self._vpn_connection_id = None
        self._zone_id = None
        self.discriminator = None

        if auto_publish_route_enabled is not None:
            self.auto_publish_route_enabled = auto_publish_route_enabled
        if creation_time is not None:
            self.creation_time = creation_time
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if tags is not None:
            self.tags = tags
        if transit_router_attachment_id is not None:
            self.transit_router_attachment_id = transit_router_attachment_id
        if transit_router_attachment_name is not None:
            self.transit_router_attachment_name = transit_router_attachment_name
        if transit_router_id is not None:
            self.transit_router_id = transit_router_id
        if update_time is not None:
            self.update_time = update_time
        if vpn_connection_id is not None:
            self.vpn_connection_id = vpn_connection_id
        if zone_id is not None:
            self.zone_id = zone_id

    @property
    def auto_publish_route_enabled(self):
        """Gets the auto_publish_route_enabled of this TransitRouterAttachmentForDescribeTransitRouterVpnAttachmentsOutput.  # noqa: E501


        :return: The auto_publish_route_enabled of this TransitRouterAttachmentForDescribeTransitRouterVpnAttachmentsOutput.  # noqa: E501
        :rtype: bool
        """
        return self._auto_publish_route_enabled

    @auto_publish_route_enabled.setter
    def auto_publish_route_enabled(self, auto_publish_route_enabled):
        """Sets the auto_publish_route_enabled of this TransitRouterAttachmentForDescribeTransitRouterVpnAttachmentsOutput.


        :param auto_publish_route_enabled: The auto_publish_route_enabled of this TransitRouterAttachmentForDescribeTransitRouterVpnAttachmentsOutput.  # noqa: E501
        :type: bool
        """

        self._auto_publish_route_enabled = auto_publish_route_enabled

    @property
    def creation_time(self):
        """Gets the creation_time of this TransitRouterAttachmentForDescribeTransitRouterVpnAttachmentsOutput.  # noqa: E501


        :return: The creation_time of this TransitRouterAttachmentForDescribeTransitRouterVpnAttachmentsOutput.  # noqa: E501
        :rtype: str
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this TransitRouterAttachmentForDescribeTransitRouterVpnAttachmentsOutput.


        :param creation_time: The creation_time of this TransitRouterAttachmentForDescribeTransitRouterVpnAttachmentsOutput.  # noqa: E501
        :type: str
        """

        self._creation_time = creation_time

    @property
    def description(self):
        """Gets the description of this TransitRouterAttachmentForDescribeTransitRouterVpnAttachmentsOutput.  # noqa: E501


        :return: The description of this TransitRouterAttachmentForDescribeTransitRouterVpnAttachmentsOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TransitRouterAttachmentForDescribeTransitRouterVpnAttachmentsOutput.


        :param description: The description of this TransitRouterAttachmentForDescribeTransitRouterVpnAttachmentsOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def status(self):
        """Gets the status of this TransitRouterAttachmentForDescribeTransitRouterVpnAttachmentsOutput.  # noqa: E501


        :return: The status of this TransitRouterAttachmentForDescribeTransitRouterVpnAttachmentsOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TransitRouterAttachmentForDescribeTransitRouterVpnAttachmentsOutput.


        :param status: The status of this TransitRouterAttachmentForDescribeTransitRouterVpnAttachmentsOutput.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def tags(self):
        """Gets the tags of this TransitRouterAttachmentForDescribeTransitRouterVpnAttachmentsOutput.  # noqa: E501


        :return: The tags of this TransitRouterAttachmentForDescribeTransitRouterVpnAttachmentsOutput.  # noqa: E501
        :rtype: list[TagForDescribeTransitRouterVpnAttachmentsOutput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this TransitRouterAttachmentForDescribeTransitRouterVpnAttachmentsOutput.


        :param tags: The tags of this TransitRouterAttachmentForDescribeTransitRouterVpnAttachmentsOutput.  # noqa: E501
        :type: list[TagForDescribeTransitRouterVpnAttachmentsOutput]
        """

        self._tags = tags

    @property
    def transit_router_attachment_id(self):
        """Gets the transit_router_attachment_id of this TransitRouterAttachmentForDescribeTransitRouterVpnAttachmentsOutput.  # noqa: E501


        :return: The transit_router_attachment_id of this TransitRouterAttachmentForDescribeTransitRouterVpnAttachmentsOutput.  # noqa: E501
        :rtype: str
        """
        return self._transit_router_attachment_id

    @transit_router_attachment_id.setter
    def transit_router_attachment_id(self, transit_router_attachment_id):
        """Sets the transit_router_attachment_id of this TransitRouterAttachmentForDescribeTransitRouterVpnAttachmentsOutput.


        :param transit_router_attachment_id: The transit_router_attachment_id of this TransitRouterAttachmentForDescribeTransitRouterVpnAttachmentsOutput.  # noqa: E501
        :type: str
        """

        self._transit_router_attachment_id = transit_router_attachment_id

    @property
    def transit_router_attachment_name(self):
        """Gets the transit_router_attachment_name of this TransitRouterAttachmentForDescribeTransitRouterVpnAttachmentsOutput.  # noqa: E501


        :return: The transit_router_attachment_name of this TransitRouterAttachmentForDescribeTransitRouterVpnAttachmentsOutput.  # noqa: E501
        :rtype: str
        """
        return self._transit_router_attachment_name

    @transit_router_attachment_name.setter
    def transit_router_attachment_name(self, transit_router_attachment_name):
        """Sets the transit_router_attachment_name of this TransitRouterAttachmentForDescribeTransitRouterVpnAttachmentsOutput.


        :param transit_router_attachment_name: The transit_router_attachment_name of this TransitRouterAttachmentForDescribeTransitRouterVpnAttachmentsOutput.  # noqa: E501
        :type: str
        """

        self._transit_router_attachment_name = transit_router_attachment_name

    @property
    def transit_router_id(self):
        """Gets the transit_router_id of this TransitRouterAttachmentForDescribeTransitRouterVpnAttachmentsOutput.  # noqa: E501


        :return: The transit_router_id of this TransitRouterAttachmentForDescribeTransitRouterVpnAttachmentsOutput.  # noqa: E501
        :rtype: str
        """
        return self._transit_router_id

    @transit_router_id.setter
    def transit_router_id(self, transit_router_id):
        """Sets the transit_router_id of this TransitRouterAttachmentForDescribeTransitRouterVpnAttachmentsOutput.


        :param transit_router_id: The transit_router_id of this TransitRouterAttachmentForDescribeTransitRouterVpnAttachmentsOutput.  # noqa: E501
        :type: str
        """

        self._transit_router_id = transit_router_id

    @property
    def update_time(self):
        """Gets the update_time of this TransitRouterAttachmentForDescribeTransitRouterVpnAttachmentsOutput.  # noqa: E501


        :return: The update_time of this TransitRouterAttachmentForDescribeTransitRouterVpnAttachmentsOutput.  # noqa: E501
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this TransitRouterAttachmentForDescribeTransitRouterVpnAttachmentsOutput.


        :param update_time: The update_time of this TransitRouterAttachmentForDescribeTransitRouterVpnAttachmentsOutput.  # noqa: E501
        :type: str
        """

        self._update_time = update_time

    @property
    def vpn_connection_id(self):
        """Gets the vpn_connection_id of this TransitRouterAttachmentForDescribeTransitRouterVpnAttachmentsOutput.  # noqa: E501


        :return: The vpn_connection_id of this TransitRouterAttachmentForDescribeTransitRouterVpnAttachmentsOutput.  # noqa: E501
        :rtype: str
        """
        return self._vpn_connection_id

    @vpn_connection_id.setter
    def vpn_connection_id(self, vpn_connection_id):
        """Sets the vpn_connection_id of this TransitRouterAttachmentForDescribeTransitRouterVpnAttachmentsOutput.


        :param vpn_connection_id: The vpn_connection_id of this TransitRouterAttachmentForDescribeTransitRouterVpnAttachmentsOutput.  # noqa: E501
        :type: str
        """

        self._vpn_connection_id = vpn_connection_id

    @property
    def zone_id(self):
        """Gets the zone_id of this TransitRouterAttachmentForDescribeTransitRouterVpnAttachmentsOutput.  # noqa: E501


        :return: The zone_id of this TransitRouterAttachmentForDescribeTransitRouterVpnAttachmentsOutput.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this TransitRouterAttachmentForDescribeTransitRouterVpnAttachmentsOutput.


        :param zone_id: The zone_id of this TransitRouterAttachmentForDescribeTransitRouterVpnAttachmentsOutput.  # noqa: E501
        :type: str
        """

        self._zone_id = zone_id

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
        if issubclass(TransitRouterAttachmentForDescribeTransitRouterVpnAttachmentsOutput, dict):
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
        if not isinstance(other, TransitRouterAttachmentForDescribeTransitRouterVpnAttachmentsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransitRouterAttachmentForDescribeTransitRouterVpnAttachmentsOutput):
            return True

        return self.to_dict() != other.to_dict()
