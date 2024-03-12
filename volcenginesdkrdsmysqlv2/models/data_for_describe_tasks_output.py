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


class DataForDescribeTasksOutput(object):
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
        'config_infos': 'list[ConfigInfoForDescribeTasksOutput]',
        'cost_time_ms': 'int',
        'create_time': 'str',
        'finish_time': 'str',
        'progress': 'int',
        'related_instance_infos': 'RelatedInstanceInfosForDescribeTasksOutput',
        'start_time': 'str',
        'task_action': 'str',
        'task_category': 'str',
        'task_desc': 'str',
        'task_id': 'str',
        'task_params': 'str',
        'task_progress': 'list[TaskProgressForDescribeTasksOutput]',
        'task_source': 'str',
        'task_status': 'str'
    }

    attribute_map = {
        'config_infos': 'ConfigInfos',
        'cost_time_ms': 'CostTimeMS',
        'create_time': 'CreateTime',
        'finish_time': 'FinishTime',
        'progress': 'Progress',
        'related_instance_infos': 'RelatedInstanceInfos',
        'start_time': 'StartTime',
        'task_action': 'TaskAction',
        'task_category': 'TaskCategory',
        'task_desc': 'TaskDesc',
        'task_id': 'TaskId',
        'task_params': 'TaskParams',
        'task_progress': 'TaskProgress',
        'task_source': 'TaskSource',
        'task_status': 'TaskStatus'
    }

    def __init__(self, config_infos=None, cost_time_ms=None, create_time=None, finish_time=None, progress=None, related_instance_infos=None, start_time=None, task_action=None, task_category=None, task_desc=None, task_id=None, task_params=None, task_progress=None, task_source=None, task_status=None, _configuration=None):  # noqa: E501
        """DataForDescribeTasksOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._config_infos = None
        self._cost_time_ms = None
        self._create_time = None
        self._finish_time = None
        self._progress = None
        self._related_instance_infos = None
        self._start_time = None
        self._task_action = None
        self._task_category = None
        self._task_desc = None
        self._task_id = None
        self._task_params = None
        self._task_progress = None
        self._task_source = None
        self._task_status = None
        self.discriminator = None

        if config_infos is not None:
            self.config_infos = config_infos
        if cost_time_ms is not None:
            self.cost_time_ms = cost_time_ms
        if create_time is not None:
            self.create_time = create_time
        if finish_time is not None:
            self.finish_time = finish_time
        if progress is not None:
            self.progress = progress
        if related_instance_infos is not None:
            self.related_instance_infos = related_instance_infos
        if start_time is not None:
            self.start_time = start_time
        if task_action is not None:
            self.task_action = task_action
        if task_category is not None:
            self.task_category = task_category
        if task_desc is not None:
            self.task_desc = task_desc
        if task_id is not None:
            self.task_id = task_id
        if task_params is not None:
            self.task_params = task_params
        if task_progress is not None:
            self.task_progress = task_progress
        if task_source is not None:
            self.task_source = task_source
        if task_status is not None:
            self.task_status = task_status

    @property
    def config_infos(self):
        """Gets the config_infos of this DataForDescribeTasksOutput.  # noqa: E501


        :return: The config_infos of this DataForDescribeTasksOutput.  # noqa: E501
        :rtype: list[ConfigInfoForDescribeTasksOutput]
        """
        return self._config_infos

    @config_infos.setter
    def config_infos(self, config_infos):
        """Sets the config_infos of this DataForDescribeTasksOutput.


        :param config_infos: The config_infos of this DataForDescribeTasksOutput.  # noqa: E501
        :type: list[ConfigInfoForDescribeTasksOutput]
        """

        self._config_infos = config_infos

    @property
    def cost_time_ms(self):
        """Gets the cost_time_ms of this DataForDescribeTasksOutput.  # noqa: E501


        :return: The cost_time_ms of this DataForDescribeTasksOutput.  # noqa: E501
        :rtype: int
        """
        return self._cost_time_ms

    @cost_time_ms.setter
    def cost_time_ms(self, cost_time_ms):
        """Sets the cost_time_ms of this DataForDescribeTasksOutput.


        :param cost_time_ms: The cost_time_ms of this DataForDescribeTasksOutput.  # noqa: E501
        :type: int
        """

        self._cost_time_ms = cost_time_ms

    @property
    def create_time(self):
        """Gets the create_time of this DataForDescribeTasksOutput.  # noqa: E501


        :return: The create_time of this DataForDescribeTasksOutput.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this DataForDescribeTasksOutput.


        :param create_time: The create_time of this DataForDescribeTasksOutput.  # noqa: E501
        :type: str
        """

        self._create_time = create_time

    @property
    def finish_time(self):
        """Gets the finish_time of this DataForDescribeTasksOutput.  # noqa: E501


        :return: The finish_time of this DataForDescribeTasksOutput.  # noqa: E501
        :rtype: str
        """
        return self._finish_time

    @finish_time.setter
    def finish_time(self, finish_time):
        """Sets the finish_time of this DataForDescribeTasksOutput.


        :param finish_time: The finish_time of this DataForDescribeTasksOutput.  # noqa: E501
        :type: str
        """

        self._finish_time = finish_time

    @property
    def progress(self):
        """Gets the progress of this DataForDescribeTasksOutput.  # noqa: E501


        :return: The progress of this DataForDescribeTasksOutput.  # noqa: E501
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this DataForDescribeTasksOutput.


        :param progress: The progress of this DataForDescribeTasksOutput.  # noqa: E501
        :type: int
        """

        self._progress = progress

    @property
    def related_instance_infos(self):
        """Gets the related_instance_infos of this DataForDescribeTasksOutput.  # noqa: E501


        :return: The related_instance_infos of this DataForDescribeTasksOutput.  # noqa: E501
        :rtype: RelatedInstanceInfosForDescribeTasksOutput
        """
        return self._related_instance_infos

    @related_instance_infos.setter
    def related_instance_infos(self, related_instance_infos):
        """Sets the related_instance_infos of this DataForDescribeTasksOutput.


        :param related_instance_infos: The related_instance_infos of this DataForDescribeTasksOutput.  # noqa: E501
        :type: RelatedInstanceInfosForDescribeTasksOutput
        """

        self._related_instance_infos = related_instance_infos

    @property
    def start_time(self):
        """Gets the start_time of this DataForDescribeTasksOutput.  # noqa: E501


        :return: The start_time of this DataForDescribeTasksOutput.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this DataForDescribeTasksOutput.


        :param start_time: The start_time of this DataForDescribeTasksOutput.  # noqa: E501
        :type: str
        """

        self._start_time = start_time

    @property
    def task_action(self):
        """Gets the task_action of this DataForDescribeTasksOutput.  # noqa: E501


        :return: The task_action of this DataForDescribeTasksOutput.  # noqa: E501
        :rtype: str
        """
        return self._task_action

    @task_action.setter
    def task_action(self, task_action):
        """Sets the task_action of this DataForDescribeTasksOutput.


        :param task_action: The task_action of this DataForDescribeTasksOutput.  # noqa: E501
        :type: str
        """

        self._task_action = task_action

    @property
    def task_category(self):
        """Gets the task_category of this DataForDescribeTasksOutput.  # noqa: E501


        :return: The task_category of this DataForDescribeTasksOutput.  # noqa: E501
        :rtype: str
        """
        return self._task_category

    @task_category.setter
    def task_category(self, task_category):
        """Sets the task_category of this DataForDescribeTasksOutput.


        :param task_category: The task_category of this DataForDescribeTasksOutput.  # noqa: E501
        :type: str
        """

        self._task_category = task_category

    @property
    def task_desc(self):
        """Gets the task_desc of this DataForDescribeTasksOutput.  # noqa: E501


        :return: The task_desc of this DataForDescribeTasksOutput.  # noqa: E501
        :rtype: str
        """
        return self._task_desc

    @task_desc.setter
    def task_desc(self, task_desc):
        """Sets the task_desc of this DataForDescribeTasksOutput.


        :param task_desc: The task_desc of this DataForDescribeTasksOutput.  # noqa: E501
        :type: str
        """

        self._task_desc = task_desc

    @property
    def task_id(self):
        """Gets the task_id of this DataForDescribeTasksOutput.  # noqa: E501


        :return: The task_id of this DataForDescribeTasksOutput.  # noqa: E501
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this DataForDescribeTasksOutput.


        :param task_id: The task_id of this DataForDescribeTasksOutput.  # noqa: E501
        :type: str
        """

        self._task_id = task_id

    @property
    def task_params(self):
        """Gets the task_params of this DataForDescribeTasksOutput.  # noqa: E501


        :return: The task_params of this DataForDescribeTasksOutput.  # noqa: E501
        :rtype: str
        """
        return self._task_params

    @task_params.setter
    def task_params(self, task_params):
        """Sets the task_params of this DataForDescribeTasksOutput.


        :param task_params: The task_params of this DataForDescribeTasksOutput.  # noqa: E501
        :type: str
        """

        self._task_params = task_params

    @property
    def task_progress(self):
        """Gets the task_progress of this DataForDescribeTasksOutput.  # noqa: E501


        :return: The task_progress of this DataForDescribeTasksOutput.  # noqa: E501
        :rtype: list[TaskProgressForDescribeTasksOutput]
        """
        return self._task_progress

    @task_progress.setter
    def task_progress(self, task_progress):
        """Sets the task_progress of this DataForDescribeTasksOutput.


        :param task_progress: The task_progress of this DataForDescribeTasksOutput.  # noqa: E501
        :type: list[TaskProgressForDescribeTasksOutput]
        """

        self._task_progress = task_progress

    @property
    def task_source(self):
        """Gets the task_source of this DataForDescribeTasksOutput.  # noqa: E501


        :return: The task_source of this DataForDescribeTasksOutput.  # noqa: E501
        :rtype: str
        """
        return self._task_source

    @task_source.setter
    def task_source(self, task_source):
        """Sets the task_source of this DataForDescribeTasksOutput.


        :param task_source: The task_source of this DataForDescribeTasksOutput.  # noqa: E501
        :type: str
        """

        self._task_source = task_source

    @property
    def task_status(self):
        """Gets the task_status of this DataForDescribeTasksOutput.  # noqa: E501


        :return: The task_status of this DataForDescribeTasksOutput.  # noqa: E501
        :rtype: str
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        """Sets the task_status of this DataForDescribeTasksOutput.


        :param task_status: The task_status of this DataForDescribeTasksOutput.  # noqa: E501
        :type: str
        """

        self._task_status = task_status

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
        if issubclass(DataForDescribeTasksOutput, dict):
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
        if not isinstance(other, DataForDescribeTasksOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataForDescribeTasksOutput):
            return True

        return self.to_dict() != other.to_dict()
