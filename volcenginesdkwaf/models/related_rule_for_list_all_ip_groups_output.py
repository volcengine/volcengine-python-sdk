# coding: utf-8

"""
    waf

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class RelatedRuleForListAllIpGroupsOutput(object):
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
        'rule_name': 'str',
        'rule_tag': 'str',
        'rule_type': 'str'
    }

    attribute_map = {
        'rule_name': 'RuleName',
        'rule_tag': 'RuleTag',
        'rule_type': 'RuleType'
    }

    def __init__(self, rule_name=None, rule_tag=None, rule_type=None, _configuration=None):  # noqa: E501
        """RelatedRuleForListAllIpGroupsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._rule_name = None
        self._rule_tag = None
        self._rule_type = None
        self.discriminator = None

        if rule_name is not None:
            self.rule_name = rule_name
        if rule_tag is not None:
            self.rule_tag = rule_tag
        if rule_type is not None:
            self.rule_type = rule_type

    @property
    def rule_name(self):
        """Gets the rule_name of this RelatedRuleForListAllIpGroupsOutput.  # noqa: E501


        :return: The rule_name of this RelatedRuleForListAllIpGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        """Sets the rule_name of this RelatedRuleForListAllIpGroupsOutput.


        :param rule_name: The rule_name of this RelatedRuleForListAllIpGroupsOutput.  # noqa: E501
        :type: str
        """

        self._rule_name = rule_name

    @property
    def rule_tag(self):
        """Gets the rule_tag of this RelatedRuleForListAllIpGroupsOutput.  # noqa: E501


        :return: The rule_tag of this RelatedRuleForListAllIpGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._rule_tag

    @rule_tag.setter
    def rule_tag(self, rule_tag):
        """Sets the rule_tag of this RelatedRuleForListAllIpGroupsOutput.


        :param rule_tag: The rule_tag of this RelatedRuleForListAllIpGroupsOutput.  # noqa: E501
        :type: str
        """

        self._rule_tag = rule_tag

    @property
    def rule_type(self):
        """Gets the rule_type of this RelatedRuleForListAllIpGroupsOutput.  # noqa: E501


        :return: The rule_type of this RelatedRuleForListAllIpGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        """Sets the rule_type of this RelatedRuleForListAllIpGroupsOutput.


        :param rule_type: The rule_type of this RelatedRuleForListAllIpGroupsOutput.  # noqa: E501
        :type: str
        """

        self._rule_type = rule_type

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
        if issubclass(RelatedRuleForListAllIpGroupsOutput, dict):
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
        if not isinstance(other, RelatedRuleForListAllIpGroupsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RelatedRuleForListAllIpGroupsOutput):
            return True

        return self.to_dict() != other.to_dict()
