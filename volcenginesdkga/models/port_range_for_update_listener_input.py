# coding: utf-8

"""
    ga

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class PortRangeForUpdateListenerInput(object):
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
        'from_port': 'int',
        'to_port': 'int'
    }

    attribute_map = {
        'from_port': 'FromPort',
        'to_port': 'ToPort'
    }

    def __init__(self, from_port=None, to_port=None, _configuration=None):  # noqa: E501
        """PortRangeForUpdateListenerInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._from_port = None
        self._to_port = None
        self.discriminator = None

        if from_port is not None:
            self.from_port = from_port
        if to_port is not None:
            self.to_port = to_port

    @property
    def from_port(self):
        """Gets the from_port of this PortRangeForUpdateListenerInput.  # noqa: E501


        :return: The from_port of this PortRangeForUpdateListenerInput.  # noqa: E501
        :rtype: int
        """
        return self._from_port

    @from_port.setter
    def from_port(self, from_port):
        """Sets the from_port of this PortRangeForUpdateListenerInput.


        :param from_port: The from_port of this PortRangeForUpdateListenerInput.  # noqa: E501
        :type: int
        """

        self._from_port = from_port

    @property
    def to_port(self):
        """Gets the to_port of this PortRangeForUpdateListenerInput.  # noqa: E501


        :return: The to_port of this PortRangeForUpdateListenerInput.  # noqa: E501
        :rtype: int
        """
        return self._to_port

    @to_port.setter
    def to_port(self, to_port):
        """Sets the to_port of this PortRangeForUpdateListenerInput.


        :param to_port: The to_port of this PortRangeForUpdateListenerInput.  # noqa: E501
        :type: int
        """

        self._to_port = to_port

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
        if issubclass(PortRangeForUpdateListenerInput, dict):
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
        if not isinstance(other, PortRangeForUpdateListenerInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PortRangeForUpdateListenerInput):
            return True

        return self.to_dict() != other.to_dict()
