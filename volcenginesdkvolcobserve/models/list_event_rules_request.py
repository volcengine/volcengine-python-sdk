# coding: utf-8

"""
    volc_observe

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ListEventRulesRequest(object):
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
        'order_by': 'str',
        'page_number': 'int',
        'page_size': 'int',
        'rule_name': 'str',
        'source': 'list[str]',
        'status': 'list[str]'
    }

    attribute_map = {
        'asc': 'Asc',
        'order_by': 'OrderBy',
        'page_number': 'PageNumber',
        'page_size': 'PageSize',
        'rule_name': 'RuleName',
        'source': 'Source',
        'status': 'Status'
    }

    def __init__(self, asc=None, order_by=None, page_number=None, page_size=None, rule_name=None, source=None, status=None, _configuration=None):  # noqa: E501
        """ListEventRulesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._asc = None
        self._order_by = None
        self._page_number = None
        self._page_size = None
        self._rule_name = None
        self._source = None
        self._status = None
        self.discriminator = None

        if asc is not None:
            self.asc = asc
        if order_by is not None:
            self.order_by = order_by
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if rule_name is not None:
            self.rule_name = rule_name
        if source is not None:
            self.source = source
        if status is not None:
            self.status = status

    @property
    def asc(self):
        """Gets the asc of this ListEventRulesRequest.  # noqa: E501


        :return: The asc of this ListEventRulesRequest.  # noqa: E501
        :rtype: bool
        """
        return self._asc

    @asc.setter
    def asc(self, asc):
        """Sets the asc of this ListEventRulesRequest.


        :param asc: The asc of this ListEventRulesRequest.  # noqa: E501
        :type: bool
        """

        self._asc = asc

    @property
    def order_by(self):
        """Gets the order_by of this ListEventRulesRequest.  # noqa: E501


        :return: The order_by of this ListEventRulesRequest.  # noqa: E501
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        """Sets the order_by of this ListEventRulesRequest.


        :param order_by: The order_by of this ListEventRulesRequest.  # noqa: E501
        :type: str
        """

        self._order_by = order_by

    @property
    def page_number(self):
        """Gets the page_number of this ListEventRulesRequest.  # noqa: E501


        :return: The page_number of this ListEventRulesRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this ListEventRulesRequest.


        :param page_number: The page_number of this ListEventRulesRequest.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this ListEventRulesRequest.  # noqa: E501


        :return: The page_size of this ListEventRulesRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ListEventRulesRequest.


        :param page_size: The page_size of this ListEventRulesRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def rule_name(self):
        """Gets the rule_name of this ListEventRulesRequest.  # noqa: E501


        :return: The rule_name of this ListEventRulesRequest.  # noqa: E501
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        """Sets the rule_name of this ListEventRulesRequest.


        :param rule_name: The rule_name of this ListEventRulesRequest.  # noqa: E501
        :type: str
        """

        self._rule_name = rule_name

    @property
    def source(self):
        """Gets the source of this ListEventRulesRequest.  # noqa: E501


        :return: The source of this ListEventRulesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this ListEventRulesRequest.


        :param source: The source of this ListEventRulesRequest.  # noqa: E501
        :type: list[str]
        """

        self._source = source

    @property
    def status(self):
        """Gets the status of this ListEventRulesRequest.  # noqa: E501


        :return: The status of this ListEventRulesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListEventRulesRequest.


        :param status: The status of this ListEventRulesRequest.  # noqa: E501
        :type: list[str]
        """

        self._status = status

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
        if issubclass(ListEventRulesRequest, dict):
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
        if not isinstance(other, ListEventRulesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListEventRulesRequest):
            return True

        return self.to_dict() != other.to_dict()