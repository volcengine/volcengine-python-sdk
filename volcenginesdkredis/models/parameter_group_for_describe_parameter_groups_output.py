# coding: utf-8

"""
    redis

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ParameterGroupForDescribeParameterGroupsOutput(object):
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
        'create_time': 'str',
        'default': 'bool',
        'description': 'str',
        'engine_version': 'str',
        'name': 'str',
        'parameter_group_id': 'str',
        'parameter_num': 'int',
        'source': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'create_time': 'CreateTime',
        'default': 'Default',
        'description': 'Description',
        'engine_version': 'EngineVersion',
        'name': 'Name',
        'parameter_group_id': 'ParameterGroupId',
        'parameter_num': 'ParameterNum',
        'source': 'Source',
        'update_time': 'UpdateTime'
    }

    def __init__(self, create_time=None, default=None, description=None, engine_version=None, name=None, parameter_group_id=None, parameter_num=None, source=None, update_time=None, _configuration=None):  # noqa: E501
        """ParameterGroupForDescribeParameterGroupsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._create_time = None
        self._default = None
        self._description = None
        self._engine_version = None
        self._name = None
        self._parameter_group_id = None
        self._parameter_num = None
        self._source = None
        self._update_time = None
        self.discriminator = None

        if create_time is not None:
            self.create_time = create_time
        if default is not None:
            self.default = default
        if description is not None:
            self.description = description
        if engine_version is not None:
            self.engine_version = engine_version
        if name is not None:
            self.name = name
        if parameter_group_id is not None:
            self.parameter_group_id = parameter_group_id
        if parameter_num is not None:
            self.parameter_num = parameter_num
        if source is not None:
            self.source = source
        if update_time is not None:
            self.update_time = update_time

    @property
    def create_time(self):
        """Gets the create_time of this ParameterGroupForDescribeParameterGroupsOutput.  # noqa: E501


        :return: The create_time of this ParameterGroupForDescribeParameterGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ParameterGroupForDescribeParameterGroupsOutput.


        :param create_time: The create_time of this ParameterGroupForDescribeParameterGroupsOutput.  # noqa: E501
        :type: str
        """

        self._create_time = create_time

    @property
    def default(self):
        """Gets the default of this ParameterGroupForDescribeParameterGroupsOutput.  # noqa: E501


        :return: The default of this ParameterGroupForDescribeParameterGroupsOutput.  # noqa: E501
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this ParameterGroupForDescribeParameterGroupsOutput.


        :param default: The default of this ParameterGroupForDescribeParameterGroupsOutput.  # noqa: E501
        :type: bool
        """

        self._default = default

    @property
    def description(self):
        """Gets the description of this ParameterGroupForDescribeParameterGroupsOutput.  # noqa: E501


        :return: The description of this ParameterGroupForDescribeParameterGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ParameterGroupForDescribeParameterGroupsOutput.


        :param description: The description of this ParameterGroupForDescribeParameterGroupsOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def engine_version(self):
        """Gets the engine_version of this ParameterGroupForDescribeParameterGroupsOutput.  # noqa: E501


        :return: The engine_version of this ParameterGroupForDescribeParameterGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        """Sets the engine_version of this ParameterGroupForDescribeParameterGroupsOutput.


        :param engine_version: The engine_version of this ParameterGroupForDescribeParameterGroupsOutput.  # noqa: E501
        :type: str
        """

        self._engine_version = engine_version

    @property
    def name(self):
        """Gets the name of this ParameterGroupForDescribeParameterGroupsOutput.  # noqa: E501


        :return: The name of this ParameterGroupForDescribeParameterGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ParameterGroupForDescribeParameterGroupsOutput.


        :param name: The name of this ParameterGroupForDescribeParameterGroupsOutput.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def parameter_group_id(self):
        """Gets the parameter_group_id of this ParameterGroupForDescribeParameterGroupsOutput.  # noqa: E501


        :return: The parameter_group_id of this ParameterGroupForDescribeParameterGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._parameter_group_id

    @parameter_group_id.setter
    def parameter_group_id(self, parameter_group_id):
        """Sets the parameter_group_id of this ParameterGroupForDescribeParameterGroupsOutput.


        :param parameter_group_id: The parameter_group_id of this ParameterGroupForDescribeParameterGroupsOutput.  # noqa: E501
        :type: str
        """

        self._parameter_group_id = parameter_group_id

    @property
    def parameter_num(self):
        """Gets the parameter_num of this ParameterGroupForDescribeParameterGroupsOutput.  # noqa: E501


        :return: The parameter_num of this ParameterGroupForDescribeParameterGroupsOutput.  # noqa: E501
        :rtype: int
        """
        return self._parameter_num

    @parameter_num.setter
    def parameter_num(self, parameter_num):
        """Sets the parameter_num of this ParameterGroupForDescribeParameterGroupsOutput.


        :param parameter_num: The parameter_num of this ParameterGroupForDescribeParameterGroupsOutput.  # noqa: E501
        :type: int
        """

        self._parameter_num = parameter_num

    @property
    def source(self):
        """Gets the source of this ParameterGroupForDescribeParameterGroupsOutput.  # noqa: E501


        :return: The source of this ParameterGroupForDescribeParameterGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this ParameterGroupForDescribeParameterGroupsOutput.


        :param source: The source of this ParameterGroupForDescribeParameterGroupsOutput.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def update_time(self):
        """Gets the update_time of this ParameterGroupForDescribeParameterGroupsOutput.  # noqa: E501


        :return: The update_time of this ParameterGroupForDescribeParameterGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ParameterGroupForDescribeParameterGroupsOutput.


        :param update_time: The update_time of this ParameterGroupForDescribeParameterGroupsOutput.  # noqa: E501
        :type: str
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
        if issubclass(ParameterGroupForDescribeParameterGroupsOutput, dict):
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
        if not isinstance(other, ParameterGroupForDescribeParameterGroupsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ParameterGroupForDescribeParameterGroupsOutput):
            return True

        return self.to_dict() != other.to_dict()
