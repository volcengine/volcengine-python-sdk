# coding: utf-8

"""
    mcs

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ReferenceDataForGetRiskOutput(object):
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
        'strategy_db_ingress_minimum_acl': 'StrategyDBIngressMinimumACLForGetRiskOutput',
        'strategy_oss_bucket_limit_anonymous_acl': 'StrategyOSSBucketLimitAnonymousACLForGetRiskOutput',
        'strategy_oss_bucket_server_encrypt': 'StrategyOSSBucketServerEncryptForGetRiskOutput',
        'strategy_oss_bucket_version_bak_recovery': 'StrategyOSSBucketVersionBakRecoveryForGetRiskOutput',
        'strategy_slbacl_open': 'StrategySLBACLOpenForGetRiskOutput',
        'strategy_slb_minimum_forward_strategy': 'StrategySLBMinimumForwardStrategyForGetRiskOutput',
        'strategy_security_group_ingress_minimum_acl': 'StrategySecurityGroupIngressMinimumACLForGetRiskOutput',
        'strategy_vm_defend_burst_solution': 'StrategyVMDefendBurstSolutionForGetRiskOutput',
        'strategy_vm_identity_auth_ssh_key_pair': 'StrategyVMIdentityAuthSSHKeyPairForGetRiskOutput',
        'strategy_vm_security_group_rule_limit_port_access': 'StrategyVMSecurityGroupRuleLimitPortAccessForGetRiskOutput'
    }

    attribute_map = {
        'strategy_db_ingress_minimum_acl': 'StrategyDBIngressMinimumACL',
        'strategy_oss_bucket_limit_anonymous_acl': 'StrategyOSSBucketLimitAnonymousACL',
        'strategy_oss_bucket_server_encrypt': 'StrategyOSSBucketServerEncrypt',
        'strategy_oss_bucket_version_bak_recovery': 'StrategyOSSBucketVersionBakRecovery',
        'strategy_slbacl_open': 'StrategySLBACLOpen',
        'strategy_slb_minimum_forward_strategy': 'StrategySLBMinimumForwardStrategy',
        'strategy_security_group_ingress_minimum_acl': 'StrategySecurityGroupIngressMinimumACL',
        'strategy_vm_defend_burst_solution': 'StrategyVMDefendBurstSolution',
        'strategy_vm_identity_auth_ssh_key_pair': 'StrategyVMIdentityAuthSSHKeyPair',
        'strategy_vm_security_group_rule_limit_port_access': 'StrategyVMSecurityGroupRuleLimitPortAccess'
    }

    def __init__(self, strategy_db_ingress_minimum_acl=None, strategy_oss_bucket_limit_anonymous_acl=None, strategy_oss_bucket_server_encrypt=None, strategy_oss_bucket_version_bak_recovery=None, strategy_slbacl_open=None, strategy_slb_minimum_forward_strategy=None, strategy_security_group_ingress_minimum_acl=None, strategy_vm_defend_burst_solution=None, strategy_vm_identity_auth_ssh_key_pair=None, strategy_vm_security_group_rule_limit_port_access=None, _configuration=None):  # noqa: E501
        """ReferenceDataForGetRiskOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._strategy_db_ingress_minimum_acl = None
        self._strategy_oss_bucket_limit_anonymous_acl = None
        self._strategy_oss_bucket_server_encrypt = None
        self._strategy_oss_bucket_version_bak_recovery = None
        self._strategy_slbacl_open = None
        self._strategy_slb_minimum_forward_strategy = None
        self._strategy_security_group_ingress_minimum_acl = None
        self._strategy_vm_defend_burst_solution = None
        self._strategy_vm_identity_auth_ssh_key_pair = None
        self._strategy_vm_security_group_rule_limit_port_access = None
        self.discriminator = None

        if strategy_db_ingress_minimum_acl is not None:
            self.strategy_db_ingress_minimum_acl = strategy_db_ingress_minimum_acl
        if strategy_oss_bucket_limit_anonymous_acl is not None:
            self.strategy_oss_bucket_limit_anonymous_acl = strategy_oss_bucket_limit_anonymous_acl
        if strategy_oss_bucket_server_encrypt is not None:
            self.strategy_oss_bucket_server_encrypt = strategy_oss_bucket_server_encrypt
        if strategy_oss_bucket_version_bak_recovery is not None:
            self.strategy_oss_bucket_version_bak_recovery = strategy_oss_bucket_version_bak_recovery
        if strategy_slbacl_open is not None:
            self.strategy_slbacl_open = strategy_slbacl_open
        if strategy_slb_minimum_forward_strategy is not None:
            self.strategy_slb_minimum_forward_strategy = strategy_slb_minimum_forward_strategy
        if strategy_security_group_ingress_minimum_acl is not None:
            self.strategy_security_group_ingress_minimum_acl = strategy_security_group_ingress_minimum_acl
        if strategy_vm_defend_burst_solution is not None:
            self.strategy_vm_defend_burst_solution = strategy_vm_defend_burst_solution
        if strategy_vm_identity_auth_ssh_key_pair is not None:
            self.strategy_vm_identity_auth_ssh_key_pair = strategy_vm_identity_auth_ssh_key_pair
        if strategy_vm_security_group_rule_limit_port_access is not None:
            self.strategy_vm_security_group_rule_limit_port_access = strategy_vm_security_group_rule_limit_port_access

    @property
    def strategy_db_ingress_minimum_acl(self):
        """Gets the strategy_db_ingress_minimum_acl of this ReferenceDataForGetRiskOutput.  # noqa: E501


        :return: The strategy_db_ingress_minimum_acl of this ReferenceDataForGetRiskOutput.  # noqa: E501
        :rtype: StrategyDBIngressMinimumACLForGetRiskOutput
        """
        return self._strategy_db_ingress_minimum_acl

    @strategy_db_ingress_minimum_acl.setter
    def strategy_db_ingress_minimum_acl(self, strategy_db_ingress_minimum_acl):
        """Sets the strategy_db_ingress_minimum_acl of this ReferenceDataForGetRiskOutput.


        :param strategy_db_ingress_minimum_acl: The strategy_db_ingress_minimum_acl of this ReferenceDataForGetRiskOutput.  # noqa: E501
        :type: StrategyDBIngressMinimumACLForGetRiskOutput
        """

        self._strategy_db_ingress_minimum_acl = strategy_db_ingress_minimum_acl

    @property
    def strategy_oss_bucket_limit_anonymous_acl(self):
        """Gets the strategy_oss_bucket_limit_anonymous_acl of this ReferenceDataForGetRiskOutput.  # noqa: E501


        :return: The strategy_oss_bucket_limit_anonymous_acl of this ReferenceDataForGetRiskOutput.  # noqa: E501
        :rtype: StrategyOSSBucketLimitAnonymousACLForGetRiskOutput
        """
        return self._strategy_oss_bucket_limit_anonymous_acl

    @strategy_oss_bucket_limit_anonymous_acl.setter
    def strategy_oss_bucket_limit_anonymous_acl(self, strategy_oss_bucket_limit_anonymous_acl):
        """Sets the strategy_oss_bucket_limit_anonymous_acl of this ReferenceDataForGetRiskOutput.


        :param strategy_oss_bucket_limit_anonymous_acl: The strategy_oss_bucket_limit_anonymous_acl of this ReferenceDataForGetRiskOutput.  # noqa: E501
        :type: StrategyOSSBucketLimitAnonymousACLForGetRiskOutput
        """

        self._strategy_oss_bucket_limit_anonymous_acl = strategy_oss_bucket_limit_anonymous_acl

    @property
    def strategy_oss_bucket_server_encrypt(self):
        """Gets the strategy_oss_bucket_server_encrypt of this ReferenceDataForGetRiskOutput.  # noqa: E501


        :return: The strategy_oss_bucket_server_encrypt of this ReferenceDataForGetRiskOutput.  # noqa: E501
        :rtype: StrategyOSSBucketServerEncryptForGetRiskOutput
        """
        return self._strategy_oss_bucket_server_encrypt

    @strategy_oss_bucket_server_encrypt.setter
    def strategy_oss_bucket_server_encrypt(self, strategy_oss_bucket_server_encrypt):
        """Sets the strategy_oss_bucket_server_encrypt of this ReferenceDataForGetRiskOutput.


        :param strategy_oss_bucket_server_encrypt: The strategy_oss_bucket_server_encrypt of this ReferenceDataForGetRiskOutput.  # noqa: E501
        :type: StrategyOSSBucketServerEncryptForGetRiskOutput
        """

        self._strategy_oss_bucket_server_encrypt = strategy_oss_bucket_server_encrypt

    @property
    def strategy_oss_bucket_version_bak_recovery(self):
        """Gets the strategy_oss_bucket_version_bak_recovery of this ReferenceDataForGetRiskOutput.  # noqa: E501


        :return: The strategy_oss_bucket_version_bak_recovery of this ReferenceDataForGetRiskOutput.  # noqa: E501
        :rtype: StrategyOSSBucketVersionBakRecoveryForGetRiskOutput
        """
        return self._strategy_oss_bucket_version_bak_recovery

    @strategy_oss_bucket_version_bak_recovery.setter
    def strategy_oss_bucket_version_bak_recovery(self, strategy_oss_bucket_version_bak_recovery):
        """Sets the strategy_oss_bucket_version_bak_recovery of this ReferenceDataForGetRiskOutput.


        :param strategy_oss_bucket_version_bak_recovery: The strategy_oss_bucket_version_bak_recovery of this ReferenceDataForGetRiskOutput.  # noqa: E501
        :type: StrategyOSSBucketVersionBakRecoveryForGetRiskOutput
        """

        self._strategy_oss_bucket_version_bak_recovery = strategy_oss_bucket_version_bak_recovery

    @property
    def strategy_slbacl_open(self):
        """Gets the strategy_slbacl_open of this ReferenceDataForGetRiskOutput.  # noqa: E501


        :return: The strategy_slbacl_open of this ReferenceDataForGetRiskOutput.  # noqa: E501
        :rtype: StrategySLBACLOpenForGetRiskOutput
        """
        return self._strategy_slbacl_open

    @strategy_slbacl_open.setter
    def strategy_slbacl_open(self, strategy_slbacl_open):
        """Sets the strategy_slbacl_open of this ReferenceDataForGetRiskOutput.


        :param strategy_slbacl_open: The strategy_slbacl_open of this ReferenceDataForGetRiskOutput.  # noqa: E501
        :type: StrategySLBACLOpenForGetRiskOutput
        """

        self._strategy_slbacl_open = strategy_slbacl_open

    @property
    def strategy_slb_minimum_forward_strategy(self):
        """Gets the strategy_slb_minimum_forward_strategy of this ReferenceDataForGetRiskOutput.  # noqa: E501


        :return: The strategy_slb_minimum_forward_strategy of this ReferenceDataForGetRiskOutput.  # noqa: E501
        :rtype: StrategySLBMinimumForwardStrategyForGetRiskOutput
        """
        return self._strategy_slb_minimum_forward_strategy

    @strategy_slb_minimum_forward_strategy.setter
    def strategy_slb_minimum_forward_strategy(self, strategy_slb_minimum_forward_strategy):
        """Sets the strategy_slb_minimum_forward_strategy of this ReferenceDataForGetRiskOutput.


        :param strategy_slb_minimum_forward_strategy: The strategy_slb_minimum_forward_strategy of this ReferenceDataForGetRiskOutput.  # noqa: E501
        :type: StrategySLBMinimumForwardStrategyForGetRiskOutput
        """

        self._strategy_slb_minimum_forward_strategy = strategy_slb_minimum_forward_strategy

    @property
    def strategy_security_group_ingress_minimum_acl(self):
        """Gets the strategy_security_group_ingress_minimum_acl of this ReferenceDataForGetRiskOutput.  # noqa: E501


        :return: The strategy_security_group_ingress_minimum_acl of this ReferenceDataForGetRiskOutput.  # noqa: E501
        :rtype: StrategySecurityGroupIngressMinimumACLForGetRiskOutput
        """
        return self._strategy_security_group_ingress_minimum_acl

    @strategy_security_group_ingress_minimum_acl.setter
    def strategy_security_group_ingress_minimum_acl(self, strategy_security_group_ingress_minimum_acl):
        """Sets the strategy_security_group_ingress_minimum_acl of this ReferenceDataForGetRiskOutput.


        :param strategy_security_group_ingress_minimum_acl: The strategy_security_group_ingress_minimum_acl of this ReferenceDataForGetRiskOutput.  # noqa: E501
        :type: StrategySecurityGroupIngressMinimumACLForGetRiskOutput
        """

        self._strategy_security_group_ingress_minimum_acl = strategy_security_group_ingress_minimum_acl

    @property
    def strategy_vm_defend_burst_solution(self):
        """Gets the strategy_vm_defend_burst_solution of this ReferenceDataForGetRiskOutput.  # noqa: E501


        :return: The strategy_vm_defend_burst_solution of this ReferenceDataForGetRiskOutput.  # noqa: E501
        :rtype: StrategyVMDefendBurstSolutionForGetRiskOutput
        """
        return self._strategy_vm_defend_burst_solution

    @strategy_vm_defend_burst_solution.setter
    def strategy_vm_defend_burst_solution(self, strategy_vm_defend_burst_solution):
        """Sets the strategy_vm_defend_burst_solution of this ReferenceDataForGetRiskOutput.


        :param strategy_vm_defend_burst_solution: The strategy_vm_defend_burst_solution of this ReferenceDataForGetRiskOutput.  # noqa: E501
        :type: StrategyVMDefendBurstSolutionForGetRiskOutput
        """

        self._strategy_vm_defend_burst_solution = strategy_vm_defend_burst_solution

    @property
    def strategy_vm_identity_auth_ssh_key_pair(self):
        """Gets the strategy_vm_identity_auth_ssh_key_pair of this ReferenceDataForGetRiskOutput.  # noqa: E501


        :return: The strategy_vm_identity_auth_ssh_key_pair of this ReferenceDataForGetRiskOutput.  # noqa: E501
        :rtype: StrategyVMIdentityAuthSSHKeyPairForGetRiskOutput
        """
        return self._strategy_vm_identity_auth_ssh_key_pair

    @strategy_vm_identity_auth_ssh_key_pair.setter
    def strategy_vm_identity_auth_ssh_key_pair(self, strategy_vm_identity_auth_ssh_key_pair):
        """Sets the strategy_vm_identity_auth_ssh_key_pair of this ReferenceDataForGetRiskOutput.


        :param strategy_vm_identity_auth_ssh_key_pair: The strategy_vm_identity_auth_ssh_key_pair of this ReferenceDataForGetRiskOutput.  # noqa: E501
        :type: StrategyVMIdentityAuthSSHKeyPairForGetRiskOutput
        """

        self._strategy_vm_identity_auth_ssh_key_pair = strategy_vm_identity_auth_ssh_key_pair

    @property
    def strategy_vm_security_group_rule_limit_port_access(self):
        """Gets the strategy_vm_security_group_rule_limit_port_access of this ReferenceDataForGetRiskOutput.  # noqa: E501


        :return: The strategy_vm_security_group_rule_limit_port_access of this ReferenceDataForGetRiskOutput.  # noqa: E501
        :rtype: StrategyVMSecurityGroupRuleLimitPortAccessForGetRiskOutput
        """
        return self._strategy_vm_security_group_rule_limit_port_access

    @strategy_vm_security_group_rule_limit_port_access.setter
    def strategy_vm_security_group_rule_limit_port_access(self, strategy_vm_security_group_rule_limit_port_access):
        """Sets the strategy_vm_security_group_rule_limit_port_access of this ReferenceDataForGetRiskOutput.


        :param strategy_vm_security_group_rule_limit_port_access: The strategy_vm_security_group_rule_limit_port_access of this ReferenceDataForGetRiskOutput.  # noqa: E501
        :type: StrategyVMSecurityGroupRuleLimitPortAccessForGetRiskOutput
        """

        self._strategy_vm_security_group_rule_limit_port_access = strategy_vm_security_group_rule_limit_port_access

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
        if issubclass(ReferenceDataForGetRiskOutput, dict):
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
        if not isinstance(other, ReferenceDataForGetRiskOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReferenceDataForGetRiskOutput):
            return True

        return self.to_dict() != other.to_dict()
