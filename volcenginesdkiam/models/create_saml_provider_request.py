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


class CreateSAMLProviderRequest(object):
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
        'description': 'str',
        'encoded_saml_metadata_document': 'str',
        'saml_provider_name': 'str',
        'sso_type': 'int',
        'status': 'int'
    }

    attribute_map = {
        'description': 'Description',
        'encoded_saml_metadata_document': 'EncodedSAMLMetadataDocument',
        'saml_provider_name': 'SAMLProviderName',
        'sso_type': 'SSOType',
        'status': 'Status'
    }

    def __init__(self, description=None, encoded_saml_metadata_document=None, saml_provider_name=None, sso_type=None, status=None, _configuration=None):  # noqa: E501
        """CreateSAMLProviderRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._description = None
        self._encoded_saml_metadata_document = None
        self._saml_provider_name = None
        self._sso_type = None
        self._status = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.encoded_saml_metadata_document = encoded_saml_metadata_document
        self.saml_provider_name = saml_provider_name
        self.sso_type = sso_type
        if status is not None:
            self.status = status

    @property
    def description(self):
        """Gets the description of this CreateSAMLProviderRequest.  # noqa: E501


        :return: The description of this CreateSAMLProviderRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateSAMLProviderRequest.


        :param description: The description of this CreateSAMLProviderRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                description is not None and len(description) > 256):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `256`")  # noqa: E501

        self._description = description

    @property
    def encoded_saml_metadata_document(self):
        """Gets the encoded_saml_metadata_document of this CreateSAMLProviderRequest.  # noqa: E501


        :return: The encoded_saml_metadata_document of this CreateSAMLProviderRequest.  # noqa: E501
        :rtype: str
        """
        return self._encoded_saml_metadata_document

    @encoded_saml_metadata_document.setter
    def encoded_saml_metadata_document(self, encoded_saml_metadata_document):
        """Sets the encoded_saml_metadata_document of this CreateSAMLProviderRequest.


        :param encoded_saml_metadata_document: The encoded_saml_metadata_document of this CreateSAMLProviderRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and encoded_saml_metadata_document is None:
            raise ValueError("Invalid value for `encoded_saml_metadata_document`, must not be `None`")  # noqa: E501

        self._encoded_saml_metadata_document = encoded_saml_metadata_document

    @property
    def saml_provider_name(self):
        """Gets the saml_provider_name of this CreateSAMLProviderRequest.  # noqa: E501


        :return: The saml_provider_name of this CreateSAMLProviderRequest.  # noqa: E501
        :rtype: str
        """
        return self._saml_provider_name

    @saml_provider_name.setter
    def saml_provider_name(self, saml_provider_name):
        """Sets the saml_provider_name of this CreateSAMLProviderRequest.


        :param saml_provider_name: The saml_provider_name of this CreateSAMLProviderRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and saml_provider_name is None:
            raise ValueError("Invalid value for `saml_provider_name`, must not be `None`")  # noqa: E501

        self._saml_provider_name = saml_provider_name

    @property
    def sso_type(self):
        """Gets the sso_type of this CreateSAMLProviderRequest.  # noqa: E501


        :return: The sso_type of this CreateSAMLProviderRequest.  # noqa: E501
        :rtype: int
        """
        return self._sso_type

    @sso_type.setter
    def sso_type(self, sso_type):
        """Sets the sso_type of this CreateSAMLProviderRequest.


        :param sso_type: The sso_type of this CreateSAMLProviderRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and sso_type is None:
            raise ValueError("Invalid value for `sso_type`, must not be `None`")  # noqa: E501

        self._sso_type = sso_type

    @property
    def status(self):
        """Gets the status of this CreateSAMLProviderRequest.  # noqa: E501


        :return: The status of this CreateSAMLProviderRequest.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateSAMLProviderRequest.


        :param status: The status of this CreateSAMLProviderRequest.  # noqa: E501
        :type: int
        """

        self._status = status

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
        if issubclass(CreateSAMLProviderRequest, dict):
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
        if not isinstance(other, CreateSAMLProviderRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateSAMLProviderRequest):
            return True

        return self.to_dict() != other.to_dict()
