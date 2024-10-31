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


class ListHostGroupRequest(object):
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
        'host_fix': 'str',
        'host_group_id': 'int',
        'list_all': 'bool',
        'name_fix': 'str',
        'page': 'int',
        'page_size': 'int',
        'rule_tag': 'str',
        'time_order_by': 'str'
    }

    attribute_map = {
        'host_fix': 'HostFix',
        'host_group_id': 'HostGroupID',
        'list_all': 'ListAll',
        'name_fix': 'NameFix',
        'page': 'Page',
        'page_size': 'PageSize',
        'rule_tag': 'RuleTag',
        'time_order_by': 'TimeOrderBy'
    }

    def __init__(self, host_fix=None, host_group_id=None, list_all=None, name_fix=None, page=None, page_size=None, rule_tag=None, time_order_by=None, _configuration=None):  # noqa: E501
        """ListHostGroupRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._host_fix = None
        self._host_group_id = None
        self._list_all = None
        self._name_fix = None
        self._page = None
        self._page_size = None
        self._rule_tag = None
        self._time_order_by = None
        self.discriminator = None

        if host_fix is not None:
            self.host_fix = host_fix
        if host_group_id is not None:
            self.host_group_id = host_group_id
        if list_all is not None:
            self.list_all = list_all
        if name_fix is not None:
            self.name_fix = name_fix
        if page is not None:
            self.page = page
        if page_size is not None:
            self.page_size = page_size
        if rule_tag is not None:
            self.rule_tag = rule_tag
        if time_order_by is not None:
            self.time_order_by = time_order_by

    @property
    def host_fix(self):
        """Gets the host_fix of this ListHostGroupRequest.  # noqa: E501


        :return: The host_fix of this ListHostGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._host_fix

    @host_fix.setter
    def host_fix(self, host_fix):
        """Sets the host_fix of this ListHostGroupRequest.


        :param host_fix: The host_fix of this ListHostGroupRequest.  # noqa: E501
        :type: str
        """

        self._host_fix = host_fix

    @property
    def host_group_id(self):
        """Gets the host_group_id of this ListHostGroupRequest.  # noqa: E501


        :return: The host_group_id of this ListHostGroupRequest.  # noqa: E501
        :rtype: int
        """
        return self._host_group_id

    @host_group_id.setter
    def host_group_id(self, host_group_id):
        """Sets the host_group_id of this ListHostGroupRequest.


        :param host_group_id: The host_group_id of this ListHostGroupRequest.  # noqa: E501
        :type: int
        """

        self._host_group_id = host_group_id

    @property
    def list_all(self):
        """Gets the list_all of this ListHostGroupRequest.  # noqa: E501


        :return: The list_all of this ListHostGroupRequest.  # noqa: E501
        :rtype: bool
        """
        return self._list_all

    @list_all.setter
    def list_all(self, list_all):
        """Sets the list_all of this ListHostGroupRequest.


        :param list_all: The list_all of this ListHostGroupRequest.  # noqa: E501
        :type: bool
        """

        self._list_all = list_all

    @property
    def name_fix(self):
        """Gets the name_fix of this ListHostGroupRequest.  # noqa: E501


        :return: The name_fix of this ListHostGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._name_fix

    @name_fix.setter
    def name_fix(self, name_fix):
        """Sets the name_fix of this ListHostGroupRequest.


        :param name_fix: The name_fix of this ListHostGroupRequest.  # noqa: E501
        :type: str
        """

        self._name_fix = name_fix

    @property
    def page(self):
        """Gets the page of this ListHostGroupRequest.  # noqa: E501


        :return: The page of this ListHostGroupRequest.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListHostGroupRequest.


        :param page: The page of this ListHostGroupRequest.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def page_size(self):
        """Gets the page_size of this ListHostGroupRequest.  # noqa: E501


        :return: The page_size of this ListHostGroupRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ListHostGroupRequest.


        :param page_size: The page_size of this ListHostGroupRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def rule_tag(self):
        """Gets the rule_tag of this ListHostGroupRequest.  # noqa: E501


        :return: The rule_tag of this ListHostGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._rule_tag

    @rule_tag.setter
    def rule_tag(self, rule_tag):
        """Sets the rule_tag of this ListHostGroupRequest.


        :param rule_tag: The rule_tag of this ListHostGroupRequest.  # noqa: E501
        :type: str
        """

        self._rule_tag = rule_tag

    @property
    def time_order_by(self):
        """Gets the time_order_by of this ListHostGroupRequest.  # noqa: E501


        :return: The time_order_by of this ListHostGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._time_order_by

    @time_order_by.setter
    def time_order_by(self, time_order_by):
        """Sets the time_order_by of this ListHostGroupRequest.


        :param time_order_by: The time_order_by of this ListHostGroupRequest.  # noqa: E501
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
        if issubclass(ListHostGroupRequest, dict):
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
        if not isinstance(other, ListHostGroupRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListHostGroupRequest):
            return True

        return self.to_dict() != other.to_dict()