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


class TemplateRuleForCreateAlertTemplateInput(object):
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
        'condition_operator': 'str',
        'evaluation_count': 'int',
        'level_conditions': 'list[LevelConditionForCreateAlertTemplateInput]',
        'multiple_conditions': 'bool',
        'name': 'str',
        'namespace': 'str',
        'sub_namespace': 'str'
    }

    attribute_map = {
        'condition_operator': 'ConditionOperator',
        'evaluation_count': 'EvaluationCount',
        'level_conditions': 'LevelConditions',
        'multiple_conditions': 'MultipleConditions',
        'name': 'Name',
        'namespace': 'Namespace',
        'sub_namespace': 'SubNamespace'
    }

    def __init__(self, condition_operator=None, evaluation_count=None, level_conditions=None, multiple_conditions=None, name=None, namespace=None, sub_namespace=None, _configuration=None):  # noqa: E501
        """TemplateRuleForCreateAlertTemplateInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._condition_operator = None
        self._evaluation_count = None
        self._level_conditions = None
        self._multiple_conditions = None
        self._name = None
        self._namespace = None
        self._sub_namespace = None
        self.discriminator = None

        if condition_operator is not None:
            self.condition_operator = condition_operator
        if evaluation_count is not None:
            self.evaluation_count = evaluation_count
        if level_conditions is not None:
            self.level_conditions = level_conditions
        if multiple_conditions is not None:
            self.multiple_conditions = multiple_conditions
        if name is not None:
            self.name = name
        if namespace is not None:
            self.namespace = namespace
        if sub_namespace is not None:
            self.sub_namespace = sub_namespace

    @property
    def condition_operator(self):
        """Gets the condition_operator of this TemplateRuleForCreateAlertTemplateInput.  # noqa: E501


        :return: The condition_operator of this TemplateRuleForCreateAlertTemplateInput.  # noqa: E501
        :rtype: str
        """
        return self._condition_operator

    @condition_operator.setter
    def condition_operator(self, condition_operator):
        """Sets the condition_operator of this TemplateRuleForCreateAlertTemplateInput.


        :param condition_operator: The condition_operator of this TemplateRuleForCreateAlertTemplateInput.  # noqa: E501
        :type: str
        """

        self._condition_operator = condition_operator

    @property
    def evaluation_count(self):
        """Gets the evaluation_count of this TemplateRuleForCreateAlertTemplateInput.  # noqa: E501


        :return: The evaluation_count of this TemplateRuleForCreateAlertTemplateInput.  # noqa: E501
        :rtype: int
        """
        return self._evaluation_count

    @evaluation_count.setter
    def evaluation_count(self, evaluation_count):
        """Sets the evaluation_count of this TemplateRuleForCreateAlertTemplateInput.


        :param evaluation_count: The evaluation_count of this TemplateRuleForCreateAlertTemplateInput.  # noqa: E501
        :type: int
        """

        self._evaluation_count = evaluation_count

    @property
    def level_conditions(self):
        """Gets the level_conditions of this TemplateRuleForCreateAlertTemplateInput.  # noqa: E501


        :return: The level_conditions of this TemplateRuleForCreateAlertTemplateInput.  # noqa: E501
        :rtype: list[LevelConditionForCreateAlertTemplateInput]
        """
        return self._level_conditions

    @level_conditions.setter
    def level_conditions(self, level_conditions):
        """Sets the level_conditions of this TemplateRuleForCreateAlertTemplateInput.


        :param level_conditions: The level_conditions of this TemplateRuleForCreateAlertTemplateInput.  # noqa: E501
        :type: list[LevelConditionForCreateAlertTemplateInput]
        """

        self._level_conditions = level_conditions

    @property
    def multiple_conditions(self):
        """Gets the multiple_conditions of this TemplateRuleForCreateAlertTemplateInput.  # noqa: E501


        :return: The multiple_conditions of this TemplateRuleForCreateAlertTemplateInput.  # noqa: E501
        :rtype: bool
        """
        return self._multiple_conditions

    @multiple_conditions.setter
    def multiple_conditions(self, multiple_conditions):
        """Sets the multiple_conditions of this TemplateRuleForCreateAlertTemplateInput.


        :param multiple_conditions: The multiple_conditions of this TemplateRuleForCreateAlertTemplateInput.  # noqa: E501
        :type: bool
        """

        self._multiple_conditions = multiple_conditions

    @property
    def name(self):
        """Gets the name of this TemplateRuleForCreateAlertTemplateInput.  # noqa: E501


        :return: The name of this TemplateRuleForCreateAlertTemplateInput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TemplateRuleForCreateAlertTemplateInput.


        :param name: The name of this TemplateRuleForCreateAlertTemplateInput.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def namespace(self):
        """Gets the namespace of this TemplateRuleForCreateAlertTemplateInput.  # noqa: E501


        :return: The namespace of this TemplateRuleForCreateAlertTemplateInput.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this TemplateRuleForCreateAlertTemplateInput.


        :param namespace: The namespace of this TemplateRuleForCreateAlertTemplateInput.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def sub_namespace(self):
        """Gets the sub_namespace of this TemplateRuleForCreateAlertTemplateInput.  # noqa: E501


        :return: The sub_namespace of this TemplateRuleForCreateAlertTemplateInput.  # noqa: E501
        :rtype: str
        """
        return self._sub_namespace

    @sub_namespace.setter
    def sub_namespace(self, sub_namespace):
        """Sets the sub_namespace of this TemplateRuleForCreateAlertTemplateInput.


        :param sub_namespace: The sub_namespace of this TemplateRuleForCreateAlertTemplateInput.  # noqa: E501
        :type: str
        """

        self._sub_namespace = sub_namespace

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
        if issubclass(TemplateRuleForCreateAlertTemplateInput, dict):
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
        if not isinstance(other, TemplateRuleForCreateAlertTemplateInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TemplateRuleForCreateAlertTemplateInput):
            return True

        return self.to_dict() != other.to_dict()
