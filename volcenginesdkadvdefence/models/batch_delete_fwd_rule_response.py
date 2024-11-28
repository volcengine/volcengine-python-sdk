# coding: utf-8

"""
    advdefence

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class BatchDeleteFwdRuleResponse(object):
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
        'ret': 'list[RetForBatchDeleteFwdRuleOutput]'
    }

    attribute_map = {
        'ret': 'Ret'
    }

    def __init__(self, ret=None, _configuration=None):  # noqa: E501
        """BatchDeleteFwdRuleResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._ret = None
        self.discriminator = None

        if ret is not None:
            self.ret = ret

    @property
    def ret(self):
        """Gets the ret of this BatchDeleteFwdRuleResponse.  # noqa: E501


        :return: The ret of this BatchDeleteFwdRuleResponse.  # noqa: E501
        :rtype: list[RetForBatchDeleteFwdRuleOutput]
        """
        return self._ret

    @ret.setter
    def ret(self, ret):
        """Sets the ret of this BatchDeleteFwdRuleResponse.


        :param ret: The ret of this BatchDeleteFwdRuleResponse.  # noqa: E501
        :type: list[RetForBatchDeleteFwdRuleOutput]
        """

        self._ret = ret

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
        if issubclass(BatchDeleteFwdRuleResponse, dict):
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
        if not isinstance(other, BatchDeleteFwdRuleResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BatchDeleteFwdRuleResponse):
            return True

        return self.to_dict() != other.to_dict()
