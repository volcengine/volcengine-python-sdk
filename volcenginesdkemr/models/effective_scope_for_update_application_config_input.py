# coding: utf-8

"""
    emr

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class EffectiveScopeForUpdateApplicationConfigInput(object):
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
        'component_names': 'list[str]',
        'effective_type': 'str',
        'node_group_ids': 'list[str]',
        'node_group_names': 'list[str]',
        'node_group_types': 'list[str]',
        'node_ids': 'list[str]',
        'node_names': 'list[str]'
    }

    attribute_map = {
        'component_names': 'ComponentNames',
        'effective_type': 'EffectiveType',
        'node_group_ids': 'NodeGroupIds',
        'node_group_names': 'NodeGroupNames',
        'node_group_types': 'NodeGroupTypes',
        'node_ids': 'NodeIds',
        'node_names': 'NodeNames'
    }

    def __init__(self, component_names=None, effective_type=None, node_group_ids=None, node_group_names=None, node_group_types=None, node_ids=None, node_names=None, _configuration=None):  # noqa: E501
        """EffectiveScopeForUpdateApplicationConfigInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._component_names = None
        self._effective_type = None
        self._node_group_ids = None
        self._node_group_names = None
        self._node_group_types = None
        self._node_ids = None
        self._node_names = None
        self.discriminator = None

        if component_names is not None:
            self.component_names = component_names
        if effective_type is not None:
            self.effective_type = effective_type
        if node_group_ids is not None:
            self.node_group_ids = node_group_ids
        if node_group_names is not None:
            self.node_group_names = node_group_names
        if node_group_types is not None:
            self.node_group_types = node_group_types
        if node_ids is not None:
            self.node_ids = node_ids
        if node_names is not None:
            self.node_names = node_names

    @property
    def component_names(self):
        """Gets the component_names of this EffectiveScopeForUpdateApplicationConfigInput.  # noqa: E501


        :return: The component_names of this EffectiveScopeForUpdateApplicationConfigInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._component_names

    @component_names.setter
    def component_names(self, component_names):
        """Sets the component_names of this EffectiveScopeForUpdateApplicationConfigInput.


        :param component_names: The component_names of this EffectiveScopeForUpdateApplicationConfigInput.  # noqa: E501
        :type: list[str]
        """

        self._component_names = component_names

    @property
    def effective_type(self):
        """Gets the effective_type of this EffectiveScopeForUpdateApplicationConfigInput.  # noqa: E501


        :return: The effective_type of this EffectiveScopeForUpdateApplicationConfigInput.  # noqa: E501
        :rtype: str
        """
        return self._effective_type

    @effective_type.setter
    def effective_type(self, effective_type):
        """Sets the effective_type of this EffectiveScopeForUpdateApplicationConfigInput.


        :param effective_type: The effective_type of this EffectiveScopeForUpdateApplicationConfigInput.  # noqa: E501
        :type: str
        """
        allowed_values = ["CLUSTER", "NODE_GROUP_NAME", "NODE_GROUP_ID", "NODE_GROUP_TYPE", "NODE_NAME", "NODE_ID", "COMPONENT_NAME"]  # noqa: E501
        if (self._configuration.client_side_validation and
                effective_type not in allowed_values):
            raise ValueError(
                "Invalid value for `effective_type` ({0}), must be one of {1}"  # noqa: E501
                .format(effective_type, allowed_values)
            )

        self._effective_type = effective_type

    @property
    def node_group_ids(self):
        """Gets the node_group_ids of this EffectiveScopeForUpdateApplicationConfigInput.  # noqa: E501


        :return: The node_group_ids of this EffectiveScopeForUpdateApplicationConfigInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._node_group_ids

    @node_group_ids.setter
    def node_group_ids(self, node_group_ids):
        """Sets the node_group_ids of this EffectiveScopeForUpdateApplicationConfigInput.


        :param node_group_ids: The node_group_ids of this EffectiveScopeForUpdateApplicationConfigInput.  # noqa: E501
        :type: list[str]
        """

        self._node_group_ids = node_group_ids

    @property
    def node_group_names(self):
        """Gets the node_group_names of this EffectiveScopeForUpdateApplicationConfigInput.  # noqa: E501


        :return: The node_group_names of this EffectiveScopeForUpdateApplicationConfigInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._node_group_names

    @node_group_names.setter
    def node_group_names(self, node_group_names):
        """Sets the node_group_names of this EffectiveScopeForUpdateApplicationConfigInput.


        :param node_group_names: The node_group_names of this EffectiveScopeForUpdateApplicationConfigInput.  # noqa: E501
        :type: list[str]
        """

        self._node_group_names = node_group_names

    @property
    def node_group_types(self):
        """Gets the node_group_types of this EffectiveScopeForUpdateApplicationConfigInput.  # noqa: E501


        :return: The node_group_types of this EffectiveScopeForUpdateApplicationConfigInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._node_group_types

    @node_group_types.setter
    def node_group_types(self, node_group_types):
        """Sets the node_group_types of this EffectiveScopeForUpdateApplicationConfigInput.


        :param node_group_types: The node_group_types of this EffectiveScopeForUpdateApplicationConfigInput.  # noqa: E501
        :type: list[str]
        """

        self._node_group_types = node_group_types

    @property
    def node_ids(self):
        """Gets the node_ids of this EffectiveScopeForUpdateApplicationConfigInput.  # noqa: E501


        :return: The node_ids of this EffectiveScopeForUpdateApplicationConfigInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._node_ids

    @node_ids.setter
    def node_ids(self, node_ids):
        """Sets the node_ids of this EffectiveScopeForUpdateApplicationConfigInput.


        :param node_ids: The node_ids of this EffectiveScopeForUpdateApplicationConfigInput.  # noqa: E501
        :type: list[str]
        """

        self._node_ids = node_ids

    @property
    def node_names(self):
        """Gets the node_names of this EffectiveScopeForUpdateApplicationConfigInput.  # noqa: E501


        :return: The node_names of this EffectiveScopeForUpdateApplicationConfigInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._node_names

    @node_names.setter
    def node_names(self, node_names):
        """Sets the node_names of this EffectiveScopeForUpdateApplicationConfigInput.


        :param node_names: The node_names of this EffectiveScopeForUpdateApplicationConfigInput.  # noqa: E501
        :type: list[str]
        """

        self._node_names = node_names

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
        if issubclass(EffectiveScopeForUpdateApplicationConfigInput, dict):
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
        if not isinstance(other, EffectiveScopeForUpdateApplicationConfigInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EffectiveScopeForUpdateApplicationConfigInput):
            return True

        return self.to_dict() != other.to_dict()
