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


class PrivateDNSNameConfigurationForDescribeVpcEndpointServicesByEndUserOutput(object):
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
        'name': 'str',
        'status': 'str',
        'type': 'str',
        'value': 'str'
    }

    attribute_map = {
        'name': 'Name',
        'status': 'Status',
        'type': 'Type',
        'value': 'Value'
    }

    def __init__(self, name=None, status=None, type=None, value=None, _configuration=None):  # noqa: E501
        """PrivateDNSNameConfigurationForDescribeVpcEndpointServicesByEndUserOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._status = None
        self._type = None
        self._value = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if value is not None:
            self.value = value

    @property
    def name(self):
        """Gets the name of this PrivateDNSNameConfigurationForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501


        :return: The name of this PrivateDNSNameConfigurationForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PrivateDNSNameConfigurationForDescribeVpcEndpointServicesByEndUserOutput.


        :param name: The name of this PrivateDNSNameConfigurationForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def status(self):
        """Gets the status of this PrivateDNSNameConfigurationForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501


        :return: The status of this PrivateDNSNameConfigurationForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PrivateDNSNameConfigurationForDescribeVpcEndpointServicesByEndUserOutput.


        :param status: The status of this PrivateDNSNameConfigurationForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def type(self):
        """Gets the type of this PrivateDNSNameConfigurationForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501


        :return: The type of this PrivateDNSNameConfigurationForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PrivateDNSNameConfigurationForDescribeVpcEndpointServicesByEndUserOutput.


        :param type: The type of this PrivateDNSNameConfigurationForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def value(self):
        """Gets the value of this PrivateDNSNameConfigurationForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501


        :return: The value of this PrivateDNSNameConfigurationForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this PrivateDNSNameConfigurationForDescribeVpcEndpointServicesByEndUserOutput.


        :param value: The value of this PrivateDNSNameConfigurationForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
        :type: str
        """

        self._value = value

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
        if issubclass(PrivateDNSNameConfigurationForDescribeVpcEndpointServicesByEndUserOutput, dict):
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
        if not isinstance(other, PrivateDNSNameConfigurationForDescribeVpcEndpointServicesByEndUserOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PrivateDNSNameConfigurationForDescribeVpcEndpointServicesByEndUserOutput):
            return True

        return self.to_dict() != other.to_dict()
