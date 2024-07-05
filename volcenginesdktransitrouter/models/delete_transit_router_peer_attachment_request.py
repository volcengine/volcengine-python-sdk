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


class DeleteTransitRouterPeerAttachmentRequest(object):
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
        'force': 'bool',
        'transit_router_attachment_id': 'str'
    }

    attribute_map = {
        'force': 'Force',
        'transit_router_attachment_id': 'TransitRouterAttachmentId'
    }

    def __init__(self, force=None, transit_router_attachment_id=None, _configuration=None):  # noqa: E501
        """DeleteTransitRouterPeerAttachmentRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._force = None
        self._transit_router_attachment_id = None
        self.discriminator = None

        if force is not None:
            self.force = force
        self.transit_router_attachment_id = transit_router_attachment_id

    @property
    def force(self):
        """Gets the force of this DeleteTransitRouterPeerAttachmentRequest.  # noqa: E501


        :return: The force of this DeleteTransitRouterPeerAttachmentRequest.  # noqa: E501
        :rtype: bool
        """
        return self._force

    @force.setter
    def force(self, force):
        """Sets the force of this DeleteTransitRouterPeerAttachmentRequest.


        :param force: The force of this DeleteTransitRouterPeerAttachmentRequest.  # noqa: E501
        :type: bool
        """

        self._force = force

    @property
    def transit_router_attachment_id(self):
        """Gets the transit_router_attachment_id of this DeleteTransitRouterPeerAttachmentRequest.  # noqa: E501


        :return: The transit_router_attachment_id of this DeleteTransitRouterPeerAttachmentRequest.  # noqa: E501
        :rtype: str
        """
        return self._transit_router_attachment_id

    @transit_router_attachment_id.setter
    def transit_router_attachment_id(self, transit_router_attachment_id):
        """Sets the transit_router_attachment_id of this DeleteTransitRouterPeerAttachmentRequest.


        :param transit_router_attachment_id: The transit_router_attachment_id of this DeleteTransitRouterPeerAttachmentRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and transit_router_attachment_id is None:
            raise ValueError("Invalid value for `transit_router_attachment_id`, must not be `None`")  # noqa: E501

        self._transit_router_attachment_id = transit_router_attachment_id

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
        if issubclass(DeleteTransitRouterPeerAttachmentRequest, dict):
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
        if not isinstance(other, DeleteTransitRouterPeerAttachmentRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeleteTransitRouterPeerAttachmentRequest):
            return True

        return self.to_dict() != other.to_dict()
