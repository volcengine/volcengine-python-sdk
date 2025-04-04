# coding: utf-8

"""
    emr

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ItemForListApplicationConfigsOutput(object):
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
        'application_name': 'str',
        'applied': 'bool',
        'config_file_name': 'str',
        'config_item_key': 'str',
        'config_item_value': 'str',
        'config_version': 'str',
        'customized': 'bool',
        'description': 'str',
        'effective_scope': 'EffectiveScopeForListApplicationConfigsOutput',
        'operator_id': 'str',
        'preset_config_item_value': 'str',
        'remark': 'str',
        'update_time': 'int'
    }

    attribute_map = {
        'application_name': 'ApplicationName',
        'applied': 'Applied',
        'config_file_name': 'ConfigFileName',
        'config_item_key': 'ConfigItemKey',
        'config_item_value': 'ConfigItemValue',
        'config_version': 'ConfigVersion',
        'customized': 'Customized',
        'description': 'Description',
        'effective_scope': 'EffectiveScope',
        'operator_id': 'OperatorId',
        'preset_config_item_value': 'PresetConfigItemValue',
        'remark': 'Remark',
        'update_time': 'UpdateTime'
    }

    def __init__(self, application_name=None, applied=None, config_file_name=None, config_item_key=None, config_item_value=None, config_version=None, customized=None, description=None, effective_scope=None, operator_id=None, preset_config_item_value=None, remark=None, update_time=None, _configuration=None):  # noqa: E501
        """ItemForListApplicationConfigsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._application_name = None
        self._applied = None
        self._config_file_name = None
        self._config_item_key = None
        self._config_item_value = None
        self._config_version = None
        self._customized = None
        self._description = None
        self._effective_scope = None
        self._operator_id = None
        self._preset_config_item_value = None
        self._remark = None
        self._update_time = None
        self.discriminator = None

        if application_name is not None:
            self.application_name = application_name
        if applied is not None:
            self.applied = applied
        if config_file_name is not None:
            self.config_file_name = config_file_name
        if config_item_key is not None:
            self.config_item_key = config_item_key
        if config_item_value is not None:
            self.config_item_value = config_item_value
        if config_version is not None:
            self.config_version = config_version
        if customized is not None:
            self.customized = customized
        if description is not None:
            self.description = description
        if effective_scope is not None:
            self.effective_scope = effective_scope
        if operator_id is not None:
            self.operator_id = operator_id
        if preset_config_item_value is not None:
            self.preset_config_item_value = preset_config_item_value
        if remark is not None:
            self.remark = remark
        if update_time is not None:
            self.update_time = update_time

    @property
    def application_name(self):
        """Gets the application_name of this ItemForListApplicationConfigsOutput.  # noqa: E501


        :return: The application_name of this ItemForListApplicationConfigsOutput.  # noqa: E501
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        """Sets the application_name of this ItemForListApplicationConfigsOutput.


        :param application_name: The application_name of this ItemForListApplicationConfigsOutput.  # noqa: E501
        :type: str
        """

        self._application_name = application_name

    @property
    def applied(self):
        """Gets the applied of this ItemForListApplicationConfigsOutput.  # noqa: E501


        :return: The applied of this ItemForListApplicationConfigsOutput.  # noqa: E501
        :rtype: bool
        """
        return self._applied

    @applied.setter
    def applied(self, applied):
        """Sets the applied of this ItemForListApplicationConfigsOutput.


        :param applied: The applied of this ItemForListApplicationConfigsOutput.  # noqa: E501
        :type: bool
        """

        self._applied = applied

    @property
    def config_file_name(self):
        """Gets the config_file_name of this ItemForListApplicationConfigsOutput.  # noqa: E501


        :return: The config_file_name of this ItemForListApplicationConfigsOutput.  # noqa: E501
        :rtype: str
        """
        return self._config_file_name

    @config_file_name.setter
    def config_file_name(self, config_file_name):
        """Sets the config_file_name of this ItemForListApplicationConfigsOutput.


        :param config_file_name: The config_file_name of this ItemForListApplicationConfigsOutput.  # noqa: E501
        :type: str
        """

        self._config_file_name = config_file_name

    @property
    def config_item_key(self):
        """Gets the config_item_key of this ItemForListApplicationConfigsOutput.  # noqa: E501


        :return: The config_item_key of this ItemForListApplicationConfigsOutput.  # noqa: E501
        :rtype: str
        """
        return self._config_item_key

    @config_item_key.setter
    def config_item_key(self, config_item_key):
        """Sets the config_item_key of this ItemForListApplicationConfigsOutput.


        :param config_item_key: The config_item_key of this ItemForListApplicationConfigsOutput.  # noqa: E501
        :type: str
        """

        self._config_item_key = config_item_key

    @property
    def config_item_value(self):
        """Gets the config_item_value of this ItemForListApplicationConfigsOutput.  # noqa: E501


        :return: The config_item_value of this ItemForListApplicationConfigsOutput.  # noqa: E501
        :rtype: str
        """
        return self._config_item_value

    @config_item_value.setter
    def config_item_value(self, config_item_value):
        """Sets the config_item_value of this ItemForListApplicationConfigsOutput.


        :param config_item_value: The config_item_value of this ItemForListApplicationConfigsOutput.  # noqa: E501
        :type: str
        """

        self._config_item_value = config_item_value

    @property
    def config_version(self):
        """Gets the config_version of this ItemForListApplicationConfigsOutput.  # noqa: E501


        :return: The config_version of this ItemForListApplicationConfigsOutput.  # noqa: E501
        :rtype: str
        """
        return self._config_version

    @config_version.setter
    def config_version(self, config_version):
        """Sets the config_version of this ItemForListApplicationConfigsOutput.


        :param config_version: The config_version of this ItemForListApplicationConfigsOutput.  # noqa: E501
        :type: str
        """

        self._config_version = config_version

    @property
    def customized(self):
        """Gets the customized of this ItemForListApplicationConfigsOutput.  # noqa: E501


        :return: The customized of this ItemForListApplicationConfigsOutput.  # noqa: E501
        :rtype: bool
        """
        return self._customized

    @customized.setter
    def customized(self, customized):
        """Sets the customized of this ItemForListApplicationConfigsOutput.


        :param customized: The customized of this ItemForListApplicationConfigsOutput.  # noqa: E501
        :type: bool
        """

        self._customized = customized

    @property
    def description(self):
        """Gets the description of this ItemForListApplicationConfigsOutput.  # noqa: E501


        :return: The description of this ItemForListApplicationConfigsOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ItemForListApplicationConfigsOutput.


        :param description: The description of this ItemForListApplicationConfigsOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def effective_scope(self):
        """Gets the effective_scope of this ItemForListApplicationConfigsOutput.  # noqa: E501


        :return: The effective_scope of this ItemForListApplicationConfigsOutput.  # noqa: E501
        :rtype: EffectiveScopeForListApplicationConfigsOutput
        """
        return self._effective_scope

    @effective_scope.setter
    def effective_scope(self, effective_scope):
        """Sets the effective_scope of this ItemForListApplicationConfigsOutput.


        :param effective_scope: The effective_scope of this ItemForListApplicationConfigsOutput.  # noqa: E501
        :type: EffectiveScopeForListApplicationConfigsOutput
        """

        self._effective_scope = effective_scope

    @property
    def operator_id(self):
        """Gets the operator_id of this ItemForListApplicationConfigsOutput.  # noqa: E501


        :return: The operator_id of this ItemForListApplicationConfigsOutput.  # noqa: E501
        :rtype: str
        """
        return self._operator_id

    @operator_id.setter
    def operator_id(self, operator_id):
        """Sets the operator_id of this ItemForListApplicationConfigsOutput.


        :param operator_id: The operator_id of this ItemForListApplicationConfigsOutput.  # noqa: E501
        :type: str
        """

        self._operator_id = operator_id

    @property
    def preset_config_item_value(self):
        """Gets the preset_config_item_value of this ItemForListApplicationConfigsOutput.  # noqa: E501


        :return: The preset_config_item_value of this ItemForListApplicationConfigsOutput.  # noqa: E501
        :rtype: str
        """
        return self._preset_config_item_value

    @preset_config_item_value.setter
    def preset_config_item_value(self, preset_config_item_value):
        """Sets the preset_config_item_value of this ItemForListApplicationConfigsOutput.


        :param preset_config_item_value: The preset_config_item_value of this ItemForListApplicationConfigsOutput.  # noqa: E501
        :type: str
        """

        self._preset_config_item_value = preset_config_item_value

    @property
    def remark(self):
        """Gets the remark of this ItemForListApplicationConfigsOutput.  # noqa: E501


        :return: The remark of this ItemForListApplicationConfigsOutput.  # noqa: E501
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this ItemForListApplicationConfigsOutput.


        :param remark: The remark of this ItemForListApplicationConfigsOutput.  # noqa: E501
        :type: str
        """

        self._remark = remark

    @property
    def update_time(self):
        """Gets the update_time of this ItemForListApplicationConfigsOutput.  # noqa: E501


        :return: The update_time of this ItemForListApplicationConfigsOutput.  # noqa: E501
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ItemForListApplicationConfigsOutput.


        :param update_time: The update_time of this ItemForListApplicationConfigsOutput.  # noqa: E501
        :type: int
        """

        self._update_time = update_time

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
        if issubclass(ItemForListApplicationConfigsOutput, dict):
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
        if not isinstance(other, ItemForListApplicationConfigsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ItemForListApplicationConfigsOutput):
            return True

        return self.to_dict() != other.to_dict()
