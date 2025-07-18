# coding: utf-8

"""
    livesaas20230801

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class UnsubscribeHostAcceleratePackOrderResponse(object):
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
        'td_result': 'list[TDResultForUnsubscribeHostAcceleratePackOrderOutput]'
    }

    attribute_map = {
        'td_result': 'TDResult'
    }

    def __init__(self, td_result=None, _configuration=None):  # noqa: E501
        """UnsubscribeHostAcceleratePackOrderResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._td_result = None
        self.discriminator = None

        if td_result is not None:
            self.td_result = td_result

    @property
    def td_result(self):
        """Gets the td_result of this UnsubscribeHostAcceleratePackOrderResponse.  # noqa: E501


        :return: The td_result of this UnsubscribeHostAcceleratePackOrderResponse.  # noqa: E501
        :rtype: list[TDResultForUnsubscribeHostAcceleratePackOrderOutput]
        """
        return self._td_result

    @td_result.setter
    def td_result(self, td_result):
        """Sets the td_result of this UnsubscribeHostAcceleratePackOrderResponse.


        :param td_result: The td_result of this UnsubscribeHostAcceleratePackOrderResponse.  # noqa: E501
        :type: list[TDResultForUnsubscribeHostAcceleratePackOrderOutput]
        """

        self._td_result = td_result

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
        if issubclass(UnsubscribeHostAcceleratePackOrderResponse, dict):
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
        if not isinstance(other, UnsubscribeHostAcceleratePackOrderResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UnsubscribeHostAcceleratePackOrderResponse):
            return True

        return self.to_dict() != other.to_dict()
