# coding: utf-8

"""
    cdn

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ConvertConvertConditionForAddCdnDomainInput(object):
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
        'condition_groups': 'list[ConditionGroupForAddCdnDomainInput]',
        'connective': 'str',
        'is_group': 'bool'
    }

    attribute_map = {
        'condition_groups': 'ConditionGroups',
        'connective': 'Connective',
        'is_group': 'IsGroup'
    }

    def __init__(self, condition_groups=None, connective=None, is_group=None, _configuration=None):  # noqa: E501
        """ConvertConvertConditionForAddCdnDomainInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._condition_groups = None
        self._connective = None
        self._is_group = None
        self.discriminator = None

        if condition_groups is not None:
            self.condition_groups = condition_groups
        if connective is not None:
            self.connective = connective
        if is_group is not None:
            self.is_group = is_group

    @property
    def condition_groups(self):
        """Gets the condition_groups of this ConvertConvertConditionForAddCdnDomainInput.  # noqa: E501


        :return: The condition_groups of this ConvertConvertConditionForAddCdnDomainInput.  # noqa: E501
        :rtype: list[ConditionGroupForAddCdnDomainInput]
        """
        return self._condition_groups

    @condition_groups.setter
    def condition_groups(self, condition_groups):
        """Sets the condition_groups of this ConvertConvertConditionForAddCdnDomainInput.


        :param condition_groups: The condition_groups of this ConvertConvertConditionForAddCdnDomainInput.  # noqa: E501
        :type: list[ConditionGroupForAddCdnDomainInput]
        """

        self._condition_groups = condition_groups

    @property
    def connective(self):
        """Gets the connective of this ConvertConvertConditionForAddCdnDomainInput.  # noqa: E501


        :return: The connective of this ConvertConvertConditionForAddCdnDomainInput.  # noqa: E501
        :rtype: str
        """
        return self._connective

    @connective.setter
    def connective(self, connective):
        """Sets the connective of this ConvertConvertConditionForAddCdnDomainInput.


        :param connective: The connective of this ConvertConvertConditionForAddCdnDomainInput.  # noqa: E501
        :type: str
        """

        self._connective = connective

    @property
    def is_group(self):
        """Gets the is_group of this ConvertConvertConditionForAddCdnDomainInput.  # noqa: E501


        :return: The is_group of this ConvertConvertConditionForAddCdnDomainInput.  # noqa: E501
        :rtype: bool
        """
        return self._is_group

    @is_group.setter
    def is_group(self, is_group):
        """Sets the is_group of this ConvertConvertConditionForAddCdnDomainInput.


        :param is_group: The is_group of this ConvertConvertConditionForAddCdnDomainInput.  # noqa: E501
        :type: bool
        """

        self._is_group = is_group

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
        if issubclass(ConvertConvertConditionForAddCdnDomainInput, dict):
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
        if not isinstance(other, ConvertConvertConditionForAddCdnDomainInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConvertConvertConditionForAddCdnDomainInput):
            return True

        return self.to_dict() != other.to_dict()
