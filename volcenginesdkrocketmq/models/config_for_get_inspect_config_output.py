# coding: utf-8

"""
    rocketmq

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ConfigForGetInspectConfigOutput(object):
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
        'configurable': 'ConfigurableForGetInspectConfigOutput',
        'describe': 'str',
        'inspect_name': 'str',
        'start_inspect_time_stamp': 'str',
        'type': 'str'
    }

    attribute_map = {
        'configurable': 'Configurable',
        'describe': 'Describe',
        'inspect_name': 'InspectName',
        'start_inspect_time_stamp': 'StartInspectTimeStamp',
        'type': 'Type'
    }

    def __init__(self, configurable=None, describe=None, inspect_name=None, start_inspect_time_stamp=None, type=None, _configuration=None):  # noqa: E501
        """ConfigForGetInspectConfigOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._configurable = None
        self._describe = None
        self._inspect_name = None
        self._start_inspect_time_stamp = None
        self._type = None
        self.discriminator = None

        if configurable is not None:
            self.configurable = configurable
        if describe is not None:
            self.describe = describe
        if inspect_name is not None:
            self.inspect_name = inspect_name
        if start_inspect_time_stamp is not None:
            self.start_inspect_time_stamp = start_inspect_time_stamp
        if type is not None:
            self.type = type

    @property
    def configurable(self):
        """Gets the configurable of this ConfigForGetInspectConfigOutput.  # noqa: E501


        :return: The configurable of this ConfigForGetInspectConfigOutput.  # noqa: E501
        :rtype: ConfigurableForGetInspectConfigOutput
        """
        return self._configurable

    @configurable.setter
    def configurable(self, configurable):
        """Sets the configurable of this ConfigForGetInspectConfigOutput.


        :param configurable: The configurable of this ConfigForGetInspectConfigOutput.  # noqa: E501
        :type: ConfigurableForGetInspectConfigOutput
        """

        self._configurable = configurable

    @property
    def describe(self):
        """Gets the describe of this ConfigForGetInspectConfigOutput.  # noqa: E501


        :return: The describe of this ConfigForGetInspectConfigOutput.  # noqa: E501
        :rtype: str
        """
        return self._describe

    @describe.setter
    def describe(self, describe):
        """Sets the describe of this ConfigForGetInspectConfigOutput.


        :param describe: The describe of this ConfigForGetInspectConfigOutput.  # noqa: E501
        :type: str
        """

        self._describe = describe

    @property
    def inspect_name(self):
        """Gets the inspect_name of this ConfigForGetInspectConfigOutput.  # noqa: E501


        :return: The inspect_name of this ConfigForGetInspectConfigOutput.  # noqa: E501
        :rtype: str
        """
        return self._inspect_name

    @inspect_name.setter
    def inspect_name(self, inspect_name):
        """Sets the inspect_name of this ConfigForGetInspectConfigOutput.


        :param inspect_name: The inspect_name of this ConfigForGetInspectConfigOutput.  # noqa: E501
        :type: str
        """

        self._inspect_name = inspect_name

    @property
    def start_inspect_time_stamp(self):
        """Gets the start_inspect_time_stamp of this ConfigForGetInspectConfigOutput.  # noqa: E501


        :return: The start_inspect_time_stamp of this ConfigForGetInspectConfigOutput.  # noqa: E501
        :rtype: str
        """
        return self._start_inspect_time_stamp

    @start_inspect_time_stamp.setter
    def start_inspect_time_stamp(self, start_inspect_time_stamp):
        """Sets the start_inspect_time_stamp of this ConfigForGetInspectConfigOutput.


        :param start_inspect_time_stamp: The start_inspect_time_stamp of this ConfigForGetInspectConfigOutput.  # noqa: E501
        :type: str
        """

        self._start_inspect_time_stamp = start_inspect_time_stamp

    @property
    def type(self):
        """Gets the type of this ConfigForGetInspectConfigOutput.  # noqa: E501


        :return: The type of this ConfigForGetInspectConfigOutput.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ConfigForGetInspectConfigOutput.


        :param type: The type of this ConfigForGetInspectConfigOutput.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(ConfigForGetInspectConfigOutput, dict):
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
        if not isinstance(other, ConfigForGetInspectConfigOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConfigForGetInspectConfigOutput):
            return True

        return self.to_dict() != other.to_dict()