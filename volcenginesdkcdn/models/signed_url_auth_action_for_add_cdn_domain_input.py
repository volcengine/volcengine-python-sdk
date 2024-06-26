# coding: utf-8

"""
    cdn

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class SignedUrlAuthActionForAddCdnDomainInput(object):
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
        'auth_algorithm': 'str',
        'backup_secret_key': 'str',
        'custom_variable_rules': 'CustomVariableRulesForAddCdnDomainInput',
        'duration': 'int',
        'keep_origin_arg': 'bool',
        'master_secret_key': 'str',
        'mpd_var_expand': 'bool',
        'rewrite_m3u8': 'bool',
        'rewrite_m3u8_rule': 'RewriteM3u8RuleForAddCdnDomainInput',
        'rewrite_mpd': 'bool',
        'sign_name': 'str',
        'signature_rule': 'list[str]',
        'time_format': 'str',
        'time_name': 'str',
        'url_auth_type': 'str',
        'url_auth_custom_action': 'UrlAuthCustomActionForAddCdnDomainInput'
    }

    attribute_map = {
        'auth_algorithm': 'AuthAlgorithm',
        'backup_secret_key': 'BackupSecretKey',
        'custom_variable_rules': 'CustomVariableRules',
        'duration': 'Duration',
        'keep_origin_arg': 'KeepOriginArg',
        'master_secret_key': 'MasterSecretKey',
        'mpd_var_expand': 'MpdVarExpand',
        'rewrite_m3u8': 'RewriteM3u8',
        'rewrite_m3u8_rule': 'RewriteM3u8Rule',
        'rewrite_mpd': 'RewriteMpd',
        'sign_name': 'SignName',
        'signature_rule': 'SignatureRule',
        'time_format': 'TimeFormat',
        'time_name': 'TimeName',
        'url_auth_type': 'URLAuthType',
        'url_auth_custom_action': 'UrlAuthCustomAction'
    }

    def __init__(self, auth_algorithm=None, backup_secret_key=None, custom_variable_rules=None, duration=None, keep_origin_arg=None, master_secret_key=None, mpd_var_expand=None, rewrite_m3u8=None, rewrite_m3u8_rule=None, rewrite_mpd=None, sign_name=None, signature_rule=None, time_format=None, time_name=None, url_auth_type=None, url_auth_custom_action=None, _configuration=None):  # noqa: E501
        """SignedUrlAuthActionForAddCdnDomainInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._auth_algorithm = None
        self._backup_secret_key = None
        self._custom_variable_rules = None
        self._duration = None
        self._keep_origin_arg = None
        self._master_secret_key = None
        self._mpd_var_expand = None
        self._rewrite_m3u8 = None
        self._rewrite_m3u8_rule = None
        self._rewrite_mpd = None
        self._sign_name = None
        self._signature_rule = None
        self._time_format = None
        self._time_name = None
        self._url_auth_type = None
        self._url_auth_custom_action = None
        self.discriminator = None

        if auth_algorithm is not None:
            self.auth_algorithm = auth_algorithm
        if backup_secret_key is not None:
            self.backup_secret_key = backup_secret_key
        if custom_variable_rules is not None:
            self.custom_variable_rules = custom_variable_rules
        if duration is not None:
            self.duration = duration
        if keep_origin_arg is not None:
            self.keep_origin_arg = keep_origin_arg
        if master_secret_key is not None:
            self.master_secret_key = master_secret_key
        if mpd_var_expand is not None:
            self.mpd_var_expand = mpd_var_expand
        if rewrite_m3u8 is not None:
            self.rewrite_m3u8 = rewrite_m3u8
        if rewrite_m3u8_rule is not None:
            self.rewrite_m3u8_rule = rewrite_m3u8_rule
        if rewrite_mpd is not None:
            self.rewrite_mpd = rewrite_mpd
        if sign_name is not None:
            self.sign_name = sign_name
        if signature_rule is not None:
            self.signature_rule = signature_rule
        if time_format is not None:
            self.time_format = time_format
        if time_name is not None:
            self.time_name = time_name
        if url_auth_type is not None:
            self.url_auth_type = url_auth_type
        if url_auth_custom_action is not None:
            self.url_auth_custom_action = url_auth_custom_action

    @property
    def auth_algorithm(self):
        """Gets the auth_algorithm of this SignedUrlAuthActionForAddCdnDomainInput.  # noqa: E501


        :return: The auth_algorithm of this SignedUrlAuthActionForAddCdnDomainInput.  # noqa: E501
        :rtype: str
        """
        return self._auth_algorithm

    @auth_algorithm.setter
    def auth_algorithm(self, auth_algorithm):
        """Sets the auth_algorithm of this SignedUrlAuthActionForAddCdnDomainInput.


        :param auth_algorithm: The auth_algorithm of this SignedUrlAuthActionForAddCdnDomainInput.  # noqa: E501
        :type: str
        """

        self._auth_algorithm = auth_algorithm

    @property
    def backup_secret_key(self):
        """Gets the backup_secret_key of this SignedUrlAuthActionForAddCdnDomainInput.  # noqa: E501


        :return: The backup_secret_key of this SignedUrlAuthActionForAddCdnDomainInput.  # noqa: E501
        :rtype: str
        """
        return self._backup_secret_key

    @backup_secret_key.setter
    def backup_secret_key(self, backup_secret_key):
        """Sets the backup_secret_key of this SignedUrlAuthActionForAddCdnDomainInput.


        :param backup_secret_key: The backup_secret_key of this SignedUrlAuthActionForAddCdnDomainInput.  # noqa: E501
        :type: str
        """

        self._backup_secret_key = backup_secret_key

    @property
    def custom_variable_rules(self):
        """Gets the custom_variable_rules of this SignedUrlAuthActionForAddCdnDomainInput.  # noqa: E501


        :return: The custom_variable_rules of this SignedUrlAuthActionForAddCdnDomainInput.  # noqa: E501
        :rtype: CustomVariableRulesForAddCdnDomainInput
        """
        return self._custom_variable_rules

    @custom_variable_rules.setter
    def custom_variable_rules(self, custom_variable_rules):
        """Sets the custom_variable_rules of this SignedUrlAuthActionForAddCdnDomainInput.


        :param custom_variable_rules: The custom_variable_rules of this SignedUrlAuthActionForAddCdnDomainInput.  # noqa: E501
        :type: CustomVariableRulesForAddCdnDomainInput
        """

        self._custom_variable_rules = custom_variable_rules

    @property
    def duration(self):
        """Gets the duration of this SignedUrlAuthActionForAddCdnDomainInput.  # noqa: E501


        :return: The duration of this SignedUrlAuthActionForAddCdnDomainInput.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this SignedUrlAuthActionForAddCdnDomainInput.


        :param duration: The duration of this SignedUrlAuthActionForAddCdnDomainInput.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def keep_origin_arg(self):
        """Gets the keep_origin_arg of this SignedUrlAuthActionForAddCdnDomainInput.  # noqa: E501


        :return: The keep_origin_arg of this SignedUrlAuthActionForAddCdnDomainInput.  # noqa: E501
        :rtype: bool
        """
        return self._keep_origin_arg

    @keep_origin_arg.setter
    def keep_origin_arg(self, keep_origin_arg):
        """Sets the keep_origin_arg of this SignedUrlAuthActionForAddCdnDomainInput.


        :param keep_origin_arg: The keep_origin_arg of this SignedUrlAuthActionForAddCdnDomainInput.  # noqa: E501
        :type: bool
        """

        self._keep_origin_arg = keep_origin_arg

    @property
    def master_secret_key(self):
        """Gets the master_secret_key of this SignedUrlAuthActionForAddCdnDomainInput.  # noqa: E501


        :return: The master_secret_key of this SignedUrlAuthActionForAddCdnDomainInput.  # noqa: E501
        :rtype: str
        """
        return self._master_secret_key

    @master_secret_key.setter
    def master_secret_key(self, master_secret_key):
        """Sets the master_secret_key of this SignedUrlAuthActionForAddCdnDomainInput.


        :param master_secret_key: The master_secret_key of this SignedUrlAuthActionForAddCdnDomainInput.  # noqa: E501
        :type: str
        """

        self._master_secret_key = master_secret_key

    @property
    def mpd_var_expand(self):
        """Gets the mpd_var_expand of this SignedUrlAuthActionForAddCdnDomainInput.  # noqa: E501


        :return: The mpd_var_expand of this SignedUrlAuthActionForAddCdnDomainInput.  # noqa: E501
        :rtype: bool
        """
        return self._mpd_var_expand

    @mpd_var_expand.setter
    def mpd_var_expand(self, mpd_var_expand):
        """Sets the mpd_var_expand of this SignedUrlAuthActionForAddCdnDomainInput.


        :param mpd_var_expand: The mpd_var_expand of this SignedUrlAuthActionForAddCdnDomainInput.  # noqa: E501
        :type: bool
        """

        self._mpd_var_expand = mpd_var_expand

    @property
    def rewrite_m3u8(self):
        """Gets the rewrite_m3u8 of this SignedUrlAuthActionForAddCdnDomainInput.  # noqa: E501


        :return: The rewrite_m3u8 of this SignedUrlAuthActionForAddCdnDomainInput.  # noqa: E501
        :rtype: bool
        """
        return self._rewrite_m3u8

    @rewrite_m3u8.setter
    def rewrite_m3u8(self, rewrite_m3u8):
        """Sets the rewrite_m3u8 of this SignedUrlAuthActionForAddCdnDomainInput.


        :param rewrite_m3u8: The rewrite_m3u8 of this SignedUrlAuthActionForAddCdnDomainInput.  # noqa: E501
        :type: bool
        """

        self._rewrite_m3u8 = rewrite_m3u8

    @property
    def rewrite_m3u8_rule(self):
        """Gets the rewrite_m3u8_rule of this SignedUrlAuthActionForAddCdnDomainInput.  # noqa: E501


        :return: The rewrite_m3u8_rule of this SignedUrlAuthActionForAddCdnDomainInput.  # noqa: E501
        :rtype: RewriteM3u8RuleForAddCdnDomainInput
        """
        return self._rewrite_m3u8_rule

    @rewrite_m3u8_rule.setter
    def rewrite_m3u8_rule(self, rewrite_m3u8_rule):
        """Sets the rewrite_m3u8_rule of this SignedUrlAuthActionForAddCdnDomainInput.


        :param rewrite_m3u8_rule: The rewrite_m3u8_rule of this SignedUrlAuthActionForAddCdnDomainInput.  # noqa: E501
        :type: RewriteM3u8RuleForAddCdnDomainInput
        """

        self._rewrite_m3u8_rule = rewrite_m3u8_rule

    @property
    def rewrite_mpd(self):
        """Gets the rewrite_mpd of this SignedUrlAuthActionForAddCdnDomainInput.  # noqa: E501


        :return: The rewrite_mpd of this SignedUrlAuthActionForAddCdnDomainInput.  # noqa: E501
        :rtype: bool
        """
        return self._rewrite_mpd

    @rewrite_mpd.setter
    def rewrite_mpd(self, rewrite_mpd):
        """Sets the rewrite_mpd of this SignedUrlAuthActionForAddCdnDomainInput.


        :param rewrite_mpd: The rewrite_mpd of this SignedUrlAuthActionForAddCdnDomainInput.  # noqa: E501
        :type: bool
        """

        self._rewrite_mpd = rewrite_mpd

    @property
    def sign_name(self):
        """Gets the sign_name of this SignedUrlAuthActionForAddCdnDomainInput.  # noqa: E501


        :return: The sign_name of this SignedUrlAuthActionForAddCdnDomainInput.  # noqa: E501
        :rtype: str
        """
        return self._sign_name

    @sign_name.setter
    def sign_name(self, sign_name):
        """Sets the sign_name of this SignedUrlAuthActionForAddCdnDomainInput.


        :param sign_name: The sign_name of this SignedUrlAuthActionForAddCdnDomainInput.  # noqa: E501
        :type: str
        """

        self._sign_name = sign_name

    @property
    def signature_rule(self):
        """Gets the signature_rule of this SignedUrlAuthActionForAddCdnDomainInput.  # noqa: E501


        :return: The signature_rule of this SignedUrlAuthActionForAddCdnDomainInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._signature_rule

    @signature_rule.setter
    def signature_rule(self, signature_rule):
        """Sets the signature_rule of this SignedUrlAuthActionForAddCdnDomainInput.


        :param signature_rule: The signature_rule of this SignedUrlAuthActionForAddCdnDomainInput.  # noqa: E501
        :type: list[str]
        """

        self._signature_rule = signature_rule

    @property
    def time_format(self):
        """Gets the time_format of this SignedUrlAuthActionForAddCdnDomainInput.  # noqa: E501


        :return: The time_format of this SignedUrlAuthActionForAddCdnDomainInput.  # noqa: E501
        :rtype: str
        """
        return self._time_format

    @time_format.setter
    def time_format(self, time_format):
        """Sets the time_format of this SignedUrlAuthActionForAddCdnDomainInput.


        :param time_format: The time_format of this SignedUrlAuthActionForAddCdnDomainInput.  # noqa: E501
        :type: str
        """

        self._time_format = time_format

    @property
    def time_name(self):
        """Gets the time_name of this SignedUrlAuthActionForAddCdnDomainInput.  # noqa: E501


        :return: The time_name of this SignedUrlAuthActionForAddCdnDomainInput.  # noqa: E501
        :rtype: str
        """
        return self._time_name

    @time_name.setter
    def time_name(self, time_name):
        """Sets the time_name of this SignedUrlAuthActionForAddCdnDomainInput.


        :param time_name: The time_name of this SignedUrlAuthActionForAddCdnDomainInput.  # noqa: E501
        :type: str
        """

        self._time_name = time_name

    @property
    def url_auth_type(self):
        """Gets the url_auth_type of this SignedUrlAuthActionForAddCdnDomainInput.  # noqa: E501


        :return: The url_auth_type of this SignedUrlAuthActionForAddCdnDomainInput.  # noqa: E501
        :rtype: str
        """
        return self._url_auth_type

    @url_auth_type.setter
    def url_auth_type(self, url_auth_type):
        """Sets the url_auth_type of this SignedUrlAuthActionForAddCdnDomainInput.


        :param url_auth_type: The url_auth_type of this SignedUrlAuthActionForAddCdnDomainInput.  # noqa: E501
        :type: str
        """

        self._url_auth_type = url_auth_type

    @property
    def url_auth_custom_action(self):
        """Gets the url_auth_custom_action of this SignedUrlAuthActionForAddCdnDomainInput.  # noqa: E501


        :return: The url_auth_custom_action of this SignedUrlAuthActionForAddCdnDomainInput.  # noqa: E501
        :rtype: UrlAuthCustomActionForAddCdnDomainInput
        """
        return self._url_auth_custom_action

    @url_auth_custom_action.setter
    def url_auth_custom_action(self, url_auth_custom_action):
        """Sets the url_auth_custom_action of this SignedUrlAuthActionForAddCdnDomainInput.


        :param url_auth_custom_action: The url_auth_custom_action of this SignedUrlAuthActionForAddCdnDomainInput.  # noqa: E501
        :type: UrlAuthCustomActionForAddCdnDomainInput
        """

        self._url_auth_custom_action = url_auth_custom_action

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
        if issubclass(SignedUrlAuthActionForAddCdnDomainInput, dict):
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
        if not isinstance(other, SignedUrlAuthActionForAddCdnDomainInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SignedUrlAuthActionForAddCdnDomainInput):
            return True

        return self.to_dict() != other.to_dict()
