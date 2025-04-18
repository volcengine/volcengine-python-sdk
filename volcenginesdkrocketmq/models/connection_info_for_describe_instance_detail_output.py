# coding: utf-8

"""
    rocketmq

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ConnectionInfoForDescribeInstanceDetailOutput(object):
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
        'endpoint_address_ip': 'str',
        'endpoint_type': 'str',
        'internal_endpoint': 'str',
        'network_type': 'str',
        'public_endpoint': 'str'
    }

    attribute_map = {
        'endpoint_address_ip': 'EndpointAddressIP',
        'endpoint_type': 'EndpointType',
        'internal_endpoint': 'InternalEndpoint',
        'network_type': 'NetworkType',
        'public_endpoint': 'PublicEndpoint'
    }

    def __init__(self, endpoint_address_ip=None, endpoint_type=None, internal_endpoint=None, network_type=None, public_endpoint=None, _configuration=None):  # noqa: E501
        """ConnectionInfoForDescribeInstanceDetailOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._endpoint_address_ip = None
        self._endpoint_type = None
        self._internal_endpoint = None
        self._network_type = None
        self._public_endpoint = None
        self.discriminator = None

        if endpoint_address_ip is not None:
            self.endpoint_address_ip = endpoint_address_ip
        if endpoint_type is not None:
            self.endpoint_type = endpoint_type
        if internal_endpoint is not None:
            self.internal_endpoint = internal_endpoint
        if network_type is not None:
            self.network_type = network_type
        if public_endpoint is not None:
            self.public_endpoint = public_endpoint

    @property
    def endpoint_address_ip(self):
        """Gets the endpoint_address_ip of this ConnectionInfoForDescribeInstanceDetailOutput.  # noqa: E501


        :return: The endpoint_address_ip of this ConnectionInfoForDescribeInstanceDetailOutput.  # noqa: E501
        :rtype: str
        """
        return self._endpoint_address_ip

    @endpoint_address_ip.setter
    def endpoint_address_ip(self, endpoint_address_ip):
        """Sets the endpoint_address_ip of this ConnectionInfoForDescribeInstanceDetailOutput.


        :param endpoint_address_ip: The endpoint_address_ip of this ConnectionInfoForDescribeInstanceDetailOutput.  # noqa: E501
        :type: str
        """

        self._endpoint_address_ip = endpoint_address_ip

    @property
    def endpoint_type(self):
        """Gets the endpoint_type of this ConnectionInfoForDescribeInstanceDetailOutput.  # noqa: E501


        :return: The endpoint_type of this ConnectionInfoForDescribeInstanceDetailOutput.  # noqa: E501
        :rtype: str
        """
        return self._endpoint_type

    @endpoint_type.setter
    def endpoint_type(self, endpoint_type):
        """Sets the endpoint_type of this ConnectionInfoForDescribeInstanceDetailOutput.


        :param endpoint_type: The endpoint_type of this ConnectionInfoForDescribeInstanceDetailOutput.  # noqa: E501
        :type: str
        """

        self._endpoint_type = endpoint_type

    @property
    def internal_endpoint(self):
        """Gets the internal_endpoint of this ConnectionInfoForDescribeInstanceDetailOutput.  # noqa: E501


        :return: The internal_endpoint of this ConnectionInfoForDescribeInstanceDetailOutput.  # noqa: E501
        :rtype: str
        """
        return self._internal_endpoint

    @internal_endpoint.setter
    def internal_endpoint(self, internal_endpoint):
        """Sets the internal_endpoint of this ConnectionInfoForDescribeInstanceDetailOutput.


        :param internal_endpoint: The internal_endpoint of this ConnectionInfoForDescribeInstanceDetailOutput.  # noqa: E501
        :type: str
        """

        self._internal_endpoint = internal_endpoint

    @property
    def network_type(self):
        """Gets the network_type of this ConnectionInfoForDescribeInstanceDetailOutput.  # noqa: E501


        :return: The network_type of this ConnectionInfoForDescribeInstanceDetailOutput.  # noqa: E501
        :rtype: str
        """
        return self._network_type

    @network_type.setter
    def network_type(self, network_type):
        """Sets the network_type of this ConnectionInfoForDescribeInstanceDetailOutput.


        :param network_type: The network_type of this ConnectionInfoForDescribeInstanceDetailOutput.  # noqa: E501
        :type: str
        """

        self._network_type = network_type

    @property
    def public_endpoint(self):
        """Gets the public_endpoint of this ConnectionInfoForDescribeInstanceDetailOutput.  # noqa: E501


        :return: The public_endpoint of this ConnectionInfoForDescribeInstanceDetailOutput.  # noqa: E501
        :rtype: str
        """
        return self._public_endpoint

    @public_endpoint.setter
    def public_endpoint(self, public_endpoint):
        """Sets the public_endpoint of this ConnectionInfoForDescribeInstanceDetailOutput.


        :param public_endpoint: The public_endpoint of this ConnectionInfoForDescribeInstanceDetailOutput.  # noqa: E501
        :type: str
        """

        self._public_endpoint = public_endpoint

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
        if issubclass(ConnectionInfoForDescribeInstanceDetailOutput, dict):
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
        if not isinstance(other, ConnectionInfoForDescribeInstanceDetailOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConnectionInfoForDescribeInstanceDetailOutput):
            return True

        return self.to_dict() != other.to_dict()
