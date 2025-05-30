# coding: utf-8

"""
    seccenter20240508

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DataForListWhiteListsOutput(object):
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
        'desc': 'str',
        'id': 'str',
        'match_alarm_name': 'str',
        'name': 'str',
        'range': 'RangeForListWhiteListsOutput',
        'rule_list': 'list[RuleListForListWhiteListsOutput]',
        'update_time': 'int',
        'user': 'str'
    }

    attribute_map = {
        'desc': 'Desc',
        'id': 'ID',
        'match_alarm_name': 'MatchAlarmName',
        'name': 'Name',
        'range': 'Range',
        'rule_list': 'RuleList',
        'update_time': 'UpdateTime',
        'user': 'User'
    }

    def __init__(self, desc=None, id=None, match_alarm_name=None, name=None, range=None, rule_list=None, update_time=None, user=None, _configuration=None):  # noqa: E501
        """DataForListWhiteListsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._desc = None
        self._id = None
        self._match_alarm_name = None
        self._name = None
        self._range = None
        self._rule_list = None
        self._update_time = None
        self._user = None
        self.discriminator = None

        if desc is not None:
            self.desc = desc
        if id is not None:
            self.id = id
        if match_alarm_name is not None:
            self.match_alarm_name = match_alarm_name
        if name is not None:
            self.name = name
        if range is not None:
            self.range = range
        if rule_list is not None:
            self.rule_list = rule_list
        if update_time is not None:
            self.update_time = update_time
        if user is not None:
            self.user = user

    @property
    def desc(self):
        """Gets the desc of this DataForListWhiteListsOutput.  # noqa: E501


        :return: The desc of this DataForListWhiteListsOutput.  # noqa: E501
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this DataForListWhiteListsOutput.


        :param desc: The desc of this DataForListWhiteListsOutput.  # noqa: E501
        :type: str
        """

        self._desc = desc

    @property
    def id(self):
        """Gets the id of this DataForListWhiteListsOutput.  # noqa: E501


        :return: The id of this DataForListWhiteListsOutput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DataForListWhiteListsOutput.


        :param id: The id of this DataForListWhiteListsOutput.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def match_alarm_name(self):
        """Gets the match_alarm_name of this DataForListWhiteListsOutput.  # noqa: E501


        :return: The match_alarm_name of this DataForListWhiteListsOutput.  # noqa: E501
        :rtype: str
        """
        return self._match_alarm_name

    @match_alarm_name.setter
    def match_alarm_name(self, match_alarm_name):
        """Sets the match_alarm_name of this DataForListWhiteListsOutput.


        :param match_alarm_name: The match_alarm_name of this DataForListWhiteListsOutput.  # noqa: E501
        :type: str
        """

        self._match_alarm_name = match_alarm_name

    @property
    def name(self):
        """Gets the name of this DataForListWhiteListsOutput.  # noqa: E501


        :return: The name of this DataForListWhiteListsOutput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DataForListWhiteListsOutput.


        :param name: The name of this DataForListWhiteListsOutput.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def range(self):
        """Gets the range of this DataForListWhiteListsOutput.  # noqa: E501


        :return: The range of this DataForListWhiteListsOutput.  # noqa: E501
        :rtype: RangeForListWhiteListsOutput
        """
        return self._range

    @range.setter
    def range(self, range):
        """Sets the range of this DataForListWhiteListsOutput.


        :param range: The range of this DataForListWhiteListsOutput.  # noqa: E501
        :type: RangeForListWhiteListsOutput
        """

        self._range = range

    @property
    def rule_list(self):
        """Gets the rule_list of this DataForListWhiteListsOutput.  # noqa: E501


        :return: The rule_list of this DataForListWhiteListsOutput.  # noqa: E501
        :rtype: list[RuleListForListWhiteListsOutput]
        """
        return self._rule_list

    @rule_list.setter
    def rule_list(self, rule_list):
        """Sets the rule_list of this DataForListWhiteListsOutput.


        :param rule_list: The rule_list of this DataForListWhiteListsOutput.  # noqa: E501
        :type: list[RuleListForListWhiteListsOutput]
        """

        self._rule_list = rule_list

    @property
    def update_time(self):
        """Gets the update_time of this DataForListWhiteListsOutput.  # noqa: E501


        :return: The update_time of this DataForListWhiteListsOutput.  # noqa: E501
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this DataForListWhiteListsOutput.


        :param update_time: The update_time of this DataForListWhiteListsOutput.  # noqa: E501
        :type: int
        """

        self._update_time = update_time

    @property
    def user(self):
        """Gets the user of this DataForListWhiteListsOutput.  # noqa: E501


        :return: The user of this DataForListWhiteListsOutput.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this DataForListWhiteListsOutput.


        :param user: The user of this DataForListWhiteListsOutput.  # noqa: E501
        :type: str
        """

        self._user = user

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
        if issubclass(DataForListWhiteListsOutput, dict):
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
        if not isinstance(other, DataForListWhiteListsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataForListWhiteListsOutput):
            return True

        return self.to_dict() != other.to_dict()
