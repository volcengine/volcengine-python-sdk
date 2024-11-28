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


class GetAlarmSyncTaskResponse(object):
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
        'base_info': 'BaseInfoForGetAlarmSyncTaskOutput'
    }

    attribute_map = {
        'base_info': 'BaseInfo'
    }

    def __init__(self, base_info=None, _configuration=None):  # noqa: E501
        """GetAlarmSyncTaskResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._base_info = None
        self.discriminator = None

        if base_info is not None:
            self.base_info = base_info

    @property
    def base_info(self):
        """Gets the base_info of this GetAlarmSyncTaskResponse.  # noqa: E501


        :return: The base_info of this GetAlarmSyncTaskResponse.  # noqa: E501
        :rtype: BaseInfoForGetAlarmSyncTaskOutput
        """
        return self._base_info

    @base_info.setter
    def base_info(self, base_info):
        """Sets the base_info of this GetAlarmSyncTaskResponse.


        :param base_info: The base_info of this GetAlarmSyncTaskResponse.  # noqa: E501
        :type: BaseInfoForGetAlarmSyncTaskOutput
        """

        self._base_info = base_info

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
        if issubclass(GetAlarmSyncTaskResponse, dict):
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
        if not isinstance(other, GetAlarmSyncTaskResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetAlarmSyncTaskResponse):
            return True

        return self.to_dict() != other.to_dict()