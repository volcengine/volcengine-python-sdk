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


class ModifyVpcEndpointAttributesRequest(object):
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
        'endpoint_id': 'str',
        'endpoint_name': 'str',
        'private_dns_enabled': 'bool'
    }

    attribute_map = {
        'description': 'Description',
        'endpoint_id': 'EndpointId',
        'endpoint_name': 'EndpointName',
        'private_dns_enabled': 'PrivateDNSEnabled'
    }

    def __init__(self, description=None, endpoint_id=None, endpoint_name=None, private_dns_enabled=None, _configuration=None):  # noqa: E501
        """ModifyVpcEndpointAttributesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._description = None
        self._endpoint_id = None
        self._endpoint_name = None
        self._private_dns_enabled = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.endpoint_id = endpoint_id
        if endpoint_name is not None:
            self.endpoint_name = endpoint_name
        if private_dns_enabled is not None:
            self.private_dns_enabled = private_dns_enabled

    @property
    def description(self):
        """Gets the description of this ModifyVpcEndpointAttributesRequest.  # noqa: E501


        :return: The description of this ModifyVpcEndpointAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ModifyVpcEndpointAttributesRequest.


        :param description: The description of this ModifyVpcEndpointAttributesRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def endpoint_id(self):
        """Gets the endpoint_id of this ModifyVpcEndpointAttributesRequest.  # noqa: E501


        :return: The endpoint_id of this ModifyVpcEndpointAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        """Sets the endpoint_id of this ModifyVpcEndpointAttributesRequest.


        :param endpoint_id: The endpoint_id of this ModifyVpcEndpointAttributesRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and endpoint_id is None:
            raise ValueError("Invalid value for `endpoint_id`, must not be `None`")  # noqa: E501

        self._endpoint_id = endpoint_id

    @property
    def endpoint_name(self):
        """Gets the endpoint_name of this ModifyVpcEndpointAttributesRequest.  # noqa: E501


        :return: The endpoint_name of this ModifyVpcEndpointAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._endpoint_name

    @endpoint_name.setter
    def endpoint_name(self, endpoint_name):
        """Sets the endpoint_name of this ModifyVpcEndpointAttributesRequest.


        :param endpoint_name: The endpoint_name of this ModifyVpcEndpointAttributesRequest.  # noqa: E501
        :type: str
        """

        self._endpoint_name = endpoint_name

    @property
    def private_dns_enabled(self):
        """Gets the private_dns_enabled of this ModifyVpcEndpointAttributesRequest.  # noqa: E501


        :return: The private_dns_enabled of this ModifyVpcEndpointAttributesRequest.  # noqa: E501
        :rtype: bool
        """
        return self._private_dns_enabled

    @private_dns_enabled.setter
    def private_dns_enabled(self, private_dns_enabled):
        """Sets the private_dns_enabled of this ModifyVpcEndpointAttributesRequest.


        :param private_dns_enabled: The private_dns_enabled of this ModifyVpcEndpointAttributesRequest.  # noqa: E501
        :type: bool
        """

        self._private_dns_enabled = private_dns_enabled

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
        if issubclass(ModifyVpcEndpointAttributesRequest, dict):
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
        if not isinstance(other, ModifyVpcEndpointAttributesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModifyVpcEndpointAttributesRequest):
            return True

        return self.to_dict() != other.to_dict()
