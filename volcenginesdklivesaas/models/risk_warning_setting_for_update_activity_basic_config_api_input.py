# coding: utf-8

"""
    livesaas

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class RiskWarningSettingForUpdateActivityBasicConfigAPIInput(object):
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
        'is_risk_warning_enable': 'int',
        'risk_warning_button_text': 'str',
        'risk_warning_content': 'str',
        'risk_warning_title': 'str'
    }

    attribute_map = {
        'is_risk_warning_enable': 'IsRiskWarningEnable',
        'risk_warning_button_text': 'RiskWarningButtonText',
        'risk_warning_content': 'RiskWarningContent',
        'risk_warning_title': 'RiskWarningTitle'
    }

    def __init__(self, is_risk_warning_enable=None, risk_warning_button_text=None, risk_warning_content=None, risk_warning_title=None, _configuration=None):  # noqa: E501
        """RiskWarningSettingForUpdateActivityBasicConfigAPIInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._is_risk_warning_enable = None
        self._risk_warning_button_text = None
        self._risk_warning_content = None
        self._risk_warning_title = None
        self.discriminator = None

        if is_risk_warning_enable is not None:
            self.is_risk_warning_enable = is_risk_warning_enable
        if risk_warning_button_text is not None:
            self.risk_warning_button_text = risk_warning_button_text
        if risk_warning_content is not None:
            self.risk_warning_content = risk_warning_content
        if risk_warning_title is not None:
            self.risk_warning_title = risk_warning_title

    @property
    def is_risk_warning_enable(self):
        """Gets the is_risk_warning_enable of this RiskWarningSettingForUpdateActivityBasicConfigAPIInput.  # noqa: E501


        :return: The is_risk_warning_enable of this RiskWarningSettingForUpdateActivityBasicConfigAPIInput.  # noqa: E501
        :rtype: int
        """
        return self._is_risk_warning_enable

    @is_risk_warning_enable.setter
    def is_risk_warning_enable(self, is_risk_warning_enable):
        """Sets the is_risk_warning_enable of this RiskWarningSettingForUpdateActivityBasicConfigAPIInput.


        :param is_risk_warning_enable: The is_risk_warning_enable of this RiskWarningSettingForUpdateActivityBasicConfigAPIInput.  # noqa: E501
        :type: int
        """

        self._is_risk_warning_enable = is_risk_warning_enable

    @property
    def risk_warning_button_text(self):
        """Gets the risk_warning_button_text of this RiskWarningSettingForUpdateActivityBasicConfigAPIInput.  # noqa: E501


        :return: The risk_warning_button_text of this RiskWarningSettingForUpdateActivityBasicConfigAPIInput.  # noqa: E501
        :rtype: str
        """
        return self._risk_warning_button_text

    @risk_warning_button_text.setter
    def risk_warning_button_text(self, risk_warning_button_text):
        """Sets the risk_warning_button_text of this RiskWarningSettingForUpdateActivityBasicConfigAPIInput.


        :param risk_warning_button_text: The risk_warning_button_text of this RiskWarningSettingForUpdateActivityBasicConfigAPIInput.  # noqa: E501
        :type: str
        """

        self._risk_warning_button_text = risk_warning_button_text

    @property
    def risk_warning_content(self):
        """Gets the risk_warning_content of this RiskWarningSettingForUpdateActivityBasicConfigAPIInput.  # noqa: E501


        :return: The risk_warning_content of this RiskWarningSettingForUpdateActivityBasicConfigAPIInput.  # noqa: E501
        :rtype: str
        """
        return self._risk_warning_content

    @risk_warning_content.setter
    def risk_warning_content(self, risk_warning_content):
        """Sets the risk_warning_content of this RiskWarningSettingForUpdateActivityBasicConfigAPIInput.


        :param risk_warning_content: The risk_warning_content of this RiskWarningSettingForUpdateActivityBasicConfigAPIInput.  # noqa: E501
        :type: str
        """

        self._risk_warning_content = risk_warning_content

    @property
    def risk_warning_title(self):
        """Gets the risk_warning_title of this RiskWarningSettingForUpdateActivityBasicConfigAPIInput.  # noqa: E501


        :return: The risk_warning_title of this RiskWarningSettingForUpdateActivityBasicConfigAPIInput.  # noqa: E501
        :rtype: str
        """
        return self._risk_warning_title

    @risk_warning_title.setter
    def risk_warning_title(self, risk_warning_title):
        """Sets the risk_warning_title of this RiskWarningSettingForUpdateActivityBasicConfigAPIInput.


        :param risk_warning_title: The risk_warning_title of this RiskWarningSettingForUpdateActivityBasicConfigAPIInput.  # noqa: E501
        :type: str
        """

        self._risk_warning_title = risk_warning_title

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
        if issubclass(RiskWarningSettingForUpdateActivityBasicConfigAPIInput, dict):
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
        if not isinstance(other, RiskWarningSettingForUpdateActivityBasicConfigAPIInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RiskWarningSettingForUpdateActivityBasicConfigAPIInput):
            return True

        return self.to_dict() != other.to_dict()
