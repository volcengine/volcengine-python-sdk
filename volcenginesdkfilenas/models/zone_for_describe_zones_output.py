# coding: utf-8

"""
    filenas

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ZoneForDescribeZonesOutput(object):
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
        'sales': 'list[SaleForDescribeZonesOutput]',
        'status': 'str',
        'zone_id': 'str',
        'zone_name': 'str'
    }

    attribute_map = {
        'sales': 'Sales',
        'status': 'Status',
        'zone_id': 'ZoneId',
        'zone_name': 'ZoneName'
    }

    def __init__(self, sales=None, status=None, zone_id=None, zone_name=None, _configuration=None):  # noqa: E501
        """ZoneForDescribeZonesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._sales = None
        self._status = None
        self._zone_id = None
        self._zone_name = None
        self.discriminator = None

        if sales is not None:
            self.sales = sales
        if status is not None:
            self.status = status
        if zone_id is not None:
            self.zone_id = zone_id
        if zone_name is not None:
            self.zone_name = zone_name

    @property
    def sales(self):
        """Gets the sales of this ZoneForDescribeZonesOutput.  # noqa: E501


        :return: The sales of this ZoneForDescribeZonesOutput.  # noqa: E501
        :rtype: list[SaleForDescribeZonesOutput]
        """
        return self._sales

    @sales.setter
    def sales(self, sales):
        """Sets the sales of this ZoneForDescribeZonesOutput.


        :param sales: The sales of this ZoneForDescribeZonesOutput.  # noqa: E501
        :type: list[SaleForDescribeZonesOutput]
        """

        self._sales = sales

    @property
    def status(self):
        """Gets the status of this ZoneForDescribeZonesOutput.  # noqa: E501


        :return: The status of this ZoneForDescribeZonesOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ZoneForDescribeZonesOutput.


        :param status: The status of this ZoneForDescribeZonesOutput.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def zone_id(self):
        """Gets the zone_id of this ZoneForDescribeZonesOutput.  # noqa: E501


        :return: The zone_id of this ZoneForDescribeZonesOutput.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this ZoneForDescribeZonesOutput.


        :param zone_id: The zone_id of this ZoneForDescribeZonesOutput.  # noqa: E501
        :type: str
        """

        self._zone_id = zone_id

    @property
    def zone_name(self):
        """Gets the zone_name of this ZoneForDescribeZonesOutput.  # noqa: E501


        :return: The zone_name of this ZoneForDescribeZonesOutput.  # noqa: E501
        :rtype: str
        """
        return self._zone_name

    @zone_name.setter
    def zone_name(self, zone_name):
        """Sets the zone_name of this ZoneForDescribeZonesOutput.


        :param zone_name: The zone_name of this ZoneForDescribeZonesOutput.  # noqa: E501
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
        if issubclass(ZoneForDescribeZonesOutput, dict):
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
        if not isinstance(other, ZoneForDescribeZonesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ZoneForDescribeZonesOutput):
            return True

        return self.to_dict() != other.to_dict()
