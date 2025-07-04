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


class TeachAssistantAccountForUpdateTeachAssistantAccountInput(object):
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
        'audience_group_ids': 'list[int]',
        'id': 'int',
        'identity_id': 'str',
        'nick_name': 'str',
        'password': 'str',
        'teach_assistant_features': 'list[int]',
        'title': 'str'
    }

    attribute_map = {
        'audience_group_ids': 'AudienceGroupIds',
        'id': 'Id',
        'identity_id': 'IdentityId',
        'nick_name': 'NickName',
        'password': 'Password',
        'teach_assistant_features': 'TeachAssistantFeatures',
        'title': 'Title'
    }

    def __init__(self, audience_group_ids=None, id=None, identity_id=None, nick_name=None, password=None, teach_assistant_features=None, title=None, _configuration=None):  # noqa: E501
        """TeachAssistantAccountForUpdateTeachAssistantAccountInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._audience_group_ids = None
        self._id = None
        self._identity_id = None
        self._nick_name = None
        self._password = None
        self._teach_assistant_features = None
        self._title = None
        self.discriminator = None

        if audience_group_ids is not None:
            self.audience_group_ids = audience_group_ids
        if id is not None:
            self.id = id
        if identity_id is not None:
            self.identity_id = identity_id
        if nick_name is not None:
            self.nick_name = nick_name
        if password is not None:
            self.password = password
        if teach_assistant_features is not None:
            self.teach_assistant_features = teach_assistant_features
        if title is not None:
            self.title = title

    @property
    def audience_group_ids(self):
        """Gets the audience_group_ids of this TeachAssistantAccountForUpdateTeachAssistantAccountInput.  # noqa: E501


        :return: The audience_group_ids of this TeachAssistantAccountForUpdateTeachAssistantAccountInput.  # noqa: E501
        :rtype: list[int]
        """
        return self._audience_group_ids

    @audience_group_ids.setter
    def audience_group_ids(self, audience_group_ids):
        """Sets the audience_group_ids of this TeachAssistantAccountForUpdateTeachAssistantAccountInput.


        :param audience_group_ids: The audience_group_ids of this TeachAssistantAccountForUpdateTeachAssistantAccountInput.  # noqa: E501
        :type: list[int]
        """

        self._audience_group_ids = audience_group_ids

    @property
    def id(self):
        """Gets the id of this TeachAssistantAccountForUpdateTeachAssistantAccountInput.  # noqa: E501


        :return: The id of this TeachAssistantAccountForUpdateTeachAssistantAccountInput.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TeachAssistantAccountForUpdateTeachAssistantAccountInput.


        :param id: The id of this TeachAssistantAccountForUpdateTeachAssistantAccountInput.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def identity_id(self):
        """Gets the identity_id of this TeachAssistantAccountForUpdateTeachAssistantAccountInput.  # noqa: E501


        :return: The identity_id of this TeachAssistantAccountForUpdateTeachAssistantAccountInput.  # noqa: E501
        :rtype: str
        """
        return self._identity_id

    @identity_id.setter
    def identity_id(self, identity_id):
        """Sets the identity_id of this TeachAssistantAccountForUpdateTeachAssistantAccountInput.


        :param identity_id: The identity_id of this TeachAssistantAccountForUpdateTeachAssistantAccountInput.  # noqa: E501
        :type: str
        """

        self._identity_id = identity_id

    @property
    def nick_name(self):
        """Gets the nick_name of this TeachAssistantAccountForUpdateTeachAssistantAccountInput.  # noqa: E501


        :return: The nick_name of this TeachAssistantAccountForUpdateTeachAssistantAccountInput.  # noqa: E501
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        """Sets the nick_name of this TeachAssistantAccountForUpdateTeachAssistantAccountInput.


        :param nick_name: The nick_name of this TeachAssistantAccountForUpdateTeachAssistantAccountInput.  # noqa: E501
        :type: str
        """

        self._nick_name = nick_name

    @property
    def password(self):
        """Gets the password of this TeachAssistantAccountForUpdateTeachAssistantAccountInput.  # noqa: E501


        :return: The password of this TeachAssistantAccountForUpdateTeachAssistantAccountInput.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this TeachAssistantAccountForUpdateTeachAssistantAccountInput.


        :param password: The password of this TeachAssistantAccountForUpdateTeachAssistantAccountInput.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def teach_assistant_features(self):
        """Gets the teach_assistant_features of this TeachAssistantAccountForUpdateTeachAssistantAccountInput.  # noqa: E501


        :return: The teach_assistant_features of this TeachAssistantAccountForUpdateTeachAssistantAccountInput.  # noqa: E501
        :rtype: list[int]
        """
        return self._teach_assistant_features

    @teach_assistant_features.setter
    def teach_assistant_features(self, teach_assistant_features):
        """Sets the teach_assistant_features of this TeachAssistantAccountForUpdateTeachAssistantAccountInput.


        :param teach_assistant_features: The teach_assistant_features of this TeachAssistantAccountForUpdateTeachAssistantAccountInput.  # noqa: E501
        :type: list[int]
        """

        self._teach_assistant_features = teach_assistant_features

    @property
    def title(self):
        """Gets the title of this TeachAssistantAccountForUpdateTeachAssistantAccountInput.  # noqa: E501


        :return: The title of this TeachAssistantAccountForUpdateTeachAssistantAccountInput.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this TeachAssistantAccountForUpdateTeachAssistantAccountInput.


        :param title: The title of this TeachAssistantAccountForUpdateTeachAssistantAccountInput.  # noqa: E501
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
        if issubclass(TeachAssistantAccountForUpdateTeachAssistantAccountInput, dict):
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
        if not isinstance(other, TeachAssistantAccountForUpdateTeachAssistantAccountInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TeachAssistantAccountForUpdateTeachAssistantAccountInput):
            return True

        return self.to_dict() != other.to_dict()
