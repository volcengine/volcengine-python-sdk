# coding: utf-8

"""
    vpc

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class AssociateRouteTableRequest(object):
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
        'gateway_id': 'str',
        'gateway_type': 'str',
        'route_table_id': 'str',
        'subnet_id': 'str'
    }

    attribute_map = {
        'client_token': 'ClientToken',
        'gateway_id': 'GatewayId',
        'gateway_type': 'GatewayType',
        'route_table_id': 'RouteTableId',
        'subnet_id': 'SubnetId'
    }

    def __init__(self, client_token=None, gateway_id=None, gateway_type=None, route_table_id=None, subnet_id=None, _configuration=None):  # noqa: E501
        """AssociateRouteTableRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._client_token = None
        self._gateway_id = None
        self._gateway_type = None
        self._route_table_id = None
        self._subnet_id = None
        self.discriminator = None

        if client_token is not None:
            self.client_token = client_token
        if gateway_id is not None:
            self.gateway_id = gateway_id
        if gateway_type is not None:
            self.gateway_type = gateway_type
        self.route_table_id = route_table_id
        if subnet_id is not None:
            self.subnet_id = subnet_id

    @property
    def client_token(self):
        """Gets the client_token of this AssociateRouteTableRequest.  # noqa: E501


        :return: The client_token of this AssociateRouteTableRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_token

    @client_token.setter
    def client_token(self, client_token):
        """Sets the client_token of this AssociateRouteTableRequest.


        :param client_token: The client_token of this AssociateRouteTableRequest.  # noqa: E501
        :type: str
        """

        self._client_token = client_token

    @property
    def gateway_id(self):
        """Gets the gateway_id of this AssociateRouteTableRequest.  # noqa: E501


        :return: The gateway_id of this AssociateRouteTableRequest.  # noqa: E501
        :rtype: str
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, gateway_id):
        """Sets the gateway_id of this AssociateRouteTableRequest.


        :param gateway_id: The gateway_id of this AssociateRouteTableRequest.  # noqa: E501
        :type: str
        """

        self._gateway_id = gateway_id

    @property
    def gateway_type(self):
        """Gets the gateway_type of this AssociateRouteTableRequest.  # noqa: E501


        :return: The gateway_type of this AssociateRouteTableRequest.  # noqa: E501
        :rtype: str
        """
        return self._gateway_type

    @gateway_type.setter
    def gateway_type(self, gateway_type):
        """Sets the gateway_type of this AssociateRouteTableRequest.


        :param gateway_type: The gateway_type of this AssociateRouteTableRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["Ipv4Gateway", "Ipv6Gateway"]  # noqa: E501
        if (self._configuration.client_side_validation and
                gateway_type not in allowed_values):
            raise ValueError(
                "Invalid value for `gateway_type` ({0}), must be one of {1}"  # noqa: E501
                .format(gateway_type, allowed_values)
            )

        self._gateway_type = gateway_type

    @property
    def route_table_id(self):
        """Gets the route_table_id of this AssociateRouteTableRequest.  # noqa: E501


        :return: The route_table_id of this AssociateRouteTableRequest.  # noqa: E501
        :rtype: str
        """
        return self._route_table_id

    @route_table_id.setter
    def route_table_id(self, route_table_id):
        """Sets the route_table_id of this AssociateRouteTableRequest.


        :param route_table_id: The route_table_id of this AssociateRouteTableRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and route_table_id is None:
            raise ValueError("Invalid value for `route_table_id`, must not be `None`")  # noqa: E501

        self._route_table_id = route_table_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this AssociateRouteTableRequest.  # noqa: E501


        :return: The subnet_id of this AssociateRouteTableRequest.  # noqa: E501
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this AssociateRouteTableRequest.


        :param subnet_id: The subnet_id of this AssociateRouteTableRequest.  # noqa: E501
        :type: str
        """

        self._subnet_id = subnet_id

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
        if issubclass(AssociateRouteTableRequest, dict):
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
        if not isinstance(other, AssociateRouteTableRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AssociateRouteTableRequest):
            return True

        return self.to_dict() != other.to_dict()
