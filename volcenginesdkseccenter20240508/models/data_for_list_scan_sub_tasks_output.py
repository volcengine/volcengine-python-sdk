# coding: utf-8

"""
    seccenter20240508

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DataForListScanSubTasksOutput(object):
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
        'agent_id': 'str',
        'fail_reason': 'str',
        'hostname': 'str',
        'status': 'str',
        'task_id': 'str',
        'update_time': 'int'
    }

    attribute_map = {
        'agent_id': 'AgentID',
        'fail_reason': 'FailReason',
        'hostname': 'Hostname',
        'status': 'Status',
        'task_id': 'TaskID',
        'update_time': 'UpdateTime'
    }

    def __init__(self, agent_id=None, fail_reason=None, hostname=None, status=None, task_id=None, update_time=None, _configuration=None):  # noqa: E501
        """DataForListScanSubTasksOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._agent_id = None
        self._fail_reason = None
        self._hostname = None
        self._status = None
        self._task_id = None
        self._update_time = None
        self.discriminator = None

        if agent_id is not None:
            self.agent_id = agent_id
        if fail_reason is not None:
            self.fail_reason = fail_reason
        if hostname is not None:
            self.hostname = hostname
        if status is not None:
            self.status = status
        if task_id is not None:
            self.task_id = task_id
        if update_time is not None:
            self.update_time = update_time

    @property
    def agent_id(self):
        """Gets the agent_id of this DataForListScanSubTasksOutput.  # noqa: E501


        :return: The agent_id of this DataForListScanSubTasksOutput.  # noqa: E501
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """Sets the agent_id of this DataForListScanSubTasksOutput.


        :param agent_id: The agent_id of this DataForListScanSubTasksOutput.  # noqa: E501
        :type: str
        """

        self._agent_id = agent_id

    @property
    def fail_reason(self):
        """Gets the fail_reason of this DataForListScanSubTasksOutput.  # noqa: E501


        :return: The fail_reason of this DataForListScanSubTasksOutput.  # noqa: E501
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        """Sets the fail_reason of this DataForListScanSubTasksOutput.


        :param fail_reason: The fail_reason of this DataForListScanSubTasksOutput.  # noqa: E501
        :type: str
        """

        self._fail_reason = fail_reason

    @property
    def hostname(self):
        """Gets the hostname of this DataForListScanSubTasksOutput.  # noqa: E501


        :return: The hostname of this DataForListScanSubTasksOutput.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this DataForListScanSubTasksOutput.


        :param hostname: The hostname of this DataForListScanSubTasksOutput.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def status(self):
        """Gets the status of this DataForListScanSubTasksOutput.  # noqa: E501


        :return: The status of this DataForListScanSubTasksOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DataForListScanSubTasksOutput.


        :param status: The status of this DataForListScanSubTasksOutput.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def task_id(self):
        """Gets the task_id of this DataForListScanSubTasksOutput.  # noqa: E501


        :return: The task_id of this DataForListScanSubTasksOutput.  # noqa: E501
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this DataForListScanSubTasksOutput.


        :param task_id: The task_id of this DataForListScanSubTasksOutput.  # noqa: E501
        :type: str
        """

        self._task_id = task_id

    @property
    def update_time(self):
        """Gets the update_time of this DataForListScanSubTasksOutput.  # noqa: E501


        :return: The update_time of this DataForListScanSubTasksOutput.  # noqa: E501
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this DataForListScanSubTasksOutput.


        :param update_time: The update_time of this DataForListScanSubTasksOutput.  # noqa: E501
        :type: int
        """

        self._update_time = update_time

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
        if issubclass(DataForListScanSubTasksOutput, dict):
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
        if not isinstance(other, DataForListScanSubTasksOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataForListScanSubTasksOutput):
            return True

        return self.to_dict() != other.to_dict()
