# coding: utf-8

"""
    rds_mysql_v2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeFailoverLogsRequest(object):
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
        'end_time': 'str',
        'instance_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'start_time': 'str'
    }

    attribute_map = {
        'end_time': 'EndTime',
        'instance_id': 'InstanceId',
        'limit': 'Limit',
        'offset': 'Offset',
        'start_time': 'StartTime'
    }

    def __init__(self, end_time=None, instance_id=None, limit=None, offset=None, start_time=None, _configuration=None):  # noqa: E501
        """DescribeFailoverLogsRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._end_time = None
        self._instance_id = None
        self._limit = None
        self._offset = None
        self._start_time = None
        self.discriminator = None

        if end_time is not None:
            self.end_time = end_time
        self.instance_id = instance_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if start_time is not None:
            self.start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this DescribeFailoverLogsRequest.  # noqa: E501


        :return: The end_time of this DescribeFailoverLogsRequest.  # noqa: E501
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this DescribeFailoverLogsRequest.


        :param end_time: The end_time of this DescribeFailoverLogsRequest.  # noqa: E501
        :type: str
        """

        self._end_time = end_time

    @property
    def instance_id(self):
        """Gets the instance_id of this DescribeFailoverLogsRequest.  # noqa: E501


        :return: The instance_id of this DescribeFailoverLogsRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this DescribeFailoverLogsRequest.


        :param instance_id: The instance_id of this DescribeFailoverLogsRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and instance_id is None:
            raise ValueError("Invalid value for `instance_id`, must not be `None`")  # noqa: E501

        self._instance_id = instance_id

    @property
    def limit(self):
        """Gets the limit of this DescribeFailoverLogsRequest.  # noqa: E501


        :return: The limit of this DescribeFailoverLogsRequest.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this DescribeFailoverLogsRequest.


        :param limit: The limit of this DescribeFailoverLogsRequest.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this DescribeFailoverLogsRequest.  # noqa: E501


        :return: The offset of this DescribeFailoverLogsRequest.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this DescribeFailoverLogsRequest.


        :param offset: The offset of this DescribeFailoverLogsRequest.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def start_time(self):
        """Gets the start_time of this DescribeFailoverLogsRequest.  # noqa: E501


        :return: The start_time of this DescribeFailoverLogsRequest.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this DescribeFailoverLogsRequest.


        :param start_time: The start_time of this DescribeFailoverLogsRequest.  # noqa: E501
        :type: str
        """

        self._start_time = start_time

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
        if issubclass(DescribeFailoverLogsRequest, dict):
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
        if not isinstance(other, DescribeFailoverLogsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeFailoverLogsRequest):
            return True

        return self.to_dict() != other.to_dict()
