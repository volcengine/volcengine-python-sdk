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


class QueryPriceForRenewRequest(object):
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
        'instance_id_list': 'list[str]',
        'product': 'str',
        'use_duration': 'int'
    }

    attribute_map = {
        'instance_id_list': 'InstanceIDList',
        'product': 'Product',
        'use_duration': 'UseDuration'
    }

    def __init__(self, instance_id_list=None, product=None, use_duration=None, _configuration=None):  # noqa: E501
        """QueryPriceForRenewRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._instance_id_list = None
        self._product = None
        self._use_duration = None
        self.discriminator = None

        if instance_id_list is not None:
            self.instance_id_list = instance_id_list
        self.product = product
        self.use_duration = use_duration

    @property
    def instance_id_list(self):
        """Gets the instance_id_list of this QueryPriceForRenewRequest.  # noqa: E501


        :return: The instance_id_list of this QueryPriceForRenewRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._instance_id_list

    @instance_id_list.setter
    def instance_id_list(self, instance_id_list):
        """Sets the instance_id_list of this QueryPriceForRenewRequest.


        :param instance_id_list: The instance_id_list of this QueryPriceForRenewRequest.  # noqa: E501
        :type: list[str]
        """

        self._instance_id_list = instance_id_list

    @property
    def product(self):
        """Gets the product of this QueryPriceForRenewRequest.  # noqa: E501


        :return: The product of this QueryPriceForRenewRequest.  # noqa: E501
        :rtype: str
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this QueryPriceForRenewRequest.


        :param product: The product of this QueryPriceForRenewRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and product is None:
            raise ValueError("Invalid value for `product`, must not be `None`")  # noqa: E501

        self._product = product

    @property
    def use_duration(self):
        """Gets the use_duration of this QueryPriceForRenewRequest.  # noqa: E501


        :return: The use_duration of this QueryPriceForRenewRequest.  # noqa: E501
        :rtype: int
        """
        return self._use_duration

    @use_duration.setter
    def use_duration(self, use_duration):
        """Sets the use_duration of this QueryPriceForRenewRequest.


        :param use_duration: The use_duration of this QueryPriceForRenewRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and use_duration is None:
            raise ValueError("Invalid value for `use_duration`, must not be `None`")  # noqa: E501

        self._use_duration = use_duration

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
        if issubclass(QueryPriceForRenewRequest, dict):
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
        if not isinstance(other, QueryPriceForRenewRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QueryPriceForRenewRequest):
            return True

        return self.to_dict() != other.to_dict()
