# coding: utf-8

"""
    ml_platform20240701

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ListInstanceTypesRequest(object):
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
        'name_contains': 'str',
        'reservation_plan_support_status': 'str',
        'support_status': 'str',
        'zone_id': 'str'
    }

    attribute_map = {
        'name_contains': 'NameContains',
        'reservation_plan_support_status': 'ReservationPlanSupportStatus',
        'support_status': 'SupportStatus',
        'zone_id': 'ZoneId'
    }

    def __init__(self, name_contains=None, reservation_plan_support_status=None, support_status=None, zone_id=None, _configuration=None):  # noqa: E501
        """ListInstanceTypesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name_contains = None
        self._reservation_plan_support_status = None
        self._support_status = None
        self._zone_id = None
        self.discriminator = None

        if name_contains is not None:
            self.name_contains = name_contains
        if reservation_plan_support_status is not None:
            self.reservation_plan_support_status = reservation_plan_support_status
        if support_status is not None:
            self.support_status = support_status
        if zone_id is not None:
            self.zone_id = zone_id

    @property
    def name_contains(self):
        """Gets the name_contains of this ListInstanceTypesRequest.  # noqa: E501


        :return: The name_contains of this ListInstanceTypesRequest.  # noqa: E501
        :rtype: str
        """
        return self._name_contains

    @name_contains.setter
    def name_contains(self, name_contains):
        """Sets the name_contains of this ListInstanceTypesRequest.


        :param name_contains: The name_contains of this ListInstanceTypesRequest.  # noqa: E501
        :type: str
        """

        self._name_contains = name_contains

    @property
    def reservation_plan_support_status(self):
        """Gets the reservation_plan_support_status of this ListInstanceTypesRequest.  # noqa: E501


        :return: The reservation_plan_support_status of this ListInstanceTypesRequest.  # noqa: E501
        :rtype: str
        """
        return self._reservation_plan_support_status

    @reservation_plan_support_status.setter
    def reservation_plan_support_status(self, reservation_plan_support_status):
        """Sets the reservation_plan_support_status of this ListInstanceTypesRequest.


        :param reservation_plan_support_status: The reservation_plan_support_status of this ListInstanceTypesRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["Valid"]  # noqa: E501
        if (self._configuration.client_side_validation and
                reservation_plan_support_status not in allowed_values):
            raise ValueError(
                "Invalid value for `reservation_plan_support_status` ({0}), must be one of {1}"  # noqa: E501
                .format(reservation_plan_support_status, allowed_values)
            )

        self._reservation_plan_support_status = reservation_plan_support_status

    @property
    def support_status(self):
        """Gets the support_status of this ListInstanceTypesRequest.  # noqa: E501


        :return: The support_status of this ListInstanceTypesRequest.  # noqa: E501
        :rtype: str
        """
        return self._support_status

    @support_status.setter
    def support_status(self, support_status):
        """Sets the support_status of this ListInstanceTypesRequest.


        :param support_status: The support_status of this ListInstanceTypesRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["Deprecated", "Valid"]  # noqa: E501
        if (self._configuration.client_side_validation and
                support_status not in allowed_values):
            raise ValueError(
                "Invalid value for `support_status` ({0}), must be one of {1}"  # noqa: E501
                .format(support_status, allowed_values)
            )

        self._support_status = support_status

    @property
    def zone_id(self):
        """Gets the zone_id of this ListInstanceTypesRequest.  # noqa: E501


        :return: The zone_id of this ListInstanceTypesRequest.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this ListInstanceTypesRequest.


        :param zone_id: The zone_id of this ListInstanceTypesRequest.  # noqa: E501
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
        if issubclass(ListInstanceTypesRequest, dict):
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
        if not isinstance(other, ListInstanceTypesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListInstanceTypesRequest):
            return True

        return self.to_dict() != other.to_dict()
