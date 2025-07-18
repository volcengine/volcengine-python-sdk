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


class GetStreamRequest(object):
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
        'fresh_expired_pull': 'str',
        'fresh_expired_push': 'str',
        'space_id': 'str',
        'stream_id': 'str',
        'stream_name': 'str',
        'streaming_index': 'str'
    }

    attribute_map = {
        'fresh_expired_pull': 'FreshExpiredPull',
        'fresh_expired_push': 'FreshExpiredPush',
        'space_id': 'SpaceID',
        'stream_id': 'StreamID',
        'stream_name': 'StreamName',
        'streaming_index': 'StreamingIndex'
    }

    def __init__(self, fresh_expired_pull=None, fresh_expired_push=None, space_id=None, stream_id=None, stream_name=None, streaming_index=None, _configuration=None):  # noqa: E501
        """GetStreamRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._fresh_expired_pull = None
        self._fresh_expired_push = None
        self._space_id = None
        self._stream_id = None
        self._stream_name = None
        self._streaming_index = None
        self.discriminator = None

        if fresh_expired_pull is not None:
            self.fresh_expired_pull = fresh_expired_pull
        if fresh_expired_push is not None:
            self.fresh_expired_push = fresh_expired_push
        if space_id is not None:
            self.space_id = space_id
        if stream_id is not None:
            self.stream_id = stream_id
        if stream_name is not None:
            self.stream_name = stream_name
        self.streaming_index = streaming_index

    @property
    def fresh_expired_pull(self):
        """Gets the fresh_expired_pull of this GetStreamRequest.  # noqa: E501


        :return: The fresh_expired_pull of this GetStreamRequest.  # noqa: E501
        :rtype: str
        """
        return self._fresh_expired_pull

    @fresh_expired_pull.setter
    def fresh_expired_pull(self, fresh_expired_pull):
        """Sets the fresh_expired_pull of this GetStreamRequest.


        :param fresh_expired_pull: The fresh_expired_pull of this GetStreamRequest.  # noqa: E501
        :type: str
        """

        self._fresh_expired_pull = fresh_expired_pull

    @property
    def fresh_expired_push(self):
        """Gets the fresh_expired_push of this GetStreamRequest.  # noqa: E501


        :return: The fresh_expired_push of this GetStreamRequest.  # noqa: E501
        :rtype: str
        """
        return self._fresh_expired_push

    @fresh_expired_push.setter
    def fresh_expired_push(self, fresh_expired_push):
        """Sets the fresh_expired_push of this GetStreamRequest.


        :param fresh_expired_push: The fresh_expired_push of this GetStreamRequest.  # noqa: E501
        :type: str
        """

        self._fresh_expired_push = fresh_expired_push

    @property
    def space_id(self):
        """Gets the space_id of this GetStreamRequest.  # noqa: E501


        :return: The space_id of this GetStreamRequest.  # noqa: E501
        :rtype: str
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        """Sets the space_id of this GetStreamRequest.


        :param space_id: The space_id of this GetStreamRequest.  # noqa: E501
        :type: str
        """

        self._space_id = space_id

    @property
    def stream_id(self):
        """Gets the stream_id of this GetStreamRequest.  # noqa: E501


        :return: The stream_id of this GetStreamRequest.  # noqa: E501
        :rtype: str
        """
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id):
        """Sets the stream_id of this GetStreamRequest.


        :param stream_id: The stream_id of this GetStreamRequest.  # noqa: E501
        :type: str
        """

        self._stream_id = stream_id

    @property
    def stream_name(self):
        """Gets the stream_name of this GetStreamRequest.  # noqa: E501


        :return: The stream_name of this GetStreamRequest.  # noqa: E501
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        """Sets the stream_name of this GetStreamRequest.


        :param stream_name: The stream_name of this GetStreamRequest.  # noqa: E501
        :type: str
        """

        self._stream_name = stream_name

    @property
    def streaming_index(self):
        """Gets the streaming_index of this GetStreamRequest.  # noqa: E501


        :return: The streaming_index of this GetStreamRequest.  # noqa: E501
        :rtype: str
        """
        return self._streaming_index

    @streaming_index.setter
    def streaming_index(self, streaming_index):
        """Sets the streaming_index of this GetStreamRequest.


        :param streaming_index: The streaming_index of this GetStreamRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and streaming_index is None:
            raise ValueError("Invalid value for `streaming_index`, must not be `None`")  # noqa: E501

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
        if issubclass(GetStreamRequest, dict):
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
        if not isinstance(other, GetStreamRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetStreamRequest):
            return True

        return self.to_dict() != other.to_dict()
