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


class PlusAlarmInfo59ForGetAlarmBySmithKeyOutput(object):
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
        'comm': 'str',
        'ld_preload': 'str',
        'pid_tree': 'str',
        'run_path': 'str',
        'socket_argv': 'str',
        'socket_pid': 'str',
        'ssh': 'str',
        'ssh_info': 'str',
        'stdin': 'str',
        'stdout': 'str',
        'uid': 'str'
    }

    attribute_map = {
        'comm': 'Comm',
        'ld_preload': 'LdPreload',
        'pid_tree': 'PidTree',
        'run_path': 'RunPath',
        'socket_argv': 'SocketArgv',
        'socket_pid': 'SocketPid',
        'ssh': 'Ssh',
        'ssh_info': 'SshInfo',
        'stdin': 'Stdin',
        'stdout': 'Stdout',
        'uid': 'Uid'
    }

    def __init__(self, comm=None, ld_preload=None, pid_tree=None, run_path=None, socket_argv=None, socket_pid=None, ssh=None, ssh_info=None, stdin=None, stdout=None, uid=None, _configuration=None):  # noqa: E501
        """PlusAlarmInfo59ForGetAlarmBySmithKeyOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._comm = None
        self._ld_preload = None
        self._pid_tree = None
        self._run_path = None
        self._socket_argv = None
        self._socket_pid = None
        self._ssh = None
        self._ssh_info = None
        self._stdin = None
        self._stdout = None
        self._uid = None
        self.discriminator = None

        if comm is not None:
            self.comm = comm
        if ld_preload is not None:
            self.ld_preload = ld_preload
        if pid_tree is not None:
            self.pid_tree = pid_tree
        if run_path is not None:
            self.run_path = run_path
        if socket_argv is not None:
            self.socket_argv = socket_argv
        if socket_pid is not None:
            self.socket_pid = socket_pid
        if ssh is not None:
            self.ssh = ssh
        if ssh_info is not None:
            self.ssh_info = ssh_info
        if stdin is not None:
            self.stdin = stdin
        if stdout is not None:
            self.stdout = stdout
        if uid is not None:
            self.uid = uid

    @property
    def comm(self):
        """Gets the comm of this PlusAlarmInfo59ForGetAlarmBySmithKeyOutput.  # noqa: E501


        :return: The comm of this PlusAlarmInfo59ForGetAlarmBySmithKeyOutput.  # noqa: E501
        :rtype: str
        """
        return self._comm

    @comm.setter
    def comm(self, comm):
        """Sets the comm of this PlusAlarmInfo59ForGetAlarmBySmithKeyOutput.


        :param comm: The comm of this PlusAlarmInfo59ForGetAlarmBySmithKeyOutput.  # noqa: E501
        :type: str
        """

        self._comm = comm

    @property
    def ld_preload(self):
        """Gets the ld_preload of this PlusAlarmInfo59ForGetAlarmBySmithKeyOutput.  # noqa: E501


        :return: The ld_preload of this PlusAlarmInfo59ForGetAlarmBySmithKeyOutput.  # noqa: E501
        :rtype: str
        """
        return self._ld_preload

    @ld_preload.setter
    def ld_preload(self, ld_preload):
        """Sets the ld_preload of this PlusAlarmInfo59ForGetAlarmBySmithKeyOutput.


        :param ld_preload: The ld_preload of this PlusAlarmInfo59ForGetAlarmBySmithKeyOutput.  # noqa: E501
        :type: str
        """

        self._ld_preload = ld_preload

    @property
    def pid_tree(self):
        """Gets the pid_tree of this PlusAlarmInfo59ForGetAlarmBySmithKeyOutput.  # noqa: E501


        :return: The pid_tree of this PlusAlarmInfo59ForGetAlarmBySmithKeyOutput.  # noqa: E501
        :rtype: str
        """
        return self._pid_tree

    @pid_tree.setter
    def pid_tree(self, pid_tree):
        """Sets the pid_tree of this PlusAlarmInfo59ForGetAlarmBySmithKeyOutput.


        :param pid_tree: The pid_tree of this PlusAlarmInfo59ForGetAlarmBySmithKeyOutput.  # noqa: E501
        :type: str
        """

        self._pid_tree = pid_tree

    @property
    def run_path(self):
        """Gets the run_path of this PlusAlarmInfo59ForGetAlarmBySmithKeyOutput.  # noqa: E501


        :return: The run_path of this PlusAlarmInfo59ForGetAlarmBySmithKeyOutput.  # noqa: E501
        :rtype: str
        """
        return self._run_path

    @run_path.setter
    def run_path(self, run_path):
        """Sets the run_path of this PlusAlarmInfo59ForGetAlarmBySmithKeyOutput.


        :param run_path: The run_path of this PlusAlarmInfo59ForGetAlarmBySmithKeyOutput.  # noqa: E501
        :type: str
        """

        self._run_path = run_path

    @property
    def socket_argv(self):
        """Gets the socket_argv of this PlusAlarmInfo59ForGetAlarmBySmithKeyOutput.  # noqa: E501


        :return: The socket_argv of this PlusAlarmInfo59ForGetAlarmBySmithKeyOutput.  # noqa: E501
        :rtype: str
        """
        return self._socket_argv

    @socket_argv.setter
    def socket_argv(self, socket_argv):
        """Sets the socket_argv of this PlusAlarmInfo59ForGetAlarmBySmithKeyOutput.


        :param socket_argv: The socket_argv of this PlusAlarmInfo59ForGetAlarmBySmithKeyOutput.  # noqa: E501
        :type: str
        """

        self._socket_argv = socket_argv

    @property
    def socket_pid(self):
        """Gets the socket_pid of this PlusAlarmInfo59ForGetAlarmBySmithKeyOutput.  # noqa: E501


        :return: The socket_pid of this PlusAlarmInfo59ForGetAlarmBySmithKeyOutput.  # noqa: E501
        :rtype: str
        """
        return self._socket_pid

    @socket_pid.setter
    def socket_pid(self, socket_pid):
        """Sets the socket_pid of this PlusAlarmInfo59ForGetAlarmBySmithKeyOutput.


        :param socket_pid: The socket_pid of this PlusAlarmInfo59ForGetAlarmBySmithKeyOutput.  # noqa: E501
        :type: str
        """

        self._socket_pid = socket_pid

    @property
    def ssh(self):
        """Gets the ssh of this PlusAlarmInfo59ForGetAlarmBySmithKeyOutput.  # noqa: E501


        :return: The ssh of this PlusAlarmInfo59ForGetAlarmBySmithKeyOutput.  # noqa: E501
        :rtype: str
        """
        return self._ssh

    @ssh.setter
    def ssh(self, ssh):
        """Sets the ssh of this PlusAlarmInfo59ForGetAlarmBySmithKeyOutput.


        :param ssh: The ssh of this PlusAlarmInfo59ForGetAlarmBySmithKeyOutput.  # noqa: E501
        :type: str
        """

        self._ssh = ssh

    @property
    def ssh_info(self):
        """Gets the ssh_info of this PlusAlarmInfo59ForGetAlarmBySmithKeyOutput.  # noqa: E501


        :return: The ssh_info of this PlusAlarmInfo59ForGetAlarmBySmithKeyOutput.  # noqa: E501
        :rtype: str
        """
        return self._ssh_info

    @ssh_info.setter
    def ssh_info(self, ssh_info):
        """Sets the ssh_info of this PlusAlarmInfo59ForGetAlarmBySmithKeyOutput.


        :param ssh_info: The ssh_info of this PlusAlarmInfo59ForGetAlarmBySmithKeyOutput.  # noqa: E501
        :type: str
        """

        self._ssh_info = ssh_info

    @property
    def stdin(self):
        """Gets the stdin of this PlusAlarmInfo59ForGetAlarmBySmithKeyOutput.  # noqa: E501


        :return: The stdin of this PlusAlarmInfo59ForGetAlarmBySmithKeyOutput.  # noqa: E501
        :rtype: str
        """
        return self._stdin

    @stdin.setter
    def stdin(self, stdin):
        """Sets the stdin of this PlusAlarmInfo59ForGetAlarmBySmithKeyOutput.


        :param stdin: The stdin of this PlusAlarmInfo59ForGetAlarmBySmithKeyOutput.  # noqa: E501
        :type: str
        """

        self._stdin = stdin

    @property
    def stdout(self):
        """Gets the stdout of this PlusAlarmInfo59ForGetAlarmBySmithKeyOutput.  # noqa: E501


        :return: The stdout of this PlusAlarmInfo59ForGetAlarmBySmithKeyOutput.  # noqa: E501
        :rtype: str
        """
        return self._stdout

    @stdout.setter
    def stdout(self, stdout):
        """Sets the stdout of this PlusAlarmInfo59ForGetAlarmBySmithKeyOutput.


        :param stdout: The stdout of this PlusAlarmInfo59ForGetAlarmBySmithKeyOutput.  # noqa: E501
        :type: str
        """

        self._stdout = stdout

    @property
    def uid(self):
        """Gets the uid of this PlusAlarmInfo59ForGetAlarmBySmithKeyOutput.  # noqa: E501


        :return: The uid of this PlusAlarmInfo59ForGetAlarmBySmithKeyOutput.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this PlusAlarmInfo59ForGetAlarmBySmithKeyOutput.


        :param uid: The uid of this PlusAlarmInfo59ForGetAlarmBySmithKeyOutput.  # noqa: E501
        :type: str
        """

        self._uid = uid

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
        if issubclass(PlusAlarmInfo59ForGetAlarmBySmithKeyOutput, dict):
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
        if not isinstance(other, PlusAlarmInfo59ForGetAlarmBySmithKeyOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PlusAlarmInfo59ForGetAlarmBySmithKeyOutput):
            return True

        return self.to_dict() != other.to_dict()
