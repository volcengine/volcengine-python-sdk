# coding: utf-8

"""
    mcs

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class PortRangeInfoForGetRiskOutput(object):
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
        'port_end': 'int',
        'port_start': 'int'
    }

    attribute_map = {
        'port_end': 'PortEnd',
        'port_start': 'PortStart'
    }

    def __init__(self, port_end=None, port_start=None, _configuration=None):  # noqa: E501
        """PortRangeInfoForGetRiskOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._port_end = None
        self._port_start = None
        self.discriminator = None

        if port_end is not None:
            self.port_end = port_end
        if port_start is not None:
            self.port_start = port_start

    @property
    def port_end(self):
        """Gets the port_end of this PortRangeInfoForGetRiskOutput.  # noqa: E501


        :return: The port_end of this PortRangeInfoForGetRiskOutput.  # noqa: E501
        :rtype: int
        """
        return self._port_end

    @port_end.setter
    def port_end(self, port_end):
        """Sets the port_end of this PortRangeInfoForGetRiskOutput.


        :param port_end: The port_end of this PortRangeInfoForGetRiskOutput.  # noqa: E501
        :type: int
        """

        self._port_end = port_end

    @property
    def port_start(self):
        """Gets the port_start of this PortRangeInfoForGetRiskOutput.  # noqa: E501


        :return: The port_start of this PortRangeInfoForGetRiskOutput.  # noqa: E501
        :rtype: int
        """
        return self._port_start

    @port_start.setter
    def port_start(self, port_start):
        """Sets the port_start of this PortRangeInfoForGetRiskOutput.


        :param port_start: The port_start of this PortRangeInfoForGetRiskOutput.  # noqa: E501
        :type: int
        """

        self._port_start = port_start

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
        if issubclass(PortRangeInfoForGetRiskOutput, dict):
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
        if not isinstance(other, PortRangeInfoForGetRiskOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PortRangeInfoForGetRiskOutput):
            return True

        return self.to_dict() != other.to_dict()
