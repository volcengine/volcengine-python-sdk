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


class AddProhibitionWhiteResponse(object):
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
        'ip_failed': 'list[IpFailedForAddProhibitionWhiteOutput]',
        'ip_success': 'list[str]'
    }

    attribute_map = {
        'ip_failed': 'IpFailed',
        'ip_success': 'IpSuccess'
    }

    def __init__(self, ip_failed=None, ip_success=None, _configuration=None):  # noqa: E501
        """AddProhibitionWhiteResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._ip_failed = None
        self._ip_success = None
        self.discriminator = None

        if ip_failed is not None:
            self.ip_failed = ip_failed
        if ip_success is not None:
            self.ip_success = ip_success

    @property
    def ip_failed(self):
        """Gets the ip_failed of this AddProhibitionWhiteResponse.  # noqa: E501


        :return: The ip_failed of this AddProhibitionWhiteResponse.  # noqa: E501
        :rtype: list[IpFailedForAddProhibitionWhiteOutput]
        """
        return self._ip_failed

    @ip_failed.setter
    def ip_failed(self, ip_failed):
        """Sets the ip_failed of this AddProhibitionWhiteResponse.


        :param ip_failed: The ip_failed of this AddProhibitionWhiteResponse.  # noqa: E501
        :type: list[IpFailedForAddProhibitionWhiteOutput]
        """

        self._ip_failed = ip_failed

    @property
    def ip_success(self):
        """Gets the ip_success of this AddProhibitionWhiteResponse.  # noqa: E501


        :return: The ip_success of this AddProhibitionWhiteResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._ip_success

    @ip_success.setter
    def ip_success(self, ip_success):
        """Sets the ip_success of this AddProhibitionWhiteResponse.


        :param ip_success: The ip_success of this AddProhibitionWhiteResponse.  # noqa: E501
        :type: list[str]
        """

        self._ip_success = ip_success

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
        if issubclass(AddProhibitionWhiteResponse, dict):
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
        if not isinstance(other, AddProhibitionWhiteResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddProhibitionWhiteResponse):
            return True

        return self.to_dict() != other.to_dict()