# coding: utf-8

"""
    livesaas20230801

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class UpdateSubAccountRequest(object):
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
        'name': 'str',
        'nick_name': 'str',
        'organization_id': 'int',
        'role_ids': 'list[int]'
    }

    attribute_map = {
        'name': 'Name',
        'nick_name': 'NickName',
        'organization_id': 'OrganizationId',
        'role_ids': 'RoleIds'
    }

    def __init__(self, name=None, nick_name=None, organization_id=None, role_ids=None, _configuration=None):  # noqa: E501
        """UpdateSubAccountRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._nick_name = None
        self._organization_id = None
        self._role_ids = None
        self.discriminator = None

        self.name = name
        if nick_name is not None:
            self.nick_name = nick_name
        if organization_id is not None:
            self.organization_id = organization_id
        if role_ids is not None:
            self.role_ids = role_ids

    @property
    def name(self):
        """Gets the name of this UpdateSubAccountRequest.  # noqa: E501


        :return: The name of this UpdateSubAccountRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateSubAccountRequest.


        :param name: The name of this UpdateSubAccountRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def nick_name(self):
        """Gets the nick_name of this UpdateSubAccountRequest.  # noqa: E501


        :return: The nick_name of this UpdateSubAccountRequest.  # noqa: E501
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        """Sets the nick_name of this UpdateSubAccountRequest.


        :param nick_name: The nick_name of this UpdateSubAccountRequest.  # noqa: E501
        :type: str
        """

        self._nick_name = nick_name

    @property
    def organization_id(self):
        """Gets the organization_id of this UpdateSubAccountRequest.  # noqa: E501


        :return: The organization_id of this UpdateSubAccountRequest.  # noqa: E501
        :rtype: int
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this UpdateSubAccountRequest.


        :param organization_id: The organization_id of this UpdateSubAccountRequest.  # noqa: E501
        :type: int
        """

        self._organization_id = organization_id

    @property
    def role_ids(self):
        """Gets the role_ids of this UpdateSubAccountRequest.  # noqa: E501


        :return: The role_ids of this UpdateSubAccountRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._role_ids

    @role_ids.setter
    def role_ids(self, role_ids):
        """Sets the role_ids of this UpdateSubAccountRequest.


        :param role_ids: The role_ids of this UpdateSubAccountRequest.  # noqa: E501
        :type: list[int]
        """

        self._role_ids = role_ids

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
        if issubclass(UpdateSubAccountRequest, dict):
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
        if not isinstance(other, UpdateSubAccountRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateSubAccountRequest):
            return True

        return self.to_dict() != other.to_dict()
