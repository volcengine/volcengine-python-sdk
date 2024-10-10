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


class ModifyPrivateLinkGatewayAttributesRequest(object):
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
        'description': 'str',
        'private_link_gateway_id': 'str',
        'private_link_gateway_name': 'str'
    }

    attribute_map = {
        'description': 'Description',
        'private_link_gateway_id': 'PrivateLinkGatewayId',
        'private_link_gateway_name': 'PrivateLinkGatewayName'
    }

    def __init__(self, description=None, private_link_gateway_id=None, private_link_gateway_name=None, _configuration=None):  # noqa: E501
        """ModifyPrivateLinkGatewayAttributesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._description = None
        self._private_link_gateway_id = None
        self._private_link_gateway_name = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.private_link_gateway_id = private_link_gateway_id
        if private_link_gateway_name is not None:
            self.private_link_gateway_name = private_link_gateway_name

    @property
    def description(self):
        """Gets the description of this ModifyPrivateLinkGatewayAttributesRequest.  # noqa: E501


        :return: The description of this ModifyPrivateLinkGatewayAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ModifyPrivateLinkGatewayAttributesRequest.


        :param description: The description of this ModifyPrivateLinkGatewayAttributesRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def private_link_gateway_id(self):
        """Gets the private_link_gateway_id of this ModifyPrivateLinkGatewayAttributesRequest.  # noqa: E501


        :return: The private_link_gateway_id of this ModifyPrivateLinkGatewayAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._private_link_gateway_id

    @private_link_gateway_id.setter
    def private_link_gateway_id(self, private_link_gateway_id):
        """Sets the private_link_gateway_id of this ModifyPrivateLinkGatewayAttributesRequest.


        :param private_link_gateway_id: The private_link_gateway_id of this ModifyPrivateLinkGatewayAttributesRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and private_link_gateway_id is None:
            raise ValueError("Invalid value for `private_link_gateway_id`, must not be `None`")  # noqa: E501

        self._private_link_gateway_id = private_link_gateway_id

    @property
    def private_link_gateway_name(self):
        """Gets the private_link_gateway_name of this ModifyPrivateLinkGatewayAttributesRequest.  # noqa: E501


        :return: The private_link_gateway_name of this ModifyPrivateLinkGatewayAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._private_link_gateway_name

    @private_link_gateway_name.setter
    def private_link_gateway_name(self, private_link_gateway_name):
        """Sets the private_link_gateway_name of this ModifyPrivateLinkGatewayAttributesRequest.


        :param private_link_gateway_name: The private_link_gateway_name of this ModifyPrivateLinkGatewayAttributesRequest.  # noqa: E501
        :type: str
        """

        self._private_link_gateway_name = private_link_gateway_name

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
        if issubclass(ModifyPrivateLinkGatewayAttributesRequest, dict):
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
        if not isinstance(other, ModifyPrivateLinkGatewayAttributesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModifyPrivateLinkGatewayAttributesRequest):
            return True

        return self.to_dict() != other.to_dict()