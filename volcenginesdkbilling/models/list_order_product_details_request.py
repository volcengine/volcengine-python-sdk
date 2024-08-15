# coding: utf-8

"""
    billing

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ListOrderProductDetailsRequest(object):
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
        'order_id': 'str'
    }

    attribute_map = {
        'max_results': 'MaxResults',
        'next_token': 'NextToken',
        'order_id': 'OrderID'
    }

    def __init__(self, max_results=None, next_token=None, order_id=None, _configuration=None):  # noqa: E501
        """ListOrderProductDetailsRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._max_results = None
        self._next_token = None
        self._order_id = None
        self.discriminator = None

        self.max_results = max_results
        self.next_token = next_token
        self.order_id = order_id

    @property
    def max_results(self):
        """Gets the max_results of this ListOrderProductDetailsRequest.  # noqa: E501


        :return: The max_results of this ListOrderProductDetailsRequest.  # noqa: E501
        :rtype: int
        """
        return self._max_results

    @max_results.setter
    def max_results(self, max_results):
        """Sets the max_results of this ListOrderProductDetailsRequest.


        :param max_results: The max_results of this ListOrderProductDetailsRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and max_results is None:
            raise ValueError("Invalid value for `max_results`, must not be `None`")  # noqa: E501

        self._max_results = max_results

    @property
    def next_token(self):
        """Gets the next_token of this ListOrderProductDetailsRequest.  # noqa: E501


        :return: The next_token of this ListOrderProductDetailsRequest.  # noqa: E501
        :rtype: str
        """
        return self._next_token

    @next_token.setter
    def next_token(self, next_token):
        """Sets the next_token of this ListOrderProductDetailsRequest.


        :param next_token: The next_token of this ListOrderProductDetailsRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and next_token is None:
            raise ValueError("Invalid value for `next_token`, must not be `None`")  # noqa: E501

        self._next_token = next_token

    @property
    def order_id(self):
        """Gets the order_id of this ListOrderProductDetailsRequest.  # noqa: E501


        :return: The order_id of this ListOrderProductDetailsRequest.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this ListOrderProductDetailsRequest.


        :param order_id: The order_id of this ListOrderProductDetailsRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and order_id is None:
            raise ValueError("Invalid value for `order_id`, must not be `None`")  # noqa: E501

        self._order_id = order_id

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
        if issubclass(ListOrderProductDetailsRequest, dict):
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
        if not isinstance(other, ListOrderProductDetailsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListOrderProductDetailsRequest):
            return True

        return self.to_dict() != other.to_dict()
