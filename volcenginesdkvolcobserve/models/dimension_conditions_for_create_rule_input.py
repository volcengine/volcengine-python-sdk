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


class DimensionConditionsForCreateRuleInput(object):
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
        'meta_condition': 'MetaConditionForCreateRuleInput',
        'project_condition': 'ProjectConditionForCreateRuleInput',
        'tag_condition': 'TagConditionForCreateRuleInput',
        'type': 'str'
    }

    attribute_map = {
        'meta_condition': 'MetaCondition',
        'project_condition': 'ProjectCondition',
        'tag_condition': 'TagCondition',
        'type': 'Type'
    }

    def __init__(self, meta_condition=None, project_condition=None, tag_condition=None, type=None, _configuration=None):  # noqa: E501
        """DimensionConditionsForCreateRuleInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._meta_condition = None
        self._project_condition = None
        self._tag_condition = None
        self._type = None
        self.discriminator = None

        if meta_condition is not None:
            self.meta_condition = meta_condition
        if project_condition is not None:
            self.project_condition = project_condition
        if tag_condition is not None:
            self.tag_condition = tag_condition
        if type is not None:
            self.type = type

    @property
    def meta_condition(self):
        """Gets the meta_condition of this DimensionConditionsForCreateRuleInput.  # noqa: E501


        :return: The meta_condition of this DimensionConditionsForCreateRuleInput.  # noqa: E501
        :rtype: MetaConditionForCreateRuleInput
        """
        return self._meta_condition

    @meta_condition.setter
    def meta_condition(self, meta_condition):
        """Sets the meta_condition of this DimensionConditionsForCreateRuleInput.


        :param meta_condition: The meta_condition of this DimensionConditionsForCreateRuleInput.  # noqa: E501
        :type: MetaConditionForCreateRuleInput
        """

        self._meta_condition = meta_condition

    @property
    def project_condition(self):
        """Gets the project_condition of this DimensionConditionsForCreateRuleInput.  # noqa: E501


        :return: The project_condition of this DimensionConditionsForCreateRuleInput.  # noqa: E501
        :rtype: ProjectConditionForCreateRuleInput
        """
        return self._project_condition

    @project_condition.setter
    def project_condition(self, project_condition):
        """Sets the project_condition of this DimensionConditionsForCreateRuleInput.


        :param project_condition: The project_condition of this DimensionConditionsForCreateRuleInput.  # noqa: E501
        :type: ProjectConditionForCreateRuleInput
        """

        self._project_condition = project_condition

    @property
    def tag_condition(self):
        """Gets the tag_condition of this DimensionConditionsForCreateRuleInput.  # noqa: E501


        :return: The tag_condition of this DimensionConditionsForCreateRuleInput.  # noqa: E501
        :rtype: TagConditionForCreateRuleInput
        """
        return self._tag_condition

    @tag_condition.setter
    def tag_condition(self, tag_condition):
        """Sets the tag_condition of this DimensionConditionsForCreateRuleInput.


        :param tag_condition: The tag_condition of this DimensionConditionsForCreateRuleInput.  # noqa: E501
        :type: TagConditionForCreateRuleInput
        """

        self._tag_condition = tag_condition

    @property
    def type(self):
        """Gets the type of this DimensionConditionsForCreateRuleInput.  # noqa: E501


        :return: The type of this DimensionConditionsForCreateRuleInput.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DimensionConditionsForCreateRuleInput.


        :param type: The type of this DimensionConditionsForCreateRuleInput.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(DimensionConditionsForCreateRuleInput, dict):
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
        if not isinstance(other, DimensionConditionsForCreateRuleInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DimensionConditionsForCreateRuleInput):
            return True

        return self.to_dict() != other.to_dict()
