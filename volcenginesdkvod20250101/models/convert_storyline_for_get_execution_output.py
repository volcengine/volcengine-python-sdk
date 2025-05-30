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


class ConvertStorylineForGetExecutionOutput(object):
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
        'clips': 'list[int]',
        'summary': 'str',
        'title': 'str'
    }

    attribute_map = {
        'clips': 'Clips',
        'summary': 'Summary',
        'title': 'Title'
    }

    def __init__(self, clips=None, summary=None, title=None, _configuration=None):  # noqa: E501
        """ConvertStorylineForGetExecutionOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._clips = None
        self._summary = None
        self._title = None
        self.discriminator = None

        if clips is not None:
            self.clips = clips
        if summary is not None:
            self.summary = summary
        if title is not None:
            self.title = title

    @property
    def clips(self):
        """Gets the clips of this ConvertStorylineForGetExecutionOutput.  # noqa: E501


        :return: The clips of this ConvertStorylineForGetExecutionOutput.  # noqa: E501
        :rtype: list[int]
        """
        return self._clips

    @clips.setter
    def clips(self, clips):
        """Sets the clips of this ConvertStorylineForGetExecutionOutput.


        :param clips: The clips of this ConvertStorylineForGetExecutionOutput.  # noqa: E501
        :type: list[int]
        """

        self._clips = clips

    @property
    def summary(self):
        """Gets the summary of this ConvertStorylineForGetExecutionOutput.  # noqa: E501


        :return: The summary of this ConvertStorylineForGetExecutionOutput.  # noqa: E501
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this ConvertStorylineForGetExecutionOutput.


        :param summary: The summary of this ConvertStorylineForGetExecutionOutput.  # noqa: E501
        :type: str
        """

        self._summary = summary

    @property
    def title(self):
        """Gets the title of this ConvertStorylineForGetExecutionOutput.  # noqa: E501


        :return: The title of this ConvertStorylineForGetExecutionOutput.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ConvertStorylineForGetExecutionOutput.


        :param title: The title of this ConvertStorylineForGetExecutionOutput.  # noqa: E501
        :type: str
        """

        self._title = title

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
        if issubclass(ConvertStorylineForGetExecutionOutput, dict):
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
        if not isinstance(other, ConvertStorylineForGetExecutionOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConvertStorylineForGetExecutionOutput):
            return True

        return self.to_dict() != other.to_dict()
