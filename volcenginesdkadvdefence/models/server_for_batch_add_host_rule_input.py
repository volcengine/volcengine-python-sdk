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


class ServerForBatchAddHostRuleInput(object):
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
        'addr': 'str',
        'back_up': 'int',
        'port': 'int',
        'protocol': 'str',
        'weight': 'int'
    }

    attribute_map = {
        'addr': 'Addr',
        'back_up': 'BackUp',
        'port': 'Port',
        'protocol': 'Protocol',
        'weight': 'Weight'
    }

    def __init__(self, addr=None, back_up=None, port=None, protocol=None, weight=None, _configuration=None):  # noqa: E501
        """ServerForBatchAddHostRuleInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._addr = None
        self._back_up = None
        self._port = None
        self._protocol = None
        self._weight = None
        self.discriminator = None

        if addr is not None:
            self.addr = addr
        if back_up is not None:
            self.back_up = back_up
        if port is not None:
            self.port = port
        if protocol is not None:
            self.protocol = protocol
        if weight is not None:
            self.weight = weight

    @property
    def addr(self):
        """Gets the addr of this ServerForBatchAddHostRuleInput.  # noqa: E501


        :return: The addr of this ServerForBatchAddHostRuleInput.  # noqa: E501
        :rtype: str
        """
        return self._addr

    @addr.setter
    def addr(self, addr):
        """Sets the addr of this ServerForBatchAddHostRuleInput.


        :param addr: The addr of this ServerForBatchAddHostRuleInput.  # noqa: E501
        :type: str
        """

        self._addr = addr

    @property
    def back_up(self):
        """Gets the back_up of this ServerForBatchAddHostRuleInput.  # noqa: E501


        :return: The back_up of this ServerForBatchAddHostRuleInput.  # noqa: E501
        :rtype: int
        """
        return self._back_up

    @back_up.setter
    def back_up(self, back_up):
        """Sets the back_up of this ServerForBatchAddHostRuleInput.


        :param back_up: The back_up of this ServerForBatchAddHostRuleInput.  # noqa: E501
        :type: int
        """

        self._back_up = back_up

    @property
    def port(self):
        """Gets the port of this ServerForBatchAddHostRuleInput.  # noqa: E501


        :return: The port of this ServerForBatchAddHostRuleInput.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ServerForBatchAddHostRuleInput.


        :param port: The port of this ServerForBatchAddHostRuleInput.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def protocol(self):
        """Gets the protocol of this ServerForBatchAddHostRuleInput.  # noqa: E501


        :return: The protocol of this ServerForBatchAddHostRuleInput.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ServerForBatchAddHostRuleInput.


        :param protocol: The protocol of this ServerForBatchAddHostRuleInput.  # noqa: E501
        :type: str
        """

        self._protocol = protocol

    @property
    def weight(self):
        """Gets the weight of this ServerForBatchAddHostRuleInput.  # noqa: E501


        :return: The weight of this ServerForBatchAddHostRuleInput.  # noqa: E501
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this ServerForBatchAddHostRuleInput.


        :param weight: The weight of this ServerForBatchAddHostRuleInput.  # noqa: E501
        :type: int
        """

        self._weight = weight

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
        if issubclass(ServerForBatchAddHostRuleInput, dict):
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
        if not isinstance(other, ServerForBatchAddHostRuleInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ServerForBatchAddHostRuleInput):
            return True

        return self.to_dict() != other.to_dict()
