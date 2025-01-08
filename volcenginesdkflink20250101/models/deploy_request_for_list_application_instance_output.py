# coding: utf-8

"""
    flink20250101

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DeployRequestForListApplicationInstanceOutput(object):
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
        'namespace': 'str',
        'priority': 'str',
        'queue': 'str',
        'resource_pool': 'str',
        'schedule_policy': 'str',
        'schedule_timeout': 'str'
    }

    attribute_map = {
        'namespace': 'Namespace',
        'priority': 'Priority',
        'queue': 'Queue',
        'resource_pool': 'ResourcePool',
        'schedule_policy': 'SchedulePolicy',
        'schedule_timeout': 'ScheduleTimeout'
    }

    def __init__(self, namespace=None, priority=None, queue=None, resource_pool=None, schedule_policy=None, schedule_timeout=None, _configuration=None):  # noqa: E501
        """DeployRequestForListApplicationInstanceOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._namespace = None
        self._priority = None
        self._queue = None
        self._resource_pool = None
        self._schedule_policy = None
        self._schedule_timeout = None
        self.discriminator = None

        if namespace is not None:
            self.namespace = namespace
        if priority is not None:
            self.priority = priority
        if queue is not None:
            self.queue = queue
        if resource_pool is not None:
            self.resource_pool = resource_pool
        if schedule_policy is not None:
            self.schedule_policy = schedule_policy
        if schedule_timeout is not None:
            self.schedule_timeout = schedule_timeout

    @property
    def namespace(self):
        """Gets the namespace of this DeployRequestForListApplicationInstanceOutput.  # noqa: E501


        :return: The namespace of this DeployRequestForListApplicationInstanceOutput.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this DeployRequestForListApplicationInstanceOutput.


        :param namespace: The namespace of this DeployRequestForListApplicationInstanceOutput.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def priority(self):
        """Gets the priority of this DeployRequestForListApplicationInstanceOutput.  # noqa: E501


        :return: The priority of this DeployRequestForListApplicationInstanceOutput.  # noqa: E501
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this DeployRequestForListApplicationInstanceOutput.


        :param priority: The priority of this DeployRequestForListApplicationInstanceOutput.  # noqa: E501
        :type: str
        """

        self._priority = priority

    @property
    def queue(self):
        """Gets the queue of this DeployRequestForListApplicationInstanceOutput.  # noqa: E501


        :return: The queue of this DeployRequestForListApplicationInstanceOutput.  # noqa: E501
        :rtype: str
        """
        return self._queue

    @queue.setter
    def queue(self, queue):
        """Sets the queue of this DeployRequestForListApplicationInstanceOutput.


        :param queue: The queue of this DeployRequestForListApplicationInstanceOutput.  # noqa: E501
        :type: str
        """

        self._queue = queue

    @property
    def resource_pool(self):
        """Gets the resource_pool of this DeployRequestForListApplicationInstanceOutput.  # noqa: E501


        :return: The resource_pool of this DeployRequestForListApplicationInstanceOutput.  # noqa: E501
        :rtype: str
        """
        return self._resource_pool

    @resource_pool.setter
    def resource_pool(self, resource_pool):
        """Sets the resource_pool of this DeployRequestForListApplicationInstanceOutput.


        :param resource_pool: The resource_pool of this DeployRequestForListApplicationInstanceOutput.  # noqa: E501
        :type: str
        """

        self._resource_pool = resource_pool

    @property
    def schedule_policy(self):
        """Gets the schedule_policy of this DeployRequestForListApplicationInstanceOutput.  # noqa: E501


        :return: The schedule_policy of this DeployRequestForListApplicationInstanceOutput.  # noqa: E501
        :rtype: str
        """
        return self._schedule_policy

    @schedule_policy.setter
    def schedule_policy(self, schedule_policy):
        """Sets the schedule_policy of this DeployRequestForListApplicationInstanceOutput.


        :param schedule_policy: The schedule_policy of this DeployRequestForListApplicationInstanceOutput.  # noqa: E501
        :type: str
        """

        self._schedule_policy = schedule_policy

    @property
    def schedule_timeout(self):
        """Gets the schedule_timeout of this DeployRequestForListApplicationInstanceOutput.  # noqa: E501


        :return: The schedule_timeout of this DeployRequestForListApplicationInstanceOutput.  # noqa: E501
        :rtype: str
        """
        return self._schedule_timeout

    @schedule_timeout.setter
    def schedule_timeout(self, schedule_timeout):
        """Sets the schedule_timeout of this DeployRequestForListApplicationInstanceOutput.


        :param schedule_timeout: The schedule_timeout of this DeployRequestForListApplicationInstanceOutput.  # noqa: E501
        :type: str
        """

        self._schedule_timeout = schedule_timeout

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
        if issubclass(DeployRequestForListApplicationInstanceOutput, dict):
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
        if not isinstance(other, DeployRequestForListApplicationInstanceOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeployRequestForListApplicationInstanceOutput):
            return True

        return self.to_dict() != other.to_dict()
