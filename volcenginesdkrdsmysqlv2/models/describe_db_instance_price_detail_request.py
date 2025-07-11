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


class DescribeDBInstancePriceDetailRequest(object):
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
        'charge_type': 'str',
        'node_info': 'list[NodeInfoForDescribeDBInstancePriceDetailInput]',
        'number': 'int',
        'period': 'int',
        'period_unit': 'str',
        'project_name': 'str',
        'proxy_node_custom': 'ProxyNodeCustomForDescribeDBInstancePriceDetailInput',
        'storage_space': 'int',
        'storage_type': 'str'
    }

    attribute_map = {
        'charge_type': 'ChargeType',
        'node_info': 'NodeInfo',
        'number': 'Number',
        'period': 'Period',
        'period_unit': 'PeriodUnit',
        'project_name': 'ProjectName',
        'proxy_node_custom': 'ProxyNodeCustom',
        'storage_space': 'StorageSpace',
        'storage_type': 'StorageType'
    }

    def __init__(self, charge_type=None, node_info=None, number=None, period=None, period_unit=None, project_name=None, proxy_node_custom=None, storage_space=None, storage_type=None, _configuration=None):  # noqa: E501
        """DescribeDBInstancePriceDetailRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._charge_type = None
        self._node_info = None
        self._number = None
        self._period = None
        self._period_unit = None
        self._project_name = None
        self._proxy_node_custom = None
        self._storage_space = None
        self._storage_type = None
        self.discriminator = None

        self.charge_type = charge_type
        if node_info is not None:
            self.node_info = node_info
        if number is not None:
            self.number = number
        if period is not None:
            self.period = period
        if period_unit is not None:
            self.period_unit = period_unit
        if project_name is not None:
            self.project_name = project_name
        if proxy_node_custom is not None:
            self.proxy_node_custom = proxy_node_custom
        self.storage_space = storage_space
        self.storage_type = storage_type

    @property
    def charge_type(self):
        """Gets the charge_type of this DescribeDBInstancePriceDetailRequest.  # noqa: E501


        :return: The charge_type of this DescribeDBInstancePriceDetailRequest.  # noqa: E501
        :rtype: str
        """
        return self._charge_type

    @charge_type.setter
    def charge_type(self, charge_type):
        """Sets the charge_type of this DescribeDBInstancePriceDetailRequest.


        :param charge_type: The charge_type of this DescribeDBInstancePriceDetailRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and charge_type is None:
            raise ValueError("Invalid value for `charge_type`, must not be `None`")  # noqa: E501

        self._charge_type = charge_type

    @property
    def node_info(self):
        """Gets the node_info of this DescribeDBInstancePriceDetailRequest.  # noqa: E501


        :return: The node_info of this DescribeDBInstancePriceDetailRequest.  # noqa: E501
        :rtype: list[NodeInfoForDescribeDBInstancePriceDetailInput]
        """
        return self._node_info

    @node_info.setter
    def node_info(self, node_info):
        """Sets the node_info of this DescribeDBInstancePriceDetailRequest.


        :param node_info: The node_info of this DescribeDBInstancePriceDetailRequest.  # noqa: E501
        :type: list[NodeInfoForDescribeDBInstancePriceDetailInput]
        """

        self._node_info = node_info

    @property
    def number(self):
        """Gets the number of this DescribeDBInstancePriceDetailRequest.  # noqa: E501


        :return: The number of this DescribeDBInstancePriceDetailRequest.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this DescribeDBInstancePriceDetailRequest.


        :param number: The number of this DescribeDBInstancePriceDetailRequest.  # noqa: E501
        :type: int
        """

        self._number = number

    @property
    def period(self):
        """Gets the period of this DescribeDBInstancePriceDetailRequest.  # noqa: E501


        :return: The period of this DescribeDBInstancePriceDetailRequest.  # noqa: E501
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this DescribeDBInstancePriceDetailRequest.


        :param period: The period of this DescribeDBInstancePriceDetailRequest.  # noqa: E501
        :type: int
        """

        self._period = period

    @property
    def period_unit(self):
        """Gets the period_unit of this DescribeDBInstancePriceDetailRequest.  # noqa: E501


        :return: The period_unit of this DescribeDBInstancePriceDetailRequest.  # noqa: E501
        :rtype: str
        """
        return self._period_unit

    @period_unit.setter
    def period_unit(self, period_unit):
        """Sets the period_unit of this DescribeDBInstancePriceDetailRequest.


        :param period_unit: The period_unit of this DescribeDBInstancePriceDetailRequest.  # noqa: E501
        :type: str
        """

        self._period_unit = period_unit

    @property
    def project_name(self):
        """Gets the project_name of this DescribeDBInstancePriceDetailRequest.  # noqa: E501


        :return: The project_name of this DescribeDBInstancePriceDetailRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this DescribeDBInstancePriceDetailRequest.


        :param project_name: The project_name of this DescribeDBInstancePriceDetailRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def proxy_node_custom(self):
        """Gets the proxy_node_custom of this DescribeDBInstancePriceDetailRequest.  # noqa: E501


        :return: The proxy_node_custom of this DescribeDBInstancePriceDetailRequest.  # noqa: E501
        :rtype: ProxyNodeCustomForDescribeDBInstancePriceDetailInput
        """
        return self._proxy_node_custom

    @proxy_node_custom.setter
    def proxy_node_custom(self, proxy_node_custom):
        """Sets the proxy_node_custom of this DescribeDBInstancePriceDetailRequest.


        :param proxy_node_custom: The proxy_node_custom of this DescribeDBInstancePriceDetailRequest.  # noqa: E501
        :type: ProxyNodeCustomForDescribeDBInstancePriceDetailInput
        """

        self._proxy_node_custom = proxy_node_custom

    @property
    def storage_space(self):
        """Gets the storage_space of this DescribeDBInstancePriceDetailRequest.  # noqa: E501


        :return: The storage_space of this DescribeDBInstancePriceDetailRequest.  # noqa: E501
        :rtype: int
        """
        return self._storage_space

    @storage_space.setter
    def storage_space(self, storage_space):
        """Sets the storage_space of this DescribeDBInstancePriceDetailRequest.


        :param storage_space: The storage_space of this DescribeDBInstancePriceDetailRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and storage_space is None:
            raise ValueError("Invalid value for `storage_space`, must not be `None`")  # noqa: E501

        self._storage_space = storage_space

    @property
    def storage_type(self):
        """Gets the storage_type of this DescribeDBInstancePriceDetailRequest.  # noqa: E501


        :return: The storage_type of this DescribeDBInstancePriceDetailRequest.  # noqa: E501
        :rtype: str
        """
        return self._storage_type

    @storage_type.setter
    def storage_type(self, storage_type):
        """Sets the storage_type of this DescribeDBInstancePriceDetailRequest.


        :param storage_type: The storage_type of this DescribeDBInstancePriceDetailRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and storage_type is None:
            raise ValueError("Invalid value for `storage_type`, must not be `None`")  # noqa: E501

        self._storage_type = storage_type

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
        if issubclass(DescribeDBInstancePriceDetailRequest, dict):
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
        if not isinstance(other, DescribeDBInstancePriceDetailRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeDBInstancePriceDetailRequest):
            return True

        return self.to_dict() != other.to_dict()
