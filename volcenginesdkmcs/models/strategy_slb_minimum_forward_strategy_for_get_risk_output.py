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


class StrategySLBMinimumForwardStrategyForGetRiskOutput(object):
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
        'slb_listener_infos': 'list[SLBListenerInfoForGetRiskOutput]'
    }

    attribute_map = {
        'slb_listener_infos': 'SLBListenerInfos'
    }

    def __init__(self, slb_listener_infos=None, _configuration=None):  # noqa: E501
        """StrategySLBMinimumForwardStrategyForGetRiskOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._slb_listener_infos = None
        self.discriminator = None

        if slb_listener_infos is not None:
            self.slb_listener_infos = slb_listener_infos

    @property
    def slb_listener_infos(self):
        """Gets the slb_listener_infos of this StrategySLBMinimumForwardStrategyForGetRiskOutput.  # noqa: E501


        :return: The slb_listener_infos of this StrategySLBMinimumForwardStrategyForGetRiskOutput.  # noqa: E501
        :rtype: list[SLBListenerInfoForGetRiskOutput]
        """
        return self._slb_listener_infos

    @slb_listener_infos.setter
    def slb_listener_infos(self, slb_listener_infos):
        """Sets the slb_listener_infos of this StrategySLBMinimumForwardStrategyForGetRiskOutput.


        :param slb_listener_infos: The slb_listener_infos of this StrategySLBMinimumForwardStrategyForGetRiskOutput.  # noqa: E501
        :type: list[SLBListenerInfoForGetRiskOutput]
        """

        self._slb_listener_infos = slb_listener_infos

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
        if issubclass(StrategySLBMinimumForwardStrategyForGetRiskOutput, dict):
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
        if not isinstance(other, StrategySLBMinimumForwardStrategyForGetRiskOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StrategySLBMinimumForwardStrategyForGetRiskOutput):
            return True

        return self.to_dict() != other.to_dict()