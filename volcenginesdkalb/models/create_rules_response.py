# coding: utf-8

"""
    alb

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class CreateRulesResponse(object):
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
        'request_id': 'str',
        'rule_ids': 'list[str]'
    }

    attribute_map = {
        'request_id': 'RequestId',
        'rule_ids': 'RuleIds'
    }

    def __init__(self, request_id=None, rule_ids=None, _configuration=None):  # noqa: E501
        """CreateRulesResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._request_id = None
        self._rule_ids = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if rule_ids is not None:
            self.rule_ids = rule_ids

    @property
    def request_id(self):
        """Gets the request_id of this CreateRulesResponse.  # noqa: E501


        :return: The request_id of this CreateRulesResponse.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this CreateRulesResponse.


        :param request_id: The request_id of this CreateRulesResponse.  # noqa: E501
        :type: str
        """

        self._request_id = request_id

    @property
    def rule_ids(self):
        """Gets the rule_ids of this CreateRulesResponse.  # noqa: E501


        :return: The rule_ids of this CreateRulesResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._rule_ids

    @rule_ids.setter
    def rule_ids(self, rule_ids):
        """Sets the rule_ids of this CreateRulesResponse.


        :param rule_ids: The rule_ids of this CreateRulesResponse.  # noqa: E501
        :type: list[str]
        """

        self._rule_ids = rule_ids

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
        if issubclass(CreateRulesResponse, dict):
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
        if not isinstance(other, CreateRulesResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateRulesResponse):
            return True

        return self.to_dict() != other.to_dict()
