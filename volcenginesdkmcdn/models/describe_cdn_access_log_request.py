# coding: utf-8

"""
    mcdn

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeCdnAccessLogRequest(object):
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
        'domain': 'str',
        'domain_id': 'str',
        'end_time': 'int',
        'pagination': 'PaginationForDescribeCdnAccessLogInput',
        'start_time': 'int',
        'sub_product': 'str',
        'vendor': 'str'
    }

    attribute_map = {
        'domain': 'Domain',
        'domain_id': 'DomainId',
        'end_time': 'EndTime',
        'pagination': 'Pagination',
        'start_time': 'StartTime',
        'sub_product': 'SubProduct',
        'vendor': 'Vendor'
    }

    def __init__(self, domain=None, domain_id=None, end_time=None, pagination=None, start_time=None, sub_product=None, vendor=None, _configuration=None):  # noqa: E501
        """DescribeCdnAccessLogRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._domain = None
        self._domain_id = None
        self._end_time = None
        self._pagination = None
        self._start_time = None
        self._sub_product = None
        self._vendor = None
        self.discriminator = None

        if domain is not None:
            self.domain = domain
        if domain_id is not None:
            self.domain_id = domain_id
        self.end_time = end_time
        if pagination is not None:
            self.pagination = pagination
        self.start_time = start_time
        if sub_product is not None:
            self.sub_product = sub_product
        if vendor is not None:
            self.vendor = vendor

    @property
    def domain(self):
        """Gets the domain of this DescribeCdnAccessLogRequest.  # noqa: E501


        :return: The domain of this DescribeCdnAccessLogRequest.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this DescribeCdnAccessLogRequest.


        :param domain: The domain of this DescribeCdnAccessLogRequest.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def domain_id(self):
        """Gets the domain_id of this DescribeCdnAccessLogRequest.  # noqa: E501


        :return: The domain_id of this DescribeCdnAccessLogRequest.  # noqa: E501
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this DescribeCdnAccessLogRequest.


        :param domain_id: The domain_id of this DescribeCdnAccessLogRequest.  # noqa: E501
        :type: str
        """

        self._domain_id = domain_id

    @property
    def end_time(self):
        """Gets the end_time of this DescribeCdnAccessLogRequest.  # noqa: E501


        :return: The end_time of this DescribeCdnAccessLogRequest.  # noqa: E501
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this DescribeCdnAccessLogRequest.


        :param end_time: The end_time of this DescribeCdnAccessLogRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and end_time is None:
            raise ValueError("Invalid value for `end_time`, must not be `None`")  # noqa: E501

        self._end_time = end_time

    @property
    def pagination(self):
        """Gets the pagination of this DescribeCdnAccessLogRequest.  # noqa: E501


        :return: The pagination of this DescribeCdnAccessLogRequest.  # noqa: E501
        :rtype: PaginationForDescribeCdnAccessLogInput
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this DescribeCdnAccessLogRequest.


        :param pagination: The pagination of this DescribeCdnAccessLogRequest.  # noqa: E501
        :type: PaginationForDescribeCdnAccessLogInput
        """

        self._pagination = pagination

    @property
    def start_time(self):
        """Gets the start_time of this DescribeCdnAccessLogRequest.  # noqa: E501


        :return: The start_time of this DescribeCdnAccessLogRequest.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this DescribeCdnAccessLogRequest.


        :param start_time: The start_time of this DescribeCdnAccessLogRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and start_time is None:
            raise ValueError("Invalid value for `start_time`, must not be `None`")  # noqa: E501

        self._start_time = start_time

    @property
    def sub_product(self):
        """Gets the sub_product of this DescribeCdnAccessLogRequest.  # noqa: E501


        :return: The sub_product of this DescribeCdnAccessLogRequest.  # noqa: E501
        :rtype: str
        """
        return self._sub_product

    @sub_product.setter
    def sub_product(self, sub_product):
        """Sets the sub_product of this DescribeCdnAccessLogRequest.


        :param sub_product: The sub_product of this DescribeCdnAccessLogRequest.  # noqa: E501
        :type: str
        """

        self._sub_product = sub_product

    @property
    def vendor(self):
        """Gets the vendor of this DescribeCdnAccessLogRequest.  # noqa: E501


        :return: The vendor of this DescribeCdnAccessLogRequest.  # noqa: E501
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this DescribeCdnAccessLogRequest.


        :param vendor: The vendor of this DescribeCdnAccessLogRequest.  # noqa: E501
        :type: str
        """

        self._vendor = vendor

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
        if issubclass(DescribeCdnAccessLogRequest, dict):
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
        if not isinstance(other, DescribeCdnAccessLogRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeCdnAccessLogRequest):
            return True

        return self.to_dict() != other.to_dict()
