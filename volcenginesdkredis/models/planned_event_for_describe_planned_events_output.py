# coding: utf-8

"""
    redis

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class PlannedEventForDescribePlannedEventsOutput(object):
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
        'action_name': 'str',
        'can_cancel': 'bool',
        'can_modify_time': 'bool',
        'event_id': 'str',
        'instance_id': 'str',
        'instance_name': 'str',
        'max_end_time': 'str',
        'plan_end_time': 'str',
        'plan_start_time': 'str',
        'status': 'str',
        'type': 'str'
    }

    attribute_map = {
        'action_name': 'ActionName',
        'can_cancel': 'CanCancel',
        'can_modify_time': 'CanModifyTime',
        'event_id': 'EventId',
        'instance_id': 'InstanceId',
        'instance_name': 'InstanceName',
        'max_end_time': 'MaxEndTime',
        'plan_end_time': 'PlanEndTime',
        'plan_start_time': 'PlanStartTime',
        'status': 'Status',
        'type': 'Type'
    }

    def __init__(self, action_name=None, can_cancel=None, can_modify_time=None, event_id=None, instance_id=None, instance_name=None, max_end_time=None, plan_end_time=None, plan_start_time=None, status=None, type=None, _configuration=None):  # noqa: E501
        """PlannedEventForDescribePlannedEventsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._action_name = None
        self._can_cancel = None
        self._can_modify_time = None
        self._event_id = None
        self._instance_id = None
        self._instance_name = None
        self._max_end_time = None
        self._plan_end_time = None
        self._plan_start_time = None
        self._status = None
        self._type = None
        self.discriminator = None

        if action_name is not None:
            self.action_name = action_name
        if can_cancel is not None:
            self.can_cancel = can_cancel
        if can_modify_time is not None:
            self.can_modify_time = can_modify_time
        if event_id is not None:
            self.event_id = event_id
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if max_end_time is not None:
            self.max_end_time = max_end_time
        if plan_end_time is not None:
            self.plan_end_time = plan_end_time
        if plan_start_time is not None:
            self.plan_start_time = plan_start_time
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type

    @property
    def action_name(self):
        """Gets the action_name of this PlannedEventForDescribePlannedEventsOutput.  # noqa: E501


        :return: The action_name of this PlannedEventForDescribePlannedEventsOutput.  # noqa: E501
        :rtype: str
        """
        return self._action_name

    @action_name.setter
    def action_name(self, action_name):
        """Sets the action_name of this PlannedEventForDescribePlannedEventsOutput.


        :param action_name: The action_name of this PlannedEventForDescribePlannedEventsOutput.  # noqa: E501
        :type: str
        """

        self._action_name = action_name

    @property
    def can_cancel(self):
        """Gets the can_cancel of this PlannedEventForDescribePlannedEventsOutput.  # noqa: E501


        :return: The can_cancel of this PlannedEventForDescribePlannedEventsOutput.  # noqa: E501
        :rtype: bool
        """
        return self._can_cancel

    @can_cancel.setter
    def can_cancel(self, can_cancel):
        """Sets the can_cancel of this PlannedEventForDescribePlannedEventsOutput.


        :param can_cancel: The can_cancel of this PlannedEventForDescribePlannedEventsOutput.  # noqa: E501
        :type: bool
        """

        self._can_cancel = can_cancel

    @property
    def can_modify_time(self):
        """Gets the can_modify_time of this PlannedEventForDescribePlannedEventsOutput.  # noqa: E501


        :return: The can_modify_time of this PlannedEventForDescribePlannedEventsOutput.  # noqa: E501
        :rtype: bool
        """
        return self._can_modify_time

    @can_modify_time.setter
    def can_modify_time(self, can_modify_time):
        """Sets the can_modify_time of this PlannedEventForDescribePlannedEventsOutput.


        :param can_modify_time: The can_modify_time of this PlannedEventForDescribePlannedEventsOutput.  # noqa: E501
        :type: bool
        """

        self._can_modify_time = can_modify_time

    @property
    def event_id(self):
        """Gets the event_id of this PlannedEventForDescribePlannedEventsOutput.  # noqa: E501


        :return: The event_id of this PlannedEventForDescribePlannedEventsOutput.  # noqa: E501
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this PlannedEventForDescribePlannedEventsOutput.


        :param event_id: The event_id of this PlannedEventForDescribePlannedEventsOutput.  # noqa: E501
        :type: str
        """

        self._event_id = event_id

    @property
    def instance_id(self):
        """Gets the instance_id of this PlannedEventForDescribePlannedEventsOutput.  # noqa: E501


        :return: The instance_id of this PlannedEventForDescribePlannedEventsOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this PlannedEventForDescribePlannedEventsOutput.


        :param instance_id: The instance_id of this PlannedEventForDescribePlannedEventsOutput.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def instance_name(self):
        """Gets the instance_name of this PlannedEventForDescribePlannedEventsOutput.  # noqa: E501


        :return: The instance_name of this PlannedEventForDescribePlannedEventsOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this PlannedEventForDescribePlannedEventsOutput.


        :param instance_name: The instance_name of this PlannedEventForDescribePlannedEventsOutput.  # noqa: E501
        :type: str
        """

        self._instance_name = instance_name

    @property
    def max_end_time(self):
        """Gets the max_end_time of this PlannedEventForDescribePlannedEventsOutput.  # noqa: E501


        :return: The max_end_time of this PlannedEventForDescribePlannedEventsOutput.  # noqa: E501
        :rtype: str
        """
        return self._max_end_time

    @max_end_time.setter
    def max_end_time(self, max_end_time):
        """Sets the max_end_time of this PlannedEventForDescribePlannedEventsOutput.


        :param max_end_time: The max_end_time of this PlannedEventForDescribePlannedEventsOutput.  # noqa: E501
        :type: str
        """

        self._max_end_time = max_end_time

    @property
    def plan_end_time(self):
        """Gets the plan_end_time of this PlannedEventForDescribePlannedEventsOutput.  # noqa: E501


        :return: The plan_end_time of this PlannedEventForDescribePlannedEventsOutput.  # noqa: E501
        :rtype: str
        """
        return self._plan_end_time

    @plan_end_time.setter
    def plan_end_time(self, plan_end_time):
        """Sets the plan_end_time of this PlannedEventForDescribePlannedEventsOutput.


        :param plan_end_time: The plan_end_time of this PlannedEventForDescribePlannedEventsOutput.  # noqa: E501
        :type: str
        """

        self._plan_end_time = plan_end_time

    @property
    def plan_start_time(self):
        """Gets the plan_start_time of this PlannedEventForDescribePlannedEventsOutput.  # noqa: E501


        :return: The plan_start_time of this PlannedEventForDescribePlannedEventsOutput.  # noqa: E501
        :rtype: str
        """
        return self._plan_start_time

    @plan_start_time.setter
    def plan_start_time(self, plan_start_time):
        """Sets the plan_start_time of this PlannedEventForDescribePlannedEventsOutput.


        :param plan_start_time: The plan_start_time of this PlannedEventForDescribePlannedEventsOutput.  # noqa: E501
        :type: str
        """

        self._plan_start_time = plan_start_time

    @property
    def status(self):
        """Gets the status of this PlannedEventForDescribePlannedEventsOutput.  # noqa: E501


        :return: The status of this PlannedEventForDescribePlannedEventsOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PlannedEventForDescribePlannedEventsOutput.


        :param status: The status of this PlannedEventForDescribePlannedEventsOutput.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def type(self):
        """Gets the type of this PlannedEventForDescribePlannedEventsOutput.  # noqa: E501


        :return: The type of this PlannedEventForDescribePlannedEventsOutput.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PlannedEventForDescribePlannedEventsOutput.


        :param type: The type of this PlannedEventForDescribePlannedEventsOutput.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(PlannedEventForDescribePlannedEventsOutput, dict):
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
        if not isinstance(other, PlannedEventForDescribePlannedEventsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PlannedEventForDescribePlannedEventsOutput):
            return True

        return self.to_dict() != other.to_dict()
