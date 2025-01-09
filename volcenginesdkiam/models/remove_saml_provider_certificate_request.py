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


class RemoveSAMLProviderCertificateRequest(object):
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
        'certificate_id': 'str'
    }

    attribute_map = {
        'certificate_id': 'CertificateId'
    }

    def __init__(self, certificate_id=None, _configuration=None):  # noqa: E501
        """RemoveSAMLProviderCertificateRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._certificate_id = None
        self.discriminator = None

        self.certificate_id = certificate_id

    @property
    def certificate_id(self):
        """Gets the certificate_id of this RemoveSAMLProviderCertificateRequest.  # noqa: E501


        :return: The certificate_id of this RemoveSAMLProviderCertificateRequest.  # noqa: E501
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        """Sets the certificate_id of this RemoveSAMLProviderCertificateRequest.


        :param certificate_id: The certificate_id of this RemoveSAMLProviderCertificateRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and certificate_id is None:
            raise ValueError("Invalid value for `certificate_id`, must not be `None`")  # noqa: E501

        self._certificate_id = certificate_id

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
        if issubclass(RemoveSAMLProviderCertificateRequest, dict):
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
        if not isinstance(other, RemoveSAMLProviderCertificateRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RemoveSAMLProviderCertificateRequest):
            return True

        return self.to_dict() != other.to_dict()
