# coding: utf-8

"""
    waf

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class UpdateWafServiceControlRequest(object):
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
        'api_enable': 'int',
        'auto_cc_enable': 'int',
        'black_ip_enable': 'int',
        'black_lct_enable': 'int',
        'bot_dytoken_enable': 'int',
        'bot_frequency_enable': 'int',
        'bot_repeat_enable': 'int',
        'bot_sequence_default_action': 'int',
        'bot_sequence_enable': 'int',
        'cc_enable': 'int',
        'custom_bot_enable': 'int',
        'custom_rsp_enable': 'int',
        'dlp_enable': 'int',
        'host': 'str',
        'project_name': 'str',
        'system_bot_enable': 'int',
        'tls_enable': 'int',
        'tamper_proof_enable': 'int',
        'waf_enable': 'int',
        'waf_white_req_enable': 'int',
        'white_enable': 'int',
        'white_field_enable': 'int'
    }

    attribute_map = {
        'api_enable': 'ApiEnable',
        'auto_cc_enable': 'AutoCCEnable',
        'black_ip_enable': 'BlackIpEnable',
        'black_lct_enable': 'BlackLctEnable',
        'bot_dytoken_enable': 'BotDytokenEnable',
        'bot_frequency_enable': 'BotFrequencyEnable',
        'bot_repeat_enable': 'BotRepeatEnable',
        'bot_sequence_default_action': 'BotSequenceDefaultAction',
        'bot_sequence_enable': 'BotSequenceEnable',
        'cc_enable': 'CcEnable',
        'custom_bot_enable': 'CustomBotEnable',
        'custom_rsp_enable': 'CustomRspEnable',
        'dlp_enable': 'DlpEnable',
        'host': 'Host',
        'project_name': 'ProjectName',
        'system_bot_enable': 'SystemBotEnable',
        'tls_enable': 'TLSEnable',
        'tamper_proof_enable': 'TamperProofEnable',
        'waf_enable': 'WafEnable',
        'waf_white_req_enable': 'WafWhiteReqEnable',
        'white_enable': 'WhiteEnable',
        'white_field_enable': 'WhiteFieldEnable'
    }

    def __init__(self, api_enable=None, auto_cc_enable=None, black_ip_enable=None, black_lct_enable=None, bot_dytoken_enable=None, bot_frequency_enable=None, bot_repeat_enable=None, bot_sequence_default_action=None, bot_sequence_enable=None, cc_enable=None, custom_bot_enable=None, custom_rsp_enable=None, dlp_enable=None, host=None, project_name=None, system_bot_enable=None, tls_enable=None, tamper_proof_enable=None, waf_enable=None, waf_white_req_enable=None, white_enable=None, white_field_enable=None, _configuration=None):  # noqa: E501
        """UpdateWafServiceControlRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._api_enable = None
        self._auto_cc_enable = None
        self._black_ip_enable = None
        self._black_lct_enable = None
        self._bot_dytoken_enable = None
        self._bot_frequency_enable = None
        self._bot_repeat_enable = None
        self._bot_sequence_default_action = None
        self._bot_sequence_enable = None
        self._cc_enable = None
        self._custom_bot_enable = None
        self._custom_rsp_enable = None
        self._dlp_enable = None
        self._host = None
        self._project_name = None
        self._system_bot_enable = None
        self._tls_enable = None
        self._tamper_proof_enable = None
        self._waf_enable = None
        self._waf_white_req_enable = None
        self._white_enable = None
        self._white_field_enable = None
        self.discriminator = None

        if api_enable is not None:
            self.api_enable = api_enable
        if auto_cc_enable is not None:
            self.auto_cc_enable = auto_cc_enable
        if black_ip_enable is not None:
            self.black_ip_enable = black_ip_enable
        if black_lct_enable is not None:
            self.black_lct_enable = black_lct_enable
        if bot_dytoken_enable is not None:
            self.bot_dytoken_enable = bot_dytoken_enable
        if bot_frequency_enable is not None:
            self.bot_frequency_enable = bot_frequency_enable
        if bot_repeat_enable is not None:
            self.bot_repeat_enable = bot_repeat_enable
        if bot_sequence_default_action is not None:
            self.bot_sequence_default_action = bot_sequence_default_action
        if bot_sequence_enable is not None:
            self.bot_sequence_enable = bot_sequence_enable
        if cc_enable is not None:
            self.cc_enable = cc_enable
        if custom_bot_enable is not None:
            self.custom_bot_enable = custom_bot_enable
        if custom_rsp_enable is not None:
            self.custom_rsp_enable = custom_rsp_enable
        if dlp_enable is not None:
            self.dlp_enable = dlp_enable
        self.host = host
        if project_name is not None:
            self.project_name = project_name
        if system_bot_enable is not None:
            self.system_bot_enable = system_bot_enable
        if tls_enable is not None:
            self.tls_enable = tls_enable
        if tamper_proof_enable is not None:
            self.tamper_proof_enable = tamper_proof_enable
        if waf_enable is not None:
            self.waf_enable = waf_enable
        if waf_white_req_enable is not None:
            self.waf_white_req_enable = waf_white_req_enable
        if white_enable is not None:
            self.white_enable = white_enable
        if white_field_enable is not None:
            self.white_field_enable = white_field_enable

    @property
    def api_enable(self):
        """Gets the api_enable of this UpdateWafServiceControlRequest.  # noqa: E501


        :return: The api_enable of this UpdateWafServiceControlRequest.  # noqa: E501
        :rtype: int
        """
        return self._api_enable

    @api_enable.setter
    def api_enable(self, api_enable):
        """Sets the api_enable of this UpdateWafServiceControlRequest.


        :param api_enable: The api_enable of this UpdateWafServiceControlRequest.  # noqa: E501
        :type: int
        """

        self._api_enable = api_enable

    @property
    def auto_cc_enable(self):
        """Gets the auto_cc_enable of this UpdateWafServiceControlRequest.  # noqa: E501


        :return: The auto_cc_enable of this UpdateWafServiceControlRequest.  # noqa: E501
        :rtype: int
        """
        return self._auto_cc_enable

    @auto_cc_enable.setter
    def auto_cc_enable(self, auto_cc_enable):
        """Sets the auto_cc_enable of this UpdateWafServiceControlRequest.


        :param auto_cc_enable: The auto_cc_enable of this UpdateWafServiceControlRequest.  # noqa: E501
        :type: int
        """

        self._auto_cc_enable = auto_cc_enable

    @property
    def black_ip_enable(self):
        """Gets the black_ip_enable of this UpdateWafServiceControlRequest.  # noqa: E501


        :return: The black_ip_enable of this UpdateWafServiceControlRequest.  # noqa: E501
        :rtype: int
        """
        return self._black_ip_enable

    @black_ip_enable.setter
    def black_ip_enable(self, black_ip_enable):
        """Sets the black_ip_enable of this UpdateWafServiceControlRequest.


        :param black_ip_enable: The black_ip_enable of this UpdateWafServiceControlRequest.  # noqa: E501
        :type: int
        """

        self._black_ip_enable = black_ip_enable

    @property
    def black_lct_enable(self):
        """Gets the black_lct_enable of this UpdateWafServiceControlRequest.  # noqa: E501


        :return: The black_lct_enable of this UpdateWafServiceControlRequest.  # noqa: E501
        :rtype: int
        """
        return self._black_lct_enable

    @black_lct_enable.setter
    def black_lct_enable(self, black_lct_enable):
        """Sets the black_lct_enable of this UpdateWafServiceControlRequest.


        :param black_lct_enable: The black_lct_enable of this UpdateWafServiceControlRequest.  # noqa: E501
        :type: int
        """

        self._black_lct_enable = black_lct_enable

    @property
    def bot_dytoken_enable(self):
        """Gets the bot_dytoken_enable of this UpdateWafServiceControlRequest.  # noqa: E501


        :return: The bot_dytoken_enable of this UpdateWafServiceControlRequest.  # noqa: E501
        :rtype: int
        """
        return self._bot_dytoken_enable

    @bot_dytoken_enable.setter
    def bot_dytoken_enable(self, bot_dytoken_enable):
        """Sets the bot_dytoken_enable of this UpdateWafServiceControlRequest.


        :param bot_dytoken_enable: The bot_dytoken_enable of this UpdateWafServiceControlRequest.  # noqa: E501
        :type: int
        """

        self._bot_dytoken_enable = bot_dytoken_enable

    @property
    def bot_frequency_enable(self):
        """Gets the bot_frequency_enable of this UpdateWafServiceControlRequest.  # noqa: E501


        :return: The bot_frequency_enable of this UpdateWafServiceControlRequest.  # noqa: E501
        :rtype: int
        """
        return self._bot_frequency_enable

    @bot_frequency_enable.setter
    def bot_frequency_enable(self, bot_frequency_enable):
        """Sets the bot_frequency_enable of this UpdateWafServiceControlRequest.


        :param bot_frequency_enable: The bot_frequency_enable of this UpdateWafServiceControlRequest.  # noqa: E501
        :type: int
        """

        self._bot_frequency_enable = bot_frequency_enable

    @property
    def bot_repeat_enable(self):
        """Gets the bot_repeat_enable of this UpdateWafServiceControlRequest.  # noqa: E501


        :return: The bot_repeat_enable of this UpdateWafServiceControlRequest.  # noqa: E501
        :rtype: int
        """
        return self._bot_repeat_enable

    @bot_repeat_enable.setter
    def bot_repeat_enable(self, bot_repeat_enable):
        """Sets the bot_repeat_enable of this UpdateWafServiceControlRequest.


        :param bot_repeat_enable: The bot_repeat_enable of this UpdateWafServiceControlRequest.  # noqa: E501
        :type: int
        """

        self._bot_repeat_enable = bot_repeat_enable

    @property
    def bot_sequence_default_action(self):
        """Gets the bot_sequence_default_action of this UpdateWafServiceControlRequest.  # noqa: E501


        :return: The bot_sequence_default_action of this UpdateWafServiceControlRequest.  # noqa: E501
        :rtype: int
        """
        return self._bot_sequence_default_action

    @bot_sequence_default_action.setter
    def bot_sequence_default_action(self, bot_sequence_default_action):
        """Sets the bot_sequence_default_action of this UpdateWafServiceControlRequest.


        :param bot_sequence_default_action: The bot_sequence_default_action of this UpdateWafServiceControlRequest.  # noqa: E501
        :type: int
        """

        self._bot_sequence_default_action = bot_sequence_default_action

    @property
    def bot_sequence_enable(self):
        """Gets the bot_sequence_enable of this UpdateWafServiceControlRequest.  # noqa: E501


        :return: The bot_sequence_enable of this UpdateWafServiceControlRequest.  # noqa: E501
        :rtype: int
        """
        return self._bot_sequence_enable

    @bot_sequence_enable.setter
    def bot_sequence_enable(self, bot_sequence_enable):
        """Sets the bot_sequence_enable of this UpdateWafServiceControlRequest.


        :param bot_sequence_enable: The bot_sequence_enable of this UpdateWafServiceControlRequest.  # noqa: E501
        :type: int
        """

        self._bot_sequence_enable = bot_sequence_enable

    @property
    def cc_enable(self):
        """Gets the cc_enable of this UpdateWafServiceControlRequest.  # noqa: E501


        :return: The cc_enable of this UpdateWafServiceControlRequest.  # noqa: E501
        :rtype: int
        """
        return self._cc_enable

    @cc_enable.setter
    def cc_enable(self, cc_enable):
        """Sets the cc_enable of this UpdateWafServiceControlRequest.


        :param cc_enable: The cc_enable of this UpdateWafServiceControlRequest.  # noqa: E501
        :type: int
        """

        self._cc_enable = cc_enable

    @property
    def custom_bot_enable(self):
        """Gets the custom_bot_enable of this UpdateWafServiceControlRequest.  # noqa: E501


        :return: The custom_bot_enable of this UpdateWafServiceControlRequest.  # noqa: E501
        :rtype: int
        """
        return self._custom_bot_enable

    @custom_bot_enable.setter
    def custom_bot_enable(self, custom_bot_enable):
        """Sets the custom_bot_enable of this UpdateWafServiceControlRequest.


        :param custom_bot_enable: The custom_bot_enable of this UpdateWafServiceControlRequest.  # noqa: E501
        :type: int
        """

        self._custom_bot_enable = custom_bot_enable

    @property
    def custom_rsp_enable(self):
        """Gets the custom_rsp_enable of this UpdateWafServiceControlRequest.  # noqa: E501


        :return: The custom_rsp_enable of this UpdateWafServiceControlRequest.  # noqa: E501
        :rtype: int
        """
        return self._custom_rsp_enable

    @custom_rsp_enable.setter
    def custom_rsp_enable(self, custom_rsp_enable):
        """Sets the custom_rsp_enable of this UpdateWafServiceControlRequest.


        :param custom_rsp_enable: The custom_rsp_enable of this UpdateWafServiceControlRequest.  # noqa: E501
        :type: int
        """

        self._custom_rsp_enable = custom_rsp_enable

    @property
    def dlp_enable(self):
        """Gets the dlp_enable of this UpdateWafServiceControlRequest.  # noqa: E501


        :return: The dlp_enable of this UpdateWafServiceControlRequest.  # noqa: E501
        :rtype: int
        """
        return self._dlp_enable

    @dlp_enable.setter
    def dlp_enable(self, dlp_enable):
        """Sets the dlp_enable of this UpdateWafServiceControlRequest.


        :param dlp_enable: The dlp_enable of this UpdateWafServiceControlRequest.  # noqa: E501
        :type: int
        """

        self._dlp_enable = dlp_enable

    @property
    def host(self):
        """Gets the host of this UpdateWafServiceControlRequest.  # noqa: E501


        :return: The host of this UpdateWafServiceControlRequest.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this UpdateWafServiceControlRequest.


        :param host: The host of this UpdateWafServiceControlRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and host is None:
            raise ValueError("Invalid value for `host`, must not be `None`")  # noqa: E501

        self._host = host

    @property
    def project_name(self):
        """Gets the project_name of this UpdateWafServiceControlRequest.  # noqa: E501


        :return: The project_name of this UpdateWafServiceControlRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this UpdateWafServiceControlRequest.


        :param project_name: The project_name of this UpdateWafServiceControlRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def system_bot_enable(self):
        """Gets the system_bot_enable of this UpdateWafServiceControlRequest.  # noqa: E501


        :return: The system_bot_enable of this UpdateWafServiceControlRequest.  # noqa: E501
        :rtype: int
        """
        return self._system_bot_enable

    @system_bot_enable.setter
    def system_bot_enable(self, system_bot_enable):
        """Sets the system_bot_enable of this UpdateWafServiceControlRequest.


        :param system_bot_enable: The system_bot_enable of this UpdateWafServiceControlRequest.  # noqa: E501
        :type: int
        """

        self._system_bot_enable = system_bot_enable

    @property
    def tls_enable(self):
        """Gets the tls_enable of this UpdateWafServiceControlRequest.  # noqa: E501


        :return: The tls_enable of this UpdateWafServiceControlRequest.  # noqa: E501
        :rtype: int
        """
        return self._tls_enable

    @tls_enable.setter
    def tls_enable(self, tls_enable):
        """Sets the tls_enable of this UpdateWafServiceControlRequest.


        :param tls_enable: The tls_enable of this UpdateWafServiceControlRequest.  # noqa: E501
        :type: int
        """

        self._tls_enable = tls_enable

    @property
    def tamper_proof_enable(self):
        """Gets the tamper_proof_enable of this UpdateWafServiceControlRequest.  # noqa: E501


        :return: The tamper_proof_enable of this UpdateWafServiceControlRequest.  # noqa: E501
        :rtype: int
        """
        return self._tamper_proof_enable

    @tamper_proof_enable.setter
    def tamper_proof_enable(self, tamper_proof_enable):
        """Sets the tamper_proof_enable of this UpdateWafServiceControlRequest.


        :param tamper_proof_enable: The tamper_proof_enable of this UpdateWafServiceControlRequest.  # noqa: E501
        :type: int
        """

        self._tamper_proof_enable = tamper_proof_enable

    @property
    def waf_enable(self):
        """Gets the waf_enable of this UpdateWafServiceControlRequest.  # noqa: E501


        :return: The waf_enable of this UpdateWafServiceControlRequest.  # noqa: E501
        :rtype: int
        """
        return self._waf_enable

    @waf_enable.setter
    def waf_enable(self, waf_enable):
        """Sets the waf_enable of this UpdateWafServiceControlRequest.


        :param waf_enable: The waf_enable of this UpdateWafServiceControlRequest.  # noqa: E501
        :type: int
        """

        self._waf_enable = waf_enable

    @property
    def waf_white_req_enable(self):
        """Gets the waf_white_req_enable of this UpdateWafServiceControlRequest.  # noqa: E501


        :return: The waf_white_req_enable of this UpdateWafServiceControlRequest.  # noqa: E501
        :rtype: int
        """
        return self._waf_white_req_enable

    @waf_white_req_enable.setter
    def waf_white_req_enable(self, waf_white_req_enable):
        """Sets the waf_white_req_enable of this UpdateWafServiceControlRequest.


        :param waf_white_req_enable: The waf_white_req_enable of this UpdateWafServiceControlRequest.  # noqa: E501
        :type: int
        """

        self._waf_white_req_enable = waf_white_req_enable

    @property
    def white_enable(self):
        """Gets the white_enable of this UpdateWafServiceControlRequest.  # noqa: E501


        :return: The white_enable of this UpdateWafServiceControlRequest.  # noqa: E501
        :rtype: int
        """
        return self._white_enable

    @white_enable.setter
    def white_enable(self, white_enable):
        """Sets the white_enable of this UpdateWafServiceControlRequest.


        :param white_enable: The white_enable of this UpdateWafServiceControlRequest.  # noqa: E501
        :type: int
        """

        self._white_enable = white_enable

    @property
    def white_field_enable(self):
        """Gets the white_field_enable of this UpdateWafServiceControlRequest.  # noqa: E501


        :return: The white_field_enable of this UpdateWafServiceControlRequest.  # noqa: E501
        :rtype: int
        """
        return self._white_field_enable

    @white_field_enable.setter
    def white_field_enable(self, white_field_enable):
        """Sets the white_field_enable of this UpdateWafServiceControlRequest.


        :param white_field_enable: The white_field_enable of this UpdateWafServiceControlRequest.  # noqa: E501
        :type: int
        """

        self._white_field_enable = white_field_enable

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
        if issubclass(UpdateWafServiceControlRequest, dict):
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
        if not isinstance(other, UpdateWafServiceControlRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateWafServiceControlRequest):
            return True

        return self.to_dict() != other.to_dict()
