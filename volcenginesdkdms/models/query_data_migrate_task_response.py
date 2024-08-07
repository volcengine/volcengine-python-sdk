# coding: utf-8

"""
    dms

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class QueryDataMigrateTaskResponse(object):
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
        'advance_config': 'AdvanceConfigForQueryDataMigrateTaskOutput',
        'basic_config': 'BasicConfigForQueryDataMigrateTaskOutput',
        'create_time': 'str',
        'source': 'SourceForQueryDataMigrateTaskOutput',
        'target': 'TargetForQueryDataMigrateTaskOutput',
        'task_id': 'int',
        'task_progress': 'TaskProgressForQueryDataMigrateTaskOutput',
        'task_report': 'TaskReportForQueryDataMigrateTaskOutput',
        'task_status': 'str'
    }

    attribute_map = {
        'advance_config': 'AdvanceConfig',
        'basic_config': 'BasicConfig',
        'create_time': 'CreateTime',
        'source': 'Source',
        'target': 'Target',
        'task_id': 'TaskID',
        'task_progress': 'TaskProgress',
        'task_report': 'TaskReport',
        'task_status': 'TaskStatus'
    }

    def __init__(self, advance_config=None, basic_config=None, create_time=None, source=None, target=None, task_id=None, task_progress=None, task_report=None, task_status=None, _configuration=None):  # noqa: E501
        """QueryDataMigrateTaskResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._advance_config = None
        self._basic_config = None
        self._create_time = None
        self._source = None
        self._target = None
        self._task_id = None
        self._task_progress = None
        self._task_report = None
        self._task_status = None
        self.discriminator = None

        if advance_config is not None:
            self.advance_config = advance_config
        if basic_config is not None:
            self.basic_config = basic_config
        if create_time is not None:
            self.create_time = create_time
        if source is not None:
            self.source = source
        if target is not None:
            self.target = target
        if task_id is not None:
            self.task_id = task_id
        if task_progress is not None:
            self.task_progress = task_progress
        if task_report is not None:
            self.task_report = task_report
        if task_status is not None:
            self.task_status = task_status

    @property
    def advance_config(self):
        """Gets the advance_config of this QueryDataMigrateTaskResponse.  # noqa: E501


        :return: The advance_config of this QueryDataMigrateTaskResponse.  # noqa: E501
        :rtype: AdvanceConfigForQueryDataMigrateTaskOutput
        """
        return self._advance_config

    @advance_config.setter
    def advance_config(self, advance_config):
        """Sets the advance_config of this QueryDataMigrateTaskResponse.


        :param advance_config: The advance_config of this QueryDataMigrateTaskResponse.  # noqa: E501
        :type: AdvanceConfigForQueryDataMigrateTaskOutput
        """

        self._advance_config = advance_config

    @property
    def basic_config(self):
        """Gets the basic_config of this QueryDataMigrateTaskResponse.  # noqa: E501


        :return: The basic_config of this QueryDataMigrateTaskResponse.  # noqa: E501
        :rtype: BasicConfigForQueryDataMigrateTaskOutput
        """
        return self._basic_config

    @basic_config.setter
    def basic_config(self, basic_config):
        """Sets the basic_config of this QueryDataMigrateTaskResponse.


        :param basic_config: The basic_config of this QueryDataMigrateTaskResponse.  # noqa: E501
        :type: BasicConfigForQueryDataMigrateTaskOutput
        """

        self._basic_config = basic_config

    @property
    def create_time(self):
        """Gets the create_time of this QueryDataMigrateTaskResponse.  # noqa: E501


        :return: The create_time of this QueryDataMigrateTaskResponse.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this QueryDataMigrateTaskResponse.


        :param create_time: The create_time of this QueryDataMigrateTaskResponse.  # noqa: E501
        :type: str
        """

        self._create_time = create_time

    @property
    def source(self):
        """Gets the source of this QueryDataMigrateTaskResponse.  # noqa: E501


        :return: The source of this QueryDataMigrateTaskResponse.  # noqa: E501
        :rtype: SourceForQueryDataMigrateTaskOutput
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this QueryDataMigrateTaskResponse.


        :param source: The source of this QueryDataMigrateTaskResponse.  # noqa: E501
        :type: SourceForQueryDataMigrateTaskOutput
        """

        self._source = source

    @property
    def target(self):
        """Gets the target of this QueryDataMigrateTaskResponse.  # noqa: E501


        :return: The target of this QueryDataMigrateTaskResponse.  # noqa: E501
        :rtype: TargetForQueryDataMigrateTaskOutput
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this QueryDataMigrateTaskResponse.


        :param target: The target of this QueryDataMigrateTaskResponse.  # noqa: E501
        :type: TargetForQueryDataMigrateTaskOutput
        """

        self._target = target

    @property
    def task_id(self):
        """Gets the task_id of this QueryDataMigrateTaskResponse.  # noqa: E501


        :return: The task_id of this QueryDataMigrateTaskResponse.  # noqa: E501
        :rtype: int
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this QueryDataMigrateTaskResponse.


        :param task_id: The task_id of this QueryDataMigrateTaskResponse.  # noqa: E501
        :type: int
        """

        self._task_id = task_id

    @property
    def task_progress(self):
        """Gets the task_progress of this QueryDataMigrateTaskResponse.  # noqa: E501


        :return: The task_progress of this QueryDataMigrateTaskResponse.  # noqa: E501
        :rtype: TaskProgressForQueryDataMigrateTaskOutput
        """
        return self._task_progress

    @task_progress.setter
    def task_progress(self, task_progress):
        """Sets the task_progress of this QueryDataMigrateTaskResponse.


        :param task_progress: The task_progress of this QueryDataMigrateTaskResponse.  # noqa: E501
        :type: TaskProgressForQueryDataMigrateTaskOutput
        """

        self._task_progress = task_progress

    @property
    def task_report(self):
        """Gets the task_report of this QueryDataMigrateTaskResponse.  # noqa: E501


        :return: The task_report of this QueryDataMigrateTaskResponse.  # noqa: E501
        :rtype: TaskReportForQueryDataMigrateTaskOutput
        """
        return self._task_report

    @task_report.setter
    def task_report(self, task_report):
        """Sets the task_report of this QueryDataMigrateTaskResponse.


        :param task_report: The task_report of this QueryDataMigrateTaskResponse.  # noqa: E501
        :type: TaskReportForQueryDataMigrateTaskOutput
        """

        self._task_report = task_report

    @property
    def task_status(self):
        """Gets the task_status of this QueryDataMigrateTaskResponse.  # noqa: E501


        :return: The task_status of this QueryDataMigrateTaskResponse.  # noqa: E501
        :rtype: str
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        """Sets the task_status of this QueryDataMigrateTaskResponse.


        :param task_status: The task_status of this QueryDataMigrateTaskResponse.  # noqa: E501
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
        if issubclass(QueryDataMigrateTaskResponse, dict):
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
        if not isinstance(other, QueryDataMigrateTaskResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QueryDataMigrateTaskResponse):
            return True

        return self.to_dict() != other.to_dict()
