# coding: utf-8

"""
    escloud

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class InstancePluginForDescribeInstancePluginsOutput(object):
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
        'description': 'str',
        'plugin_name': 'str',
        'status': 'str',
        'version': 'str'
    }

    attribute_map = {
        'description': 'Description',
        'plugin_name': 'PluginName',
        'status': 'Status',
        'version': 'Version'
    }

    def __init__(self, description=None, plugin_name=None, status=None, version=None, _configuration=None):  # noqa: E501
        """InstancePluginForDescribeInstancePluginsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._description = None
        self._plugin_name = None
        self._status = None
        self._version = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if plugin_name is not None:
            self.plugin_name = plugin_name
        if status is not None:
            self.status = status
        if version is not None:
            self.version = version

    @property
    def description(self):
        """Gets the description of this InstancePluginForDescribeInstancePluginsOutput.  # noqa: E501


        :return: The description of this InstancePluginForDescribeInstancePluginsOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InstancePluginForDescribeInstancePluginsOutput.


        :param description: The description of this InstancePluginForDescribeInstancePluginsOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def plugin_name(self):
        """Gets the plugin_name of this InstancePluginForDescribeInstancePluginsOutput.  # noqa: E501


        :return: The plugin_name of this InstancePluginForDescribeInstancePluginsOutput.  # noqa: E501
        :rtype: str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        """Sets the plugin_name of this InstancePluginForDescribeInstancePluginsOutput.


        :param plugin_name: The plugin_name of this InstancePluginForDescribeInstancePluginsOutput.  # noqa: E501
        :type: str
        """

        self._plugin_name = plugin_name

    @property
    def status(self):
        """Gets the status of this InstancePluginForDescribeInstancePluginsOutput.  # noqa: E501


        :return: The status of this InstancePluginForDescribeInstancePluginsOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InstancePluginForDescribeInstancePluginsOutput.


        :param status: The status of this InstancePluginForDescribeInstancePluginsOutput.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def version(self):
        """Gets the version of this InstancePluginForDescribeInstancePluginsOutput.  # noqa: E501


        :return: The version of this InstancePluginForDescribeInstancePluginsOutput.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this InstancePluginForDescribeInstancePluginsOutput.


        :param version: The version of this InstancePluginForDescribeInstancePluginsOutput.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if issubclass(InstancePluginForDescribeInstancePluginsOutput, dict):
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
        if not isinstance(other, InstancePluginForDescribeInstancePluginsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InstancePluginForDescribeInstancePluginsOutput):
            return True

        return self.to_dict() != other.to_dict()
