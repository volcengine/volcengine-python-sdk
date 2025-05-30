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


class ListMlpAlarmTagsRequest(object):
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
        'alarm_id_list': 'str',
        'alarm_type': 'str',
        'alert_tags': 'str',
        'top_group_id': 'str'
    }

    attribute_map = {
        'alarm_id_list': 'AlarmIDList',
        'alarm_type': 'AlarmType',
        'alert_tags': 'AlertTags',
        'top_group_id': 'TopGroupID'
    }

    def __init__(self, alarm_id_list=None, alarm_type=None, alert_tags=None, top_group_id=None, _configuration=None):  # noqa: E501
        """ListMlpAlarmTagsRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._alarm_id_list = None
        self._alarm_type = None
        self._alert_tags = None
        self._top_group_id = None
        self.discriminator = None

        if alarm_id_list is not None:
            self.alarm_id_list = alarm_id_list
        if alarm_type is not None:
            self.alarm_type = alarm_type
        if alert_tags is not None:
            self.alert_tags = alert_tags
        if top_group_id is not None:
            self.top_group_id = top_group_id

    @property
    def alarm_id_list(self):
        """Gets the alarm_id_list of this ListMlpAlarmTagsRequest.  # noqa: E501


        :return: The alarm_id_list of this ListMlpAlarmTagsRequest.  # noqa: E501
        :rtype: str
        """
        return self._alarm_id_list

    @alarm_id_list.setter
    def alarm_id_list(self, alarm_id_list):
        """Sets the alarm_id_list of this ListMlpAlarmTagsRequest.


        :param alarm_id_list: The alarm_id_list of this ListMlpAlarmTagsRequest.  # noqa: E501
        :type: str
        """

        self._alarm_id_list = alarm_id_list

    @property
    def alarm_type(self):
        """Gets the alarm_type of this ListMlpAlarmTagsRequest.  # noqa: E501


        :return: The alarm_type of this ListMlpAlarmTagsRequest.  # noqa: E501
        :rtype: str
        """
        return self._alarm_type

    @alarm_type.setter
    def alarm_type(self, alarm_type):
        """Sets the alarm_type of this ListMlpAlarmTagsRequest.


        :param alarm_type: The alarm_type of this ListMlpAlarmTagsRequest.  # noqa: E501
        :type: str
        """

        self._alarm_type = alarm_type

    @property
    def alert_tags(self):
        """Gets the alert_tags of this ListMlpAlarmTagsRequest.  # noqa: E501


        :return: The alert_tags of this ListMlpAlarmTagsRequest.  # noqa: E501
        :rtype: str
        """
        return self._alert_tags

    @alert_tags.setter
    def alert_tags(self, alert_tags):
        """Sets the alert_tags of this ListMlpAlarmTagsRequest.


        :param alert_tags: The alert_tags of this ListMlpAlarmTagsRequest.  # noqa: E501
        :type: str
        """

        self._alert_tags = alert_tags

    @property
    def top_group_id(self):
        """Gets the top_group_id of this ListMlpAlarmTagsRequest.  # noqa: E501


        :return: The top_group_id of this ListMlpAlarmTagsRequest.  # noqa: E501
        :rtype: str
        """
        return self._top_group_id

    @top_group_id.setter
    def top_group_id(self, top_group_id):
        """Sets the top_group_id of this ListMlpAlarmTagsRequest.


        :param top_group_id: The top_group_id of this ListMlpAlarmTagsRequest.  # noqa: E501
        :type: str
        """

        self._top_group_id = top_group_id

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
        if issubclass(ListMlpAlarmTagsRequest, dict):
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
        if not isinstance(other, ListMlpAlarmTagsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListMlpAlarmTagsRequest):
            return True

        return self.to_dict() != other.to_dict()
