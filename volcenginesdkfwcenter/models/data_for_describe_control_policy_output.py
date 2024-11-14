# coding: utf-8

"""
    fwcenter

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DataForDescribeControlPolicyOutput(object):
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
        'account_id': 'str',
        'action': 'str',
        'description': 'str',
        'dest_port': 'str',
        'dest_port_group_type': 'str',
        'dest_port_list': 'list[str]',
        'dest_port_type': 'str',
        'destination': 'str',
        'destination_cidr_list': 'list[str]',
        'destination_group_type': 'str',
        'destination_type': 'str',
        'direction': 'str',
        'effect_status': 'int',
        'end_time': 'int',
        'hit_cnt': 'int',
        'is_effected': 'bool',
        'prio': 'int',
        'proto': 'str',
        'repeat_days': 'list[int]',
        'repeat_end_time': 'str',
        'repeat_start_time': 'str',
        'repeat_type': 'str',
        'rule_id': 'str',
        'source': 'str',
        'source_cidr_list': 'list[str]',
        'source_group_type': 'str',
        'source_type': 'str',
        'start_time': 'int',
        'status': 'bool',
        'update_time': 'int',
        'use_count': 'int'
    }

    attribute_map = {
        'account_id': 'AccountId',
        'action': 'Action',
        'description': 'Description',
        'dest_port': 'DestPort',
        'dest_port_group_type': 'DestPortGroupType',
        'dest_port_list': 'DestPortList',
        'dest_port_type': 'DestPortType',
        'destination': 'Destination',
        'destination_cidr_list': 'DestinationCidrList',
        'destination_group_type': 'DestinationGroupType',
        'destination_type': 'DestinationType',
        'direction': 'Direction',
        'effect_status': 'EffectStatus',
        'end_time': 'EndTime',
        'hit_cnt': 'HitCnt',
        'is_effected': 'IsEffected',
        'prio': 'Prio',
        'proto': 'Proto',
        'repeat_days': 'RepeatDays',
        'repeat_end_time': 'RepeatEndTime',
        'repeat_start_time': 'RepeatStartTime',
        'repeat_type': 'RepeatType',
        'rule_id': 'RuleId',
        'source': 'Source',
        'source_cidr_list': 'SourceCidrList',
        'source_group_type': 'SourceGroupType',
        'source_type': 'SourceType',
        'start_time': 'StartTime',
        'status': 'Status',
        'update_time': 'UpdateTime',
        'use_count': 'UseCount'
    }

    def __init__(self, account_id=None, action=None, description=None, dest_port=None, dest_port_group_type=None, dest_port_list=None, dest_port_type=None, destination=None, destination_cidr_list=None, destination_group_type=None, destination_type=None, direction=None, effect_status=None, end_time=None, hit_cnt=None, is_effected=None, prio=None, proto=None, repeat_days=None, repeat_end_time=None, repeat_start_time=None, repeat_type=None, rule_id=None, source=None, source_cidr_list=None, source_group_type=None, source_type=None, start_time=None, status=None, update_time=None, use_count=None, _configuration=None):  # noqa: E501
        """DataForDescribeControlPolicyOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_id = None
        self._action = None
        self._description = None
        self._dest_port = None
        self._dest_port_group_type = None
        self._dest_port_list = None
        self._dest_port_type = None
        self._destination = None
        self._destination_cidr_list = None
        self._destination_group_type = None
        self._destination_type = None
        self._direction = None
        self._effect_status = None
        self._end_time = None
        self._hit_cnt = None
        self._is_effected = None
        self._prio = None
        self._proto = None
        self._repeat_days = None
        self._repeat_end_time = None
        self._repeat_start_time = None
        self._repeat_type = None
        self._rule_id = None
        self._source = None
        self._source_cidr_list = None
        self._source_group_type = None
        self._source_type = None
        self._start_time = None
        self._status = None
        self._update_time = None
        self._use_count = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if action is not None:
            self.action = action
        if description is not None:
            self.description = description
        if dest_port is not None:
            self.dest_port = dest_port
        if dest_port_group_type is not None:
            self.dest_port_group_type = dest_port_group_type
        if dest_port_list is not None:
            self.dest_port_list = dest_port_list
        if dest_port_type is not None:
            self.dest_port_type = dest_port_type
        if destination is not None:
            self.destination = destination
        if destination_cidr_list is not None:
            self.destination_cidr_list = destination_cidr_list
        if destination_group_type is not None:
            self.destination_group_type = destination_group_type
        if destination_type is not None:
            self.destination_type = destination_type
        if direction is not None:
            self.direction = direction
        if effect_status is not None:
            self.effect_status = effect_status
        if end_time is not None:
            self.end_time = end_time
        if hit_cnt is not None:
            self.hit_cnt = hit_cnt
        if is_effected is not None:
            self.is_effected = is_effected
        if prio is not None:
            self.prio = prio
        if proto is not None:
            self.proto = proto
        if repeat_days is not None:
            self.repeat_days = repeat_days
        if repeat_end_time is not None:
            self.repeat_end_time = repeat_end_time
        if repeat_start_time is not None:
            self.repeat_start_time = repeat_start_time
        if repeat_type is not None:
            self.repeat_type = repeat_type
        if rule_id is not None:
            self.rule_id = rule_id
        if source is not None:
            self.source = source
        if source_cidr_list is not None:
            self.source_cidr_list = source_cidr_list
        if source_group_type is not None:
            self.source_group_type = source_group_type
        if source_type is not None:
            self.source_type = source_type
        if start_time is not None:
            self.start_time = start_time
        if status is not None:
            self.status = status
        if update_time is not None:
            self.update_time = update_time
        if use_count is not None:
            self.use_count = use_count

    @property
    def account_id(self):
        """Gets the account_id of this DataForDescribeControlPolicyOutput.  # noqa: E501


        :return: The account_id of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this DataForDescribeControlPolicyOutput.


        :param account_id: The account_id of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def action(self):
        """Gets the action of this DataForDescribeControlPolicyOutput.  # noqa: E501


        :return: The action of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this DataForDescribeControlPolicyOutput.


        :param action: The action of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def description(self):
        """Gets the description of this DataForDescribeControlPolicyOutput.  # noqa: E501


        :return: The description of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DataForDescribeControlPolicyOutput.


        :param description: The description of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def dest_port(self):
        """Gets the dest_port of this DataForDescribeControlPolicyOutput.  # noqa: E501


        :return: The dest_port of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :rtype: str
        """
        return self._dest_port

    @dest_port.setter
    def dest_port(self, dest_port):
        """Sets the dest_port of this DataForDescribeControlPolicyOutput.


        :param dest_port: The dest_port of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :type: str
        """

        self._dest_port = dest_port

    @property
    def dest_port_group_type(self):
        """Gets the dest_port_group_type of this DataForDescribeControlPolicyOutput.  # noqa: E501


        :return: The dest_port_group_type of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :rtype: str
        """
        return self._dest_port_group_type

    @dest_port_group_type.setter
    def dest_port_group_type(self, dest_port_group_type):
        """Sets the dest_port_group_type of this DataForDescribeControlPolicyOutput.


        :param dest_port_group_type: The dest_port_group_type of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :type: str
        """

        self._dest_port_group_type = dest_port_group_type

    @property
    def dest_port_list(self):
        """Gets the dest_port_list of this DataForDescribeControlPolicyOutput.  # noqa: E501


        :return: The dest_port_list of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._dest_port_list

    @dest_port_list.setter
    def dest_port_list(self, dest_port_list):
        """Sets the dest_port_list of this DataForDescribeControlPolicyOutput.


        :param dest_port_list: The dest_port_list of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :type: list[str]
        """

        self._dest_port_list = dest_port_list

    @property
    def dest_port_type(self):
        """Gets the dest_port_type of this DataForDescribeControlPolicyOutput.  # noqa: E501


        :return: The dest_port_type of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :rtype: str
        """
        return self._dest_port_type

    @dest_port_type.setter
    def dest_port_type(self, dest_port_type):
        """Sets the dest_port_type of this DataForDescribeControlPolicyOutput.


        :param dest_port_type: The dest_port_type of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :type: str
        """

        self._dest_port_type = dest_port_type

    @property
    def destination(self):
        """Gets the destination of this DataForDescribeControlPolicyOutput.  # noqa: E501


        :return: The destination of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this DataForDescribeControlPolicyOutput.


        :param destination: The destination of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :type: str
        """

        self._destination = destination

    @property
    def destination_cidr_list(self):
        """Gets the destination_cidr_list of this DataForDescribeControlPolicyOutput.  # noqa: E501


        :return: The destination_cidr_list of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._destination_cidr_list

    @destination_cidr_list.setter
    def destination_cidr_list(self, destination_cidr_list):
        """Sets the destination_cidr_list of this DataForDescribeControlPolicyOutput.


        :param destination_cidr_list: The destination_cidr_list of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :type: list[str]
        """

        self._destination_cidr_list = destination_cidr_list

    @property
    def destination_group_type(self):
        """Gets the destination_group_type of this DataForDescribeControlPolicyOutput.  # noqa: E501


        :return: The destination_group_type of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :rtype: str
        """
        return self._destination_group_type

    @destination_group_type.setter
    def destination_group_type(self, destination_group_type):
        """Sets the destination_group_type of this DataForDescribeControlPolicyOutput.


        :param destination_group_type: The destination_group_type of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :type: str
        """

        self._destination_group_type = destination_group_type

    @property
    def destination_type(self):
        """Gets the destination_type of this DataForDescribeControlPolicyOutput.  # noqa: E501


        :return: The destination_type of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :rtype: str
        """
        return self._destination_type

    @destination_type.setter
    def destination_type(self, destination_type):
        """Sets the destination_type of this DataForDescribeControlPolicyOutput.


        :param destination_type: The destination_type of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :type: str
        """

        self._destination_type = destination_type

    @property
    def direction(self):
        """Gets the direction of this DataForDescribeControlPolicyOutput.  # noqa: E501


        :return: The direction of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this DataForDescribeControlPolicyOutput.


        :param direction: The direction of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :type: str
        """

        self._direction = direction

    @property
    def effect_status(self):
        """Gets the effect_status of this DataForDescribeControlPolicyOutput.  # noqa: E501


        :return: The effect_status of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :rtype: int
        """
        return self._effect_status

    @effect_status.setter
    def effect_status(self, effect_status):
        """Sets the effect_status of this DataForDescribeControlPolicyOutput.


        :param effect_status: The effect_status of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :type: int
        """

        self._effect_status = effect_status

    @property
    def end_time(self):
        """Gets the end_time of this DataForDescribeControlPolicyOutput.  # noqa: E501


        :return: The end_time of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this DataForDescribeControlPolicyOutput.


        :param end_time: The end_time of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :type: int
        """

        self._end_time = end_time

    @property
    def hit_cnt(self):
        """Gets the hit_cnt of this DataForDescribeControlPolicyOutput.  # noqa: E501


        :return: The hit_cnt of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :rtype: int
        """
        return self._hit_cnt

    @hit_cnt.setter
    def hit_cnt(self, hit_cnt):
        """Sets the hit_cnt of this DataForDescribeControlPolicyOutput.


        :param hit_cnt: The hit_cnt of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :type: int
        """

        self._hit_cnt = hit_cnt

    @property
    def is_effected(self):
        """Gets the is_effected of this DataForDescribeControlPolicyOutput.  # noqa: E501


        :return: The is_effected of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :rtype: bool
        """
        return self._is_effected

    @is_effected.setter
    def is_effected(self, is_effected):
        """Sets the is_effected of this DataForDescribeControlPolicyOutput.


        :param is_effected: The is_effected of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :type: bool
        """

        self._is_effected = is_effected

    @property
    def prio(self):
        """Gets the prio of this DataForDescribeControlPolicyOutput.  # noqa: E501


        :return: The prio of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :rtype: int
        """
        return self._prio

    @prio.setter
    def prio(self, prio):
        """Sets the prio of this DataForDescribeControlPolicyOutput.


        :param prio: The prio of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :type: int
        """

        self._prio = prio

    @property
    def proto(self):
        """Gets the proto of this DataForDescribeControlPolicyOutput.  # noqa: E501


        :return: The proto of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :rtype: str
        """
        return self._proto

    @proto.setter
    def proto(self, proto):
        """Sets the proto of this DataForDescribeControlPolicyOutput.


        :param proto: The proto of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :type: str
        """

        self._proto = proto

    @property
    def repeat_days(self):
        """Gets the repeat_days of this DataForDescribeControlPolicyOutput.  # noqa: E501


        :return: The repeat_days of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :rtype: list[int]
        """
        return self._repeat_days

    @repeat_days.setter
    def repeat_days(self, repeat_days):
        """Sets the repeat_days of this DataForDescribeControlPolicyOutput.


        :param repeat_days: The repeat_days of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :type: list[int]
        """

        self._repeat_days = repeat_days

    @property
    def repeat_end_time(self):
        """Gets the repeat_end_time of this DataForDescribeControlPolicyOutput.  # noqa: E501


        :return: The repeat_end_time of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :rtype: str
        """
        return self._repeat_end_time

    @repeat_end_time.setter
    def repeat_end_time(self, repeat_end_time):
        """Sets the repeat_end_time of this DataForDescribeControlPolicyOutput.


        :param repeat_end_time: The repeat_end_time of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :type: str
        """

        self._repeat_end_time = repeat_end_time

    @property
    def repeat_start_time(self):
        """Gets the repeat_start_time of this DataForDescribeControlPolicyOutput.  # noqa: E501


        :return: The repeat_start_time of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :rtype: str
        """
        return self._repeat_start_time

    @repeat_start_time.setter
    def repeat_start_time(self, repeat_start_time):
        """Sets the repeat_start_time of this DataForDescribeControlPolicyOutput.


        :param repeat_start_time: The repeat_start_time of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :type: str
        """

        self._repeat_start_time = repeat_start_time

    @property
    def repeat_type(self):
        """Gets the repeat_type of this DataForDescribeControlPolicyOutput.  # noqa: E501


        :return: The repeat_type of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :rtype: str
        """
        return self._repeat_type

    @repeat_type.setter
    def repeat_type(self, repeat_type):
        """Sets the repeat_type of this DataForDescribeControlPolicyOutput.


        :param repeat_type: The repeat_type of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :type: str
        """

        self._repeat_type = repeat_type

    @property
    def rule_id(self):
        """Gets the rule_id of this DataForDescribeControlPolicyOutput.  # noqa: E501


        :return: The rule_id of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """Sets the rule_id of this DataForDescribeControlPolicyOutput.


        :param rule_id: The rule_id of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :type: str
        """

        self._rule_id = rule_id

    @property
    def source(self):
        """Gets the source of this DataForDescribeControlPolicyOutput.  # noqa: E501


        :return: The source of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this DataForDescribeControlPolicyOutput.


        :param source: The source of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def source_cidr_list(self):
        """Gets the source_cidr_list of this DataForDescribeControlPolicyOutput.  # noqa: E501


        :return: The source_cidr_list of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._source_cidr_list

    @source_cidr_list.setter
    def source_cidr_list(self, source_cidr_list):
        """Sets the source_cidr_list of this DataForDescribeControlPolicyOutput.


        :param source_cidr_list: The source_cidr_list of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :type: list[str]
        """

        self._source_cidr_list = source_cidr_list

    @property
    def source_group_type(self):
        """Gets the source_group_type of this DataForDescribeControlPolicyOutput.  # noqa: E501


        :return: The source_group_type of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :rtype: str
        """
        return self._source_group_type

    @source_group_type.setter
    def source_group_type(self, source_group_type):
        """Sets the source_group_type of this DataForDescribeControlPolicyOutput.


        :param source_group_type: The source_group_type of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :type: str
        """

        self._source_group_type = source_group_type

    @property
    def source_type(self):
        """Gets the source_type of this DataForDescribeControlPolicyOutput.  # noqa: E501


        :return: The source_type of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this DataForDescribeControlPolicyOutput.


        :param source_type: The source_type of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :type: str
        """

        self._source_type = source_type

    @property
    def start_time(self):
        """Gets the start_time of this DataForDescribeControlPolicyOutput.  # noqa: E501


        :return: The start_time of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this DataForDescribeControlPolicyOutput.


        :param start_time: The start_time of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :type: int
        """

        self._start_time = start_time

    @property
    def status(self):
        """Gets the status of this DataForDescribeControlPolicyOutput.  # noqa: E501


        :return: The status of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :rtype: bool
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DataForDescribeControlPolicyOutput.


        :param status: The status of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :type: bool
        """

        self._status = status

    @property
    def update_time(self):
        """Gets the update_time of this DataForDescribeControlPolicyOutput.  # noqa: E501


        :return: The update_time of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this DataForDescribeControlPolicyOutput.


        :param update_time: The update_time of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :type: int
        """

        self._update_time = update_time

    @property
    def use_count(self):
        """Gets the use_count of this DataForDescribeControlPolicyOutput.  # noqa: E501


        :return: The use_count of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :rtype: int
        """
        return self._use_count

    @use_count.setter
    def use_count(self, use_count):
        """Sets the use_count of this DataForDescribeControlPolicyOutput.


        :param use_count: The use_count of this DataForDescribeControlPolicyOutput.  # noqa: E501
        :type: int
        """

        self._use_count = use_count

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
        if issubclass(DataForDescribeControlPolicyOutput, dict):
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
        if not isinstance(other, DataForDescribeControlPolicyOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataForDescribeControlPolicyOutput):
            return True

        return self.to_dict() != other.to_dict()
