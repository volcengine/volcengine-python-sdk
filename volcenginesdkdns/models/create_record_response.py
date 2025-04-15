# coding: utf-8

"""
    dns

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class CreateRecordResponse(object):
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
        'created_at': 'str',
        'enable': 'bool',
        'fqdn': 'str',
        'host': 'str',
        'line': 'str',
        'operators': 'list[str]',
        'pqdn': 'str',
        'record_id': 'str',
        'record_set_id': 'str',
        'remark': 'str',
        'ttl': 'int',
        'tags': 'list[str]',
        'type': 'str',
        'updated_at': 'str',
        'value': 'str',
        'weight': 'int'
    }

    attribute_map = {
        'created_at': 'CreatedAt',
        'enable': 'Enable',
        'fqdn': 'FQDN',
        'host': 'Host',
        'line': 'Line',
        'operators': 'Operators',
        'pqdn': 'PQDN',
        'record_id': 'RecordID',
        'record_set_id': 'RecordSetID',
        'remark': 'Remark',
        'ttl': 'TTL',
        'tags': 'Tags',
        'type': 'Type',
        'updated_at': 'UpdatedAt',
        'value': 'Value',
        'weight': 'Weight'
    }

    def __init__(self, created_at=None, enable=None, fqdn=None, host=None, line=None, operators=None, pqdn=None, record_id=None, record_set_id=None, remark=None, ttl=None, tags=None, type=None, updated_at=None, value=None, weight=None, _configuration=None):  # noqa: E501
        """CreateRecordResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._created_at = None
        self._enable = None
        self._fqdn = None
        self._host = None
        self._line = None
        self._operators = None
        self._pqdn = None
        self._record_id = None
        self._record_set_id = None
        self._remark = None
        self._ttl = None
        self._tags = None
        self._type = None
        self._updated_at = None
        self._value = None
        self._weight = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if enable is not None:
            self.enable = enable
        if fqdn is not None:
            self.fqdn = fqdn
        if host is not None:
            self.host = host
        if line is not None:
            self.line = line
        if operators is not None:
            self.operators = operators
        if pqdn is not None:
            self.pqdn = pqdn
        if record_id is not None:
            self.record_id = record_id
        if record_set_id is not None:
            self.record_set_id = record_set_id
        if remark is not None:
            self.remark = remark
        if ttl is not None:
            self.ttl = ttl
        if tags is not None:
            self.tags = tags
        if type is not None:
            self.type = type
        if updated_at is not None:
            self.updated_at = updated_at
        if value is not None:
            self.value = value
        if weight is not None:
            self.weight = weight

    @property
    def created_at(self):
        """Gets the created_at of this CreateRecordResponse.  # noqa: E501


        :return: The created_at of this CreateRecordResponse.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this CreateRecordResponse.


        :param created_at: The created_at of this CreateRecordResponse.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def enable(self):
        """Gets the enable of this CreateRecordResponse.  # noqa: E501


        :return: The enable of this CreateRecordResponse.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this CreateRecordResponse.


        :param enable: The enable of this CreateRecordResponse.  # noqa: E501
        :type: bool
        """

        self._enable = enable

    @property
    def fqdn(self):
        """Gets the fqdn of this CreateRecordResponse.  # noqa: E501


        :return: The fqdn of this CreateRecordResponse.  # noqa: E501
        :rtype: str
        """
        return self._fqdn

    @fqdn.setter
    def fqdn(self, fqdn):
        """Sets the fqdn of this CreateRecordResponse.


        :param fqdn: The fqdn of this CreateRecordResponse.  # noqa: E501
        :type: str
        """

        self._fqdn = fqdn

    @property
    def host(self):
        """Gets the host of this CreateRecordResponse.  # noqa: E501


        :return: The host of this CreateRecordResponse.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this CreateRecordResponse.


        :param host: The host of this CreateRecordResponse.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def line(self):
        """Gets the line of this CreateRecordResponse.  # noqa: E501


        :return: The line of this CreateRecordResponse.  # noqa: E501
        :rtype: str
        """
        return self._line

    @line.setter
    def line(self, line):
        """Sets the line of this CreateRecordResponse.


        :param line: The line of this CreateRecordResponse.  # noqa: E501
        :type: str
        """

        self._line = line

    @property
    def operators(self):
        """Gets the operators of this CreateRecordResponse.  # noqa: E501


        :return: The operators of this CreateRecordResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._operators

    @operators.setter
    def operators(self, operators):
        """Sets the operators of this CreateRecordResponse.


        :param operators: The operators of this CreateRecordResponse.  # noqa: E501
        :type: list[str]
        """

        self._operators = operators

    @property
    def pqdn(self):
        """Gets the pqdn of this CreateRecordResponse.  # noqa: E501


        :return: The pqdn of this CreateRecordResponse.  # noqa: E501
        :rtype: str
        """
        return self._pqdn

    @pqdn.setter
    def pqdn(self, pqdn):
        """Sets the pqdn of this CreateRecordResponse.


        :param pqdn: The pqdn of this CreateRecordResponse.  # noqa: E501
        :type: str
        """

        self._pqdn = pqdn

    @property
    def record_id(self):
        """Gets the record_id of this CreateRecordResponse.  # noqa: E501


        :return: The record_id of this CreateRecordResponse.  # noqa: E501
        :rtype: str
        """
        return self._record_id

    @record_id.setter
    def record_id(self, record_id):
        """Sets the record_id of this CreateRecordResponse.


        :param record_id: The record_id of this CreateRecordResponse.  # noqa: E501
        :type: str
        """

        self._record_id = record_id

    @property
    def record_set_id(self):
        """Gets the record_set_id of this CreateRecordResponse.  # noqa: E501


        :return: The record_set_id of this CreateRecordResponse.  # noqa: E501
        :rtype: str
        """
        return self._record_set_id

    @record_set_id.setter
    def record_set_id(self, record_set_id):
        """Sets the record_set_id of this CreateRecordResponse.


        :param record_set_id: The record_set_id of this CreateRecordResponse.  # noqa: E501
        :type: str
        """

        self._record_set_id = record_set_id

    @property
    def remark(self):
        """Gets the remark of this CreateRecordResponse.  # noqa: E501


        :return: The remark of this CreateRecordResponse.  # noqa: E501
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this CreateRecordResponse.


        :param remark: The remark of this CreateRecordResponse.  # noqa: E501
        :type: str
        """

        self._remark = remark

    @property
    def ttl(self):
        """Gets the ttl of this CreateRecordResponse.  # noqa: E501


        :return: The ttl of this CreateRecordResponse.  # noqa: E501
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this CreateRecordResponse.


        :param ttl: The ttl of this CreateRecordResponse.  # noqa: E501
        :type: int
        """

        self._ttl = ttl

    @property
    def tags(self):
        """Gets the tags of this CreateRecordResponse.  # noqa: E501


        :return: The tags of this CreateRecordResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateRecordResponse.


        :param tags: The tags of this CreateRecordResponse.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def type(self):
        """Gets the type of this CreateRecordResponse.  # noqa: E501


        :return: The type of this CreateRecordResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateRecordResponse.


        :param type: The type of this CreateRecordResponse.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def updated_at(self):
        """Gets the updated_at of this CreateRecordResponse.  # noqa: E501


        :return: The updated_at of this CreateRecordResponse.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this CreateRecordResponse.


        :param updated_at: The updated_at of this CreateRecordResponse.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

    @property
    def value(self):
        """Gets the value of this CreateRecordResponse.  # noqa: E501


        :return: The value of this CreateRecordResponse.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CreateRecordResponse.


        :param value: The value of this CreateRecordResponse.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def weight(self):
        """Gets the weight of this CreateRecordResponse.  # noqa: E501


        :return: The weight of this CreateRecordResponse.  # noqa: E501
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this CreateRecordResponse.


        :param weight: The weight of this CreateRecordResponse.  # noqa: E501
        :type: int
        """

        self._weight = weight

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
        if issubclass(CreateRecordResponse, dict):
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
        if not isinstance(other, CreateRecordResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateRecordResponse):
            return True

        return self.to_dict() != other.to_dict()
