# coding: utf-8

"""
    storage_ebs

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class PurchaseReservedStorageCapacityRequest(object):
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
        'client_token': 'str',
        'effective_at': 'str',
        'period': 'int',
        'period_unit': 'str',
        'rsc_auto_renew': 'bool',
        'reserved_capacity': 'int',
        'reserved_storage_capacity_name': 'str',
        'volume_type': 'str',
        'zone_id': 'str'
    }

    attribute_map = {
        'client_token': 'ClientToken',
        'effective_at': 'EffectiveAt',
        'period': 'Period',
        'period_unit': 'PeriodUnit',
        'rsc_auto_renew': 'RSCAutoRenew',
        'reserved_capacity': 'ReservedCapacity',
        'reserved_storage_capacity_name': 'ReservedStorageCapacityName',
        'volume_type': 'VolumeType',
        'zone_id': 'ZoneId'
    }

    def __init__(self, client_token=None, effective_at=None, period=None, period_unit=None, rsc_auto_renew=None, reserved_capacity=None, reserved_storage_capacity_name=None, volume_type=None, zone_id=None, _configuration=None):  # noqa: E501
        """PurchaseReservedStorageCapacityRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._client_token = None
        self._effective_at = None
        self._period = None
        self._period_unit = None
        self._rsc_auto_renew = None
        self._reserved_capacity = None
        self._reserved_storage_capacity_name = None
        self._volume_type = None
        self._zone_id = None
        self.discriminator = None

        if client_token is not None:
            self.client_token = client_token
        if effective_at is not None:
            self.effective_at = effective_at
        if period is not None:
            self.period = period
        if period_unit is not None:
            self.period_unit = period_unit
        if rsc_auto_renew is not None:
            self.rsc_auto_renew = rsc_auto_renew
        if reserved_capacity is not None:
            self.reserved_capacity = reserved_capacity
        if reserved_storage_capacity_name is not None:
            self.reserved_storage_capacity_name = reserved_storage_capacity_name
        if volume_type is not None:
            self.volume_type = volume_type
        if zone_id is not None:
            self.zone_id = zone_id

    @property
    def client_token(self):
        """Gets the client_token of this PurchaseReservedStorageCapacityRequest.  # noqa: E501


        :return: The client_token of this PurchaseReservedStorageCapacityRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_token

    @client_token.setter
    def client_token(self, client_token):
        """Sets the client_token of this PurchaseReservedStorageCapacityRequest.


        :param client_token: The client_token of this PurchaseReservedStorageCapacityRequest.  # noqa: E501
        :type: str
        """

        self._client_token = client_token

    @property
    def effective_at(self):
        """Gets the effective_at of this PurchaseReservedStorageCapacityRequest.  # noqa: E501


        :return: The effective_at of this PurchaseReservedStorageCapacityRequest.  # noqa: E501
        :rtype: str
        """
        return self._effective_at

    @effective_at.setter
    def effective_at(self, effective_at):
        """Sets the effective_at of this PurchaseReservedStorageCapacityRequest.


        :param effective_at: The effective_at of this PurchaseReservedStorageCapacityRequest.  # noqa: E501
        :type: str
        """

        self._effective_at = effective_at

    @property
    def period(self):
        """Gets the period of this PurchaseReservedStorageCapacityRequest.  # noqa: E501


        :return: The period of this PurchaseReservedStorageCapacityRequest.  # noqa: E501
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this PurchaseReservedStorageCapacityRequest.


        :param period: The period of this PurchaseReservedStorageCapacityRequest.  # noqa: E501
        :type: int
        """

        self._period = period

    @property
    def period_unit(self):
        """Gets the period_unit of this PurchaseReservedStorageCapacityRequest.  # noqa: E501


        :return: The period_unit of this PurchaseReservedStorageCapacityRequest.  # noqa: E501
        :rtype: str
        """
        return self._period_unit

    @period_unit.setter
    def period_unit(self, period_unit):
        """Sets the period_unit of this PurchaseReservedStorageCapacityRequest.


        :param period_unit: The period_unit of this PurchaseReservedStorageCapacityRequest.  # noqa: E501
        :type: str
        """

        self._period_unit = period_unit

    @property
    def rsc_auto_renew(self):
        """Gets the rsc_auto_renew of this PurchaseReservedStorageCapacityRequest.  # noqa: E501


        :return: The rsc_auto_renew of this PurchaseReservedStorageCapacityRequest.  # noqa: E501
        :rtype: bool
        """
        return self._rsc_auto_renew

    @rsc_auto_renew.setter
    def rsc_auto_renew(self, rsc_auto_renew):
        """Sets the rsc_auto_renew of this PurchaseReservedStorageCapacityRequest.


        :param rsc_auto_renew: The rsc_auto_renew of this PurchaseReservedStorageCapacityRequest.  # noqa: E501
        :type: bool
        """

        self._rsc_auto_renew = rsc_auto_renew

    @property
    def reserved_capacity(self):
        """Gets the reserved_capacity of this PurchaseReservedStorageCapacityRequest.  # noqa: E501


        :return: The reserved_capacity of this PurchaseReservedStorageCapacityRequest.  # noqa: E501
        :rtype: int
        """
        return self._reserved_capacity

    @reserved_capacity.setter
    def reserved_capacity(self, reserved_capacity):
        """Sets the reserved_capacity of this PurchaseReservedStorageCapacityRequest.


        :param reserved_capacity: The reserved_capacity of this PurchaseReservedStorageCapacityRequest.  # noqa: E501
        :type: int
        """

        self._reserved_capacity = reserved_capacity

    @property
    def reserved_storage_capacity_name(self):
        """Gets the reserved_storage_capacity_name of this PurchaseReservedStorageCapacityRequest.  # noqa: E501


        :return: The reserved_storage_capacity_name of this PurchaseReservedStorageCapacityRequest.  # noqa: E501
        :rtype: str
        """
        return self._reserved_storage_capacity_name

    @reserved_storage_capacity_name.setter
    def reserved_storage_capacity_name(self, reserved_storage_capacity_name):
        """Sets the reserved_storage_capacity_name of this PurchaseReservedStorageCapacityRequest.


        :param reserved_storage_capacity_name: The reserved_storage_capacity_name of this PurchaseReservedStorageCapacityRequest.  # noqa: E501
        :type: str
        """

        self._reserved_storage_capacity_name = reserved_storage_capacity_name

    @property
    def volume_type(self):
        """Gets the volume_type of this PurchaseReservedStorageCapacityRequest.  # noqa: E501


        :return: The volume_type of this PurchaseReservedStorageCapacityRequest.  # noqa: E501
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        """Sets the volume_type of this PurchaseReservedStorageCapacityRequest.


        :param volume_type: The volume_type of this PurchaseReservedStorageCapacityRequest.  # noqa: E501
        :type: str
        """

        self._volume_type = volume_type

    @property
    def zone_id(self):
        """Gets the zone_id of this PurchaseReservedStorageCapacityRequest.  # noqa: E501


        :return: The zone_id of this PurchaseReservedStorageCapacityRequest.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this PurchaseReservedStorageCapacityRequest.


        :param zone_id: The zone_id of this PurchaseReservedStorageCapacityRequest.  # noqa: E501
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
        if issubclass(PurchaseReservedStorageCapacityRequest, dict):
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
        if not isinstance(other, PurchaseReservedStorageCapacityRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PurchaseReservedStorageCapacityRequest):
            return True

        return self.to_dict() != other.to_dict()
