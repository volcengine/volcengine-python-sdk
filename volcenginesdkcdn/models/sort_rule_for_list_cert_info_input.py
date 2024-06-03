# coding: utf-8

"""
    cdn

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class SortRuleForListCertInfoInput(object):
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
        'asc': 'bool',
        'order_by': 'str'
    }

    attribute_map = {
        'asc': 'Asc',
        'order_by': 'OrderBy'
    }

    def __init__(self, asc=None, order_by=None, _configuration=None):  # noqa: E501
        """SortRuleForListCertInfoInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._asc = None
        self._order_by = None
        self.discriminator = None

        if asc is not None:
            self.asc = asc
        if order_by is not None:
            self.order_by = order_by

    @property
    def asc(self):
        """Gets the asc of this SortRuleForListCertInfoInput.  # noqa: E501


        :return: The asc of this SortRuleForListCertInfoInput.  # noqa: E501
        :rtype: bool
        """
        return self._asc

    @asc.setter
    def asc(self, asc):
        """Sets the asc of this SortRuleForListCertInfoInput.


        :param asc: The asc of this SortRuleForListCertInfoInput.  # noqa: E501
        :type: bool
        """

        self._asc = asc

    @property
    def order_by(self):
        """Gets the order_by of this SortRuleForListCertInfoInput.  # noqa: E501


        :return: The order_by of this SortRuleForListCertInfoInput.  # noqa: E501
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        """Sets the order_by of this SortRuleForListCertInfoInput.


        :param order_by: The order_by of this SortRuleForListCertInfoInput.  # noqa: E501
        :type: str
        """

        self._order_by = order_by

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
        if issubclass(SortRuleForListCertInfoInput, dict):
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
        if not isinstance(other, SortRuleForListCertInfoInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SortRuleForListCertInfoInput):
            return True

        return self.to_dict() != other.to_dict()