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


class ListRolesResponse(object):
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
        'limit': 'int',
        'offset': 'int',
        'role_metadata': 'list[RoleMetadataForListRolesOutput]',
        'total': 'int'
    }

    attribute_map = {
        'limit': 'Limit',
        'offset': 'Offset',
        'role_metadata': 'RoleMetadata',
        'total': 'Total'
    }

    def __init__(self, limit=None, offset=None, role_metadata=None, total=None, _configuration=None):  # noqa: E501
        """ListRolesResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._limit = None
        self._offset = None
        self._role_metadata = None
        self._total = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if role_metadata is not None:
            self.role_metadata = role_metadata
        if total is not None:
            self.total = total

    @property
    def limit(self):
        """Gets the limit of this ListRolesResponse.  # noqa: E501


        :return: The limit of this ListRolesResponse.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListRolesResponse.


        :param limit: The limit of this ListRolesResponse.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListRolesResponse.  # noqa: E501


        :return: The offset of this ListRolesResponse.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListRolesResponse.


        :param offset: The offset of this ListRolesResponse.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def role_metadata(self):
        """Gets the role_metadata of this ListRolesResponse.  # noqa: E501


        :return: The role_metadata of this ListRolesResponse.  # noqa: E501
        :rtype: list[RoleMetadataForListRolesOutput]
        """
        return self._role_metadata

    @role_metadata.setter
    def role_metadata(self, role_metadata):
        """Sets the role_metadata of this ListRolesResponse.


        :param role_metadata: The role_metadata of this ListRolesResponse.  # noqa: E501
        :type: list[RoleMetadataForListRolesOutput]
        """

        self._role_metadata = role_metadata

    @property
    def total(self):
        """Gets the total of this ListRolesResponse.  # noqa: E501


        :return: The total of this ListRolesResponse.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListRolesResponse.


        :param total: The total of this ListRolesResponse.  # noqa: E501
        :type: int
        """

        self._total = total

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
        if issubclass(ListRolesResponse, dict):
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
        if not isinstance(other, ListRolesResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListRolesResponse):
            return True

        return self.to_dict() != other.to_dict()
