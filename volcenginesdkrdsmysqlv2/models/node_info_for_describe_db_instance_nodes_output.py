# coding: utf-8

"""
    rds_mysql_v2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class NodeInfoForDescribeDBInstanceNodesOutput(object):
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
        'cpu_used_percentage': 'float',
        'last_io_error': 'str',
        'last_sql_error': 'str',
        'memory_used_percentage': 'float',
        'node_id': 'str',
        'node_status': 'str',
        'node_type': 'str',
        'slave_io_running': 'bool',
        'slave_sql_running': 'bool',
        'space_used_percentage': 'float',
        'sync_delay': 'int',
        'zone_id': 'str'
    }

    attribute_map = {
        'cpu_used_percentage': 'CPUUsedPercentage',
        'last_io_error': 'LastIOError',
        'last_sql_error': 'LastSQLError',
        'memory_used_percentage': 'MemoryUsedPercentage',
        'node_id': 'NodeId',
        'node_status': 'NodeStatus',
        'node_type': 'NodeType',
        'slave_io_running': 'SlaveIORunning',
        'slave_sql_running': 'SlaveSQLRunning',
        'space_used_percentage': 'SpaceUsedPercentage',
        'sync_delay': 'SyncDelay',
        'zone_id': 'ZoneId'
    }

    def __init__(self, cpu_used_percentage=None, last_io_error=None, last_sql_error=None, memory_used_percentage=None, node_id=None, node_status=None, node_type=None, slave_io_running=None, slave_sql_running=None, space_used_percentage=None, sync_delay=None, zone_id=None, _configuration=None):  # noqa: E501
        """NodeInfoForDescribeDBInstanceNodesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cpu_used_percentage = None
        self._last_io_error = None
        self._last_sql_error = None
        self._memory_used_percentage = None
        self._node_id = None
        self._node_status = None
        self._node_type = None
        self._slave_io_running = None
        self._slave_sql_running = None
        self._space_used_percentage = None
        self._sync_delay = None
        self._zone_id = None
        self.discriminator = None

        if cpu_used_percentage is not None:
            self.cpu_used_percentage = cpu_used_percentage
        if last_io_error is not None:
            self.last_io_error = last_io_error
        if last_sql_error is not None:
            self.last_sql_error = last_sql_error
        if memory_used_percentage is not None:
            self.memory_used_percentage = memory_used_percentage
        if node_id is not None:
            self.node_id = node_id
        if node_status is not None:
            self.node_status = node_status
        if node_type is not None:
            self.node_type = node_type
        if slave_io_running is not None:
            self.slave_io_running = slave_io_running
        if slave_sql_running is not None:
            self.slave_sql_running = slave_sql_running
        if space_used_percentage is not None:
            self.space_used_percentage = space_used_percentage
        if sync_delay is not None:
            self.sync_delay = sync_delay
        if zone_id is not None:
            self.zone_id = zone_id

    @property
    def cpu_used_percentage(self):
        """Gets the cpu_used_percentage of this NodeInfoForDescribeDBInstanceNodesOutput.  # noqa: E501


        :return: The cpu_used_percentage of this NodeInfoForDescribeDBInstanceNodesOutput.  # noqa: E501
        :rtype: float
        """
        return self._cpu_used_percentage

    @cpu_used_percentage.setter
    def cpu_used_percentage(self, cpu_used_percentage):
        """Sets the cpu_used_percentage of this NodeInfoForDescribeDBInstanceNodesOutput.


        :param cpu_used_percentage: The cpu_used_percentage of this NodeInfoForDescribeDBInstanceNodesOutput.  # noqa: E501
        :type: float
        """

        self._cpu_used_percentage = cpu_used_percentage

    @property
    def last_io_error(self):
        """Gets the last_io_error of this NodeInfoForDescribeDBInstanceNodesOutput.  # noqa: E501


        :return: The last_io_error of this NodeInfoForDescribeDBInstanceNodesOutput.  # noqa: E501
        :rtype: str
        """
        return self._last_io_error

    @last_io_error.setter
    def last_io_error(self, last_io_error):
        """Sets the last_io_error of this NodeInfoForDescribeDBInstanceNodesOutput.


        :param last_io_error: The last_io_error of this NodeInfoForDescribeDBInstanceNodesOutput.  # noqa: E501
        :type: str
        """

        self._last_io_error = last_io_error

    @property
    def last_sql_error(self):
        """Gets the last_sql_error of this NodeInfoForDescribeDBInstanceNodesOutput.  # noqa: E501


        :return: The last_sql_error of this NodeInfoForDescribeDBInstanceNodesOutput.  # noqa: E501
        :rtype: str
        """
        return self._last_sql_error

    @last_sql_error.setter
    def last_sql_error(self, last_sql_error):
        """Sets the last_sql_error of this NodeInfoForDescribeDBInstanceNodesOutput.


        :param last_sql_error: The last_sql_error of this NodeInfoForDescribeDBInstanceNodesOutput.  # noqa: E501
        :type: str
        """

        self._last_sql_error = last_sql_error

    @property
    def memory_used_percentage(self):
        """Gets the memory_used_percentage of this NodeInfoForDescribeDBInstanceNodesOutput.  # noqa: E501


        :return: The memory_used_percentage of this NodeInfoForDescribeDBInstanceNodesOutput.  # noqa: E501
        :rtype: float
        """
        return self._memory_used_percentage

    @memory_used_percentage.setter
    def memory_used_percentage(self, memory_used_percentage):
        """Sets the memory_used_percentage of this NodeInfoForDescribeDBInstanceNodesOutput.


        :param memory_used_percentage: The memory_used_percentage of this NodeInfoForDescribeDBInstanceNodesOutput.  # noqa: E501
        :type: float
        """

        self._memory_used_percentage = memory_used_percentage

    @property
    def node_id(self):
        """Gets the node_id of this NodeInfoForDescribeDBInstanceNodesOutput.  # noqa: E501


        :return: The node_id of this NodeInfoForDescribeDBInstanceNodesOutput.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this NodeInfoForDescribeDBInstanceNodesOutput.


        :param node_id: The node_id of this NodeInfoForDescribeDBInstanceNodesOutput.  # noqa: E501
        :type: str
        """

        self._node_id = node_id

    @property
    def node_status(self):
        """Gets the node_status of this NodeInfoForDescribeDBInstanceNodesOutput.  # noqa: E501


        :return: The node_status of this NodeInfoForDescribeDBInstanceNodesOutput.  # noqa: E501
        :rtype: str
        """
        return self._node_status

    @node_status.setter
    def node_status(self, node_status):
        """Sets the node_status of this NodeInfoForDescribeDBInstanceNodesOutput.


        :param node_status: The node_status of this NodeInfoForDescribeDBInstanceNodesOutput.  # noqa: E501
        :type: str
        """

        self._node_status = node_status

    @property
    def node_type(self):
        """Gets the node_type of this NodeInfoForDescribeDBInstanceNodesOutput.  # noqa: E501


        :return: The node_type of this NodeInfoForDescribeDBInstanceNodesOutput.  # noqa: E501
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this NodeInfoForDescribeDBInstanceNodesOutput.


        :param node_type: The node_type of this NodeInfoForDescribeDBInstanceNodesOutput.  # noqa: E501
        :type: str
        """

        self._node_type = node_type

    @property
    def slave_io_running(self):
        """Gets the slave_io_running of this NodeInfoForDescribeDBInstanceNodesOutput.  # noqa: E501


        :return: The slave_io_running of this NodeInfoForDescribeDBInstanceNodesOutput.  # noqa: E501
        :rtype: bool
        """
        return self._slave_io_running

    @slave_io_running.setter
    def slave_io_running(self, slave_io_running):
        """Sets the slave_io_running of this NodeInfoForDescribeDBInstanceNodesOutput.


        :param slave_io_running: The slave_io_running of this NodeInfoForDescribeDBInstanceNodesOutput.  # noqa: E501
        :type: bool
        """

        self._slave_io_running = slave_io_running

    @property
    def slave_sql_running(self):
        """Gets the slave_sql_running of this NodeInfoForDescribeDBInstanceNodesOutput.  # noqa: E501


        :return: The slave_sql_running of this NodeInfoForDescribeDBInstanceNodesOutput.  # noqa: E501
        :rtype: bool
        """
        return self._slave_sql_running

    @slave_sql_running.setter
    def slave_sql_running(self, slave_sql_running):
        """Sets the slave_sql_running of this NodeInfoForDescribeDBInstanceNodesOutput.


        :param slave_sql_running: The slave_sql_running of this NodeInfoForDescribeDBInstanceNodesOutput.  # noqa: E501
        :type: bool
        """

        self._slave_sql_running = slave_sql_running

    @property
    def space_used_percentage(self):
        """Gets the space_used_percentage of this NodeInfoForDescribeDBInstanceNodesOutput.  # noqa: E501


        :return: The space_used_percentage of this NodeInfoForDescribeDBInstanceNodesOutput.  # noqa: E501
        :rtype: float
        """
        return self._space_used_percentage

    @space_used_percentage.setter
    def space_used_percentage(self, space_used_percentage):
        """Sets the space_used_percentage of this NodeInfoForDescribeDBInstanceNodesOutput.


        :param space_used_percentage: The space_used_percentage of this NodeInfoForDescribeDBInstanceNodesOutput.  # noqa: E501
        :type: float
        """

        self._space_used_percentage = space_used_percentage

    @property
    def sync_delay(self):
        """Gets the sync_delay of this NodeInfoForDescribeDBInstanceNodesOutput.  # noqa: E501


        :return: The sync_delay of this NodeInfoForDescribeDBInstanceNodesOutput.  # noqa: E501
        :rtype: int
        """
        return self._sync_delay

    @sync_delay.setter
    def sync_delay(self, sync_delay):
        """Sets the sync_delay of this NodeInfoForDescribeDBInstanceNodesOutput.


        :param sync_delay: The sync_delay of this NodeInfoForDescribeDBInstanceNodesOutput.  # noqa: E501
        :type: int
        """

        self._sync_delay = sync_delay

    @property
    def zone_id(self):
        """Gets the zone_id of this NodeInfoForDescribeDBInstanceNodesOutput.  # noqa: E501


        :return: The zone_id of this NodeInfoForDescribeDBInstanceNodesOutput.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this NodeInfoForDescribeDBInstanceNodesOutput.


        :param zone_id: The zone_id of this NodeInfoForDescribeDBInstanceNodesOutput.  # noqa: E501
        :type: str
        """

        self._zone_id = zone_id

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
        if issubclass(NodeInfoForDescribeDBInstanceNodesOutput, dict):
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
        if not isinstance(other, NodeInfoForDescribeDBInstanceNodesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NodeInfoForDescribeDBInstanceNodesOutput):
            return True

        return self.to_dict() != other.to_dict()
