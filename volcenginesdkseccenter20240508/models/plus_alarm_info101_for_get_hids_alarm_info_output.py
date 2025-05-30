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


class PlusAlarmInfo101ForGetHidsAlarmInfoOutput(object):
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
        'ptrace_request': 'str',
        'target_argv': 'str',
        'target_pid': 'str'
    }

    attribute_map = {
        'ptrace_request': 'PtraceRequest',
        'target_argv': 'TargetArgv',
        'target_pid': 'TargetPid'
    }

    def __init__(self, ptrace_request=None, target_argv=None, target_pid=None, _configuration=None):  # noqa: E501
        """PlusAlarmInfo101ForGetHidsAlarmInfoOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._ptrace_request = None
        self._target_argv = None
        self._target_pid = None
        self.discriminator = None

        if ptrace_request is not None:
            self.ptrace_request = ptrace_request
        if target_argv is not None:
            self.target_argv = target_argv
        if target_pid is not None:
            self.target_pid = target_pid

    @property
    def ptrace_request(self):
        """Gets the ptrace_request of this PlusAlarmInfo101ForGetHidsAlarmInfoOutput.  # noqa: E501


        :return: The ptrace_request of this PlusAlarmInfo101ForGetHidsAlarmInfoOutput.  # noqa: E501
        :rtype: str
        """
        return self._ptrace_request

    @ptrace_request.setter
    def ptrace_request(self, ptrace_request):
        """Sets the ptrace_request of this PlusAlarmInfo101ForGetHidsAlarmInfoOutput.


        :param ptrace_request: The ptrace_request of this PlusAlarmInfo101ForGetHidsAlarmInfoOutput.  # noqa: E501
        :type: str
        """

        self._ptrace_request = ptrace_request

    @property
    def target_argv(self):
        """Gets the target_argv of this PlusAlarmInfo101ForGetHidsAlarmInfoOutput.  # noqa: E501


        :return: The target_argv of this PlusAlarmInfo101ForGetHidsAlarmInfoOutput.  # noqa: E501
        :rtype: str
        """
        return self._target_argv

    @target_argv.setter
    def target_argv(self, target_argv):
        """Sets the target_argv of this PlusAlarmInfo101ForGetHidsAlarmInfoOutput.


        :param target_argv: The target_argv of this PlusAlarmInfo101ForGetHidsAlarmInfoOutput.  # noqa: E501
        :type: str
        """

        self._target_argv = target_argv

    @property
    def target_pid(self):
        """Gets the target_pid of this PlusAlarmInfo101ForGetHidsAlarmInfoOutput.  # noqa: E501


        :return: The target_pid of this PlusAlarmInfo101ForGetHidsAlarmInfoOutput.  # noqa: E501
        :rtype: str
        """
        return self._target_pid

    @target_pid.setter
    def target_pid(self, target_pid):
        """Sets the target_pid of this PlusAlarmInfo101ForGetHidsAlarmInfoOutput.


        :param target_pid: The target_pid of this PlusAlarmInfo101ForGetHidsAlarmInfoOutput.  # noqa: E501
        :type: str
        """

        self._target_pid = target_pid

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
        if issubclass(PlusAlarmInfo101ForGetHidsAlarmInfoOutput, dict):
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
        if not isinstance(other, PlusAlarmInfo101ForGetHidsAlarmInfoOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PlusAlarmInfo101ForGetHidsAlarmInfoOutput):
            return True

        return self.to_dict() != other.to_dict()
