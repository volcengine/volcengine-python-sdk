# coding: utf-8

"""
    tis

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class GetQuotaInfoResponse(object):
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
        'device_info_list': 'DeviceInfoListForGetQuotaInfoOutput',
        'quota_info_list': 'list[QuotaInfoListForGetQuotaInfoOutput]'
    }

    attribute_map = {
        'device_info_list': 'deviceInfoList',
        'quota_info_list': 'quotaInfoList'
    }

    def __init__(self, device_info_list=None, quota_info_list=None, _configuration=None):  # noqa: E501
        """GetQuotaInfoResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._device_info_list = None
        self._quota_info_list = None
        self.discriminator = None

        if device_info_list is not None:
            self.device_info_list = device_info_list
        if quota_info_list is not None:
            self.quota_info_list = quota_info_list

    @property
    def device_info_list(self):
        """Gets the device_info_list of this GetQuotaInfoResponse.  # noqa: E501


        :return: The device_info_list of this GetQuotaInfoResponse.  # noqa: E501
        :rtype: DeviceInfoListForGetQuotaInfoOutput
        """
        return self._device_info_list

    @device_info_list.setter
    def device_info_list(self, device_info_list):
        """Sets the device_info_list of this GetQuotaInfoResponse.


        :param device_info_list: The device_info_list of this GetQuotaInfoResponse.  # noqa: E501
        :type: DeviceInfoListForGetQuotaInfoOutput
        """

        self._device_info_list = device_info_list

    @property
    def quota_info_list(self):
        """Gets the quota_info_list of this GetQuotaInfoResponse.  # noqa: E501


        :return: The quota_info_list of this GetQuotaInfoResponse.  # noqa: E501
        :rtype: list[QuotaInfoListForGetQuotaInfoOutput]
        """
        return self._quota_info_list

    @quota_info_list.setter
    def quota_info_list(self, quota_info_list):
        """Sets the quota_info_list of this GetQuotaInfoResponse.


        :param quota_info_list: The quota_info_list of this GetQuotaInfoResponse.  # noqa: E501
        :type: list[QuotaInfoListForGetQuotaInfoOutput]
        """

        self._quota_info_list = quota_info_list

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
        if issubclass(GetQuotaInfoResponse, dict):
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
        if not isinstance(other, GetQuotaInfoResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetQuotaInfoResponse):
            return True

        return self.to_dict() != other.to_dict()
