# coding: utf-8

"""
    vpn

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ModifyVpnConnectionHealthCheckerRequest(object):
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
        'check_interval': 'int',
        'checker_id': 'str',
        'client_token': 'str',
        'down_time': 'int',
        'local_ip': 'str',
        'remote_ip': 'str',
        'timeout': 'int',
        'up_time': 'int',
        'vpn_connection_id': 'str'
    }

    attribute_map = {
        'check_interval': 'CheckInterval',
        'checker_id': 'CheckerId',
        'client_token': 'ClientToken',
        'down_time': 'DownTime',
        'local_ip': 'LocalIp',
        'remote_ip': 'RemoteIp',
        'timeout': 'Timeout',
        'up_time': 'UpTime',
        'vpn_connection_id': 'VpnConnectionId'
    }

    def __init__(self, check_interval=None, checker_id=None, client_token=None, down_time=None, local_ip=None, remote_ip=None, timeout=None, up_time=None, vpn_connection_id=None, _configuration=None):  # noqa: E501
        """ModifyVpnConnectionHealthCheckerRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._check_interval = None
        self._checker_id = None
        self._client_token = None
        self._down_time = None
        self._local_ip = None
        self._remote_ip = None
        self._timeout = None
        self._up_time = None
        self._vpn_connection_id = None
        self.discriminator = None

        self.check_interval = check_interval
        self.checker_id = checker_id
        if client_token is not None:
            self.client_token = client_token
        if down_time is not None:
            self.down_time = down_time
        if local_ip is not None:
            self.local_ip = local_ip
        if remote_ip is not None:
            self.remote_ip = remote_ip
        if timeout is not None:
            self.timeout = timeout
        if up_time is not None:
            self.up_time = up_time
        self.vpn_connection_id = vpn_connection_id

    @property
    def check_interval(self):
        """Gets the check_interval of this ModifyVpnConnectionHealthCheckerRequest.  # noqa: E501


        :return: The check_interval of this ModifyVpnConnectionHealthCheckerRequest.  # noqa: E501
        :rtype: int
        """
        return self._check_interval

    @check_interval.setter
    def check_interval(self, check_interval):
        """Sets the check_interval of this ModifyVpnConnectionHealthCheckerRequest.


        :param check_interval: The check_interval of this ModifyVpnConnectionHealthCheckerRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and check_interval is None:
            raise ValueError("Invalid value for `check_interval`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                check_interval is not None and check_interval > 300):  # noqa: E501
            raise ValueError("Invalid value for `check_interval`, must be a value less than or equal to `300`")  # noqa: E501
        if (self._configuration.client_side_validation and
                check_interval is not None and check_interval < 3):  # noqa: E501
            raise ValueError("Invalid value for `check_interval`, must be a value greater than or equal to `3`")  # noqa: E501

        self._check_interval = check_interval

    @property
    def checker_id(self):
        """Gets the checker_id of this ModifyVpnConnectionHealthCheckerRequest.  # noqa: E501


        :return: The checker_id of this ModifyVpnConnectionHealthCheckerRequest.  # noqa: E501
        :rtype: str
        """
        return self._checker_id

    @checker_id.setter
    def checker_id(self, checker_id):
        """Sets the checker_id of this ModifyVpnConnectionHealthCheckerRequest.


        :param checker_id: The checker_id of this ModifyVpnConnectionHealthCheckerRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and checker_id is None:
            raise ValueError("Invalid value for `checker_id`, must not be `None`")  # noqa: E501

        self._checker_id = checker_id

    @property
    def client_token(self):
        """Gets the client_token of this ModifyVpnConnectionHealthCheckerRequest.  # noqa: E501


        :return: The client_token of this ModifyVpnConnectionHealthCheckerRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_token

    @client_token.setter
    def client_token(self, client_token):
        """Sets the client_token of this ModifyVpnConnectionHealthCheckerRequest.


        :param client_token: The client_token of this ModifyVpnConnectionHealthCheckerRequest.  # noqa: E501
        :type: str
        """

        self._client_token = client_token

    @property
    def down_time(self):
        """Gets the down_time of this ModifyVpnConnectionHealthCheckerRequest.  # noqa: E501


        :return: The down_time of this ModifyVpnConnectionHealthCheckerRequest.  # noqa: E501
        :rtype: int
        """
        return self._down_time

    @down_time.setter
    def down_time(self, down_time):
        """Sets the down_time of this ModifyVpnConnectionHealthCheckerRequest.


        :param down_time: The down_time of this ModifyVpnConnectionHealthCheckerRequest.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                down_time is not None and down_time > 10):  # noqa: E501
            raise ValueError("Invalid value for `down_time`, must be a value less than or equal to `10`")  # noqa: E501
        if (self._configuration.client_side_validation and
                down_time is not None and down_time < 1):  # noqa: E501
            raise ValueError("Invalid value for `down_time`, must be a value greater than or equal to `1`")  # noqa: E501

        self._down_time = down_time

    @property
    def local_ip(self):
        """Gets the local_ip of this ModifyVpnConnectionHealthCheckerRequest.  # noqa: E501


        :return: The local_ip of this ModifyVpnConnectionHealthCheckerRequest.  # noqa: E501
        :rtype: str
        """
        return self._local_ip

    @local_ip.setter
    def local_ip(self, local_ip):
        """Sets the local_ip of this ModifyVpnConnectionHealthCheckerRequest.


        :param local_ip: The local_ip of this ModifyVpnConnectionHealthCheckerRequest.  # noqa: E501
        :type: str
        """

        self._local_ip = local_ip

    @property
    def remote_ip(self):
        """Gets the remote_ip of this ModifyVpnConnectionHealthCheckerRequest.  # noqa: E501


        :return: The remote_ip of this ModifyVpnConnectionHealthCheckerRequest.  # noqa: E501
        :rtype: str
        """
        return self._remote_ip

    @remote_ip.setter
    def remote_ip(self, remote_ip):
        """Sets the remote_ip of this ModifyVpnConnectionHealthCheckerRequest.


        :param remote_ip: The remote_ip of this ModifyVpnConnectionHealthCheckerRequest.  # noqa: E501
        :type: str
        """

        self._remote_ip = remote_ip

    @property
    def timeout(self):
        """Gets the timeout of this ModifyVpnConnectionHealthCheckerRequest.  # noqa: E501


        :return: The timeout of this ModifyVpnConnectionHealthCheckerRequest.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this ModifyVpnConnectionHealthCheckerRequest.


        :param timeout: The timeout of this ModifyVpnConnectionHealthCheckerRequest.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                timeout is not None and timeout > 300):  # noqa: E501
            raise ValueError("Invalid value for `timeout`, must be a value less than or equal to `300`")  # noqa: E501
        if (self._configuration.client_side_validation and
                timeout is not None and timeout < 1):  # noqa: E501
            raise ValueError("Invalid value for `timeout`, must be a value greater than or equal to `1`")  # noqa: E501

        self._timeout = timeout

    @property
    def up_time(self):
        """Gets the up_time of this ModifyVpnConnectionHealthCheckerRequest.  # noqa: E501


        :return: The up_time of this ModifyVpnConnectionHealthCheckerRequest.  # noqa: E501
        :rtype: int
        """
        return self._up_time

    @up_time.setter
    def up_time(self, up_time):
        """Sets the up_time of this ModifyVpnConnectionHealthCheckerRequest.


        :param up_time: The up_time of this ModifyVpnConnectionHealthCheckerRequest.  # noqa: E501
        :type: int
        """

        self._up_time = up_time

    @property
    def vpn_connection_id(self):
        """Gets the vpn_connection_id of this ModifyVpnConnectionHealthCheckerRequest.  # noqa: E501


        :return: The vpn_connection_id of this ModifyVpnConnectionHealthCheckerRequest.  # noqa: E501
        :rtype: str
        """
        return self._vpn_connection_id

    @vpn_connection_id.setter
    def vpn_connection_id(self, vpn_connection_id):
        """Sets the vpn_connection_id of this ModifyVpnConnectionHealthCheckerRequest.


        :param vpn_connection_id: The vpn_connection_id of this ModifyVpnConnectionHealthCheckerRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and vpn_connection_id is None:
            raise ValueError("Invalid value for `vpn_connection_id`, must not be `None`")  # noqa: E501

        self._vpn_connection_id = vpn_connection_id

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
        if issubclass(ModifyVpnConnectionHealthCheckerRequest, dict):
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
        if not isinstance(other, ModifyVpnConnectionHealthCheckerRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModifyVpnConnectionHealthCheckerRequest):
            return True

        return self.to_dict() != other.to_dict()