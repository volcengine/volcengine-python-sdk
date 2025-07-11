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


class LineDetailForGetCustomActMsgAPIOutput(object):
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
        'back_push_info': 'list[BackPushInfoForGetCustomActMsgAPIOutput]',
        'backup_forward_info': 'list[BackupForwardInfoForGetCustomActMsgAPIOutput]',
        'expire_time': 'int',
        'forward_info': 'list[ForwardInfoForGetCustomActMsgAPIOutput]',
        'line_id': 'int',
        'line_name': 'str',
        'main_push_info': 'list[MainPushInfoForGetCustomActMsgAPIOutput]'
    }

    attribute_map = {
        'back_push_info': 'BackPushInfo',
        'backup_forward_info': 'BackupForwardInfo',
        'expire_time': 'ExpireTime',
        'forward_info': 'ForwardInfo',
        'line_id': 'LineId',
        'line_name': 'LineName',
        'main_push_info': 'MainPushInfo'
    }

    def __init__(self, back_push_info=None, backup_forward_info=None, expire_time=None, forward_info=None, line_id=None, line_name=None, main_push_info=None, _configuration=None):  # noqa: E501
        """LineDetailForGetCustomActMsgAPIOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._back_push_info = None
        self._backup_forward_info = None
        self._expire_time = None
        self._forward_info = None
        self._line_id = None
        self._line_name = None
        self._main_push_info = None
        self.discriminator = None

        if back_push_info is not None:
            self.back_push_info = back_push_info
        if backup_forward_info is not None:
            self.backup_forward_info = backup_forward_info
        if expire_time is not None:
            self.expire_time = expire_time
        if forward_info is not None:
            self.forward_info = forward_info
        if line_id is not None:
            self.line_id = line_id
        if line_name is not None:
            self.line_name = line_name
        if main_push_info is not None:
            self.main_push_info = main_push_info

    @property
    def back_push_info(self):
        """Gets the back_push_info of this LineDetailForGetCustomActMsgAPIOutput.  # noqa: E501


        :return: The back_push_info of this LineDetailForGetCustomActMsgAPIOutput.  # noqa: E501
        :rtype: list[BackPushInfoForGetCustomActMsgAPIOutput]
        """
        return self._back_push_info

    @back_push_info.setter
    def back_push_info(self, back_push_info):
        """Sets the back_push_info of this LineDetailForGetCustomActMsgAPIOutput.


        :param back_push_info: The back_push_info of this LineDetailForGetCustomActMsgAPIOutput.  # noqa: E501
        :type: list[BackPushInfoForGetCustomActMsgAPIOutput]
        """

        self._back_push_info = back_push_info

    @property
    def backup_forward_info(self):
        """Gets the backup_forward_info of this LineDetailForGetCustomActMsgAPIOutput.  # noqa: E501


        :return: The backup_forward_info of this LineDetailForGetCustomActMsgAPIOutput.  # noqa: E501
        :rtype: list[BackupForwardInfoForGetCustomActMsgAPIOutput]
        """
        return self._backup_forward_info

    @backup_forward_info.setter
    def backup_forward_info(self, backup_forward_info):
        """Sets the backup_forward_info of this LineDetailForGetCustomActMsgAPIOutput.


        :param backup_forward_info: The backup_forward_info of this LineDetailForGetCustomActMsgAPIOutput.  # noqa: E501
        :type: list[BackupForwardInfoForGetCustomActMsgAPIOutput]
        """

        self._backup_forward_info = backup_forward_info

    @property
    def expire_time(self):
        """Gets the expire_time of this LineDetailForGetCustomActMsgAPIOutput.  # noqa: E501


        :return: The expire_time of this LineDetailForGetCustomActMsgAPIOutput.  # noqa: E501
        :rtype: int
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this LineDetailForGetCustomActMsgAPIOutput.


        :param expire_time: The expire_time of this LineDetailForGetCustomActMsgAPIOutput.  # noqa: E501
        :type: int
        """

        self._expire_time = expire_time

    @property
    def forward_info(self):
        """Gets the forward_info of this LineDetailForGetCustomActMsgAPIOutput.  # noqa: E501


        :return: The forward_info of this LineDetailForGetCustomActMsgAPIOutput.  # noqa: E501
        :rtype: list[ForwardInfoForGetCustomActMsgAPIOutput]
        """
        return self._forward_info

    @forward_info.setter
    def forward_info(self, forward_info):
        """Sets the forward_info of this LineDetailForGetCustomActMsgAPIOutput.


        :param forward_info: The forward_info of this LineDetailForGetCustomActMsgAPIOutput.  # noqa: E501
        :type: list[ForwardInfoForGetCustomActMsgAPIOutput]
        """

        self._forward_info = forward_info

    @property
    def line_id(self):
        """Gets the line_id of this LineDetailForGetCustomActMsgAPIOutput.  # noqa: E501


        :return: The line_id of this LineDetailForGetCustomActMsgAPIOutput.  # noqa: E501
        :rtype: int
        """
        return self._line_id

    @line_id.setter
    def line_id(self, line_id):
        """Sets the line_id of this LineDetailForGetCustomActMsgAPIOutput.


        :param line_id: The line_id of this LineDetailForGetCustomActMsgAPIOutput.  # noqa: E501
        :type: int
        """

        self._line_id = line_id

    @property
    def line_name(self):
        """Gets the line_name of this LineDetailForGetCustomActMsgAPIOutput.  # noqa: E501


        :return: The line_name of this LineDetailForGetCustomActMsgAPIOutput.  # noqa: E501
        :rtype: str
        """
        return self._line_name

    @line_name.setter
    def line_name(self, line_name):
        """Sets the line_name of this LineDetailForGetCustomActMsgAPIOutput.


        :param line_name: The line_name of this LineDetailForGetCustomActMsgAPIOutput.  # noqa: E501
        :type: str
        """

        self._line_name = line_name

    @property
    def main_push_info(self):
        """Gets the main_push_info of this LineDetailForGetCustomActMsgAPIOutput.  # noqa: E501


        :return: The main_push_info of this LineDetailForGetCustomActMsgAPIOutput.  # noqa: E501
        :rtype: list[MainPushInfoForGetCustomActMsgAPIOutput]
        """
        return self._main_push_info

    @main_push_info.setter
    def main_push_info(self, main_push_info):
        """Sets the main_push_info of this LineDetailForGetCustomActMsgAPIOutput.


        :param main_push_info: The main_push_info of this LineDetailForGetCustomActMsgAPIOutput.  # noqa: E501
        :type: list[MainPushInfoForGetCustomActMsgAPIOutput]
        """

        self._main_push_info = main_push_info

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
        if issubclass(LineDetailForGetCustomActMsgAPIOutput, dict):
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
        if not isinstance(other, LineDetailForGetCustomActMsgAPIOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LineDetailForGetCustomActMsgAPIOutput):
            return True

        return self.to_dict() != other.to_dict()
