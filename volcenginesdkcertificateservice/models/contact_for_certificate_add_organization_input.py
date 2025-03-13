# coding: utf-8

"""
    certificate_service

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ContactForCertificateAddOrganizationInput(object):
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
        'first_name': 'str',
        'id_card_no': 'str',
        'last_name': 'str',
        'phone': 'str'
    }

    attribute_map = {
        'email': 'Email',
        'first_name': 'FirstName',
        'id_card_no': 'IdCardNo',
        'last_name': 'LastName',
        'phone': 'Phone'
    }

    def __init__(self, email=None, first_name=None, id_card_no=None, last_name=None, phone=None, _configuration=None):  # noqa: E501
        """ContactForCertificateAddOrganizationInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._email = None
        self._first_name = None
        self._id_card_no = None
        self._last_name = None
        self._phone = None
        self.discriminator = None

        if email is not None:
            self.email = email
        if first_name is not None:
            self.first_name = first_name
        if id_card_no is not None:
            self.id_card_no = id_card_no
        if last_name is not None:
            self.last_name = last_name
        if phone is not None:
            self.phone = phone

    @property
    def email(self):
        """Gets the email of this ContactForCertificateAddOrganizationInput.  # noqa: E501


        :return: The email of this ContactForCertificateAddOrganizationInput.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ContactForCertificateAddOrganizationInput.


        :param email: The email of this ContactForCertificateAddOrganizationInput.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def first_name(self):
        """Gets the first_name of this ContactForCertificateAddOrganizationInput.  # noqa: E501


        :return: The first_name of this ContactForCertificateAddOrganizationInput.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this ContactForCertificateAddOrganizationInput.


        :param first_name: The first_name of this ContactForCertificateAddOrganizationInput.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def id_card_no(self):
        """Gets the id_card_no of this ContactForCertificateAddOrganizationInput.  # noqa: E501


        :return: The id_card_no of this ContactForCertificateAddOrganizationInput.  # noqa: E501
        :rtype: str
        """
        return self._id_card_no

    @id_card_no.setter
    def id_card_no(self, id_card_no):
        """Sets the id_card_no of this ContactForCertificateAddOrganizationInput.


        :param id_card_no: The id_card_no of this ContactForCertificateAddOrganizationInput.  # noqa: E501
        :type: str
        """

        self._id_card_no = id_card_no

    @property
    def last_name(self):
        """Gets the last_name of this ContactForCertificateAddOrganizationInput.  # noqa: E501


        :return: The last_name of this ContactForCertificateAddOrganizationInput.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this ContactForCertificateAddOrganizationInput.


        :param last_name: The last_name of this ContactForCertificateAddOrganizationInput.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def phone(self):
        """Gets the phone of this ContactForCertificateAddOrganizationInput.  # noqa: E501


        :return: The phone of this ContactForCertificateAddOrganizationInput.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this ContactForCertificateAddOrganizationInput.


        :param phone: The phone of this ContactForCertificateAddOrganizationInput.  # noqa: E501
        :type: str
        """

        self._phone = phone

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
        if issubclass(ContactForCertificateAddOrganizationInput, dict):
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
        if not isinstance(other, ContactForCertificateAddOrganizationInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ContactForCertificateAddOrganizationInput):
            return True

        return self.to_dict() != other.to_dict()
