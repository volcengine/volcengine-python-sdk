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


class GetResourcesRequest(object):
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
        'resource_trn_list': 'list[str]',
        'resource_type_filters': 'list[str]',
        'tag_filters': 'list[TagFilterForGetResourcesInput]'
    }

    attribute_map = {
        'max_results': 'MaxResults',
        'next_token': 'NextToken',
        'resource_trn_list': 'ResourceTrnList',
        'resource_type_filters': 'ResourceTypeFilters',
        'tag_filters': 'TagFilters'
    }

    def __init__(self, max_results=None, next_token=None, resource_trn_list=None, resource_type_filters=None, tag_filters=None, _configuration=None):  # noqa: E501
        """GetResourcesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._max_results = None
        self._next_token = None
        self._resource_trn_list = None
        self._resource_type_filters = None
        self._tag_filters = None
        self.discriminator = None

        if max_results is not None:
            self.max_results = max_results
        if next_token is not None:
            self.next_token = next_token
        if resource_trn_list is not None:
            self.resource_trn_list = resource_trn_list
        if resource_type_filters is not None:
            self.resource_type_filters = resource_type_filters
        if tag_filters is not None:
            self.tag_filters = tag_filters

    @property
    def max_results(self):
        """Gets the max_results of this GetResourcesRequest.  # noqa: E501


        :return: The max_results of this GetResourcesRequest.  # noqa: E501
        :rtype: int
        """
        return self._max_results

    @max_results.setter
    def max_results(self, max_results):
        """Sets the max_results of this GetResourcesRequest.


        :param max_results: The max_results of this GetResourcesRequest.  # noqa: E501
        :type: int
        """

        self._max_results = max_results

    @property
    def next_token(self):
        """Gets the next_token of this GetResourcesRequest.  # noqa: E501


        :return: The next_token of this GetResourcesRequest.  # noqa: E501
        :rtype: str
        """
        return self._next_token

    @next_token.setter
    def next_token(self, next_token):
        """Sets the next_token of this GetResourcesRequest.


        :param next_token: The next_token of this GetResourcesRequest.  # noqa: E501
        :type: str
        """

        self._next_token = next_token

    @property
    def resource_trn_list(self):
        """Gets the resource_trn_list of this GetResourcesRequest.  # noqa: E501


        :return: The resource_trn_list of this GetResourcesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._resource_trn_list

    @resource_trn_list.setter
    def resource_trn_list(self, resource_trn_list):
        """Sets the resource_trn_list of this GetResourcesRequest.


        :param resource_trn_list: The resource_trn_list of this GetResourcesRequest.  # noqa: E501
        :type: list[str]
        """

        self._resource_trn_list = resource_trn_list

    @property
    def resource_type_filters(self):
        """Gets the resource_type_filters of this GetResourcesRequest.  # noqa: E501


        :return: The resource_type_filters of this GetResourcesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._resource_type_filters

    @resource_type_filters.setter
    def resource_type_filters(self, resource_type_filters):
        """Sets the resource_type_filters of this GetResourcesRequest.


        :param resource_type_filters: The resource_type_filters of this GetResourcesRequest.  # noqa: E501
        :type: list[str]
        """

        self._resource_type_filters = resource_type_filters

    @property
    def tag_filters(self):
        """Gets the tag_filters of this GetResourcesRequest.  # noqa: E501


        :return: The tag_filters of this GetResourcesRequest.  # noqa: E501
        :rtype: list[TagFilterForGetResourcesInput]
        """
        return self._tag_filters

    @tag_filters.setter
    def tag_filters(self, tag_filters):
        """Sets the tag_filters of this GetResourcesRequest.


        :param tag_filters: The tag_filters of this GetResourcesRequest.  # noqa: E501
        :type: list[TagFilterForGetResourcesInput]
        """

        self._tag_filters = tag_filters

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
        if issubclass(GetResourcesRequest, dict):
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
        if not isinstance(other, GetResourcesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetResourcesRequest):
            return True

        return self.to_dict() != other.to_dict()
