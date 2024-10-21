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


class InvokeCommandRequest(object):
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
        'command_id': 'str',
        'frequency': 'str',
        'instance_ids': 'list[str]',
        'invocation_description': 'str',
        'invocation_name': 'str',
        'launch_time': 'str',
        'parameters': 'str',
        'project_name': 'str',
        'recurrence_end_time': 'str',
        'repeat_mode': 'str',
        'tags': 'list[TagForInvokeCommandInput]',
        'timeout': 'int',
        'username': 'str',
        'working_dir': 'str'
    }

    attribute_map = {
        'command_id': 'CommandId',
        'frequency': 'Frequency',
        'instance_ids': 'InstanceIds',
        'invocation_description': 'InvocationDescription',
        'invocation_name': 'InvocationName',
        'launch_time': 'LaunchTime',
        'parameters': 'Parameters',
        'project_name': 'ProjectName',
        'recurrence_end_time': 'RecurrenceEndTime',
        'repeat_mode': 'RepeatMode',
        'tags': 'Tags',
        'timeout': 'Timeout',
        'username': 'Username',
        'working_dir': 'WorkingDir'
    }

    def __init__(self, command_id=None, frequency=None, instance_ids=None, invocation_description=None, invocation_name=None, launch_time=None, parameters=None, project_name=None, recurrence_end_time=None, repeat_mode=None, tags=None, timeout=None, username=None, working_dir=None, _configuration=None):  # noqa: E501
        """InvokeCommandRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._command_id = None
        self._frequency = None
        self._instance_ids = None
        self._invocation_description = None
        self._invocation_name = None
        self._launch_time = None
        self._parameters = None
        self._project_name = None
        self._recurrence_end_time = None
        self._repeat_mode = None
        self._tags = None
        self._timeout = None
        self._username = None
        self._working_dir = None
        self.discriminator = None

        self.command_id = command_id
        if frequency is not None:
            self.frequency = frequency
        if instance_ids is not None:
            self.instance_ids = instance_ids
        if invocation_description is not None:
            self.invocation_description = invocation_description
        if invocation_name is not None:
            self.invocation_name = invocation_name
        if launch_time is not None:
            self.launch_time = launch_time
        if parameters is not None:
            self.parameters = parameters
        if project_name is not None:
            self.project_name = project_name
        if recurrence_end_time is not None:
            self.recurrence_end_time = recurrence_end_time
        if repeat_mode is not None:
            self.repeat_mode = repeat_mode
        if tags is not None:
            self.tags = tags
        if timeout is not None:
            self.timeout = timeout
        if username is not None:
            self.username = username
        if working_dir is not None:
            self.working_dir = working_dir

    @property
    def command_id(self):
        """Gets the command_id of this InvokeCommandRequest.  # noqa: E501


        :return: The command_id of this InvokeCommandRequest.  # noqa: E501
        :rtype: str
        """
        return self._command_id

    @command_id.setter
    def command_id(self, command_id):
        """Sets the command_id of this InvokeCommandRequest.


        :param command_id: The command_id of this InvokeCommandRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and command_id is None:
            raise ValueError("Invalid value for `command_id`, must not be `None`")  # noqa: E501

        self._command_id = command_id

    @property
    def frequency(self):
        """Gets the frequency of this InvokeCommandRequest.  # noqa: E501


        :return: The frequency of this InvokeCommandRequest.  # noqa: E501
        :rtype: str
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this InvokeCommandRequest.


        :param frequency: The frequency of this InvokeCommandRequest.  # noqa: E501
        :type: str
        """

        self._frequency = frequency

    @property
    def instance_ids(self):
        """Gets the instance_ids of this InvokeCommandRequest.  # noqa: E501


        :return: The instance_ids of this InvokeCommandRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._instance_ids

    @instance_ids.setter
    def instance_ids(self, instance_ids):
        """Sets the instance_ids of this InvokeCommandRequest.


        :param instance_ids: The instance_ids of this InvokeCommandRequest.  # noqa: E501
        :type: list[str]
        """

        self._instance_ids = instance_ids

    @property
    def invocation_description(self):
        """Gets the invocation_description of this InvokeCommandRequest.  # noqa: E501


        :return: The invocation_description of this InvokeCommandRequest.  # noqa: E501
        :rtype: str
        """
        return self._invocation_description

    @invocation_description.setter
    def invocation_description(self, invocation_description):
        """Sets the invocation_description of this InvokeCommandRequest.


        :param invocation_description: The invocation_description of this InvokeCommandRequest.  # noqa: E501
        :type: str
        """

        self._invocation_description = invocation_description

    @property
    def invocation_name(self):
        """Gets the invocation_name of this InvokeCommandRequest.  # noqa: E501


        :return: The invocation_name of this InvokeCommandRequest.  # noqa: E501
        :rtype: str
        """
        return self._invocation_name

    @invocation_name.setter
    def invocation_name(self, invocation_name):
        """Sets the invocation_name of this InvokeCommandRequest.


        :param invocation_name: The invocation_name of this InvokeCommandRequest.  # noqa: E501
        :type: str
        """

        self._invocation_name = invocation_name

    @property
    def launch_time(self):
        """Gets the launch_time of this InvokeCommandRequest.  # noqa: E501


        :return: The launch_time of this InvokeCommandRequest.  # noqa: E501
        :rtype: str
        """
        return self._launch_time

    @launch_time.setter
    def launch_time(self, launch_time):
        """Sets the launch_time of this InvokeCommandRequest.


        :param launch_time: The launch_time of this InvokeCommandRequest.  # noqa: E501
        :type: str
        """

        self._launch_time = launch_time

    @property
    def parameters(self):
        """Gets the parameters of this InvokeCommandRequest.  # noqa: E501


        :return: The parameters of this InvokeCommandRequest.  # noqa: E501
        :rtype: str
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this InvokeCommandRequest.


        :param parameters: The parameters of this InvokeCommandRequest.  # noqa: E501
        :type: str
        """

        self._parameters = parameters

    @property
    def project_name(self):
        """Gets the project_name of this InvokeCommandRequest.  # noqa: E501


        :return: The project_name of this InvokeCommandRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this InvokeCommandRequest.


        :param project_name: The project_name of this InvokeCommandRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def recurrence_end_time(self):
        """Gets the recurrence_end_time of this InvokeCommandRequest.  # noqa: E501


        :return: The recurrence_end_time of this InvokeCommandRequest.  # noqa: E501
        :rtype: str
        """
        return self._recurrence_end_time

    @recurrence_end_time.setter
    def recurrence_end_time(self, recurrence_end_time):
        """Sets the recurrence_end_time of this InvokeCommandRequest.


        :param recurrence_end_time: The recurrence_end_time of this InvokeCommandRequest.  # noqa: E501
        :type: str
        """

        self._recurrence_end_time = recurrence_end_time

    @property
    def repeat_mode(self):
        """Gets the repeat_mode of this InvokeCommandRequest.  # noqa: E501


        :return: The repeat_mode of this InvokeCommandRequest.  # noqa: E501
        :rtype: str
        """
        return self._repeat_mode

    @repeat_mode.setter
    def repeat_mode(self, repeat_mode):
        """Sets the repeat_mode of this InvokeCommandRequest.


        :param repeat_mode: The repeat_mode of this InvokeCommandRequest.  # noqa: E501
        :type: str
        """

        self._repeat_mode = repeat_mode

    @property
    def tags(self):
        """Gets the tags of this InvokeCommandRequest.  # noqa: E501


        :return: The tags of this InvokeCommandRequest.  # noqa: E501
        :rtype: list[TagForInvokeCommandInput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this InvokeCommandRequest.


        :param tags: The tags of this InvokeCommandRequest.  # noqa: E501
        :type: list[TagForInvokeCommandInput]
        """

        self._tags = tags

    @property
    def timeout(self):
        """Gets the timeout of this InvokeCommandRequest.  # noqa: E501


        :return: The timeout of this InvokeCommandRequest.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this InvokeCommandRequest.


        :param timeout: The timeout of this InvokeCommandRequest.  # noqa: E501
        :type: int
        """

        self._timeout = timeout

    @property
    def username(self):
        """Gets the username of this InvokeCommandRequest.  # noqa: E501


        :return: The username of this InvokeCommandRequest.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this InvokeCommandRequest.


        :param username: The username of this InvokeCommandRequest.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def working_dir(self):
        """Gets the working_dir of this InvokeCommandRequest.  # noqa: E501


        :return: The working_dir of this InvokeCommandRequest.  # noqa: E501
        :rtype: str
        """
        return self._working_dir

    @working_dir.setter
    def working_dir(self, working_dir):
        """Sets the working_dir of this InvokeCommandRequest.


        :param working_dir: The working_dir of this InvokeCommandRequest.  # noqa: E501
        :type: str
        """

        self._working_dir = working_dir

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
        if issubclass(InvokeCommandRequest, dict):
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
        if not isinstance(other, InvokeCommandRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InvokeCommandRequest):
            return True

        return self.to_dict() != other.to_dict()
