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


class AlarmContentForGetHidsAlarmSummaryInfoOutput(object):
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
        'alarm_node': 'AlarmNodeForGetHidsAlarmSummaryInfoOutput',
        'audit_log_alarm': 'AuditLogAlarmForGetHidsAlarmSummaryInfoOutput',
        'extend_info': 'ExtendInfoForGetHidsAlarmSummaryInfoOutput',
        'file_downloadable': 'bool',
        'kill_chain_node_list': 'list[KillChainNodeListForGetHidsAlarmSummaryInfoOutput]',
        'kill_chain_step_list': 'list[str]',
        'virus_hit_data_list': 'list[VirusHitDataListForGetHidsAlarmSummaryInfoOutput]'
    }

    attribute_map = {
        'alarm_node': 'AlarmNode',
        'audit_log_alarm': 'AuditLogAlarm',
        'extend_info': 'ExtendInfo',
        'file_downloadable': 'FileDownloadable',
        'kill_chain_node_list': 'KillChainNodeList',
        'kill_chain_step_list': 'KillChainStepList',
        'virus_hit_data_list': 'VirusHitDataList'
    }

    def __init__(self, alarm_node=None, audit_log_alarm=None, extend_info=None, file_downloadable=None, kill_chain_node_list=None, kill_chain_step_list=None, virus_hit_data_list=None, _configuration=None):  # noqa: E501
        """AlarmContentForGetHidsAlarmSummaryInfoOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._alarm_node = None
        self._audit_log_alarm = None
        self._extend_info = None
        self._file_downloadable = None
        self._kill_chain_node_list = None
        self._kill_chain_step_list = None
        self._virus_hit_data_list = None
        self.discriminator = None

        if alarm_node is not None:
            self.alarm_node = alarm_node
        if audit_log_alarm is not None:
            self.audit_log_alarm = audit_log_alarm
        if extend_info is not None:
            self.extend_info = extend_info
        if file_downloadable is not None:
            self.file_downloadable = file_downloadable
        if kill_chain_node_list is not None:
            self.kill_chain_node_list = kill_chain_node_list
        if kill_chain_step_list is not None:
            self.kill_chain_step_list = kill_chain_step_list
        if virus_hit_data_list is not None:
            self.virus_hit_data_list = virus_hit_data_list

    @property
    def alarm_node(self):
        """Gets the alarm_node of this AlarmContentForGetHidsAlarmSummaryInfoOutput.  # noqa: E501


        :return: The alarm_node of this AlarmContentForGetHidsAlarmSummaryInfoOutput.  # noqa: E501
        :rtype: AlarmNodeForGetHidsAlarmSummaryInfoOutput
        """
        return self._alarm_node

    @alarm_node.setter
    def alarm_node(self, alarm_node):
        """Sets the alarm_node of this AlarmContentForGetHidsAlarmSummaryInfoOutput.


        :param alarm_node: The alarm_node of this AlarmContentForGetHidsAlarmSummaryInfoOutput.  # noqa: E501
        :type: AlarmNodeForGetHidsAlarmSummaryInfoOutput
        """

        self._alarm_node = alarm_node

    @property
    def audit_log_alarm(self):
        """Gets the audit_log_alarm of this AlarmContentForGetHidsAlarmSummaryInfoOutput.  # noqa: E501


        :return: The audit_log_alarm of this AlarmContentForGetHidsAlarmSummaryInfoOutput.  # noqa: E501
        :rtype: AuditLogAlarmForGetHidsAlarmSummaryInfoOutput
        """
        return self._audit_log_alarm

    @audit_log_alarm.setter
    def audit_log_alarm(self, audit_log_alarm):
        """Sets the audit_log_alarm of this AlarmContentForGetHidsAlarmSummaryInfoOutput.


        :param audit_log_alarm: The audit_log_alarm of this AlarmContentForGetHidsAlarmSummaryInfoOutput.  # noqa: E501
        :type: AuditLogAlarmForGetHidsAlarmSummaryInfoOutput
        """

        self._audit_log_alarm = audit_log_alarm

    @property
    def extend_info(self):
        """Gets the extend_info of this AlarmContentForGetHidsAlarmSummaryInfoOutput.  # noqa: E501


        :return: The extend_info of this AlarmContentForGetHidsAlarmSummaryInfoOutput.  # noqa: E501
        :rtype: ExtendInfoForGetHidsAlarmSummaryInfoOutput
        """
        return self._extend_info

    @extend_info.setter
    def extend_info(self, extend_info):
        """Sets the extend_info of this AlarmContentForGetHidsAlarmSummaryInfoOutput.


        :param extend_info: The extend_info of this AlarmContentForGetHidsAlarmSummaryInfoOutput.  # noqa: E501
        :type: ExtendInfoForGetHidsAlarmSummaryInfoOutput
        """

        self._extend_info = extend_info

    @property
    def file_downloadable(self):
        """Gets the file_downloadable of this AlarmContentForGetHidsAlarmSummaryInfoOutput.  # noqa: E501


        :return: The file_downloadable of this AlarmContentForGetHidsAlarmSummaryInfoOutput.  # noqa: E501
        :rtype: bool
        """
        return self._file_downloadable

    @file_downloadable.setter
    def file_downloadable(self, file_downloadable):
        """Sets the file_downloadable of this AlarmContentForGetHidsAlarmSummaryInfoOutput.


        :param file_downloadable: The file_downloadable of this AlarmContentForGetHidsAlarmSummaryInfoOutput.  # noqa: E501
        :type: bool
        """

        self._file_downloadable = file_downloadable

    @property
    def kill_chain_node_list(self):
        """Gets the kill_chain_node_list of this AlarmContentForGetHidsAlarmSummaryInfoOutput.  # noqa: E501


        :return: The kill_chain_node_list of this AlarmContentForGetHidsAlarmSummaryInfoOutput.  # noqa: E501
        :rtype: list[KillChainNodeListForGetHidsAlarmSummaryInfoOutput]
        """
        return self._kill_chain_node_list

    @kill_chain_node_list.setter
    def kill_chain_node_list(self, kill_chain_node_list):
        """Sets the kill_chain_node_list of this AlarmContentForGetHidsAlarmSummaryInfoOutput.


        :param kill_chain_node_list: The kill_chain_node_list of this AlarmContentForGetHidsAlarmSummaryInfoOutput.  # noqa: E501
        :type: list[KillChainNodeListForGetHidsAlarmSummaryInfoOutput]
        """

        self._kill_chain_node_list = kill_chain_node_list

    @property
    def kill_chain_step_list(self):
        """Gets the kill_chain_step_list of this AlarmContentForGetHidsAlarmSummaryInfoOutput.  # noqa: E501


        :return: The kill_chain_step_list of this AlarmContentForGetHidsAlarmSummaryInfoOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._kill_chain_step_list

    @kill_chain_step_list.setter
    def kill_chain_step_list(self, kill_chain_step_list):
        """Sets the kill_chain_step_list of this AlarmContentForGetHidsAlarmSummaryInfoOutput.


        :param kill_chain_step_list: The kill_chain_step_list of this AlarmContentForGetHidsAlarmSummaryInfoOutput.  # noqa: E501
        :type: list[str]
        """

        self._kill_chain_step_list = kill_chain_step_list

    @property
    def virus_hit_data_list(self):
        """Gets the virus_hit_data_list of this AlarmContentForGetHidsAlarmSummaryInfoOutput.  # noqa: E501


        :return: The virus_hit_data_list of this AlarmContentForGetHidsAlarmSummaryInfoOutput.  # noqa: E501
        :rtype: list[VirusHitDataListForGetHidsAlarmSummaryInfoOutput]
        """
        return self._virus_hit_data_list

    @virus_hit_data_list.setter
    def virus_hit_data_list(self, virus_hit_data_list):
        """Sets the virus_hit_data_list of this AlarmContentForGetHidsAlarmSummaryInfoOutput.


        :param virus_hit_data_list: The virus_hit_data_list of this AlarmContentForGetHidsAlarmSummaryInfoOutput.  # noqa: E501
        :type: list[VirusHitDataListForGetHidsAlarmSummaryInfoOutput]
        """

        self._virus_hit_data_list = virus_hit_data_list

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
        if issubclass(AlarmContentForGetHidsAlarmSummaryInfoOutput, dict):
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
        if not isinstance(other, AlarmContentForGetHidsAlarmSummaryInfoOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AlarmContentForGetHidsAlarmSummaryInfoOutput):
            return True

        return self.to_dict() != other.to_dict()
