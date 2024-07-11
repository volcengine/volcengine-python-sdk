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


class DescribeTransitRoutersResponse(object):
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
        'page_number': 'int',
        'page_size': 'int',
        'total_count': 'int',
        'transit_routers': 'list[TransitRouterForDescribeTransitRoutersOutput]'
    }

    attribute_map = {
        'page_number': 'PageNumber',
        'page_size': 'PageSize',
        'total_count': 'TotalCount',
        'transit_routers': 'TransitRouters'
    }

    def __init__(self, page_number=None, page_size=None, total_count=None, transit_routers=None, _configuration=None):  # noqa: E501
        """DescribeTransitRoutersResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._page_number = None
        self._page_size = None
        self._total_count = None
        self._transit_routers = None
        self.discriminator = None

        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if total_count is not None:
            self.total_count = total_count
        if transit_routers is not None:
            self.transit_routers = transit_routers

    @property
    def page_number(self):
        """Gets the page_number of this DescribeTransitRoutersResponse.  # noqa: E501


        :return: The page_number of this DescribeTransitRoutersResponse.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this DescribeTransitRoutersResponse.


        :param page_number: The page_number of this DescribeTransitRoutersResponse.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this DescribeTransitRoutersResponse.  # noqa: E501


        :return: The page_size of this DescribeTransitRoutersResponse.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this DescribeTransitRoutersResponse.


        :param page_size: The page_size of this DescribeTransitRoutersResponse.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def total_count(self):
        """Gets the total_count of this DescribeTransitRoutersResponse.  # noqa: E501


        :return: The total_count of this DescribeTransitRoutersResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this DescribeTransitRoutersResponse.


        :param total_count: The total_count of this DescribeTransitRoutersResponse.  # noqa: E501
        :type: int
        """

        self._total_count = total_count

    @property
    def transit_routers(self):
        """Gets the transit_routers of this DescribeTransitRoutersResponse.  # noqa: E501


        :return: The transit_routers of this DescribeTransitRoutersResponse.  # noqa: E501
        :rtype: list[TransitRouterForDescribeTransitRoutersOutput]
        """
        return self._transit_routers

    @transit_routers.setter
    def transit_routers(self, transit_routers):
        """Sets the transit_routers of this DescribeTransitRoutersResponse.


        :param transit_routers: The transit_routers of this DescribeTransitRoutersResponse.  # noqa: E501
        :type: list[TransitRouterForDescribeTransitRoutersOutput]
        """

        self._transit_routers = transit_routers

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
        if issubclass(DescribeTransitRoutersResponse, dict):
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
        if not isinstance(other, DescribeTransitRoutersResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeTransitRoutersResponse):
            return True

        return self.to_dict() != other.to_dict()
