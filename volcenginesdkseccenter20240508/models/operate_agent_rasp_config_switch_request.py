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


class OperateAgentRaspConfigSwitchRequest(object):
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
        'switch_on': 'bool',
        'top_group_id': 'str'
    }

    attribute_map = {
        'agent_ids': 'AgentIDs',
        'switch_on': 'SwitchOn',
        'top_group_id': 'TopGroupID'
    }

    def __init__(self, agent_ids=None, switch_on=None, top_group_id=None, _configuration=None):  # noqa: E501
        """OperateAgentRaspConfigSwitchRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._agent_ids = None
        self._switch_on = None
        self._top_group_id = None
        self.discriminator = None

        if agent_ids is not None:
            self.agent_ids = agent_ids
        if switch_on is not None:
            self.switch_on = switch_on
        if top_group_id is not None:
            self.top_group_id = top_group_id

    @property
    def agent_ids(self):
        """Gets the agent_ids of this OperateAgentRaspConfigSwitchRequest.  # noqa: E501


        :return: The agent_ids of this OperateAgentRaspConfigSwitchRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._agent_ids

    @agent_ids.setter
    def agent_ids(self, agent_ids):
        """Sets the agent_ids of this OperateAgentRaspConfigSwitchRequest.


        :param agent_ids: The agent_ids of this OperateAgentRaspConfigSwitchRequest.  # noqa: E501
        :type: list[str]
        """

        self._agent_ids = agent_ids

    @property
    def switch_on(self):
        """Gets the switch_on of this OperateAgentRaspConfigSwitchRequest.  # noqa: E501


        :return: The switch_on of this OperateAgentRaspConfigSwitchRequest.  # noqa: E501
        :rtype: bool
        """
        return self._switch_on

    @switch_on.setter
    def switch_on(self, switch_on):
        """Sets the switch_on of this OperateAgentRaspConfigSwitchRequest.


        :param switch_on: The switch_on of this OperateAgentRaspConfigSwitchRequest.  # noqa: E501
        :type: bool
        """

        self._switch_on = switch_on

    @property
    def top_group_id(self):
        """Gets the top_group_id of this OperateAgentRaspConfigSwitchRequest.  # noqa: E501


        :return: The top_group_id of this OperateAgentRaspConfigSwitchRequest.  # noqa: E501
        :rtype: str
        """
        return self._top_group_id

    @top_group_id.setter
    def top_group_id(self, top_group_id):
        """Sets the top_group_id of this OperateAgentRaspConfigSwitchRequest.


        :param top_group_id: The top_group_id of this OperateAgentRaspConfigSwitchRequest.  # noqa: E501
        :type: str
        """

        self._top_group_id = top_group_id

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
        if issubclass(OperateAgentRaspConfigSwitchRequest, dict):
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
        if not isinstance(other, OperateAgentRaspConfigSwitchRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OperateAgentRaspConfigSwitchRequest):
            return True

        return self.to_dict() != other.to_dict()
