# coding: utf-8

"""
    iam

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class UserGroupForListGroupsOutput(object):
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
        'account_id': 'int',
        'create_date': 'str',
        'description': 'str',
        'display_name': 'str',
        'update_date': 'str',
        'user_group_id': 'int',
        'user_group_name': 'str'
    }

    attribute_map = {
        'account_id': 'AccountID',
        'create_date': 'CreateDate',
        'description': 'Description',
        'display_name': 'DisplayName',
        'update_date': 'UpdateDate',
        'user_group_id': 'UserGroupID',
        'user_group_name': 'UserGroupName'
    }

    def __init__(self, account_id=None, create_date=None, description=None, display_name=None, update_date=None, user_group_id=None, user_group_name=None, _configuration=None):  # noqa: E501
        """UserGroupForListGroupsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_id = None
        self._create_date = None
        self._description = None
        self._display_name = None
        self._update_date = None
        self._user_group_id = None
        self._user_group_name = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if create_date is not None:
            self.create_date = create_date
        if description is not None:
            self.description = description
        if display_name is not None:
            self.display_name = display_name
        if update_date is not None:
            self.update_date = update_date
        if user_group_id is not None:
            self.user_group_id = user_group_id
        if user_group_name is not None:
            self.user_group_name = user_group_name

    @property
    def account_id(self):
        """Gets the account_id of this UserGroupForListGroupsOutput.  # noqa: E501


        :return: The account_id of this UserGroupForListGroupsOutput.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this UserGroupForListGroupsOutput.


        :param account_id: The account_id of this UserGroupForListGroupsOutput.  # noqa: E501
        :type: int
        """

        self._account_id = account_id

    @property
    def create_date(self):
        """Gets the create_date of this UserGroupForListGroupsOutput.  # noqa: E501


        :return: The create_date of this UserGroupForListGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this UserGroupForListGroupsOutput.


        :param create_date: The create_date of this UserGroupForListGroupsOutput.  # noqa: E501
        :type: str
        """

        self._create_date = create_date

    @property
    def description(self):
        """Gets the description of this UserGroupForListGroupsOutput.  # noqa: E501


        :return: The description of this UserGroupForListGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UserGroupForListGroupsOutput.


        :param description: The description of this UserGroupForListGroupsOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def display_name(self):
        """Gets the display_name of this UserGroupForListGroupsOutput.  # noqa: E501


        :return: The display_name of this UserGroupForListGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this UserGroupForListGroupsOutput.


        :param display_name: The display_name of this UserGroupForListGroupsOutput.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def update_date(self):
        """Gets the update_date of this UserGroupForListGroupsOutput.  # noqa: E501


        :return: The update_date of this UserGroupForListGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._update_date

    @update_date.setter
    def update_date(self, update_date):
        """Sets the update_date of this UserGroupForListGroupsOutput.


        :param update_date: The update_date of this UserGroupForListGroupsOutput.  # noqa: E501
        :type: str
        """

        self._update_date = update_date

    @property
    def user_group_id(self):
        """Gets the user_group_id of this UserGroupForListGroupsOutput.  # noqa: E501


        :return: The user_group_id of this UserGroupForListGroupsOutput.  # noqa: E501
        :rtype: int
        """
        return self._user_group_id

    @user_group_id.setter
    def user_group_id(self, user_group_id):
        """Sets the user_group_id of this UserGroupForListGroupsOutput.


        :param user_group_id: The user_group_id of this UserGroupForListGroupsOutput.  # noqa: E501
        :type: int
        """

        self._user_group_id = user_group_id

    @property
    def user_group_name(self):
        """Gets the user_group_name of this UserGroupForListGroupsOutput.  # noqa: E501


        :return: The user_group_name of this UserGroupForListGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._user_group_name

    @user_group_name.setter
    def user_group_name(self, user_group_name):
        """Sets the user_group_name of this UserGroupForListGroupsOutput.


        :param user_group_name: The user_group_name of this UserGroupForListGroupsOutput.  # noqa: E501
        :type: str
        """

        self._user_group_name = user_group_name

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
        if issubclass(UserGroupForListGroupsOutput, dict):
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
        if not isinstance(other, UserGroupForListGroupsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserGroupForListGroupsOutput):
            return True

        return self.to_dict() != other.to_dict()
