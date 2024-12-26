# coding: utf-8

"""
    cloud_trail20180101

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class StopLoggingRequest(object):
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
        'trail_name': 'str'
    }

    attribute_map = {
        'trail_name': 'TrailName'
    }

    def __init__(self, trail_name=None, _configuration=None):  # noqa: E501
        """StopLoggingRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._trail_name = None
        self.discriminator = None

        if trail_name is not None:
            self.trail_name = trail_name

    @property
    def trail_name(self):
        """Gets the trail_name of this StopLoggingRequest.  # noqa: E501


        :return: The trail_name of this StopLoggingRequest.  # noqa: E501
        :rtype: str
        """
        return self._trail_name

    @trail_name.setter
    def trail_name(self, trail_name):
        """Sets the trail_name of this StopLoggingRequest.


        :param trail_name: The trail_name of this StopLoggingRequest.  # noqa: E501
        :type: str
        """

        self._trail_name = trail_name

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
        if issubclass(StopLoggingRequest, dict):
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
        if not isinstance(other, StopLoggingRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StopLoggingRequest):
            return True

        return self.to_dict() != other.to_dict()
