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


class CreateFailureDataMigrateTaskRequest(object):
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
        'origin_task_id': 'int',
        'task_name': 'str'
    }

    attribute_map = {
        'origin_task_id': 'OriginTaskID',
        'task_name': 'TaskName'
    }

    def __init__(self, origin_task_id=None, task_name=None, _configuration=None):  # noqa: E501
        """CreateFailureDataMigrateTaskRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._origin_task_id = None
        self._task_name = None
        self.discriminator = None

        self.origin_task_id = origin_task_id
        self.task_name = task_name

    @property
    def origin_task_id(self):
        """Gets the origin_task_id of this CreateFailureDataMigrateTaskRequest.  # noqa: E501


        :return: The origin_task_id of this CreateFailureDataMigrateTaskRequest.  # noqa: E501
        :rtype: int
        """
        return self._origin_task_id

    @origin_task_id.setter
    def origin_task_id(self, origin_task_id):
        """Sets the origin_task_id of this CreateFailureDataMigrateTaskRequest.


        :param origin_task_id: The origin_task_id of this CreateFailureDataMigrateTaskRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and origin_task_id is None:
            raise ValueError("Invalid value for `origin_task_id`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                origin_task_id is not None and origin_task_id < 0):  # noqa: E501
            raise ValueError("Invalid value for `origin_task_id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._origin_task_id = origin_task_id

    @property
    def task_name(self):
        """Gets the task_name of this CreateFailureDataMigrateTaskRequest.  # noqa: E501


        :return: The task_name of this CreateFailureDataMigrateTaskRequest.  # noqa: E501
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this CreateFailureDataMigrateTaskRequest.


        :param task_name: The task_name of this CreateFailureDataMigrateTaskRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and task_name is None:
            raise ValueError("Invalid value for `task_name`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                task_name is not None and len(task_name) > 32):
            raise ValueError("Invalid value for `task_name`, length must be less than or equal to `32`")  # noqa: E501
        if (self._configuration.client_side_validation and
                task_name is not None and len(task_name) < 3):
            raise ValueError("Invalid value for `task_name`, length must be greater than or equal to `3`")  # noqa: E501

        self._task_name = task_name

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
        if issubclass(CreateFailureDataMigrateTaskRequest, dict):
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
        if not isinstance(other, CreateFailureDataMigrateTaskRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateFailureDataMigrateTaskRequest):
            return True

        return self.to_dict() != other.to_dict()