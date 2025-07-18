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


class UpdateAccountCustomLinkConfigRequest(object):
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
        'backgroud_image_url': 'str',
        'backgroud_music_url': 'str'
    }

    attribute_map = {
        'backgroud_image_url': 'BackgroudImageUrl',
        'backgroud_music_url': 'BackgroudMusicUrl'
    }

    def __init__(self, backgroud_image_url=None, backgroud_music_url=None, _configuration=None):  # noqa: E501
        """UpdateAccountCustomLinkConfigRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._backgroud_image_url = None
        self._backgroud_music_url = None
        self.discriminator = None

        if backgroud_image_url is not None:
            self.backgroud_image_url = backgroud_image_url
        if backgroud_music_url is not None:
            self.backgroud_music_url = backgroud_music_url

    @property
    def backgroud_image_url(self):
        """Gets the backgroud_image_url of this UpdateAccountCustomLinkConfigRequest.  # noqa: E501


        :return: The backgroud_image_url of this UpdateAccountCustomLinkConfigRequest.  # noqa: E501
        :rtype: str
        """
        return self._backgroud_image_url

    @backgroud_image_url.setter
    def backgroud_image_url(self, backgroud_image_url):
        """Sets the backgroud_image_url of this UpdateAccountCustomLinkConfigRequest.


        :param backgroud_image_url: The backgroud_image_url of this UpdateAccountCustomLinkConfigRequest.  # noqa: E501
        :type: str
        """

        self._backgroud_image_url = backgroud_image_url

    @property
    def backgroud_music_url(self):
        """Gets the backgroud_music_url of this UpdateAccountCustomLinkConfigRequest.  # noqa: E501


        :return: The backgroud_music_url of this UpdateAccountCustomLinkConfigRequest.  # noqa: E501
        :rtype: str
        """
        return self._backgroud_music_url

    @backgroud_music_url.setter
    def backgroud_music_url(self, backgroud_music_url):
        """Sets the backgroud_music_url of this UpdateAccountCustomLinkConfigRequest.


        :param backgroud_music_url: The backgroud_music_url of this UpdateAccountCustomLinkConfigRequest.  # noqa: E501
        :type: str
        """

        self._backgroud_music_url = backgroud_music_url

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
        if issubclass(UpdateAccountCustomLinkConfigRequest, dict):
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
        if not isinstance(other, UpdateAccountCustomLinkConfigRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateAccountCustomLinkConfigRequest):
            return True

        return self.to_dict() != other.to_dict()
