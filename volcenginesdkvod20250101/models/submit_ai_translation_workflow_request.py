# coding: utf-8

"""
    vod20250101

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class SubmitAITranslationWorkflowRequest(object):
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
        'operator_config': 'OperatorConfigForSubmitAITranslationWorkflowInput',
        'space_name': 'str',
        'translation_config': 'TranslationConfigForSubmitAITranslationWorkflowInput',
        'vid': 'str'
    }

    attribute_map = {
        'operator_config': 'OperatorConfig',
        'space_name': 'SpaceName',
        'translation_config': 'TranslationConfig',
        'vid': 'Vid'
    }

    def __init__(self, operator_config=None, space_name=None, translation_config=None, vid=None, _configuration=None):  # noqa: E501
        """SubmitAITranslationWorkflowRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._operator_config = None
        self._space_name = None
        self._translation_config = None
        self._vid = None
        self.discriminator = None

        if operator_config is not None:
            self.operator_config = operator_config
        self.space_name = space_name
        if translation_config is not None:
            self.translation_config = translation_config
        self.vid = vid

    @property
    def operator_config(self):
        """Gets the operator_config of this SubmitAITranslationWorkflowRequest.  # noqa: E501


        :return: The operator_config of this SubmitAITranslationWorkflowRequest.  # noqa: E501
        :rtype: OperatorConfigForSubmitAITranslationWorkflowInput
        """
        return self._operator_config

    @operator_config.setter
    def operator_config(self, operator_config):
        """Sets the operator_config of this SubmitAITranslationWorkflowRequest.


        :param operator_config: The operator_config of this SubmitAITranslationWorkflowRequest.  # noqa: E501
        :type: OperatorConfigForSubmitAITranslationWorkflowInput
        """

        self._operator_config = operator_config

    @property
    def space_name(self):
        """Gets the space_name of this SubmitAITranslationWorkflowRequest.  # noqa: E501


        :return: The space_name of this SubmitAITranslationWorkflowRequest.  # noqa: E501
        :rtype: str
        """
        return self._space_name

    @space_name.setter
    def space_name(self, space_name):
        """Sets the space_name of this SubmitAITranslationWorkflowRequest.


        :param space_name: The space_name of this SubmitAITranslationWorkflowRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and space_name is None:
            raise ValueError("Invalid value for `space_name`, must not be `None`")  # noqa: E501

        self._space_name = space_name

    @property
    def translation_config(self):
        """Gets the translation_config of this SubmitAITranslationWorkflowRequest.  # noqa: E501


        :return: The translation_config of this SubmitAITranslationWorkflowRequest.  # noqa: E501
        :rtype: TranslationConfigForSubmitAITranslationWorkflowInput
        """
        return self._translation_config

    @translation_config.setter
    def translation_config(self, translation_config):
        """Sets the translation_config of this SubmitAITranslationWorkflowRequest.


        :param translation_config: The translation_config of this SubmitAITranslationWorkflowRequest.  # noqa: E501
        :type: TranslationConfigForSubmitAITranslationWorkflowInput
        """

        self._translation_config = translation_config

    @property
    def vid(self):
        """Gets the vid of this SubmitAITranslationWorkflowRequest.  # noqa: E501


        :return: The vid of this SubmitAITranslationWorkflowRequest.  # noqa: E501
        :rtype: str
        """
        return self._vid

    @vid.setter
    def vid(self, vid):
        """Sets the vid of this SubmitAITranslationWorkflowRequest.


        :param vid: The vid of this SubmitAITranslationWorkflowRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and vid is None:
            raise ValueError("Invalid value for `vid`, must not be `None`")  # noqa: E501

        self._vid = vid

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
        if issubclass(SubmitAITranslationWorkflowRequest, dict):
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
        if not isinstance(other, SubmitAITranslationWorkflowRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SubmitAITranslationWorkflowRequest):
            return True

        return self.to_dict() != other.to_dict()
