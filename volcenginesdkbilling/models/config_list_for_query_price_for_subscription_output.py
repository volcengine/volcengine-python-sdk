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


class ConfigListForQueryPriceForSubscriptionOutput(object):
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
        'charge_item_code': 'str',
        'configuration_code': 'str',
        'discount_amount': 'str',
        'discount_detail': 'DiscountDetailForQueryPriceForSubscriptionOutput',
        'original_amount': 'str',
        'price': 'str',
        'quantity': 'int'
    }

    attribute_map = {
        'charge_item_code': 'ChargeItemCode',
        'configuration_code': 'ConfigurationCode',
        'discount_amount': 'DiscountAmount',
        'discount_detail': 'DiscountDetail',
        'original_amount': 'OriginalAmount',
        'price': 'Price',
        'quantity': 'Quantity'
    }

    def __init__(self, charge_item_code=None, configuration_code=None, discount_amount=None, discount_detail=None, original_amount=None, price=None, quantity=None, _configuration=None):  # noqa: E501
        """ConfigListForQueryPriceForSubscriptionOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._charge_item_code = None
        self._configuration_code = None
        self._discount_amount = None
        self._discount_detail = None
        self._original_amount = None
        self._price = None
        self._quantity = None
        self.discriminator = None

        if charge_item_code is not None:
            self.charge_item_code = charge_item_code
        if configuration_code is not None:
            self.configuration_code = configuration_code
        if discount_amount is not None:
            self.discount_amount = discount_amount
        if discount_detail is not None:
            self.discount_detail = discount_detail
        if original_amount is not None:
            self.original_amount = original_amount
        if price is not None:
            self.price = price
        if quantity is not None:
            self.quantity = quantity

    @property
    def charge_item_code(self):
        """Gets the charge_item_code of this ConfigListForQueryPriceForSubscriptionOutput.  # noqa: E501


        :return: The charge_item_code of this ConfigListForQueryPriceForSubscriptionOutput.  # noqa: E501
        :rtype: str
        """
        return self._charge_item_code

    @charge_item_code.setter
    def charge_item_code(self, charge_item_code):
        """Sets the charge_item_code of this ConfigListForQueryPriceForSubscriptionOutput.


        :param charge_item_code: The charge_item_code of this ConfigListForQueryPriceForSubscriptionOutput.  # noqa: E501
        :type: str
        """

        self._charge_item_code = charge_item_code

    @property
    def configuration_code(self):
        """Gets the configuration_code of this ConfigListForQueryPriceForSubscriptionOutput.  # noqa: E501


        :return: The configuration_code of this ConfigListForQueryPriceForSubscriptionOutput.  # noqa: E501
        :rtype: str
        """
        return self._configuration_code

    @configuration_code.setter
    def configuration_code(self, configuration_code):
        """Sets the configuration_code of this ConfigListForQueryPriceForSubscriptionOutput.


        :param configuration_code: The configuration_code of this ConfigListForQueryPriceForSubscriptionOutput.  # noqa: E501
        :type: str
        """

        self._configuration_code = configuration_code

    @property
    def discount_amount(self):
        """Gets the discount_amount of this ConfigListForQueryPriceForSubscriptionOutput.  # noqa: E501


        :return: The discount_amount of this ConfigListForQueryPriceForSubscriptionOutput.  # noqa: E501
        :rtype: str
        """
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        """Sets the discount_amount of this ConfigListForQueryPriceForSubscriptionOutput.


        :param discount_amount: The discount_amount of this ConfigListForQueryPriceForSubscriptionOutput.  # noqa: E501
        :type: str
        """

        self._discount_amount = discount_amount

    @property
    def discount_detail(self):
        """Gets the discount_detail of this ConfigListForQueryPriceForSubscriptionOutput.  # noqa: E501


        :return: The discount_detail of this ConfigListForQueryPriceForSubscriptionOutput.  # noqa: E501
        :rtype: DiscountDetailForQueryPriceForSubscriptionOutput
        """
        return self._discount_detail

    @discount_detail.setter
    def discount_detail(self, discount_detail):
        """Sets the discount_detail of this ConfigListForQueryPriceForSubscriptionOutput.


        :param discount_detail: The discount_detail of this ConfigListForQueryPriceForSubscriptionOutput.  # noqa: E501
        :type: DiscountDetailForQueryPriceForSubscriptionOutput
        """

        self._discount_detail = discount_detail

    @property
    def original_amount(self):
        """Gets the original_amount of this ConfigListForQueryPriceForSubscriptionOutput.  # noqa: E501


        :return: The original_amount of this ConfigListForQueryPriceForSubscriptionOutput.  # noqa: E501
        :rtype: str
        """
        return self._original_amount

    @original_amount.setter
    def original_amount(self, original_amount):
        """Sets the original_amount of this ConfigListForQueryPriceForSubscriptionOutput.


        :param original_amount: The original_amount of this ConfigListForQueryPriceForSubscriptionOutput.  # noqa: E501
        :type: str
        """

        self._original_amount = original_amount

    @property
    def price(self):
        """Gets the price of this ConfigListForQueryPriceForSubscriptionOutput.  # noqa: E501


        :return: The price of this ConfigListForQueryPriceForSubscriptionOutput.  # noqa: E501
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this ConfigListForQueryPriceForSubscriptionOutput.


        :param price: The price of this ConfigListForQueryPriceForSubscriptionOutput.  # noqa: E501
        :type: str
        """

        self._price = price

    @property
    def quantity(self):
        """Gets the quantity of this ConfigListForQueryPriceForSubscriptionOutput.  # noqa: E501


        :return: The quantity of this ConfigListForQueryPriceForSubscriptionOutput.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this ConfigListForQueryPriceForSubscriptionOutput.


        :param quantity: The quantity of this ConfigListForQueryPriceForSubscriptionOutput.  # noqa: E501
        :type: int
        """

        self._quantity = quantity

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
        if issubclass(ConfigListForQueryPriceForSubscriptionOutput, dict):
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
        if not isinstance(other, ConfigListForQueryPriceForSubscriptionOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConfigListForQueryPriceForSubscriptionOutput):
            return True

        return self.to_dict() != other.to_dict()
