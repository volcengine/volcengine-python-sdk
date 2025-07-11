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


class WatermarkConfigForUpdateVodPlayerConfigInput(object):
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
        'angle': 'int',
        'content': 'str',
        'font_color': 'str',
        'font_size': 'int',
        'is_play_page_watermark_enable': 'int',
        'opacity': 'int'
    }

    attribute_map = {
        'angle': 'Angle',
        'content': 'Content',
        'font_color': 'FontColor',
        'font_size': 'FontSize',
        'is_play_page_watermark_enable': 'IsPlayPageWatermarkEnable',
        'opacity': 'Opacity'
    }

    def __init__(self, angle=None, content=None, font_color=None, font_size=None, is_play_page_watermark_enable=None, opacity=None, _configuration=None):  # noqa: E501
        """WatermarkConfigForUpdateVodPlayerConfigInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._angle = None
        self._content = None
        self._font_color = None
        self._font_size = None
        self._is_play_page_watermark_enable = None
        self._opacity = None
        self.discriminator = None

        if angle is not None:
            self.angle = angle
        if content is not None:
            self.content = content
        if font_color is not None:
            self.font_color = font_color
        if font_size is not None:
            self.font_size = font_size
        if is_play_page_watermark_enable is not None:
            self.is_play_page_watermark_enable = is_play_page_watermark_enable
        if opacity is not None:
            self.opacity = opacity

    @property
    def angle(self):
        """Gets the angle of this WatermarkConfigForUpdateVodPlayerConfigInput.  # noqa: E501


        :return: The angle of this WatermarkConfigForUpdateVodPlayerConfigInput.  # noqa: E501
        :rtype: int
        """
        return self._angle

    @angle.setter
    def angle(self, angle):
        """Sets the angle of this WatermarkConfigForUpdateVodPlayerConfigInput.


        :param angle: The angle of this WatermarkConfigForUpdateVodPlayerConfigInput.  # noqa: E501
        :type: int
        """

        self._angle = angle

    @property
    def content(self):
        """Gets the content of this WatermarkConfigForUpdateVodPlayerConfigInput.  # noqa: E501


        :return: The content of this WatermarkConfigForUpdateVodPlayerConfigInput.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this WatermarkConfigForUpdateVodPlayerConfigInput.


        :param content: The content of this WatermarkConfigForUpdateVodPlayerConfigInput.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def font_color(self):
        """Gets the font_color of this WatermarkConfigForUpdateVodPlayerConfigInput.  # noqa: E501


        :return: The font_color of this WatermarkConfigForUpdateVodPlayerConfigInput.  # noqa: E501
        :rtype: str
        """
        return self._font_color

    @font_color.setter
    def font_color(self, font_color):
        """Sets the font_color of this WatermarkConfigForUpdateVodPlayerConfigInput.


        :param font_color: The font_color of this WatermarkConfigForUpdateVodPlayerConfigInput.  # noqa: E501
        :type: str
        """

        self._font_color = font_color

    @property
    def font_size(self):
        """Gets the font_size of this WatermarkConfigForUpdateVodPlayerConfigInput.  # noqa: E501


        :return: The font_size of this WatermarkConfigForUpdateVodPlayerConfigInput.  # noqa: E501
        :rtype: int
        """
        return self._font_size

    @font_size.setter
    def font_size(self, font_size):
        """Sets the font_size of this WatermarkConfigForUpdateVodPlayerConfigInput.


        :param font_size: The font_size of this WatermarkConfigForUpdateVodPlayerConfigInput.  # noqa: E501
        :type: int
        """

        self._font_size = font_size

    @property
    def is_play_page_watermark_enable(self):
        """Gets the is_play_page_watermark_enable of this WatermarkConfigForUpdateVodPlayerConfigInput.  # noqa: E501


        :return: The is_play_page_watermark_enable of this WatermarkConfigForUpdateVodPlayerConfigInput.  # noqa: E501
        :rtype: int
        """
        return self._is_play_page_watermark_enable

    @is_play_page_watermark_enable.setter
    def is_play_page_watermark_enable(self, is_play_page_watermark_enable):
        """Sets the is_play_page_watermark_enable of this WatermarkConfigForUpdateVodPlayerConfigInput.


        :param is_play_page_watermark_enable: The is_play_page_watermark_enable of this WatermarkConfigForUpdateVodPlayerConfigInput.  # noqa: E501
        :type: int
        """

        self._is_play_page_watermark_enable = is_play_page_watermark_enable

    @property
    def opacity(self):
        """Gets the opacity of this WatermarkConfigForUpdateVodPlayerConfigInput.  # noqa: E501


        :return: The opacity of this WatermarkConfigForUpdateVodPlayerConfigInput.  # noqa: E501
        :rtype: int
        """
        return self._opacity

    @opacity.setter
    def opacity(self, opacity):
        """Sets the opacity of this WatermarkConfigForUpdateVodPlayerConfigInput.


        :param opacity: The opacity of this WatermarkConfigForUpdateVodPlayerConfigInput.  # noqa: E501
        :type: int
        """

        self._opacity = opacity

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
        if issubclass(WatermarkConfigForUpdateVodPlayerConfigInput, dict):
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
        if not isinstance(other, WatermarkConfigForUpdateVodPlayerConfigInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WatermarkConfigForUpdateVodPlayerConfigInput):
            return True

        return self.to_dict() != other.to_dict()
