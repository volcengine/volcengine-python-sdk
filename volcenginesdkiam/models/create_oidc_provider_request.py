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


class CreateOIDCProviderRequest(object):
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
        'client_ids': 'list[str]',
        'description': 'str',
        'issuance_limit_time': 'int',
        'issuer_url': 'str',
        'oidc_provider_name': 'str',
        'thumbprints': 'list[str]'
    }

    attribute_map = {
        'client_ids': 'ClientIDs',
        'description': 'Description',
        'issuance_limit_time': 'IssuanceLimitTime',
        'issuer_url': 'IssuerURL',
        'oidc_provider_name': 'OIDCProviderName',
        'thumbprints': 'Thumbprints'
    }

    def __init__(self, client_ids=None, description=None, issuance_limit_time=None, issuer_url=None, oidc_provider_name=None, thumbprints=None, _configuration=None):  # noqa: E501
        """CreateOIDCProviderRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._client_ids = None
        self._description = None
        self._issuance_limit_time = None
        self._issuer_url = None
        self._oidc_provider_name = None
        self._thumbprints = None
        self.discriminator = None

        if client_ids is not None:
            self.client_ids = client_ids
        if description is not None:
            self.description = description
        if issuance_limit_time is not None:
            self.issuance_limit_time = issuance_limit_time
        self.issuer_url = issuer_url
        self.oidc_provider_name = oidc_provider_name
        if thumbprints is not None:
            self.thumbprints = thumbprints

    @property
    def client_ids(self):
        """Gets the client_ids of this CreateOIDCProviderRequest.  # noqa: E501


        :return: The client_ids of this CreateOIDCProviderRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._client_ids

    @client_ids.setter
    def client_ids(self, client_ids):
        """Sets the client_ids of this CreateOIDCProviderRequest.


        :param client_ids: The client_ids of this CreateOIDCProviderRequest.  # noqa: E501
        :type: list[str]
        """

        self._client_ids = client_ids

    @property
    def description(self):
        """Gets the description of this CreateOIDCProviderRequest.  # noqa: E501


        :return: The description of this CreateOIDCProviderRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateOIDCProviderRequest.


        :param description: The description of this CreateOIDCProviderRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def issuance_limit_time(self):
        """Gets the issuance_limit_time of this CreateOIDCProviderRequest.  # noqa: E501


        :return: The issuance_limit_time of this CreateOIDCProviderRequest.  # noqa: E501
        :rtype: int
        """
        return self._issuance_limit_time

    @issuance_limit_time.setter
    def issuance_limit_time(self, issuance_limit_time):
        """Sets the issuance_limit_time of this CreateOIDCProviderRequest.


        :param issuance_limit_time: The issuance_limit_time of this CreateOIDCProviderRequest.  # noqa: E501
        :type: int
        """

        self._issuance_limit_time = issuance_limit_time

    @property
    def issuer_url(self):
        """Gets the issuer_url of this CreateOIDCProviderRequest.  # noqa: E501


        :return: The issuer_url of this CreateOIDCProviderRequest.  # noqa: E501
        :rtype: str
        """
        return self._issuer_url

    @issuer_url.setter
    def issuer_url(self, issuer_url):
        """Sets the issuer_url of this CreateOIDCProviderRequest.


        :param issuer_url: The issuer_url of this CreateOIDCProviderRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and issuer_url is None:
            raise ValueError("Invalid value for `issuer_url`, must not be `None`")  # noqa: E501

        self._issuer_url = issuer_url

    @property
    def oidc_provider_name(self):
        """Gets the oidc_provider_name of this CreateOIDCProviderRequest.  # noqa: E501


        :return: The oidc_provider_name of this CreateOIDCProviderRequest.  # noqa: E501
        :rtype: str
        """
        return self._oidc_provider_name

    @oidc_provider_name.setter
    def oidc_provider_name(self, oidc_provider_name):
        """Sets the oidc_provider_name of this CreateOIDCProviderRequest.


        :param oidc_provider_name: The oidc_provider_name of this CreateOIDCProviderRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and oidc_provider_name is None:
            raise ValueError("Invalid value for `oidc_provider_name`, must not be `None`")  # noqa: E501

        self._oidc_provider_name = oidc_provider_name

    @property
    def thumbprints(self):
        """Gets the thumbprints of this CreateOIDCProviderRequest.  # noqa: E501


        :return: The thumbprints of this CreateOIDCProviderRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._thumbprints

    @thumbprints.setter
    def thumbprints(self, thumbprints):
        """Sets the thumbprints of this CreateOIDCProviderRequest.


        :param thumbprints: The thumbprints of this CreateOIDCProviderRequest.  # noqa: E501
        :type: list[str]
        """

        self._thumbprints = thumbprints

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
        if issubclass(CreateOIDCProviderRequest, dict):
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
        if not isinstance(other, CreateOIDCProviderRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateOIDCProviderRequest):
            return True

        return self.to_dict() != other.to_dict()
