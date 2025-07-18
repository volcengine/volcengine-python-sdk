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


class WhiteListForGetWhiteListOutput(object):
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
        'external_user_id': 'str',
        'nick_name': 'str'
    }

    attribute_map = {
        'external_user_id': 'ExternalUserId',
        'nick_name': 'NickName'
    }

    def __init__(self, external_user_id=None, nick_name=None, _configuration=None):  # noqa: E501
        """WhiteListForGetWhiteListOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._external_user_id = None
        self._nick_name = None
        self.discriminator = None

        if external_user_id is not None:
            self.external_user_id = external_user_id
        if nick_name is not None:
            self.nick_name = nick_name

    @property
    def external_user_id(self):
        """Gets the external_user_id of this WhiteListForGetWhiteListOutput.  # noqa: E501


        :return: The external_user_id of this WhiteListForGetWhiteListOutput.  # noqa: E501
        :rtype: str
        """
        return self._external_user_id

    @external_user_id.setter
    def external_user_id(self, external_user_id):
        """Sets the external_user_id of this WhiteListForGetWhiteListOutput.


        :param external_user_id: The external_user_id of this WhiteListForGetWhiteListOutput.  # noqa: E501
        :type: str
        """

        self._external_user_id = external_user_id

    @property
    def nick_name(self):
        """Gets the nick_name of this WhiteListForGetWhiteListOutput.  # noqa: E501


        :return: The nick_name of this WhiteListForGetWhiteListOutput.  # noqa: E501
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        """Sets the nick_name of this WhiteListForGetWhiteListOutput.


        :param nick_name: The nick_name of this WhiteListForGetWhiteListOutput.  # noqa: E501
        :type: str
        """

        self._nick_name = nick_name

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
        if issubclass(WhiteListForGetWhiteListOutput, dict):
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
        if not isinstance(other, WhiteListForGetWhiteListOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WhiteListForGetWhiteListOutput):
            return True

        return self.to_dict() != other.to_dict()
