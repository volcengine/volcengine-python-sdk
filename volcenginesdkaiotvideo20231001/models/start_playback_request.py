# coding: utf-8

"""
    aiotvideo20231001

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class StartPlaybackRequest(object):
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
        'end_time': 'int',
        'space_id': 'str',
        'start_time': 'int',
        'stream_id': 'str'
    }

    attribute_map = {
        'end_time': 'EndTime',
        'space_id': 'SpaceID',
        'start_time': 'StartTime',
        'stream_id': 'StreamID'
    }

    def __init__(self, end_time=None, space_id=None, start_time=None, stream_id=None, _configuration=None):  # noqa: E501
        """StartPlaybackRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._end_time = None
        self._space_id = None
        self._start_time = None
        self._stream_id = None
        self.discriminator = None

        self.end_time = end_time
        if space_id is not None:
            self.space_id = space_id
        self.start_time = start_time
        self.stream_id = stream_id

    @property
    def end_time(self):
        """Gets the end_time of this StartPlaybackRequest.  # noqa: E501


        :return: The end_time of this StartPlaybackRequest.  # noqa: E501
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this StartPlaybackRequest.


        :param end_time: The end_time of this StartPlaybackRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and end_time is None:
            raise ValueError("Invalid value for `end_time`, must not be `None`")  # noqa: E501

        self._end_time = end_time

    @property
    def space_id(self):
        """Gets the space_id of this StartPlaybackRequest.  # noqa: E501


        :return: The space_id of this StartPlaybackRequest.  # noqa: E501
        :rtype: str
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        """Sets the space_id of this StartPlaybackRequest.


        :param space_id: The space_id of this StartPlaybackRequest.  # noqa: E501
        :type: str
        """

        self._space_id = space_id

    @property
    def start_time(self):
        """Gets the start_time of this StartPlaybackRequest.  # noqa: E501


        :return: The start_time of this StartPlaybackRequest.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this StartPlaybackRequest.


        :param start_time: The start_time of this StartPlaybackRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and start_time is None:
            raise ValueError("Invalid value for `start_time`, must not be `None`")  # noqa: E501

        self._start_time = start_time

    @property
    def stream_id(self):
        """Gets the stream_id of this StartPlaybackRequest.  # noqa: E501


        :return: The stream_id of this StartPlaybackRequest.  # noqa: E501
        :rtype: str
        """
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id):
        """Sets the stream_id of this StartPlaybackRequest.


        :param stream_id: The stream_id of this StartPlaybackRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and stream_id is None:
            raise ValueError("Invalid value for `stream_id`, must not be `None`")  # noqa: E501

        self._stream_id = stream_id

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
        if issubclass(StartPlaybackRequest, dict):
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
        if not isinstance(other, StartPlaybackRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StartPlaybackRequest):
            return True

        return self.to_dict() != other.to_dict()
