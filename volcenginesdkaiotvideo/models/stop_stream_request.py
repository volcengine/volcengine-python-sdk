# coding: utf-8

"""
    aiotvideo

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class StopStreamRequest(object):
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
        'is_smart': 'bool',
        'resolution': 'str',
        'space_id': 'str',
        'stream_id': 'str',
        'streaming_index': 'int'
    }

    attribute_map = {
        'is_smart': 'IsSmart',
        'resolution': 'Resolution',
        'space_id': 'SpaceID',
        'stream_id': 'StreamID',
        'streaming_index': 'StreamingIndex'
    }

    def __init__(self, is_smart=None, resolution=None, space_id=None, stream_id=None, streaming_index=None, _configuration=None):  # noqa: E501
        """StopStreamRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._is_smart = None
        self._resolution = None
        self._space_id = None
        self._stream_id = None
        self._streaming_index = None
        self.discriminator = None

        if is_smart is not None:
            self.is_smart = is_smart
        if resolution is not None:
            self.resolution = resolution
        if space_id is not None:
            self.space_id = space_id
        self.stream_id = stream_id
        if streaming_index is not None:
            self.streaming_index = streaming_index

    @property
    def is_smart(self):
        """Gets the is_smart of this StopStreamRequest.  # noqa: E501


        :return: The is_smart of this StopStreamRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_smart

    @is_smart.setter
    def is_smart(self, is_smart):
        """Sets the is_smart of this StopStreamRequest.


        :param is_smart: The is_smart of this StopStreamRequest.  # noqa: E501
        :type: bool
        """

        self._is_smart = is_smart

    @property
    def resolution(self):
        """Gets the resolution of this StopStreamRequest.  # noqa: E501


        :return: The resolution of this StopStreamRequest.  # noqa: E501
        :rtype: str
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """Sets the resolution of this StopStreamRequest.


        :param resolution: The resolution of this StopStreamRequest.  # noqa: E501
        :type: str
        """

        self._resolution = resolution

    @property
    def space_id(self):
        """Gets the space_id of this StopStreamRequest.  # noqa: E501


        :return: The space_id of this StopStreamRequest.  # noqa: E501
        :rtype: str
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        """Sets the space_id of this StopStreamRequest.


        :param space_id: The space_id of this StopStreamRequest.  # noqa: E501
        :type: str
        """

        self._space_id = space_id

    @property
    def stream_id(self):
        """Gets the stream_id of this StopStreamRequest.  # noqa: E501


        :return: The stream_id of this StopStreamRequest.  # noqa: E501
        :rtype: str
        """
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id):
        """Sets the stream_id of this StopStreamRequest.


        :param stream_id: The stream_id of this StopStreamRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and stream_id is None:
            raise ValueError("Invalid value for `stream_id`, must not be `None`")  # noqa: E501

        self._stream_id = stream_id

    @property
    def streaming_index(self):
        """Gets the streaming_index of this StopStreamRequest.  # noqa: E501


        :return: The streaming_index of this StopStreamRequest.  # noqa: E501
        :rtype: int
        """
        return self._streaming_index

    @streaming_index.setter
    def streaming_index(self, streaming_index):
        """Sets the streaming_index of this StopStreamRequest.


        :param streaming_index: The streaming_index of this StopStreamRequest.  # noqa: E501
        :type: int
        """

        self._streaming_index = streaming_index

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
        if issubclass(StopStreamRequest, dict):
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
        if not isinstance(other, StopStreamRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StopStreamRequest):
            return True

        return self.to_dict() != other.to_dict()
