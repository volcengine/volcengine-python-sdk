# coding: utf-8

"""
    transitrouter

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class TransitRouterBandwidthPackageForDescribeTransitRouterBandwidthPackagesBillingOutput(object):
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
        'billing_status': 'int',
        'billing_type': 'int',
        'expired_time': 'str',
        'reclaim_time': 'str',
        'remain_renew_times': 'int',
        'renew_type': 'str',
        'transit_router_bandwidth_package_id': 'str'
    }

    attribute_map = {
        'billing_status': 'BillingStatus',
        'billing_type': 'BillingType',
        'expired_time': 'ExpiredTime',
        'reclaim_time': 'ReclaimTime',
        'remain_renew_times': 'RemainRenewTimes',
        'renew_type': 'RenewType',
        'transit_router_bandwidth_package_id': 'TransitRouterBandwidthPackageId'
    }

    def __init__(self, billing_status=None, billing_type=None, expired_time=None, reclaim_time=None, remain_renew_times=None, renew_type=None, transit_router_bandwidth_package_id=None, _configuration=None):  # noqa: E501
        """TransitRouterBandwidthPackageForDescribeTransitRouterBandwidthPackagesBillingOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._billing_status = None
        self._billing_type = None
        self._expired_time = None
        self._reclaim_time = None
        self._remain_renew_times = None
        self._renew_type = None
        self._transit_router_bandwidth_package_id = None
        self.discriminator = None

        if billing_status is not None:
            self.billing_status = billing_status
        if billing_type is not None:
            self.billing_type = billing_type
        if expired_time is not None:
            self.expired_time = expired_time
        if reclaim_time is not None:
            self.reclaim_time = reclaim_time
        if remain_renew_times is not None:
            self.remain_renew_times = remain_renew_times
        if renew_type is not None:
            self.renew_type = renew_type
        if transit_router_bandwidth_package_id is not None:
            self.transit_router_bandwidth_package_id = transit_router_bandwidth_package_id

    @property
    def billing_status(self):
        """Gets the billing_status of this TransitRouterBandwidthPackageForDescribeTransitRouterBandwidthPackagesBillingOutput.  # noqa: E501


        :return: The billing_status of this TransitRouterBandwidthPackageForDescribeTransitRouterBandwidthPackagesBillingOutput.  # noqa: E501
        :rtype: int
        """
        return self._billing_status

    @billing_status.setter
    def billing_status(self, billing_status):
        """Sets the billing_status of this TransitRouterBandwidthPackageForDescribeTransitRouterBandwidthPackagesBillingOutput.


        :param billing_status: The billing_status of this TransitRouterBandwidthPackageForDescribeTransitRouterBandwidthPackagesBillingOutput.  # noqa: E501
        :type: int
        """

        self._billing_status = billing_status

    @property
    def billing_type(self):
        """Gets the billing_type of this TransitRouterBandwidthPackageForDescribeTransitRouterBandwidthPackagesBillingOutput.  # noqa: E501


        :return: The billing_type of this TransitRouterBandwidthPackageForDescribeTransitRouterBandwidthPackagesBillingOutput.  # noqa: E501
        :rtype: int
        """
        return self._billing_type

    @billing_type.setter
    def billing_type(self, billing_type):
        """Sets the billing_type of this TransitRouterBandwidthPackageForDescribeTransitRouterBandwidthPackagesBillingOutput.


        :param billing_type: The billing_type of this TransitRouterBandwidthPackageForDescribeTransitRouterBandwidthPackagesBillingOutput.  # noqa: E501
        :type: int
        """

        self._billing_type = billing_type

    @property
    def expired_time(self):
        """Gets the expired_time of this TransitRouterBandwidthPackageForDescribeTransitRouterBandwidthPackagesBillingOutput.  # noqa: E501


        :return: The expired_time of this TransitRouterBandwidthPackageForDescribeTransitRouterBandwidthPackagesBillingOutput.  # noqa: E501
        :rtype: str
        """
        return self._expired_time

    @expired_time.setter
    def expired_time(self, expired_time):
        """Sets the expired_time of this TransitRouterBandwidthPackageForDescribeTransitRouterBandwidthPackagesBillingOutput.


        :param expired_time: The expired_time of this TransitRouterBandwidthPackageForDescribeTransitRouterBandwidthPackagesBillingOutput.  # noqa: E501
        :type: str
        """

        self._expired_time = expired_time

    @property
    def reclaim_time(self):
        """Gets the reclaim_time of this TransitRouterBandwidthPackageForDescribeTransitRouterBandwidthPackagesBillingOutput.  # noqa: E501


        :return: The reclaim_time of this TransitRouterBandwidthPackageForDescribeTransitRouterBandwidthPackagesBillingOutput.  # noqa: E501
        :rtype: str
        """
        return self._reclaim_time

    @reclaim_time.setter
    def reclaim_time(self, reclaim_time):
        """Sets the reclaim_time of this TransitRouterBandwidthPackageForDescribeTransitRouterBandwidthPackagesBillingOutput.


        :param reclaim_time: The reclaim_time of this TransitRouterBandwidthPackageForDescribeTransitRouterBandwidthPackagesBillingOutput.  # noqa: E501
        :type: str
        """

        self._reclaim_time = reclaim_time

    @property
    def remain_renew_times(self):
        """Gets the remain_renew_times of this TransitRouterBandwidthPackageForDescribeTransitRouterBandwidthPackagesBillingOutput.  # noqa: E501


        :return: The remain_renew_times of this TransitRouterBandwidthPackageForDescribeTransitRouterBandwidthPackagesBillingOutput.  # noqa: E501
        :rtype: int
        """
        return self._remain_renew_times

    @remain_renew_times.setter
    def remain_renew_times(self, remain_renew_times):
        """Sets the remain_renew_times of this TransitRouterBandwidthPackageForDescribeTransitRouterBandwidthPackagesBillingOutput.


        :param remain_renew_times: The remain_renew_times of this TransitRouterBandwidthPackageForDescribeTransitRouterBandwidthPackagesBillingOutput.  # noqa: E501
        :type: int
        """

        self._remain_renew_times = remain_renew_times

    @property
    def renew_type(self):
        """Gets the renew_type of this TransitRouterBandwidthPackageForDescribeTransitRouterBandwidthPackagesBillingOutput.  # noqa: E501


        :return: The renew_type of this TransitRouterBandwidthPackageForDescribeTransitRouterBandwidthPackagesBillingOutput.  # noqa: E501
        :rtype: str
        """
        return self._renew_type

    @renew_type.setter
    def renew_type(self, renew_type):
        """Sets the renew_type of this TransitRouterBandwidthPackageForDescribeTransitRouterBandwidthPackagesBillingOutput.


        :param renew_type: The renew_type of this TransitRouterBandwidthPackageForDescribeTransitRouterBandwidthPackagesBillingOutput.  # noqa: E501
        :type: str
        """

        self._renew_type = renew_type

    @property
    def transit_router_bandwidth_package_id(self):
        """Gets the transit_router_bandwidth_package_id of this TransitRouterBandwidthPackageForDescribeTransitRouterBandwidthPackagesBillingOutput.  # noqa: E501


        :return: The transit_router_bandwidth_package_id of this TransitRouterBandwidthPackageForDescribeTransitRouterBandwidthPackagesBillingOutput.  # noqa: E501
        :rtype: str
        """
        return self._transit_router_bandwidth_package_id

    @transit_router_bandwidth_package_id.setter
    def transit_router_bandwidth_package_id(self, transit_router_bandwidth_package_id):
        """Sets the transit_router_bandwidth_package_id of this TransitRouterBandwidthPackageForDescribeTransitRouterBandwidthPackagesBillingOutput.


        :param transit_router_bandwidth_package_id: The transit_router_bandwidth_package_id of this TransitRouterBandwidthPackageForDescribeTransitRouterBandwidthPackagesBillingOutput.  # noqa: E501
        :type: str
        """

        self._transit_router_bandwidth_package_id = transit_router_bandwidth_package_id

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
        if issubclass(TransitRouterBandwidthPackageForDescribeTransitRouterBandwidthPackagesBillingOutput, dict):
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
        if not isinstance(other, TransitRouterBandwidthPackageForDescribeTransitRouterBandwidthPackagesBillingOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransitRouterBandwidthPackageForDescribeTransitRouterBandwidthPackagesBillingOutput):
            return True

        return self.to_dict() != other.to_dict()
