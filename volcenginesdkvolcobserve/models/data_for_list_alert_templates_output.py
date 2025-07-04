# coding: utf-8

"""
    volc_observe

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DataForListAlertTemplatesOutput(object):
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
        'applied_project_name': 'str',
        'created_at': 'str',
        'description': 'str',
        'id': 'str',
        'name': 'str',
        'no_data': 'NoDataForListAlertTemplatesOutput',
        'notify_mode': 'str',
        'object_groups': 'list[ObjectGroupForListAlertTemplatesOutput]',
        'recovery_notify': 'RecoveryNotifyForListAlertTemplatesOutput',
        'silence_time': 'int',
        'template_rules': 'list[TemplateRuleForListAlertTemplatesOutput]',
        'updated_at': 'str'
    }

    attribute_map = {
        'applied_project_name': 'AppliedProjectName',
        'created_at': 'CreatedAt',
        'description': 'Description',
        'id': 'Id',
        'name': 'Name',
        'no_data': 'NoData',
        'notify_mode': 'NotifyMode',
        'object_groups': 'ObjectGroups',
        'recovery_notify': 'RecoveryNotify',
        'silence_time': 'SilenceTime',
        'template_rules': 'TemplateRules',
        'updated_at': 'UpdatedAt'
    }

    def __init__(self, applied_project_name=None, created_at=None, description=None, id=None, name=None, no_data=None, notify_mode=None, object_groups=None, recovery_notify=None, silence_time=None, template_rules=None, updated_at=None, _configuration=None):  # noqa: E501
        """DataForListAlertTemplatesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._applied_project_name = None
        self._created_at = None
        self._description = None
        self._id = None
        self._name = None
        self._no_data = None
        self._notify_mode = None
        self._object_groups = None
        self._recovery_notify = None
        self._silence_time = None
        self._template_rules = None
        self._updated_at = None
        self.discriminator = None

        if applied_project_name is not None:
            self.applied_project_name = applied_project_name
        if created_at is not None:
            self.created_at = created_at
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if no_data is not None:
            self.no_data = no_data
        if notify_mode is not None:
            self.notify_mode = notify_mode
        if object_groups is not None:
            self.object_groups = object_groups
        if recovery_notify is not None:
            self.recovery_notify = recovery_notify
        if silence_time is not None:
            self.silence_time = silence_time
        if template_rules is not None:
            self.template_rules = template_rules
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def applied_project_name(self):
        """Gets the applied_project_name of this DataForListAlertTemplatesOutput.  # noqa: E501


        :return: The applied_project_name of this DataForListAlertTemplatesOutput.  # noqa: E501
        :rtype: str
        """
        return self._applied_project_name

    @applied_project_name.setter
    def applied_project_name(self, applied_project_name):
        """Sets the applied_project_name of this DataForListAlertTemplatesOutput.


        :param applied_project_name: The applied_project_name of this DataForListAlertTemplatesOutput.  # noqa: E501
        :type: str
        """

        self._applied_project_name = applied_project_name

    @property
    def created_at(self):
        """Gets the created_at of this DataForListAlertTemplatesOutput.  # noqa: E501


        :return: The created_at of this DataForListAlertTemplatesOutput.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this DataForListAlertTemplatesOutput.


        :param created_at: The created_at of this DataForListAlertTemplatesOutput.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def description(self):
        """Gets the description of this DataForListAlertTemplatesOutput.  # noqa: E501


        :return: The description of this DataForListAlertTemplatesOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DataForListAlertTemplatesOutput.


        :param description: The description of this DataForListAlertTemplatesOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this DataForListAlertTemplatesOutput.  # noqa: E501


        :return: The id of this DataForListAlertTemplatesOutput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DataForListAlertTemplatesOutput.


        :param id: The id of this DataForListAlertTemplatesOutput.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this DataForListAlertTemplatesOutput.  # noqa: E501


        :return: The name of this DataForListAlertTemplatesOutput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DataForListAlertTemplatesOutput.


        :param name: The name of this DataForListAlertTemplatesOutput.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def no_data(self):
        """Gets the no_data of this DataForListAlertTemplatesOutput.  # noqa: E501


        :return: The no_data of this DataForListAlertTemplatesOutput.  # noqa: E501
        :rtype: NoDataForListAlertTemplatesOutput
        """
        return self._no_data

    @no_data.setter
    def no_data(self, no_data):
        """Sets the no_data of this DataForListAlertTemplatesOutput.


        :param no_data: The no_data of this DataForListAlertTemplatesOutput.  # noqa: E501
        :type: NoDataForListAlertTemplatesOutput
        """

        self._no_data = no_data

    @property
    def notify_mode(self):
        """Gets the notify_mode of this DataForListAlertTemplatesOutput.  # noqa: E501


        :return: The notify_mode of this DataForListAlertTemplatesOutput.  # noqa: E501
        :rtype: str
        """
        return self._notify_mode

    @notify_mode.setter
    def notify_mode(self, notify_mode):
        """Sets the notify_mode of this DataForListAlertTemplatesOutput.


        :param notify_mode: The notify_mode of this DataForListAlertTemplatesOutput.  # noqa: E501
        :type: str
        """

        self._notify_mode = notify_mode

    @property
    def object_groups(self):
        """Gets the object_groups of this DataForListAlertTemplatesOutput.  # noqa: E501


        :return: The object_groups of this DataForListAlertTemplatesOutput.  # noqa: E501
        :rtype: list[ObjectGroupForListAlertTemplatesOutput]
        """
        return self._object_groups

    @object_groups.setter
    def object_groups(self, object_groups):
        """Sets the object_groups of this DataForListAlertTemplatesOutput.


        :param object_groups: The object_groups of this DataForListAlertTemplatesOutput.  # noqa: E501
        :type: list[ObjectGroupForListAlertTemplatesOutput]
        """

        self._object_groups = object_groups

    @property
    def recovery_notify(self):
        """Gets the recovery_notify of this DataForListAlertTemplatesOutput.  # noqa: E501


        :return: The recovery_notify of this DataForListAlertTemplatesOutput.  # noqa: E501
        :rtype: RecoveryNotifyForListAlertTemplatesOutput
        """
        return self._recovery_notify

    @recovery_notify.setter
    def recovery_notify(self, recovery_notify):
        """Sets the recovery_notify of this DataForListAlertTemplatesOutput.


        :param recovery_notify: The recovery_notify of this DataForListAlertTemplatesOutput.  # noqa: E501
        :type: RecoveryNotifyForListAlertTemplatesOutput
        """

        self._recovery_notify = recovery_notify

    @property
    def silence_time(self):
        """Gets the silence_time of this DataForListAlertTemplatesOutput.  # noqa: E501


        :return: The silence_time of this DataForListAlertTemplatesOutput.  # noqa: E501
        :rtype: int
        """
        return self._silence_time

    @silence_time.setter
    def silence_time(self, silence_time):
        """Sets the silence_time of this DataForListAlertTemplatesOutput.


        :param silence_time: The silence_time of this DataForListAlertTemplatesOutput.  # noqa: E501
        :type: int
        """

        self._silence_time = silence_time

    @property
    def template_rules(self):
        """Gets the template_rules of this DataForListAlertTemplatesOutput.  # noqa: E501


        :return: The template_rules of this DataForListAlertTemplatesOutput.  # noqa: E501
        :rtype: list[TemplateRuleForListAlertTemplatesOutput]
        """
        return self._template_rules

    @template_rules.setter
    def template_rules(self, template_rules):
        """Sets the template_rules of this DataForListAlertTemplatesOutput.


        :param template_rules: The template_rules of this DataForListAlertTemplatesOutput.  # noqa: E501
        :type: list[TemplateRuleForListAlertTemplatesOutput]
        """

        self._template_rules = template_rules

    @property
    def updated_at(self):
        """Gets the updated_at of this DataForListAlertTemplatesOutput.  # noqa: E501


        :return: The updated_at of this DataForListAlertTemplatesOutput.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this DataForListAlertTemplatesOutput.


        :param updated_at: The updated_at of this DataForListAlertTemplatesOutput.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

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
        if issubclass(DataForListAlertTemplatesOutput, dict):
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
        if not isinstance(other, DataForListAlertTemplatesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataForListAlertTemplatesOutput):
            return True

        return self.to_dict() != other.to_dict()
