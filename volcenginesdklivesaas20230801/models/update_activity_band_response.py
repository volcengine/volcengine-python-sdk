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


class UpdateActivityBandResponse(object):
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
        'graphic_introduction': 'GraphicIntroductionForUpdateActivityBandOutput',
        'vertical_icon_url': 'str'
    }

    attribute_map = {
        'graphic_introduction': 'GraphicIntroduction',
        'vertical_icon_url': 'VerticalIconUrl'
    }

    def __init__(self, graphic_introduction=None, vertical_icon_url=None, _configuration=None):  # noqa: E501
        """UpdateActivityBandResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._graphic_introduction = None
        self._vertical_icon_url = None
        self.discriminator = None

        if graphic_introduction is not None:
            self.graphic_introduction = graphic_introduction
        if vertical_icon_url is not None:
            self.vertical_icon_url = vertical_icon_url

    @property
    def graphic_introduction(self):
        """Gets the graphic_introduction of this UpdateActivityBandResponse.  # noqa: E501


        :return: The graphic_introduction of this UpdateActivityBandResponse.  # noqa: E501
        :rtype: GraphicIntroductionForUpdateActivityBandOutput
        """
        return self._graphic_introduction

    @graphic_introduction.setter
    def graphic_introduction(self, graphic_introduction):
        """Sets the graphic_introduction of this UpdateActivityBandResponse.


        :param graphic_introduction: The graphic_introduction of this UpdateActivityBandResponse.  # noqa: E501
        :type: GraphicIntroductionForUpdateActivityBandOutput
        """

        self._graphic_introduction = graphic_introduction

    @property
    def vertical_icon_url(self):
        """Gets the vertical_icon_url of this UpdateActivityBandResponse.  # noqa: E501


        :return: The vertical_icon_url of this UpdateActivityBandResponse.  # noqa: E501
        :rtype: str
        """
        return self._vertical_icon_url

    @vertical_icon_url.setter
    def vertical_icon_url(self, vertical_icon_url):
        """Sets the vertical_icon_url of this UpdateActivityBandResponse.


        :param vertical_icon_url: The vertical_icon_url of this UpdateActivityBandResponse.  # noqa: E501
        :type: str
        """

        self._vertical_icon_url = vertical_icon_url

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
        if issubclass(UpdateActivityBandResponse, dict):
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
        if not isinstance(other, UpdateActivityBandResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateActivityBandResponse):
            return True

        return self.to_dict() != other.to_dict()
