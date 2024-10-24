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


class DescribeTopicsRequest(object):
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
        'message_type': 'int',
        'page_number': 'int',
        'page_size': 'int',
        'sort_by': 'str',
        'sort_order': 'str',
        'topic_name': 'str'
    }

    attribute_map = {
        'instance_id': 'InstanceId',
        'message_type': 'MessageType',
        'page_number': 'PageNumber',
        'page_size': 'PageSize',
        'sort_by': 'SortBy',
        'sort_order': 'SortOrder',
        'topic_name': 'TopicName'
    }

    def __init__(self, instance_id=None, message_type=None, page_number=None, page_size=None, sort_by=None, sort_order=None, topic_name=None, _configuration=None):  # noqa: E501
        """DescribeTopicsRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._instance_id = None
        self._message_type = None
        self._page_number = None
        self._page_size = None
        self._sort_by = None
        self._sort_order = None
        self._topic_name = None
        self.discriminator = None

        self.instance_id = instance_id
        if message_type is not None:
            self.message_type = message_type
        self.page_number = page_number
        self.page_size = page_size
        if sort_by is not None:
            self.sort_by = sort_by
        if sort_order is not None:
            self.sort_order = sort_order
        if topic_name is not None:
            self.topic_name = topic_name

    @property
    def instance_id(self):
        """Gets the instance_id of this DescribeTopicsRequest.  # noqa: E501


        :return: The instance_id of this DescribeTopicsRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this DescribeTopicsRequest.


        :param instance_id: The instance_id of this DescribeTopicsRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and instance_id is None:
            raise ValueError("Invalid value for `instance_id`, must not be `None`")  # noqa: E501

        self._instance_id = instance_id

    @property
    def message_type(self):
        """Gets the message_type of this DescribeTopicsRequest.  # noqa: E501


        :return: The message_type of this DescribeTopicsRequest.  # noqa: E501
        :rtype: int
        """
        return self._message_type

    @message_type.setter
    def message_type(self, message_type):
        """Sets the message_type of this DescribeTopicsRequest.


        :param message_type: The message_type of this DescribeTopicsRequest.  # noqa: E501
        :type: int
        """

        self._message_type = message_type

    @property
    def page_number(self):
        """Gets the page_number of this DescribeTopicsRequest.  # noqa: E501


        :return: The page_number of this DescribeTopicsRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this DescribeTopicsRequest.


        :param page_number: The page_number of this DescribeTopicsRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and page_number is None:
            raise ValueError("Invalid value for `page_number`, must not be `None`")  # noqa: E501

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this DescribeTopicsRequest.  # noqa: E501


        :return: The page_size of this DescribeTopicsRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this DescribeTopicsRequest.


        :param page_size: The page_size of this DescribeTopicsRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and page_size is None:
            raise ValueError("Invalid value for `page_size`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                page_size is not None and page_size > 100):  # noqa: E501
            raise ValueError("Invalid value for `page_size`, must be a value less than or equal to `100`")  # noqa: E501
        if (self._configuration.client_side_validation and
                page_size is not None and page_size < 1):  # noqa: E501
            raise ValueError("Invalid value for `page_size`, must be a value greater than or equal to `1`")  # noqa: E501

        self._page_size = page_size

    @property
    def sort_by(self):
        """Gets the sort_by of this DescribeTopicsRequest.  # noqa: E501


        :return: The sort_by of this DescribeTopicsRequest.  # noqa: E501
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        """Sets the sort_by of this DescribeTopicsRequest.


        :param sort_by: The sort_by of this DescribeTopicsRequest.  # noqa: E501
        :type: str
        """

        self._sort_by = sort_by

    @property
    def sort_order(self):
        """Gets the sort_order of this DescribeTopicsRequest.  # noqa: E501


        :return: The sort_order of this DescribeTopicsRequest.  # noqa: E501
        :rtype: str
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this DescribeTopicsRequest.


        :param sort_order: The sort_order of this DescribeTopicsRequest.  # noqa: E501
        :type: str
        """

        self._sort_order = sort_order

    @property
    def topic_name(self):
        """Gets the topic_name of this DescribeTopicsRequest.  # noqa: E501


        :return: The topic_name of this DescribeTopicsRequest.  # noqa: E501
        :rtype: str
        """
        return self._topic_name

    @topic_name.setter
    def topic_name(self, topic_name):
        """Sets the topic_name of this DescribeTopicsRequest.


        :param topic_name: The topic_name of this DescribeTopicsRequest.  # noqa: E501
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
        if issubclass(DescribeTopicsRequest, dict):
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
        if not isinstance(other, DescribeTopicsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeTopicsRequest):
            return True

        return self.to_dict() != other.to_dict()
