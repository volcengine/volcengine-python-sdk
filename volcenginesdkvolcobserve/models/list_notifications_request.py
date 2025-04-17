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


class ListNotificationsRequest(object):
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
        'ids': 'list[str]',
        'levels': 'list[str]',
        'name': 'str',
        'page_number': 'int',
        'page_size': 'int',
        'rule_ids': 'list[str]'
    }

    attribute_map = {
        'ids': 'Ids',
        'levels': 'Levels',
        'name': 'Name',
        'page_number': 'PageNumber',
        'page_size': 'PageSize',
        'rule_ids': 'RuleIds'
    }

    def __init__(self, ids=None, levels=None, name=None, page_number=None, page_size=None, rule_ids=None, _configuration=None):  # noqa: E501
        """ListNotificationsRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._ids = None
        self._levels = None
        self._name = None
        self._page_number = None
        self._page_size = None
        self._rule_ids = None
        self.discriminator = None

        if ids is not None:
            self.ids = ids
        if levels is not None:
            self.levels = levels
        if name is not None:
            self.name = name
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if rule_ids is not None:
            self.rule_ids = rule_ids

    @property
    def ids(self):
        """Gets the ids of this ListNotificationsRequest.  # noqa: E501


        :return: The ids of this ListNotificationsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this ListNotificationsRequest.


        :param ids: The ids of this ListNotificationsRequest.  # noqa: E501
        :type: list[str]
        """

        self._ids = ids

    @property
    def levels(self):
        """Gets the levels of this ListNotificationsRequest.  # noqa: E501


        :return: The levels of this ListNotificationsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._levels

    @levels.setter
    def levels(self, levels):
        """Sets the levels of this ListNotificationsRequest.


        :param levels: The levels of this ListNotificationsRequest.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["notice", "warning", "critical", "recovery"]  # noqa: E501
        if (self._configuration.client_side_validation and
                not set(levels).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `levels` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(levels) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._levels = levels

    @property
    def name(self):
        """Gets the name of this ListNotificationsRequest.  # noqa: E501


        :return: The name of this ListNotificationsRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListNotificationsRequest.


        :param name: The name of this ListNotificationsRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def page_number(self):
        """Gets the page_number of this ListNotificationsRequest.  # noqa: E501


        :return: The page_number of this ListNotificationsRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this ListNotificationsRequest.


        :param page_number: The page_number of this ListNotificationsRequest.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this ListNotificationsRequest.  # noqa: E501


        :return: The page_size of this ListNotificationsRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ListNotificationsRequest.


        :param page_size: The page_size of this ListNotificationsRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def rule_ids(self):
        """Gets the rule_ids of this ListNotificationsRequest.  # noqa: E501


        :return: The rule_ids of this ListNotificationsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._rule_ids

    @rule_ids.setter
    def rule_ids(self, rule_ids):
        """Sets the rule_ids of this ListNotificationsRequest.


        :param rule_ids: The rule_ids of this ListNotificationsRequest.  # noqa: E501
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
        if issubclass(ListNotificationsRequest, dict):
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
        if not isinstance(other, ListNotificationsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListNotificationsRequest):
            return True

        return self.to_dict() != other.to_dict()
