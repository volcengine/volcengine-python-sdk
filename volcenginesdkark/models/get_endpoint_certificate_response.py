# coding: utf-8

"""
    ark

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class GetEndpointCertificateResponse(object):
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
        'not_after': 'int',
        'not_before': 'int',
        'pca_host': 'str',
        'pca_instance_certificate': 'str',
        'pca_name': 'str',
        'pca_root_ca_certificate': 'str',
        'pca_sub_ca_certificate': 'str'
    }

    attribute_map = {
        'not_after': 'NotAfter',
        'not_before': 'NotBefore',
        'pca_host': 'PCAHost',
        'pca_instance_certificate': 'PCAInstanceCertificate',
        'pca_name': 'PCAName',
        'pca_root_ca_certificate': 'PCARootCACertificate',
        'pca_sub_ca_certificate': 'PCASubCACertificate'
    }

    def __init__(self, not_after=None, not_before=None, pca_host=None, pca_instance_certificate=None, pca_name=None, pca_root_ca_certificate=None, pca_sub_ca_certificate=None, _configuration=None):  # noqa: E501
        """GetEndpointCertificateResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._not_after = None
        self._not_before = None
        self._pca_host = None
        self._pca_instance_certificate = None
        self._pca_name = None
        self._pca_root_ca_certificate = None
        self._pca_sub_ca_certificate = None
        self.discriminator = None

        if not_after is not None:
            self.not_after = not_after
        if not_before is not None:
            self.not_before = not_before
        if pca_host is not None:
            self.pca_host = pca_host
        if pca_instance_certificate is not None:
            self.pca_instance_certificate = pca_instance_certificate
        if pca_name is not None:
            self.pca_name = pca_name
        if pca_root_ca_certificate is not None:
            self.pca_root_ca_certificate = pca_root_ca_certificate
        if pca_sub_ca_certificate is not None:
            self.pca_sub_ca_certificate = pca_sub_ca_certificate

    @property
    def not_after(self):
        """Gets the not_after of this GetEndpointCertificateResponse.  # noqa: E501


        :return: The not_after of this GetEndpointCertificateResponse.  # noqa: E501
        :rtype: int
        """
        return self._not_after

    @not_after.setter
    def not_after(self, not_after):
        """Sets the not_after of this GetEndpointCertificateResponse.


        :param not_after: The not_after of this GetEndpointCertificateResponse.  # noqa: E501
        :type: int
        """

        self._not_after = not_after

    @property
    def not_before(self):
        """Gets the not_before of this GetEndpointCertificateResponse.  # noqa: E501


        :return: The not_before of this GetEndpointCertificateResponse.  # noqa: E501
        :rtype: int
        """
        return self._not_before

    @not_before.setter
    def not_before(self, not_before):
        """Sets the not_before of this GetEndpointCertificateResponse.


        :param not_before: The not_before of this GetEndpointCertificateResponse.  # noqa: E501
        :type: int
        """

        self._not_before = not_before

    @property
    def pca_host(self):
        """Gets the pca_host of this GetEndpointCertificateResponse.  # noqa: E501


        :return: The pca_host of this GetEndpointCertificateResponse.  # noqa: E501
        :rtype: str
        """
        return self._pca_host

    @pca_host.setter
    def pca_host(self, pca_host):
        """Sets the pca_host of this GetEndpointCertificateResponse.


        :param pca_host: The pca_host of this GetEndpointCertificateResponse.  # noqa: E501
        :type: str
        """

        self._pca_host = pca_host

    @property
    def pca_instance_certificate(self):
        """Gets the pca_instance_certificate of this GetEndpointCertificateResponse.  # noqa: E501


        :return: The pca_instance_certificate of this GetEndpointCertificateResponse.  # noqa: E501
        :rtype: str
        """
        return self._pca_instance_certificate

    @pca_instance_certificate.setter
    def pca_instance_certificate(self, pca_instance_certificate):
        """Sets the pca_instance_certificate of this GetEndpointCertificateResponse.


        :param pca_instance_certificate: The pca_instance_certificate of this GetEndpointCertificateResponse.  # noqa: E501
        :type: str
        """

        self._pca_instance_certificate = pca_instance_certificate

    @property
    def pca_name(self):
        """Gets the pca_name of this GetEndpointCertificateResponse.  # noqa: E501


        :return: The pca_name of this GetEndpointCertificateResponse.  # noqa: E501
        :rtype: str
        """
        return self._pca_name

    @pca_name.setter
    def pca_name(self, pca_name):
        """Sets the pca_name of this GetEndpointCertificateResponse.


        :param pca_name: The pca_name of this GetEndpointCertificateResponse.  # noqa: E501
        :type: str
        """

        self._pca_name = pca_name

    @property
    def pca_root_ca_certificate(self):
        """Gets the pca_root_ca_certificate of this GetEndpointCertificateResponse.  # noqa: E501


        :return: The pca_root_ca_certificate of this GetEndpointCertificateResponse.  # noqa: E501
        :rtype: str
        """
        return self._pca_root_ca_certificate

    @pca_root_ca_certificate.setter
    def pca_root_ca_certificate(self, pca_root_ca_certificate):
        """Sets the pca_root_ca_certificate of this GetEndpointCertificateResponse.


        :param pca_root_ca_certificate: The pca_root_ca_certificate of this GetEndpointCertificateResponse.  # noqa: E501
        :type: str
        """

        self._pca_root_ca_certificate = pca_root_ca_certificate

    @property
    def pca_sub_ca_certificate(self):
        """Gets the pca_sub_ca_certificate of this GetEndpointCertificateResponse.  # noqa: E501


        :return: The pca_sub_ca_certificate of this GetEndpointCertificateResponse.  # noqa: E501
        :rtype: str
        """
        return self._pca_sub_ca_certificate

    @pca_sub_ca_certificate.setter
    def pca_sub_ca_certificate(self, pca_sub_ca_certificate):
        """Sets the pca_sub_ca_certificate of this GetEndpointCertificateResponse.


        :param pca_sub_ca_certificate: The pca_sub_ca_certificate of this GetEndpointCertificateResponse.  # noqa: E501
        :type: str
        """

        self._pca_sub_ca_certificate = pca_sub_ca_certificate

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
        if issubclass(GetEndpointCertificateResponse, dict):
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
        if not isinstance(other, GetEndpointCertificateResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetEndpointCertificateResponse):
            return True

        return self.to_dict() != other.to_dict()
