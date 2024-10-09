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


class DescribeIpAddressPoolCidrBlocksResponse(object):
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
        'ip_address_poo_cidr_blocks': 'list[IpAddressPooCidrBlockForDescribeIpAddressPoolCidrBlocksOutput]',
        'next_token': 'str',
        'page_number': 'int',
        'request_id': 'str',
        'total_count': 'int'
    }

    attribute_map = {
        'ip_address_poo_cidr_blocks': 'IpAddressPooCidrBlocks',
        'next_token': 'NextToken',
        'page_number': 'PageNumber',
        'request_id': 'RequestId',
        'total_count': 'TotalCount'
    }

    def __init__(self, ip_address_poo_cidr_blocks=None, next_token=None, page_number=None, request_id=None, total_count=None, _configuration=None):  # noqa: E501
        """DescribeIpAddressPoolCidrBlocksResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._ip_address_poo_cidr_blocks = None
        self._next_token = None
        self._page_number = None
        self._request_id = None
        self._total_count = None
        self.discriminator = None

        if ip_address_poo_cidr_blocks is not None:
            self.ip_address_poo_cidr_blocks = ip_address_poo_cidr_blocks
        if next_token is not None:
            self.next_token = next_token
        if page_number is not None:
            self.page_number = page_number
        if request_id is not None:
            self.request_id = request_id
        if total_count is not None:
            self.total_count = total_count

    @property
    def ip_address_poo_cidr_blocks(self):
        """Gets the ip_address_poo_cidr_blocks of this DescribeIpAddressPoolCidrBlocksResponse.  # noqa: E501


        :return: The ip_address_poo_cidr_blocks of this DescribeIpAddressPoolCidrBlocksResponse.  # noqa: E501
        :rtype: list[IpAddressPooCidrBlockForDescribeIpAddressPoolCidrBlocksOutput]
        """
        return self._ip_address_poo_cidr_blocks

    @ip_address_poo_cidr_blocks.setter
    def ip_address_poo_cidr_blocks(self, ip_address_poo_cidr_blocks):
        """Sets the ip_address_poo_cidr_blocks of this DescribeIpAddressPoolCidrBlocksResponse.


        :param ip_address_poo_cidr_blocks: The ip_address_poo_cidr_blocks of this DescribeIpAddressPoolCidrBlocksResponse.  # noqa: E501
        :type: list[IpAddressPooCidrBlockForDescribeIpAddressPoolCidrBlocksOutput]
        """

        self._ip_address_poo_cidr_blocks = ip_address_poo_cidr_blocks

    @property
    def next_token(self):
        """Gets the next_token of this DescribeIpAddressPoolCidrBlocksResponse.  # noqa: E501


        :return: The next_token of this DescribeIpAddressPoolCidrBlocksResponse.  # noqa: E501
        :rtype: str
        """
        return self._next_token

    @next_token.setter
    def next_token(self, next_token):
        """Sets the next_token of this DescribeIpAddressPoolCidrBlocksResponse.


        :param next_token: The next_token of this DescribeIpAddressPoolCidrBlocksResponse.  # noqa: E501
        :type: str
        """

        self._next_token = next_token

    @property
    def page_number(self):
        """Gets the page_number of this DescribeIpAddressPoolCidrBlocksResponse.  # noqa: E501


        :return: The page_number of this DescribeIpAddressPoolCidrBlocksResponse.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this DescribeIpAddressPoolCidrBlocksResponse.


        :param page_number: The page_number of this DescribeIpAddressPoolCidrBlocksResponse.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def request_id(self):
        """Gets the request_id of this DescribeIpAddressPoolCidrBlocksResponse.  # noqa: E501


        :return: The request_id of this DescribeIpAddressPoolCidrBlocksResponse.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this DescribeIpAddressPoolCidrBlocksResponse.


        :param request_id: The request_id of this DescribeIpAddressPoolCidrBlocksResponse.  # noqa: E501
        :type: str
        """

        self._request_id = request_id

    @property
    def total_count(self):
        """Gets the total_count of this DescribeIpAddressPoolCidrBlocksResponse.  # noqa: E501


        :return: The total_count of this DescribeIpAddressPoolCidrBlocksResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this DescribeIpAddressPoolCidrBlocksResponse.


        :param total_count: The total_count of this DescribeIpAddressPoolCidrBlocksResponse.  # noqa: E501
        :type: int
        """

        self._total_count = total_count

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
        if issubclass(DescribeIpAddressPoolCidrBlocksResponse, dict):
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
        if not isinstance(other, DescribeIpAddressPoolCidrBlocksResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeIpAddressPoolCidrBlocksResponse):
            return True

        return self.to_dict() != other.to_dict()
