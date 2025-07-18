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


class UpdateAccountBanStatusRequest(object):
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
        'ban_status': 'int',
        'user_ids': 'list[int]'
    }

    attribute_map = {
        'ban_status': 'BanStatus',
        'user_ids': 'UserIds'
    }

    def __init__(self, ban_status=None, user_ids=None, _configuration=None):  # noqa: E501
        """UpdateAccountBanStatusRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._ban_status = None
        self._user_ids = None
        self.discriminator = None

        self.ban_status = ban_status
        if user_ids is not None:
            self.user_ids = user_ids

    @property
    def ban_status(self):
        """Gets the ban_status of this UpdateAccountBanStatusRequest.  # noqa: E501


        :return: The ban_status of this UpdateAccountBanStatusRequest.  # noqa: E501
        :rtype: int
        """
        return self._ban_status

    @ban_status.setter
    def ban_status(self, ban_status):
        """Sets the ban_status of this UpdateAccountBanStatusRequest.


        :param ban_status: The ban_status of this UpdateAccountBanStatusRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and ban_status is None:
            raise ValueError("Invalid value for `ban_status`, must not be `None`")  # noqa: E501

        self._ban_status = ban_status

    @property
    def user_ids(self):
        """Gets the user_ids of this UpdateAccountBanStatusRequest.  # noqa: E501


        :return: The user_ids of this UpdateAccountBanStatusRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._user_ids

    @user_ids.setter
    def user_ids(self, user_ids):
        """Sets the user_ids of this UpdateAccountBanStatusRequest.


        :param user_ids: The user_ids of this UpdateAccountBanStatusRequest.  # noqa: E501
        :type: list[int]
        """

        self._user_ids = user_ids

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
        if issubclass(UpdateAccountBanStatusRequest, dict):
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
        if not isinstance(other, UpdateAccountBanStatusRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateAccountBanStatusRequest):
            return True

        return self.to_dict() != other.to_dict()
