# coding: utf-8

"""
    rocketmq

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class MessageListForQueryMessageByTimestampOutput(object):
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
        'body': 'str',
        'create_timestamp': 'int',
        'is_exist': 'bool',
        'message_id': 'str',
        'message_key': 'str',
        'message_size': 'int',
        'producer_host': 'str',
        'store_timestamp': 'int',
        'tag': 'str',
        'topic_name': 'str'
    }

    attribute_map = {
        'body': 'Body',
        'create_timestamp': 'CreateTimestamp',
        'is_exist': 'IsExist',
        'message_id': 'MessageId',
        'message_key': 'MessageKey',
        'message_size': 'MessageSize',
        'producer_host': 'ProducerHost',
        'store_timestamp': 'StoreTimestamp',
        'tag': 'Tag',
        'topic_name': 'TopicName'
    }

    def __init__(self, body=None, create_timestamp=None, is_exist=None, message_id=None, message_key=None, message_size=None, producer_host=None, store_timestamp=None, tag=None, topic_name=None, _configuration=None):  # noqa: E501
        """MessageListForQueryMessageByTimestampOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._body = None
        self._create_timestamp = None
        self._is_exist = None
        self._message_id = None
        self._message_key = None
        self._message_size = None
        self._producer_host = None
        self._store_timestamp = None
        self._tag = None
        self._topic_name = None
        self.discriminator = None

        if body is not None:
            self.body = body
        if create_timestamp is not None:
            self.create_timestamp = create_timestamp
        if is_exist is not None:
            self.is_exist = is_exist
        if message_id is not None:
            self.message_id = message_id
        if message_key is not None:
            self.message_key = message_key
        if message_size is not None:
            self.message_size = message_size
        if producer_host is not None:
            self.producer_host = producer_host
        if store_timestamp is not None:
            self.store_timestamp = store_timestamp
        if tag is not None:
            self.tag = tag
        if topic_name is not None:
            self.topic_name = topic_name

    @property
    def body(self):
        """Gets the body of this MessageListForQueryMessageByTimestampOutput.  # noqa: E501


        :return: The body of this MessageListForQueryMessageByTimestampOutput.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this MessageListForQueryMessageByTimestampOutput.


        :param body: The body of this MessageListForQueryMessageByTimestampOutput.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def create_timestamp(self):
        """Gets the create_timestamp of this MessageListForQueryMessageByTimestampOutput.  # noqa: E501


        :return: The create_timestamp of this MessageListForQueryMessageByTimestampOutput.  # noqa: E501
        :rtype: int
        """
        return self._create_timestamp

    @create_timestamp.setter
    def create_timestamp(self, create_timestamp):
        """Sets the create_timestamp of this MessageListForQueryMessageByTimestampOutput.


        :param create_timestamp: The create_timestamp of this MessageListForQueryMessageByTimestampOutput.  # noqa: E501
        :type: int
        """

        self._create_timestamp = create_timestamp

    @property
    def is_exist(self):
        """Gets the is_exist of this MessageListForQueryMessageByTimestampOutput.  # noqa: E501


        :return: The is_exist of this MessageListForQueryMessageByTimestampOutput.  # noqa: E501
        :rtype: bool
        """
        return self._is_exist

    @is_exist.setter
    def is_exist(self, is_exist):
        """Sets the is_exist of this MessageListForQueryMessageByTimestampOutput.


        :param is_exist: The is_exist of this MessageListForQueryMessageByTimestampOutput.  # noqa: E501
        :type: bool
        """

        self._is_exist = is_exist

    @property
    def message_id(self):
        """Gets the message_id of this MessageListForQueryMessageByTimestampOutput.  # noqa: E501


        :return: The message_id of this MessageListForQueryMessageByTimestampOutput.  # noqa: E501
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        """Sets the message_id of this MessageListForQueryMessageByTimestampOutput.


        :param message_id: The message_id of this MessageListForQueryMessageByTimestampOutput.  # noqa: E501
        :type: str
        """

        self._message_id = message_id

    @property
    def message_key(self):
        """Gets the message_key of this MessageListForQueryMessageByTimestampOutput.  # noqa: E501


        :return: The message_key of this MessageListForQueryMessageByTimestampOutput.  # noqa: E501
        :rtype: str
        """
        return self._message_key

    @message_key.setter
    def message_key(self, message_key):
        """Sets the message_key of this MessageListForQueryMessageByTimestampOutput.


        :param message_key: The message_key of this MessageListForQueryMessageByTimestampOutput.  # noqa: E501
        :type: str
        """

        self._message_key = message_key

    @property
    def message_size(self):
        """Gets the message_size of this MessageListForQueryMessageByTimestampOutput.  # noqa: E501


        :return: The message_size of this MessageListForQueryMessageByTimestampOutput.  # noqa: E501
        :rtype: int
        """
        return self._message_size

    @message_size.setter
    def message_size(self, message_size):
        """Sets the message_size of this MessageListForQueryMessageByTimestampOutput.


        :param message_size: The message_size of this MessageListForQueryMessageByTimestampOutput.  # noqa: E501
        :type: int
        """

        self._message_size = message_size

    @property
    def producer_host(self):
        """Gets the producer_host of this MessageListForQueryMessageByTimestampOutput.  # noqa: E501


        :return: The producer_host of this MessageListForQueryMessageByTimestampOutput.  # noqa: E501
        :rtype: str
        """
        return self._producer_host

    @producer_host.setter
    def producer_host(self, producer_host):
        """Sets the producer_host of this MessageListForQueryMessageByTimestampOutput.


        :param producer_host: The producer_host of this MessageListForQueryMessageByTimestampOutput.  # noqa: E501
        :type: str
        """

        self._producer_host = producer_host

    @property
    def store_timestamp(self):
        """Gets the store_timestamp of this MessageListForQueryMessageByTimestampOutput.  # noqa: E501


        :return: The store_timestamp of this MessageListForQueryMessageByTimestampOutput.  # noqa: E501
        :rtype: int
        """
        return self._store_timestamp

    @store_timestamp.setter
    def store_timestamp(self, store_timestamp):
        """Sets the store_timestamp of this MessageListForQueryMessageByTimestampOutput.


        :param store_timestamp: The store_timestamp of this MessageListForQueryMessageByTimestampOutput.  # noqa: E501
        :type: int
        """

        self._store_timestamp = store_timestamp

    @property
    def tag(self):
        """Gets the tag of this MessageListForQueryMessageByTimestampOutput.  # noqa: E501


        :return: The tag of this MessageListForQueryMessageByTimestampOutput.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this MessageListForQueryMessageByTimestampOutput.


        :param tag: The tag of this MessageListForQueryMessageByTimestampOutput.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def topic_name(self):
        """Gets the topic_name of this MessageListForQueryMessageByTimestampOutput.  # noqa: E501


        :return: The topic_name of this MessageListForQueryMessageByTimestampOutput.  # noqa: E501
        :rtype: str
        """
        return self._topic_name

    @topic_name.setter
    def topic_name(self, topic_name):
        """Sets the topic_name of this MessageListForQueryMessageByTimestampOutput.


        :param topic_name: The topic_name of this MessageListForQueryMessageByTimestampOutput.  # noqa: E501
        :type: str
        """

        self._topic_name = topic_name

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
        if issubclass(MessageListForQueryMessageByTimestampOutput, dict):
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
        if not isinstance(other, MessageListForQueryMessageByTimestampOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MessageListForQueryMessageByTimestampOutput):
            return True

        return self.to_dict() != other.to_dict()
