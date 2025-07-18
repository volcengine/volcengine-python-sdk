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


class CreateNLBSecurityPolicyRequest(object):
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
        'ciphers': 'list[str]',
        'client_token': 'str',
        'project_name': 'str',
        'security_policy_name': 'str',
        'tags': 'list[TagForCreateNLBSecurityPolicyInput]',
        'tls_versions': 'list[str]'
    }

    attribute_map = {
        'ciphers': 'Ciphers',
        'client_token': 'ClientToken',
        'project_name': 'ProjectName',
        'security_policy_name': 'SecurityPolicyName',
        'tags': 'Tags',
        'tls_versions': 'TlsVersions'
    }

    def __init__(self, ciphers=None, client_token=None, project_name=None, security_policy_name=None, tags=None, tls_versions=None, _configuration=None):  # noqa: E501
        """CreateNLBSecurityPolicyRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._ciphers = None
        self._client_token = None
        self._project_name = None
        self._security_policy_name = None
        self._tags = None
        self._tls_versions = None
        self.discriminator = None

        if ciphers is not None:
            self.ciphers = ciphers
        if client_token is not None:
            self.client_token = client_token
        if project_name is not None:
            self.project_name = project_name
        if security_policy_name is not None:
            self.security_policy_name = security_policy_name
        if tags is not None:
            self.tags = tags
        if tls_versions is not None:
            self.tls_versions = tls_versions

    @property
    def ciphers(self):
        """Gets the ciphers of this CreateNLBSecurityPolicyRequest.  # noqa: E501


        :return: The ciphers of this CreateNLBSecurityPolicyRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._ciphers

    @ciphers.setter
    def ciphers(self, ciphers):
        """Sets the ciphers of this CreateNLBSecurityPolicyRequest.


        :param ciphers: The ciphers of this CreateNLBSecurityPolicyRequest.  # noqa: E501
        :type: list[str]
        """

        self._ciphers = ciphers

    @property
    def client_token(self):
        """Gets the client_token of this CreateNLBSecurityPolicyRequest.  # noqa: E501


        :return: The client_token of this CreateNLBSecurityPolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_token

    @client_token.setter
    def client_token(self, client_token):
        """Sets the client_token of this CreateNLBSecurityPolicyRequest.


        :param client_token: The client_token of this CreateNLBSecurityPolicyRequest.  # noqa: E501
        :type: str
        """

        self._client_token = client_token

    @property
    def project_name(self):
        """Gets the project_name of this CreateNLBSecurityPolicyRequest.  # noqa: E501


        :return: The project_name of this CreateNLBSecurityPolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this CreateNLBSecurityPolicyRequest.


        :param project_name: The project_name of this CreateNLBSecurityPolicyRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def security_policy_name(self):
        """Gets the security_policy_name of this CreateNLBSecurityPolicyRequest.  # noqa: E501


        :return: The security_policy_name of this CreateNLBSecurityPolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._security_policy_name

    @security_policy_name.setter
    def security_policy_name(self, security_policy_name):
        """Sets the security_policy_name of this CreateNLBSecurityPolicyRequest.


        :param security_policy_name: The security_policy_name of this CreateNLBSecurityPolicyRequest.  # noqa: E501
        :type: str
        """

        self._security_policy_name = security_policy_name

    @property
    def tags(self):
        """Gets the tags of this CreateNLBSecurityPolicyRequest.  # noqa: E501


        :return: The tags of this CreateNLBSecurityPolicyRequest.  # noqa: E501
        :rtype: list[TagForCreateNLBSecurityPolicyInput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateNLBSecurityPolicyRequest.


        :param tags: The tags of this CreateNLBSecurityPolicyRequest.  # noqa: E501
        :type: list[TagForCreateNLBSecurityPolicyInput]
        """

        self._tags = tags

    @property
    def tls_versions(self):
        """Gets the tls_versions of this CreateNLBSecurityPolicyRequest.  # noqa: E501


        :return: The tls_versions of this CreateNLBSecurityPolicyRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._tls_versions

    @tls_versions.setter
    def tls_versions(self, tls_versions):
        """Sets the tls_versions of this CreateNLBSecurityPolicyRequest.


        :param tls_versions: The tls_versions of this CreateNLBSecurityPolicyRequest.  # noqa: E501
        :type: list[str]
        """

        self._tls_versions = tls_versions

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
        if issubclass(CreateNLBSecurityPolicyRequest, dict):
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
        if not isinstance(other, CreateNLBSecurityPolicyRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateNLBSecurityPolicyRequest):
            return True

        return self.to_dict() != other.to_dict()
