# coding: utf-8

"""
    alb

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DomainExtensionForDescribeListenerAttributesOutput(object):
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
        'cert_center_certificate_id': 'str',
        'certificate_id': 'str',
        'certificate_source': 'str',
        'domain': 'str',
        'domain_extension_id': 'str',
        'listener_id': 'str',
        'san': 'str'
    }

    attribute_map = {
        'cert_center_certificate_id': 'CertCenterCertificateId',
        'certificate_id': 'CertificateId',
        'certificate_source': 'CertificateSource',
        'domain': 'Domain',
        'domain_extension_id': 'DomainExtensionId',
        'listener_id': 'ListenerId',
        'san': 'San'
    }

    def __init__(self, cert_center_certificate_id=None, certificate_id=None, certificate_source=None, domain=None, domain_extension_id=None, listener_id=None, san=None, _configuration=None):  # noqa: E501
        """DomainExtensionForDescribeListenerAttributesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cert_center_certificate_id = None
        self._certificate_id = None
        self._certificate_source = None
        self._domain = None
        self._domain_extension_id = None
        self._listener_id = None
        self._san = None
        self.discriminator = None

        if cert_center_certificate_id is not None:
            self.cert_center_certificate_id = cert_center_certificate_id
        if certificate_id is not None:
            self.certificate_id = certificate_id
        if certificate_source is not None:
            self.certificate_source = certificate_source
        if domain is not None:
            self.domain = domain
        if domain_extension_id is not None:
            self.domain_extension_id = domain_extension_id
        if listener_id is not None:
            self.listener_id = listener_id
        if san is not None:
            self.san = san

    @property
    def cert_center_certificate_id(self):
        """Gets the cert_center_certificate_id of this DomainExtensionForDescribeListenerAttributesOutput.  # noqa: E501


        :return: The cert_center_certificate_id of this DomainExtensionForDescribeListenerAttributesOutput.  # noqa: E501
        :rtype: str
        """
        return self._cert_center_certificate_id

    @cert_center_certificate_id.setter
    def cert_center_certificate_id(self, cert_center_certificate_id):
        """Sets the cert_center_certificate_id of this DomainExtensionForDescribeListenerAttributesOutput.


        :param cert_center_certificate_id: The cert_center_certificate_id of this DomainExtensionForDescribeListenerAttributesOutput.  # noqa: E501
        :type: str
        """

        self._cert_center_certificate_id = cert_center_certificate_id

    @property
    def certificate_id(self):
        """Gets the certificate_id of this DomainExtensionForDescribeListenerAttributesOutput.  # noqa: E501


        :return: The certificate_id of this DomainExtensionForDescribeListenerAttributesOutput.  # noqa: E501
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        """Sets the certificate_id of this DomainExtensionForDescribeListenerAttributesOutput.


        :param certificate_id: The certificate_id of this DomainExtensionForDescribeListenerAttributesOutput.  # noqa: E501
        :type: str
        """

        self._certificate_id = certificate_id

    @property
    def certificate_source(self):
        """Gets the certificate_source of this DomainExtensionForDescribeListenerAttributesOutput.  # noqa: E501


        :return: The certificate_source of this DomainExtensionForDescribeListenerAttributesOutput.  # noqa: E501
        :rtype: str
        """
        return self._certificate_source

    @certificate_source.setter
    def certificate_source(self, certificate_source):
        """Sets the certificate_source of this DomainExtensionForDescribeListenerAttributesOutput.


        :param certificate_source: The certificate_source of this DomainExtensionForDescribeListenerAttributesOutput.  # noqa: E501
        :type: str
        """

        self._certificate_source = certificate_source

    @property
    def domain(self):
        """Gets the domain of this DomainExtensionForDescribeListenerAttributesOutput.  # noqa: E501


        :return: The domain of this DomainExtensionForDescribeListenerAttributesOutput.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this DomainExtensionForDescribeListenerAttributesOutput.


        :param domain: The domain of this DomainExtensionForDescribeListenerAttributesOutput.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def domain_extension_id(self):
        """Gets the domain_extension_id of this DomainExtensionForDescribeListenerAttributesOutput.  # noqa: E501


        :return: The domain_extension_id of this DomainExtensionForDescribeListenerAttributesOutput.  # noqa: E501
        :rtype: str
        """
        return self._domain_extension_id

    @domain_extension_id.setter
    def domain_extension_id(self, domain_extension_id):
        """Sets the domain_extension_id of this DomainExtensionForDescribeListenerAttributesOutput.


        :param domain_extension_id: The domain_extension_id of this DomainExtensionForDescribeListenerAttributesOutput.  # noqa: E501
        :type: str
        """

        self._domain_extension_id = domain_extension_id

    @property
    def listener_id(self):
        """Gets the listener_id of this DomainExtensionForDescribeListenerAttributesOutput.  # noqa: E501


        :return: The listener_id of this DomainExtensionForDescribeListenerAttributesOutput.  # noqa: E501
        :rtype: str
        """
        return self._listener_id

    @listener_id.setter
    def listener_id(self, listener_id):
        """Sets the listener_id of this DomainExtensionForDescribeListenerAttributesOutput.


        :param listener_id: The listener_id of this DomainExtensionForDescribeListenerAttributesOutput.  # noqa: E501
        :type: str
        """

        self._listener_id = listener_id

    @property
    def san(self):
        """Gets the san of this DomainExtensionForDescribeListenerAttributesOutput.  # noqa: E501


        :return: The san of this DomainExtensionForDescribeListenerAttributesOutput.  # noqa: E501
        :rtype: str
        """
        return self._san

    @san.setter
    def san(self, san):
        """Sets the san of this DomainExtensionForDescribeListenerAttributesOutput.


        :param san: The san of this DomainExtensionForDescribeListenerAttributesOutput.  # noqa: E501
        :type: str
        """

        self._san = san

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
        if issubclass(DomainExtensionForDescribeListenerAttributesOutput, dict):
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
        if not isinstance(other, DomainExtensionForDescribeListenerAttributesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DomainExtensionForDescribeListenerAttributesOutput):
            return True

        return self.to_dict() != other.to_dict()
