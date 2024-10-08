# coding: utf-8

"""
    mcdn

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeDnsScheduleActiveWeightsResponse(object):
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
        'active_weights': 'list[ActiveWeightForDescribeDnsScheduleActiveWeightsOutput]',
        'time_at': 'int'
    }

    attribute_map = {
        'active_weights': 'ActiveWeights',
        'time_at': 'TimeAt'
    }

    def __init__(self, active_weights=None, time_at=None, _configuration=None):  # noqa: E501
        """DescribeDnsScheduleActiveWeightsResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._active_weights = None
        self._time_at = None
        self.discriminator = None

        if active_weights is not None:
            self.active_weights = active_weights
        if time_at is not None:
            self.time_at = time_at

    @property
    def active_weights(self):
        """Gets the active_weights of this DescribeDnsScheduleActiveWeightsResponse.  # noqa: E501


        :return: The active_weights of this DescribeDnsScheduleActiveWeightsResponse.  # noqa: E501
        :rtype: list[ActiveWeightForDescribeDnsScheduleActiveWeightsOutput]
        """
        return self._active_weights

    @active_weights.setter
    def active_weights(self, active_weights):
        """Sets the active_weights of this DescribeDnsScheduleActiveWeightsResponse.


        :param active_weights: The active_weights of this DescribeDnsScheduleActiveWeightsResponse.  # noqa: E501
        :type: list[ActiveWeightForDescribeDnsScheduleActiveWeightsOutput]
        """

        self._active_weights = active_weights

    @property
    def time_at(self):
        """Gets the time_at of this DescribeDnsScheduleActiveWeightsResponse.  # noqa: E501


        :return: The time_at of this DescribeDnsScheduleActiveWeightsResponse.  # noqa: E501
        :rtype: int
        """
        return self._time_at

    @time_at.setter
    def time_at(self, time_at):
        """Sets the time_at of this DescribeDnsScheduleActiveWeightsResponse.


        :param time_at: The time_at of this DescribeDnsScheduleActiveWeightsResponse.  # noqa: E501
        :type: int
        """

        self._time_at = time_at

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
        if issubclass(DescribeDnsScheduleActiveWeightsResponse, dict):
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
        if not isinstance(other, DescribeDnsScheduleActiveWeightsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeDnsScheduleActiveWeightsResponse):
            return True

        return self.to_dict() != other.to_dict()
