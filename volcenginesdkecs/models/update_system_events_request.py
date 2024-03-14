# coding: utf-8

"""
    ecs

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class UpdateSystemEventsRequest(object):
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
        'event_ids': 'list[str]',
        'operated_end_at': 'str',
        'operated_start_at': 'str',
        'status': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'event_ids': 'EventIds',
        'operated_end_at': 'OperatedEndAt',
        'operated_start_at': 'OperatedStartAt',
        'status': 'Status',
        'updated_at': 'UpdatedAt'
    }

    def __init__(self, event_ids=None, operated_end_at=None, operated_start_at=None, status=None, updated_at=None, _configuration=None):  # noqa: E501
        """UpdateSystemEventsRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._event_ids = None
        self._operated_end_at = None
        self._operated_start_at = None
        self._status = None
        self._updated_at = None
        self.discriminator = None

        if event_ids is not None:
            self.event_ids = event_ids
        if operated_end_at is not None:
            self.operated_end_at = operated_end_at
        if operated_start_at is not None:
            self.operated_start_at = operated_start_at
        self.status = status
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def event_ids(self):
        """Gets the event_ids of this UpdateSystemEventsRequest.  # noqa: E501


        :return: The event_ids of this UpdateSystemEventsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._event_ids

    @event_ids.setter
    def event_ids(self, event_ids):
        """Sets the event_ids of this UpdateSystemEventsRequest.


        :param event_ids: The event_ids of this UpdateSystemEventsRequest.  # noqa: E501
        :type: list[str]
        """

        self._event_ids = event_ids

    @property
    def operated_end_at(self):
        """Gets the operated_end_at of this UpdateSystemEventsRequest.  # noqa: E501


        :return: The operated_end_at of this UpdateSystemEventsRequest.  # noqa: E501
        :rtype: str
        """
        return self._operated_end_at

    @operated_end_at.setter
    def operated_end_at(self, operated_end_at):
        """Sets the operated_end_at of this UpdateSystemEventsRequest.


        :param operated_end_at: The operated_end_at of this UpdateSystemEventsRequest.  # noqa: E501
        :type: str
        """

        self._operated_end_at = operated_end_at

    @property
    def operated_start_at(self):
        """Gets the operated_start_at of this UpdateSystemEventsRequest.  # noqa: E501


        :return: The operated_start_at of this UpdateSystemEventsRequest.  # noqa: E501
        :rtype: str
        """
        return self._operated_start_at

    @operated_start_at.setter
    def operated_start_at(self, operated_start_at):
        """Sets the operated_start_at of this UpdateSystemEventsRequest.


        :param operated_start_at: The operated_start_at of this UpdateSystemEventsRequest.  # noqa: E501
        :type: str
        """

        self._operated_start_at = operated_start_at

    @property
    def status(self):
        """Gets the status of this UpdateSystemEventsRequest.  # noqa: E501


        :return: The status of this UpdateSystemEventsRequest.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateSystemEventsRequest.


        :param status: The status of this UpdateSystemEventsRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def updated_at(self):
        """Gets the updated_at of this UpdateSystemEventsRequest.  # noqa: E501


        :return: The updated_at of this UpdateSystemEventsRequest.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this UpdateSystemEventsRequest.


        :param updated_at: The updated_at of this UpdateSystemEventsRequest.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

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
        if issubclass(UpdateSystemEventsRequest, dict):
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
        if not isinstance(other, UpdateSystemEventsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateSystemEventsRequest):
            return True

        return self.to_dict() != other.to_dict()
