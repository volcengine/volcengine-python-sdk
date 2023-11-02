# coding: utf-8

"""
    rds_mysql_v2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ChargeItemPriceForDescribeDBInstancePriceDifferenceOutput(object):
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
        'charge_item_key': 'str',
        'charge_item_type': 'str',
        'charge_item_value': 'int',
        'discount_price': 'float',
        'original_price': 'float',
        'payable_price': 'float'
    }

    attribute_map = {
        'charge_item_key': 'ChargeItemKey',
        'charge_item_type': 'ChargeItemType',
        'charge_item_value': 'ChargeItemValue',
        'discount_price': 'DiscountPrice',
        'original_price': 'OriginalPrice',
        'payable_price': 'PayablePrice'
    }

    def __init__(self, charge_item_key=None, charge_item_type=None, charge_item_value=None, discount_price=None, original_price=None, payable_price=None, _configuration=None):  # noqa: E501
        """ChargeItemPriceForDescribeDBInstancePriceDifferenceOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._charge_item_key = None
        self._charge_item_type = None
        self._charge_item_value = None
        self._discount_price = None
        self._original_price = None
        self._payable_price = None
        self.discriminator = None

        if charge_item_key is not None:
            self.charge_item_key = charge_item_key
        if charge_item_type is not None:
            self.charge_item_type = charge_item_type
        if charge_item_value is not None:
            self.charge_item_value = charge_item_value
        if discount_price is not None:
            self.discount_price = discount_price
        if original_price is not None:
            self.original_price = original_price
        if payable_price is not None:
            self.payable_price = payable_price

    @property
    def charge_item_key(self):
        """Gets the charge_item_key of this ChargeItemPriceForDescribeDBInstancePriceDifferenceOutput.  # noqa: E501


        :return: The charge_item_key of this ChargeItemPriceForDescribeDBInstancePriceDifferenceOutput.  # noqa: E501
        :rtype: str
        """
        return self._charge_item_key

    @charge_item_key.setter
    def charge_item_key(self, charge_item_key):
        """Sets the charge_item_key of this ChargeItemPriceForDescribeDBInstancePriceDifferenceOutput.


        :param charge_item_key: The charge_item_key of this ChargeItemPriceForDescribeDBInstancePriceDifferenceOutput.  # noqa: E501
        :type: str
        """

        self._charge_item_key = charge_item_key

    @property
    def charge_item_type(self):
        """Gets the charge_item_type of this ChargeItemPriceForDescribeDBInstancePriceDifferenceOutput.  # noqa: E501


        :return: The charge_item_type of this ChargeItemPriceForDescribeDBInstancePriceDifferenceOutput.  # noqa: E501
        :rtype: str
        """
        return self._charge_item_type

    @charge_item_type.setter
    def charge_item_type(self, charge_item_type):
        """Sets the charge_item_type of this ChargeItemPriceForDescribeDBInstancePriceDifferenceOutput.


        :param charge_item_type: The charge_item_type of this ChargeItemPriceForDescribeDBInstancePriceDifferenceOutput.  # noqa: E501
        :type: str
        """

        self._charge_item_type = charge_item_type

    @property
    def charge_item_value(self):
        """Gets the charge_item_value of this ChargeItemPriceForDescribeDBInstancePriceDifferenceOutput.  # noqa: E501


        :return: The charge_item_value of this ChargeItemPriceForDescribeDBInstancePriceDifferenceOutput.  # noqa: E501
        :rtype: int
        """
        return self._charge_item_value

    @charge_item_value.setter
    def charge_item_value(self, charge_item_value):
        """Sets the charge_item_value of this ChargeItemPriceForDescribeDBInstancePriceDifferenceOutput.


        :param charge_item_value: The charge_item_value of this ChargeItemPriceForDescribeDBInstancePriceDifferenceOutput.  # noqa: E501
        :type: int
        """

        self._charge_item_value = charge_item_value

    @property
    def discount_price(self):
        """Gets the discount_price of this ChargeItemPriceForDescribeDBInstancePriceDifferenceOutput.  # noqa: E501


        :return: The discount_price of this ChargeItemPriceForDescribeDBInstancePriceDifferenceOutput.  # noqa: E501
        :rtype: float
        """
        return self._discount_price

    @discount_price.setter
    def discount_price(self, discount_price):
        """Sets the discount_price of this ChargeItemPriceForDescribeDBInstancePriceDifferenceOutput.


        :param discount_price: The discount_price of this ChargeItemPriceForDescribeDBInstancePriceDifferenceOutput.  # noqa: E501
        :type: float
        """

        self._discount_price = discount_price

    @property
    def original_price(self):
        """Gets the original_price of this ChargeItemPriceForDescribeDBInstancePriceDifferenceOutput.  # noqa: E501


        :return: The original_price of this ChargeItemPriceForDescribeDBInstancePriceDifferenceOutput.  # noqa: E501
        :rtype: float
        """
        return self._original_price

    @original_price.setter
    def original_price(self, original_price):
        """Sets the original_price of this ChargeItemPriceForDescribeDBInstancePriceDifferenceOutput.


        :param original_price: The original_price of this ChargeItemPriceForDescribeDBInstancePriceDifferenceOutput.  # noqa: E501
        :type: float
        """

        self._original_price = original_price

    @property
    def payable_price(self):
        """Gets the payable_price of this ChargeItemPriceForDescribeDBInstancePriceDifferenceOutput.  # noqa: E501


        :return: The payable_price of this ChargeItemPriceForDescribeDBInstancePriceDifferenceOutput.  # noqa: E501
        :rtype: float
        """
        return self._payable_price

    @payable_price.setter
    def payable_price(self, payable_price):
        """Sets the payable_price of this ChargeItemPriceForDescribeDBInstancePriceDifferenceOutput.


        :param payable_price: The payable_price of this ChargeItemPriceForDescribeDBInstancePriceDifferenceOutput.  # noqa: E501
        :type: float
        """

        self._payable_price = payable_price

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
        if issubclass(ChargeItemPriceForDescribeDBInstancePriceDifferenceOutput, dict):
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
        if not isinstance(other, ChargeItemPriceForDescribeDBInstancePriceDifferenceOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ChargeItemPriceForDescribeDBInstancePriceDifferenceOutput):
            return True

        return self.to_dict() != other.to_dict()
