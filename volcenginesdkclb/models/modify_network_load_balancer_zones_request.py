# coding: utf-8

"""
    clb

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ModifyNetworkLoadBalancerZonesRequest(object):
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
        'add_zone_mappings': 'list[AddZoneMappingForModifyNetworkLoadBalancerZonesInput]',
        'delete_zone_mappings': 'list[str]',
        'load_balancer_id': 'str'
    }

    attribute_map = {
        'add_zone_mappings': 'AddZoneMappings',
        'delete_zone_mappings': 'DeleteZoneMappings',
        'load_balancer_id': 'LoadBalancerId'
    }

    def __init__(self, add_zone_mappings=None, delete_zone_mappings=None, load_balancer_id=None, _configuration=None):  # noqa: E501
        """ModifyNetworkLoadBalancerZonesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._add_zone_mappings = None
        self._delete_zone_mappings = None
        self._load_balancer_id = None
        self.discriminator = None

        if add_zone_mappings is not None:
            self.add_zone_mappings = add_zone_mappings
        if delete_zone_mappings is not None:
            self.delete_zone_mappings = delete_zone_mappings
        self.load_balancer_id = load_balancer_id

    @property
    def add_zone_mappings(self):
        """Gets the add_zone_mappings of this ModifyNetworkLoadBalancerZonesRequest.  # noqa: E501


        :return: The add_zone_mappings of this ModifyNetworkLoadBalancerZonesRequest.  # noqa: E501
        :rtype: list[AddZoneMappingForModifyNetworkLoadBalancerZonesInput]
        """
        return self._add_zone_mappings

    @add_zone_mappings.setter
    def add_zone_mappings(self, add_zone_mappings):
        """Sets the add_zone_mappings of this ModifyNetworkLoadBalancerZonesRequest.


        :param add_zone_mappings: The add_zone_mappings of this ModifyNetworkLoadBalancerZonesRequest.  # noqa: E501
        :type: list[AddZoneMappingForModifyNetworkLoadBalancerZonesInput]
        """

        self._add_zone_mappings = add_zone_mappings

    @property
    def delete_zone_mappings(self):
        """Gets the delete_zone_mappings of this ModifyNetworkLoadBalancerZonesRequest.  # noqa: E501


        :return: The delete_zone_mappings of this ModifyNetworkLoadBalancerZonesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._delete_zone_mappings

    @delete_zone_mappings.setter
    def delete_zone_mappings(self, delete_zone_mappings):
        """Sets the delete_zone_mappings of this ModifyNetworkLoadBalancerZonesRequest.


        :param delete_zone_mappings: The delete_zone_mappings of this ModifyNetworkLoadBalancerZonesRequest.  # noqa: E501
        :type: list[str]
        """

        self._delete_zone_mappings = delete_zone_mappings

    @property
    def load_balancer_id(self):
        """Gets the load_balancer_id of this ModifyNetworkLoadBalancerZonesRequest.  # noqa: E501


        :return: The load_balancer_id of this ModifyNetworkLoadBalancerZonesRequest.  # noqa: E501
        :rtype: str
        """
        return self._load_balancer_id

    @load_balancer_id.setter
    def load_balancer_id(self, load_balancer_id):
        """Sets the load_balancer_id of this ModifyNetworkLoadBalancerZonesRequest.


        :param load_balancer_id: The load_balancer_id of this ModifyNetworkLoadBalancerZonesRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and load_balancer_id is None:
            raise ValueError("Invalid value for `load_balancer_id`, must not be `None`")  # noqa: E501

        self._load_balancer_id = load_balancer_id

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
        if issubclass(ModifyNetworkLoadBalancerZonesRequest, dict):
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
        if not isinstance(other, ModifyNetworkLoadBalancerZonesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModifyNetworkLoadBalancerZonesRequest):
            return True

        return self.to_dict() != other.to_dict()
