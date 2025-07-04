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


class CreateBotAnalyseProtectRuleRequest(object):
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
        'accurate_group': 'list[AccurateGroupForCreateBotAnalyseProtectRuleInput]',
        'action_after_verification': 'int',
        'action_type': 'int',
        'effect_time': 'int',
        'enable': 'int',
        'exemption_time': 'int',
        'field': 'str',
        'host': 'str',
        'name': 'str',
        'path': 'str',
        'path_threshold': 'int',
        'project_name': 'str',
        'rule_priority': 'int',
        'single_proportion': 'float',
        'single_threshold': 'int',
        'statistical_duration': 'int',
        'statistical_type': 'int'
    }

    attribute_map = {
        'accurate_group': 'AccurateGroup',
        'action_after_verification': 'ActionAfterVerification',
        'action_type': 'ActionType',
        'effect_time': 'EffectTime',
        'enable': 'Enable',
        'exemption_time': 'ExemptionTime',
        'field': 'Field',
        'host': 'Host',
        'name': 'Name',
        'path': 'Path',
        'path_threshold': 'PathThreshold',
        'project_name': 'ProjectName',
        'rule_priority': 'RulePriority',
        'single_proportion': 'SingleProportion',
        'single_threshold': 'SingleThreshold',
        'statistical_duration': 'StatisticalDuration',
        'statistical_type': 'StatisticalType'
    }

    def __init__(self, accurate_group=None, action_after_verification=None, action_type=None, effect_time=None, enable=None, exemption_time=None, field=None, host=None, name=None, path=None, path_threshold=None, project_name=None, rule_priority=None, single_proportion=None, single_threshold=None, statistical_duration=None, statistical_type=None, _configuration=None):  # noqa: E501
        """CreateBotAnalyseProtectRuleRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._accurate_group = None
        self._action_after_verification = None
        self._action_type = None
        self._effect_time = None
        self._enable = None
        self._exemption_time = None
        self._field = None
        self._host = None
        self._name = None
        self._path = None
        self._path_threshold = None
        self._project_name = None
        self._rule_priority = None
        self._single_proportion = None
        self._single_threshold = None
        self._statistical_duration = None
        self._statistical_type = None
        self.discriminator = None

        if accurate_group is not None:
            self.accurate_group = accurate_group
        if action_after_verification is not None:
            self.action_after_verification = action_after_verification
        self.action_type = action_type
        self.effect_time = effect_time
        self.enable = enable
        if exemption_time is not None:
            self.exemption_time = exemption_time
        self.field = field
        self.host = host
        self.name = name
        self.path = path
        if path_threshold is not None:
            self.path_threshold = path_threshold
        if project_name is not None:
            self.project_name = project_name
        self.rule_priority = rule_priority
        if single_proportion is not None:
            self.single_proportion = single_proportion
        self.single_threshold = single_threshold
        self.statistical_duration = statistical_duration
        self.statistical_type = statistical_type

    @property
    def accurate_group(self):
        """Gets the accurate_group of this CreateBotAnalyseProtectRuleRequest.  # noqa: E501


        :return: The accurate_group of this CreateBotAnalyseProtectRuleRequest.  # noqa: E501
        :rtype: list[AccurateGroupForCreateBotAnalyseProtectRuleInput]
        """
        return self._accurate_group

    @accurate_group.setter
    def accurate_group(self, accurate_group):
        """Sets the accurate_group of this CreateBotAnalyseProtectRuleRequest.


        :param accurate_group: The accurate_group of this CreateBotAnalyseProtectRuleRequest.  # noqa: E501
        :type: list[AccurateGroupForCreateBotAnalyseProtectRuleInput]
        """

        self._accurate_group = accurate_group

    @property
    def action_after_verification(self):
        """Gets the action_after_verification of this CreateBotAnalyseProtectRuleRequest.  # noqa: E501


        :return: The action_after_verification of this CreateBotAnalyseProtectRuleRequest.  # noqa: E501
        :rtype: int
        """
        return self._action_after_verification

    @action_after_verification.setter
    def action_after_verification(self, action_after_verification):
        """Sets the action_after_verification of this CreateBotAnalyseProtectRuleRequest.


        :param action_after_verification: The action_after_verification of this CreateBotAnalyseProtectRuleRequest.  # noqa: E501
        :type: int
        """

        self._action_after_verification = action_after_verification

    @property
    def action_type(self):
        """Gets the action_type of this CreateBotAnalyseProtectRuleRequest.  # noqa: E501


        :return: The action_type of this CreateBotAnalyseProtectRuleRequest.  # noqa: E501
        :rtype: int
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """Sets the action_type of this CreateBotAnalyseProtectRuleRequest.


        :param action_type: The action_type of this CreateBotAnalyseProtectRuleRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and action_type is None:
            raise ValueError("Invalid value for `action_type`, must not be `None`")  # noqa: E501

        self._action_type = action_type

    @property
    def effect_time(self):
        """Gets the effect_time of this CreateBotAnalyseProtectRuleRequest.  # noqa: E501


        :return: The effect_time of this CreateBotAnalyseProtectRuleRequest.  # noqa: E501
        :rtype: int
        """
        return self._effect_time

    @effect_time.setter
    def effect_time(self, effect_time):
        """Sets the effect_time of this CreateBotAnalyseProtectRuleRequest.


        :param effect_time: The effect_time of this CreateBotAnalyseProtectRuleRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and effect_time is None:
            raise ValueError("Invalid value for `effect_time`, must not be `None`")  # noqa: E501

        self._effect_time = effect_time

    @property
    def enable(self):
        """Gets the enable of this CreateBotAnalyseProtectRuleRequest.  # noqa: E501


        :return: The enable of this CreateBotAnalyseProtectRuleRequest.  # noqa: E501
        :rtype: int
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this CreateBotAnalyseProtectRuleRequest.


        :param enable: The enable of this CreateBotAnalyseProtectRuleRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and enable is None:
            raise ValueError("Invalid value for `enable`, must not be `None`")  # noqa: E501

        self._enable = enable

    @property
    def exemption_time(self):
        """Gets the exemption_time of this CreateBotAnalyseProtectRuleRequest.  # noqa: E501


        :return: The exemption_time of this CreateBotAnalyseProtectRuleRequest.  # noqa: E501
        :rtype: int
        """
        return self._exemption_time

    @exemption_time.setter
    def exemption_time(self, exemption_time):
        """Sets the exemption_time of this CreateBotAnalyseProtectRuleRequest.


        :param exemption_time: The exemption_time of this CreateBotAnalyseProtectRuleRequest.  # noqa: E501
        :type: int
        """

        self._exemption_time = exemption_time

    @property
    def field(self):
        """Gets the field of this CreateBotAnalyseProtectRuleRequest.  # noqa: E501


        :return: The field of this CreateBotAnalyseProtectRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this CreateBotAnalyseProtectRuleRequest.


        :param field: The field of this CreateBotAnalyseProtectRuleRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and field is None:
            raise ValueError("Invalid value for `field`, must not be `None`")  # noqa: E501

        self._field = field

    @property
    def host(self):
        """Gets the host of this CreateBotAnalyseProtectRuleRequest.  # noqa: E501


        :return: The host of this CreateBotAnalyseProtectRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this CreateBotAnalyseProtectRuleRequest.


        :param host: The host of this CreateBotAnalyseProtectRuleRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and host is None:
            raise ValueError("Invalid value for `host`, must not be `None`")  # noqa: E501

        self._host = host

    @property
    def name(self):
        """Gets the name of this CreateBotAnalyseProtectRuleRequest.  # noqa: E501


        :return: The name of this CreateBotAnalyseProtectRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateBotAnalyseProtectRuleRequest.


        :param name: The name of this CreateBotAnalyseProtectRuleRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def path(self):
        """Gets the path of this CreateBotAnalyseProtectRuleRequest.  # noqa: E501


        :return: The path of this CreateBotAnalyseProtectRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this CreateBotAnalyseProtectRuleRequest.


        :param path: The path of this CreateBotAnalyseProtectRuleRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def path_threshold(self):
        """Gets the path_threshold of this CreateBotAnalyseProtectRuleRequest.  # noqa: E501


        :return: The path_threshold of this CreateBotAnalyseProtectRuleRequest.  # noqa: E501
        :rtype: int
        """
        return self._path_threshold

    @path_threshold.setter
    def path_threshold(self, path_threshold):
        """Sets the path_threshold of this CreateBotAnalyseProtectRuleRequest.


        :param path_threshold: The path_threshold of this CreateBotAnalyseProtectRuleRequest.  # noqa: E501
        :type: int
        """

        self._path_threshold = path_threshold

    @property
    def project_name(self):
        """Gets the project_name of this CreateBotAnalyseProtectRuleRequest.  # noqa: E501


        :return: The project_name of this CreateBotAnalyseProtectRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this CreateBotAnalyseProtectRuleRequest.


        :param project_name: The project_name of this CreateBotAnalyseProtectRuleRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def rule_priority(self):
        """Gets the rule_priority of this CreateBotAnalyseProtectRuleRequest.  # noqa: E501


        :return: The rule_priority of this CreateBotAnalyseProtectRuleRequest.  # noqa: E501
        :rtype: int
        """
        return self._rule_priority

    @rule_priority.setter
    def rule_priority(self, rule_priority):
        """Sets the rule_priority of this CreateBotAnalyseProtectRuleRequest.


        :param rule_priority: The rule_priority of this CreateBotAnalyseProtectRuleRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and rule_priority is None:
            raise ValueError("Invalid value for `rule_priority`, must not be `None`")  # noqa: E501

        self._rule_priority = rule_priority

    @property
    def single_proportion(self):
        """Gets the single_proportion of this CreateBotAnalyseProtectRuleRequest.  # noqa: E501


        :return: The single_proportion of this CreateBotAnalyseProtectRuleRequest.  # noqa: E501
        :rtype: float
        """
        return self._single_proportion

    @single_proportion.setter
    def single_proportion(self, single_proportion):
        """Sets the single_proportion of this CreateBotAnalyseProtectRuleRequest.


        :param single_proportion: The single_proportion of this CreateBotAnalyseProtectRuleRequest.  # noqa: E501
        :type: float
        """

        self._single_proportion = single_proportion

    @property
    def single_threshold(self):
        """Gets the single_threshold of this CreateBotAnalyseProtectRuleRequest.  # noqa: E501


        :return: The single_threshold of this CreateBotAnalyseProtectRuleRequest.  # noqa: E501
        :rtype: int
        """
        return self._single_threshold

    @single_threshold.setter
    def single_threshold(self, single_threshold):
        """Sets the single_threshold of this CreateBotAnalyseProtectRuleRequest.


        :param single_threshold: The single_threshold of this CreateBotAnalyseProtectRuleRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and single_threshold is None:
            raise ValueError("Invalid value for `single_threshold`, must not be `None`")  # noqa: E501

        self._single_threshold = single_threshold

    @property
    def statistical_duration(self):
        """Gets the statistical_duration of this CreateBotAnalyseProtectRuleRequest.  # noqa: E501


        :return: The statistical_duration of this CreateBotAnalyseProtectRuleRequest.  # noqa: E501
        :rtype: int
        """
        return self._statistical_duration

    @statistical_duration.setter
    def statistical_duration(self, statistical_duration):
        """Sets the statistical_duration of this CreateBotAnalyseProtectRuleRequest.


        :param statistical_duration: The statistical_duration of this CreateBotAnalyseProtectRuleRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and statistical_duration is None:
            raise ValueError("Invalid value for `statistical_duration`, must not be `None`")  # noqa: E501

        self._statistical_duration = statistical_duration

    @property
    def statistical_type(self):
        """Gets the statistical_type of this CreateBotAnalyseProtectRuleRequest.  # noqa: E501


        :return: The statistical_type of this CreateBotAnalyseProtectRuleRequest.  # noqa: E501
        :rtype: int
        """
        return self._statistical_type

    @statistical_type.setter
    def statistical_type(self, statistical_type):
        """Sets the statistical_type of this CreateBotAnalyseProtectRuleRequest.


        :param statistical_type: The statistical_type of this CreateBotAnalyseProtectRuleRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and statistical_type is None:
            raise ValueError("Invalid value for `statistical_type`, must not be `None`")  # noqa: E501

        self._statistical_type = statistical_type

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
        if issubclass(CreateBotAnalyseProtectRuleRequest, dict):
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
        if not isinstance(other, CreateBotAnalyseProtectRuleRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateBotAnalyseProtectRuleRequest):
            return True

        return self.to_dict() != other.to_dict()
