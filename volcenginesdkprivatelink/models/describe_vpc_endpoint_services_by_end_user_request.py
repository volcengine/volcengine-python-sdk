# coding: utf-8

"""
    privatelink

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeVpcEndpointServicesByEndUserRequest(object):
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
        'filter_financial_locked': 'str',
        'page_number': 'int',
        'page_size': 'int',
        'service_id': 'str',
        'service_name': 'str',
        'service_owner': 'str',
        'service_type': 'str'
    }

    attribute_map = {
        'filter_financial_locked': 'FilterFinancialLocked',
        'page_number': 'PageNumber',
        'page_size': 'PageSize',
        'service_id': 'ServiceId',
        'service_name': 'ServiceName',
        'service_owner': 'ServiceOwner',
        'service_type': 'ServiceType'
    }

    def __init__(self, filter_financial_locked=None, page_number=None, page_size=None, service_id=None, service_name=None, service_owner=None, service_type=None, _configuration=None):  # noqa: E501
        """DescribeVpcEndpointServicesByEndUserRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._filter_financial_locked = None
        self._page_number = None
        self._page_size = None
        self._service_id = None
        self._service_name = None
        self._service_owner = None
        self._service_type = None
        self.discriminator = None

        if filter_financial_locked is not None:
            self.filter_financial_locked = filter_financial_locked
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if service_id is not None:
            self.service_id = service_id
        if service_name is not None:
            self.service_name = service_name
        if service_owner is not None:
            self.service_owner = service_owner
        if service_type is not None:
            self.service_type = service_type

    @property
    def filter_financial_locked(self):
        """Gets the filter_financial_locked of this DescribeVpcEndpointServicesByEndUserRequest.  # noqa: E501


        :return: The filter_financial_locked of this DescribeVpcEndpointServicesByEndUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._filter_financial_locked

    @filter_financial_locked.setter
    def filter_financial_locked(self, filter_financial_locked):
        """Sets the filter_financial_locked of this DescribeVpcEndpointServicesByEndUserRequest.


        :param filter_financial_locked: The filter_financial_locked of this DescribeVpcEndpointServicesByEndUserRequest.  # noqa: E501
        :type: str
        """

        self._filter_financial_locked = filter_financial_locked

    @property
    def page_number(self):
        """Gets the page_number of this DescribeVpcEndpointServicesByEndUserRequest.  # noqa: E501


        :return: The page_number of this DescribeVpcEndpointServicesByEndUserRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this DescribeVpcEndpointServicesByEndUserRequest.


        :param page_number: The page_number of this DescribeVpcEndpointServicesByEndUserRequest.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this DescribeVpcEndpointServicesByEndUserRequest.  # noqa: E501


        :return: The page_size of this DescribeVpcEndpointServicesByEndUserRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this DescribeVpcEndpointServicesByEndUserRequest.


        :param page_size: The page_size of this DescribeVpcEndpointServicesByEndUserRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def service_id(self):
        """Gets the service_id of this DescribeVpcEndpointServicesByEndUserRequest.  # noqa: E501


        :return: The service_id of this DescribeVpcEndpointServicesByEndUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this DescribeVpcEndpointServicesByEndUserRequest.


        :param service_id: The service_id of this DescribeVpcEndpointServicesByEndUserRequest.  # noqa: E501
        :type: str
        """

        self._service_id = service_id

    @property
    def service_name(self):
        """Gets the service_name of this DescribeVpcEndpointServicesByEndUserRequest.  # noqa: E501


        :return: The service_name of this DescribeVpcEndpointServicesByEndUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this DescribeVpcEndpointServicesByEndUserRequest.


        :param service_name: The service_name of this DescribeVpcEndpointServicesByEndUserRequest.  # noqa: E501
        :type: str
        """

        self._service_name = service_name

    @property
    def service_owner(self):
        """Gets the service_owner of this DescribeVpcEndpointServicesByEndUserRequest.  # noqa: E501


        :return: The service_owner of this DescribeVpcEndpointServicesByEndUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._service_owner

    @service_owner.setter
    def service_owner(self, service_owner):
        """Sets the service_owner of this DescribeVpcEndpointServicesByEndUserRequest.


        :param service_owner: The service_owner of this DescribeVpcEndpointServicesByEndUserRequest.  # noqa: E501
        :type: str
        """

        self._service_owner = service_owner

    @property
    def service_type(self):
        """Gets the service_type of this DescribeVpcEndpointServicesByEndUserRequest.  # noqa: E501


        :return: The service_type of this DescribeVpcEndpointServicesByEndUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this DescribeVpcEndpointServicesByEndUserRequest.


        :param service_type: The service_type of this DescribeVpcEndpointServicesByEndUserRequest.  # noqa: E501
        :type: str
        """

        self._service_type = service_type

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
        if issubclass(DescribeVpcEndpointServicesByEndUserRequest, dict):
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
        if not isinstance(other, DescribeVpcEndpointServicesByEndUserRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeVpcEndpointServicesByEndUserRequest):
            return True

        return self.to_dict() != other.to_dict()
