# coding: utf-8

"""
    resource_share

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeResourceSharesResponse(object):
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
        'resource_shares': 'list[ResourceShareForDescribeResourceSharesOutput]'
    }

    attribute_map = {
        'next_token': 'NextToken',
        'resource_shares': 'ResourceShares'
    }

    def __init__(self, next_token=None, resource_shares=None, _configuration=None):  # noqa: E501
        """DescribeResourceSharesResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._next_token = None
        self._resource_shares = None
        self.discriminator = None

        if next_token is not None:
            self.next_token = next_token
        if resource_shares is not None:
            self.resource_shares = resource_shares

    @property
    def next_token(self):
        """Gets the next_token of this DescribeResourceSharesResponse.  # noqa: E501


        :return: The next_token of this DescribeResourceSharesResponse.  # noqa: E501
        :rtype: str
        """
        return self._next_token

    @next_token.setter
    def next_token(self, next_token):
        """Sets the next_token of this DescribeResourceSharesResponse.


        :param next_token: The next_token of this DescribeResourceSharesResponse.  # noqa: E501
        :type: str
        """

        self._next_token = next_token

    @property
    def resource_shares(self):
        """Gets the resource_shares of this DescribeResourceSharesResponse.  # noqa: E501


        :return: The resource_shares of this DescribeResourceSharesResponse.  # noqa: E501
        :rtype: list[ResourceShareForDescribeResourceSharesOutput]
        """
        return self._resource_shares

    @resource_shares.setter
    def resource_shares(self, resource_shares):
        """Sets the resource_shares of this DescribeResourceSharesResponse.


        :param resource_shares: The resource_shares of this DescribeResourceSharesResponse.  # noqa: E501
        :type: list[ResourceShareForDescribeResourceSharesOutput]
        """

        self._resource_shares = resource_shares

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
        if issubclass(DescribeResourceSharesResponse, dict):
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
        if not isinstance(other, DescribeResourceSharesResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeResourceSharesResponse):
            return True

        return self.to_dict() != other.to_dict()
