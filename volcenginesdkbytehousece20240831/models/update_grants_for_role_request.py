# coding: utf-8

"""
    bytehouse_ce20240831

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class UpdateGrantsForRoleRequest(object):
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
        'action_type': 'str',
        'grants': 'list[GrantForUpdateGrantsForRoleInput]',
        'role_id': 'int'
    }

    attribute_map = {
        'action_type': 'ActionType',
        'grants': 'Grants',
        'role_id': 'RoleID'
    }

    def __init__(self, action_type=None, grants=None, role_id=None, _configuration=None):  # noqa: E501
        """UpdateGrantsForRoleRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._action_type = None
        self._grants = None
        self._role_id = None
        self.discriminator = None

        self.action_type = action_type
        if grants is not None:
            self.grants = grants
        self.role_id = role_id

    @property
    def action_type(self):
        """Gets the action_type of this UpdateGrantsForRoleRequest.  # noqa: E501


        :return: The action_type of this UpdateGrantsForRoleRequest.  # noqa: E501
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """Sets the action_type of this UpdateGrantsForRoleRequest.


        :param action_type: The action_type of this UpdateGrantsForRoleRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and action_type is None:
            raise ValueError("Invalid value for `action_type`, must not be `None`")  # noqa: E501
        allowed_values = ["GRANT", "REVOKE"]  # noqa: E501
        if (self._configuration.client_side_validation and
                action_type not in allowed_values):
            raise ValueError(
                "Invalid value for `action_type` ({0}), must be one of {1}"  # noqa: E501
                .format(action_type, allowed_values)
            )

        self._action_type = action_type

    @property
    def grants(self):
        """Gets the grants of this UpdateGrantsForRoleRequest.  # noqa: E501


        :return: The grants of this UpdateGrantsForRoleRequest.  # noqa: E501
        :rtype: list[GrantForUpdateGrantsForRoleInput]
        """
        return self._grants

    @grants.setter
    def grants(self, grants):
        """Sets the grants of this UpdateGrantsForRoleRequest.


        :param grants: The grants of this UpdateGrantsForRoleRequest.  # noqa: E501
        :type: list[GrantForUpdateGrantsForRoleInput]
        """

        self._grants = grants

    @property
    def role_id(self):
        """Gets the role_id of this UpdateGrantsForRoleRequest.  # noqa: E501


        :return: The role_id of this UpdateGrantsForRoleRequest.  # noqa: E501
        :rtype: int
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this UpdateGrantsForRoleRequest.


        :param role_id: The role_id of this UpdateGrantsForRoleRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and role_id is None:
            raise ValueError("Invalid value for `role_id`, must not be `None`")  # noqa: E501

        self._role_id = role_id

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
        if issubclass(UpdateGrantsForRoleRequest, dict):
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
        if not isinstance(other, UpdateGrantsForRoleRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateGrantsForRoleRequest):
            return True

        return self.to_dict() != other.to_dict()
