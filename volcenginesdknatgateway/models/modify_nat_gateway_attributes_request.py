# coding: utf-8

"""
    natgateway

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ModifyNatGatewayAttributesRequest(object):
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
        'nat_gateway_id': 'str',
        'nat_gateway_name': 'str',
        'spec': 'str'
    }

    attribute_map = {
        'description': 'Description',
        'nat_gateway_id': 'NatGatewayId',
        'nat_gateway_name': 'NatGatewayName',
        'spec': 'Spec'
    }

    def __init__(self, description=None, nat_gateway_id=None, nat_gateway_name=None, spec=None, _configuration=None):  # noqa: E501
        """ModifyNatGatewayAttributesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._description = None
        self._nat_gateway_id = None
        self._nat_gateway_name = None
        self._spec = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.nat_gateway_id = nat_gateway_id
        if nat_gateway_name is not None:
            self.nat_gateway_name = nat_gateway_name
        if spec is not None:
            self.spec = spec

    @property
    def description(self):
        """Gets the description of this ModifyNatGatewayAttributesRequest.  # noqa: E501


        :return: The description of this ModifyNatGatewayAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ModifyNatGatewayAttributesRequest.


        :param description: The description of this ModifyNatGatewayAttributesRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                description is not None and len(description) > 255):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                description is not None and len(description) < 1):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `1`")  # noqa: E501

        self._description = description

    @property
    def nat_gateway_id(self):
        """Gets the nat_gateway_id of this ModifyNatGatewayAttributesRequest.  # noqa: E501


        :return: The nat_gateway_id of this ModifyNatGatewayAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._nat_gateway_id

    @nat_gateway_id.setter
    def nat_gateway_id(self, nat_gateway_id):
        """Sets the nat_gateway_id of this ModifyNatGatewayAttributesRequest.


        :param nat_gateway_id: The nat_gateway_id of this ModifyNatGatewayAttributesRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and nat_gateway_id is None:
            raise ValueError("Invalid value for `nat_gateway_id`, must not be `None`")  # noqa: E501

        self._nat_gateway_id = nat_gateway_id

    @property
    def nat_gateway_name(self):
        """Gets the nat_gateway_name of this ModifyNatGatewayAttributesRequest.  # noqa: E501


        :return: The nat_gateway_name of this ModifyNatGatewayAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._nat_gateway_name

    @nat_gateway_name.setter
    def nat_gateway_name(self, nat_gateway_name):
        """Sets the nat_gateway_name of this ModifyNatGatewayAttributesRequest.


        :param nat_gateway_name: The nat_gateway_name of this ModifyNatGatewayAttributesRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                nat_gateway_name is not None and len(nat_gateway_name) > 128):
            raise ValueError("Invalid value for `nat_gateway_name`, length must be less than or equal to `128`")  # noqa: E501
        if (self._configuration.client_side_validation and
                nat_gateway_name is not None and len(nat_gateway_name) < 1):
            raise ValueError("Invalid value for `nat_gateway_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._nat_gateway_name = nat_gateway_name

    @property
    def spec(self):
        """Gets the spec of this ModifyNatGatewayAttributesRequest.  # noqa: E501


        :return: The spec of this ModifyNatGatewayAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this ModifyNatGatewayAttributesRequest.


        :param spec: The spec of this ModifyNatGatewayAttributesRequest.  # noqa: E501
        :type: str
        """

        self._spec = spec

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
        if issubclass(ModifyNatGatewayAttributesRequest, dict):
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
        if not isinstance(other, ModifyNatGatewayAttributesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModifyNatGatewayAttributesRequest):
            return True

        return self.to_dict() != other.to_dict()
