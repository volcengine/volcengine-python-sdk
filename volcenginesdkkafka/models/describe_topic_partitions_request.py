# coding: utf-8

"""
    kafka

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeTopicPartitionsRequest(object):
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
        'instance_id': 'str',
        'page_number': 'int',
        'page_size': 'int',
        'partition_ids': 'list[int]',
        'topic_name': 'str',
        'under_insync_only': 'bool'
    }

    attribute_map = {
        'instance_id': 'InstanceId',
        'page_number': 'PageNumber',
        'page_size': 'PageSize',
        'partition_ids': 'PartitionIds',
        'topic_name': 'TopicName',
        'under_insync_only': 'UnderInsyncOnly'
    }

    def __init__(self, instance_id=None, page_number=None, page_size=None, partition_ids=None, topic_name=None, under_insync_only=None, _configuration=None):  # noqa: E501
        """DescribeTopicPartitionsRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._instance_id = None
        self._page_number = None
        self._page_size = None
        self._partition_ids = None
        self._topic_name = None
        self._under_insync_only = None
        self.discriminator = None

        self.instance_id = instance_id
        self.page_number = page_number
        self.page_size = page_size
        if partition_ids is not None:
            self.partition_ids = partition_ids
        self.topic_name = topic_name
        if under_insync_only is not None:
            self.under_insync_only = under_insync_only

    @property
    def instance_id(self):
        """Gets the instance_id of this DescribeTopicPartitionsRequest.  # noqa: E501


        :return: The instance_id of this DescribeTopicPartitionsRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this DescribeTopicPartitionsRequest.


        :param instance_id: The instance_id of this DescribeTopicPartitionsRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and instance_id is None:
            raise ValueError("Invalid value for `instance_id`, must not be `None`")  # noqa: E501

        self._instance_id = instance_id

    @property
    def page_number(self):
        """Gets the page_number of this DescribeTopicPartitionsRequest.  # noqa: E501


        :return: The page_number of this DescribeTopicPartitionsRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this DescribeTopicPartitionsRequest.


        :param page_number: The page_number of this DescribeTopicPartitionsRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and page_number is None:
            raise ValueError("Invalid value for `page_number`, must not be `None`")  # noqa: E501

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this DescribeTopicPartitionsRequest.  # noqa: E501


        :return: The page_size of this DescribeTopicPartitionsRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this DescribeTopicPartitionsRequest.


        :param page_size: The page_size of this DescribeTopicPartitionsRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and page_size is None:
            raise ValueError("Invalid value for `page_size`, must not be `None`")  # noqa: E501

        self._page_size = page_size

    @property
    def partition_ids(self):
        """Gets the partition_ids of this DescribeTopicPartitionsRequest.  # noqa: E501


        :return: The partition_ids of this DescribeTopicPartitionsRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._partition_ids

    @partition_ids.setter
    def partition_ids(self, partition_ids):
        """Sets the partition_ids of this DescribeTopicPartitionsRequest.


        :param partition_ids: The partition_ids of this DescribeTopicPartitionsRequest.  # noqa: E501
        :type: list[int]
        """

        self._partition_ids = partition_ids

    @property
    def topic_name(self):
        """Gets the topic_name of this DescribeTopicPartitionsRequest.  # noqa: E501


        :return: The topic_name of this DescribeTopicPartitionsRequest.  # noqa: E501
        :rtype: str
        """
        return self._topic_name

    @topic_name.setter
    def topic_name(self, topic_name):
        """Sets the topic_name of this DescribeTopicPartitionsRequest.


        :param topic_name: The topic_name of this DescribeTopicPartitionsRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and topic_name is None:
            raise ValueError("Invalid value for `topic_name`, must not be `None`")  # noqa: E501

        self._topic_name = topic_name

    @property
    def under_insync_only(self):
        """Gets the under_insync_only of this DescribeTopicPartitionsRequest.  # noqa: E501


        :return: The under_insync_only of this DescribeTopicPartitionsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._under_insync_only

    @under_insync_only.setter
    def under_insync_only(self, under_insync_only):
        """Sets the under_insync_only of this DescribeTopicPartitionsRequest.


        :param under_insync_only: The under_insync_only of this DescribeTopicPartitionsRequest.  # noqa: E501
        :type: bool
        """

        self._under_insync_only = under_insync_only

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
        if issubclass(DescribeTopicPartitionsRequest, dict):
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
        if not isinstance(other, DescribeTopicPartitionsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeTopicPartitionsRequest):
            return True

        return self.to_dict() != other.to_dict()
