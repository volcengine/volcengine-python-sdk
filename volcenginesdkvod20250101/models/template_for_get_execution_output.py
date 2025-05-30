# coding: utf-8

"""
    vod20250101

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class TemplateForGetExecutionOutput(object):
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
        'byte_hd': 'ByteHDForGetExecutionOutput',
        'enhance': 'EnhanceForGetExecutionOutput',
        'transcode_audio': 'TranscodeAudioForGetExecutionOutput',
        'transcode_video': 'TranscodeVideoForGetExecutionOutput',
        'type': 'str'
    }

    attribute_map = {
        'byte_hd': 'ByteHD',
        'enhance': 'Enhance',
        'transcode_audio': 'TranscodeAudio',
        'transcode_video': 'TranscodeVideo',
        'type': 'Type'
    }

    def __init__(self, byte_hd=None, enhance=None, transcode_audio=None, transcode_video=None, type=None, _configuration=None):  # noqa: E501
        """TemplateForGetExecutionOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._byte_hd = None
        self._enhance = None
        self._transcode_audio = None
        self._transcode_video = None
        self._type = None
        self.discriminator = None

        if byte_hd is not None:
            self.byte_hd = byte_hd
        if enhance is not None:
            self.enhance = enhance
        if transcode_audio is not None:
            self.transcode_audio = transcode_audio
        if transcode_video is not None:
            self.transcode_video = transcode_video
        if type is not None:
            self.type = type

    @property
    def byte_hd(self):
        """Gets the byte_hd of this TemplateForGetExecutionOutput.  # noqa: E501


        :return: The byte_hd of this TemplateForGetExecutionOutput.  # noqa: E501
        :rtype: ByteHDForGetExecutionOutput
        """
        return self._byte_hd

    @byte_hd.setter
    def byte_hd(self, byte_hd):
        """Sets the byte_hd of this TemplateForGetExecutionOutput.


        :param byte_hd: The byte_hd of this TemplateForGetExecutionOutput.  # noqa: E501
        :type: ByteHDForGetExecutionOutput
        """

        self._byte_hd = byte_hd

    @property
    def enhance(self):
        """Gets the enhance of this TemplateForGetExecutionOutput.  # noqa: E501


        :return: The enhance of this TemplateForGetExecutionOutput.  # noqa: E501
        :rtype: EnhanceForGetExecutionOutput
        """
        return self._enhance

    @enhance.setter
    def enhance(self, enhance):
        """Sets the enhance of this TemplateForGetExecutionOutput.


        :param enhance: The enhance of this TemplateForGetExecutionOutput.  # noqa: E501
        :type: EnhanceForGetExecutionOutput
        """

        self._enhance = enhance

    @property
    def transcode_audio(self):
        """Gets the transcode_audio of this TemplateForGetExecutionOutput.  # noqa: E501


        :return: The transcode_audio of this TemplateForGetExecutionOutput.  # noqa: E501
        :rtype: TranscodeAudioForGetExecutionOutput
        """
        return self._transcode_audio

    @transcode_audio.setter
    def transcode_audio(self, transcode_audio):
        """Sets the transcode_audio of this TemplateForGetExecutionOutput.


        :param transcode_audio: The transcode_audio of this TemplateForGetExecutionOutput.  # noqa: E501
        :type: TranscodeAudioForGetExecutionOutput
        """

        self._transcode_audio = transcode_audio

    @property
    def transcode_video(self):
        """Gets the transcode_video of this TemplateForGetExecutionOutput.  # noqa: E501


        :return: The transcode_video of this TemplateForGetExecutionOutput.  # noqa: E501
        :rtype: TranscodeVideoForGetExecutionOutput
        """
        return self._transcode_video

    @transcode_video.setter
    def transcode_video(self, transcode_video):
        """Sets the transcode_video of this TemplateForGetExecutionOutput.


        :param transcode_video: The transcode_video of this TemplateForGetExecutionOutput.  # noqa: E501
        :type: TranscodeVideoForGetExecutionOutput
        """

        self._transcode_video = transcode_video

    @property
    def type(self):
        """Gets the type of this TemplateForGetExecutionOutput.  # noqa: E501


        :return: The type of this TemplateForGetExecutionOutput.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TemplateForGetExecutionOutput.


        :param type: The type of this TemplateForGetExecutionOutput.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(TemplateForGetExecutionOutput, dict):
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
        if not isinstance(other, TemplateForGetExecutionOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TemplateForGetExecutionOutput):
            return True

        return self.to_dict() != other.to_dict()
