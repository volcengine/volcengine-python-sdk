# coding: utf-8

"""
    advdefence

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ProtoPortForBatchAddHostRuleInput(object):
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
        'ports': 'list[int]',
        'protocol': 'str'
    }

    attribute_map = {
        'ports': 'Ports',
        'protocol': 'Protocol'
    }

    def __init__(self, ports=None, protocol=None, _configuration=None):  # noqa: E501
        """ProtoPortForBatchAddHostRuleInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._ports = None
        self._protocol = None
        self.discriminator = None

        if ports is not None:
            self.ports = ports
        if protocol is not None:
            self.protocol = protocol

    @property
    def ports(self):
        """Gets the ports of this ProtoPortForBatchAddHostRuleInput.  # noqa: E501


        :return: The ports of this ProtoPortForBatchAddHostRuleInput.  # noqa: E501
        :rtype: list[int]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this ProtoPortForBatchAddHostRuleInput.


        :param ports: The ports of this ProtoPortForBatchAddHostRuleInput.  # noqa: E501
        :type: list[int]
        """

        self._ports = ports

    @property
    def protocol(self):
        """Gets the protocol of this ProtoPortForBatchAddHostRuleInput.  # noqa: E501


        :return: The protocol of this ProtoPortForBatchAddHostRuleInput.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ProtoPortForBatchAddHostRuleInput.


        :param protocol: The protocol of this ProtoPortForBatchAddHostRuleInput.  # noqa: E501
        :type: str
        """

        self._protocol = protocol

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
        if issubclass(ProtoPortForBatchAddHostRuleInput, dict):
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
        if not isinstance(other, ProtoPortForBatchAddHostRuleInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProtoPortForBatchAddHostRuleInput):
            return True

        return self.to_dict() != other.to_dict()
