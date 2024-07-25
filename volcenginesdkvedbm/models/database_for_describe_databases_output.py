# coding: utf-8

"""
    vedbm

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DatabaseForDescribeDatabasesOutput(object):
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
        'character_set_name': 'str',
        'db_name': 'str',
        'databases_privileges': 'list[DatabasesPrivilegeForDescribeDatabasesOutput]'
    }

    attribute_map = {
        'character_set_name': 'CharacterSetName',
        'db_name': 'DBName',
        'databases_privileges': 'DatabasesPrivileges'
    }

    def __init__(self, character_set_name=None, db_name=None, databases_privileges=None, _configuration=None):  # noqa: E501
        """DatabaseForDescribeDatabasesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._character_set_name = None
        self._db_name = None
        self._databases_privileges = None
        self.discriminator = None

        if character_set_name is not None:
            self.character_set_name = character_set_name
        if db_name is not None:
            self.db_name = db_name
        if databases_privileges is not None:
            self.databases_privileges = databases_privileges

    @property
    def character_set_name(self):
        """Gets the character_set_name of this DatabaseForDescribeDatabasesOutput.  # noqa: E501


        :return: The character_set_name of this DatabaseForDescribeDatabasesOutput.  # noqa: E501
        :rtype: str
        """
        return self._character_set_name

    @character_set_name.setter
    def character_set_name(self, character_set_name):
        """Sets the character_set_name of this DatabaseForDescribeDatabasesOutput.


        :param character_set_name: The character_set_name of this DatabaseForDescribeDatabasesOutput.  # noqa: E501
        :type: str
        """

        self._character_set_name = character_set_name

    @property
    def db_name(self):
        """Gets the db_name of this DatabaseForDescribeDatabasesOutput.  # noqa: E501


        :return: The db_name of this DatabaseForDescribeDatabasesOutput.  # noqa: E501
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """Sets the db_name of this DatabaseForDescribeDatabasesOutput.


        :param db_name: The db_name of this DatabaseForDescribeDatabasesOutput.  # noqa: E501
        :type: str
        """

        self._db_name = db_name

    @property
    def databases_privileges(self):
        """Gets the databases_privileges of this DatabaseForDescribeDatabasesOutput.  # noqa: E501


        :return: The databases_privileges of this DatabaseForDescribeDatabasesOutput.  # noqa: E501
        :rtype: list[DatabasesPrivilegeForDescribeDatabasesOutput]
        """
        return self._databases_privileges

    @databases_privileges.setter
    def databases_privileges(self, databases_privileges):
        """Sets the databases_privileges of this DatabaseForDescribeDatabasesOutput.


        :param databases_privileges: The databases_privileges of this DatabaseForDescribeDatabasesOutput.  # noqa: E501
        :type: list[DatabasesPrivilegeForDescribeDatabasesOutput]
        """

        self._databases_privileges = databases_privileges

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
        if issubclass(DatabaseForDescribeDatabasesOutput, dict):
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
        if not isinstance(other, DatabaseForDescribeDatabasesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DatabaseForDescribeDatabasesOutput):
            return True

        return self.to_dict() != other.to_dict()