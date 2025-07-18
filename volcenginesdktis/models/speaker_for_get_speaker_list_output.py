# coding: utf-8

"""
    tis

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class SpeakerForGetSpeakerListOutput(object):
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
        'description': 'str',
        'id': 'str',
        'language': 'str',
        'name': 'str',
        'type': 'str'
    }

    attribute_map = {
        'description': 'Description',
        'id': 'ID',
        'language': 'Language',
        'name': 'Name',
        'type': 'Type'
    }

    def __init__(self, description=None, id=None, language=None, name=None, type=None, _configuration=None):  # noqa: E501
        """SpeakerForGetSpeakerListOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._description = None
        self._id = None
        self._language = None
        self._name = None
        self._type = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if language is not None:
            self.language = language
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type

    @property
    def description(self):
        """Gets the description of this SpeakerForGetSpeakerListOutput.  # noqa: E501


        :return: The description of this SpeakerForGetSpeakerListOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SpeakerForGetSpeakerListOutput.


        :param description: The description of this SpeakerForGetSpeakerListOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this SpeakerForGetSpeakerListOutput.  # noqa: E501


        :return: The id of this SpeakerForGetSpeakerListOutput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SpeakerForGetSpeakerListOutput.


        :param id: The id of this SpeakerForGetSpeakerListOutput.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def language(self):
        """Gets the language of this SpeakerForGetSpeakerListOutput.  # noqa: E501


        :return: The language of this SpeakerForGetSpeakerListOutput.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this SpeakerForGetSpeakerListOutput.


        :param language: The language of this SpeakerForGetSpeakerListOutput.  # noqa: E501
        :type: str
        """

        self._language = language

    @property
    def name(self):
        """Gets the name of this SpeakerForGetSpeakerListOutput.  # noqa: E501


        :return: The name of this SpeakerForGetSpeakerListOutput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SpeakerForGetSpeakerListOutput.


        :param name: The name of this SpeakerForGetSpeakerListOutput.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this SpeakerForGetSpeakerListOutput.  # noqa: E501


        :return: The type of this SpeakerForGetSpeakerListOutput.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SpeakerForGetSpeakerListOutput.


        :param type: The type of this SpeakerForGetSpeakerListOutput.  # noqa: E501
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
        if issubclass(SpeakerForGetSpeakerListOutput, dict):
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
        if not isinstance(other, SpeakerForGetSpeakerListOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SpeakerForGetSpeakerListOutput):
            return True

        return self.to_dict() != other.to_dict()
