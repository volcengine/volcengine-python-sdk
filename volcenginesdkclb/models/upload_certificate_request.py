# coding: utf-8

"""
    clb

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class UploadCertificateRequest(object):
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
        'certificate_name': 'str',
        'description': 'str',
        'private_key': 'str',
        'project_name': 'str',
        'public_key': 'str'
    }

    attribute_map = {
        'certificate_name': 'CertificateName',
        'description': 'Description',
        'private_key': 'PrivateKey',
        'project_name': 'ProjectName',
        'public_key': 'PublicKey'
    }

    def __init__(self, certificate_name=None, description=None, private_key=None, project_name=None, public_key=None, _configuration=None):  # noqa: E501
        """UploadCertificateRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._certificate_name = None
        self._description = None
        self._private_key = None
        self._project_name = None
        self._public_key = None
        self.discriminator = None

        if certificate_name is not None:
            self.certificate_name = certificate_name
        if description is not None:
            self.description = description
        self.private_key = private_key
        if project_name is not None:
            self.project_name = project_name
        self.public_key = public_key

    @property
    def certificate_name(self):
        """Gets the certificate_name of this UploadCertificateRequest.  # noqa: E501


        :return: The certificate_name of this UploadCertificateRequest.  # noqa: E501
        :rtype: str
        """
        return self._certificate_name

    @certificate_name.setter
    def certificate_name(self, certificate_name):
        """Sets the certificate_name of this UploadCertificateRequest.


        :param certificate_name: The certificate_name of this UploadCertificateRequest.  # noqa: E501
        :type: str
        """

        self._certificate_name = certificate_name

    @property
    def description(self):
        """Gets the description of this UploadCertificateRequest.  # noqa: E501


        :return: The description of this UploadCertificateRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UploadCertificateRequest.


        :param description: The description of this UploadCertificateRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def private_key(self):
        """Gets the private_key of this UploadCertificateRequest.  # noqa: E501


        :return: The private_key of this UploadCertificateRequest.  # noqa: E501
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this UploadCertificateRequest.


        :param private_key: The private_key of this UploadCertificateRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and private_key is None:
            raise ValueError("Invalid value for `private_key`, must not be `None`")  # noqa: E501

        self._private_key = private_key

    @property
    def project_name(self):
        """Gets the project_name of this UploadCertificateRequest.  # noqa: E501


        :return: The project_name of this UploadCertificateRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this UploadCertificateRequest.


        :param project_name: The project_name of this UploadCertificateRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def public_key(self):
        """Gets the public_key of this UploadCertificateRequest.  # noqa: E501


        :return: The public_key of this UploadCertificateRequest.  # noqa: E501
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this UploadCertificateRequest.


        :param public_key: The public_key of this UploadCertificateRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and public_key is None:
            raise ValueError("Invalid value for `public_key`, must not be `None`")  # noqa: E501

        self._public_key = public_key

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
        if issubclass(UploadCertificateRequest, dict):
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
        if not isinstance(other, UploadCertificateRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UploadCertificateRequest):
            return True

        return self.to_dict() != other.to_dict()
