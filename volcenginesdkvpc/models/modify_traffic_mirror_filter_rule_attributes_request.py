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


class ModifyTrafficMirrorFilterRuleAttributesRequest(object):
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
        'destination_cidr_block': 'str',
        'destination_port_range': 'str',
        'policy': 'str',
        'priority': 'int',
        'protocol': 'str',
        'source_cidr_block': 'str',
        'source_port_range': 'str',
        'traffic_direction': 'str',
        'traffic_mirror_filter_rule_id': 'str'
    }

    attribute_map = {
        'description': 'Description',
        'destination_cidr_block': 'DestinationCidrBlock',
        'destination_port_range': 'DestinationPortRange',
        'policy': 'Policy',
        'priority': 'Priority',
        'protocol': 'Protocol',
        'source_cidr_block': 'SourceCidrBlock',
        'source_port_range': 'SourcePortRange',
        'traffic_direction': 'TrafficDirection',
        'traffic_mirror_filter_rule_id': 'TrafficMirrorFilterRuleId'
    }

    def __init__(self, description=None, destination_cidr_block=None, destination_port_range=None, policy=None, priority=None, protocol=None, source_cidr_block=None, source_port_range=None, traffic_direction=None, traffic_mirror_filter_rule_id=None, _configuration=None):  # noqa: E501
        """ModifyTrafficMirrorFilterRuleAttributesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._description = None
        self._destination_cidr_block = None
        self._destination_port_range = None
        self._policy = None
        self._priority = None
        self._protocol = None
        self._source_cidr_block = None
        self._source_port_range = None
        self._traffic_direction = None
        self._traffic_mirror_filter_rule_id = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if destination_cidr_block is not None:
            self.destination_cidr_block = destination_cidr_block
        if destination_port_range is not None:
            self.destination_port_range = destination_port_range
        if policy is not None:
            self.policy = policy
        if priority is not None:
            self.priority = priority
        if protocol is not None:
            self.protocol = protocol
        if source_cidr_block is not None:
            self.source_cidr_block = source_cidr_block
        if source_port_range is not None:
            self.source_port_range = source_port_range
        if traffic_direction is not None:
            self.traffic_direction = traffic_direction
        self.traffic_mirror_filter_rule_id = traffic_mirror_filter_rule_id

    @property
    def description(self):
        """Gets the description of this ModifyTrafficMirrorFilterRuleAttributesRequest.  # noqa: E501


        :return: The description of this ModifyTrafficMirrorFilterRuleAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ModifyTrafficMirrorFilterRuleAttributesRequest.


        :param description: The description of this ModifyTrafficMirrorFilterRuleAttributesRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def destination_cidr_block(self):
        """Gets the destination_cidr_block of this ModifyTrafficMirrorFilterRuleAttributesRequest.  # noqa: E501


        :return: The destination_cidr_block of this ModifyTrafficMirrorFilterRuleAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._destination_cidr_block

    @destination_cidr_block.setter
    def destination_cidr_block(self, destination_cidr_block):
        """Sets the destination_cidr_block of this ModifyTrafficMirrorFilterRuleAttributesRequest.


        :param destination_cidr_block: The destination_cidr_block of this ModifyTrafficMirrorFilterRuleAttributesRequest.  # noqa: E501
        :type: str
        """

        self._destination_cidr_block = destination_cidr_block

    @property
    def destination_port_range(self):
        """Gets the destination_port_range of this ModifyTrafficMirrorFilterRuleAttributesRequest.  # noqa: E501


        :return: The destination_port_range of this ModifyTrafficMirrorFilterRuleAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._destination_port_range

    @destination_port_range.setter
    def destination_port_range(self, destination_port_range):
        """Sets the destination_port_range of this ModifyTrafficMirrorFilterRuleAttributesRequest.


        :param destination_port_range: The destination_port_range of this ModifyTrafficMirrorFilterRuleAttributesRequest.  # noqa: E501
        :type: str
        """

        self._destination_port_range = destination_port_range

    @property
    def policy(self):
        """Gets the policy of this ModifyTrafficMirrorFilterRuleAttributesRequest.  # noqa: E501


        :return: The policy of this ModifyTrafficMirrorFilterRuleAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this ModifyTrafficMirrorFilterRuleAttributesRequest.


        :param policy: The policy of this ModifyTrafficMirrorFilterRuleAttributesRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["accept", "reject"]  # noqa: E501
        if (self._configuration.client_side_validation and
                policy not in allowed_values):
            raise ValueError(
                "Invalid value for `policy` ({0}), must be one of {1}"  # noqa: E501
                .format(policy, allowed_values)
            )

        self._policy = policy

    @property
    def priority(self):
        """Gets the priority of this ModifyTrafficMirrorFilterRuleAttributesRequest.  # noqa: E501


        :return: The priority of this ModifyTrafficMirrorFilterRuleAttributesRequest.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this ModifyTrafficMirrorFilterRuleAttributesRequest.


        :param priority: The priority of this ModifyTrafficMirrorFilterRuleAttributesRequest.  # noqa: E501
        :type: int
        """

        self._priority = priority

    @property
    def protocol(self):
        """Gets the protocol of this ModifyTrafficMirrorFilterRuleAttributesRequest.  # noqa: E501


        :return: The protocol of this ModifyTrafficMirrorFilterRuleAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ModifyTrafficMirrorFilterRuleAttributesRequest.


        :param protocol: The protocol of this ModifyTrafficMirrorFilterRuleAttributesRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["icmp", "icmpv6", "tcp", "udp", "all"]  # noqa: E501
        if (self._configuration.client_side_validation and
                protocol not in allowed_values):
            raise ValueError(
                "Invalid value for `protocol` ({0}), must be one of {1}"  # noqa: E501
                .format(protocol, allowed_values)
            )

        self._protocol = protocol

    @property
    def source_cidr_block(self):
        """Gets the source_cidr_block of this ModifyTrafficMirrorFilterRuleAttributesRequest.  # noqa: E501


        :return: The source_cidr_block of this ModifyTrafficMirrorFilterRuleAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._source_cidr_block

    @source_cidr_block.setter
    def source_cidr_block(self, source_cidr_block):
        """Sets the source_cidr_block of this ModifyTrafficMirrorFilterRuleAttributesRequest.


        :param source_cidr_block: The source_cidr_block of this ModifyTrafficMirrorFilterRuleAttributesRequest.  # noqa: E501
        :type: str
        """

        self._source_cidr_block = source_cidr_block

    @property
    def source_port_range(self):
        """Gets the source_port_range of this ModifyTrafficMirrorFilterRuleAttributesRequest.  # noqa: E501


        :return: The source_port_range of this ModifyTrafficMirrorFilterRuleAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._source_port_range

    @source_port_range.setter
    def source_port_range(self, source_port_range):
        """Sets the source_port_range of this ModifyTrafficMirrorFilterRuleAttributesRequest.


        :param source_port_range: The source_port_range of this ModifyTrafficMirrorFilterRuleAttributesRequest.  # noqa: E501
        :type: str
        """

        self._source_port_range = source_port_range

    @property
    def traffic_direction(self):
        """Gets the traffic_direction of this ModifyTrafficMirrorFilterRuleAttributesRequest.  # noqa: E501


        :return: The traffic_direction of this ModifyTrafficMirrorFilterRuleAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._traffic_direction

    @traffic_direction.setter
    def traffic_direction(self, traffic_direction):
        """Sets the traffic_direction of this ModifyTrafficMirrorFilterRuleAttributesRequest.


        :param traffic_direction: The traffic_direction of this ModifyTrafficMirrorFilterRuleAttributesRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["egress", "ingress"]  # noqa: E501
        if (self._configuration.client_side_validation and
                traffic_direction not in allowed_values):
            raise ValueError(
                "Invalid value for `traffic_direction` ({0}), must be one of {1}"  # noqa: E501
                .format(traffic_direction, allowed_values)
            )

        self._traffic_direction = traffic_direction

    @property
    def traffic_mirror_filter_rule_id(self):
        """Gets the traffic_mirror_filter_rule_id of this ModifyTrafficMirrorFilterRuleAttributesRequest.  # noqa: E501


        :return: The traffic_mirror_filter_rule_id of this ModifyTrafficMirrorFilterRuleAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._traffic_mirror_filter_rule_id

    @traffic_mirror_filter_rule_id.setter
    def traffic_mirror_filter_rule_id(self, traffic_mirror_filter_rule_id):
        """Sets the traffic_mirror_filter_rule_id of this ModifyTrafficMirrorFilterRuleAttributesRequest.


        :param traffic_mirror_filter_rule_id: The traffic_mirror_filter_rule_id of this ModifyTrafficMirrorFilterRuleAttributesRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and traffic_mirror_filter_rule_id is None:
            raise ValueError("Invalid value for `traffic_mirror_filter_rule_id`, must not be `None`")  # noqa: E501

        self._traffic_mirror_filter_rule_id = traffic_mirror_filter_rule_id

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
        if issubclass(ModifyTrafficMirrorFilterRuleAttributesRequest, dict):
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
        if not isinstance(other, ModifyTrafficMirrorFilterRuleAttributesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModifyTrafficMirrorFilterRuleAttributesRequest):
            return True

        return self.to_dict() != other.to_dict()
