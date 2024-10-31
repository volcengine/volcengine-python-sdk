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


class BotSequenceForCreateDomainOutput(object):
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
        'bot_sequence_default_action': 'int',
        'bot_sequence_enable': 'int'
    }

    attribute_map = {
        'bot_sequence_default_action': 'BotSequenceDefaultAction',
        'bot_sequence_enable': 'BotSequenceEnable'
    }

    def __init__(self, bot_sequence_default_action=None, bot_sequence_enable=None, _configuration=None):  # noqa: E501
        """BotSequenceForCreateDomainOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bot_sequence_default_action = None
        self._bot_sequence_enable = None
        self.discriminator = None

        if bot_sequence_default_action is not None:
            self.bot_sequence_default_action = bot_sequence_default_action
        if bot_sequence_enable is not None:
            self.bot_sequence_enable = bot_sequence_enable

    @property
    def bot_sequence_default_action(self):
        """Gets the bot_sequence_default_action of this BotSequenceForCreateDomainOutput.  # noqa: E501


        :return: The bot_sequence_default_action of this BotSequenceForCreateDomainOutput.  # noqa: E501
        :rtype: int
        """
        return self._bot_sequence_default_action

    @bot_sequence_default_action.setter
    def bot_sequence_default_action(self, bot_sequence_default_action):
        """Sets the bot_sequence_default_action of this BotSequenceForCreateDomainOutput.


        :param bot_sequence_default_action: The bot_sequence_default_action of this BotSequenceForCreateDomainOutput.  # noqa: E501
        :type: int
        """

        self._bot_sequence_default_action = bot_sequence_default_action

    @property
    def bot_sequence_enable(self):
        """Gets the bot_sequence_enable of this BotSequenceForCreateDomainOutput.  # noqa: E501


        :return: The bot_sequence_enable of this BotSequenceForCreateDomainOutput.  # noqa: E501
        :rtype: int
        """
        return self._bot_sequence_enable

    @bot_sequence_enable.setter
    def bot_sequence_enable(self, bot_sequence_enable):
        """Sets the bot_sequence_enable of this BotSequenceForCreateDomainOutput.


        :param bot_sequence_enable: The bot_sequence_enable of this BotSequenceForCreateDomainOutput.  # noqa: E501
        :type: int
        """

        self._bot_sequence_enable = bot_sequence_enable

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
        if issubclass(BotSequenceForCreateDomainOutput, dict):
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
        if not isinstance(other, BotSequenceForCreateDomainOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BotSequenceForCreateDomainOutput):
            return True

        return self.to_dict() != other.to_dict()