# coding: utf-8

"""
    redis

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeBigKeysRequest(object):
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
        'key_type': 'str',
        'order_by': 'str',
        'order_type': 'str',
        'page_size': 'int',
        'query_end_time': 'str',
        'query_start_time': 'str'
    }

    attribute_map = {
        'instance_id': 'InstanceId',
        'key_type': 'KeyType',
        'order_by': 'OrderBy',
        'order_type': 'OrderType',
        'page_size': 'PageSize',
        'query_end_time': 'QueryEndTime',
        'query_start_time': 'QueryStartTime'
    }

    def __init__(self, instance_id=None, key_type=None, order_by=None, order_type=None, page_size=None, query_end_time=None, query_start_time=None, _configuration=None):  # noqa: E501
        """DescribeBigKeysRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._instance_id = None
        self._key_type = None
        self._order_by = None
        self._order_type = None
        self._page_size = None
        self._query_end_time = None
        self._query_start_time = None
        self.discriminator = None

        self.instance_id = instance_id
        if key_type is not None:
            self.key_type = key_type
        if order_by is not None:
            self.order_by = order_by
        if order_type is not None:
            self.order_type = order_type
        self.page_size = page_size
        if query_end_time is not None:
            self.query_end_time = query_end_time
        if query_start_time is not None:
            self.query_start_time = query_start_time

    @property
    def instance_id(self):
        """Gets the instance_id of this DescribeBigKeysRequest.  # noqa: E501


        :return: The instance_id of this DescribeBigKeysRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this DescribeBigKeysRequest.


        :param instance_id: The instance_id of this DescribeBigKeysRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and instance_id is None:
            raise ValueError("Invalid value for `instance_id`, must not be `None`")  # noqa: E501

        self._instance_id = instance_id

    @property
    def key_type(self):
        """Gets the key_type of this DescribeBigKeysRequest.  # noqa: E501


        :return: The key_type of this DescribeBigKeysRequest.  # noqa: E501
        :rtype: str
        """
        return self._key_type

    @key_type.setter
    def key_type(self, key_type):
        """Sets the key_type of this DescribeBigKeysRequest.


        :param key_type: The key_type of this DescribeBigKeysRequest.  # noqa: E501
        :type: str
        """

        self._key_type = key_type

    @property
    def order_by(self):
        """Gets the order_by of this DescribeBigKeysRequest.  # noqa: E501


        :return: The order_by of this DescribeBigKeysRequest.  # noqa: E501
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        """Sets the order_by of this DescribeBigKeysRequest.


        :param order_by: The order_by of this DescribeBigKeysRequest.  # noqa: E501
        :type: str
        """

        self._order_by = order_by

    @property
    def order_type(self):
        """Gets the order_type of this DescribeBigKeysRequest.  # noqa: E501


        :return: The order_type of this DescribeBigKeysRequest.  # noqa: E501
        :rtype: str
        """
        return self._order_type

    @order_type.setter
    def order_type(self, order_type):
        """Sets the order_type of this DescribeBigKeysRequest.


        :param order_type: The order_type of this DescribeBigKeysRequest.  # noqa: E501
        :type: str
        """

        self._order_type = order_type

    @property
    def page_size(self):
        """Gets the page_size of this DescribeBigKeysRequest.  # noqa: E501


        :return: The page_size of this DescribeBigKeysRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this DescribeBigKeysRequest.


        :param page_size: The page_size of this DescribeBigKeysRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and page_size is None:
            raise ValueError("Invalid value for `page_size`, must not be `None`")  # noqa: E501

        self._page_size = page_size

    @property
    def query_end_time(self):
        """Gets the query_end_time of this DescribeBigKeysRequest.  # noqa: E501


        :return: The query_end_time of this DescribeBigKeysRequest.  # noqa: E501
        :rtype: str
        """
        return self._query_end_time

    @query_end_time.setter
    def query_end_time(self, query_end_time):
        """Sets the query_end_time of this DescribeBigKeysRequest.


        :param query_end_time: The query_end_time of this DescribeBigKeysRequest.  # noqa: E501
        :type: str
        """

        self._query_end_time = query_end_time

    @property
    def query_start_time(self):
        """Gets the query_start_time of this DescribeBigKeysRequest.  # noqa: E501


        :return: The query_start_time of this DescribeBigKeysRequest.  # noqa: E501
        :rtype: str
        """
        return self._query_start_time

    @query_start_time.setter
    def query_start_time(self, query_start_time):
        """Sets the query_start_time of this DescribeBigKeysRequest.


        :param query_start_time: The query_start_time of this DescribeBigKeysRequest.  # noqa: E501
        :type: str
        """

        self._query_start_time = query_start_time

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
        if issubclass(DescribeBigKeysRequest, dict):
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
        if not isinstance(other, DescribeBigKeysRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeBigKeysRequest):
            return True

        return self.to_dict() != other.to_dict()