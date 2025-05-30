# coding: utf-8

"""
    ml_platform20240701

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class AutoCompactGPUResourceRuleForCreateResourceQueueInput(object):
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
        'affected_workload_types': 'list[str]',
        'cron_specs': 'list[CronSpecForCreateResourceQueueInput]',
        'enabled': 'bool',
        'id': 'str',
        'on_unschedulable': 'bool'
    }

    attribute_map = {
        'affected_workload_types': 'AffectedWorkloadTypes',
        'cron_specs': 'CronSpecs',
        'enabled': 'Enabled',
        'id': 'Id',
        'on_unschedulable': 'OnUnschedulable'
    }

    def __init__(self, affected_workload_types=None, cron_specs=None, enabled=None, id=None, on_unschedulable=None, _configuration=None):  # noqa: E501
        """AutoCompactGPUResourceRuleForCreateResourceQueueInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._affected_workload_types = None
        self._cron_specs = None
        self._enabled = None
        self._id = None
        self._on_unschedulable = None
        self.discriminator = None

        if affected_workload_types is not None:
            self.affected_workload_types = affected_workload_types
        if cron_specs is not None:
            self.cron_specs = cron_specs
        if enabled is not None:
            self.enabled = enabled
        if id is not None:
            self.id = id
        if on_unschedulable is not None:
            self.on_unschedulable = on_unschedulable

    @property
    def affected_workload_types(self):
        """Gets the affected_workload_types of this AutoCompactGPUResourceRuleForCreateResourceQueueInput.  # noqa: E501


        :return: The affected_workload_types of this AutoCompactGPUResourceRuleForCreateResourceQueueInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._affected_workload_types

    @affected_workload_types.setter
    def affected_workload_types(self, affected_workload_types):
        """Sets the affected_workload_types of this AutoCompactGPUResourceRuleForCreateResourceQueueInput.


        :param affected_workload_types: The affected_workload_types of this AutoCompactGPUResourceRuleForCreateResourceQueueInput.  # noqa: E501
        :type: list[str]
        """

        self._affected_workload_types = affected_workload_types

    @property
    def cron_specs(self):
        """Gets the cron_specs of this AutoCompactGPUResourceRuleForCreateResourceQueueInput.  # noqa: E501


        :return: The cron_specs of this AutoCompactGPUResourceRuleForCreateResourceQueueInput.  # noqa: E501
        :rtype: list[CronSpecForCreateResourceQueueInput]
        """
        return self._cron_specs

    @cron_specs.setter
    def cron_specs(self, cron_specs):
        """Sets the cron_specs of this AutoCompactGPUResourceRuleForCreateResourceQueueInput.


        :param cron_specs: The cron_specs of this AutoCompactGPUResourceRuleForCreateResourceQueueInput.  # noqa: E501
        :type: list[CronSpecForCreateResourceQueueInput]
        """

        self._cron_specs = cron_specs

    @property
    def enabled(self):
        """Gets the enabled of this AutoCompactGPUResourceRuleForCreateResourceQueueInput.  # noqa: E501


        :return: The enabled of this AutoCompactGPUResourceRuleForCreateResourceQueueInput.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this AutoCompactGPUResourceRuleForCreateResourceQueueInput.


        :param enabled: The enabled of this AutoCompactGPUResourceRuleForCreateResourceQueueInput.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def id(self):
        """Gets the id of this AutoCompactGPUResourceRuleForCreateResourceQueueInput.  # noqa: E501


        :return: The id of this AutoCompactGPUResourceRuleForCreateResourceQueueInput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AutoCompactGPUResourceRuleForCreateResourceQueueInput.


        :param id: The id of this AutoCompactGPUResourceRuleForCreateResourceQueueInput.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def on_unschedulable(self):
        """Gets the on_unschedulable of this AutoCompactGPUResourceRuleForCreateResourceQueueInput.  # noqa: E501


        :return: The on_unschedulable of this AutoCompactGPUResourceRuleForCreateResourceQueueInput.  # noqa: E501
        :rtype: bool
        """
        return self._on_unschedulable

    @on_unschedulable.setter
    def on_unschedulable(self, on_unschedulable):
        """Sets the on_unschedulable of this AutoCompactGPUResourceRuleForCreateResourceQueueInput.


        :param on_unschedulable: The on_unschedulable of this AutoCompactGPUResourceRuleForCreateResourceQueueInput.  # noqa: E501
        :type: bool
        """

        self._on_unschedulable = on_unschedulable

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
        if issubclass(AutoCompactGPUResourceRuleForCreateResourceQueueInput, dict):
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
        if not isinstance(other, AutoCompactGPUResourceRuleForCreateResourceQueueInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AutoCompactGPUResourceRuleForCreateResourceQueueInput):
            return True

        return self.to_dict() != other.to_dict()
