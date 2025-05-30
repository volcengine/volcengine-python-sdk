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


class DataForGetFingerprintSoftwareOutput(object):
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
        'agent_id': 'str',
        'agent_tags': 'list[str]',
        'eip_address': 'str',
        'hostname': 'str',
        'id': 'str',
        'name': 'str',
        'primary_ip_address': 'str',
        'start_time': 'int',
        'type': 'str',
        'update_time': 'int',
        'version': 'str'
    }

    attribute_map = {
        'agent_id': 'AgentID',
        'agent_tags': 'AgentTags',
        'eip_address': 'EipAddress',
        'hostname': 'Hostname',
        'id': 'ID',
        'name': 'Name',
        'primary_ip_address': 'PrimaryIpAddress',
        'start_time': 'StartTime',
        'type': 'Type',
        'update_time': 'UpdateTime',
        'version': 'Version'
    }

    def __init__(self, agent_id=None, agent_tags=None, eip_address=None, hostname=None, id=None, name=None, primary_ip_address=None, start_time=None, type=None, update_time=None, version=None, _configuration=None):  # noqa: E501
        """DataForGetFingerprintSoftwareOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._agent_id = None
        self._agent_tags = None
        self._eip_address = None
        self._hostname = None
        self._id = None
        self._name = None
        self._primary_ip_address = None
        self._start_time = None
        self._type = None
        self._update_time = None
        self._version = None
        self.discriminator = None

        if agent_id is not None:
            self.agent_id = agent_id
        if agent_tags is not None:
            self.agent_tags = agent_tags
        if eip_address is not None:
            self.eip_address = eip_address
        if hostname is not None:
            self.hostname = hostname
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if primary_ip_address is not None:
            self.primary_ip_address = primary_ip_address
        if start_time is not None:
            self.start_time = start_time
        if type is not None:
            self.type = type
        if update_time is not None:
            self.update_time = update_time
        if version is not None:
            self.version = version

    @property
    def agent_id(self):
        """Gets the agent_id of this DataForGetFingerprintSoftwareOutput.  # noqa: E501


        :return: The agent_id of this DataForGetFingerprintSoftwareOutput.  # noqa: E501
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """Sets the agent_id of this DataForGetFingerprintSoftwareOutput.


        :param agent_id: The agent_id of this DataForGetFingerprintSoftwareOutput.  # noqa: E501
        :type: str
        """

        self._agent_id = agent_id

    @property
    def agent_tags(self):
        """Gets the agent_tags of this DataForGetFingerprintSoftwareOutput.  # noqa: E501


        :return: The agent_tags of this DataForGetFingerprintSoftwareOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._agent_tags

    @agent_tags.setter
    def agent_tags(self, agent_tags):
        """Sets the agent_tags of this DataForGetFingerprintSoftwareOutput.


        :param agent_tags: The agent_tags of this DataForGetFingerprintSoftwareOutput.  # noqa: E501
        :type: list[str]
        """

        self._agent_tags = agent_tags

    @property
    def eip_address(self):
        """Gets the eip_address of this DataForGetFingerprintSoftwareOutput.  # noqa: E501


        :return: The eip_address of this DataForGetFingerprintSoftwareOutput.  # noqa: E501
        :rtype: str
        """
        return self._eip_address

    @eip_address.setter
    def eip_address(self, eip_address):
        """Sets the eip_address of this DataForGetFingerprintSoftwareOutput.


        :param eip_address: The eip_address of this DataForGetFingerprintSoftwareOutput.  # noqa: E501
        :type: str
        """

        self._eip_address = eip_address

    @property
    def hostname(self):
        """Gets the hostname of this DataForGetFingerprintSoftwareOutput.  # noqa: E501


        :return: The hostname of this DataForGetFingerprintSoftwareOutput.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this DataForGetFingerprintSoftwareOutput.


        :param hostname: The hostname of this DataForGetFingerprintSoftwareOutput.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def id(self):
        """Gets the id of this DataForGetFingerprintSoftwareOutput.  # noqa: E501


        :return: The id of this DataForGetFingerprintSoftwareOutput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DataForGetFingerprintSoftwareOutput.


        :param id: The id of this DataForGetFingerprintSoftwareOutput.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this DataForGetFingerprintSoftwareOutput.  # noqa: E501


        :return: The name of this DataForGetFingerprintSoftwareOutput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DataForGetFingerprintSoftwareOutput.


        :param name: The name of this DataForGetFingerprintSoftwareOutput.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def primary_ip_address(self):
        """Gets the primary_ip_address of this DataForGetFingerprintSoftwareOutput.  # noqa: E501


        :return: The primary_ip_address of this DataForGetFingerprintSoftwareOutput.  # noqa: E501
        :rtype: str
        """
        return self._primary_ip_address

    @primary_ip_address.setter
    def primary_ip_address(self, primary_ip_address):
        """Sets the primary_ip_address of this DataForGetFingerprintSoftwareOutput.


        :param primary_ip_address: The primary_ip_address of this DataForGetFingerprintSoftwareOutput.  # noqa: E501
        :type: str
        """

        self._primary_ip_address = primary_ip_address

    @property
    def start_time(self):
        """Gets the start_time of this DataForGetFingerprintSoftwareOutput.  # noqa: E501


        :return: The start_time of this DataForGetFingerprintSoftwareOutput.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this DataForGetFingerprintSoftwareOutput.


        :param start_time: The start_time of this DataForGetFingerprintSoftwareOutput.  # noqa: E501
        :type: int
        """

        self._start_time = start_time

    @property
    def type(self):
        """Gets the type of this DataForGetFingerprintSoftwareOutput.  # noqa: E501


        :return: The type of this DataForGetFingerprintSoftwareOutput.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DataForGetFingerprintSoftwareOutput.


        :param type: The type of this DataForGetFingerprintSoftwareOutput.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def update_time(self):
        """Gets the update_time of this DataForGetFingerprintSoftwareOutput.  # noqa: E501


        :return: The update_time of this DataForGetFingerprintSoftwareOutput.  # noqa: E501
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this DataForGetFingerprintSoftwareOutput.


        :param update_time: The update_time of this DataForGetFingerprintSoftwareOutput.  # noqa: E501
        :type: int
        """

        self._update_time = update_time

    @property
    def version(self):
        """Gets the version of this DataForGetFingerprintSoftwareOutput.  # noqa: E501


        :return: The version of this DataForGetFingerprintSoftwareOutput.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DataForGetFingerprintSoftwareOutput.


        :param version: The version of this DataForGetFingerprintSoftwareOutput.  # noqa: E501
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
        if issubclass(DataForGetFingerprintSoftwareOutput, dict):
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
        if not isinstance(other, DataForGetFingerprintSoftwareOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataForGetFingerprintSoftwareOutput):
            return True

        return self.to_dict() != other.to_dict()
