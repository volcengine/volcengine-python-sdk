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


class AddSAMLProviderCertificateRequest(object):
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
        'saml_provider_name': 'str',
        'x509_certificate': 'str'
    }

    attribute_map = {
        'saml_provider_name': 'SAMLProviderName',
        'x509_certificate': 'X509Certificate'
    }

    def __init__(self, saml_provider_name=None, x509_certificate=None, _configuration=None):  # noqa: E501
        """AddSAMLProviderCertificateRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._saml_provider_name = None
        self._x509_certificate = None
        self.discriminator = None

        self.saml_provider_name = saml_provider_name
        self.x509_certificate = x509_certificate

    @property
    def saml_provider_name(self):
        """Gets the saml_provider_name of this AddSAMLProviderCertificateRequest.  # noqa: E501


        :return: The saml_provider_name of this AddSAMLProviderCertificateRequest.  # noqa: E501
        :rtype: str
        """
        return self._saml_provider_name

    @saml_provider_name.setter
    def saml_provider_name(self, saml_provider_name):
        """Sets the saml_provider_name of this AddSAMLProviderCertificateRequest.


        :param saml_provider_name: The saml_provider_name of this AddSAMLProviderCertificateRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and saml_provider_name is None:
            raise ValueError("Invalid value for `saml_provider_name`, must not be `None`")  # noqa: E501

        self._saml_provider_name = saml_provider_name

    @property
    def x509_certificate(self):
        """Gets the x509_certificate of this AddSAMLProviderCertificateRequest.  # noqa: E501


        :return: The x509_certificate of this AddSAMLProviderCertificateRequest.  # noqa: E501
        :rtype: str
        """
        return self._x509_certificate

    @x509_certificate.setter
    def x509_certificate(self, x509_certificate):
        """Sets the x509_certificate of this AddSAMLProviderCertificateRequest.


        :param x509_certificate: The x509_certificate of this AddSAMLProviderCertificateRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and x509_certificate is None:
            raise ValueError("Invalid value for `x509_certificate`, must not be `None`")  # noqa: E501

        self._x509_certificate = x509_certificate

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
        if issubclass(AddSAMLProviderCertificateRequest, dict):
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
        if not isinstance(other, AddSAMLProviderCertificateRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddSAMLProviderCertificateRequest):
            return True

        return self.to_dict() != other.to_dict()