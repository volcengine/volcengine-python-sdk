# coding: utf-8

"""
    cloud_detect

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class PingConfigForCreateTaskInput(object):
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
        'connect_timeout': 'float',
        'enable_divide_package': 'bool',
        'execute_interval': 'float',
        'packages_num': 'int',
        'packages_size': 'int',
        'protocol_type': 'int',
        'timeout': 'int'
    }

    attribute_map = {
        'connect_timeout': 'ConnectTimeout',
        'enable_divide_package': 'EnableDividePackage',
        'execute_interval': 'ExecuteInterval',
        'packages_num': 'PackagesNum',
        'packages_size': 'PackagesSize',
        'protocol_type': 'ProtocolType',
        'timeout': 'Timeout'
    }

    def __init__(self, connect_timeout=None, enable_divide_package=None, execute_interval=None, packages_num=None, packages_size=None, protocol_type=None, timeout=None, _configuration=None):  # noqa: E501
        """PingConfigForCreateTaskInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._connect_timeout = None
        self._enable_divide_package = None
        self._execute_interval = None
        self._packages_num = None
        self._packages_size = None
        self._protocol_type = None
        self._timeout = None
        self.discriminator = None

        if connect_timeout is not None:
            self.connect_timeout = connect_timeout
        if enable_divide_package is not None:
            self.enable_divide_package = enable_divide_package
        if execute_interval is not None:
            self.execute_interval = execute_interval
        if packages_num is not None:
            self.packages_num = packages_num
        if packages_size is not None:
            self.packages_size = packages_size
        if protocol_type is not None:
            self.protocol_type = protocol_type
        if timeout is not None:
            self.timeout = timeout

    @property
    def connect_timeout(self):
        """Gets the connect_timeout of this PingConfigForCreateTaskInput.  # noqa: E501


        :return: The connect_timeout of this PingConfigForCreateTaskInput.  # noqa: E501
        :rtype: float
        """
        return self._connect_timeout

    @connect_timeout.setter
    def connect_timeout(self, connect_timeout):
        """Sets the connect_timeout of this PingConfigForCreateTaskInput.


        :param connect_timeout: The connect_timeout of this PingConfigForCreateTaskInput.  # noqa: E501
        :type: float
        """

        self._connect_timeout = connect_timeout

    @property
    def enable_divide_package(self):
        """Gets the enable_divide_package of this PingConfigForCreateTaskInput.  # noqa: E501


        :return: The enable_divide_package of this PingConfigForCreateTaskInput.  # noqa: E501
        :rtype: bool
        """
        return self._enable_divide_package

    @enable_divide_package.setter
    def enable_divide_package(self, enable_divide_package):
        """Sets the enable_divide_package of this PingConfigForCreateTaskInput.


        :param enable_divide_package: The enable_divide_package of this PingConfigForCreateTaskInput.  # noqa: E501
        :type: bool
        """

        self._enable_divide_package = enable_divide_package

    @property
    def execute_interval(self):
        """Gets the execute_interval of this PingConfigForCreateTaskInput.  # noqa: E501


        :return: The execute_interval of this PingConfigForCreateTaskInput.  # noqa: E501
        :rtype: float
        """
        return self._execute_interval

    @execute_interval.setter
    def execute_interval(self, execute_interval):
        """Sets the execute_interval of this PingConfigForCreateTaskInput.


        :param execute_interval: The execute_interval of this PingConfigForCreateTaskInput.  # noqa: E501
        :type: float
        """

        self._execute_interval = execute_interval

    @property
    def packages_num(self):
        """Gets the packages_num of this PingConfigForCreateTaskInput.  # noqa: E501


        :return: The packages_num of this PingConfigForCreateTaskInput.  # noqa: E501
        :rtype: int
        """
        return self._packages_num

    @packages_num.setter
    def packages_num(self, packages_num):
        """Sets the packages_num of this PingConfigForCreateTaskInput.


        :param packages_num: The packages_num of this PingConfigForCreateTaskInput.  # noqa: E501
        :type: int
        """

        self._packages_num = packages_num

    @property
    def packages_size(self):
        """Gets the packages_size of this PingConfigForCreateTaskInput.  # noqa: E501


        :return: The packages_size of this PingConfigForCreateTaskInput.  # noqa: E501
        :rtype: int
        """
        return self._packages_size

    @packages_size.setter
    def packages_size(self, packages_size):
        """Sets the packages_size of this PingConfigForCreateTaskInput.


        :param packages_size: The packages_size of this PingConfigForCreateTaskInput.  # noqa: E501
        :type: int
        """

        self._packages_size = packages_size

    @property
    def protocol_type(self):
        """Gets the protocol_type of this PingConfigForCreateTaskInput.  # noqa: E501


        :return: The protocol_type of this PingConfigForCreateTaskInput.  # noqa: E501
        :rtype: int
        """
        return self._protocol_type

    @protocol_type.setter
    def protocol_type(self, protocol_type):
        """Sets the protocol_type of this PingConfigForCreateTaskInput.


        :param protocol_type: The protocol_type of this PingConfigForCreateTaskInput.  # noqa: E501
        :type: int
        """

        self._protocol_type = protocol_type

    @property
    def timeout(self):
        """Gets the timeout of this PingConfigForCreateTaskInput.  # noqa: E501


        :return: The timeout of this PingConfigForCreateTaskInput.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this PingConfigForCreateTaskInput.


        :param timeout: The timeout of this PingConfigForCreateTaskInput.  # noqa: E501
        :type: int
        """

        self._timeout = timeout

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
        if issubclass(PingConfigForCreateTaskInput, dict):
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
        if not isinstance(other, PingConfigForCreateTaskInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PingConfigForCreateTaskInput):
            return True

        return self.to_dict() != other.to_dict()
