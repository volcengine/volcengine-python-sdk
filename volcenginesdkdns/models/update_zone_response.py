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


class UpdateZoneResponse(object):
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
        'cache_stage': 'int',
        'configuration_code': 'str',
        'created_at': 'str',
        'dns_security': 'str',
        'expired_time': 'int',
        'instance_id': 'str',
        'is_sub_domain': 'bool',
        'last_operator': 'str',
        'record_count': 'int',
        'remark': 'str',
        'trade_code': 'str',
        'updated_at': 'str',
        'zid': 'int',
        'zone_name': 'str'
    }

    attribute_map = {
        'cache_stage': 'CacheStage',
        'configuration_code': 'ConfigurationCode',
        'created_at': 'CreatedAt',
        'dns_security': 'DnsSecurity',
        'expired_time': 'ExpiredTime',
        'instance_id': 'InstanceID',
        'is_sub_domain': 'IsSubDomain',
        'last_operator': 'LastOperator',
        'record_count': 'RecordCount',
        'remark': 'Remark',
        'trade_code': 'TradeCode',
        'updated_at': 'UpdatedAt',
        'zid': 'ZID',
        'zone_name': 'ZoneName'
    }

    def __init__(self, cache_stage=None, configuration_code=None, created_at=None, dns_security=None, expired_time=None, instance_id=None, is_sub_domain=None, last_operator=None, record_count=None, remark=None, trade_code=None, updated_at=None, zid=None, zone_name=None, _configuration=None):  # noqa: E501
        """UpdateZoneResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cache_stage = None
        self._configuration_code = None
        self._created_at = None
        self._dns_security = None
        self._expired_time = None
        self._instance_id = None
        self._is_sub_domain = None
        self._last_operator = None
        self._record_count = None
        self._remark = None
        self._trade_code = None
        self._updated_at = None
        self._zid = None
        self._zone_name = None
        self.discriminator = None

        if cache_stage is not None:
            self.cache_stage = cache_stage
        if configuration_code is not None:
            self.configuration_code = configuration_code
        if created_at is not None:
            self.created_at = created_at
        if dns_security is not None:
            self.dns_security = dns_security
        if expired_time is not None:
            self.expired_time = expired_time
        if instance_id is not None:
            self.instance_id = instance_id
        if is_sub_domain is not None:
            self.is_sub_domain = is_sub_domain
        if last_operator is not None:
            self.last_operator = last_operator
        if record_count is not None:
            self.record_count = record_count
        if remark is not None:
            self.remark = remark
        if trade_code is not None:
            self.trade_code = trade_code
        if updated_at is not None:
            self.updated_at = updated_at
        if zid is not None:
            self.zid = zid
        if zone_name is not None:
            self.zone_name = zone_name

    @property
    def cache_stage(self):
        """Gets the cache_stage of this UpdateZoneResponse.  # noqa: E501


        :return: The cache_stage of this UpdateZoneResponse.  # noqa: E501
        :rtype: int
        """
        return self._cache_stage

    @cache_stage.setter
    def cache_stage(self, cache_stage):
        """Sets the cache_stage of this UpdateZoneResponse.


        :param cache_stage: The cache_stage of this UpdateZoneResponse.  # noqa: E501
        :type: int
        """

        self._cache_stage = cache_stage

    @property
    def configuration_code(self):
        """Gets the configuration_code of this UpdateZoneResponse.  # noqa: E501


        :return: The configuration_code of this UpdateZoneResponse.  # noqa: E501
        :rtype: str
        """
        return self._configuration_code

    @configuration_code.setter
    def configuration_code(self, configuration_code):
        """Sets the configuration_code of this UpdateZoneResponse.


        :param configuration_code: The configuration_code of this UpdateZoneResponse.  # noqa: E501
        :type: str
        """

        self._configuration_code = configuration_code

    @property
    def created_at(self):
        """Gets the created_at of this UpdateZoneResponse.  # noqa: E501


        :return: The created_at of this UpdateZoneResponse.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this UpdateZoneResponse.


        :param created_at: The created_at of this UpdateZoneResponse.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def dns_security(self):
        """Gets the dns_security of this UpdateZoneResponse.  # noqa: E501


        :return: The dns_security of this UpdateZoneResponse.  # noqa: E501
        :rtype: str
        """
        return self._dns_security

    @dns_security.setter
    def dns_security(self, dns_security):
        """Sets the dns_security of this UpdateZoneResponse.


        :param dns_security: The dns_security of this UpdateZoneResponse.  # noqa: E501
        :type: str
        """

        self._dns_security = dns_security

    @property
    def expired_time(self):
        """Gets the expired_time of this UpdateZoneResponse.  # noqa: E501


        :return: The expired_time of this UpdateZoneResponse.  # noqa: E501
        :rtype: int
        """
        return self._expired_time

    @expired_time.setter
    def expired_time(self, expired_time):
        """Sets the expired_time of this UpdateZoneResponse.


        :param expired_time: The expired_time of this UpdateZoneResponse.  # noqa: E501
        :type: int
        """

        self._expired_time = expired_time

    @property
    def instance_id(self):
        """Gets the instance_id of this UpdateZoneResponse.  # noqa: E501


        :return: The instance_id of this UpdateZoneResponse.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this UpdateZoneResponse.


        :param instance_id: The instance_id of this UpdateZoneResponse.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def is_sub_domain(self):
        """Gets the is_sub_domain of this UpdateZoneResponse.  # noqa: E501


        :return: The is_sub_domain of this UpdateZoneResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_sub_domain

    @is_sub_domain.setter
    def is_sub_domain(self, is_sub_domain):
        """Sets the is_sub_domain of this UpdateZoneResponse.


        :param is_sub_domain: The is_sub_domain of this UpdateZoneResponse.  # noqa: E501
        :type: bool
        """

        self._is_sub_domain = is_sub_domain

    @property
    def last_operator(self):
        """Gets the last_operator of this UpdateZoneResponse.  # noqa: E501


        :return: The last_operator of this UpdateZoneResponse.  # noqa: E501
        :rtype: str
        """
        return self._last_operator

    @last_operator.setter
    def last_operator(self, last_operator):
        """Sets the last_operator of this UpdateZoneResponse.


        :param last_operator: The last_operator of this UpdateZoneResponse.  # noqa: E501
        :type: str
        """

        self._last_operator = last_operator

    @property
    def record_count(self):
        """Gets the record_count of this UpdateZoneResponse.  # noqa: E501


        :return: The record_count of this UpdateZoneResponse.  # noqa: E501
        :rtype: int
        """
        return self._record_count

    @record_count.setter
    def record_count(self, record_count):
        """Sets the record_count of this UpdateZoneResponse.


        :param record_count: The record_count of this UpdateZoneResponse.  # noqa: E501
        :type: int
        """

        self._record_count = record_count

    @property
    def remark(self):
        """Gets the remark of this UpdateZoneResponse.  # noqa: E501


        :return: The remark of this UpdateZoneResponse.  # noqa: E501
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this UpdateZoneResponse.


        :param remark: The remark of this UpdateZoneResponse.  # noqa: E501
        :type: str
        """

        self._remark = remark

    @property
    def trade_code(self):
        """Gets the trade_code of this UpdateZoneResponse.  # noqa: E501


        :return: The trade_code of this UpdateZoneResponse.  # noqa: E501
        :rtype: str
        """
        return self._trade_code

    @trade_code.setter
    def trade_code(self, trade_code):
        """Sets the trade_code of this UpdateZoneResponse.


        :param trade_code: The trade_code of this UpdateZoneResponse.  # noqa: E501
        :type: str
        """

        self._trade_code = trade_code

    @property
    def updated_at(self):
        """Gets the updated_at of this UpdateZoneResponse.  # noqa: E501


        :return: The updated_at of this UpdateZoneResponse.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this UpdateZoneResponse.


        :param updated_at: The updated_at of this UpdateZoneResponse.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

    @property
    def zid(self):
        """Gets the zid of this UpdateZoneResponse.  # noqa: E501


        :return: The zid of this UpdateZoneResponse.  # noqa: E501
        :rtype: int
        """
        return self._zid

    @zid.setter
    def zid(self, zid):
        """Sets the zid of this UpdateZoneResponse.


        :param zid: The zid of this UpdateZoneResponse.  # noqa: E501
        :type: int
        """

        self._zid = zid

    @property
    def zone_name(self):
        """Gets the zone_name of this UpdateZoneResponse.  # noqa: E501


        :return: The zone_name of this UpdateZoneResponse.  # noqa: E501
        :rtype: str
        """
        return self._zone_name

    @zone_name.setter
    def zone_name(self, zone_name):
        """Sets the zone_name of this UpdateZoneResponse.


        :param zone_name: The zone_name of this UpdateZoneResponse.  # noqa: E501
        :type: str
        """

        self._zone_name = zone_name

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
        if issubclass(UpdateZoneResponse, dict):
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
        if not isinstance(other, UpdateZoneResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateZoneResponse):
            return True

        return self.to_dict() != other.to_dict()
