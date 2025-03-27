# coding: utf-8

"""
    rds_mssql

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeTosRestoreTasksRequest(object):
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
        'instance_name': 'str',
        'page_number': 'int',
        'page_size': 'int',
        'project_name': 'str',
        'query_end_time': 'str',
        'query_start_time': 'str',
        'restore_task_ids': 'list[str]'
    }

    attribute_map = {
        'instance_id': 'InstanceId',
        'instance_name': 'InstanceName',
        'page_number': 'PageNumber',
        'page_size': 'PageSize',
        'project_name': 'ProjectName',
        'query_end_time': 'QueryEndTime',
        'query_start_time': 'QueryStartTime',
        'restore_task_ids': 'RestoreTaskIds'
    }

    def __init__(self, instance_id=None, instance_name=None, page_number=None, page_size=None, project_name=None, query_end_time=None, query_start_time=None, restore_task_ids=None, _configuration=None):  # noqa: E501
        """DescribeTosRestoreTasksRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._instance_id = None
        self._instance_name = None
        self._page_number = None
        self._page_size = None
        self._project_name = None
        self._query_end_time = None
        self._query_start_time = None
        self._restore_task_ids = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if project_name is not None:
            self.project_name = project_name
        if query_end_time is not None:
            self.query_end_time = query_end_time
        if query_start_time is not None:
            self.query_start_time = query_start_time
        if restore_task_ids is not None:
            self.restore_task_ids = restore_task_ids

    @property
    def instance_id(self):
        """Gets the instance_id of this DescribeTosRestoreTasksRequest.  # noqa: E501


        :return: The instance_id of this DescribeTosRestoreTasksRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this DescribeTosRestoreTasksRequest.


        :param instance_id: The instance_id of this DescribeTosRestoreTasksRequest.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def instance_name(self):
        """Gets the instance_name of this DescribeTosRestoreTasksRequest.  # noqa: E501


        :return: The instance_name of this DescribeTosRestoreTasksRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this DescribeTosRestoreTasksRequest.


        :param instance_name: The instance_name of this DescribeTosRestoreTasksRequest.  # noqa: E501
        :type: str
        """

        self._instance_name = instance_name

    @property
    def page_number(self):
        """Gets the page_number of this DescribeTosRestoreTasksRequest.  # noqa: E501


        :return: The page_number of this DescribeTosRestoreTasksRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this DescribeTosRestoreTasksRequest.


        :param page_number: The page_number of this DescribeTosRestoreTasksRequest.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this DescribeTosRestoreTasksRequest.  # noqa: E501


        :return: The page_size of this DescribeTosRestoreTasksRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this DescribeTosRestoreTasksRequest.


        :param page_size: The page_size of this DescribeTosRestoreTasksRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def project_name(self):
        """Gets the project_name of this DescribeTosRestoreTasksRequest.  # noqa: E501


        :return: The project_name of this DescribeTosRestoreTasksRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this DescribeTosRestoreTasksRequest.


        :param project_name: The project_name of this DescribeTosRestoreTasksRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def query_end_time(self):
        """Gets the query_end_time of this DescribeTosRestoreTasksRequest.  # noqa: E501


        :return: The query_end_time of this DescribeTosRestoreTasksRequest.  # noqa: E501
        :rtype: str
        """
        return self._query_end_time

    @query_end_time.setter
    def query_end_time(self, query_end_time):
        """Sets the query_end_time of this DescribeTosRestoreTasksRequest.


        :param query_end_time: The query_end_time of this DescribeTosRestoreTasksRequest.  # noqa: E501
        :type: str
        """

        self._query_end_time = query_end_time

    @property
    def query_start_time(self):
        """Gets the query_start_time of this DescribeTosRestoreTasksRequest.  # noqa: E501


        :return: The query_start_time of this DescribeTosRestoreTasksRequest.  # noqa: E501
        :rtype: str
        """
        return self._query_start_time

    @query_start_time.setter
    def query_start_time(self, query_start_time):
        """Sets the query_start_time of this DescribeTosRestoreTasksRequest.


        :param query_start_time: The query_start_time of this DescribeTosRestoreTasksRequest.  # noqa: E501
        :type: str
        """

        self._query_start_time = query_start_time

    @property
    def restore_task_ids(self):
        """Gets the restore_task_ids of this DescribeTosRestoreTasksRequest.  # noqa: E501


        :return: The restore_task_ids of this DescribeTosRestoreTasksRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._restore_task_ids

    @restore_task_ids.setter
    def restore_task_ids(self, restore_task_ids):
        """Sets the restore_task_ids of this DescribeTosRestoreTasksRequest.


        :param restore_task_ids: The restore_task_ids of this DescribeTosRestoreTasksRequest.  # noqa: E501
        :type: list[str]
        """

        self._restore_task_ids = restore_task_ids

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
        if issubclass(DescribeTosRestoreTasksRequest, dict):
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
        if not isinstance(other, DescribeTosRestoreTasksRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeTosRestoreTasksRequest):
            return True

        return self.to_dict() != other.to_dict()
