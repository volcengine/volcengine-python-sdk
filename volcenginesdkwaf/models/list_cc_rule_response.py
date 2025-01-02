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


class ListCCRuleResponse(object):
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
        'enable_count': 'int',
        'insert_time': 'str',
        'rule_group': 'list[RuleGroupForListCCRuleOutput]',
        'total_count': 'int',
        'url': 'str'
    }

    attribute_map = {
        'enable_count': 'EnableCount',
        'insert_time': 'InsertTime',
        'rule_group': 'RuleGroup',
        'total_count': 'TotalCount',
        'url': 'Url'
    }

    def __init__(self, enable_count=None, insert_time=None, rule_group=None, total_count=None, url=None, _configuration=None):  # noqa: E501
        """ListCCRuleResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._enable_count = None
        self._insert_time = None
        self._rule_group = None
        self._total_count = None
        self._url = None
        self.discriminator = None

        if enable_count is not None:
            self.enable_count = enable_count
        if insert_time is not None:
            self.insert_time = insert_time
        if rule_group is not None:
            self.rule_group = rule_group
        if total_count is not None:
            self.total_count = total_count
        if url is not None:
            self.url = url

    @property
    def enable_count(self):
        """Gets the enable_count of this ListCCRuleResponse.  # noqa: E501


        :return: The enable_count of this ListCCRuleResponse.  # noqa: E501
        :rtype: int
        """
        return self._enable_count

    @enable_count.setter
    def enable_count(self, enable_count):
        """Sets the enable_count of this ListCCRuleResponse.


        :param enable_count: The enable_count of this ListCCRuleResponse.  # noqa: E501
        :type: int
        """

        self._enable_count = enable_count

    @property
    def insert_time(self):
        """Gets the insert_time of this ListCCRuleResponse.  # noqa: E501


        :return: The insert_time of this ListCCRuleResponse.  # noqa: E501
        :rtype: str
        """
        return self._insert_time

    @insert_time.setter
    def insert_time(self, insert_time):
        """Sets the insert_time of this ListCCRuleResponse.


        :param insert_time: The insert_time of this ListCCRuleResponse.  # noqa: E501
        :type: str
        """

        self._insert_time = insert_time

    @property
    def rule_group(self):
        """Gets the rule_group of this ListCCRuleResponse.  # noqa: E501


        :return: The rule_group of this ListCCRuleResponse.  # noqa: E501
        :rtype: list[RuleGroupForListCCRuleOutput]
        """
        return self._rule_group

    @rule_group.setter
    def rule_group(self, rule_group):
        """Sets the rule_group of this ListCCRuleResponse.


        :param rule_group: The rule_group of this ListCCRuleResponse.  # noqa: E501
        :type: list[RuleGroupForListCCRuleOutput]
        """

        self._rule_group = rule_group

    @property
    def total_count(self):
        """Gets the total_count of this ListCCRuleResponse.  # noqa: E501


        :return: The total_count of this ListCCRuleResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListCCRuleResponse.


        :param total_count: The total_count of this ListCCRuleResponse.  # noqa: E501
        :type: int
        """

        self._total_count = total_count

    @property
    def url(self):
        """Gets the url of this ListCCRuleResponse.  # noqa: E501


        :return: The url of this ListCCRuleResponse.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ListCCRuleResponse.


        :param url: The url of this ListCCRuleResponse.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(ListCCRuleResponse, dict):
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
        if not isinstance(other, ListCCRuleResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListCCRuleResponse):
            return True

        return self.to_dict() != other.to_dict()