# coding: utf-8

"""
    vmp

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ItemForListAlertsOutput(object):
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
        'alerting_rule_id': 'str',
        'alerting_rule_query': 'AlertingRuleQueryForListAlertsOutput',
        'alerting_rule_type': 'str',
        'current_level': 'str',
        'current_phase': 'str',
        'id': 'str',
        'initial_alert_timestamp': 'str',
        'last_alert_timestamp': 'str',
        'levels': 'list[LevelForListAlertsOutput]',
        'resolve_timestamp': 'str',
        'resource': 'ResourceForListAlertsOutput'
    }

    attribute_map = {
        'alerting_rule_id': 'AlertingRuleId',
        'alerting_rule_query': 'AlertingRuleQuery',
        'alerting_rule_type': 'AlertingRuleType',
        'current_level': 'CurrentLevel',
        'current_phase': 'CurrentPhase',
        'id': 'Id',
        'initial_alert_timestamp': 'InitialAlertTimestamp',
        'last_alert_timestamp': 'LastAlertTimestamp',
        'levels': 'Levels',
        'resolve_timestamp': 'ResolveTimestamp',
        'resource': 'Resource'
    }

    def __init__(self, alerting_rule_id=None, alerting_rule_query=None, alerting_rule_type=None, current_level=None, current_phase=None, id=None, initial_alert_timestamp=None, last_alert_timestamp=None, levels=None, resolve_timestamp=None, resource=None, _configuration=None):  # noqa: E501
        """ItemForListAlertsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._alerting_rule_id = None
        self._alerting_rule_query = None
        self._alerting_rule_type = None
        self._current_level = None
        self._current_phase = None
        self._id = None
        self._initial_alert_timestamp = None
        self._last_alert_timestamp = None
        self._levels = None
        self._resolve_timestamp = None
        self._resource = None
        self.discriminator = None

        if alerting_rule_id is not None:
            self.alerting_rule_id = alerting_rule_id
        if alerting_rule_query is not None:
            self.alerting_rule_query = alerting_rule_query
        if alerting_rule_type is not None:
            self.alerting_rule_type = alerting_rule_type
        if current_level is not None:
            self.current_level = current_level
        if current_phase is not None:
            self.current_phase = current_phase
        if id is not None:
            self.id = id
        if initial_alert_timestamp is not None:
            self.initial_alert_timestamp = initial_alert_timestamp
        if last_alert_timestamp is not None:
            self.last_alert_timestamp = last_alert_timestamp
        if levels is not None:
            self.levels = levels
        if resolve_timestamp is not None:
            self.resolve_timestamp = resolve_timestamp
        if resource is not None:
            self.resource = resource

    @property
    def alerting_rule_id(self):
        """Gets the alerting_rule_id of this ItemForListAlertsOutput.  # noqa: E501


        :return: The alerting_rule_id of this ItemForListAlertsOutput.  # noqa: E501
        :rtype: str
        """
        return self._alerting_rule_id

    @alerting_rule_id.setter
    def alerting_rule_id(self, alerting_rule_id):
        """Sets the alerting_rule_id of this ItemForListAlertsOutput.


        :param alerting_rule_id: The alerting_rule_id of this ItemForListAlertsOutput.  # noqa: E501
        :type: str
        """

        self._alerting_rule_id = alerting_rule_id

    @property
    def alerting_rule_query(self):
        """Gets the alerting_rule_query of this ItemForListAlertsOutput.  # noqa: E501


        :return: The alerting_rule_query of this ItemForListAlertsOutput.  # noqa: E501
        :rtype: AlertingRuleQueryForListAlertsOutput
        """
        return self._alerting_rule_query

    @alerting_rule_query.setter
    def alerting_rule_query(self, alerting_rule_query):
        """Sets the alerting_rule_query of this ItemForListAlertsOutput.


        :param alerting_rule_query: The alerting_rule_query of this ItemForListAlertsOutput.  # noqa: E501
        :type: AlertingRuleQueryForListAlertsOutput
        """

        self._alerting_rule_query = alerting_rule_query

    @property
    def alerting_rule_type(self):
        """Gets the alerting_rule_type of this ItemForListAlertsOutput.  # noqa: E501


        :return: The alerting_rule_type of this ItemForListAlertsOutput.  # noqa: E501
        :rtype: str
        """
        return self._alerting_rule_type

    @alerting_rule_type.setter
    def alerting_rule_type(self, alerting_rule_type):
        """Sets the alerting_rule_type of this ItemForListAlertsOutput.


        :param alerting_rule_type: The alerting_rule_type of this ItemForListAlertsOutput.  # noqa: E501
        :type: str
        """

        self._alerting_rule_type = alerting_rule_type

    @property
    def current_level(self):
        """Gets the current_level of this ItemForListAlertsOutput.  # noqa: E501


        :return: The current_level of this ItemForListAlertsOutput.  # noqa: E501
        :rtype: str
        """
        return self._current_level

    @current_level.setter
    def current_level(self, current_level):
        """Sets the current_level of this ItemForListAlertsOutput.


        :param current_level: The current_level of this ItemForListAlertsOutput.  # noqa: E501
        :type: str
        """

        self._current_level = current_level

    @property
    def current_phase(self):
        """Gets the current_phase of this ItemForListAlertsOutput.  # noqa: E501


        :return: The current_phase of this ItemForListAlertsOutput.  # noqa: E501
        :rtype: str
        """
        return self._current_phase

    @current_phase.setter
    def current_phase(self, current_phase):
        """Sets the current_phase of this ItemForListAlertsOutput.


        :param current_phase: The current_phase of this ItemForListAlertsOutput.  # noqa: E501
        :type: str
        """

        self._current_phase = current_phase

    @property
    def id(self):
        """Gets the id of this ItemForListAlertsOutput.  # noqa: E501


        :return: The id of this ItemForListAlertsOutput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ItemForListAlertsOutput.


        :param id: The id of this ItemForListAlertsOutput.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def initial_alert_timestamp(self):
        """Gets the initial_alert_timestamp of this ItemForListAlertsOutput.  # noqa: E501


        :return: The initial_alert_timestamp of this ItemForListAlertsOutput.  # noqa: E501
        :rtype: str
        """
        return self._initial_alert_timestamp

    @initial_alert_timestamp.setter
    def initial_alert_timestamp(self, initial_alert_timestamp):
        """Sets the initial_alert_timestamp of this ItemForListAlertsOutput.


        :param initial_alert_timestamp: The initial_alert_timestamp of this ItemForListAlertsOutput.  # noqa: E501
        :type: str
        """

        self._initial_alert_timestamp = initial_alert_timestamp

    @property
    def last_alert_timestamp(self):
        """Gets the last_alert_timestamp of this ItemForListAlertsOutput.  # noqa: E501


        :return: The last_alert_timestamp of this ItemForListAlertsOutput.  # noqa: E501
        :rtype: str
        """
        return self._last_alert_timestamp

    @last_alert_timestamp.setter
    def last_alert_timestamp(self, last_alert_timestamp):
        """Sets the last_alert_timestamp of this ItemForListAlertsOutput.


        :param last_alert_timestamp: The last_alert_timestamp of this ItemForListAlertsOutput.  # noqa: E501
        :type: str
        """

        self._last_alert_timestamp = last_alert_timestamp

    @property
    def levels(self):
        """Gets the levels of this ItemForListAlertsOutput.  # noqa: E501


        :return: The levels of this ItemForListAlertsOutput.  # noqa: E501
        :rtype: list[LevelForListAlertsOutput]
        """
        return self._levels

    @levels.setter
    def levels(self, levels):
        """Sets the levels of this ItemForListAlertsOutput.


        :param levels: The levels of this ItemForListAlertsOutput.  # noqa: E501
        :type: list[LevelForListAlertsOutput]
        """

        self._levels = levels

    @property
    def resolve_timestamp(self):
        """Gets the resolve_timestamp of this ItemForListAlertsOutput.  # noqa: E501


        :return: The resolve_timestamp of this ItemForListAlertsOutput.  # noqa: E501
        :rtype: str
        """
        return self._resolve_timestamp

    @resolve_timestamp.setter
    def resolve_timestamp(self, resolve_timestamp):
        """Sets the resolve_timestamp of this ItemForListAlertsOutput.


        :param resolve_timestamp: The resolve_timestamp of this ItemForListAlertsOutput.  # noqa: E501
        :type: str
        """

        self._resolve_timestamp = resolve_timestamp

    @property
    def resource(self):
        """Gets the resource of this ItemForListAlertsOutput.  # noqa: E501


        :return: The resource of this ItemForListAlertsOutput.  # noqa: E501
        :rtype: ResourceForListAlertsOutput
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this ItemForListAlertsOutput.


        :param resource: The resource of this ItemForListAlertsOutput.  # noqa: E501
        :type: ResourceForListAlertsOutput
        """

        self._resource = resource

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
        if issubclass(ItemForListAlertsOutput, dict):
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
        if not isinstance(other, ItemForListAlertsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ItemForListAlertsOutput):
            return True

        return self.to_dict() != other.to_dict()
