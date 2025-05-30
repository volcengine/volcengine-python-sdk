# coding: utf-8

"""
    seccenter20240508

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class PlusAlarmInfo603ForGetHidsAlarmInfoOutput(object):
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
        'ko_file': 'str'
    }

    attribute_map = {
        'ko_file': 'KoFile'
    }

    def __init__(self, ko_file=None, _configuration=None):  # noqa: E501
        """PlusAlarmInfo603ForGetHidsAlarmInfoOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._ko_file = None
        self.discriminator = None

        if ko_file is not None:
            self.ko_file = ko_file

    @property
    def ko_file(self):
        """Gets the ko_file of this PlusAlarmInfo603ForGetHidsAlarmInfoOutput.  # noqa: E501


        :return: The ko_file of this PlusAlarmInfo603ForGetHidsAlarmInfoOutput.  # noqa: E501
        :rtype: str
        """
        return self._ko_file

    @ko_file.setter
    def ko_file(self, ko_file):
        """Sets the ko_file of this PlusAlarmInfo603ForGetHidsAlarmInfoOutput.


        :param ko_file: The ko_file of this PlusAlarmInfo603ForGetHidsAlarmInfoOutput.  # noqa: E501
        :type: str
        """

        self._ko_file = ko_file

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
        if issubclass(PlusAlarmInfo603ForGetHidsAlarmInfoOutput, dict):
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
        if not isinstance(other, PlusAlarmInfo603ForGetHidsAlarmInfoOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PlusAlarmInfo603ForGetHidsAlarmInfoOutput):
            return True

        return self.to_dict() != other.to_dict()
