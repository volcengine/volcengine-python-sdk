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


class GetSecurityContactResponse(object):
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
        'email': 'str',
        'email_is_verify': 'bool',
        'mobile_phone': 'str',
        'mobile_phone_is_verify': 'bool',
        'new_secure_contact_info': 'NewSecureContactInfoForGetSecurityContactOutput'
    }

    attribute_map = {
        'email': 'Email',
        'email_is_verify': 'EmailIsVerify',
        'mobile_phone': 'MobilePhone',
        'mobile_phone_is_verify': 'MobilePhoneIsVerify',
        'new_secure_contact_info': 'NewSecureContactInfo'
    }

    def __init__(self, email=None, email_is_verify=None, mobile_phone=None, mobile_phone_is_verify=None, new_secure_contact_info=None, _configuration=None):  # noqa: E501
        """GetSecurityContactResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._email = None
        self._email_is_verify = None
        self._mobile_phone = None
        self._mobile_phone_is_verify = None
        self._new_secure_contact_info = None
        self.discriminator = None

        if email is not None:
            self.email = email
        if email_is_verify is not None:
            self.email_is_verify = email_is_verify
        if mobile_phone is not None:
            self.mobile_phone = mobile_phone
        if mobile_phone_is_verify is not None:
            self.mobile_phone_is_verify = mobile_phone_is_verify
        if new_secure_contact_info is not None:
            self.new_secure_contact_info = new_secure_contact_info

    @property
    def email(self):
        """Gets the email of this GetSecurityContactResponse.  # noqa: E501


        :return: The email of this GetSecurityContactResponse.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this GetSecurityContactResponse.


        :param email: The email of this GetSecurityContactResponse.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def email_is_verify(self):
        """Gets the email_is_verify of this GetSecurityContactResponse.  # noqa: E501


        :return: The email_is_verify of this GetSecurityContactResponse.  # noqa: E501
        :rtype: bool
        """
        return self._email_is_verify

    @email_is_verify.setter
    def email_is_verify(self, email_is_verify):
        """Sets the email_is_verify of this GetSecurityContactResponse.


        :param email_is_verify: The email_is_verify of this GetSecurityContactResponse.  # noqa: E501
        :type: bool
        """

        self._email_is_verify = email_is_verify

    @property
    def mobile_phone(self):
        """Gets the mobile_phone of this GetSecurityContactResponse.  # noqa: E501


        :return: The mobile_phone of this GetSecurityContactResponse.  # noqa: E501
        :rtype: str
        """
        return self._mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, mobile_phone):
        """Sets the mobile_phone of this GetSecurityContactResponse.


        :param mobile_phone: The mobile_phone of this GetSecurityContactResponse.  # noqa: E501
        :type: str
        """

        self._mobile_phone = mobile_phone

    @property
    def mobile_phone_is_verify(self):
        """Gets the mobile_phone_is_verify of this GetSecurityContactResponse.  # noqa: E501


        :return: The mobile_phone_is_verify of this GetSecurityContactResponse.  # noqa: E501
        :rtype: bool
        """
        return self._mobile_phone_is_verify

    @mobile_phone_is_verify.setter
    def mobile_phone_is_verify(self, mobile_phone_is_verify):
        """Sets the mobile_phone_is_verify of this GetSecurityContactResponse.


        :param mobile_phone_is_verify: The mobile_phone_is_verify of this GetSecurityContactResponse.  # noqa: E501
        :type: bool
        """

        self._mobile_phone_is_verify = mobile_phone_is_verify

    @property
    def new_secure_contact_info(self):
        """Gets the new_secure_contact_info of this GetSecurityContactResponse.  # noqa: E501


        :return: The new_secure_contact_info of this GetSecurityContactResponse.  # noqa: E501
        :rtype: NewSecureContactInfoForGetSecurityContactOutput
        """
        return self._new_secure_contact_info

    @new_secure_contact_info.setter
    def new_secure_contact_info(self, new_secure_contact_info):
        """Sets the new_secure_contact_info of this GetSecurityContactResponse.


        :param new_secure_contact_info: The new_secure_contact_info of this GetSecurityContactResponse.  # noqa: E501
        :type: NewSecureContactInfoForGetSecurityContactOutput
        """

        self._new_secure_contact_info = new_secure_contact_info

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
        if issubclass(GetSecurityContactResponse, dict):
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
        if not isinstance(other, GetSecurityContactResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetSecurityContactResponse):
            return True

        return self.to_dict() != other.to_dict()
