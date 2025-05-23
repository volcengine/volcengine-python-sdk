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


class QueryMessageByOffsetRequest(object):
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
        'broker_name': 'str',
        'instance_id': 'str',
        'need_body': 'bool',
        'offset': 'str',
        'queue_id': 'int',
        'topic_name': 'str'
    }

    attribute_map = {
        'broker_name': 'BrokerName',
        'instance_id': 'InstanceId',
        'need_body': 'NeedBody',
        'offset': 'Offset',
        'queue_id': 'QueueId',
        'topic_name': 'TopicName'
    }

    def __init__(self, broker_name=None, instance_id=None, need_body=None, offset=None, queue_id=None, topic_name=None, _configuration=None):  # noqa: E501
        """QueryMessageByOffsetRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._broker_name = None
        self._instance_id = None
        self._need_body = None
        self._offset = None
        self._queue_id = None
        self._topic_name = None
        self.discriminator = None

        self.broker_name = broker_name
        self.instance_id = instance_id
        self.need_body = need_body
        self.offset = offset
        self.queue_id = queue_id
        self.topic_name = topic_name

    @property
    def broker_name(self):
        """Gets the broker_name of this QueryMessageByOffsetRequest.  # noqa: E501


        :return: The broker_name of this QueryMessageByOffsetRequest.  # noqa: E501
        :rtype: str
        """
        return self._broker_name

    @broker_name.setter
    def broker_name(self, broker_name):
        """Sets the broker_name of this QueryMessageByOffsetRequest.


        :param broker_name: The broker_name of this QueryMessageByOffsetRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and broker_name is None:
            raise ValueError("Invalid value for `broker_name`, must not be `None`")  # noqa: E501

        self._broker_name = broker_name

    @property
    def instance_id(self):
        """Gets the instance_id of this QueryMessageByOffsetRequest.  # noqa: E501


        :return: The instance_id of this QueryMessageByOffsetRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this QueryMessageByOffsetRequest.


        :param instance_id: The instance_id of this QueryMessageByOffsetRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and instance_id is None:
            raise ValueError("Invalid value for `instance_id`, must not be `None`")  # noqa: E501

        self._instance_id = instance_id

    @property
    def need_body(self):
        """Gets the need_body of this QueryMessageByOffsetRequest.  # noqa: E501


        :return: The need_body of this QueryMessageByOffsetRequest.  # noqa: E501
        :rtype: bool
        """
        return self._need_body

    @need_body.setter
    def need_body(self, need_body):
        """Sets the need_body of this QueryMessageByOffsetRequest.


        :param need_body: The need_body of this QueryMessageByOffsetRequest.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and need_body is None:
            raise ValueError("Invalid value for `need_body`, must not be `None`")  # noqa: E501

        self._need_body = need_body

    @property
    def offset(self):
        """Gets the offset of this QueryMessageByOffsetRequest.  # noqa: E501


        :return: The offset of this QueryMessageByOffsetRequest.  # noqa: E501
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this QueryMessageByOffsetRequest.


        :param offset: The offset of this QueryMessageByOffsetRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and offset is None:
            raise ValueError("Invalid value for `offset`, must not be `None`")  # noqa: E501

        self._offset = offset

    @property
    def queue_id(self):
        """Gets the queue_id of this QueryMessageByOffsetRequest.  # noqa: E501


        :return: The queue_id of this QueryMessageByOffsetRequest.  # noqa: E501
        :rtype: int
        """
        return self._queue_id

    @queue_id.setter
    def queue_id(self, queue_id):
        """Sets the queue_id of this QueryMessageByOffsetRequest.


        :param queue_id: The queue_id of this QueryMessageByOffsetRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and queue_id is None:
            raise ValueError("Invalid value for `queue_id`, must not be `None`")  # noqa: E501

        self._queue_id = queue_id

    @property
    def topic_name(self):
        """Gets the topic_name of this QueryMessageByOffsetRequest.  # noqa: E501


        :return: The topic_name of this QueryMessageByOffsetRequest.  # noqa: E501
        :rtype: str
        """
        return self._topic_name

    @topic_name.setter
    def topic_name(self, topic_name):
        """Sets the topic_name of this QueryMessageByOffsetRequest.


        :param topic_name: The topic_name of this QueryMessageByOffsetRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and topic_name is None:
            raise ValueError("Invalid value for `topic_name`, must not be `None`")  # noqa: E501

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
        if issubclass(QueryMessageByOffsetRequest, dict):
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
        if not isinstance(other, QueryMessageByOffsetRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QueryMessageByOffsetRequest):
            return True

        return self.to_dict() != other.to_dict()
