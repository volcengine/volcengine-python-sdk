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


class CreateClusterUserGroupRequest(object):
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
        'cluster_id': 'str',
        'description': 'str',
        'members': 'list[str]',
        'user_group_name': 'str'
    }

    attribute_map = {
        'cluster_id': 'ClusterId',
        'description': 'Description',
        'members': 'Members',
        'user_group_name': 'UserGroupName'
    }

    def __init__(self, cluster_id=None, description=None, members=None, user_group_name=None, _configuration=None):  # noqa: E501
        """CreateClusterUserGroupRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cluster_id = None
        self._description = None
        self._members = None
        self._user_group_name = None
        self.discriminator = None

        self.cluster_id = cluster_id
        if description is not None:
            self.description = description
        if members is not None:
            self.members = members
        self.user_group_name = user_group_name

    @property
    def cluster_id(self):
        """Gets the cluster_id of this CreateClusterUserGroupRequest.  # noqa: E501


        :return: The cluster_id of this CreateClusterUserGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this CreateClusterUserGroupRequest.


        :param cluster_id: The cluster_id of this CreateClusterUserGroupRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and cluster_id is None:
            raise ValueError("Invalid value for `cluster_id`, must not be `None`")  # noqa: E501

        self._cluster_id = cluster_id

    @property
    def description(self):
        """Gets the description of this CreateClusterUserGroupRequest.  # noqa: E501


        :return: The description of this CreateClusterUserGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateClusterUserGroupRequest.


        :param description: The description of this CreateClusterUserGroupRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def members(self):
        """Gets the members of this CreateClusterUserGroupRequest.  # noqa: E501


        :return: The members of this CreateClusterUserGroupRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this CreateClusterUserGroupRequest.


        :param members: The members of this CreateClusterUserGroupRequest.  # noqa: E501
        :type: list[str]
        """

        self._members = members

    @property
    def user_group_name(self):
        """Gets the user_group_name of this CreateClusterUserGroupRequest.  # noqa: E501


        :return: The user_group_name of this CreateClusterUserGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._user_group_name

    @user_group_name.setter
    def user_group_name(self, user_group_name):
        """Sets the user_group_name of this CreateClusterUserGroupRequest.


        :param user_group_name: The user_group_name of this CreateClusterUserGroupRequest.  # noqa: E501
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
        if issubclass(CreateClusterUserGroupRequest, dict):
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
        if not isinstance(other, CreateClusterUserGroupRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateClusterUserGroupRequest):
            return True

        return self.to_dict() != other.to_dict()
