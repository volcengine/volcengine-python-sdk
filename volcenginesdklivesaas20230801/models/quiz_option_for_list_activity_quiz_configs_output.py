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


class QuizOptionForListActivityQuizConfigsOutput(object):
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
        'option_count': 'int',
        'option_name': 'str',
        'option_percent': 'str',
        'option_site': 'str'
    }

    attribute_map = {
        'option_count': 'OptionCount',
        'option_name': 'OptionName',
        'option_percent': 'OptionPercent',
        'option_site': 'OptionSite'
    }

    def __init__(self, option_count=None, option_name=None, option_percent=None, option_site=None, _configuration=None):  # noqa: E501
        """QuizOptionForListActivityQuizConfigsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._option_count = None
        self._option_name = None
        self._option_percent = None
        self._option_site = None
        self.discriminator = None

        if option_count is not None:
            self.option_count = option_count
        if option_name is not None:
            self.option_name = option_name
        if option_percent is not None:
            self.option_percent = option_percent
        if option_site is not None:
            self.option_site = option_site

    @property
    def option_count(self):
        """Gets the option_count of this QuizOptionForListActivityQuizConfigsOutput.  # noqa: E501


        :return: The option_count of this QuizOptionForListActivityQuizConfigsOutput.  # noqa: E501
        :rtype: int
        """
        return self._option_count

    @option_count.setter
    def option_count(self, option_count):
        """Sets the option_count of this QuizOptionForListActivityQuizConfigsOutput.


        :param option_count: The option_count of this QuizOptionForListActivityQuizConfigsOutput.  # noqa: E501
        :type: int
        """

        self._option_count = option_count

    @property
    def option_name(self):
        """Gets the option_name of this QuizOptionForListActivityQuizConfigsOutput.  # noqa: E501


        :return: The option_name of this QuizOptionForListActivityQuizConfigsOutput.  # noqa: E501
        :rtype: str
        """
        return self._option_name

    @option_name.setter
    def option_name(self, option_name):
        """Sets the option_name of this QuizOptionForListActivityQuizConfigsOutput.


        :param option_name: The option_name of this QuizOptionForListActivityQuizConfigsOutput.  # noqa: E501
        :type: str
        """

        self._option_name = option_name

    @property
    def option_percent(self):
        """Gets the option_percent of this QuizOptionForListActivityQuizConfigsOutput.  # noqa: E501


        :return: The option_percent of this QuizOptionForListActivityQuizConfigsOutput.  # noqa: E501
        :rtype: str
        """
        return self._option_percent

    @option_percent.setter
    def option_percent(self, option_percent):
        """Sets the option_percent of this QuizOptionForListActivityQuizConfigsOutput.


        :param option_percent: The option_percent of this QuizOptionForListActivityQuizConfigsOutput.  # noqa: E501
        :type: str
        """

        self._option_percent = option_percent

    @property
    def option_site(self):
        """Gets the option_site of this QuizOptionForListActivityQuizConfigsOutput.  # noqa: E501


        :return: The option_site of this QuizOptionForListActivityQuizConfigsOutput.  # noqa: E501
        :rtype: str
        """
        return self._option_site

    @option_site.setter
    def option_site(self, option_site):
        """Sets the option_site of this QuizOptionForListActivityQuizConfigsOutput.


        :param option_site: The option_site of this QuizOptionForListActivityQuizConfigsOutput.  # noqa: E501
        :type: str
        """

        self._option_site = option_site

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
        if issubclass(QuizOptionForListActivityQuizConfigsOutput, dict):
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
        if not isinstance(other, QuizOptionForListActivityQuizConfigsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QuizOptionForListActivityQuizConfigsOutput):
            return True

        return self.to_dict() != other.to_dict()
