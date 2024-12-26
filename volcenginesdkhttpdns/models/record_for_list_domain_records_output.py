# coding: utf-8

"""
    httpdns

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class RecordForListDomainRecordsOutput(object):
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
        'create_time': 'str',
        'enable': 'bool',
        'id': 'int',
        'record_alias': 'str',
        'target': 'list[str]',
        'ttl': 'int',
        'weights': 'list[WeightForListDomainRecordsOutput]'
    }

    attribute_map = {
        'create_time': 'CreateTime',
        'enable': 'Enable',
        'id': 'Id',
        'record_alias': 'RecordAlias',
        'target': 'Target',
        'ttl': 'Ttl',
        'weights': 'Weights'
    }

    def __init__(self, create_time=None, enable=None, id=None, record_alias=None, target=None, ttl=None, weights=None, _configuration=None):  # noqa: E501
        """RecordForListDomainRecordsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._create_time = None
        self._enable = None
        self._id = None
        self._record_alias = None
        self._target = None
        self._ttl = None
        self._weights = None
        self.discriminator = None

        if create_time is not None:
            self.create_time = create_time
        if enable is not None:
            self.enable = enable
        if id is not None:
            self.id = id
        if record_alias is not None:
            self.record_alias = record_alias
        if target is not None:
            self.target = target
        if ttl is not None:
            self.ttl = ttl
        if weights is not None:
            self.weights = weights

    @property
    def create_time(self):
        """Gets the create_time of this RecordForListDomainRecordsOutput.  # noqa: E501


        :return: The create_time of this RecordForListDomainRecordsOutput.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this RecordForListDomainRecordsOutput.


        :param create_time: The create_time of this RecordForListDomainRecordsOutput.  # noqa: E501
        :type: str
        """

        self._create_time = create_time

    @property
    def enable(self):
        """Gets the enable of this RecordForListDomainRecordsOutput.  # noqa: E501


        :return: The enable of this RecordForListDomainRecordsOutput.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this RecordForListDomainRecordsOutput.


        :param enable: The enable of this RecordForListDomainRecordsOutput.  # noqa: E501
        :type: bool
        """

        self._enable = enable

    @property
    def id(self):
        """Gets the id of this RecordForListDomainRecordsOutput.  # noqa: E501


        :return: The id of this RecordForListDomainRecordsOutput.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RecordForListDomainRecordsOutput.


        :param id: The id of this RecordForListDomainRecordsOutput.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def record_alias(self):
        """Gets the record_alias of this RecordForListDomainRecordsOutput.  # noqa: E501


        :return: The record_alias of this RecordForListDomainRecordsOutput.  # noqa: E501
        :rtype: str
        """
        return self._record_alias

    @record_alias.setter
    def record_alias(self, record_alias):
        """Sets the record_alias of this RecordForListDomainRecordsOutput.


        :param record_alias: The record_alias of this RecordForListDomainRecordsOutput.  # noqa: E501
        :type: str
        """

        self._record_alias = record_alias

    @property
    def target(self):
        """Gets the target of this RecordForListDomainRecordsOutput.  # noqa: E501


        :return: The target of this RecordForListDomainRecordsOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this RecordForListDomainRecordsOutput.


        :param target: The target of this RecordForListDomainRecordsOutput.  # noqa: E501
        :type: list[str]
        """

        self._target = target

    @property
    def ttl(self):
        """Gets the ttl of this RecordForListDomainRecordsOutput.  # noqa: E501


        :return: The ttl of this RecordForListDomainRecordsOutput.  # noqa: E501
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this RecordForListDomainRecordsOutput.


        :param ttl: The ttl of this RecordForListDomainRecordsOutput.  # noqa: E501
        :type: int
        """

        self._ttl = ttl

    @property
    def weights(self):
        """Gets the weights of this RecordForListDomainRecordsOutput.  # noqa: E501


        :return: The weights of this RecordForListDomainRecordsOutput.  # noqa: E501
        :rtype: list[WeightForListDomainRecordsOutput]
        """
        return self._weights

    @weights.setter
    def weights(self, weights):
        """Sets the weights of this RecordForListDomainRecordsOutput.


        :param weights: The weights of this RecordForListDomainRecordsOutput.  # noqa: E501
        :type: list[WeightForListDomainRecordsOutput]
        """

        self._weights = weights

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
        if issubclass(RecordForListDomainRecordsOutput, dict):
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
        if not isinstance(other, RecordForListDomainRecordsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RecordForListDomainRecordsOutput):
            return True

        return self.to_dict() != other.to_dict()
