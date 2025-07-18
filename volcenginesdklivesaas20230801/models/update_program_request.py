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


class UpdateProgramRequest(object):
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
        'id': 'int',
        'loop_videos': 'list[LoopVideoForUpdateProgramInput]',
        'program_name': 'str'
    }

    attribute_map = {
        'id': 'Id',
        'loop_videos': 'LoopVideos',
        'program_name': 'ProgramName'
    }

    def __init__(self, id=None, loop_videos=None, program_name=None, _configuration=None):  # noqa: E501
        """UpdateProgramRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._loop_videos = None
        self._program_name = None
        self.discriminator = None

        self.id = id
        if loop_videos is not None:
            self.loop_videos = loop_videos
        if program_name is not None:
            self.program_name = program_name

    @property
    def id(self):
        """Gets the id of this UpdateProgramRequest.  # noqa: E501


        :return: The id of this UpdateProgramRequest.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateProgramRequest.


        :param id: The id of this UpdateProgramRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def loop_videos(self):
        """Gets the loop_videos of this UpdateProgramRequest.  # noqa: E501


        :return: The loop_videos of this UpdateProgramRequest.  # noqa: E501
        :rtype: list[LoopVideoForUpdateProgramInput]
        """
        return self._loop_videos

    @loop_videos.setter
    def loop_videos(self, loop_videos):
        """Sets the loop_videos of this UpdateProgramRequest.


        :param loop_videos: The loop_videos of this UpdateProgramRequest.  # noqa: E501
        :type: list[LoopVideoForUpdateProgramInput]
        """

        self._loop_videos = loop_videos

    @property
    def program_name(self):
        """Gets the program_name of this UpdateProgramRequest.  # noqa: E501


        :return: The program_name of this UpdateProgramRequest.  # noqa: E501
        :rtype: str
        """
        return self._program_name

    @program_name.setter
    def program_name(self, program_name):
        """Sets the program_name of this UpdateProgramRequest.


        :param program_name: The program_name of this UpdateProgramRequest.  # noqa: E501
        :type: str
        """

        self._program_name = program_name

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
        if issubclass(UpdateProgramRequest, dict):
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
        if not isinstance(other, UpdateProgramRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateProgramRequest):
            return True

        return self.to_dict() != other.to_dict()
