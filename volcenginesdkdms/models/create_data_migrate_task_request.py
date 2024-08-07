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


class CreateDataMigrateTaskRequest(object):
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
        'advance_config': 'AdvanceConfigForCreateDataMigrateTaskInput',
        'basic_config': 'BasicConfigForCreateDataMigrateTaskInput',
        'source': 'SourceForCreateDataMigrateTaskInput',
        'target': 'TargetForCreateDataMigrateTaskInput'
    }

    attribute_map = {
        'advance_config': 'AdvanceConfig',
        'basic_config': 'BasicConfig',
        'source': 'Source',
        'target': 'Target'
    }

    def __init__(self, advance_config=None, basic_config=None, source=None, target=None, _configuration=None):  # noqa: E501
        """CreateDataMigrateTaskRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._advance_config = None
        self._basic_config = None
        self._source = None
        self._target = None
        self.discriminator = None

        if advance_config is not None:
            self.advance_config = advance_config
        if basic_config is not None:
            self.basic_config = basic_config
        if source is not None:
            self.source = source
        if target is not None:
            self.target = target

    @property
    def advance_config(self):
        """Gets the advance_config of this CreateDataMigrateTaskRequest.  # noqa: E501


        :return: The advance_config of this CreateDataMigrateTaskRequest.  # noqa: E501
        :rtype: AdvanceConfigForCreateDataMigrateTaskInput
        """
        return self._advance_config

    @advance_config.setter
    def advance_config(self, advance_config):
        """Sets the advance_config of this CreateDataMigrateTaskRequest.


        :param advance_config: The advance_config of this CreateDataMigrateTaskRequest.  # noqa: E501
        :type: AdvanceConfigForCreateDataMigrateTaskInput
        """

        self._advance_config = advance_config

    @property
    def basic_config(self):
        """Gets the basic_config of this CreateDataMigrateTaskRequest.  # noqa: E501


        :return: The basic_config of this CreateDataMigrateTaskRequest.  # noqa: E501
        :rtype: BasicConfigForCreateDataMigrateTaskInput
        """
        return self._basic_config

    @basic_config.setter
    def basic_config(self, basic_config):
        """Sets the basic_config of this CreateDataMigrateTaskRequest.


        :param basic_config: The basic_config of this CreateDataMigrateTaskRequest.  # noqa: E501
        :type: BasicConfigForCreateDataMigrateTaskInput
        """

        self._basic_config = basic_config

    @property
    def source(self):
        """Gets the source of this CreateDataMigrateTaskRequest.  # noqa: E501


        :return: The source of this CreateDataMigrateTaskRequest.  # noqa: E501
        :rtype: SourceForCreateDataMigrateTaskInput
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this CreateDataMigrateTaskRequest.


        :param source: The source of this CreateDataMigrateTaskRequest.  # noqa: E501
        :type: SourceForCreateDataMigrateTaskInput
        """

        self._source = source

    @property
    def target(self):
        """Gets the target of this CreateDataMigrateTaskRequest.  # noqa: E501


        :return: The target of this CreateDataMigrateTaskRequest.  # noqa: E501
        :rtype: TargetForCreateDataMigrateTaskInput
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this CreateDataMigrateTaskRequest.


        :param target: The target of this CreateDataMigrateTaskRequest.  # noqa: E501
        :type: TargetForCreateDataMigrateTaskInput
        """

        self._target = target

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
        if issubclass(CreateDataMigrateTaskRequest, dict):
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
        if not isinstance(other, CreateDataMigrateTaskRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateDataMigrateTaskRequest):
            return True

        return self.to_dict() != other.to_dict()
