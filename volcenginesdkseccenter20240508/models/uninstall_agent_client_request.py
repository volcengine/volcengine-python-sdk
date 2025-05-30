# coding: utf-8

"""
    seccenter20240508

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class UninstallAgentClientRequest(object):
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
        'agent_ids': 'list[str]',
        'reasons': 'list[str]',
        'suggestion': 'str',
        'type': 'str'
    }

    attribute_map = {
        'agent_ids': 'AgentIDs',
        'reasons': 'Reasons',
        'suggestion': 'Suggestion',
        'type': 'Type'
    }

    def __init__(self, agent_ids=None, reasons=None, suggestion=None, type=None, _configuration=None):  # noqa: E501
        """UninstallAgentClientRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._agent_ids = None
        self._reasons = None
        self._suggestion = None
        self._type = None
        self.discriminator = None

        if agent_ids is not None:
            self.agent_ids = agent_ids
        if reasons is not None:
            self.reasons = reasons
        if suggestion is not None:
            self.suggestion = suggestion
        if type is not None:
            self.type = type

    @property
    def agent_ids(self):
        """Gets the agent_ids of this UninstallAgentClientRequest.  # noqa: E501


        :return: The agent_ids of this UninstallAgentClientRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._agent_ids

    @agent_ids.setter
    def agent_ids(self, agent_ids):
        """Sets the agent_ids of this UninstallAgentClientRequest.


        :param agent_ids: The agent_ids of this UninstallAgentClientRequest.  # noqa: E501
        :type: list[str]
        """

        self._agent_ids = agent_ids

    @property
    def reasons(self):
        """Gets the reasons of this UninstallAgentClientRequest.  # noqa: E501


        :return: The reasons of this UninstallAgentClientRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._reasons

    @reasons.setter
    def reasons(self, reasons):
        """Sets the reasons of this UninstallAgentClientRequest.


        :param reasons: The reasons of this UninstallAgentClientRequest.  # noqa: E501
        :type: list[str]
        """

        self._reasons = reasons

    @property
    def suggestion(self):
        """Gets the suggestion of this UninstallAgentClientRequest.  # noqa: E501


        :return: The suggestion of this UninstallAgentClientRequest.  # noqa: E501
        :rtype: str
        """
        return self._suggestion

    @suggestion.setter
    def suggestion(self, suggestion):
        """Sets the suggestion of this UninstallAgentClientRequest.


        :param suggestion: The suggestion of this UninstallAgentClientRequest.  # noqa: E501
        :type: str
        """

        self._suggestion = suggestion

    @property
    def type(self):
        """Gets the type of this UninstallAgentClientRequest.  # noqa: E501


        :return: The type of this UninstallAgentClientRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UninstallAgentClientRequest.


        :param type: The type of this UninstallAgentClientRequest.  # noqa: E501
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
        if issubclass(UninstallAgentClientRequest, dict):
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
        if not isinstance(other, UninstallAgentClientRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UninstallAgentClientRequest):
            return True

        return self.to_dict() != other.to_dict()
