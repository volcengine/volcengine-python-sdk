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


class AccurateForCreateCustomBotConfigInput(object):
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
        'accurate_rules': 'list[AccurateRuleForCreateCustomBotConfigInput]',
        'logic': 'int'
    }

    attribute_map = {
        'accurate_rules': 'AccurateRules',
        'logic': 'Logic'
    }

    def __init__(self, accurate_rules=None, logic=None, _configuration=None):  # noqa: E501
        """AccurateForCreateCustomBotConfigInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._accurate_rules = None
        self._logic = None
        self.discriminator = None

        if accurate_rules is not None:
            self.accurate_rules = accurate_rules
        if logic is not None:
            self.logic = logic

    @property
    def accurate_rules(self):
        """Gets the accurate_rules of this AccurateForCreateCustomBotConfigInput.  # noqa: E501


        :return: The accurate_rules of this AccurateForCreateCustomBotConfigInput.  # noqa: E501
        :rtype: list[AccurateRuleForCreateCustomBotConfigInput]
        """
        return self._accurate_rules

    @accurate_rules.setter
    def accurate_rules(self, accurate_rules):
        """Sets the accurate_rules of this AccurateForCreateCustomBotConfigInput.


        :param accurate_rules: The accurate_rules of this AccurateForCreateCustomBotConfigInput.  # noqa: E501
        :type: list[AccurateRuleForCreateCustomBotConfigInput]
        """

        self._accurate_rules = accurate_rules

    @property
    def logic(self):
        """Gets the logic of this AccurateForCreateCustomBotConfigInput.  # noqa: E501


        :return: The logic of this AccurateForCreateCustomBotConfigInput.  # noqa: E501
        :rtype: int
        """
        return self._logic

    @logic.setter
    def logic(self, logic):
        """Sets the logic of this AccurateForCreateCustomBotConfigInput.


        :param logic: The logic of this AccurateForCreateCustomBotConfigInput.  # noqa: E501
        :type: int
        """

        self._logic = logic

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
        if issubclass(AccurateForCreateCustomBotConfigInput, dict):
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
        if not isinstance(other, AccurateForCreateCustomBotConfigInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccurateForCreateCustomBotConfigInput):
            return True

        return self.to_dict() != other.to_dict()
