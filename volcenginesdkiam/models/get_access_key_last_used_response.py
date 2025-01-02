# coding: utf-8

"""
    iam

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class GetAccessKeyLastUsedResponse(object):
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
        'access_key_last_used': 'AccessKeyLastUsedForGetAccessKeyLastUsedOutput'
    }

    attribute_map = {
        'access_key_last_used': 'AccessKeyLastUsed'
    }

    def __init__(self, access_key_last_used=None, _configuration=None):  # noqa: E501
        """GetAccessKeyLastUsedResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._access_key_last_used = None
        self.discriminator = None

        if access_key_last_used is not None:
            self.access_key_last_used = access_key_last_used

    @property
    def access_key_last_used(self):
        """Gets the access_key_last_used of this GetAccessKeyLastUsedResponse.  # noqa: E501


        :return: The access_key_last_used of this GetAccessKeyLastUsedResponse.  # noqa: E501
        :rtype: AccessKeyLastUsedForGetAccessKeyLastUsedOutput
        """
        return self._access_key_last_used

    @access_key_last_used.setter
    def access_key_last_used(self, access_key_last_used):
        """Sets the access_key_last_used of this GetAccessKeyLastUsedResponse.


        :param access_key_last_used: The access_key_last_used of this GetAccessKeyLastUsedResponse.  # noqa: E501
        :type: AccessKeyLastUsedForGetAccessKeyLastUsedOutput
        """

        self._access_key_last_used = access_key_last_used

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
        if issubclass(GetAccessKeyLastUsedResponse, dict):
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
        if not isinstance(other, GetAccessKeyLastUsedResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetAccessKeyLastUsedResponse):
            return True

        return self.to_dict() != other.to_dict()