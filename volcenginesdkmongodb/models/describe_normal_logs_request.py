# coding: utf-8

"""
    mongodb

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeNormalLogsRequest(object):
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
        'context': 'str',
        'end_time': 'int',
        'instance_id': 'str',
        'limit': 'int',
        'log_level': 'str',
        'pod_name': 'str',
        'sort': 'str',
        'start_time': 'int'
    }

    attribute_map = {
        'context': 'Context',
        'end_time': 'EndTime',
        'instance_id': 'InstanceId',
        'limit': 'Limit',
        'log_level': 'LogLevel',
        'pod_name': 'PodName',
        'sort': 'Sort',
        'start_time': 'StartTime'
    }

    def __init__(self, context=None, end_time=None, instance_id=None, limit=None, log_level=None, pod_name=None, sort=None, start_time=None, _configuration=None):  # noqa: E501
        """DescribeNormalLogsRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._context = None
        self._end_time = None
        self._instance_id = None
        self._limit = None
        self._log_level = None
        self._pod_name = None
        self._sort = None
        self._start_time = None
        self.discriminator = None

        if context is not None:
            self.context = context
        self.end_time = end_time
        self.instance_id = instance_id
        self.limit = limit
        if log_level is not None:
            self.log_level = log_level
        self.pod_name = pod_name
        if sort is not None:
            self.sort = sort
        self.start_time = start_time

    @property
    def context(self):
        """Gets the context of this DescribeNormalLogsRequest.  # noqa: E501


        :return: The context of this DescribeNormalLogsRequest.  # noqa: E501
        :rtype: str
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this DescribeNormalLogsRequest.


        :param context: The context of this DescribeNormalLogsRequest.  # noqa: E501
        :type: str
        """

        self._context = context

    @property
    def end_time(self):
        """Gets the end_time of this DescribeNormalLogsRequest.  # noqa: E501


        :return: The end_time of this DescribeNormalLogsRequest.  # noqa: E501
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this DescribeNormalLogsRequest.


        :param end_time: The end_time of this DescribeNormalLogsRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and end_time is None:
            raise ValueError("Invalid value for `end_time`, must not be `None`")  # noqa: E501

        self._end_time = end_time

    @property
    def instance_id(self):
        """Gets the instance_id of this DescribeNormalLogsRequest.  # noqa: E501


        :return: The instance_id of this DescribeNormalLogsRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this DescribeNormalLogsRequest.


        :param instance_id: The instance_id of this DescribeNormalLogsRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and instance_id is None:
            raise ValueError("Invalid value for `instance_id`, must not be `None`")  # noqa: E501

        self._instance_id = instance_id

    @property
    def limit(self):
        """Gets the limit of this DescribeNormalLogsRequest.  # noqa: E501


        :return: The limit of this DescribeNormalLogsRequest.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this DescribeNormalLogsRequest.


        :param limit: The limit of this DescribeNormalLogsRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and limit is None:
            raise ValueError("Invalid value for `limit`, must not be `None`")  # noqa: E501

        self._limit = limit

    @property
    def log_level(self):
        """Gets the log_level of this DescribeNormalLogsRequest.  # noqa: E501


        :return: The log_level of this DescribeNormalLogsRequest.  # noqa: E501
        :rtype: str
        """
        return self._log_level

    @log_level.setter
    def log_level(self, log_level):
        """Sets the log_level of this DescribeNormalLogsRequest.


        :param log_level: The log_level of this DescribeNormalLogsRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["ErrorLog", "RunningLog"]  # noqa: E501
        if (self._configuration.client_side_validation and
                log_level not in allowed_values):
            raise ValueError(
                "Invalid value for `log_level` ({0}), must be one of {1}"  # noqa: E501
                .format(log_level, allowed_values)
            )

        self._log_level = log_level

    @property
    def pod_name(self):
        """Gets the pod_name of this DescribeNormalLogsRequest.  # noqa: E501


        :return: The pod_name of this DescribeNormalLogsRequest.  # noqa: E501
        :rtype: str
        """
        return self._pod_name

    @pod_name.setter
    def pod_name(self, pod_name):
        """Sets the pod_name of this DescribeNormalLogsRequest.


        :param pod_name: The pod_name of this DescribeNormalLogsRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and pod_name is None:
            raise ValueError("Invalid value for `pod_name`, must not be `None`")  # noqa: E501

        self._pod_name = pod_name

    @property
    def sort(self):
        """Gets the sort of this DescribeNormalLogsRequest.  # noqa: E501


        :return: The sort of this DescribeNormalLogsRequest.  # noqa: E501
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this DescribeNormalLogsRequest.


        :param sort: The sort of this DescribeNormalLogsRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["ASC", "DESC"]  # noqa: E501
        if (self._configuration.client_side_validation and
                sort not in allowed_values):
            raise ValueError(
                "Invalid value for `sort` ({0}), must be one of {1}"  # noqa: E501
                .format(sort, allowed_values)
            )

        self._sort = sort

    @property
    def start_time(self):
        """Gets the start_time of this DescribeNormalLogsRequest.  # noqa: E501


        :return: The start_time of this DescribeNormalLogsRequest.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this DescribeNormalLogsRequest.


        :param start_time: The start_time of this DescribeNormalLogsRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and start_time is None:
            raise ValueError("Invalid value for `start_time`, must not be `None`")  # noqa: E501

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
        if issubclass(DescribeNormalLogsRequest, dict):
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
        if not isinstance(other, DescribeNormalLogsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeNormalLogsRequest):
            return True

        return self.to_dict() != other.to_dict()
