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


class GetApiV1AlarmDetailRequest(object):
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
        'alarm_id': 'str'
    }

    attribute_map = {
        'alarm_id': 'alarm_id'
    }

    def __init__(self, alarm_id=None, _configuration=None):  # noqa: E501
        """GetApiV1AlarmDetailRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._alarm_id = None
        self.discriminator = None

        self.alarm_id = alarm_id

    @property
    def alarm_id(self):
        """Gets the alarm_id of this GetApiV1AlarmDetailRequest.  # noqa: E501


        :return: The alarm_id of this GetApiV1AlarmDetailRequest.  # noqa: E501
        :rtype: str
        """
        return self._alarm_id

    @alarm_id.setter
    def alarm_id(self, alarm_id):
        """Sets the alarm_id of this GetApiV1AlarmDetailRequest.


        :param alarm_id: The alarm_id of this GetApiV1AlarmDetailRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and alarm_id is None:
            raise ValueError("Invalid value for `alarm_id`, must not be `None`")  # noqa: E501

        self._alarm_id = alarm_id

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
        if issubclass(GetApiV1AlarmDetailRequest, dict):
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
        if not isinstance(other, GetApiV1AlarmDetailRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetApiV1AlarmDetailRequest):
            return True

        return self.to_dict() != other.to_dict()