# coding: utf-8

"""
    rds_mysql_v2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class RestartDBInstanceRequest(object):
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
        'apply_scope': 'str',
        'custom_node_ids': 'list[str]',
        'instance_id': 'str',
        'specified_switch_end_time': 'str',
        'specified_switch_start_time': 'str',
        'switch_type': 'str'
    }

    attribute_map = {
        'apply_scope': 'ApplyScope',
        'custom_node_ids': 'CustomNodeIds',
        'instance_id': 'InstanceId',
        'specified_switch_end_time': 'SpecifiedSwitchEndTime',
        'specified_switch_start_time': 'SpecifiedSwitchStartTime',
        'switch_type': 'SwitchType'
    }

    def __init__(self, apply_scope=None, custom_node_ids=None, instance_id=None, specified_switch_end_time=None, specified_switch_start_time=None, switch_type=None, _configuration=None):  # noqa: E501
        """RestartDBInstanceRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._apply_scope = None
        self._custom_node_ids = None
        self._instance_id = None
        self._specified_switch_end_time = None
        self._specified_switch_start_time = None
        self._switch_type = None
        self.discriminator = None

        if apply_scope is not None:
            self.apply_scope = apply_scope
        if custom_node_ids is not None:
            self.custom_node_ids = custom_node_ids
        self.instance_id = instance_id
        if specified_switch_end_time is not None:
            self.specified_switch_end_time = specified_switch_end_time
        if specified_switch_start_time is not None:
            self.specified_switch_start_time = specified_switch_start_time
        if switch_type is not None:
            self.switch_type = switch_type

    @property
    def apply_scope(self):
        """Gets the apply_scope of this RestartDBInstanceRequest.  # noqa: E501


        :return: The apply_scope of this RestartDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._apply_scope

    @apply_scope.setter
    def apply_scope(self, apply_scope):
        """Sets the apply_scope of this RestartDBInstanceRequest.


        :param apply_scope: The apply_scope of this RestartDBInstanceRequest.  # noqa: E501
        :type: str
        """

        self._apply_scope = apply_scope

    @property
    def custom_node_ids(self):
        """Gets the custom_node_ids of this RestartDBInstanceRequest.  # noqa: E501


        :return: The custom_node_ids of this RestartDBInstanceRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._custom_node_ids

    @custom_node_ids.setter
    def custom_node_ids(self, custom_node_ids):
        """Sets the custom_node_ids of this RestartDBInstanceRequest.


        :param custom_node_ids: The custom_node_ids of this RestartDBInstanceRequest.  # noqa: E501
        :type: list[str]
        """

        self._custom_node_ids = custom_node_ids

    @property
    def instance_id(self):
        """Gets the instance_id of this RestartDBInstanceRequest.  # noqa: E501


        :return: The instance_id of this RestartDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this RestartDBInstanceRequest.


        :param instance_id: The instance_id of this RestartDBInstanceRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and instance_id is None:
            raise ValueError("Invalid value for `instance_id`, must not be `None`")  # noqa: E501

        self._instance_id = instance_id

    @property
    def specified_switch_end_time(self):
        """Gets the specified_switch_end_time of this RestartDBInstanceRequest.  # noqa: E501


        :return: The specified_switch_end_time of this RestartDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._specified_switch_end_time

    @specified_switch_end_time.setter
    def specified_switch_end_time(self, specified_switch_end_time):
        """Sets the specified_switch_end_time of this RestartDBInstanceRequest.


        :param specified_switch_end_time: The specified_switch_end_time of this RestartDBInstanceRequest.  # noqa: E501
        :type: str
        """

        self._specified_switch_end_time = specified_switch_end_time

    @property
    def specified_switch_start_time(self):
        """Gets the specified_switch_start_time of this RestartDBInstanceRequest.  # noqa: E501


        :return: The specified_switch_start_time of this RestartDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._specified_switch_start_time

    @specified_switch_start_time.setter
    def specified_switch_start_time(self, specified_switch_start_time):
        """Sets the specified_switch_start_time of this RestartDBInstanceRequest.


        :param specified_switch_start_time: The specified_switch_start_time of this RestartDBInstanceRequest.  # noqa: E501
        :type: str
        """

        self._specified_switch_start_time = specified_switch_start_time

    @property
    def switch_type(self):
        """Gets the switch_type of this RestartDBInstanceRequest.  # noqa: E501


        :return: The switch_type of this RestartDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._switch_type

    @switch_type.setter
    def switch_type(self, switch_type):
        """Sets the switch_type of this RestartDBInstanceRequest.


        :param switch_type: The switch_type of this RestartDBInstanceRequest.  # noqa: E501
        :type: str
        """

        self._switch_type = switch_type

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
        if issubclass(RestartDBInstanceRequest, dict):
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
        if not isinstance(other, RestartDBInstanceRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RestartDBInstanceRequest):
            return True

        return self.to_dict() != other.to_dict()
