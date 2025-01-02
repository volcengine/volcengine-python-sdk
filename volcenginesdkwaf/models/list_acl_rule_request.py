# coding: utf-8

"""
    waf

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ListAclRuleRequest(object):
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
        'acl_type': 'str',
        'action': 'list[str]',
        'defence_host': 'list[str]',
        'enable': 'list[int]',
        'page': 'int',
        'page_size': 'int',
        'project_name': 'str',
        'rule_name': 'str',
        'rule_tag': 'str',
        'time_order_by': 'str'
    }

    attribute_map = {
        'acl_type': 'AclType',
        'action': 'Action',
        'defence_host': 'DefenceHost',
        'enable': 'Enable',
        'page': 'Page',
        'page_size': 'PageSize',
        'project_name': 'ProjectName',
        'rule_name': 'RuleName',
        'rule_tag': 'RuleTag',
        'time_order_by': 'TimeOrderBy'
    }

    def __init__(self, acl_type=None, action=None, defence_host=None, enable=None, page=None, page_size=None, project_name=None, rule_name=None, rule_tag=None, time_order_by=None, _configuration=None):  # noqa: E501
        """ListAclRuleRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._acl_type = None
        self._action = None
        self._defence_host = None
        self._enable = None
        self._page = None
        self._page_size = None
        self._project_name = None
        self._rule_name = None
        self._rule_tag = None
        self._time_order_by = None
        self.discriminator = None

        self.acl_type = acl_type
        if action is not None:
            self.action = action
        if defence_host is not None:
            self.defence_host = defence_host
        if enable is not None:
            self.enable = enable
        if page is not None:
            self.page = page
        if page_size is not None:
            self.page_size = page_size
        if project_name is not None:
            self.project_name = project_name
        if rule_name is not None:
            self.rule_name = rule_name
        if rule_tag is not None:
            self.rule_tag = rule_tag
        if time_order_by is not None:
            self.time_order_by = time_order_by

    @property
    def acl_type(self):
        """Gets the acl_type of this ListAclRuleRequest.  # noqa: E501


        :return: The acl_type of this ListAclRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._acl_type

    @acl_type.setter
    def acl_type(self, acl_type):
        """Sets the acl_type of this ListAclRuleRequest.


        :param acl_type: The acl_type of this ListAclRuleRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and acl_type is None:
            raise ValueError("Invalid value for `acl_type`, must not be `None`")  # noqa: E501

        self._acl_type = acl_type

    @property
    def action(self):
        """Gets the action of this ListAclRuleRequest.  # noqa: E501


        :return: The action of this ListAclRuleRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ListAclRuleRequest.


        :param action: The action of this ListAclRuleRequest.  # noqa: E501
        :type: list[str]
        """

        self._action = action

    @property
    def defence_host(self):
        """Gets the defence_host of this ListAclRuleRequest.  # noqa: E501


        :return: The defence_host of this ListAclRuleRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._defence_host

    @defence_host.setter
    def defence_host(self, defence_host):
        """Sets the defence_host of this ListAclRuleRequest.


        :param defence_host: The defence_host of this ListAclRuleRequest.  # noqa: E501
        :type: list[str]
        """

        self._defence_host = defence_host

    @property
    def enable(self):
        """Gets the enable of this ListAclRuleRequest.  # noqa: E501


        :return: The enable of this ListAclRuleRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this ListAclRuleRequest.


        :param enable: The enable of this ListAclRuleRequest.  # noqa: E501
        :type: list[int]
        """

        self._enable = enable

    @property
    def page(self):
        """Gets the page of this ListAclRuleRequest.  # noqa: E501


        :return: The page of this ListAclRuleRequest.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListAclRuleRequest.


        :param page: The page of this ListAclRuleRequest.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def page_size(self):
        """Gets the page_size of this ListAclRuleRequest.  # noqa: E501


        :return: The page_size of this ListAclRuleRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ListAclRuleRequest.


        :param page_size: The page_size of this ListAclRuleRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def project_name(self):
        """Gets the project_name of this ListAclRuleRequest.  # noqa: E501


        :return: The project_name of this ListAclRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this ListAclRuleRequest.


        :param project_name: The project_name of this ListAclRuleRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def rule_name(self):
        """Gets the rule_name of this ListAclRuleRequest.  # noqa: E501


        :return: The rule_name of this ListAclRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        """Sets the rule_name of this ListAclRuleRequest.


        :param rule_name: The rule_name of this ListAclRuleRequest.  # noqa: E501
        :type: str
        """

        self._rule_name = rule_name

    @property
    def rule_tag(self):
        """Gets the rule_tag of this ListAclRuleRequest.  # noqa: E501


        :return: The rule_tag of this ListAclRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._rule_tag

    @rule_tag.setter
    def rule_tag(self, rule_tag):
        """Sets the rule_tag of this ListAclRuleRequest.


        :param rule_tag: The rule_tag of this ListAclRuleRequest.  # noqa: E501
        :type: str
        """

        self._rule_tag = rule_tag

    @property
    def time_order_by(self):
        """Gets the time_order_by of this ListAclRuleRequest.  # noqa: E501


        :return: The time_order_by of this ListAclRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._time_order_by

    @time_order_by.setter
    def time_order_by(self, time_order_by):
        """Sets the time_order_by of this ListAclRuleRequest.


        :param time_order_by: The time_order_by of this ListAclRuleRequest.  # noqa: E501
        :type: str
        """

        self._time_order_by = time_order_by

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
        if issubclass(ListAclRuleRequest, dict):
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
        if not isinstance(other, ListAclRuleRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListAclRuleRequest):
            return True

        return self.to_dict() != other.to_dict()
