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


class HostGroupListForListHostGroupOutput(object):
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
        'description': 'str',
        'host_count': 'int',
        'host_group_id': 'int',
        'host_list': 'list[str]',
        'name': 'str',
        'related_rules': 'list[RelatedRuleForListHostGroupOutput]',
        'update_time': 'str'
    }

    attribute_map = {
        'description': 'Description',
        'host_count': 'HostCount',
        'host_group_id': 'HostGroupId',
        'host_list': 'HostList',
        'name': 'Name',
        'related_rules': 'RelatedRules',
        'update_time': 'UpdateTime'
    }

    def __init__(self, description=None, host_count=None, host_group_id=None, host_list=None, name=None, related_rules=None, update_time=None, _configuration=None):  # noqa: E501
        """HostGroupListForListHostGroupOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._description = None
        self._host_count = None
        self._host_group_id = None
        self._host_list = None
        self._name = None
        self._related_rules = None
        self._update_time = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if host_count is not None:
            self.host_count = host_count
        if host_group_id is not None:
            self.host_group_id = host_group_id
        if host_list is not None:
            self.host_list = host_list
        if name is not None:
            self.name = name
        if related_rules is not None:
            self.related_rules = related_rules
        if update_time is not None:
            self.update_time = update_time

    @property
    def description(self):
        """Gets the description of this HostGroupListForListHostGroupOutput.  # noqa: E501


        :return: The description of this HostGroupListForListHostGroupOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this HostGroupListForListHostGroupOutput.


        :param description: The description of this HostGroupListForListHostGroupOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def host_count(self):
        """Gets the host_count of this HostGroupListForListHostGroupOutput.  # noqa: E501


        :return: The host_count of this HostGroupListForListHostGroupOutput.  # noqa: E501
        :rtype: int
        """
        return self._host_count

    @host_count.setter
    def host_count(self, host_count):
        """Sets the host_count of this HostGroupListForListHostGroupOutput.


        :param host_count: The host_count of this HostGroupListForListHostGroupOutput.  # noqa: E501
        :type: int
        """

        self._host_count = host_count

    @property
    def host_group_id(self):
        """Gets the host_group_id of this HostGroupListForListHostGroupOutput.  # noqa: E501


        :return: The host_group_id of this HostGroupListForListHostGroupOutput.  # noqa: E501
        :rtype: int
        """
        return self._host_group_id

    @host_group_id.setter
    def host_group_id(self, host_group_id):
        """Sets the host_group_id of this HostGroupListForListHostGroupOutput.


        :param host_group_id: The host_group_id of this HostGroupListForListHostGroupOutput.  # noqa: E501
        :type: int
        """

        self._host_group_id = host_group_id

    @property
    def host_list(self):
        """Gets the host_list of this HostGroupListForListHostGroupOutput.  # noqa: E501


        :return: The host_list of this HostGroupListForListHostGroupOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._host_list

    @host_list.setter
    def host_list(self, host_list):
        """Sets the host_list of this HostGroupListForListHostGroupOutput.


        :param host_list: The host_list of this HostGroupListForListHostGroupOutput.  # noqa: E501
        :type: list[str]
        """

        self._host_list = host_list

    @property
    def name(self):
        """Gets the name of this HostGroupListForListHostGroupOutput.  # noqa: E501


        :return: The name of this HostGroupListForListHostGroupOutput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HostGroupListForListHostGroupOutput.


        :param name: The name of this HostGroupListForListHostGroupOutput.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def related_rules(self):
        """Gets the related_rules of this HostGroupListForListHostGroupOutput.  # noqa: E501


        :return: The related_rules of this HostGroupListForListHostGroupOutput.  # noqa: E501
        :rtype: list[RelatedRuleForListHostGroupOutput]
        """
        return self._related_rules

    @related_rules.setter
    def related_rules(self, related_rules):
        """Sets the related_rules of this HostGroupListForListHostGroupOutput.


        :param related_rules: The related_rules of this HostGroupListForListHostGroupOutput.  # noqa: E501
        :type: list[RelatedRuleForListHostGroupOutput]
        """

        self._related_rules = related_rules

    @property
    def update_time(self):
        """Gets the update_time of this HostGroupListForListHostGroupOutput.  # noqa: E501


        :return: The update_time of this HostGroupListForListHostGroupOutput.  # noqa: E501
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this HostGroupListForListHostGroupOutput.


        :param update_time: The update_time of this HostGroupListForListHostGroupOutput.  # noqa: E501
        :type: str
        """

        self._update_time = update_time

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
        if issubclass(HostGroupListForListHostGroupOutput, dict):
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
        if not isinstance(other, HostGroupListForListHostGroupOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HostGroupListForListHostGroupOutput):
            return True

        return self.to_dict() != other.to_dict()