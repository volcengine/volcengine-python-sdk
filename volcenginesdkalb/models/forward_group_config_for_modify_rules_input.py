# coding: utf-8

"""
    alb

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ForwardGroupConfigForModifyRulesInput(object):
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
        'server_group_tuples': 'list[ForwardGroupConfigServerGroupTupleForModifyRulesInput]',
        'sticky_session_enabled': 'str',
        'sticky_session_timeout': 'int'
    }

    attribute_map = {
        'server_group_tuples': 'ServerGroupTuples',
        'sticky_session_enabled': 'StickySessionEnabled',
        'sticky_session_timeout': 'StickySessionTimeout'
    }

    def __init__(self, server_group_tuples=None, sticky_session_enabled=None, sticky_session_timeout=None, _configuration=None):  # noqa: E501
        """ForwardGroupConfigForModifyRulesInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._server_group_tuples = None
        self._sticky_session_enabled = None
        self._sticky_session_timeout = None
        self.discriminator = None

        if server_group_tuples is not None:
            self.server_group_tuples = server_group_tuples
        if sticky_session_enabled is not None:
            self.sticky_session_enabled = sticky_session_enabled
        if sticky_session_timeout is not None:
            self.sticky_session_timeout = sticky_session_timeout

    @property
    def server_group_tuples(self):
        """Gets the server_group_tuples of this ForwardGroupConfigForModifyRulesInput.  # noqa: E501


        :return: The server_group_tuples of this ForwardGroupConfigForModifyRulesInput.  # noqa: E501
        :rtype: list[ForwardGroupConfigServerGroupTupleForModifyRulesInput]
        """
        return self._server_group_tuples

    @server_group_tuples.setter
    def server_group_tuples(self, server_group_tuples):
        """Sets the server_group_tuples of this ForwardGroupConfigForModifyRulesInput.


        :param server_group_tuples: The server_group_tuples of this ForwardGroupConfigForModifyRulesInput.  # noqa: E501
        :type: list[ForwardGroupConfigServerGroupTupleForModifyRulesInput]
        """

        self._server_group_tuples = server_group_tuples

    @property
    def sticky_session_enabled(self):
        """Gets the sticky_session_enabled of this ForwardGroupConfigForModifyRulesInput.  # noqa: E501


        :return: The sticky_session_enabled of this ForwardGroupConfigForModifyRulesInput.  # noqa: E501
        :rtype: str
        """
        return self._sticky_session_enabled

    @sticky_session_enabled.setter
    def sticky_session_enabled(self, sticky_session_enabled):
        """Sets the sticky_session_enabled of this ForwardGroupConfigForModifyRulesInput.


        :param sticky_session_enabled: The sticky_session_enabled of this ForwardGroupConfigForModifyRulesInput.  # noqa: E501
        :type: str
        """

        self._sticky_session_enabled = sticky_session_enabled

    @property
    def sticky_session_timeout(self):
        """Gets the sticky_session_timeout of this ForwardGroupConfigForModifyRulesInput.  # noqa: E501


        :return: The sticky_session_timeout of this ForwardGroupConfigForModifyRulesInput.  # noqa: E501
        :rtype: int
        """
        return self._sticky_session_timeout

    @sticky_session_timeout.setter
    def sticky_session_timeout(self, sticky_session_timeout):
        """Sets the sticky_session_timeout of this ForwardGroupConfigForModifyRulesInput.


        :param sticky_session_timeout: The sticky_session_timeout of this ForwardGroupConfigForModifyRulesInput.  # noqa: E501
        :type: int
        """

        self._sticky_session_timeout = sticky_session_timeout

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
        if issubclass(ForwardGroupConfigForModifyRulesInput, dict):
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
        if not isinstance(other, ForwardGroupConfigForModifyRulesInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ForwardGroupConfigForModifyRulesInput):
            return True

        return self.to_dict() != other.to_dict()
