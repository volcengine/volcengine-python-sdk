# coding: utf-8

"""
    tag

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class GetTagsResponse(object):
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
        'tags': 'list[TagForGetTagsOutput]'
    }

    attribute_map = {
        'next_token': 'NextToken',
        'tags': 'Tags'
    }

    def __init__(self, next_token=None, tags=None, _configuration=None):  # noqa: E501
        """GetTagsResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._next_token = None
        self._tags = None
        self.discriminator = None

        if next_token is not None:
            self.next_token = next_token
        if tags is not None:
            self.tags = tags

    @property
    def next_token(self):
        """Gets the next_token of this GetTagsResponse.  # noqa: E501


        :return: The next_token of this GetTagsResponse.  # noqa: E501
        :rtype: str
        """
        return self._next_token

    @next_token.setter
    def next_token(self, next_token):
        """Sets the next_token of this GetTagsResponse.


        :param next_token: The next_token of this GetTagsResponse.  # noqa: E501
        :type: str
        """

        self._next_token = next_token

    @property
    def tags(self):
        """Gets the tags of this GetTagsResponse.  # noqa: E501


        :return: The tags of this GetTagsResponse.  # noqa: E501
        :rtype: list[TagForGetTagsOutput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this GetTagsResponse.


        :param tags: The tags of this GetTagsResponse.  # noqa: E501
        :type: list[TagForGetTagsOutput]
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
        if issubclass(GetTagsResponse, dict):
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
        if not isinstance(other, GetTagsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetTagsResponse):
            return True

        return self.to_dict() != other.to_dict()
