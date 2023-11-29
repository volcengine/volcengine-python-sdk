# coding: utf-8

"""
    vpc

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeRouteEntryListRequest(object):
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
        'destination_cidr_block': 'str',
        'destination_prefix_list_id': 'str',
        'max_results': 'int',
        'next_hop_id': 'str',
        'next_hop_type': 'str',
        'next_token': 'str',
        'page_number': 'int',
        'page_size': 'int',
        'route_entry_id': 'str',
        'route_entry_name': 'str',
        'route_entry_type': 'str',
        'route_table_id': 'str'
    }

    attribute_map = {
        'destination_cidr_block': 'DestinationCidrBlock',
        'destination_prefix_list_id': 'DestinationPrefixListId',
        'max_results': 'MaxResults',
        'next_hop_id': 'NextHopId',
        'next_hop_type': 'NextHopType',
        'next_token': 'NextToken',
        'page_number': 'PageNumber',
        'page_size': 'PageSize',
        'route_entry_id': 'RouteEntryId',
        'route_entry_name': 'RouteEntryName',
        'route_entry_type': 'RouteEntryType',
        'route_table_id': 'RouteTableId'
    }

    def __init__(self, destination_cidr_block=None, destination_prefix_list_id=None, max_results=None, next_hop_id=None, next_hop_type=None, next_token=None, page_number=None, page_size=None, route_entry_id=None, route_entry_name=None, route_entry_type=None, route_table_id=None, _configuration=None):  # noqa: E501
        """DescribeRouteEntryListRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._destination_cidr_block = None
        self._destination_prefix_list_id = None
        self._max_results = None
        self._next_hop_id = None
        self._next_hop_type = None
        self._next_token = None
        self._page_number = None
        self._page_size = None
        self._route_entry_id = None
        self._route_entry_name = None
        self._route_entry_type = None
        self._route_table_id = None
        self.discriminator = None

        if destination_cidr_block is not None:
            self.destination_cidr_block = destination_cidr_block
        if destination_prefix_list_id is not None:
            self.destination_prefix_list_id = destination_prefix_list_id
        if max_results is not None:
            self.max_results = max_results
        if next_hop_id is not None:
            self.next_hop_id = next_hop_id
        if next_hop_type is not None:
            self.next_hop_type = next_hop_type
        if next_token is not None:
            self.next_token = next_token
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if route_entry_id is not None:
            self.route_entry_id = route_entry_id
        if route_entry_name is not None:
            self.route_entry_name = route_entry_name
        if route_entry_type is not None:
            self.route_entry_type = route_entry_type
        self.route_table_id = route_table_id

    @property
    def destination_cidr_block(self):
        """Gets the destination_cidr_block of this DescribeRouteEntryListRequest.  # noqa: E501


        :return: The destination_cidr_block of this DescribeRouteEntryListRequest.  # noqa: E501
        :rtype: str
        """
        return self._destination_cidr_block

    @destination_cidr_block.setter
    def destination_cidr_block(self, destination_cidr_block):
        """Sets the destination_cidr_block of this DescribeRouteEntryListRequest.


        :param destination_cidr_block: The destination_cidr_block of this DescribeRouteEntryListRequest.  # noqa: E501
        :type: str
        """

        self._destination_cidr_block = destination_cidr_block

    @property
    def destination_prefix_list_id(self):
        """Gets the destination_prefix_list_id of this DescribeRouteEntryListRequest.  # noqa: E501


        :return: The destination_prefix_list_id of this DescribeRouteEntryListRequest.  # noqa: E501
        :rtype: str
        """
        return self._destination_prefix_list_id

    @destination_prefix_list_id.setter
    def destination_prefix_list_id(self, destination_prefix_list_id):
        """Sets the destination_prefix_list_id of this DescribeRouteEntryListRequest.


        :param destination_prefix_list_id: The destination_prefix_list_id of this DescribeRouteEntryListRequest.  # noqa: E501
        :type: str
        """

        self._destination_prefix_list_id = destination_prefix_list_id

    @property
    def max_results(self):
        """Gets the max_results of this DescribeRouteEntryListRequest.  # noqa: E501


        :return: The max_results of this DescribeRouteEntryListRequest.  # noqa: E501
        :rtype: int
        """
        return self._max_results

    @max_results.setter
    def max_results(self, max_results):
        """Sets the max_results of this DescribeRouteEntryListRequest.


        :param max_results: The max_results of this DescribeRouteEntryListRequest.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                max_results is not None and max_results > 100):  # noqa: E501
            raise ValueError("Invalid value for `max_results`, must be a value less than or equal to `100`")  # noqa: E501
        if (self._configuration.client_side_validation and
                max_results is not None and max_results < 1):  # noqa: E501
            raise ValueError("Invalid value for `max_results`, must be a value greater than or equal to `1`")  # noqa: E501

        self._max_results = max_results

    @property
    def next_hop_id(self):
        """Gets the next_hop_id of this DescribeRouteEntryListRequest.  # noqa: E501


        :return: The next_hop_id of this DescribeRouteEntryListRequest.  # noqa: E501
        :rtype: str
        """
        return self._next_hop_id

    @next_hop_id.setter
    def next_hop_id(self, next_hop_id):
        """Sets the next_hop_id of this DescribeRouteEntryListRequest.


        :param next_hop_id: The next_hop_id of this DescribeRouteEntryListRequest.  # noqa: E501
        :type: str
        """

        self._next_hop_id = next_hop_id

    @property
    def next_hop_type(self):
        """Gets the next_hop_type of this DescribeRouteEntryListRequest.  # noqa: E501


        :return: The next_hop_type of this DescribeRouteEntryListRequest.  # noqa: E501
        :rtype: str
        """
        return self._next_hop_type

    @next_hop_type.setter
    def next_hop_type(self, next_hop_type):
        """Sets the next_hop_type of this DescribeRouteEntryListRequest.


        :param next_hop_type: The next_hop_type of this DescribeRouteEntryListRequest.  # noqa: E501
        :type: str
        """

        self._next_hop_type = next_hop_type

    @property
    def next_token(self):
        """Gets the next_token of this DescribeRouteEntryListRequest.  # noqa: E501


        :return: The next_token of this DescribeRouteEntryListRequest.  # noqa: E501
        :rtype: str
        """
        return self._next_token

    @next_token.setter
    def next_token(self, next_token):
        """Sets the next_token of this DescribeRouteEntryListRequest.


        :param next_token: The next_token of this DescribeRouteEntryListRequest.  # noqa: E501
        :type: str
        """

        self._next_token = next_token

    @property
    def page_number(self):
        """Gets the page_number of this DescribeRouteEntryListRequest.  # noqa: E501


        :return: The page_number of this DescribeRouteEntryListRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this DescribeRouteEntryListRequest.


        :param page_number: The page_number of this DescribeRouteEntryListRequest.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this DescribeRouteEntryListRequest.  # noqa: E501


        :return: The page_size of this DescribeRouteEntryListRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this DescribeRouteEntryListRequest.


        :param page_size: The page_size of this DescribeRouteEntryListRequest.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                page_size is not None and page_size > 100):  # noqa: E501
            raise ValueError("Invalid value for `page_size`, must be a value less than or equal to `100`")  # noqa: E501

        self._page_size = page_size

    @property
    def route_entry_id(self):
        """Gets the route_entry_id of this DescribeRouteEntryListRequest.  # noqa: E501


        :return: The route_entry_id of this DescribeRouteEntryListRequest.  # noqa: E501
        :rtype: str
        """
        return self._route_entry_id

    @route_entry_id.setter
    def route_entry_id(self, route_entry_id):
        """Sets the route_entry_id of this DescribeRouteEntryListRequest.


        :param route_entry_id: The route_entry_id of this DescribeRouteEntryListRequest.  # noqa: E501
        :type: str
        """

        self._route_entry_id = route_entry_id

    @property
    def route_entry_name(self):
        """Gets the route_entry_name of this DescribeRouteEntryListRequest.  # noqa: E501


        :return: The route_entry_name of this DescribeRouteEntryListRequest.  # noqa: E501
        :rtype: str
        """
        return self._route_entry_name

    @route_entry_name.setter
    def route_entry_name(self, route_entry_name):
        """Sets the route_entry_name of this DescribeRouteEntryListRequest.


        :param route_entry_name: The route_entry_name of this DescribeRouteEntryListRequest.  # noqa: E501
        :type: str
        """

        self._route_entry_name = route_entry_name

    @property
    def route_entry_type(self):
        """Gets the route_entry_type of this DescribeRouteEntryListRequest.  # noqa: E501


        :return: The route_entry_type of this DescribeRouteEntryListRequest.  # noqa: E501
        :rtype: str
        """
        return self._route_entry_type

    @route_entry_type.setter
    def route_entry_type(self, route_entry_type):
        """Sets the route_entry_type of this DescribeRouteEntryListRequest.


        :param route_entry_type: The route_entry_type of this DescribeRouteEntryListRequest.  # noqa: E501
        :type: str
        """

        self._route_entry_type = route_entry_type

    @property
    def route_table_id(self):
        """Gets the route_table_id of this DescribeRouteEntryListRequest.  # noqa: E501


        :return: The route_table_id of this DescribeRouteEntryListRequest.  # noqa: E501
        :rtype: str
        """
        return self._route_table_id

    @route_table_id.setter
    def route_table_id(self, route_table_id):
        """Sets the route_table_id of this DescribeRouteEntryListRequest.


        :param route_table_id: The route_table_id of this DescribeRouteEntryListRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and route_table_id is None:
            raise ValueError("Invalid value for `route_table_id`, must not be `None`")  # noqa: E501

        self._route_table_id = route_table_id

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
        if issubclass(DescribeRouteEntryListRequest, dict):
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
        if not isinstance(other, DescribeRouteEntryListRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeRouteEntryListRequest):
            return True

        return self.to_dict() != other.to_dict()
