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


class UrlAuthCustomActionForDescribeCdnConfigOutput(object):
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
        'exp_time_cap_rule': 'ExpTimeCapRuleForDescribeCdnConfigOutput',
        'param_cal_rules': 'list[str]',
        'sign_cap_rule': 'SignCapRuleForDescribeCdnConfigOutput',
        'sign_join_symbol': 'str',
        'sign_param': 'list[SignParamForDescribeCdnConfigOutput]'
    }

    attribute_map = {
        'exp_time_cap_rule': 'ExpTimeCapRule',
        'param_cal_rules': 'ParamCalRules',
        'sign_cap_rule': 'SignCapRule',
        'sign_join_symbol': 'SignJoinSymbol',
        'sign_param': 'SignParam'
    }

    def __init__(self, exp_time_cap_rule=None, param_cal_rules=None, sign_cap_rule=None, sign_join_symbol=None, sign_param=None, _configuration=None):  # noqa: E501
        """UrlAuthCustomActionForDescribeCdnConfigOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._exp_time_cap_rule = None
        self._param_cal_rules = None
        self._sign_cap_rule = None
        self._sign_join_symbol = None
        self._sign_param = None
        self.discriminator = None

        if exp_time_cap_rule is not None:
            self.exp_time_cap_rule = exp_time_cap_rule
        if param_cal_rules is not None:
            self.param_cal_rules = param_cal_rules
        if sign_cap_rule is not None:
            self.sign_cap_rule = sign_cap_rule
        if sign_join_symbol is not None:
            self.sign_join_symbol = sign_join_symbol
        if sign_param is not None:
            self.sign_param = sign_param

    @property
    def exp_time_cap_rule(self):
        """Gets the exp_time_cap_rule of this UrlAuthCustomActionForDescribeCdnConfigOutput.  # noqa: E501


        :return: The exp_time_cap_rule of this UrlAuthCustomActionForDescribeCdnConfigOutput.  # noqa: E501
        :rtype: ExpTimeCapRuleForDescribeCdnConfigOutput
        """
        return self._exp_time_cap_rule

    @exp_time_cap_rule.setter
    def exp_time_cap_rule(self, exp_time_cap_rule):
        """Sets the exp_time_cap_rule of this UrlAuthCustomActionForDescribeCdnConfigOutput.


        :param exp_time_cap_rule: The exp_time_cap_rule of this UrlAuthCustomActionForDescribeCdnConfigOutput.  # noqa: E501
        :type: ExpTimeCapRuleForDescribeCdnConfigOutput
        """

        self._exp_time_cap_rule = exp_time_cap_rule

    @property
    def param_cal_rules(self):
        """Gets the param_cal_rules of this UrlAuthCustomActionForDescribeCdnConfigOutput.  # noqa: E501


        :return: The param_cal_rules of this UrlAuthCustomActionForDescribeCdnConfigOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._param_cal_rules

    @param_cal_rules.setter
    def param_cal_rules(self, param_cal_rules):
        """Sets the param_cal_rules of this UrlAuthCustomActionForDescribeCdnConfigOutput.


        :param param_cal_rules: The param_cal_rules of this UrlAuthCustomActionForDescribeCdnConfigOutput.  # noqa: E501
        :type: list[str]
        """

        self._param_cal_rules = param_cal_rules

    @property
    def sign_cap_rule(self):
        """Gets the sign_cap_rule of this UrlAuthCustomActionForDescribeCdnConfigOutput.  # noqa: E501


        :return: The sign_cap_rule of this UrlAuthCustomActionForDescribeCdnConfigOutput.  # noqa: E501
        :rtype: SignCapRuleForDescribeCdnConfigOutput
        """
        return self._sign_cap_rule

    @sign_cap_rule.setter
    def sign_cap_rule(self, sign_cap_rule):
        """Sets the sign_cap_rule of this UrlAuthCustomActionForDescribeCdnConfigOutput.


        :param sign_cap_rule: The sign_cap_rule of this UrlAuthCustomActionForDescribeCdnConfigOutput.  # noqa: E501
        :type: SignCapRuleForDescribeCdnConfigOutput
        """

        self._sign_cap_rule = sign_cap_rule

    @property
    def sign_join_symbol(self):
        """Gets the sign_join_symbol of this UrlAuthCustomActionForDescribeCdnConfigOutput.  # noqa: E501


        :return: The sign_join_symbol of this UrlAuthCustomActionForDescribeCdnConfigOutput.  # noqa: E501
        :rtype: str
        """
        return self._sign_join_symbol

    @sign_join_symbol.setter
    def sign_join_symbol(self, sign_join_symbol):
        """Sets the sign_join_symbol of this UrlAuthCustomActionForDescribeCdnConfigOutput.


        :param sign_join_symbol: The sign_join_symbol of this UrlAuthCustomActionForDescribeCdnConfigOutput.  # noqa: E501
        :type: str
        """

        self._sign_join_symbol = sign_join_symbol

    @property
    def sign_param(self):
        """Gets the sign_param of this UrlAuthCustomActionForDescribeCdnConfigOutput.  # noqa: E501


        :return: The sign_param of this UrlAuthCustomActionForDescribeCdnConfigOutput.  # noqa: E501
        :rtype: list[SignParamForDescribeCdnConfigOutput]
        """
        return self._sign_param

    @sign_param.setter
    def sign_param(self, sign_param):
        """Sets the sign_param of this UrlAuthCustomActionForDescribeCdnConfigOutput.


        :param sign_param: The sign_param of this UrlAuthCustomActionForDescribeCdnConfigOutput.  # noqa: E501
        :type: list[SignParamForDescribeCdnConfigOutput]
        """

        self._sign_param = sign_param

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
        if issubclass(UrlAuthCustomActionForDescribeCdnConfigOutput, dict):
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
        if not isinstance(other, UrlAuthCustomActionForDescribeCdnConfigOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UrlAuthCustomActionForDescribeCdnConfigOutput):
            return True

        return self.to_dict() != other.to_dict()