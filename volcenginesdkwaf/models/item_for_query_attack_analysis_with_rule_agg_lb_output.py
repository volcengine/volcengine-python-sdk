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


class ItemForQueryAttackAnalysisWithRuleAggLbOutput(object):
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
        'count': 'float',
        'key': 'str',
        'rule_tags': 'list[str]'
    }

    attribute_map = {
        'count': 'Count',
        'key': 'Key',
        'rule_tags': 'RuleTags'
    }

    def __init__(self, count=None, key=None, rule_tags=None, _configuration=None):  # noqa: E501
        """ItemForQueryAttackAnalysisWithRuleAggLbOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._count = None
        self._key = None
        self._rule_tags = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if key is not None:
            self.key = key
        if rule_tags is not None:
            self.rule_tags = rule_tags

    @property
    def count(self):
        """Gets the count of this ItemForQueryAttackAnalysisWithRuleAggLbOutput.  # noqa: E501


        :return: The count of this ItemForQueryAttackAnalysisWithRuleAggLbOutput.  # noqa: E501
        :rtype: float
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ItemForQueryAttackAnalysisWithRuleAggLbOutput.


        :param count: The count of this ItemForQueryAttackAnalysisWithRuleAggLbOutput.  # noqa: E501
        :type: float
        """

        self._count = count

    @property
    def key(self):
        """Gets the key of this ItemForQueryAttackAnalysisWithRuleAggLbOutput.  # noqa: E501


        :return: The key of this ItemForQueryAttackAnalysisWithRuleAggLbOutput.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ItemForQueryAttackAnalysisWithRuleAggLbOutput.


        :param key: The key of this ItemForQueryAttackAnalysisWithRuleAggLbOutput.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def rule_tags(self):
        """Gets the rule_tags of this ItemForQueryAttackAnalysisWithRuleAggLbOutput.  # noqa: E501


        :return: The rule_tags of this ItemForQueryAttackAnalysisWithRuleAggLbOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._rule_tags

    @rule_tags.setter
    def rule_tags(self, rule_tags):
        """Sets the rule_tags of this ItemForQueryAttackAnalysisWithRuleAggLbOutput.


        :param rule_tags: The rule_tags of this ItemForQueryAttackAnalysisWithRuleAggLbOutput.  # noqa: E501
        :type: list[str]
        """

        self._rule_tags = rule_tags

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
        if issubclass(ItemForQueryAttackAnalysisWithRuleAggLbOutput, dict):
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
        if not isinstance(other, ItemForQueryAttackAnalysisWithRuleAggLbOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ItemForQueryAttackAnalysisWithRuleAggLbOutput):
            return True

        return self.to_dict() != other.to_dict()
