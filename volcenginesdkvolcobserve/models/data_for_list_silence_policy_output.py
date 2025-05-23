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


class DataForListSilencePolicyOutput(object):
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
        'created_at': 'str',
        'description': 'str',
        'effect_time': 'EffectTimeForListSilencePolicyOutput',
        'enable_state': 'str',
        'id': 'str',
        'name': 'str',
        'namespace': 'str',
        'silence_conditions': 'SilenceConditionsForListSilencePolicyOutput',
        'silence_type': 'str',
        'updated_at': 'str',
        'valid_reason': 'str',
        'valid_state': 'str'
    }

    attribute_map = {
        'created_at': 'CreatedAt',
        'description': 'Description',
        'effect_time': 'EffectTime',
        'enable_state': 'EnableState',
        'id': 'Id',
        'name': 'Name',
        'namespace': 'Namespace',
        'silence_conditions': 'SilenceConditions',
        'silence_type': 'SilenceType',
        'updated_at': 'UpdatedAt',
        'valid_reason': 'ValidReason',
        'valid_state': 'ValidState'
    }

    def __init__(self, created_at=None, description=None, effect_time=None, enable_state=None, id=None, name=None, namespace=None, silence_conditions=None, silence_type=None, updated_at=None, valid_reason=None, valid_state=None, _configuration=None):  # noqa: E501
        """DataForListSilencePolicyOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._created_at = None
        self._description = None
        self._effect_time = None
        self._enable_state = None
        self._id = None
        self._name = None
        self._namespace = None
        self._silence_conditions = None
        self._silence_type = None
        self._updated_at = None
        self._valid_reason = None
        self._valid_state = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if description is not None:
            self.description = description
        if effect_time is not None:
            self.effect_time = effect_time
        if enable_state is not None:
            self.enable_state = enable_state
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if namespace is not None:
            self.namespace = namespace
        if silence_conditions is not None:
            self.silence_conditions = silence_conditions
        if silence_type is not None:
            self.silence_type = silence_type
        if updated_at is not None:
            self.updated_at = updated_at
        if valid_reason is not None:
            self.valid_reason = valid_reason
        if valid_state is not None:
            self.valid_state = valid_state

    @property
    def created_at(self):
        """Gets the created_at of this DataForListSilencePolicyOutput.  # noqa: E501


        :return: The created_at of this DataForListSilencePolicyOutput.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this DataForListSilencePolicyOutput.


        :param created_at: The created_at of this DataForListSilencePolicyOutput.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def description(self):
        """Gets the description of this DataForListSilencePolicyOutput.  # noqa: E501


        :return: The description of this DataForListSilencePolicyOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DataForListSilencePolicyOutput.


        :param description: The description of this DataForListSilencePolicyOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def effect_time(self):
        """Gets the effect_time of this DataForListSilencePolicyOutput.  # noqa: E501


        :return: The effect_time of this DataForListSilencePolicyOutput.  # noqa: E501
        :rtype: EffectTimeForListSilencePolicyOutput
        """
        return self._effect_time

    @effect_time.setter
    def effect_time(self, effect_time):
        """Sets the effect_time of this DataForListSilencePolicyOutput.


        :param effect_time: The effect_time of this DataForListSilencePolicyOutput.  # noqa: E501
        :type: EffectTimeForListSilencePolicyOutput
        """

        self._effect_time = effect_time

    @property
    def enable_state(self):
        """Gets the enable_state of this DataForListSilencePolicyOutput.  # noqa: E501


        :return: The enable_state of this DataForListSilencePolicyOutput.  # noqa: E501
        :rtype: str
        """
        return self._enable_state

    @enable_state.setter
    def enable_state(self, enable_state):
        """Sets the enable_state of this DataForListSilencePolicyOutput.


        :param enable_state: The enable_state of this DataForListSilencePolicyOutput.  # noqa: E501
        :type: str
        """

        self._enable_state = enable_state

    @property
    def id(self):
        """Gets the id of this DataForListSilencePolicyOutput.  # noqa: E501


        :return: The id of this DataForListSilencePolicyOutput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DataForListSilencePolicyOutput.


        :param id: The id of this DataForListSilencePolicyOutput.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this DataForListSilencePolicyOutput.  # noqa: E501


        :return: The name of this DataForListSilencePolicyOutput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DataForListSilencePolicyOutput.


        :param name: The name of this DataForListSilencePolicyOutput.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def namespace(self):
        """Gets the namespace of this DataForListSilencePolicyOutput.  # noqa: E501


        :return: The namespace of this DataForListSilencePolicyOutput.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this DataForListSilencePolicyOutput.


        :param namespace: The namespace of this DataForListSilencePolicyOutput.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def silence_conditions(self):
        """Gets the silence_conditions of this DataForListSilencePolicyOutput.  # noqa: E501


        :return: The silence_conditions of this DataForListSilencePolicyOutput.  # noqa: E501
        :rtype: SilenceConditionsForListSilencePolicyOutput
        """
        return self._silence_conditions

    @silence_conditions.setter
    def silence_conditions(self, silence_conditions):
        """Sets the silence_conditions of this DataForListSilencePolicyOutput.


        :param silence_conditions: The silence_conditions of this DataForListSilencePolicyOutput.  # noqa: E501
        :type: SilenceConditionsForListSilencePolicyOutput
        """

        self._silence_conditions = silence_conditions

    @property
    def silence_type(self):
        """Gets the silence_type of this DataForListSilencePolicyOutput.  # noqa: E501


        :return: The silence_type of this DataForListSilencePolicyOutput.  # noqa: E501
        :rtype: str
        """
        return self._silence_type

    @silence_type.setter
    def silence_type(self, silence_type):
        """Sets the silence_type of this DataForListSilencePolicyOutput.


        :param silence_type: The silence_type of this DataForListSilencePolicyOutput.  # noqa: E501
        :type: str
        """

        self._silence_type = silence_type

    @property
    def updated_at(self):
        """Gets the updated_at of this DataForListSilencePolicyOutput.  # noqa: E501


        :return: The updated_at of this DataForListSilencePolicyOutput.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this DataForListSilencePolicyOutput.


        :param updated_at: The updated_at of this DataForListSilencePolicyOutput.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

    @property
    def valid_reason(self):
        """Gets the valid_reason of this DataForListSilencePolicyOutput.  # noqa: E501


        :return: The valid_reason of this DataForListSilencePolicyOutput.  # noqa: E501
        :rtype: str
        """
        return self._valid_reason

    @valid_reason.setter
    def valid_reason(self, valid_reason):
        """Sets the valid_reason of this DataForListSilencePolicyOutput.


        :param valid_reason: The valid_reason of this DataForListSilencePolicyOutput.  # noqa: E501
        :type: str
        """

        self._valid_reason = valid_reason

    @property
    def valid_state(self):
        """Gets the valid_state of this DataForListSilencePolicyOutput.  # noqa: E501


        :return: The valid_state of this DataForListSilencePolicyOutput.  # noqa: E501
        :rtype: str
        """
        return self._valid_state

    @valid_state.setter
    def valid_state(self, valid_state):
        """Sets the valid_state of this DataForListSilencePolicyOutput.


        :param valid_state: The valid_state of this DataForListSilencePolicyOutput.  # noqa: E501
        :type: str
        """

        self._valid_state = valid_state

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
        if issubclass(DataForListSilencePolicyOutput, dict):
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
        if not isinstance(other, DataForListSilencePolicyOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataForListSilencePolicyOutput):
            return True

        return self.to_dict() != other.to_dict()
