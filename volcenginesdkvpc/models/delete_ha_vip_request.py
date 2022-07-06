# coding: utf-8

"""
    vpc

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DeleteHaVipRequest(object):
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
        'ha_vip_id': 'str'
    }

    attribute_map = {
        'ha_vip_id': 'HaVipId'
    }

    def __init__(self, ha_vip_id=None, _configuration=None):  # noqa: E501
        """DeleteHaVipRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._ha_vip_id = None
        self.discriminator = None

        self.ha_vip_id = ha_vip_id

    @property
    def ha_vip_id(self):
        """Gets the ha_vip_id of this DeleteHaVipRequest.  # noqa: E501


        :return: The ha_vip_id of this DeleteHaVipRequest.  # noqa: E501
        :rtype: str
        """
        return self._ha_vip_id

    @ha_vip_id.setter
    def ha_vip_id(self, ha_vip_id):
        """Sets the ha_vip_id of this DeleteHaVipRequest.


        :param ha_vip_id: The ha_vip_id of this DeleteHaVipRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and ha_vip_id is None:
            raise ValueError("Invalid value for `ha_vip_id`, must not be `None`")  # noqa: E501

        self._ha_vip_id = ha_vip_id

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
        if issubclass(DeleteHaVipRequest, dict):
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
        if not isinstance(other, DeleteHaVipRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeleteHaVipRequest):
            return True

        return self.to_dict() != other.to_dict()
