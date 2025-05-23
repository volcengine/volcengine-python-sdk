# coding: utf-8

"""
    pca

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DownloadLeafInstanceResponse(object):
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
        'certificate': 'str',
        'certificate_chain': 'str',
        'encrypt_certificate': 'str',
        'encrypt_private_key': 'str',
        'private_key': 'str',
        'tarball_bytes': 'str'
    }

    attribute_map = {
        'certificate': 'certificate',
        'certificate_chain': 'certificate_chain',
        'encrypt_certificate': 'encrypt_certificate',
        'encrypt_private_key': 'encrypt_private_key',
        'private_key': 'private_key',
        'tarball_bytes': 'tarball_bytes'
    }

    def __init__(self, certificate=None, certificate_chain=None, encrypt_certificate=None, encrypt_private_key=None, private_key=None, tarball_bytes=None, _configuration=None):  # noqa: E501
        """DownloadLeafInstanceResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._certificate = None
        self._certificate_chain = None
        self._encrypt_certificate = None
        self._encrypt_private_key = None
        self._private_key = None
        self._tarball_bytes = None
        self.discriminator = None

        if certificate is not None:
            self.certificate = certificate
        if certificate_chain is not None:
            self.certificate_chain = certificate_chain
        if encrypt_certificate is not None:
            self.encrypt_certificate = encrypt_certificate
        if encrypt_private_key is not None:
            self.encrypt_private_key = encrypt_private_key
        if private_key is not None:
            self.private_key = private_key
        if tarball_bytes is not None:
            self.tarball_bytes = tarball_bytes

    @property
    def certificate(self):
        """Gets the certificate of this DownloadLeafInstanceResponse.  # noqa: E501


        :return: The certificate of this DownloadLeafInstanceResponse.  # noqa: E501
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this DownloadLeafInstanceResponse.


        :param certificate: The certificate of this DownloadLeafInstanceResponse.  # noqa: E501
        :type: str
        """

        self._certificate = certificate

    @property
    def certificate_chain(self):
        """Gets the certificate_chain of this DownloadLeafInstanceResponse.  # noqa: E501


        :return: The certificate_chain of this DownloadLeafInstanceResponse.  # noqa: E501
        :rtype: str
        """
        return self._certificate_chain

    @certificate_chain.setter
    def certificate_chain(self, certificate_chain):
        """Sets the certificate_chain of this DownloadLeafInstanceResponse.


        :param certificate_chain: The certificate_chain of this DownloadLeafInstanceResponse.  # noqa: E501
        :type: str
        """

        self._certificate_chain = certificate_chain

    @property
    def encrypt_certificate(self):
        """Gets the encrypt_certificate of this DownloadLeafInstanceResponse.  # noqa: E501


        :return: The encrypt_certificate of this DownloadLeafInstanceResponse.  # noqa: E501
        :rtype: str
        """
        return self._encrypt_certificate

    @encrypt_certificate.setter
    def encrypt_certificate(self, encrypt_certificate):
        """Sets the encrypt_certificate of this DownloadLeafInstanceResponse.


        :param encrypt_certificate: The encrypt_certificate of this DownloadLeafInstanceResponse.  # noqa: E501
        :type: str
        """

        self._encrypt_certificate = encrypt_certificate

    @property
    def encrypt_private_key(self):
        """Gets the encrypt_private_key of this DownloadLeafInstanceResponse.  # noqa: E501


        :return: The encrypt_private_key of this DownloadLeafInstanceResponse.  # noqa: E501
        :rtype: str
        """
        return self._encrypt_private_key

    @encrypt_private_key.setter
    def encrypt_private_key(self, encrypt_private_key):
        """Sets the encrypt_private_key of this DownloadLeafInstanceResponse.


        :param encrypt_private_key: The encrypt_private_key of this DownloadLeafInstanceResponse.  # noqa: E501
        :type: str
        """

        self._encrypt_private_key = encrypt_private_key

    @property
    def private_key(self):
        """Gets the private_key of this DownloadLeafInstanceResponse.  # noqa: E501


        :return: The private_key of this DownloadLeafInstanceResponse.  # noqa: E501
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this DownloadLeafInstanceResponse.


        :param private_key: The private_key of this DownloadLeafInstanceResponse.  # noqa: E501
        :type: str
        """

        self._private_key = private_key

    @property
    def tarball_bytes(self):
        """Gets the tarball_bytes of this DownloadLeafInstanceResponse.  # noqa: E501


        :return: The tarball_bytes of this DownloadLeafInstanceResponse.  # noqa: E501
        :rtype: str
        """
        return self._tarball_bytes

    @tarball_bytes.setter
    def tarball_bytes(self, tarball_bytes):
        """Sets the tarball_bytes of this DownloadLeafInstanceResponse.


        :param tarball_bytes: The tarball_bytes of this DownloadLeafInstanceResponse.  # noqa: E501
        :type: str
        """

        self._tarball_bytes = tarball_bytes

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
        if issubclass(DownloadLeafInstanceResponse, dict):
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
        if not isinstance(other, DownloadLeafInstanceResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DownloadLeafInstanceResponse):
            return True

        return self.to_dict() != other.to_dict()
