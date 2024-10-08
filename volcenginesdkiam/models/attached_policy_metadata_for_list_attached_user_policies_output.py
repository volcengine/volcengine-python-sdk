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


class AttachedPolicyMetadataForListAttachedUserPoliciesOutput(object):
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
        'attach_date': 'str',
        'description': 'str',
        'policy_name': 'str',
        'policy_scope': 'list[PolicyScopeForListAttachedUserPoliciesOutput]',
        'policy_trn': 'str',
        'policy_type': 'str'
    }

    attribute_map = {
        'attach_date': 'AttachDate',
        'description': 'Description',
        'policy_name': 'PolicyName',
        'policy_scope': 'PolicyScope',
        'policy_trn': 'PolicyTrn',
        'policy_type': 'PolicyType'
    }

    def __init__(self, attach_date=None, description=None, policy_name=None, policy_scope=None, policy_trn=None, policy_type=None, _configuration=None):  # noqa: E501
        """AttachedPolicyMetadataForListAttachedUserPoliciesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._attach_date = None
        self._description = None
        self._policy_name = None
        self._policy_scope = None
        self._policy_trn = None
        self._policy_type = None
        self.discriminator = None

        if attach_date is not None:
            self.attach_date = attach_date
        if description is not None:
            self.description = description
        if policy_name is not None:
            self.policy_name = policy_name
        if policy_scope is not None:
            self.policy_scope = policy_scope
        if policy_trn is not None:
            self.policy_trn = policy_trn
        if policy_type is not None:
            self.policy_type = policy_type

    @property
    def attach_date(self):
        """Gets the attach_date of this AttachedPolicyMetadataForListAttachedUserPoliciesOutput.  # noqa: E501


        :return: The attach_date of this AttachedPolicyMetadataForListAttachedUserPoliciesOutput.  # noqa: E501
        :rtype: str
        """
        return self._attach_date

    @attach_date.setter
    def attach_date(self, attach_date):
        """Sets the attach_date of this AttachedPolicyMetadataForListAttachedUserPoliciesOutput.


        :param attach_date: The attach_date of this AttachedPolicyMetadataForListAttachedUserPoliciesOutput.  # noqa: E501
        :type: str
        """

        self._attach_date = attach_date

    @property
    def description(self):
        """Gets the description of this AttachedPolicyMetadataForListAttachedUserPoliciesOutput.  # noqa: E501


        :return: The description of this AttachedPolicyMetadataForListAttachedUserPoliciesOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AttachedPolicyMetadataForListAttachedUserPoliciesOutput.


        :param description: The description of this AttachedPolicyMetadataForListAttachedUserPoliciesOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def policy_name(self):
        """Gets the policy_name of this AttachedPolicyMetadataForListAttachedUserPoliciesOutput.  # noqa: E501


        :return: The policy_name of this AttachedPolicyMetadataForListAttachedUserPoliciesOutput.  # noqa: E501
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        """Sets the policy_name of this AttachedPolicyMetadataForListAttachedUserPoliciesOutput.


        :param policy_name: The policy_name of this AttachedPolicyMetadataForListAttachedUserPoliciesOutput.  # noqa: E501
        :type: str
        """

        self._policy_name = policy_name

    @property
    def policy_scope(self):
        """Gets the policy_scope of this AttachedPolicyMetadataForListAttachedUserPoliciesOutput.  # noqa: E501


        :return: The policy_scope of this AttachedPolicyMetadataForListAttachedUserPoliciesOutput.  # noqa: E501
        :rtype: list[PolicyScopeForListAttachedUserPoliciesOutput]
        """
        return self._policy_scope

    @policy_scope.setter
    def policy_scope(self, policy_scope):
        """Sets the policy_scope of this AttachedPolicyMetadataForListAttachedUserPoliciesOutput.


        :param policy_scope: The policy_scope of this AttachedPolicyMetadataForListAttachedUserPoliciesOutput.  # noqa: E501
        :type: list[PolicyScopeForListAttachedUserPoliciesOutput]
        """

        self._policy_scope = policy_scope

    @property
    def policy_trn(self):
        """Gets the policy_trn of this AttachedPolicyMetadataForListAttachedUserPoliciesOutput.  # noqa: E501


        :return: The policy_trn of this AttachedPolicyMetadataForListAttachedUserPoliciesOutput.  # noqa: E501
        :rtype: str
        """
        return self._policy_trn

    @policy_trn.setter
    def policy_trn(self, policy_trn):
        """Sets the policy_trn of this AttachedPolicyMetadataForListAttachedUserPoliciesOutput.


        :param policy_trn: The policy_trn of this AttachedPolicyMetadataForListAttachedUserPoliciesOutput.  # noqa: E501
        :type: str
        """

        self._policy_trn = policy_trn

    @property
    def policy_type(self):
        """Gets the policy_type of this AttachedPolicyMetadataForListAttachedUserPoliciesOutput.  # noqa: E501


        :return: The policy_type of this AttachedPolicyMetadataForListAttachedUserPoliciesOutput.  # noqa: E501
        :rtype: str
        """
        return self._policy_type

    @policy_type.setter
    def policy_type(self, policy_type):
        """Sets the policy_type of this AttachedPolicyMetadataForListAttachedUserPoliciesOutput.


        :param policy_type: The policy_type of this AttachedPolicyMetadataForListAttachedUserPoliciesOutput.  # noqa: E501
        :type: str
        """

        self._policy_type = policy_type

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
        if issubclass(AttachedPolicyMetadataForListAttachedUserPoliciesOutput, dict):
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
        if not isinstance(other, AttachedPolicyMetadataForListAttachedUserPoliciesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AttachedPolicyMetadataForListAttachedUserPoliciesOutput):
            return True

        return self.to_dict() != other.to_dict()
