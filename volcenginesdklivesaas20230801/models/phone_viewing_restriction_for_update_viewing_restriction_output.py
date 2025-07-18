# coding: utf-8

"""
    livesaas20230801

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class PhoneViewingRestrictionForUpdateViewingRestrictionOutput(object):
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
        'enable_sms': 'bool',
        'enable_trial': 'bool',
        'is_phone_list_mode': 'bool',
        'prompt': 'str',
        'trial_time': 'int'
    }

    attribute_map = {
        'enable_sms': 'EnableSMS',
        'enable_trial': 'EnableTrial',
        'is_phone_list_mode': 'IsPhoneListMode',
        'prompt': 'Prompt',
        'trial_time': 'TrialTime'
    }

    def __init__(self, enable_sms=None, enable_trial=None, is_phone_list_mode=None, prompt=None, trial_time=None, _configuration=None):  # noqa: E501
        """PhoneViewingRestrictionForUpdateViewingRestrictionOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._enable_sms = None
        self._enable_trial = None
        self._is_phone_list_mode = None
        self._prompt = None
        self._trial_time = None
        self.discriminator = None

        if enable_sms is not None:
            self.enable_sms = enable_sms
        if enable_trial is not None:
            self.enable_trial = enable_trial
        if is_phone_list_mode is not None:
            self.is_phone_list_mode = is_phone_list_mode
        if prompt is not None:
            self.prompt = prompt
        if trial_time is not None:
            self.trial_time = trial_time

    @property
    def enable_sms(self):
        """Gets the enable_sms of this PhoneViewingRestrictionForUpdateViewingRestrictionOutput.  # noqa: E501


        :return: The enable_sms of this PhoneViewingRestrictionForUpdateViewingRestrictionOutput.  # noqa: E501
        :rtype: bool
        """
        return self._enable_sms

    @enable_sms.setter
    def enable_sms(self, enable_sms):
        """Sets the enable_sms of this PhoneViewingRestrictionForUpdateViewingRestrictionOutput.


        :param enable_sms: The enable_sms of this PhoneViewingRestrictionForUpdateViewingRestrictionOutput.  # noqa: E501
        :type: bool
        """

        self._enable_sms = enable_sms

    @property
    def enable_trial(self):
        """Gets the enable_trial of this PhoneViewingRestrictionForUpdateViewingRestrictionOutput.  # noqa: E501


        :return: The enable_trial of this PhoneViewingRestrictionForUpdateViewingRestrictionOutput.  # noqa: E501
        :rtype: bool
        """
        return self._enable_trial

    @enable_trial.setter
    def enable_trial(self, enable_trial):
        """Sets the enable_trial of this PhoneViewingRestrictionForUpdateViewingRestrictionOutput.


        :param enable_trial: The enable_trial of this PhoneViewingRestrictionForUpdateViewingRestrictionOutput.  # noqa: E501
        :type: bool
        """

        self._enable_trial = enable_trial

    @property
    def is_phone_list_mode(self):
        """Gets the is_phone_list_mode of this PhoneViewingRestrictionForUpdateViewingRestrictionOutput.  # noqa: E501


        :return: The is_phone_list_mode of this PhoneViewingRestrictionForUpdateViewingRestrictionOutput.  # noqa: E501
        :rtype: bool
        """
        return self._is_phone_list_mode

    @is_phone_list_mode.setter
    def is_phone_list_mode(self, is_phone_list_mode):
        """Sets the is_phone_list_mode of this PhoneViewingRestrictionForUpdateViewingRestrictionOutput.


        :param is_phone_list_mode: The is_phone_list_mode of this PhoneViewingRestrictionForUpdateViewingRestrictionOutput.  # noqa: E501
        :type: bool
        """

        self._is_phone_list_mode = is_phone_list_mode

    @property
    def prompt(self):
        """Gets the prompt of this PhoneViewingRestrictionForUpdateViewingRestrictionOutput.  # noqa: E501


        :return: The prompt of this PhoneViewingRestrictionForUpdateViewingRestrictionOutput.  # noqa: E501
        :rtype: str
        """
        return self._prompt

    @prompt.setter
    def prompt(self, prompt):
        """Sets the prompt of this PhoneViewingRestrictionForUpdateViewingRestrictionOutput.


        :param prompt: The prompt of this PhoneViewingRestrictionForUpdateViewingRestrictionOutput.  # noqa: E501
        :type: str
        """

        self._prompt = prompt

    @property
    def trial_time(self):
        """Gets the trial_time of this PhoneViewingRestrictionForUpdateViewingRestrictionOutput.  # noqa: E501


        :return: The trial_time of this PhoneViewingRestrictionForUpdateViewingRestrictionOutput.  # noqa: E501
        :rtype: int
        """
        return self._trial_time

    @trial_time.setter
    def trial_time(self, trial_time):
        """Sets the trial_time of this PhoneViewingRestrictionForUpdateViewingRestrictionOutput.


        :param trial_time: The trial_time of this PhoneViewingRestrictionForUpdateViewingRestrictionOutput.  # noqa: E501
        :type: int
        """

        self._trial_time = trial_time

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
        if issubclass(PhoneViewingRestrictionForUpdateViewingRestrictionOutput, dict):
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
        if not isinstance(other, PhoneViewingRestrictionForUpdateViewingRestrictionOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PhoneViewingRestrictionForUpdateViewingRestrictionOutput):
            return True

        return self.to_dict() != other.to_dict()
