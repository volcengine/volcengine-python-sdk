# coding: utf-8

"""
    volc_observe

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class LevelConditionForListRulesOutput(object):
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
        'conditions': 'list[ConditionForListRulesOutput]',
        'level': 'str'
    }

    attribute_map = {
        'conditions': 'Conditions',
        'level': 'Level'
    }

    def __init__(self, conditions=None, level=None, _configuration=None):  # noqa: E501
        """LevelConditionForListRulesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._conditions = None
        self._level = None
        self.discriminator = None

        if conditions is not None:
            self.conditions = conditions
        if level is not None:
            self.level = level

    @property
    def conditions(self):
        """Gets the conditions of this LevelConditionForListRulesOutput.  # noqa: E501


        :return: The conditions of this LevelConditionForListRulesOutput.  # noqa: E501
        :rtype: list[ConditionForListRulesOutput]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this LevelConditionForListRulesOutput.


        :param conditions: The conditions of this LevelConditionForListRulesOutput.  # noqa: E501
        :type: list[ConditionForListRulesOutput]
        """

        self._conditions = conditions

    @property
    def level(self):
        """Gets the level of this LevelConditionForListRulesOutput.  # noqa: E501


        :return: The level of this LevelConditionForListRulesOutput.  # noqa: E501
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this LevelConditionForListRulesOutput.


        :param level: The level of this LevelConditionForListRulesOutput.  # noqa: E501
        :type: str
        """

        self._level = level

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
        if issubclass(LevelConditionForListRulesOutput, dict):
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
        if not isinstance(other, LevelConditionForListRulesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LevelConditionForListRulesOutput):
            return True

        return self.to_dict() != other.to_dict()
