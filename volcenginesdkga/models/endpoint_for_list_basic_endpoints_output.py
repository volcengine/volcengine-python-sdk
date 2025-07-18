# coding: utf-8

"""
    ga

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class EndpointForListBasicEndpointsOutput(object):
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
        'accelerate_ips': 'list[AccelerateIPForListBasicEndpointsOutput]',
        'accelerator_id': 'str',
        'edge_node': 'str',
        'edge_node_alias': 'str',
        'endpoint_address': 'str',
        'endpoint_group_id': 'str',
        'endpoint_id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'accelerate_ips': 'AccelerateIPs',
        'accelerator_id': 'AcceleratorId',
        'edge_node': 'EdgeNode',
        'edge_node_alias': 'EdgeNodeAlias',
        'endpoint_address': 'EndpointAddress',
        'endpoint_group_id': 'EndpointGroupId',
        'endpoint_id': 'EndpointId',
        'type': 'Type'
    }

    def __init__(self, accelerate_ips=None, accelerator_id=None, edge_node=None, edge_node_alias=None, endpoint_address=None, endpoint_group_id=None, endpoint_id=None, type=None, _configuration=None):  # noqa: E501
        """EndpointForListBasicEndpointsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._accelerate_ips = None
        self._accelerator_id = None
        self._edge_node = None
        self._edge_node_alias = None
        self._endpoint_address = None
        self._endpoint_group_id = None
        self._endpoint_id = None
        self._type = None
        self.discriminator = None

        if accelerate_ips is not None:
            self.accelerate_ips = accelerate_ips
        if accelerator_id is not None:
            self.accelerator_id = accelerator_id
        if edge_node is not None:
            self.edge_node = edge_node
        if edge_node_alias is not None:
            self.edge_node_alias = edge_node_alias
        if endpoint_address is not None:
            self.endpoint_address = endpoint_address
        if endpoint_group_id is not None:
            self.endpoint_group_id = endpoint_group_id
        if endpoint_id is not None:
            self.endpoint_id = endpoint_id
        if type is not None:
            self.type = type

    @property
    def accelerate_ips(self):
        """Gets the accelerate_ips of this EndpointForListBasicEndpointsOutput.  # noqa: E501


        :return: The accelerate_ips of this EndpointForListBasicEndpointsOutput.  # noqa: E501
        :rtype: list[AccelerateIPForListBasicEndpointsOutput]
        """
        return self._accelerate_ips

    @accelerate_ips.setter
    def accelerate_ips(self, accelerate_ips):
        """Sets the accelerate_ips of this EndpointForListBasicEndpointsOutput.


        :param accelerate_ips: The accelerate_ips of this EndpointForListBasicEndpointsOutput.  # noqa: E501
        :type: list[AccelerateIPForListBasicEndpointsOutput]
        """

        self._accelerate_ips = accelerate_ips

    @property
    def accelerator_id(self):
        """Gets the accelerator_id of this EndpointForListBasicEndpointsOutput.  # noqa: E501


        :return: The accelerator_id of this EndpointForListBasicEndpointsOutput.  # noqa: E501
        :rtype: str
        """
        return self._accelerator_id

    @accelerator_id.setter
    def accelerator_id(self, accelerator_id):
        """Sets the accelerator_id of this EndpointForListBasicEndpointsOutput.


        :param accelerator_id: The accelerator_id of this EndpointForListBasicEndpointsOutput.  # noqa: E501
        :type: str
        """

        self._accelerator_id = accelerator_id

    @property
    def edge_node(self):
        """Gets the edge_node of this EndpointForListBasicEndpointsOutput.  # noqa: E501


        :return: The edge_node of this EndpointForListBasicEndpointsOutput.  # noqa: E501
        :rtype: str
        """
        return self._edge_node

    @edge_node.setter
    def edge_node(self, edge_node):
        """Sets the edge_node of this EndpointForListBasicEndpointsOutput.


        :param edge_node: The edge_node of this EndpointForListBasicEndpointsOutput.  # noqa: E501
        :type: str
        """

        self._edge_node = edge_node

    @property
    def edge_node_alias(self):
        """Gets the edge_node_alias of this EndpointForListBasicEndpointsOutput.  # noqa: E501


        :return: The edge_node_alias of this EndpointForListBasicEndpointsOutput.  # noqa: E501
        :rtype: str
        """
        return self._edge_node_alias

    @edge_node_alias.setter
    def edge_node_alias(self, edge_node_alias):
        """Sets the edge_node_alias of this EndpointForListBasicEndpointsOutput.


        :param edge_node_alias: The edge_node_alias of this EndpointForListBasicEndpointsOutput.  # noqa: E501
        :type: str
        """

        self._edge_node_alias = edge_node_alias

    @property
    def endpoint_address(self):
        """Gets the endpoint_address of this EndpointForListBasicEndpointsOutput.  # noqa: E501


        :return: The endpoint_address of this EndpointForListBasicEndpointsOutput.  # noqa: E501
        :rtype: str
        """
        return self._endpoint_address

    @endpoint_address.setter
    def endpoint_address(self, endpoint_address):
        """Sets the endpoint_address of this EndpointForListBasicEndpointsOutput.


        :param endpoint_address: The endpoint_address of this EndpointForListBasicEndpointsOutput.  # noqa: E501
        :type: str
        """

        self._endpoint_address = endpoint_address

    @property
    def endpoint_group_id(self):
        """Gets the endpoint_group_id of this EndpointForListBasicEndpointsOutput.  # noqa: E501


        :return: The endpoint_group_id of this EndpointForListBasicEndpointsOutput.  # noqa: E501
        :rtype: str
        """
        return self._endpoint_group_id

    @endpoint_group_id.setter
    def endpoint_group_id(self, endpoint_group_id):
        """Sets the endpoint_group_id of this EndpointForListBasicEndpointsOutput.


        :param endpoint_group_id: The endpoint_group_id of this EndpointForListBasicEndpointsOutput.  # noqa: E501
        :type: str
        """

        self._endpoint_group_id = endpoint_group_id

    @property
    def endpoint_id(self):
        """Gets the endpoint_id of this EndpointForListBasicEndpointsOutput.  # noqa: E501


        :return: The endpoint_id of this EndpointForListBasicEndpointsOutput.  # noqa: E501
        :rtype: str
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        """Sets the endpoint_id of this EndpointForListBasicEndpointsOutput.


        :param endpoint_id: The endpoint_id of this EndpointForListBasicEndpointsOutput.  # noqa: E501
        :type: str
        """

        self._endpoint_id = endpoint_id

    @property
    def type(self):
        """Gets the type of this EndpointForListBasicEndpointsOutput.  # noqa: E501


        :return: The type of this EndpointForListBasicEndpointsOutput.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EndpointForListBasicEndpointsOutput.


        :param type: The type of this EndpointForListBasicEndpointsOutput.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(EndpointForListBasicEndpointsOutput, dict):
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
        if not isinstance(other, EndpointForListBasicEndpointsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EndpointForListBasicEndpointsOutput):
            return True

        return self.to_dict() != other.to_dict()
