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


class UserMetadataForListUsersOutput(object):
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
        'email': 'str',
        'email_is_verify': 'bool',
        'id': 'int',
        'mobile_phone': 'str',
        'mobile_phone_is_verify': 'bool',
        'tags': 'list[TagForListUsersOutput]',
        'trn': 'str',
        'update_date': 'str',
        'user_name': 'str'
    }

    attribute_map = {
        'account_id': 'AccountId',
        'create_date': 'CreateDate',
        'description': 'Description',
        'display_name': 'DisplayName',
        'email': 'Email',
        'email_is_verify': 'EmailIsVerify',
        'id': 'Id',
        'mobile_phone': 'MobilePhone',
        'mobile_phone_is_verify': 'MobilePhoneIsVerify',
        'tags': 'Tags',
        'trn': 'Trn',
        'update_date': 'UpdateDate',
        'user_name': 'UserName'
    }

    def __init__(self, account_id=None, create_date=None, description=None, display_name=None, email=None, email_is_verify=None, id=None, mobile_phone=None, mobile_phone_is_verify=None, tags=None, trn=None, update_date=None, user_name=None, _configuration=None):  # noqa: E501
        """UserMetadataForListUsersOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_id = None
        self._create_date = None
        self._description = None
        self._display_name = None
        self._email = None
        self._email_is_verify = None
        self._id = None
        self._mobile_phone = None
        self._mobile_phone_is_verify = None
        self._tags = None
        self._trn = None
        self._update_date = None
        self._user_name = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if create_date is not None:
            self.create_date = create_date
        if description is not None:
            self.description = description
        if display_name is not None:
            self.display_name = display_name
        if email is not None:
            self.email = email
        if email_is_verify is not None:
            self.email_is_verify = email_is_verify
        if id is not None:
            self.id = id
        if mobile_phone is not None:
            self.mobile_phone = mobile_phone
        if mobile_phone_is_verify is not None:
            self.mobile_phone_is_verify = mobile_phone_is_verify
        if tags is not None:
            self.tags = tags
        if trn is not None:
            self.trn = trn
        if update_date is not None:
            self.update_date = update_date
        if user_name is not None:
            self.user_name = user_name

    @property
    def account_id(self):
        """Gets the account_id of this UserMetadataForListUsersOutput.  # noqa: E501


        :return: The account_id of this UserMetadataForListUsersOutput.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this UserMetadataForListUsersOutput.


        :param account_id: The account_id of this UserMetadataForListUsersOutput.  # noqa: E501
        :type: int
        """

        self._account_id = account_id

    @property
    def create_date(self):
        """Gets the create_date of this UserMetadataForListUsersOutput.  # noqa: E501


        :return: The create_date of this UserMetadataForListUsersOutput.  # noqa: E501
        :rtype: str
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this UserMetadataForListUsersOutput.


        :param create_date: The create_date of this UserMetadataForListUsersOutput.  # noqa: E501
        :type: str
        """

        self._create_date = create_date

    @property
    def description(self):
        """Gets the description of this UserMetadataForListUsersOutput.  # noqa: E501


        :return: The description of this UserMetadataForListUsersOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UserMetadataForListUsersOutput.


        :param description: The description of this UserMetadataForListUsersOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def display_name(self):
        """Gets the display_name of this UserMetadataForListUsersOutput.  # noqa: E501


        :return: The display_name of this UserMetadataForListUsersOutput.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this UserMetadataForListUsersOutput.


        :param display_name: The display_name of this UserMetadataForListUsersOutput.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def email(self):
        """Gets the email of this UserMetadataForListUsersOutput.  # noqa: E501


        :return: The email of this UserMetadataForListUsersOutput.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserMetadataForListUsersOutput.


        :param email: The email of this UserMetadataForListUsersOutput.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def email_is_verify(self):
        """Gets the email_is_verify of this UserMetadataForListUsersOutput.  # noqa: E501


        :return: The email_is_verify of this UserMetadataForListUsersOutput.  # noqa: E501
        :rtype: bool
        """
        return self._email_is_verify

    @email_is_verify.setter
    def email_is_verify(self, email_is_verify):
        """Sets the email_is_verify of this UserMetadataForListUsersOutput.


        :param email_is_verify: The email_is_verify of this UserMetadataForListUsersOutput.  # noqa: E501
        :type: bool
        """

        self._email_is_verify = email_is_verify

    @property
    def id(self):
        """Gets the id of this UserMetadataForListUsersOutput.  # noqa: E501


        :return: The id of this UserMetadataForListUsersOutput.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserMetadataForListUsersOutput.


        :param id: The id of this UserMetadataForListUsersOutput.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def mobile_phone(self):
        """Gets the mobile_phone of this UserMetadataForListUsersOutput.  # noqa: E501


        :return: The mobile_phone of this UserMetadataForListUsersOutput.  # noqa: E501
        :rtype: str
        """
        return self._mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, mobile_phone):
        """Sets the mobile_phone of this UserMetadataForListUsersOutput.


        :param mobile_phone: The mobile_phone of this UserMetadataForListUsersOutput.  # noqa: E501
        :type: str
        """

        self._mobile_phone = mobile_phone

    @property
    def mobile_phone_is_verify(self):
        """Gets the mobile_phone_is_verify of this UserMetadataForListUsersOutput.  # noqa: E501


        :return: The mobile_phone_is_verify of this UserMetadataForListUsersOutput.  # noqa: E501
        :rtype: bool
        """
        return self._mobile_phone_is_verify

    @mobile_phone_is_verify.setter
    def mobile_phone_is_verify(self, mobile_phone_is_verify):
        """Sets the mobile_phone_is_verify of this UserMetadataForListUsersOutput.


        :param mobile_phone_is_verify: The mobile_phone_is_verify of this UserMetadataForListUsersOutput.  # noqa: E501
        :type: bool
        """

        self._mobile_phone_is_verify = mobile_phone_is_verify

    @property
    def tags(self):
        """Gets the tags of this UserMetadataForListUsersOutput.  # noqa: E501


        :return: The tags of this UserMetadataForListUsersOutput.  # noqa: E501
        :rtype: list[TagForListUsersOutput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this UserMetadataForListUsersOutput.


        :param tags: The tags of this UserMetadataForListUsersOutput.  # noqa: E501
        :type: list[TagForListUsersOutput]
        """

        self._tags = tags

    @property
    def trn(self):
        """Gets the trn of this UserMetadataForListUsersOutput.  # noqa: E501


        :return: The trn of this UserMetadataForListUsersOutput.  # noqa: E501
        :rtype: str
        """
        return self._trn

    @trn.setter
    def trn(self, trn):
        """Sets the trn of this UserMetadataForListUsersOutput.


        :param trn: The trn of this UserMetadataForListUsersOutput.  # noqa: E501
        :type: str
        """

        self._trn = trn

    @property
    def update_date(self):
        """Gets the update_date of this UserMetadataForListUsersOutput.  # noqa: E501


        :return: The update_date of this UserMetadataForListUsersOutput.  # noqa: E501
        :rtype: str
        """
        return self._update_date

    @update_date.setter
    def update_date(self, update_date):
        """Sets the update_date of this UserMetadataForListUsersOutput.


        :param update_date: The update_date of this UserMetadataForListUsersOutput.  # noqa: E501
        :type: str
        """

        self._update_date = update_date

    @property
    def user_name(self):
        """Gets the user_name of this UserMetadataForListUsersOutput.  # noqa: E501


        :return: The user_name of this UserMetadataForListUsersOutput.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this UserMetadataForListUsersOutput.


        :param user_name: The user_name of this UserMetadataForListUsersOutput.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

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
        if issubclass(UserMetadataForListUsersOutput, dict):
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
        if not isinstance(other, UserMetadataForListUsersOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserMetadataForListUsersOutput):
            return True

        return self.to_dict() != other.to_dict()
