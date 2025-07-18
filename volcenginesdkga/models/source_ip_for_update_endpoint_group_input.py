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


class SourceIPForUpdateEndpointGroupInput(object):
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
        'ip_range': 'str',
        'ip_range_id': 'str'
    }

    attribute_map = {
        'ip_range': 'IPRange',
        'ip_range_id': 'IPRangeId'
    }

    def __init__(self, ip_range=None, ip_range_id=None, _configuration=None):  # noqa: E501
        """SourceIPForUpdateEndpointGroupInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._ip_range = None
        self._ip_range_id = None
        self.discriminator = None

        if ip_range is not None:
            self.ip_range = ip_range
        if ip_range_id is not None:
            self.ip_range_id = ip_range_id

    @property
    def ip_range(self):
        """Gets the ip_range of this SourceIPForUpdateEndpointGroupInput.  # noqa: E501


        :return: The ip_range of this SourceIPForUpdateEndpointGroupInput.  # noqa: E501
        :rtype: str
        """
        return self._ip_range

    @ip_range.setter
    def ip_range(self, ip_range):
        """Sets the ip_range of this SourceIPForUpdateEndpointGroupInput.


        :param ip_range: The ip_range of this SourceIPForUpdateEndpointGroupInput.  # noqa: E501
        :type: str
        """

        self._ip_range = ip_range

    @property
    def ip_range_id(self):
        """Gets the ip_range_id of this SourceIPForUpdateEndpointGroupInput.  # noqa: E501


        :return: The ip_range_id of this SourceIPForUpdateEndpointGroupInput.  # noqa: E501
        :rtype: str
        """
        return self._ip_range_id

    @ip_range_id.setter
    def ip_range_id(self, ip_range_id):
        """Sets the ip_range_id of this SourceIPForUpdateEndpointGroupInput.


        :param ip_range_id: The ip_range_id of this SourceIPForUpdateEndpointGroupInput.  # noqa: E501
        :type: str
        """

        self._ip_range_id = ip_range_id

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
        if issubclass(SourceIPForUpdateEndpointGroupInput, dict):
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
        if not isinstance(other, SourceIPForUpdateEndpointGroupInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SourceIPForUpdateEndpointGroupInput):
            return True

        return self.to_dict() != other.to_dict()
