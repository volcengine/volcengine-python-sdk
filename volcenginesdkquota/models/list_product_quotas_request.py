# coding: utf-8

"""
    quota

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ListProductQuotasRequest(object):
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
        'dimensions': 'list[DimensionForListProductQuotasInput]',
        'max_results': 'int',
        'next_token': 'str',
        'provider_code': 'str',
        'quota_code': 'str',
        'quota_type': 'str',
        'sort_order': 'str'
    }

    attribute_map = {
        'dimensions': 'Dimensions',
        'max_results': 'MaxResults',
        'next_token': 'NextToken',
        'provider_code': 'ProviderCode',
        'quota_code': 'QuotaCode',
        'quota_type': 'QuotaType',
        'sort_order': 'SortOrder'
    }

    def __init__(self, dimensions=None, max_results=None, next_token=None, provider_code=None, quota_code=None, quota_type=None, sort_order=None, _configuration=None):  # noqa: E501
        """ListProductQuotasRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._dimensions = None
        self._max_results = None
        self._next_token = None
        self._provider_code = None
        self._quota_code = None
        self._quota_type = None
        self._sort_order = None
        self.discriminator = None

        if dimensions is not None:
            self.dimensions = dimensions
        if max_results is not None:
            self.max_results = max_results
        if next_token is not None:
            self.next_token = next_token
        self.provider_code = provider_code
        if quota_code is not None:
            self.quota_code = quota_code
        if quota_type is not None:
            self.quota_type = quota_type
        if sort_order is not None:
            self.sort_order = sort_order

    @property
    def dimensions(self):
        """Gets the dimensions of this ListProductQuotasRequest.  # noqa: E501


        :return: The dimensions of this ListProductQuotasRequest.  # noqa: E501
        :rtype: list[DimensionForListProductQuotasInput]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """Sets the dimensions of this ListProductQuotasRequest.


        :param dimensions: The dimensions of this ListProductQuotasRequest.  # noqa: E501
        :type: list[DimensionForListProductQuotasInput]
        """

        self._dimensions = dimensions

    @property
    def max_results(self):
        """Gets the max_results of this ListProductQuotasRequest.  # noqa: E501


        :return: The max_results of this ListProductQuotasRequest.  # noqa: E501
        :rtype: int
        """
        return self._max_results

    @max_results.setter
    def max_results(self, max_results):
        """Sets the max_results of this ListProductQuotasRequest.


        :param max_results: The max_results of this ListProductQuotasRequest.  # noqa: E501
        :type: int
        """

        self._max_results = max_results

    @property
    def next_token(self):
        """Gets the next_token of this ListProductQuotasRequest.  # noqa: E501


        :return: The next_token of this ListProductQuotasRequest.  # noqa: E501
        :rtype: str
        """
        return self._next_token

    @next_token.setter
    def next_token(self, next_token):
        """Sets the next_token of this ListProductQuotasRequest.


        :param next_token: The next_token of this ListProductQuotasRequest.  # noqa: E501
        :type: str
        """

        self._next_token = next_token

    @property
    def provider_code(self):
        """Gets the provider_code of this ListProductQuotasRequest.  # noqa: E501


        :return: The provider_code of this ListProductQuotasRequest.  # noqa: E501
        :rtype: str
        """
        return self._provider_code

    @provider_code.setter
    def provider_code(self, provider_code):
        """Sets the provider_code of this ListProductQuotasRequest.


        :param provider_code: The provider_code of this ListProductQuotasRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and provider_code is None:
            raise ValueError("Invalid value for `provider_code`, must not be `None`")  # noqa: E501

        self._provider_code = provider_code

    @property
    def quota_code(self):
        """Gets the quota_code of this ListProductQuotasRequest.  # noqa: E501


        :return: The quota_code of this ListProductQuotasRequest.  # noqa: E501
        :rtype: str
        """
        return self._quota_code

    @quota_code.setter
    def quota_code(self, quota_code):
        """Sets the quota_code of this ListProductQuotasRequest.


        :param quota_code: The quota_code of this ListProductQuotasRequest.  # noqa: E501
        :type: str
        """

        self._quota_code = quota_code

    @property
    def quota_type(self):
        """Gets the quota_type of this ListProductQuotasRequest.  # noqa: E501


        :return: The quota_type of this ListProductQuotasRequest.  # noqa: E501
        :rtype: str
        """
        return self._quota_type

    @quota_type.setter
    def quota_type(self, quota_type):
        """Sets the quota_type of this ListProductQuotasRequest.


        :param quota_type: The quota_type of this ListProductQuotasRequest.  # noqa: E501
        :type: str
        """

        self._quota_type = quota_type

    @property
    def sort_order(self):
        """Gets the sort_order of this ListProductQuotasRequest.  # noqa: E501


        :return: The sort_order of this ListProductQuotasRequest.  # noqa: E501
        :rtype: str
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this ListProductQuotasRequest.


        :param sort_order: The sort_order of this ListProductQuotasRequest.  # noqa: E501
        :type: str
        """

        self._sort_order = sort_order

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
        if issubclass(ListProductQuotasRequest, dict):
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
        if not isinstance(other, ListProductQuotasRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListProductQuotasRequest):
            return True

        return self.to_dict() != other.to_dict()
