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


class SecurityPolicyForDescribeNLBSystemSecurityPoliciesOutput(object):
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
        'security_policy_id': 'str',
        'security_policy_name': 'str',
        'tls_versions': 'list[str]'
    }

    attribute_map = {
        'ciphers': 'Ciphers',
        'security_policy_id': 'SecurityPolicyId',
        'security_policy_name': 'SecurityPolicyName',
        'tls_versions': 'TlsVersions'
    }

    def __init__(self, ciphers=None, security_policy_id=None, security_policy_name=None, tls_versions=None, _configuration=None):  # noqa: E501
        """SecurityPolicyForDescribeNLBSystemSecurityPoliciesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._ciphers = None
        self._security_policy_id = None
        self._security_policy_name = None
        self._tls_versions = None
        self.discriminator = None

        if ciphers is not None:
            self.ciphers = ciphers
        if security_policy_id is not None:
            self.security_policy_id = security_policy_id
        if security_policy_name is not None:
            self.security_policy_name = security_policy_name
        if tls_versions is not None:
            self.tls_versions = tls_versions

    @property
    def ciphers(self):
        """Gets the ciphers of this SecurityPolicyForDescribeNLBSystemSecurityPoliciesOutput.  # noqa: E501


        :return: The ciphers of this SecurityPolicyForDescribeNLBSystemSecurityPoliciesOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._ciphers

    @ciphers.setter
    def ciphers(self, ciphers):
        """Sets the ciphers of this SecurityPolicyForDescribeNLBSystemSecurityPoliciesOutput.


        :param ciphers: The ciphers of this SecurityPolicyForDescribeNLBSystemSecurityPoliciesOutput.  # noqa: E501
        :type: list[str]
        """

        self._ciphers = ciphers

    @property
    def security_policy_id(self):
        """Gets the security_policy_id of this SecurityPolicyForDescribeNLBSystemSecurityPoliciesOutput.  # noqa: E501


        :return: The security_policy_id of this SecurityPolicyForDescribeNLBSystemSecurityPoliciesOutput.  # noqa: E501
        :rtype: str
        """
        return self._security_policy_id

    @security_policy_id.setter
    def security_policy_id(self, security_policy_id):
        """Sets the security_policy_id of this SecurityPolicyForDescribeNLBSystemSecurityPoliciesOutput.


        :param security_policy_id: The security_policy_id of this SecurityPolicyForDescribeNLBSystemSecurityPoliciesOutput.  # noqa: E501
        :type: str
        """

        self._security_policy_id = security_policy_id

    @property
    def security_policy_name(self):
        """Gets the security_policy_name of this SecurityPolicyForDescribeNLBSystemSecurityPoliciesOutput.  # noqa: E501


        :return: The security_policy_name of this SecurityPolicyForDescribeNLBSystemSecurityPoliciesOutput.  # noqa: E501
        :rtype: str
        """
        return self._security_policy_name

    @security_policy_name.setter
    def security_policy_name(self, security_policy_name):
        """Sets the security_policy_name of this SecurityPolicyForDescribeNLBSystemSecurityPoliciesOutput.


        :param security_policy_name: The security_policy_name of this SecurityPolicyForDescribeNLBSystemSecurityPoliciesOutput.  # noqa: E501
        :type: str
        """

        self._security_policy_name = security_policy_name

    @property
    def tls_versions(self):
        """Gets the tls_versions of this SecurityPolicyForDescribeNLBSystemSecurityPoliciesOutput.  # noqa: E501


        :return: The tls_versions of this SecurityPolicyForDescribeNLBSystemSecurityPoliciesOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._tls_versions

    @tls_versions.setter
    def tls_versions(self, tls_versions):
        """Sets the tls_versions of this SecurityPolicyForDescribeNLBSystemSecurityPoliciesOutput.


        :param tls_versions: The tls_versions of this SecurityPolicyForDescribeNLBSystemSecurityPoliciesOutput.  # noqa: E501
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
        if issubclass(SecurityPolicyForDescribeNLBSystemSecurityPoliciesOutput, dict):
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
        if not isinstance(other, SecurityPolicyForDescribeNLBSystemSecurityPoliciesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SecurityPolicyForDescribeNLBSystemSecurityPoliciesOutput):
            return True

        return self.to_dict() != other.to_dict()
