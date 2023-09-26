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


class CommandForDescribeCommandsOutput(object):
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
        'command_content': 'str',
        'command_id': 'str',
        'created_at': 'str',
        'description': 'str',
        'enable_parameter': 'bool',
        'invocation_times': 'int',
        'name': 'str',
        'parameter_definitions': 'list[ParameterDefinitionForDescribeCommandsOutput]',
        'provider': 'str',
        'timeout': 'int',
        'type': 'str',
        'updated_at': 'str',
        'username': 'str',
        'working_dir': 'str'
    }

    attribute_map = {
        'command_content': 'CommandContent',
        'command_id': 'CommandId',
        'created_at': 'CreatedAt',
        'description': 'Description',
        'enable_parameter': 'EnableParameter',
        'invocation_times': 'InvocationTimes',
        'name': 'Name',
        'parameter_definitions': 'ParameterDefinitions',
        'provider': 'Provider',
        'timeout': 'Timeout',
        'type': 'Type',
        'updated_at': 'UpdatedAt',
        'username': 'Username',
        'working_dir': 'WorkingDir'
    }

    def __init__(self, command_content=None, command_id=None, created_at=None, description=None, enable_parameter=None, invocation_times=None, name=None, parameter_definitions=None, provider=None, timeout=None, type=None, updated_at=None, username=None, working_dir=None, _configuration=None):  # noqa: E501
        """CommandForDescribeCommandsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._command_content = None
        self._command_id = None
        self._created_at = None
        self._description = None
        self._enable_parameter = None
        self._invocation_times = None
        self._name = None
        self._parameter_definitions = None
        self._provider = None
        self._timeout = None
        self._type = None
        self._updated_at = None
        self._username = None
        self._working_dir = None
        self.discriminator = None

        if command_content is not None:
            self.command_content = command_content
        if command_id is not None:
            self.command_id = command_id
        if created_at is not None:
            self.created_at = created_at
        if description is not None:
            self.description = description
        if enable_parameter is not None:
            self.enable_parameter = enable_parameter
        if invocation_times is not None:
            self.invocation_times = invocation_times
        if name is not None:
            self.name = name
        if parameter_definitions is not None:
            self.parameter_definitions = parameter_definitions
        if provider is not None:
            self.provider = provider
        if timeout is not None:
            self.timeout = timeout
        if type is not None:
            self.type = type
        if updated_at is not None:
            self.updated_at = updated_at
        if username is not None:
            self.username = username
        if working_dir is not None:
            self.working_dir = working_dir

    @property
    def command_content(self):
        """Gets the command_content of this CommandForDescribeCommandsOutput.  # noqa: E501


        :return: The command_content of this CommandForDescribeCommandsOutput.  # noqa: E501
        :rtype: str
        """
        return self._command_content

    @command_content.setter
    def command_content(self, command_content):
        """Sets the command_content of this CommandForDescribeCommandsOutput.


        :param command_content: The command_content of this CommandForDescribeCommandsOutput.  # noqa: E501
        :type: str
        """

        self._command_content = command_content

    @property
    def command_id(self):
        """Gets the command_id of this CommandForDescribeCommandsOutput.  # noqa: E501


        :return: The command_id of this CommandForDescribeCommandsOutput.  # noqa: E501
        :rtype: str
        """
        return self._command_id

    @command_id.setter
    def command_id(self, command_id):
        """Sets the command_id of this CommandForDescribeCommandsOutput.


        :param command_id: The command_id of this CommandForDescribeCommandsOutput.  # noqa: E501
        :type: str
        """

        self._command_id = command_id

    @property
    def created_at(self):
        """Gets the created_at of this CommandForDescribeCommandsOutput.  # noqa: E501


        :return: The created_at of this CommandForDescribeCommandsOutput.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this CommandForDescribeCommandsOutput.


        :param created_at: The created_at of this CommandForDescribeCommandsOutput.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def description(self):
        """Gets the description of this CommandForDescribeCommandsOutput.  # noqa: E501


        :return: The description of this CommandForDescribeCommandsOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CommandForDescribeCommandsOutput.


        :param description: The description of this CommandForDescribeCommandsOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def enable_parameter(self):
        """Gets the enable_parameter of this CommandForDescribeCommandsOutput.  # noqa: E501


        :return: The enable_parameter of this CommandForDescribeCommandsOutput.  # noqa: E501
        :rtype: bool
        """
        return self._enable_parameter

    @enable_parameter.setter
    def enable_parameter(self, enable_parameter):
        """Sets the enable_parameter of this CommandForDescribeCommandsOutput.


        :param enable_parameter: The enable_parameter of this CommandForDescribeCommandsOutput.  # noqa: E501
        :type: bool
        """

        self._enable_parameter = enable_parameter

    @property
    def invocation_times(self):
        """Gets the invocation_times of this CommandForDescribeCommandsOutput.  # noqa: E501


        :return: The invocation_times of this CommandForDescribeCommandsOutput.  # noqa: E501
        :rtype: int
        """
        return self._invocation_times

    @invocation_times.setter
    def invocation_times(self, invocation_times):
        """Sets the invocation_times of this CommandForDescribeCommandsOutput.


        :param invocation_times: The invocation_times of this CommandForDescribeCommandsOutput.  # noqa: E501
        :type: int
        """

        self._invocation_times = invocation_times

    @property
    def name(self):
        """Gets the name of this CommandForDescribeCommandsOutput.  # noqa: E501


        :return: The name of this CommandForDescribeCommandsOutput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CommandForDescribeCommandsOutput.


        :param name: The name of this CommandForDescribeCommandsOutput.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def parameter_definitions(self):
        """Gets the parameter_definitions of this CommandForDescribeCommandsOutput.  # noqa: E501


        :return: The parameter_definitions of this CommandForDescribeCommandsOutput.  # noqa: E501
        :rtype: list[ParameterDefinitionForDescribeCommandsOutput]
        """
        return self._parameter_definitions

    @parameter_definitions.setter
    def parameter_definitions(self, parameter_definitions):
        """Sets the parameter_definitions of this CommandForDescribeCommandsOutput.


        :param parameter_definitions: The parameter_definitions of this CommandForDescribeCommandsOutput.  # noqa: E501
        :type: list[ParameterDefinitionForDescribeCommandsOutput]
        """

        self._parameter_definitions = parameter_definitions

    @property
    def provider(self):
        """Gets the provider of this CommandForDescribeCommandsOutput.  # noqa: E501


        :return: The provider of this CommandForDescribeCommandsOutput.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this CommandForDescribeCommandsOutput.


        :param provider: The provider of this CommandForDescribeCommandsOutput.  # noqa: E501
        :type: str
        """

        self._provider = provider

    @property
    def timeout(self):
        """Gets the timeout of this CommandForDescribeCommandsOutput.  # noqa: E501


        :return: The timeout of this CommandForDescribeCommandsOutput.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this CommandForDescribeCommandsOutput.


        :param timeout: The timeout of this CommandForDescribeCommandsOutput.  # noqa: E501
        :type: int
        """

        self._timeout = timeout

    @property
    def type(self):
        """Gets the type of this CommandForDescribeCommandsOutput.  # noqa: E501


        :return: The type of this CommandForDescribeCommandsOutput.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CommandForDescribeCommandsOutput.


        :param type: The type of this CommandForDescribeCommandsOutput.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def updated_at(self):
        """Gets the updated_at of this CommandForDescribeCommandsOutput.  # noqa: E501


        :return: The updated_at of this CommandForDescribeCommandsOutput.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this CommandForDescribeCommandsOutput.


        :param updated_at: The updated_at of this CommandForDescribeCommandsOutput.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

    @property
    def username(self):
        """Gets the username of this CommandForDescribeCommandsOutput.  # noqa: E501


        :return: The username of this CommandForDescribeCommandsOutput.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this CommandForDescribeCommandsOutput.


        :param username: The username of this CommandForDescribeCommandsOutput.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def working_dir(self):
        """Gets the working_dir of this CommandForDescribeCommandsOutput.  # noqa: E501


        :return: The working_dir of this CommandForDescribeCommandsOutput.  # noqa: E501
        :rtype: str
        """
        return self._working_dir

    @working_dir.setter
    def working_dir(self, working_dir):
        """Sets the working_dir of this CommandForDescribeCommandsOutput.


        :param working_dir: The working_dir of this CommandForDescribeCommandsOutput.  # noqa: E501
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
        if issubclass(CommandForDescribeCommandsOutput, dict):
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
        if not isinstance(other, CommandForDescribeCommandsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CommandForDescribeCommandsOutput):
            return True

        return self.to_dict() != other.to_dict()