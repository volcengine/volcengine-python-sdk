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


class CommAlarmInfoForGetHidsAlarmInfoOutput(object):
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
        'argv': 'str',
        '_exec': 'str',
        'pgid': 'str',
        'pgid_argv': 'str',
        'pid': 'str',
        'ppid': 'str',
        'ppid_argv': 'str',
        'username': 'str'
    }

    attribute_map = {
        'argv': 'Argv',
        '_exec': 'Exec',
        'pgid': 'Pgid',
        'pgid_argv': 'PgidArgv',
        'pid': 'Pid',
        'ppid': 'Ppid',
        'ppid_argv': 'PpidArgv',
        'username': 'Username'
    }

    def __init__(self, argv=None, _exec=None, pgid=None, pgid_argv=None, pid=None, ppid=None, ppid_argv=None, username=None, _configuration=None):  # noqa: E501
        """CommAlarmInfoForGetHidsAlarmInfoOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._argv = None
        self.__exec = None
        self._pgid = None
        self._pgid_argv = None
        self._pid = None
        self._ppid = None
        self._ppid_argv = None
        self._username = None
        self.discriminator = None

        if argv is not None:
            self.argv = argv
        if _exec is not None:
            self._exec = _exec
        if pgid is not None:
            self.pgid = pgid
        if pgid_argv is not None:
            self.pgid_argv = pgid_argv
        if pid is not None:
            self.pid = pid
        if ppid is not None:
            self.ppid = ppid
        if ppid_argv is not None:
            self.ppid_argv = ppid_argv
        if username is not None:
            self.username = username

    @property
    def argv(self):
        """Gets the argv of this CommAlarmInfoForGetHidsAlarmInfoOutput.  # noqa: E501


        :return: The argv of this CommAlarmInfoForGetHidsAlarmInfoOutput.  # noqa: E501
        :rtype: str
        """
        return self._argv

    @argv.setter
    def argv(self, argv):
        """Sets the argv of this CommAlarmInfoForGetHidsAlarmInfoOutput.


        :param argv: The argv of this CommAlarmInfoForGetHidsAlarmInfoOutput.  # noqa: E501
        :type: str
        """

        self._argv = argv

    @property
    def _exec(self):
        """Gets the _exec of this CommAlarmInfoForGetHidsAlarmInfoOutput.  # noqa: E501


        :return: The _exec of this CommAlarmInfoForGetHidsAlarmInfoOutput.  # noqa: E501
        :rtype: str
        """
        return self.__exec

    @_exec.setter
    def _exec(self, _exec):
        """Sets the _exec of this CommAlarmInfoForGetHidsAlarmInfoOutput.


        :param _exec: The _exec of this CommAlarmInfoForGetHidsAlarmInfoOutput.  # noqa: E501
        :type: str
        """

        self.__exec = _exec

    @property
    def pgid(self):
        """Gets the pgid of this CommAlarmInfoForGetHidsAlarmInfoOutput.  # noqa: E501


        :return: The pgid of this CommAlarmInfoForGetHidsAlarmInfoOutput.  # noqa: E501
        :rtype: str
        """
        return self._pgid

    @pgid.setter
    def pgid(self, pgid):
        """Sets the pgid of this CommAlarmInfoForGetHidsAlarmInfoOutput.


        :param pgid: The pgid of this CommAlarmInfoForGetHidsAlarmInfoOutput.  # noqa: E501
        :type: str
        """

        self._pgid = pgid

    @property
    def pgid_argv(self):
        """Gets the pgid_argv of this CommAlarmInfoForGetHidsAlarmInfoOutput.  # noqa: E501


        :return: The pgid_argv of this CommAlarmInfoForGetHidsAlarmInfoOutput.  # noqa: E501
        :rtype: str
        """
        return self._pgid_argv

    @pgid_argv.setter
    def pgid_argv(self, pgid_argv):
        """Sets the pgid_argv of this CommAlarmInfoForGetHidsAlarmInfoOutput.


        :param pgid_argv: The pgid_argv of this CommAlarmInfoForGetHidsAlarmInfoOutput.  # noqa: E501
        :type: str
        """

        self._pgid_argv = pgid_argv

    @property
    def pid(self):
        """Gets the pid of this CommAlarmInfoForGetHidsAlarmInfoOutput.  # noqa: E501


        :return: The pid of this CommAlarmInfoForGetHidsAlarmInfoOutput.  # noqa: E501
        :rtype: str
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        """Sets the pid of this CommAlarmInfoForGetHidsAlarmInfoOutput.


        :param pid: The pid of this CommAlarmInfoForGetHidsAlarmInfoOutput.  # noqa: E501
        :type: str
        """

        self._pid = pid

    @property
    def ppid(self):
        """Gets the ppid of this CommAlarmInfoForGetHidsAlarmInfoOutput.  # noqa: E501


        :return: The ppid of this CommAlarmInfoForGetHidsAlarmInfoOutput.  # noqa: E501
        :rtype: str
        """
        return self._ppid

    @ppid.setter
    def ppid(self, ppid):
        """Sets the ppid of this CommAlarmInfoForGetHidsAlarmInfoOutput.


        :param ppid: The ppid of this CommAlarmInfoForGetHidsAlarmInfoOutput.  # noqa: E501
        :type: str
        """

        self._ppid = ppid

    @property
    def ppid_argv(self):
        """Gets the ppid_argv of this CommAlarmInfoForGetHidsAlarmInfoOutput.  # noqa: E501


        :return: The ppid_argv of this CommAlarmInfoForGetHidsAlarmInfoOutput.  # noqa: E501
        :rtype: str
        """
        return self._ppid_argv

    @ppid_argv.setter
    def ppid_argv(self, ppid_argv):
        """Sets the ppid_argv of this CommAlarmInfoForGetHidsAlarmInfoOutput.


        :param ppid_argv: The ppid_argv of this CommAlarmInfoForGetHidsAlarmInfoOutput.  # noqa: E501
        :type: str
        """

        self._ppid_argv = ppid_argv

    @property
    def username(self):
        """Gets the username of this CommAlarmInfoForGetHidsAlarmInfoOutput.  # noqa: E501


        :return: The username of this CommAlarmInfoForGetHidsAlarmInfoOutput.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this CommAlarmInfoForGetHidsAlarmInfoOutput.


        :param username: The username of this CommAlarmInfoForGetHidsAlarmInfoOutput.  # noqa: E501
        :type: str
        """

        self._username = username

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
        if issubclass(CommAlarmInfoForGetHidsAlarmInfoOutput, dict):
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
        if not isinstance(other, CommAlarmInfoForGetHidsAlarmInfoOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CommAlarmInfoForGetHidsAlarmInfoOutput):
            return True

        return self.to_dict() != other.to_dict()
