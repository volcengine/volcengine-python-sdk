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


class GetWhiteListResponse(object):
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
        'activity_id': 'int',
        'white_list': 'list[WhiteListForGetWhiteListOutput]'
    }

    attribute_map = {
        'activity_id': 'ActivityId',
        'white_list': 'WhiteList'
    }

    def __init__(self, activity_id=None, white_list=None, _configuration=None):  # noqa: E501
        """GetWhiteListResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._activity_id = None
        self._white_list = None
        self.discriminator = None

        if activity_id is not None:
            self.activity_id = activity_id
        if white_list is not None:
            self.white_list = white_list

    @property
    def activity_id(self):
        """Gets the activity_id of this GetWhiteListResponse.  # noqa: E501


        :return: The activity_id of this GetWhiteListResponse.  # noqa: E501
        :rtype: int
        """
        return self._activity_id

    @activity_id.setter
    def activity_id(self, activity_id):
        """Sets the activity_id of this GetWhiteListResponse.


        :param activity_id: The activity_id of this GetWhiteListResponse.  # noqa: E501
        :type: int
        """

        self._activity_id = activity_id

    @property
    def white_list(self):
        """Gets the white_list of this GetWhiteListResponse.  # noqa: E501


        :return: The white_list of this GetWhiteListResponse.  # noqa: E501
        :rtype: list[WhiteListForGetWhiteListOutput]
        """
        return self._white_list

    @white_list.setter
    def white_list(self, white_list):
        """Sets the white_list of this GetWhiteListResponse.


        :param white_list: The white_list of this GetWhiteListResponse.  # noqa: E501
        :type: list[WhiteListForGetWhiteListOutput]
        """

        self._white_list = white_list

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
        if issubclass(GetWhiteListResponse, dict):
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
        if not isinstance(other, GetWhiteListResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetWhiteListResponse):
            return True

        return self.to_dict() != other.to_dict()
