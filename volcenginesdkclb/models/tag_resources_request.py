# coding: utf-8

"""
    clb

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class TagResourcesRequest(object):
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
        'resource_ids': 'list[str]',
        'resource_type': 'str',
        'tags': 'list[TagForTagResourcesInput]'
    }

    attribute_map = {
        'resource_ids': 'ResourceIds',
        'resource_type': 'ResourceType',
        'tags': 'Tags'
    }

    def __init__(self, resource_ids=None, resource_type=None, tags=None, _configuration=None):  # noqa: E501
        """TagResourcesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._resource_ids = None
        self._resource_type = None
        self._tags = None
        self.discriminator = None

        if resource_ids is not None:
            self.resource_ids = resource_ids
        self.resource_type = resource_type
        if tags is not None:
            self.tags = tags

    @property
    def resource_ids(self):
        """Gets the resource_ids of this TagResourcesRequest.  # noqa: E501


        :return: The resource_ids of this TagResourcesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._resource_ids

    @resource_ids.setter
    def resource_ids(self, resource_ids):
        """Sets the resource_ids of this TagResourcesRequest.


        :param resource_ids: The resource_ids of this TagResourcesRequest.  # noqa: E501
        :type: list[str]
        """

        self._resource_ids = resource_ids

    @property
    def resource_type(self):
        """Gets the resource_type of this TagResourcesRequest.  # noqa: E501


        :return: The resource_type of this TagResourcesRequest.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this TagResourcesRequest.


        :param resource_type: The resource_type of this TagResourcesRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and resource_type is None:
            raise ValueError("Invalid value for `resource_type`, must not be `None`")  # noqa: E501
        allowed_values = ["CLB", "acl", "certificate", "listener", "servergroup", "rule", "ec"]  # noqa: E501
        if (self._configuration.client_side_validation and
                resource_type not in allowed_values):
            raise ValueError(
                "Invalid value for `resource_type` ({0}), must be one of {1}"  # noqa: E501
                .format(resource_type, allowed_values)
            )

        self._resource_type = resource_type

    @property
    def tags(self):
        """Gets the tags of this TagResourcesRequest.  # noqa: E501


        :return: The tags of this TagResourcesRequest.  # noqa: E501
        :rtype: list[TagForTagResourcesInput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this TagResourcesRequest.


        :param tags: The tags of this TagResourcesRequest.  # noqa: E501
        :type: list[TagForTagResourcesInput]
        """

        self._tags = tags

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
        if issubclass(TagResourcesRequest, dict):
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
        if not isinstance(other, TagResourcesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TagResourcesRequest):
            return True

        return self.to_dict() != other.to_dict()
