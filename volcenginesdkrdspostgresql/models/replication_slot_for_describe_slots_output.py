# coding: utf-8

"""
    rds_postgresql

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ReplicationSlotForDescribeSlotsOutput(object):
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
        'database': 'str',
        'ip_address': 'str',
        'plugin': 'str',
        'slot_name': 'str',
        'slot_status': 'str',
        'slot_type': 'str',
        'temporary': 'bool',
        'wal_delay': 'int'
    }

    attribute_map = {
        'database': 'Database',
        'ip_address': 'IPAddress',
        'plugin': 'Plugin',
        'slot_name': 'SlotName',
        'slot_status': 'SlotStatus',
        'slot_type': 'SlotType',
        'temporary': 'Temporary',
        'wal_delay': 'WalDelay'
    }

    def __init__(self, database=None, ip_address=None, plugin=None, slot_name=None, slot_status=None, slot_type=None, temporary=None, wal_delay=None, _configuration=None):  # noqa: E501
        """ReplicationSlotForDescribeSlotsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._database = None
        self._ip_address = None
        self._plugin = None
        self._slot_name = None
        self._slot_status = None
        self._slot_type = None
        self._temporary = None
        self._wal_delay = None
        self.discriminator = None

        if database is not None:
            self.database = database
        if ip_address is not None:
            self.ip_address = ip_address
        if plugin is not None:
            self.plugin = plugin
        if slot_name is not None:
            self.slot_name = slot_name
        if slot_status is not None:
            self.slot_status = slot_status
        if slot_type is not None:
            self.slot_type = slot_type
        if temporary is not None:
            self.temporary = temporary
        if wal_delay is not None:
            self.wal_delay = wal_delay

    @property
    def database(self):
        """Gets the database of this ReplicationSlotForDescribeSlotsOutput.  # noqa: E501


        :return: The database of this ReplicationSlotForDescribeSlotsOutput.  # noqa: E501
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        """Sets the database of this ReplicationSlotForDescribeSlotsOutput.


        :param database: The database of this ReplicationSlotForDescribeSlotsOutput.  # noqa: E501
        :type: str
        """

        self._database = database

    @property
    def ip_address(self):
        """Gets the ip_address of this ReplicationSlotForDescribeSlotsOutput.  # noqa: E501


        :return: The ip_address of this ReplicationSlotForDescribeSlotsOutput.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this ReplicationSlotForDescribeSlotsOutput.


        :param ip_address: The ip_address of this ReplicationSlotForDescribeSlotsOutput.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

    @property
    def plugin(self):
        """Gets the plugin of this ReplicationSlotForDescribeSlotsOutput.  # noqa: E501


        :return: The plugin of this ReplicationSlotForDescribeSlotsOutput.  # noqa: E501
        :rtype: str
        """
        return self._plugin

    @plugin.setter
    def plugin(self, plugin):
        """Sets the plugin of this ReplicationSlotForDescribeSlotsOutput.


        :param plugin: The plugin of this ReplicationSlotForDescribeSlotsOutput.  # noqa: E501
        :type: str
        """

        self._plugin = plugin

    @property
    def slot_name(self):
        """Gets the slot_name of this ReplicationSlotForDescribeSlotsOutput.  # noqa: E501


        :return: The slot_name of this ReplicationSlotForDescribeSlotsOutput.  # noqa: E501
        :rtype: str
        """
        return self._slot_name

    @slot_name.setter
    def slot_name(self, slot_name):
        """Sets the slot_name of this ReplicationSlotForDescribeSlotsOutput.


        :param slot_name: The slot_name of this ReplicationSlotForDescribeSlotsOutput.  # noqa: E501
        :type: str
        """

        self._slot_name = slot_name

    @property
    def slot_status(self):
        """Gets the slot_status of this ReplicationSlotForDescribeSlotsOutput.  # noqa: E501


        :return: The slot_status of this ReplicationSlotForDescribeSlotsOutput.  # noqa: E501
        :rtype: str
        """
        return self._slot_status

    @slot_status.setter
    def slot_status(self, slot_status):
        """Sets the slot_status of this ReplicationSlotForDescribeSlotsOutput.


        :param slot_status: The slot_status of this ReplicationSlotForDescribeSlotsOutput.  # noqa: E501
        :type: str
        """

        self._slot_status = slot_status

    @property
    def slot_type(self):
        """Gets the slot_type of this ReplicationSlotForDescribeSlotsOutput.  # noqa: E501


        :return: The slot_type of this ReplicationSlotForDescribeSlotsOutput.  # noqa: E501
        :rtype: str
        """
        return self._slot_type

    @slot_type.setter
    def slot_type(self, slot_type):
        """Sets the slot_type of this ReplicationSlotForDescribeSlotsOutput.


        :param slot_type: The slot_type of this ReplicationSlotForDescribeSlotsOutput.  # noqa: E501
        :type: str
        """

        self._slot_type = slot_type

    @property
    def temporary(self):
        """Gets the temporary of this ReplicationSlotForDescribeSlotsOutput.  # noqa: E501


        :return: The temporary of this ReplicationSlotForDescribeSlotsOutput.  # noqa: E501
        :rtype: bool
        """
        return self._temporary

    @temporary.setter
    def temporary(self, temporary):
        """Sets the temporary of this ReplicationSlotForDescribeSlotsOutput.


        :param temporary: The temporary of this ReplicationSlotForDescribeSlotsOutput.  # noqa: E501
        :type: bool
        """

        self._temporary = temporary

    @property
    def wal_delay(self):
        """Gets the wal_delay of this ReplicationSlotForDescribeSlotsOutput.  # noqa: E501


        :return: The wal_delay of this ReplicationSlotForDescribeSlotsOutput.  # noqa: E501
        :rtype: int
        """
        return self._wal_delay

    @wal_delay.setter
    def wal_delay(self, wal_delay):
        """Sets the wal_delay of this ReplicationSlotForDescribeSlotsOutput.


        :param wal_delay: The wal_delay of this ReplicationSlotForDescribeSlotsOutput.  # noqa: E501
        :type: int
        """

        self._wal_delay = wal_delay

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
        if issubclass(ReplicationSlotForDescribeSlotsOutput, dict):
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
        if not isinstance(other, ReplicationSlotForDescribeSlotsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReplicationSlotForDescribeSlotsOutput):
            return True

        return self.to_dict() != other.to_dict()
