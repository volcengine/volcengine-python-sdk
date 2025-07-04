# coding: utf-8

"""
    livesaas

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class PollingChatAPIRequest(object):
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
        'activity_id': 'int',
        'audience_group_id': 'int',
        'chat_id': 'int',
        'count': 'int',
        'polling_type': 'int'
    }

    attribute_map = {
        'activity_id': 'ActivityId',
        'audience_group_id': 'AudienceGroupId',
        'chat_id': 'ChatId',
        'count': 'Count',
        'polling_type': 'PollingType'
    }

    def __init__(self, activity_id=None, audience_group_id=None, chat_id=None, count=None, polling_type=None, _configuration=None):  # noqa: E501
        """PollingChatAPIRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._activity_id = None
        self._audience_group_id = None
        self._chat_id = None
        self._count = None
        self._polling_type = None
        self.discriminator = None

        self.activity_id = activity_id
        if audience_group_id is not None:
            self.audience_group_id = audience_group_id
        self.chat_id = chat_id
        if count is not None:
            self.count = count
        if polling_type is not None:
            self.polling_type = polling_type

    @property
    def activity_id(self):
        """Gets the activity_id of this PollingChatAPIRequest.  # noqa: E501


        :return: The activity_id of this PollingChatAPIRequest.  # noqa: E501
        :rtype: int
        """
        return self._activity_id

    @activity_id.setter
    def activity_id(self, activity_id):
        """Sets the activity_id of this PollingChatAPIRequest.


        :param activity_id: The activity_id of this PollingChatAPIRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and activity_id is None:
            raise ValueError("Invalid value for `activity_id`, must not be `None`")  # noqa: E501

        self._activity_id = activity_id

    @property
    def audience_group_id(self):
        """Gets the audience_group_id of this PollingChatAPIRequest.  # noqa: E501


        :return: The audience_group_id of this PollingChatAPIRequest.  # noqa: E501
        :rtype: int
        """
        return self._audience_group_id

    @audience_group_id.setter
    def audience_group_id(self, audience_group_id):
        """Sets the audience_group_id of this PollingChatAPIRequest.


        :param audience_group_id: The audience_group_id of this PollingChatAPIRequest.  # noqa: E501
        :type: int
        """

        self._audience_group_id = audience_group_id

    @property
    def chat_id(self):
        """Gets the chat_id of this PollingChatAPIRequest.  # noqa: E501


        :return: The chat_id of this PollingChatAPIRequest.  # noqa: E501
        :rtype: int
        """
        return self._chat_id

    @chat_id.setter
    def chat_id(self, chat_id):
        """Sets the chat_id of this PollingChatAPIRequest.


        :param chat_id: The chat_id of this PollingChatAPIRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and chat_id is None:
            raise ValueError("Invalid value for `chat_id`, must not be `None`")  # noqa: E501

        self._chat_id = chat_id

    @property
    def count(self):
        """Gets the count of this PollingChatAPIRequest.  # noqa: E501


        :return: The count of this PollingChatAPIRequest.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this PollingChatAPIRequest.


        :param count: The count of this PollingChatAPIRequest.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def polling_type(self):
        """Gets the polling_type of this PollingChatAPIRequest.  # noqa: E501


        :return: The polling_type of this PollingChatAPIRequest.  # noqa: E501
        :rtype: int
        """
        return self._polling_type

    @polling_type.setter
    def polling_type(self, polling_type):
        """Sets the polling_type of this PollingChatAPIRequest.


        :param polling_type: The polling_type of this PollingChatAPIRequest.  # noqa: E501
        :type: int
        """

        self._polling_type = polling_type

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
        if issubclass(PollingChatAPIRequest, dict):
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
        if not isinstance(other, PollingChatAPIRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PollingChatAPIRequest):
            return True

        return self.to_dict() != other.to_dict()
