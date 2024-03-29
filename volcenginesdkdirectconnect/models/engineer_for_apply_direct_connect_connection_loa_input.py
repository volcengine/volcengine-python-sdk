# coding: utf-8

"""
    directconnect

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class EngineerForApplyDirectConnectConnectionLoaInput(object):
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
        'certificate_no': 'str',
        'certificate_type': 'str',
        'contact_phone': 'str',
        'name': 'str'
    }

    attribute_map = {
        'certificate_no': 'CertificateNo',
        'certificate_type': 'CertificateType',
        'contact_phone': 'ContactPhone',
        'name': 'Name'
    }

    def __init__(self, certificate_no=None, certificate_type=None, contact_phone=None, name=None, _configuration=None):  # noqa: E501
        """EngineerForApplyDirectConnectConnectionLoaInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._certificate_no = None
        self._certificate_type = None
        self._contact_phone = None
        self._name = None
        self.discriminator = None

        self.certificate_no = certificate_no
        self.certificate_type = certificate_type
        self.contact_phone = contact_phone
        self.name = name

    @property
    def certificate_no(self):
        """Gets the certificate_no of this EngineerForApplyDirectConnectConnectionLoaInput.  # noqa: E501


        :return: The certificate_no of this EngineerForApplyDirectConnectConnectionLoaInput.  # noqa: E501
        :rtype: str
        """
        return self._certificate_no

    @certificate_no.setter
    def certificate_no(self, certificate_no):
        """Sets the certificate_no of this EngineerForApplyDirectConnectConnectionLoaInput.


        :param certificate_no: The certificate_no of this EngineerForApplyDirectConnectConnectionLoaInput.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and certificate_no is None:
            raise ValueError("Invalid value for `certificate_no`, must not be `None`")  # noqa: E501

        self._certificate_no = certificate_no

    @property
    def certificate_type(self):
        """Gets the certificate_type of this EngineerForApplyDirectConnectConnectionLoaInput.  # noqa: E501


        :return: The certificate_type of this EngineerForApplyDirectConnectConnectionLoaInput.  # noqa: E501
        :rtype: str
        """
        return self._certificate_type

    @certificate_type.setter
    def certificate_type(self, certificate_type):
        """Sets the certificate_type of this EngineerForApplyDirectConnectConnectionLoaInput.


        :param certificate_type: The certificate_type of this EngineerForApplyDirectConnectConnectionLoaInput.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and certificate_type is None:
            raise ValueError("Invalid value for `certificate_type`, must not be `None`")  # noqa: E501

        self._certificate_type = certificate_type

    @property
    def contact_phone(self):
        """Gets the contact_phone of this EngineerForApplyDirectConnectConnectionLoaInput.  # noqa: E501


        :return: The contact_phone of this EngineerForApplyDirectConnectConnectionLoaInput.  # noqa: E501
        :rtype: str
        """
        return self._contact_phone

    @contact_phone.setter
    def contact_phone(self, contact_phone):
        """Sets the contact_phone of this EngineerForApplyDirectConnectConnectionLoaInput.


        :param contact_phone: The contact_phone of this EngineerForApplyDirectConnectConnectionLoaInput.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and contact_phone is None:
            raise ValueError("Invalid value for `contact_phone`, must not be `None`")  # noqa: E501

        self._contact_phone = contact_phone

    @property
    def name(self):
        """Gets the name of this EngineerForApplyDirectConnectConnectionLoaInput.  # noqa: E501


        :return: The name of this EngineerForApplyDirectConnectConnectionLoaInput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EngineerForApplyDirectConnectConnectionLoaInput.


        :param name: The name of this EngineerForApplyDirectConnectConnectionLoaInput.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if issubclass(EngineerForApplyDirectConnectConnectionLoaInput, dict):
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
        if not isinstance(other, EngineerForApplyDirectConnectConnectionLoaInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EngineerForApplyDirectConnectConnectionLoaInput):
            return True

        return self.to_dict() != other.to_dict()
