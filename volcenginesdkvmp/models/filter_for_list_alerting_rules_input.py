# coding: utf-8

"""
    vmp

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class FilterForListAlertingRulesInput(object):
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
        'group_ids': 'list[str]',
        'ids': 'list[str]',
        'name': 'str',
        'notify_group_policy_ids': 'list[str]',
        'notify_policy_ids': 'list[str]',
        'status': 'str',
        'template_ids': 'list[str]',
        'type': 'str',
        'workspace_id': 'str'
    }

    attribute_map = {
        'group_ids': 'GroupIds',
        'ids': 'Ids',
        'name': 'Name',
        'notify_group_policy_ids': 'NotifyGroupPolicyIds',
        'notify_policy_ids': 'NotifyPolicyIds',
        'status': 'Status',
        'template_ids': 'TemplateIds',
        'type': 'Type',
        'workspace_id': 'WorkspaceId'
    }

    def __init__(self, group_ids=None, ids=None, name=None, notify_group_policy_ids=None, notify_policy_ids=None, status=None, template_ids=None, type=None, workspace_id=None, _configuration=None):  # noqa: E501
        """FilterForListAlertingRulesInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._group_ids = None
        self._ids = None
        self._name = None
        self._notify_group_policy_ids = None
        self._notify_policy_ids = None
        self._status = None
        self._template_ids = None
        self._type = None
        self._workspace_id = None
        self.discriminator = None

        if group_ids is not None:
            self.group_ids = group_ids
        if ids is not None:
            self.ids = ids
        if name is not None:
            self.name = name
        if notify_group_policy_ids is not None:
            self.notify_group_policy_ids = notify_group_policy_ids
        if notify_policy_ids is not None:
            self.notify_policy_ids = notify_policy_ids
        if status is not None:
            self.status = status
        if template_ids is not None:
            self.template_ids = template_ids
        if type is not None:
            self.type = type
        if workspace_id is not None:
            self.workspace_id = workspace_id

    @property
    def group_ids(self):
        """Gets the group_ids of this FilterForListAlertingRulesInput.  # noqa: E501


        :return: The group_ids of this FilterForListAlertingRulesInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._group_ids

    @group_ids.setter
    def group_ids(self, group_ids):
        """Sets the group_ids of this FilterForListAlertingRulesInput.


        :param group_ids: The group_ids of this FilterForListAlertingRulesInput.  # noqa: E501
        :type: list[str]
        """

        self._group_ids = group_ids

    @property
    def ids(self):
        """Gets the ids of this FilterForListAlertingRulesInput.  # noqa: E501


        :return: The ids of this FilterForListAlertingRulesInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this FilterForListAlertingRulesInput.


        :param ids: The ids of this FilterForListAlertingRulesInput.  # noqa: E501
        :type: list[str]
        """

        self._ids = ids

    @property
    def name(self):
        """Gets the name of this FilterForListAlertingRulesInput.  # noqa: E501


        :return: The name of this FilterForListAlertingRulesInput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FilterForListAlertingRulesInput.


        :param name: The name of this FilterForListAlertingRulesInput.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def notify_group_policy_ids(self):
        """Gets the notify_group_policy_ids of this FilterForListAlertingRulesInput.  # noqa: E501


        :return: The notify_group_policy_ids of this FilterForListAlertingRulesInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._notify_group_policy_ids

    @notify_group_policy_ids.setter
    def notify_group_policy_ids(self, notify_group_policy_ids):
        """Sets the notify_group_policy_ids of this FilterForListAlertingRulesInput.


        :param notify_group_policy_ids: The notify_group_policy_ids of this FilterForListAlertingRulesInput.  # noqa: E501
        :type: list[str]
        """

        self._notify_group_policy_ids = notify_group_policy_ids

    @property
    def notify_policy_ids(self):
        """Gets the notify_policy_ids of this FilterForListAlertingRulesInput.  # noqa: E501


        :return: The notify_policy_ids of this FilterForListAlertingRulesInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._notify_policy_ids

    @notify_policy_ids.setter
    def notify_policy_ids(self, notify_policy_ids):
        """Sets the notify_policy_ids of this FilterForListAlertingRulesInput.


        :param notify_policy_ids: The notify_policy_ids of this FilterForListAlertingRulesInput.  # noqa: E501
        :type: list[str]
        """

        self._notify_policy_ids = notify_policy_ids

    @property
    def status(self):
        """Gets the status of this FilterForListAlertingRulesInput.  # noqa: E501


        :return: The status of this FilterForListAlertingRulesInput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this FilterForListAlertingRulesInput.


        :param status: The status of this FilterForListAlertingRulesInput.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def template_ids(self):
        """Gets the template_ids of this FilterForListAlertingRulesInput.  # noqa: E501


        :return: The template_ids of this FilterForListAlertingRulesInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._template_ids

    @template_ids.setter
    def template_ids(self, template_ids):
        """Sets the template_ids of this FilterForListAlertingRulesInput.


        :param template_ids: The template_ids of this FilterForListAlertingRulesInput.  # noqa: E501
        :type: list[str]
        """

        self._template_ids = template_ids

    @property
    def type(self):
        """Gets the type of this FilterForListAlertingRulesInput.  # noqa: E501


        :return: The type of this FilterForListAlertingRulesInput.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FilterForListAlertingRulesInput.


        :param type: The type of this FilterForListAlertingRulesInput.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def workspace_id(self):
        """Gets the workspace_id of this FilterForListAlertingRulesInput.  # noqa: E501


        :return: The workspace_id of this FilterForListAlertingRulesInput.  # noqa: E501
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this FilterForListAlertingRulesInput.


        :param workspace_id: The workspace_id of this FilterForListAlertingRulesInput.  # noqa: E501
        :type: str
        """

        self._workspace_id = workspace_id

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
        if issubclass(FilterForListAlertingRulesInput, dict):
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
        if not isinstance(other, FilterForListAlertingRulesInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FilterForListAlertingRulesInput):
            return True

        return self.to_dict() != other.to_dict()
