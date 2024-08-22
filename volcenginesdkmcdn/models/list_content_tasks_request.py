# coding: utf-8

"""
    mcdn

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ListContentTasksRequest(object):
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
        'domain': 'str',
        'end_time': 'int',
        'pagination': 'PaginationForListContentTasksInput',
        'start_time': 'int',
        'task_id': 'str',
        'task_status': 'str',
        'task_type': 'str',
        'url': 'str'
    }

    attribute_map = {
        'domain': 'Domain',
        'end_time': 'EndTime',
        'pagination': 'Pagination',
        'start_time': 'StartTime',
        'task_id': 'TaskId',
        'task_status': 'TaskStatus',
        'task_type': 'TaskType',
        'url': 'Url'
    }

    def __init__(self, domain=None, end_time=None, pagination=None, start_time=None, task_id=None, task_status=None, task_type=None, url=None, _configuration=None):  # noqa: E501
        """ListContentTasksRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._domain = None
        self._end_time = None
        self._pagination = None
        self._start_time = None
        self._task_id = None
        self._task_status = None
        self._task_type = None
        self._url = None
        self.discriminator = None

        if domain is not None:
            self.domain = domain
        if end_time is not None:
            self.end_time = end_time
        if pagination is not None:
            self.pagination = pagination
        if start_time is not None:
            self.start_time = start_time
        if task_id is not None:
            self.task_id = task_id
        if task_status is not None:
            self.task_status = task_status
        if task_type is not None:
            self.task_type = task_type
        if url is not None:
            self.url = url

    @property
    def domain(self):
        """Gets the domain of this ListContentTasksRequest.  # noqa: E501


        :return: The domain of this ListContentTasksRequest.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this ListContentTasksRequest.


        :param domain: The domain of this ListContentTasksRequest.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def end_time(self):
        """Gets the end_time of this ListContentTasksRequest.  # noqa: E501


        :return: The end_time of this ListContentTasksRequest.  # noqa: E501
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListContentTasksRequest.


        :param end_time: The end_time of this ListContentTasksRequest.  # noqa: E501
        :type: int
        """

        self._end_time = end_time

    @property
    def pagination(self):
        """Gets the pagination of this ListContentTasksRequest.  # noqa: E501


        :return: The pagination of this ListContentTasksRequest.  # noqa: E501
        :rtype: PaginationForListContentTasksInput
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this ListContentTasksRequest.


        :param pagination: The pagination of this ListContentTasksRequest.  # noqa: E501
        :type: PaginationForListContentTasksInput
        """

        self._pagination = pagination

    @property
    def start_time(self):
        """Gets the start_time of this ListContentTasksRequest.  # noqa: E501


        :return: The start_time of this ListContentTasksRequest.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListContentTasksRequest.


        :param start_time: The start_time of this ListContentTasksRequest.  # noqa: E501
        :type: int
        """

        self._start_time = start_time

    @property
    def task_id(self):
        """Gets the task_id of this ListContentTasksRequest.  # noqa: E501


        :return: The task_id of this ListContentTasksRequest.  # noqa: E501
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this ListContentTasksRequest.


        :param task_id: The task_id of this ListContentTasksRequest.  # noqa: E501
        :type: str
        """

        self._task_id = task_id

    @property
    def task_status(self):
        """Gets the task_status of this ListContentTasksRequest.  # noqa: E501


        :return: The task_status of this ListContentTasksRequest.  # noqa: E501
        :rtype: str
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        """Sets the task_status of this ListContentTasksRequest.


        :param task_status: The task_status of this ListContentTasksRequest.  # noqa: E501
        :type: str
        """

        self._task_status = task_status

    @property
    def task_type(self):
        """Gets the task_type of this ListContentTasksRequest.  # noqa: E501


        :return: The task_type of this ListContentTasksRequest.  # noqa: E501
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this ListContentTasksRequest.


        :param task_type: The task_type of this ListContentTasksRequest.  # noqa: E501
        :type: str
        """

        self._task_type = task_type

    @property
    def url(self):
        """Gets the url of this ListContentTasksRequest.  # noqa: E501


        :return: The url of this ListContentTasksRequest.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ListContentTasksRequest.


        :param url: The url of this ListContentTasksRequest.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(ListContentTasksRequest, dict):
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
        if not isinstance(other, ListContentTasksRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListContentTasksRequest):
            return True

        return self.to_dict() != other.to_dict()
