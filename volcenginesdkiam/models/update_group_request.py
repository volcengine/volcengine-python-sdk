# coding: utf-8

"""
    iam

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class UpdateGroupRequest(object):
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
        'new_description': 'str',
        'new_display_name': 'str',
        'new_user_group_name': 'str',
        'user_group_name': 'str'
    }

    attribute_map = {
        'new_description': 'NewDescription',
        'new_display_name': 'NewDisplayName',
        'new_user_group_name': 'NewUserGroupName',
        'user_group_name': 'UserGroupName'
    }

    def __init__(self, new_description=None, new_display_name=None, new_user_group_name=None, user_group_name=None, _configuration=None):  # noqa: E501
        """UpdateGroupRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._new_description = None
        self._new_display_name = None
        self._new_user_group_name = None
        self._user_group_name = None
        self.discriminator = None

        if new_description is not None:
            self.new_description = new_description
        if new_display_name is not None:
            self.new_display_name = new_display_name
        if new_user_group_name is not None:
            self.new_user_group_name = new_user_group_name
        self.user_group_name = user_group_name

    @property
    def new_description(self):
        """Gets the new_description of this UpdateGroupRequest.  # noqa: E501


        :return: The new_description of this UpdateGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._new_description

    @new_description.setter
    def new_description(self, new_description):
        """Sets the new_description of this UpdateGroupRequest.


        :param new_description: The new_description of this UpdateGroupRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                new_description is not None and len(new_description) > 128):
            raise ValueError("Invalid value for `new_description`, length must be less than or equal to `128`")  # noqa: E501

        self._new_description = new_description

    @property
    def new_display_name(self):
        """Gets the new_display_name of this UpdateGroupRequest.  # noqa: E501


        :return: The new_display_name of this UpdateGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._new_display_name

    @new_display_name.setter
    def new_display_name(self, new_display_name):
        """Sets the new_display_name of this UpdateGroupRequest.


        :param new_display_name: The new_display_name of this UpdateGroupRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                new_display_name is not None and len(new_display_name) > 64):
            raise ValueError("Invalid value for `new_display_name`, length must be less than or equal to `64`")  # noqa: E501

        self._new_display_name = new_display_name

    @property
    def new_user_group_name(self):
        """Gets the new_user_group_name of this UpdateGroupRequest.  # noqa: E501


        :return: The new_user_group_name of this UpdateGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._new_user_group_name

    @new_user_group_name.setter
    def new_user_group_name(self, new_user_group_name):
        """Sets the new_user_group_name of this UpdateGroupRequest.


        :param new_user_group_name: The new_user_group_name of this UpdateGroupRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                new_user_group_name is not None and len(new_user_group_name) > 64):
            raise ValueError("Invalid value for `new_user_group_name`, length must be less than or equal to `64`")  # noqa: E501

        self._new_user_group_name = new_user_group_name

    @property
    def user_group_name(self):
        """Gets the user_group_name of this UpdateGroupRequest.  # noqa: E501


        :return: The user_group_name of this UpdateGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._user_group_name

    @user_group_name.setter
    def user_group_name(self, user_group_name):
        """Sets the user_group_name of this UpdateGroupRequest.


        :param user_group_name: The user_group_name of this UpdateGroupRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and user_group_name is None:
            raise ValueError("Invalid value for `user_group_name`, must not be `None`")  # noqa: E501

        self._user_group_name = user_group_name

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
        if issubclass(UpdateGroupRequest, dict):
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
        if not isinstance(other, UpdateGroupRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateGroupRequest):
            return True

        return self.to_dict() != other.to_dict()