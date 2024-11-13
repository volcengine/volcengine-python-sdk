# coding: utf-8

"""
    fwcenter

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class UpdateNatFirewallControlPolicySwitchRequest(object):
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
        'direction': 'str',
        'nat_firewall_id': 'str',
        'rule_ids': 'list[str]',
        'status': 'bool'
    }

    attribute_map = {
        'direction': 'Direction',
        'nat_firewall_id': 'NatFirewallId',
        'rule_ids': 'RuleIds',
        'status': 'Status'
    }

    def __init__(self, direction=None, nat_firewall_id=None, rule_ids=None, status=None, _configuration=None):  # noqa: E501
        """UpdateNatFirewallControlPolicySwitchRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._direction = None
        self._nat_firewall_id = None
        self._rule_ids = None
        self._status = None
        self.discriminator = None

        self.direction = direction
        self.nat_firewall_id = nat_firewall_id
        if rule_ids is not None:
            self.rule_ids = rule_ids
        if status is not None:
            self.status = status

    @property
    def direction(self):
        """Gets the direction of this UpdateNatFirewallControlPolicySwitchRequest.  # noqa: E501


        :return: The direction of this UpdateNatFirewallControlPolicySwitchRequest.  # noqa: E501
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this UpdateNatFirewallControlPolicySwitchRequest.


        :param direction: The direction of this UpdateNatFirewallControlPolicySwitchRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and direction is None:
            raise ValueError("Invalid value for `direction`, must not be `None`")  # noqa: E501
        allowed_values = ["in", "out"]  # noqa: E501
        if (self._configuration.client_side_validation and
                direction not in allowed_values):
            raise ValueError(
                "Invalid value for `direction` ({0}), must be one of {1}"  # noqa: E501
                .format(direction, allowed_values)
            )

        self._direction = direction

    @property
    def nat_firewall_id(self):
        """Gets the nat_firewall_id of this UpdateNatFirewallControlPolicySwitchRequest.  # noqa: E501


        :return: The nat_firewall_id of this UpdateNatFirewallControlPolicySwitchRequest.  # noqa: E501
        :rtype: str
        """
        return self._nat_firewall_id

    @nat_firewall_id.setter
    def nat_firewall_id(self, nat_firewall_id):
        """Sets the nat_firewall_id of this UpdateNatFirewallControlPolicySwitchRequest.


        :param nat_firewall_id: The nat_firewall_id of this UpdateNatFirewallControlPolicySwitchRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and nat_firewall_id is None:
            raise ValueError("Invalid value for `nat_firewall_id`, must not be `None`")  # noqa: E501

        self._nat_firewall_id = nat_firewall_id

    @property
    def rule_ids(self):
        """Gets the rule_ids of this UpdateNatFirewallControlPolicySwitchRequest.  # noqa: E501


        :return: The rule_ids of this UpdateNatFirewallControlPolicySwitchRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._rule_ids

    @rule_ids.setter
    def rule_ids(self, rule_ids):
        """Sets the rule_ids of this UpdateNatFirewallControlPolicySwitchRequest.


        :param rule_ids: The rule_ids of this UpdateNatFirewallControlPolicySwitchRequest.  # noqa: E501
        :type: list[str]
        """

        self._rule_ids = rule_ids

    @property
    def status(self):
        """Gets the status of this UpdateNatFirewallControlPolicySwitchRequest.  # noqa: E501


        :return: The status of this UpdateNatFirewallControlPolicySwitchRequest.  # noqa: E501
        :rtype: bool
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateNatFirewallControlPolicySwitchRequest.


        :param status: The status of this UpdateNatFirewallControlPolicySwitchRequest.  # noqa: E501
        :type: bool
        """

        self._status = status

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
        if issubclass(UpdateNatFirewallControlPolicySwitchRequest, dict):
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
        if not isinstance(other, UpdateNatFirewallControlPolicySwitchRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateNatFirewallControlPolicySwitchRequest):
            return True

        return self.to_dict() != other.to_dict()
