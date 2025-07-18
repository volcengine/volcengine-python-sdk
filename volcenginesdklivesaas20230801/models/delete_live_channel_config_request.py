# coding: utf-8

"""
    livesaas20230801

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DeleteLiveChannelConfigRequest(object):
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
        'line_id': 'int',
        'line_index': 'int'
    }

    attribute_map = {
        'activity_id': 'ActivityId',
        'line_id': 'LineId',
        'line_index': 'LineIndex'
    }

    def __init__(self, activity_id=None, line_id=None, line_index=None, _configuration=None):  # noqa: E501
        """DeleteLiveChannelConfigRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._activity_id = None
        self._line_id = None
        self._line_index = None
        self.discriminator = None

        self.activity_id = activity_id
        if line_id is not None:
            self.line_id = line_id
        if line_index is not None:
            self.line_index = line_index

    @property
    def activity_id(self):
        """Gets the activity_id of this DeleteLiveChannelConfigRequest.  # noqa: E501


        :return: The activity_id of this DeleteLiveChannelConfigRequest.  # noqa: E501
        :rtype: int
        """
        return self._activity_id

    @activity_id.setter
    def activity_id(self, activity_id):
        """Sets the activity_id of this DeleteLiveChannelConfigRequest.


        :param activity_id: The activity_id of this DeleteLiveChannelConfigRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and activity_id is None:
            raise ValueError("Invalid value for `activity_id`, must not be `None`")  # noqa: E501

        self._activity_id = activity_id

    @property
    def line_id(self):
        """Gets the line_id of this DeleteLiveChannelConfigRequest.  # noqa: E501


        :return: The line_id of this DeleteLiveChannelConfigRequest.  # noqa: E501
        :rtype: int
        """
        return self._line_id

    @line_id.setter
    def line_id(self, line_id):
        """Sets the line_id of this DeleteLiveChannelConfigRequest.


        :param line_id: The line_id of this DeleteLiveChannelConfigRequest.  # noqa: E501
        :type: int
        """

        self._line_id = line_id

    @property
    def line_index(self):
        """Gets the line_index of this DeleteLiveChannelConfigRequest.  # noqa: E501


        :return: The line_index of this DeleteLiveChannelConfigRequest.  # noqa: E501
        :rtype: int
        """
        return self._line_index

    @line_index.setter
    def line_index(self, line_index):
        """Sets the line_index of this DeleteLiveChannelConfigRequest.


        :param line_index: The line_index of this DeleteLiveChannelConfigRequest.  # noqa: E501
        :type: int
        """

        self._line_index = line_index

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
        if issubclass(DeleteLiveChannelConfigRequest, dict):
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
        if not isinstance(other, DeleteLiveChannelConfigRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeleteLiveChannelConfigRequest):
            return True

        return self.to_dict() != other.to_dict()
