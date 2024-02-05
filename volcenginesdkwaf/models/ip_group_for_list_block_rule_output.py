# coding: utf-8

"""
    waf

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class IpGroupForListBlockRuleOutput(object):
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
        'ip_group_id': 'int',
        'name': 'str'
    }

    attribute_map = {
        'ip_group_id': 'IpGroupId',
        'name': 'Name'
    }

    def __init__(self, ip_group_id=None, name=None, _configuration=None):  # noqa: E501
        """IpGroupForListBlockRuleOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._ip_group_id = None
        self._name = None
        self.discriminator = None

        if ip_group_id is not None:
            self.ip_group_id = ip_group_id
        if name is not None:
            self.name = name

    @property
    def ip_group_id(self):
        """Gets the ip_group_id of this IpGroupForListBlockRuleOutput.  # noqa: E501


        :return: The ip_group_id of this IpGroupForListBlockRuleOutput.  # noqa: E501
        :rtype: int
        """
        return self._ip_group_id

    @ip_group_id.setter
    def ip_group_id(self, ip_group_id):
        """Sets the ip_group_id of this IpGroupForListBlockRuleOutput.


        :param ip_group_id: The ip_group_id of this IpGroupForListBlockRuleOutput.  # noqa: E501
        :type: int
        """

        self._ip_group_id = ip_group_id

    @property
    def name(self):
        """Gets the name of this IpGroupForListBlockRuleOutput.  # noqa: E501


        :return: The name of this IpGroupForListBlockRuleOutput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IpGroupForListBlockRuleOutput.


        :param name: The name of this IpGroupForListBlockRuleOutput.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(IpGroupForListBlockRuleOutput, dict):
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
        if not isinstance(other, IpGroupForListBlockRuleOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IpGroupForListBlockRuleOutput):
            return True

        return self.to_dict() != other.to_dict()
