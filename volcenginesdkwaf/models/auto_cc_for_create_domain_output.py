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


class AutoCCForCreateDomainOutput(object):
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
        'action': 'str',
        'auto_cc_enable': 'int',
        'defence_level': 'str'
    }

    attribute_map = {
        'action': 'Action',
        'auto_cc_enable': 'AutoCCEnable',
        'defence_level': 'DefenceLevel'
    }

    def __init__(self, action=None, auto_cc_enable=None, defence_level=None, _configuration=None):  # noqa: E501
        """AutoCCForCreateDomainOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._action = None
        self._auto_cc_enable = None
        self._defence_level = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if auto_cc_enable is not None:
            self.auto_cc_enable = auto_cc_enable
        if defence_level is not None:
            self.defence_level = defence_level

    @property
    def action(self):
        """Gets the action of this AutoCCForCreateDomainOutput.  # noqa: E501


        :return: The action of this AutoCCForCreateDomainOutput.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this AutoCCForCreateDomainOutput.


        :param action: The action of this AutoCCForCreateDomainOutput.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def auto_cc_enable(self):
        """Gets the auto_cc_enable of this AutoCCForCreateDomainOutput.  # noqa: E501


        :return: The auto_cc_enable of this AutoCCForCreateDomainOutput.  # noqa: E501
        :rtype: int
        """
        return self._auto_cc_enable

    @auto_cc_enable.setter
    def auto_cc_enable(self, auto_cc_enable):
        """Sets the auto_cc_enable of this AutoCCForCreateDomainOutput.


        :param auto_cc_enable: The auto_cc_enable of this AutoCCForCreateDomainOutput.  # noqa: E501
        :type: int
        """

        self._auto_cc_enable = auto_cc_enable

    @property
    def defence_level(self):
        """Gets the defence_level of this AutoCCForCreateDomainOutput.  # noqa: E501


        :return: The defence_level of this AutoCCForCreateDomainOutput.  # noqa: E501
        :rtype: str
        """
        return self._defence_level

    @defence_level.setter
    def defence_level(self, defence_level):
        """Sets the defence_level of this AutoCCForCreateDomainOutput.


        :param defence_level: The defence_level of this AutoCCForCreateDomainOutput.  # noqa: E501
        :type: str
        """

        self._defence_level = defence_level

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
        if issubclass(AutoCCForCreateDomainOutput, dict):
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
        if not isinstance(other, AutoCCForCreateDomainOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AutoCCForCreateDomainOutput):
            return True

        return self.to_dict() != other.to_dict()
