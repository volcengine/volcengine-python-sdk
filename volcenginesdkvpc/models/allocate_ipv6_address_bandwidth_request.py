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


class AllocateIpv6AddressBandwidthRequest(object):
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
        'bandwidth': 'int',
        'bandwidth_package_id': 'str',
        'billing_type': 'int',
        'client_token': 'str',
        'ipv6_address': 'str',
        'project_name': 'str',
        'tags': 'list[TagForAllocateIpv6AddressBandwidthInput]'
    }

    attribute_map = {
        'bandwidth': 'Bandwidth',
        'bandwidth_package_id': 'BandwidthPackageId',
        'billing_type': 'BillingType',
        'client_token': 'ClientToken',
        'ipv6_address': 'Ipv6Address',
        'project_name': 'ProjectName',
        'tags': 'Tags'
    }

    def __init__(self, bandwidth=None, bandwidth_package_id=None, billing_type=None, client_token=None, ipv6_address=None, project_name=None, tags=None, _configuration=None):  # noqa: E501
        """AllocateIpv6AddressBandwidthRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bandwidth = None
        self._bandwidth_package_id = None
        self._billing_type = None
        self._client_token = None
        self._ipv6_address = None
        self._project_name = None
        self._tags = None
        self.discriminator = None

        if bandwidth is not None:
            self.bandwidth = bandwidth
        if bandwidth_package_id is not None:
            self.bandwidth_package_id = bandwidth_package_id
        self.billing_type = billing_type
        if client_token is not None:
            self.client_token = client_token
        self.ipv6_address = ipv6_address
        if project_name is not None:
            self.project_name = project_name
        if tags is not None:
            self.tags = tags

    @property
    def bandwidth(self):
        """Gets the bandwidth of this AllocateIpv6AddressBandwidthRequest.  # noqa: E501


        :return: The bandwidth of this AllocateIpv6AddressBandwidthRequest.  # noqa: E501
        :rtype: int
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this AllocateIpv6AddressBandwidthRequest.


        :param bandwidth: The bandwidth of this AllocateIpv6AddressBandwidthRequest.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                bandwidth is not None and bandwidth < 1):  # noqa: E501
            raise ValueError("Invalid value for `bandwidth`, must be a value greater than or equal to `1`")  # noqa: E501

        self._bandwidth = bandwidth

    @property
    def bandwidth_package_id(self):
        """Gets the bandwidth_package_id of this AllocateIpv6AddressBandwidthRequest.  # noqa: E501


        :return: The bandwidth_package_id of this AllocateIpv6AddressBandwidthRequest.  # noqa: E501
        :rtype: str
        """
        return self._bandwidth_package_id

    @bandwidth_package_id.setter
    def bandwidth_package_id(self, bandwidth_package_id):
        """Sets the bandwidth_package_id of this AllocateIpv6AddressBandwidthRequest.


        :param bandwidth_package_id: The bandwidth_package_id of this AllocateIpv6AddressBandwidthRequest.  # noqa: E501
        :type: str
        """

        self._bandwidth_package_id = bandwidth_package_id

    @property
    def billing_type(self):
        """Gets the billing_type of this AllocateIpv6AddressBandwidthRequest.  # noqa: E501


        :return: The billing_type of this AllocateIpv6AddressBandwidthRequest.  # noqa: E501
        :rtype: int
        """
        return self._billing_type

    @billing_type.setter
    def billing_type(self, billing_type):
        """Sets the billing_type of this AllocateIpv6AddressBandwidthRequest.


        :param billing_type: The billing_type of this AllocateIpv6AddressBandwidthRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and billing_type is None:
            raise ValueError("Invalid value for `billing_type`, must not be `None`")  # noqa: E501

        self._billing_type = billing_type

    @property
    def client_token(self):
        """Gets the client_token of this AllocateIpv6AddressBandwidthRequest.  # noqa: E501


        :return: The client_token of this AllocateIpv6AddressBandwidthRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_token

    @client_token.setter
    def client_token(self, client_token):
        """Sets the client_token of this AllocateIpv6AddressBandwidthRequest.


        :param client_token: The client_token of this AllocateIpv6AddressBandwidthRequest.  # noqa: E501
        :type: str
        """

        self._client_token = client_token

    @property
    def ipv6_address(self):
        """Gets the ipv6_address of this AllocateIpv6AddressBandwidthRequest.  # noqa: E501


        :return: The ipv6_address of this AllocateIpv6AddressBandwidthRequest.  # noqa: E501
        :rtype: str
        """
        return self._ipv6_address

    @ipv6_address.setter
    def ipv6_address(self, ipv6_address):
        """Sets the ipv6_address of this AllocateIpv6AddressBandwidthRequest.


        :param ipv6_address: The ipv6_address of this AllocateIpv6AddressBandwidthRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and ipv6_address is None:
            raise ValueError("Invalid value for `ipv6_address`, must not be `None`")  # noqa: E501

        self._ipv6_address = ipv6_address

    @property
    def project_name(self):
        """Gets the project_name of this AllocateIpv6AddressBandwidthRequest.  # noqa: E501


        :return: The project_name of this AllocateIpv6AddressBandwidthRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this AllocateIpv6AddressBandwidthRequest.


        :param project_name: The project_name of this AllocateIpv6AddressBandwidthRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def tags(self):
        """Gets the tags of this AllocateIpv6AddressBandwidthRequest.  # noqa: E501


        :return: The tags of this AllocateIpv6AddressBandwidthRequest.  # noqa: E501
        :rtype: list[TagForAllocateIpv6AddressBandwidthInput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this AllocateIpv6AddressBandwidthRequest.


        :param tags: The tags of this AllocateIpv6AddressBandwidthRequest.  # noqa: E501
        :type: list[TagForAllocateIpv6AddressBandwidthInput]
        """

        self._tags = tags

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
        if issubclass(AllocateIpv6AddressBandwidthRequest, dict):
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
        if not isinstance(other, AllocateIpv6AddressBandwidthRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AllocateIpv6AddressBandwidthRequest):
            return True

        return self.to_dict() != other.to_dict()
