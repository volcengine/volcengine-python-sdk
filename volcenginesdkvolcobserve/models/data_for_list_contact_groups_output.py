# coding: utf-8

"""
    volc_observe

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DataForListContactGroupsOutput(object):
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
        'account_id': 'str',
        'created_at': 'str',
        'description': 'str',
        'id': 'str',
        'name': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'account_id': 'AccountId',
        'created_at': 'CreatedAt',
        'description': 'Description',
        'id': 'Id',
        'name': 'Name',
        'updated_at': 'UpdatedAt'
    }

    def __init__(self, account_id=None, created_at=None, description=None, id=None, name=None, updated_at=None, _configuration=None):  # noqa: E501
        """DataForListContactGroupsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_id = None
        self._created_at = None
        self._description = None
        self._id = None
        self._name = None
        self._updated_at = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if created_at is not None:
            self.created_at = created_at
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def account_id(self):
        """Gets the account_id of this DataForListContactGroupsOutput.  # noqa: E501


        :return: The account_id of this DataForListContactGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this DataForListContactGroupsOutput.


        :param account_id: The account_id of this DataForListContactGroupsOutput.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def created_at(self):
        """Gets the created_at of this DataForListContactGroupsOutput.  # noqa: E501


        :return: The created_at of this DataForListContactGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this DataForListContactGroupsOutput.


        :param created_at: The created_at of this DataForListContactGroupsOutput.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def description(self):
        """Gets the description of this DataForListContactGroupsOutput.  # noqa: E501


        :return: The description of this DataForListContactGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DataForListContactGroupsOutput.


        :param description: The description of this DataForListContactGroupsOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this DataForListContactGroupsOutput.  # noqa: E501


        :return: The id of this DataForListContactGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DataForListContactGroupsOutput.


        :param id: The id of this DataForListContactGroupsOutput.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this DataForListContactGroupsOutput.  # noqa: E501


        :return: The name of this DataForListContactGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DataForListContactGroupsOutput.


        :param name: The name of this DataForListContactGroupsOutput.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def updated_at(self):
        """Gets the updated_at of this DataForListContactGroupsOutput.  # noqa: E501


        :return: The updated_at of this DataForListContactGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this DataForListContactGroupsOutput.


        :param updated_at: The updated_at of this DataForListContactGroupsOutput.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

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
        if issubclass(DataForListContactGroupsOutput, dict):
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
        if not isinstance(other, DataForListContactGroupsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataForListContactGroupsOutput):
            return True

        return self.to_dict() != other.to_dict()
