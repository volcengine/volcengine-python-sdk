# coding: utf-8

"""
    ecs

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class RdmaForDescribeInstanceTypesOutput(object):
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
        'rdma_network_interfaces': 'int',
        'rdma_product_name': 'str'
    }

    attribute_map = {
        'rdma_network_interfaces': 'RdmaNetworkInterfaces',
        'rdma_product_name': 'RdmaProductName'
    }

    def __init__(self, rdma_network_interfaces=None, rdma_product_name=None, _configuration=None):  # noqa: E501
        """RdmaForDescribeInstanceTypesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._rdma_network_interfaces = None
        self._rdma_product_name = None
        self.discriminator = None

        if rdma_network_interfaces is not None:
            self.rdma_network_interfaces = rdma_network_interfaces
        if rdma_product_name is not None:
            self.rdma_product_name = rdma_product_name

    @property
    def rdma_network_interfaces(self):
        """Gets the rdma_network_interfaces of this RdmaForDescribeInstanceTypesOutput.  # noqa: E501


        :return: The rdma_network_interfaces of this RdmaForDescribeInstanceTypesOutput.  # noqa: E501
        :rtype: int
        """
        return self._rdma_network_interfaces

    @rdma_network_interfaces.setter
    def rdma_network_interfaces(self, rdma_network_interfaces):
        """Sets the rdma_network_interfaces of this RdmaForDescribeInstanceTypesOutput.


        :param rdma_network_interfaces: The rdma_network_interfaces of this RdmaForDescribeInstanceTypesOutput.  # noqa: E501
        :type: int
        """

        self._rdma_network_interfaces = rdma_network_interfaces

    @property
    def rdma_product_name(self):
        """Gets the rdma_product_name of this RdmaForDescribeInstanceTypesOutput.  # noqa: E501


        :return: The rdma_product_name of this RdmaForDescribeInstanceTypesOutput.  # noqa: E501
        :rtype: str
        """
        return self._rdma_product_name

    @rdma_product_name.setter
    def rdma_product_name(self, rdma_product_name):
        """Sets the rdma_product_name of this RdmaForDescribeInstanceTypesOutput.


        :param rdma_product_name: The rdma_product_name of this RdmaForDescribeInstanceTypesOutput.  # noqa: E501
        :type: str
        """

        self._rdma_product_name = rdma_product_name

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
        if issubclass(RdmaForDescribeInstanceTypesOutput, dict):
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
        if not isinstance(other, RdmaForDescribeInstanceTypesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RdmaForDescribeInstanceTypesOutput):
            return True

        return self.to_dict() != other.to_dict()
