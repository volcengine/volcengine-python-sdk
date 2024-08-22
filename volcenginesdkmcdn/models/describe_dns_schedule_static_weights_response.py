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


class DescribeDnsScheduleStaticWeightsResponse(object):
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
        'static_weights': 'list[StaticWeightForDescribeDnsScheduleStaticWeightsOutput]',
        'template_info': 'TemplateInfoForDescribeDnsScheduleStaticWeightsOutput',
        'weight_mode': 'str'
    }

    attribute_map = {
        'static_weights': 'StaticWeights',
        'template_info': 'TemplateInfo',
        'weight_mode': 'WeightMode'
    }

    def __init__(self, static_weights=None, template_info=None, weight_mode=None, _configuration=None):  # noqa: E501
        """DescribeDnsScheduleStaticWeightsResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._static_weights = None
        self._template_info = None
        self._weight_mode = None
        self.discriminator = None

        if static_weights is not None:
            self.static_weights = static_weights
        if template_info is not None:
            self.template_info = template_info
        if weight_mode is not None:
            self.weight_mode = weight_mode

    @property
    def static_weights(self):
        """Gets the static_weights of this DescribeDnsScheduleStaticWeightsResponse.  # noqa: E501


        :return: The static_weights of this DescribeDnsScheduleStaticWeightsResponse.  # noqa: E501
        :rtype: list[StaticWeightForDescribeDnsScheduleStaticWeightsOutput]
        """
        return self._static_weights

    @static_weights.setter
    def static_weights(self, static_weights):
        """Sets the static_weights of this DescribeDnsScheduleStaticWeightsResponse.


        :param static_weights: The static_weights of this DescribeDnsScheduleStaticWeightsResponse.  # noqa: E501
        :type: list[StaticWeightForDescribeDnsScheduleStaticWeightsOutput]
        """

        self._static_weights = static_weights

    @property
    def template_info(self):
        """Gets the template_info of this DescribeDnsScheduleStaticWeightsResponse.  # noqa: E501


        :return: The template_info of this DescribeDnsScheduleStaticWeightsResponse.  # noqa: E501
        :rtype: TemplateInfoForDescribeDnsScheduleStaticWeightsOutput
        """
        return self._template_info

    @template_info.setter
    def template_info(self, template_info):
        """Sets the template_info of this DescribeDnsScheduleStaticWeightsResponse.


        :param template_info: The template_info of this DescribeDnsScheduleStaticWeightsResponse.  # noqa: E501
        :type: TemplateInfoForDescribeDnsScheduleStaticWeightsOutput
        """

        self._template_info = template_info

    @property
    def weight_mode(self):
        """Gets the weight_mode of this DescribeDnsScheduleStaticWeightsResponse.  # noqa: E501


        :return: The weight_mode of this DescribeDnsScheduleStaticWeightsResponse.  # noqa: E501
        :rtype: str
        """
        return self._weight_mode

    @weight_mode.setter
    def weight_mode(self, weight_mode):
        """Sets the weight_mode of this DescribeDnsScheduleStaticWeightsResponse.


        :param weight_mode: The weight_mode of this DescribeDnsScheduleStaticWeightsResponse.  # noqa: E501
        :type: str
        """

        self._weight_mode = weight_mode

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
        if issubclass(DescribeDnsScheduleStaticWeightsResponse, dict):
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
        if not isinstance(other, DescribeDnsScheduleStaticWeightsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeDnsScheduleStaticWeightsResponse):
            return True

        return self.to_dict() != other.to_dict()
