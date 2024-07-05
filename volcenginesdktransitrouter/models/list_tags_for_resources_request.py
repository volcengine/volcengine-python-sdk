# coding: utf-8

"""
    transitrouter

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ListTagsForResourcesRequest(object):
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
        'max_results': 'int',
        'next_token': 'str',
        'resource_ids': 'list[str]',
        'resource_type': 'str',
        'tag_filters': 'list[TagFilterForListTagsForResourcesInput]',
        'tag_type': 'str'
    }

    attribute_map = {
        'max_results': 'MaxResults',
        'next_token': 'NextToken',
        'resource_ids': 'ResourceIds',
        'resource_type': 'ResourceType',
        'tag_filters': 'TagFilters',
        'tag_type': 'TagType'
    }

    def __init__(self, max_results=None, next_token=None, resource_ids=None, resource_type=None, tag_filters=None, tag_type=None, _configuration=None):  # noqa: E501
        """ListTagsForResourcesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._max_results = None
        self._next_token = None
        self._resource_ids = None
        self._resource_type = None
        self._tag_filters = None
        self._tag_type = None
        self.discriminator = None

        if max_results is not None:
            self.max_results = max_results
        if next_token is not None:
            self.next_token = next_token
        if resource_ids is not None:
            self.resource_ids = resource_ids
        self.resource_type = resource_type
        if tag_filters is not None:
            self.tag_filters = tag_filters
        if tag_type is not None:
            self.tag_type = tag_type

    @property
    def max_results(self):
        """Gets the max_results of this ListTagsForResourcesRequest.  # noqa: E501


        :return: The max_results of this ListTagsForResourcesRequest.  # noqa: E501
        :rtype: int
        """
        return self._max_results

    @max_results.setter
    def max_results(self, max_results):
        """Sets the max_results of this ListTagsForResourcesRequest.


        :param max_results: The max_results of this ListTagsForResourcesRequest.  # noqa: E501
        :type: int
        """

        self._max_results = max_results

    @property
    def next_token(self):
        """Gets the next_token of this ListTagsForResourcesRequest.  # noqa: E501


        :return: The next_token of this ListTagsForResourcesRequest.  # noqa: E501
        :rtype: str
        """
        return self._next_token

    @next_token.setter
    def next_token(self, next_token):
        """Sets the next_token of this ListTagsForResourcesRequest.


        :param next_token: The next_token of this ListTagsForResourcesRequest.  # noqa: E501
        :type: str
        """

        self._next_token = next_token

    @property
    def resource_ids(self):
        """Gets the resource_ids of this ListTagsForResourcesRequest.  # noqa: E501


        :return: The resource_ids of this ListTagsForResourcesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._resource_ids

    @resource_ids.setter
    def resource_ids(self, resource_ids):
        """Sets the resource_ids of this ListTagsForResourcesRequest.


        :param resource_ids: The resource_ids of this ListTagsForResourcesRequest.  # noqa: E501
        :type: list[str]
        """

        self._resource_ids = resource_ids

    @property
    def resource_type(self):
        """Gets the resource_type of this ListTagsForResourcesRequest.  # noqa: E501


        :return: The resource_type of this ListTagsForResourcesRequest.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ListTagsForResourcesRequest.


        :param resource_type: The resource_type of this ListTagsForResourcesRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and resource_type is None:
            raise ValueError("Invalid value for `resource_type`, must not be `None`")  # noqa: E501

        self._resource_type = resource_type

    @property
    def tag_filters(self):
        """Gets the tag_filters of this ListTagsForResourcesRequest.  # noqa: E501


        :return: The tag_filters of this ListTagsForResourcesRequest.  # noqa: E501
        :rtype: list[TagFilterForListTagsForResourcesInput]
        """
        return self._tag_filters

    @tag_filters.setter
    def tag_filters(self, tag_filters):
        """Sets the tag_filters of this ListTagsForResourcesRequest.


        :param tag_filters: The tag_filters of this ListTagsForResourcesRequest.  # noqa: E501
        :type: list[TagFilterForListTagsForResourcesInput]
        """

        self._tag_filters = tag_filters

    @property
    def tag_type(self):
        """Gets the tag_type of this ListTagsForResourcesRequest.  # noqa: E501


        :return: The tag_type of this ListTagsForResourcesRequest.  # noqa: E501
        :rtype: str
        """
        return self._tag_type

    @tag_type.setter
    def tag_type(self, tag_type):
        """Sets the tag_type of this ListTagsForResourcesRequest.


        :param tag_type: The tag_type of this ListTagsForResourcesRequest.  # noqa: E501
        :type: str
        """

        self._tag_type = tag_type

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
        if issubclass(ListTagsForResourcesRequest, dict):
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
        if not isinstance(other, ListTagsForResourcesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListTagsForResourcesRequest):
            return True

        return self.to_dict() != other.to_dict()
