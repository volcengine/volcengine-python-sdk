# coding: utf-8

"""
    dataleap

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DTSOpenListTagResourceGroupsResponse(object):
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
        'next_token': 'str',
        'resource_tags': 'list[ResourceTagForDTSOpenListTagResourceGroupsOutput]'
    }

    attribute_map = {
        'next_token': 'NextToken',
        'resource_tags': 'ResourceTags'
    }

    def __init__(self, next_token=None, resource_tags=None, _configuration=None):  # noqa: E501
        """DTSOpenListTagResourceGroupsResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._next_token = None
        self._resource_tags = None
        self.discriminator = None

        if next_token is not None:
            self.next_token = next_token
        if resource_tags is not None:
            self.resource_tags = resource_tags

    @property
    def next_token(self):
        """Gets the next_token of this DTSOpenListTagResourceGroupsResponse.  # noqa: E501


        :return: The next_token of this DTSOpenListTagResourceGroupsResponse.  # noqa: E501
        :rtype: str
        """
        return self._next_token

    @next_token.setter
    def next_token(self, next_token):
        """Sets the next_token of this DTSOpenListTagResourceGroupsResponse.


        :param next_token: The next_token of this DTSOpenListTagResourceGroupsResponse.  # noqa: E501
        :type: str
        """

        self._next_token = next_token

    @property
    def resource_tags(self):
        """Gets the resource_tags of this DTSOpenListTagResourceGroupsResponse.  # noqa: E501


        :return: The resource_tags of this DTSOpenListTagResourceGroupsResponse.  # noqa: E501
        :rtype: list[ResourceTagForDTSOpenListTagResourceGroupsOutput]
        """
        return self._resource_tags

    @resource_tags.setter
    def resource_tags(self, resource_tags):
        """Sets the resource_tags of this DTSOpenListTagResourceGroupsResponse.


        :param resource_tags: The resource_tags of this DTSOpenListTagResourceGroupsResponse.  # noqa: E501
        :type: list[ResourceTagForDTSOpenListTagResourceGroupsOutput]
        """

        self._resource_tags = resource_tags

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
        if issubclass(DTSOpenListTagResourceGroupsResponse, dict):
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
        if not isinstance(other, DTSOpenListTagResourceGroupsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DTSOpenListTagResourceGroupsResponse):
            return True

        return self.to_dict() != other.to_dict()
