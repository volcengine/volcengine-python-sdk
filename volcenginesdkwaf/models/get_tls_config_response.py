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


class GetTLSConfigResponse(object):
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
        'alarm_threshold': 'int',
        'capacity_alert': 'bool',
        'capacity_alert_interval': 'int',
        'domain_list': 'list[str]',
        'field_list': 'FieldListForGetTLSConfigOutput',
        'field_select_all': 'bool',
        'project_id': 'str',
        'project_name': 'str',
        'tls_region': 'str',
        'tls_storage_time': 'int',
        'tls_total_capacity': 'int',
        'tls_total_usage': 'int',
        'topic_id': 'str',
        'topic_name': 'str',
        'total_domain_list': 'list[str]',
        'waf_action_list': 'WafActionListForGetTLSConfigOutput',
        'waf_action_select_all': 'bool'
    }

    attribute_map = {
        'alarm_threshold': 'AlarmThreshold',
        'capacity_alert': 'CapacityAlert',
        'capacity_alert_interval': 'CapacityAlertInterval',
        'domain_list': 'DomainList',
        'field_list': 'FieldList',
        'field_select_all': 'FieldSelectAll',
        'project_id': 'ProjectID',
        'project_name': 'ProjectName',
        'tls_region': 'TLSRegion',
        'tls_storage_time': 'TLSStorageTime',
        'tls_total_capacity': 'TLSTotalCapacity',
        'tls_total_usage': 'TLSTotalUsage',
        'topic_id': 'TopicID',
        'topic_name': 'TopicName',
        'total_domain_list': 'TotalDomainList',
        'waf_action_list': 'WafActionList',
        'waf_action_select_all': 'WafActionSelectAll'
    }

    def __init__(self, alarm_threshold=None, capacity_alert=None, capacity_alert_interval=None, domain_list=None, field_list=None, field_select_all=None, project_id=None, project_name=None, tls_region=None, tls_storage_time=None, tls_total_capacity=None, tls_total_usage=None, topic_id=None, topic_name=None, total_domain_list=None, waf_action_list=None, waf_action_select_all=None, _configuration=None):  # noqa: E501
        """GetTLSConfigResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._alarm_threshold = None
        self._capacity_alert = None
        self._capacity_alert_interval = None
        self._domain_list = None
        self._field_list = None
        self._field_select_all = None
        self._project_id = None
        self._project_name = None
        self._tls_region = None
        self._tls_storage_time = None
        self._tls_total_capacity = None
        self._tls_total_usage = None
        self._topic_id = None
        self._topic_name = None
        self._total_domain_list = None
        self._waf_action_list = None
        self._waf_action_select_all = None
        self.discriminator = None

        if alarm_threshold is not None:
            self.alarm_threshold = alarm_threshold
        if capacity_alert is not None:
            self.capacity_alert = capacity_alert
        if capacity_alert_interval is not None:
            self.capacity_alert_interval = capacity_alert_interval
        if domain_list is not None:
            self.domain_list = domain_list
        if field_list is not None:
            self.field_list = field_list
        if field_select_all is not None:
            self.field_select_all = field_select_all
        if project_id is not None:
            self.project_id = project_id
        if project_name is not None:
            self.project_name = project_name
        if tls_region is not None:
            self.tls_region = tls_region
        if tls_storage_time is not None:
            self.tls_storage_time = tls_storage_time
        if tls_total_capacity is not None:
            self.tls_total_capacity = tls_total_capacity
        if tls_total_usage is not None:
            self.tls_total_usage = tls_total_usage
        if topic_id is not None:
            self.topic_id = topic_id
        if topic_name is not None:
            self.topic_name = topic_name
        if total_domain_list is not None:
            self.total_domain_list = total_domain_list
        if waf_action_list is not None:
            self.waf_action_list = waf_action_list
        if waf_action_select_all is not None:
            self.waf_action_select_all = waf_action_select_all

    @property
    def alarm_threshold(self):
        """Gets the alarm_threshold of this GetTLSConfigResponse.  # noqa: E501


        :return: The alarm_threshold of this GetTLSConfigResponse.  # noqa: E501
        :rtype: int
        """
        return self._alarm_threshold

    @alarm_threshold.setter
    def alarm_threshold(self, alarm_threshold):
        """Sets the alarm_threshold of this GetTLSConfigResponse.


        :param alarm_threshold: The alarm_threshold of this GetTLSConfigResponse.  # noqa: E501
        :type: int
        """

        self._alarm_threshold = alarm_threshold

    @property
    def capacity_alert(self):
        """Gets the capacity_alert of this GetTLSConfigResponse.  # noqa: E501


        :return: The capacity_alert of this GetTLSConfigResponse.  # noqa: E501
        :rtype: bool
        """
        return self._capacity_alert

    @capacity_alert.setter
    def capacity_alert(self, capacity_alert):
        """Sets the capacity_alert of this GetTLSConfigResponse.


        :param capacity_alert: The capacity_alert of this GetTLSConfigResponse.  # noqa: E501
        :type: bool
        """

        self._capacity_alert = capacity_alert

    @property
    def capacity_alert_interval(self):
        """Gets the capacity_alert_interval of this GetTLSConfigResponse.  # noqa: E501


        :return: The capacity_alert_interval of this GetTLSConfigResponse.  # noqa: E501
        :rtype: int
        """
        return self._capacity_alert_interval

    @capacity_alert_interval.setter
    def capacity_alert_interval(self, capacity_alert_interval):
        """Sets the capacity_alert_interval of this GetTLSConfigResponse.


        :param capacity_alert_interval: The capacity_alert_interval of this GetTLSConfigResponse.  # noqa: E501
        :type: int
        """

        self._capacity_alert_interval = capacity_alert_interval

    @property
    def domain_list(self):
        """Gets the domain_list of this GetTLSConfigResponse.  # noqa: E501


        :return: The domain_list of this GetTLSConfigResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._domain_list

    @domain_list.setter
    def domain_list(self, domain_list):
        """Sets the domain_list of this GetTLSConfigResponse.


        :param domain_list: The domain_list of this GetTLSConfigResponse.  # noqa: E501
        :type: list[str]
        """

        self._domain_list = domain_list

    @property
    def field_list(self):
        """Gets the field_list of this GetTLSConfigResponse.  # noqa: E501


        :return: The field_list of this GetTLSConfigResponse.  # noqa: E501
        :rtype: FieldListForGetTLSConfigOutput
        """
        return self._field_list

    @field_list.setter
    def field_list(self, field_list):
        """Sets the field_list of this GetTLSConfigResponse.


        :param field_list: The field_list of this GetTLSConfigResponse.  # noqa: E501
        :type: FieldListForGetTLSConfigOutput
        """

        self._field_list = field_list

    @property
    def field_select_all(self):
        """Gets the field_select_all of this GetTLSConfigResponse.  # noqa: E501


        :return: The field_select_all of this GetTLSConfigResponse.  # noqa: E501
        :rtype: bool
        """
        return self._field_select_all

    @field_select_all.setter
    def field_select_all(self, field_select_all):
        """Sets the field_select_all of this GetTLSConfigResponse.


        :param field_select_all: The field_select_all of this GetTLSConfigResponse.  # noqa: E501
        :type: bool
        """

        self._field_select_all = field_select_all

    @property
    def project_id(self):
        """Gets the project_id of this GetTLSConfigResponse.  # noqa: E501


        :return: The project_id of this GetTLSConfigResponse.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this GetTLSConfigResponse.


        :param project_id: The project_id of this GetTLSConfigResponse.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def project_name(self):
        """Gets the project_name of this GetTLSConfigResponse.  # noqa: E501


        :return: The project_name of this GetTLSConfigResponse.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this GetTLSConfigResponse.


        :param project_name: The project_name of this GetTLSConfigResponse.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def tls_region(self):
        """Gets the tls_region of this GetTLSConfigResponse.  # noqa: E501


        :return: The tls_region of this GetTLSConfigResponse.  # noqa: E501
        :rtype: str
        """
        return self._tls_region

    @tls_region.setter
    def tls_region(self, tls_region):
        """Sets the tls_region of this GetTLSConfigResponse.


        :param tls_region: The tls_region of this GetTLSConfigResponse.  # noqa: E501
        :type: str
        """

        self._tls_region = tls_region

    @property
    def tls_storage_time(self):
        """Gets the tls_storage_time of this GetTLSConfigResponse.  # noqa: E501


        :return: The tls_storage_time of this GetTLSConfigResponse.  # noqa: E501
        :rtype: int
        """
        return self._tls_storage_time

    @tls_storage_time.setter
    def tls_storage_time(self, tls_storage_time):
        """Sets the tls_storage_time of this GetTLSConfigResponse.


        :param tls_storage_time: The tls_storage_time of this GetTLSConfigResponse.  # noqa: E501
        :type: int
        """

        self._tls_storage_time = tls_storage_time

    @property
    def tls_total_capacity(self):
        """Gets the tls_total_capacity of this GetTLSConfigResponse.  # noqa: E501


        :return: The tls_total_capacity of this GetTLSConfigResponse.  # noqa: E501
        :rtype: int
        """
        return self._tls_total_capacity

    @tls_total_capacity.setter
    def tls_total_capacity(self, tls_total_capacity):
        """Sets the tls_total_capacity of this GetTLSConfigResponse.


        :param tls_total_capacity: The tls_total_capacity of this GetTLSConfigResponse.  # noqa: E501
        :type: int
        """

        self._tls_total_capacity = tls_total_capacity

    @property
    def tls_total_usage(self):
        """Gets the tls_total_usage of this GetTLSConfigResponse.  # noqa: E501


        :return: The tls_total_usage of this GetTLSConfigResponse.  # noqa: E501
        :rtype: int
        """
        return self._tls_total_usage

    @tls_total_usage.setter
    def tls_total_usage(self, tls_total_usage):
        """Sets the tls_total_usage of this GetTLSConfigResponse.


        :param tls_total_usage: The tls_total_usage of this GetTLSConfigResponse.  # noqa: E501
        :type: int
        """

        self._tls_total_usage = tls_total_usage

    @property
    def topic_id(self):
        """Gets the topic_id of this GetTLSConfigResponse.  # noqa: E501


        :return: The topic_id of this GetTLSConfigResponse.  # noqa: E501
        :rtype: str
        """
        return self._topic_id

    @topic_id.setter
    def topic_id(self, topic_id):
        """Sets the topic_id of this GetTLSConfigResponse.


        :param topic_id: The topic_id of this GetTLSConfigResponse.  # noqa: E501
        :type: str
        """

        self._topic_id = topic_id

    @property
    def topic_name(self):
        """Gets the topic_name of this GetTLSConfigResponse.  # noqa: E501


        :return: The topic_name of this GetTLSConfigResponse.  # noqa: E501
        :rtype: str
        """
        return self._topic_name

    @topic_name.setter
    def topic_name(self, topic_name):
        """Sets the topic_name of this GetTLSConfigResponse.


        :param topic_name: The topic_name of this GetTLSConfigResponse.  # noqa: E501
        :type: str
        """

        self._topic_name = topic_name

    @property
    def total_domain_list(self):
        """Gets the total_domain_list of this GetTLSConfigResponse.  # noqa: E501


        :return: The total_domain_list of this GetTLSConfigResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._total_domain_list

    @total_domain_list.setter
    def total_domain_list(self, total_domain_list):
        """Sets the total_domain_list of this GetTLSConfigResponse.


        :param total_domain_list: The total_domain_list of this GetTLSConfigResponse.  # noqa: E501
        :type: list[str]
        """

        self._total_domain_list = total_domain_list

    @property
    def waf_action_list(self):
        """Gets the waf_action_list of this GetTLSConfigResponse.  # noqa: E501


        :return: The waf_action_list of this GetTLSConfigResponse.  # noqa: E501
        :rtype: WafActionListForGetTLSConfigOutput
        """
        return self._waf_action_list

    @waf_action_list.setter
    def waf_action_list(self, waf_action_list):
        """Sets the waf_action_list of this GetTLSConfigResponse.


        :param waf_action_list: The waf_action_list of this GetTLSConfigResponse.  # noqa: E501
        :type: WafActionListForGetTLSConfigOutput
        """

        self._waf_action_list = waf_action_list

    @property
    def waf_action_select_all(self):
        """Gets the waf_action_select_all of this GetTLSConfigResponse.  # noqa: E501


        :return: The waf_action_select_all of this GetTLSConfigResponse.  # noqa: E501
        :rtype: bool
        """
        return self._waf_action_select_all

    @waf_action_select_all.setter
    def waf_action_select_all(self, waf_action_select_all):
        """Sets the waf_action_select_all of this GetTLSConfigResponse.


        :param waf_action_select_all: The waf_action_select_all of this GetTLSConfigResponse.  # noqa: E501
        :type: bool
        """

        self._waf_action_select_all = waf_action_select_all

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
        if issubclass(GetTLSConfigResponse, dict):
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
        if not isinstance(other, GetTLSConfigResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetTLSConfigResponse):
            return True

        return self.to_dict() != other.to_dict()
