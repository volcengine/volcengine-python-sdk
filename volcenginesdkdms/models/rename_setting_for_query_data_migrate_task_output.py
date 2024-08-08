# coding: utf-8

"""
    dms

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class RenameSettingForQueryDataMigrateTaskOutput(object):
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
        'pattern': 'str',
        'replace_str': 'str'
    }

    attribute_map = {
        'pattern': 'Pattern',
        'replace_str': 'ReplaceStr'
    }

    def __init__(self, pattern=None, replace_str=None, _configuration=None):  # noqa: E501
        """RenameSettingForQueryDataMigrateTaskOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._pattern = None
        self._replace_str = None
        self.discriminator = None

        if pattern is not None:
            self.pattern = pattern
        if replace_str is not None:
            self.replace_str = replace_str

    @property
    def pattern(self):
        """Gets the pattern of this RenameSettingForQueryDataMigrateTaskOutput.  # noqa: E501


        :return: The pattern of this RenameSettingForQueryDataMigrateTaskOutput.  # noqa: E501
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        """Sets the pattern of this RenameSettingForQueryDataMigrateTaskOutput.


        :param pattern: The pattern of this RenameSettingForQueryDataMigrateTaskOutput.  # noqa: E501
        :type: str
        """

        self._pattern = pattern

    @property
    def replace_str(self):
        """Gets the replace_str of this RenameSettingForQueryDataMigrateTaskOutput.  # noqa: E501


        :return: The replace_str of this RenameSettingForQueryDataMigrateTaskOutput.  # noqa: E501
        :rtype: str
        """
        return self._replace_str

    @replace_str.setter
    def replace_str(self, replace_str):
        """Sets the replace_str of this RenameSettingForQueryDataMigrateTaskOutput.


        :param replace_str: The replace_str of this RenameSettingForQueryDataMigrateTaskOutput.  # noqa: E501
        :type: str
        """

        self._replace_str = replace_str

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
        if issubclass(RenameSettingForQueryDataMigrateTaskOutput, dict):
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
        if not isinstance(other, RenameSettingForQueryDataMigrateTaskOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RenameSettingForQueryDataMigrateTaskOutput):
            return True

        return self.to_dict() != other.to_dict()
