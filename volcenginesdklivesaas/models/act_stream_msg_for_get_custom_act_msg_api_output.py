# coding: utf-8

"""
    livesaas

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ActStreamMsgForGetCustomActMsgAPIOutput(object):
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
        'line_details': 'list[LineDetailForGetCustomActMsgAPIOutput]'
    }

    attribute_map = {
        'line_details': 'LineDetails'
    }

    def __init__(self, line_details=None, _configuration=None):  # noqa: E501
        """ActStreamMsgForGetCustomActMsgAPIOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._line_details = None
        self.discriminator = None

        if line_details is not None:
            self.line_details = line_details

    @property
    def line_details(self):
        """Gets the line_details of this ActStreamMsgForGetCustomActMsgAPIOutput.  # noqa: E501


        :return: The line_details of this ActStreamMsgForGetCustomActMsgAPIOutput.  # noqa: E501
        :rtype: list[LineDetailForGetCustomActMsgAPIOutput]
        """
        return self._line_details

    @line_details.setter
    def line_details(self, line_details):
        """Sets the line_details of this ActStreamMsgForGetCustomActMsgAPIOutput.


        :param line_details: The line_details of this ActStreamMsgForGetCustomActMsgAPIOutput.  # noqa: E501
        :type: list[LineDetailForGetCustomActMsgAPIOutput]
        """

        self._line_details = line_details

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
        if issubclass(ActStreamMsgForGetCustomActMsgAPIOutput, dict):
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
        if not isinstance(other, ActStreamMsgForGetCustomActMsgAPIOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ActStreamMsgForGetCustomActMsgAPIOutput):
            return True

        return self.to_dict() != other.to_dict()
