# coding: utf-8

"""
    livesaas20230801

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ConvertUAInfoForUpdateActivityProductOutput(object):
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
        'ua_infos': 'list[UAInfoForUpdateActivityProductOutput]'
    }

    attribute_map = {
        'ua_infos': 'UAInfos'
    }

    def __init__(self, ua_infos=None, _configuration=None):  # noqa: E501
        """ConvertUAInfoForUpdateActivityProductOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._ua_infos = None
        self.discriminator = None

        if ua_infos is not None:
            self.ua_infos = ua_infos

    @property
    def ua_infos(self):
        """Gets the ua_infos of this ConvertUAInfoForUpdateActivityProductOutput.  # noqa: E501


        :return: The ua_infos of this ConvertUAInfoForUpdateActivityProductOutput.  # noqa: E501
        :rtype: list[UAInfoForUpdateActivityProductOutput]
        """
        return self._ua_infos

    @ua_infos.setter
    def ua_infos(self, ua_infos):
        """Sets the ua_infos of this ConvertUAInfoForUpdateActivityProductOutput.


        :param ua_infos: The ua_infos of this ConvertUAInfoForUpdateActivityProductOutput.  # noqa: E501
        :type: list[UAInfoForUpdateActivityProductOutput]
        """

        self._ua_infos = ua_infos

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
        if issubclass(ConvertUAInfoForUpdateActivityProductOutput, dict):
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
        if not isinstance(other, ConvertUAInfoForUpdateActivityProductOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConvertUAInfoForUpdateActivityProductOutput):
            return True

        return self.to_dict() != other.to_dict()
