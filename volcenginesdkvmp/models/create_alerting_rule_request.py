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


class CreateAlertingRuleRequest(object):
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
        'annotations': 'list[AnnotationForCreateAlertingRuleInput]',
        'description': 'str',
        'labels': 'list[LabelForCreateAlertingRuleInput]',
        'levels': 'list[LevelForCreateAlertingRuleInput]',
        'name': 'str',
        'notify_group_policy_id': 'str',
        'notify_policy_id': 'str',
        'query': 'QueryForCreateAlertingRuleInput',
        'type': 'str'
    }

    attribute_map = {
        'annotations': 'Annotations',
        'description': 'Description',
        'labels': 'Labels',
        'levels': 'Levels',
        'name': 'Name',
        'notify_group_policy_id': 'NotifyGroupPolicyId',
        'notify_policy_id': 'NotifyPolicyId',
        'query': 'Query',
        'type': 'Type'
    }

    def __init__(self, annotations=None, description=None, labels=None, levels=None, name=None, notify_group_policy_id=None, notify_policy_id=None, query=None, type=None, _configuration=None):  # noqa: E501
        """CreateAlertingRuleRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._annotations = None
        self._description = None
        self._labels = None
        self._levels = None
        self._name = None
        self._notify_group_policy_id = None
        self._notify_policy_id = None
        self._query = None
        self._type = None
        self.discriminator = None

        if annotations is not None:
            self.annotations = annotations
        if description is not None:
            self.description = description
        if labels is not None:
            self.labels = labels
        if levels is not None:
            self.levels = levels
        self.name = name
        self.notify_group_policy_id = notify_group_policy_id
        if notify_policy_id is not None:
            self.notify_policy_id = notify_policy_id
        if query is not None:
            self.query = query
        self.type = type

    @property
    def annotations(self):
        """Gets the annotations of this CreateAlertingRuleRequest.  # noqa: E501


        :return: The annotations of this CreateAlertingRuleRequest.  # noqa: E501
        :rtype: list[AnnotationForCreateAlertingRuleInput]
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this CreateAlertingRuleRequest.


        :param annotations: The annotations of this CreateAlertingRuleRequest.  # noqa: E501
        :type: list[AnnotationForCreateAlertingRuleInput]
        """

        self._annotations = annotations

    @property
    def description(self):
        """Gets the description of this CreateAlertingRuleRequest.  # noqa: E501


        :return: The description of this CreateAlertingRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateAlertingRuleRequest.


        :param description: The description of this CreateAlertingRuleRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def labels(self):
        """Gets the labels of this CreateAlertingRuleRequest.  # noqa: E501


        :return: The labels of this CreateAlertingRuleRequest.  # noqa: E501
        :rtype: list[LabelForCreateAlertingRuleInput]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this CreateAlertingRuleRequest.


        :param labels: The labels of this CreateAlertingRuleRequest.  # noqa: E501
        :type: list[LabelForCreateAlertingRuleInput]
        """

        self._labels = labels

    @property
    def levels(self):
        """Gets the levels of this CreateAlertingRuleRequest.  # noqa: E501


        :return: The levels of this CreateAlertingRuleRequest.  # noqa: E501
        :rtype: list[LevelForCreateAlertingRuleInput]
        """
        return self._levels

    @levels.setter
    def levels(self, levels):
        """Sets the levels of this CreateAlertingRuleRequest.


        :param levels: The levels of this CreateAlertingRuleRequest.  # noqa: E501
        :type: list[LevelForCreateAlertingRuleInput]
        """

        self._levels = levels

    @property
    def name(self):
        """Gets the name of this CreateAlertingRuleRequest.  # noqa: E501


        :return: The name of this CreateAlertingRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateAlertingRuleRequest.


        :param name: The name of this CreateAlertingRuleRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def notify_group_policy_id(self):
        """Gets the notify_group_policy_id of this CreateAlertingRuleRequest.  # noqa: E501


        :return: The notify_group_policy_id of this CreateAlertingRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._notify_group_policy_id

    @notify_group_policy_id.setter
    def notify_group_policy_id(self, notify_group_policy_id):
        """Sets the notify_group_policy_id of this CreateAlertingRuleRequest.


        :param notify_group_policy_id: The notify_group_policy_id of this CreateAlertingRuleRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and notify_group_policy_id is None:
            raise ValueError("Invalid value for `notify_group_policy_id`, must not be `None`")  # noqa: E501

        self._notify_group_policy_id = notify_group_policy_id

    @property
    def notify_policy_id(self):
        """Gets the notify_policy_id of this CreateAlertingRuleRequest.  # noqa: E501


        :return: The notify_policy_id of this CreateAlertingRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._notify_policy_id

    @notify_policy_id.setter
    def notify_policy_id(self, notify_policy_id):
        """Sets the notify_policy_id of this CreateAlertingRuleRequest.


        :param notify_policy_id: The notify_policy_id of this CreateAlertingRuleRequest.  # noqa: E501
        :type: str
        """

        self._notify_policy_id = notify_policy_id

    @property
    def query(self):
        """Gets the query of this CreateAlertingRuleRequest.  # noqa: E501


        :return: The query of this CreateAlertingRuleRequest.  # noqa: E501
        :rtype: QueryForCreateAlertingRuleInput
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this CreateAlertingRuleRequest.


        :param query: The query of this CreateAlertingRuleRequest.  # noqa: E501
        :type: QueryForCreateAlertingRuleInput
        """

        self._query = query

    @property
    def type(self):
        """Gets the type of this CreateAlertingRuleRequest.  # noqa: E501


        :return: The type of this CreateAlertingRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateAlertingRuleRequest.


        :param type: The type of this CreateAlertingRuleRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if issubclass(CreateAlertingRuleRequest, dict):
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
        if not isinstance(other, CreateAlertingRuleRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateAlertingRuleRequest):
            return True

        return self.to_dict() != other.to_dict()
