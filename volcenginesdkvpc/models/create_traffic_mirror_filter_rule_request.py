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


class CreateTrafficMirrorFilterRuleRequest(object):
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
        'description': 'str',
        'destination_cidr_block': 'str',
        'destination_port_range': 'str',
        'policy': 'str',
        'priority': 'int',
        'protocol': 'str',
        'source_cidr_block': 'str',
        'source_port_range': 'str',
        'traffic_direction': 'str',
        'traffic_mirror_filter_id': 'str'
    }

    attribute_map = {
        'client_token': 'ClientToken',
        'description': 'Description',
        'destination_cidr_block': 'DestinationCidrBlock',
        'destination_port_range': 'DestinationPortRange',
        'policy': 'Policy',
        'priority': 'Priority',
        'protocol': 'Protocol',
        'source_cidr_block': 'SourceCidrBlock',
        'source_port_range': 'SourcePortRange',
        'traffic_direction': 'TrafficDirection',
        'traffic_mirror_filter_id': 'TrafficMirrorFilterId'
    }

    def __init__(self, client_token=None, description=None, destination_cidr_block=None, destination_port_range=None, policy=None, priority=None, protocol=None, source_cidr_block=None, source_port_range=None, traffic_direction=None, traffic_mirror_filter_id=None, _configuration=None):  # noqa: E501
        """CreateTrafficMirrorFilterRuleRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._client_token = None
        self._description = None
        self._destination_cidr_block = None
        self._destination_port_range = None
        self._policy = None
        self._priority = None
        self._protocol = None
        self._source_cidr_block = None
        self._source_port_range = None
        self._traffic_direction = None
        self._traffic_mirror_filter_id = None
        self.discriminator = None

        if client_token is not None:
            self.client_token = client_token
        if description is not None:
            self.description = description
        self.destination_cidr_block = destination_cidr_block
        if destination_port_range is not None:
            self.destination_port_range = destination_port_range
        self.policy = policy
        if priority is not None:
            self.priority = priority
        self.protocol = protocol
        self.source_cidr_block = source_cidr_block
        if source_port_range is not None:
            self.source_port_range = source_port_range
        self.traffic_direction = traffic_direction
        self.traffic_mirror_filter_id = traffic_mirror_filter_id

    @property
    def client_token(self):
        """Gets the client_token of this CreateTrafficMirrorFilterRuleRequest.  # noqa: E501


        :return: The client_token of this CreateTrafficMirrorFilterRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_token

    @client_token.setter
    def client_token(self, client_token):
        """Sets the client_token of this CreateTrafficMirrorFilterRuleRequest.


        :param client_token: The client_token of this CreateTrafficMirrorFilterRuleRequest.  # noqa: E501
        :type: str
        """

        self._client_token = client_token

    @property
    def description(self):
        """Gets the description of this CreateTrafficMirrorFilterRuleRequest.  # noqa: E501


        :return: The description of this CreateTrafficMirrorFilterRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateTrafficMirrorFilterRuleRequest.


        :param description: The description of this CreateTrafficMirrorFilterRuleRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def destination_cidr_block(self):
        """Gets the destination_cidr_block of this CreateTrafficMirrorFilterRuleRequest.  # noqa: E501


        :return: The destination_cidr_block of this CreateTrafficMirrorFilterRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._destination_cidr_block

    @destination_cidr_block.setter
    def destination_cidr_block(self, destination_cidr_block):
        """Sets the destination_cidr_block of this CreateTrafficMirrorFilterRuleRequest.


        :param destination_cidr_block: The destination_cidr_block of this CreateTrafficMirrorFilterRuleRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and destination_cidr_block is None:
            raise ValueError("Invalid value for `destination_cidr_block`, must not be `None`")  # noqa: E501

        self._destination_cidr_block = destination_cidr_block

    @property
    def destination_port_range(self):
        """Gets the destination_port_range of this CreateTrafficMirrorFilterRuleRequest.  # noqa: E501


        :return: The destination_port_range of this CreateTrafficMirrorFilterRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._destination_port_range

    @destination_port_range.setter
    def destination_port_range(self, destination_port_range):
        """Sets the destination_port_range of this CreateTrafficMirrorFilterRuleRequest.


        :param destination_port_range: The destination_port_range of this CreateTrafficMirrorFilterRuleRequest.  # noqa: E501
        :type: str
        """

        self._destination_port_range = destination_port_range

    @property
    def policy(self):
        """Gets the policy of this CreateTrafficMirrorFilterRuleRequest.  # noqa: E501


        :return: The policy of this CreateTrafficMirrorFilterRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this CreateTrafficMirrorFilterRuleRequest.


        :param policy: The policy of this CreateTrafficMirrorFilterRuleRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and policy is None:
            raise ValueError("Invalid value for `policy`, must not be `None`")  # noqa: E501
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
        """Gets the priority of this CreateTrafficMirrorFilterRuleRequest.  # noqa: E501


        :return: The priority of this CreateTrafficMirrorFilterRuleRequest.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this CreateTrafficMirrorFilterRuleRequest.


        :param priority: The priority of this CreateTrafficMirrorFilterRuleRequest.  # noqa: E501
        :type: int
        """

        self._priority = priority

    @property
    def protocol(self):
        """Gets the protocol of this CreateTrafficMirrorFilterRuleRequest.  # noqa: E501


        :return: The protocol of this CreateTrafficMirrorFilterRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this CreateTrafficMirrorFilterRuleRequest.


        :param protocol: The protocol of this CreateTrafficMirrorFilterRuleRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and protocol is None:
            raise ValueError("Invalid value for `protocol`, must not be `None`")  # noqa: E501
        allowed_values = ["tcp", "udp", "icmp", "all"]  # noqa: E501
        if (self._configuration.client_side_validation and
                protocol not in allowed_values):
            raise ValueError(
                "Invalid value for `protocol` ({0}), must be one of {1}"  # noqa: E501
                .format(protocol, allowed_values)
            )

        self._protocol = protocol

    @property
    def source_cidr_block(self):
        """Gets the source_cidr_block of this CreateTrafficMirrorFilterRuleRequest.  # noqa: E501


        :return: The source_cidr_block of this CreateTrafficMirrorFilterRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._source_cidr_block

    @source_cidr_block.setter
    def source_cidr_block(self, source_cidr_block):
        """Sets the source_cidr_block of this CreateTrafficMirrorFilterRuleRequest.


        :param source_cidr_block: The source_cidr_block of this CreateTrafficMirrorFilterRuleRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and source_cidr_block is None:
            raise ValueError("Invalid value for `source_cidr_block`, must not be `None`")  # noqa: E501

        self._source_cidr_block = source_cidr_block

    @property
    def source_port_range(self):
        """Gets the source_port_range of this CreateTrafficMirrorFilterRuleRequest.  # noqa: E501


        :return: The source_port_range of this CreateTrafficMirrorFilterRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._source_port_range

    @source_port_range.setter
    def source_port_range(self, source_port_range):
        """Sets the source_port_range of this CreateTrafficMirrorFilterRuleRequest.


        :param source_port_range: The source_port_range of this CreateTrafficMirrorFilterRuleRequest.  # noqa: E501
        :type: str
        """

        self._source_port_range = source_port_range

    @property
    def traffic_direction(self):
        """Gets the traffic_direction of this CreateTrafficMirrorFilterRuleRequest.  # noqa: E501


        :return: The traffic_direction of this CreateTrafficMirrorFilterRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._traffic_direction

    @traffic_direction.setter
    def traffic_direction(self, traffic_direction):
        """Sets the traffic_direction of this CreateTrafficMirrorFilterRuleRequest.


        :param traffic_direction: The traffic_direction of this CreateTrafficMirrorFilterRuleRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and traffic_direction is None:
            raise ValueError("Invalid value for `traffic_direction`, must not be `None`")  # noqa: E501
        allowed_values = ["egress", "ingress"]  # noqa: E501
        if (self._configuration.client_side_validation and
                traffic_direction not in allowed_values):
            raise ValueError(
                "Invalid value for `traffic_direction` ({0}), must be one of {1}"  # noqa: E501
                .format(traffic_direction, allowed_values)
            )

        self._traffic_direction = traffic_direction

    @property
    def traffic_mirror_filter_id(self):
        """Gets the traffic_mirror_filter_id of this CreateTrafficMirrorFilterRuleRequest.  # noqa: E501


        :return: The traffic_mirror_filter_id of this CreateTrafficMirrorFilterRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._traffic_mirror_filter_id

    @traffic_mirror_filter_id.setter
    def traffic_mirror_filter_id(self, traffic_mirror_filter_id):
        """Sets the traffic_mirror_filter_id of this CreateTrafficMirrorFilterRuleRequest.


        :param traffic_mirror_filter_id: The traffic_mirror_filter_id of this CreateTrafficMirrorFilterRuleRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and traffic_mirror_filter_id is None:
            raise ValueError("Invalid value for `traffic_mirror_filter_id`, must not be `None`")  # noqa: E501

        self._traffic_mirror_filter_id = traffic_mirror_filter_id

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
        if issubclass(CreateTrafficMirrorFilterRuleRequest, dict):
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
        if not isinstance(other, CreateTrafficMirrorFilterRuleRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateTrafficMirrorFilterRuleRequest):
            return True

        return self.to_dict() != other.to_dict()