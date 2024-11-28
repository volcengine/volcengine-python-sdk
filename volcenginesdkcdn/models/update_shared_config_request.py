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


class UpdateSharedConfigRequest(object):
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
        'allow_ip_access_rule': 'AllowIpAccessRuleForUpdateSharedConfigInput',
        'allow_referer_access_rule': 'AllowRefererAccessRuleForUpdateSharedConfigInput',
        'common_match_list': 'CommonMatchListForUpdateSharedConfigInput',
        'config_name': 'str',
        'deny_ip_access_rule': 'DenyIpAccessRuleForUpdateSharedConfigInput',
        'deny_referer_access_rule': 'DenyRefererAccessRuleForUpdateSharedConfigInput'
    }

    attribute_map = {
        'allow_ip_access_rule': 'AllowIpAccessRule',
        'allow_referer_access_rule': 'AllowRefererAccessRule',
        'common_match_list': 'CommonMatchList',
        'config_name': 'ConfigName',
        'deny_ip_access_rule': 'DenyIpAccessRule',
        'deny_referer_access_rule': 'DenyRefererAccessRule'
    }

    def __init__(self, allow_ip_access_rule=None, allow_referer_access_rule=None, common_match_list=None, config_name=None, deny_ip_access_rule=None, deny_referer_access_rule=None, _configuration=None):  # noqa: E501
        """UpdateSharedConfigRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._allow_ip_access_rule = None
        self._allow_referer_access_rule = None
        self._common_match_list = None
        self._config_name = None
        self._deny_ip_access_rule = None
        self._deny_referer_access_rule = None
        self.discriminator = None

        if allow_ip_access_rule is not None:
            self.allow_ip_access_rule = allow_ip_access_rule
        if allow_referer_access_rule is not None:
            self.allow_referer_access_rule = allow_referer_access_rule
        if common_match_list is not None:
            self.common_match_list = common_match_list
        self.config_name = config_name
        if deny_ip_access_rule is not None:
            self.deny_ip_access_rule = deny_ip_access_rule
        if deny_referer_access_rule is not None:
            self.deny_referer_access_rule = deny_referer_access_rule

    @property
    def allow_ip_access_rule(self):
        """Gets the allow_ip_access_rule of this UpdateSharedConfigRequest.  # noqa: E501


        :return: The allow_ip_access_rule of this UpdateSharedConfigRequest.  # noqa: E501
        :rtype: AllowIpAccessRuleForUpdateSharedConfigInput
        """
        return self._allow_ip_access_rule

    @allow_ip_access_rule.setter
    def allow_ip_access_rule(self, allow_ip_access_rule):
        """Sets the allow_ip_access_rule of this UpdateSharedConfigRequest.


        :param allow_ip_access_rule: The allow_ip_access_rule of this UpdateSharedConfigRequest.  # noqa: E501
        :type: AllowIpAccessRuleForUpdateSharedConfigInput
        """

        self._allow_ip_access_rule = allow_ip_access_rule

    @property
    def allow_referer_access_rule(self):
        """Gets the allow_referer_access_rule of this UpdateSharedConfigRequest.  # noqa: E501


        :return: The allow_referer_access_rule of this UpdateSharedConfigRequest.  # noqa: E501
        :rtype: AllowRefererAccessRuleForUpdateSharedConfigInput
        """
        return self._allow_referer_access_rule

    @allow_referer_access_rule.setter
    def allow_referer_access_rule(self, allow_referer_access_rule):
        """Sets the allow_referer_access_rule of this UpdateSharedConfigRequest.


        :param allow_referer_access_rule: The allow_referer_access_rule of this UpdateSharedConfigRequest.  # noqa: E501
        :type: AllowRefererAccessRuleForUpdateSharedConfigInput
        """

        self._allow_referer_access_rule = allow_referer_access_rule

    @property
    def common_match_list(self):
        """Gets the common_match_list of this UpdateSharedConfigRequest.  # noqa: E501


        :return: The common_match_list of this UpdateSharedConfigRequest.  # noqa: E501
        :rtype: CommonMatchListForUpdateSharedConfigInput
        """
        return self._common_match_list

    @common_match_list.setter
    def common_match_list(self, common_match_list):
        """Sets the common_match_list of this UpdateSharedConfigRequest.


        :param common_match_list: The common_match_list of this UpdateSharedConfigRequest.  # noqa: E501
        :type: CommonMatchListForUpdateSharedConfigInput
        """

        self._common_match_list = common_match_list

    @property
    def config_name(self):
        """Gets the config_name of this UpdateSharedConfigRequest.  # noqa: E501


        :return: The config_name of this UpdateSharedConfigRequest.  # noqa: E501
        :rtype: str
        """
        return self._config_name

    @config_name.setter
    def config_name(self, config_name):
        """Sets the config_name of this UpdateSharedConfigRequest.


        :param config_name: The config_name of this UpdateSharedConfigRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and config_name is None:
            raise ValueError("Invalid value for `config_name`, must not be `None`")  # noqa: E501

        self._config_name = config_name

    @property
    def deny_ip_access_rule(self):
        """Gets the deny_ip_access_rule of this UpdateSharedConfigRequest.  # noqa: E501


        :return: The deny_ip_access_rule of this UpdateSharedConfigRequest.  # noqa: E501
        :rtype: DenyIpAccessRuleForUpdateSharedConfigInput
        """
        return self._deny_ip_access_rule

    @deny_ip_access_rule.setter
    def deny_ip_access_rule(self, deny_ip_access_rule):
        """Sets the deny_ip_access_rule of this UpdateSharedConfigRequest.


        :param deny_ip_access_rule: The deny_ip_access_rule of this UpdateSharedConfigRequest.  # noqa: E501
        :type: DenyIpAccessRuleForUpdateSharedConfigInput
        """

        self._deny_ip_access_rule = deny_ip_access_rule

    @property
    def deny_referer_access_rule(self):
        """Gets the deny_referer_access_rule of this UpdateSharedConfigRequest.  # noqa: E501


        :return: The deny_referer_access_rule of this UpdateSharedConfigRequest.  # noqa: E501
        :rtype: DenyRefererAccessRuleForUpdateSharedConfigInput
        """
        return self._deny_referer_access_rule

    @deny_referer_access_rule.setter
    def deny_referer_access_rule(self, deny_referer_access_rule):
        """Sets the deny_referer_access_rule of this UpdateSharedConfigRequest.


        :param deny_referer_access_rule: The deny_referer_access_rule of this UpdateSharedConfigRequest.  # noqa: E501
        :type: DenyRefererAccessRuleForUpdateSharedConfigInput
        """

        self._deny_referer_access_rule = deny_referer_access_rule

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
        if issubclass(UpdateSharedConfigRequest, dict):
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
        if not isinstance(other, UpdateSharedConfigRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateSharedConfigRequest):
            return True

        return self.to_dict() != other.to_dict()
