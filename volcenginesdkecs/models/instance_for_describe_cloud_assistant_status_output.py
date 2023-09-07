# coding: utf-8

"""
    ecs

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class InstanceForDescribeCloudAssistantStatusOutput(object):
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
        'client_version': 'str',
        'host_name': 'str',
        'instance_id': 'str',
        'instance_name': 'str',
        'last_heartbeat_time': 'str',
        'os_type': 'str',
        'os_version': 'str',
        'status': 'str'
    }

    attribute_map = {
        'client_version': 'ClientVersion',
        'host_name': 'HostName',
        'instance_id': 'InstanceId',
        'instance_name': 'InstanceName',
        'last_heartbeat_time': 'LastHeartbeatTime',
        'os_type': 'OsType',
        'os_version': 'OsVersion',
        'status': 'Status'
    }

    def __init__(self, client_version=None, host_name=None, instance_id=None, instance_name=None, last_heartbeat_time=None, os_type=None, os_version=None, status=None, _configuration=None):  # noqa: E501
        """InstanceForDescribeCloudAssistantStatusOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._client_version = None
        self._host_name = None
        self._instance_id = None
        self._instance_name = None
        self._last_heartbeat_time = None
        self._os_type = None
        self._os_version = None
        self._status = None
        self.discriminator = None

        if client_version is not None:
            self.client_version = client_version
        if host_name is not None:
            self.host_name = host_name
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if last_heartbeat_time is not None:
            self.last_heartbeat_time = last_heartbeat_time
        if os_type is not None:
            self.os_type = os_type
        if os_version is not None:
            self.os_version = os_version
        if status is not None:
            self.status = status

    @property
    def client_version(self):
        """Gets the client_version of this InstanceForDescribeCloudAssistantStatusOutput.  # noqa: E501


        :return: The client_version of this InstanceForDescribeCloudAssistantStatusOutput.  # noqa: E501
        :rtype: str
        """
        return self._client_version

    @client_version.setter
    def client_version(self, client_version):
        """Sets the client_version of this InstanceForDescribeCloudAssistantStatusOutput.


        :param client_version: The client_version of this InstanceForDescribeCloudAssistantStatusOutput.  # noqa: E501
        :type: str
        """

        self._client_version = client_version

    @property
    def host_name(self):
        """Gets the host_name of this InstanceForDescribeCloudAssistantStatusOutput.  # noqa: E501


        :return: The host_name of this InstanceForDescribeCloudAssistantStatusOutput.  # noqa: E501
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this InstanceForDescribeCloudAssistantStatusOutput.


        :param host_name: The host_name of this InstanceForDescribeCloudAssistantStatusOutput.  # noqa: E501
        :type: str
        """

        self._host_name = host_name

    @property
    def instance_id(self):
        """Gets the instance_id of this InstanceForDescribeCloudAssistantStatusOutput.  # noqa: E501


        :return: The instance_id of this InstanceForDescribeCloudAssistantStatusOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this InstanceForDescribeCloudAssistantStatusOutput.


        :param instance_id: The instance_id of this InstanceForDescribeCloudAssistantStatusOutput.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def instance_name(self):
        """Gets the instance_name of this InstanceForDescribeCloudAssistantStatusOutput.  # noqa: E501


        :return: The instance_name of this InstanceForDescribeCloudAssistantStatusOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this InstanceForDescribeCloudAssistantStatusOutput.


        :param instance_name: The instance_name of this InstanceForDescribeCloudAssistantStatusOutput.  # noqa: E501
        :type: str
        """

        self._instance_name = instance_name

    @property
    def last_heartbeat_time(self):
        """Gets the last_heartbeat_time of this InstanceForDescribeCloudAssistantStatusOutput.  # noqa: E501


        :return: The last_heartbeat_time of this InstanceForDescribeCloudAssistantStatusOutput.  # noqa: E501
        :rtype: str
        """
        return self._last_heartbeat_time

    @last_heartbeat_time.setter
    def last_heartbeat_time(self, last_heartbeat_time):
        """Sets the last_heartbeat_time of this InstanceForDescribeCloudAssistantStatusOutput.


        :param last_heartbeat_time: The last_heartbeat_time of this InstanceForDescribeCloudAssistantStatusOutput.  # noqa: E501
        :type: str
        """

        self._last_heartbeat_time = last_heartbeat_time

    @property
    def os_type(self):
        """Gets the os_type of this InstanceForDescribeCloudAssistantStatusOutput.  # noqa: E501


        :return: The os_type of this InstanceForDescribeCloudAssistantStatusOutput.  # noqa: E501
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this InstanceForDescribeCloudAssistantStatusOutput.


        :param os_type: The os_type of this InstanceForDescribeCloudAssistantStatusOutput.  # noqa: E501
        :type: str
        """

        self._os_type = os_type

    @property
    def os_version(self):
        """Gets the os_version of this InstanceForDescribeCloudAssistantStatusOutput.  # noqa: E501


        :return: The os_version of this InstanceForDescribeCloudAssistantStatusOutput.  # noqa: E501
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """Sets the os_version of this InstanceForDescribeCloudAssistantStatusOutput.


        :param os_version: The os_version of this InstanceForDescribeCloudAssistantStatusOutput.  # noqa: E501
        :type: str
        """

        self._os_version = os_version

    @property
    def status(self):
        """Gets the status of this InstanceForDescribeCloudAssistantStatusOutput.  # noqa: E501


        :return: The status of this InstanceForDescribeCloudAssistantStatusOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InstanceForDescribeCloudAssistantStatusOutput.


        :param status: The status of this InstanceForDescribeCloudAssistantStatusOutput.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(InstanceForDescribeCloudAssistantStatusOutput, dict):
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
        if not isinstance(other, InstanceForDescribeCloudAssistantStatusOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InstanceForDescribeCloudAssistantStatusOutput):
            return True

        return self.to_dict() != other.to_dict()
