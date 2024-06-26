# coding: utf-8

"""
    auto_scaling

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class RemoveInstancesRequest(object):
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
        'decrease_desired_capacity': 'bool',
        'force_delete': 'bool',
        'instance_ids': 'list[str]',
        'lifecycle_hook': 'bool',
        'remove_mode': 'str',
        'scaling_group_id': 'str'
    }

    attribute_map = {
        'decrease_desired_capacity': 'DecreaseDesiredCapacity',
        'force_delete': 'ForceDelete',
        'instance_ids': 'InstanceIds',
        'lifecycle_hook': 'LifecycleHook',
        'remove_mode': 'RemoveMode',
        'scaling_group_id': 'ScalingGroupId'
    }

    def __init__(self, decrease_desired_capacity=None, force_delete=None, instance_ids=None, lifecycle_hook=None, remove_mode=None, scaling_group_id=None, _configuration=None):  # noqa: E501
        """RemoveInstancesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._decrease_desired_capacity = None
        self._force_delete = None
        self._instance_ids = None
        self._lifecycle_hook = None
        self._remove_mode = None
        self._scaling_group_id = None
        self.discriminator = None

        if decrease_desired_capacity is not None:
            self.decrease_desired_capacity = decrease_desired_capacity
        if force_delete is not None:
            self.force_delete = force_delete
        if instance_ids is not None:
            self.instance_ids = instance_ids
        if lifecycle_hook is not None:
            self.lifecycle_hook = lifecycle_hook
        if remove_mode is not None:
            self.remove_mode = remove_mode
        self.scaling_group_id = scaling_group_id

    @property
    def decrease_desired_capacity(self):
        """Gets the decrease_desired_capacity of this RemoveInstancesRequest.  # noqa: E501


        :return: The decrease_desired_capacity of this RemoveInstancesRequest.  # noqa: E501
        :rtype: bool
        """
        return self._decrease_desired_capacity

    @decrease_desired_capacity.setter
    def decrease_desired_capacity(self, decrease_desired_capacity):
        """Sets the decrease_desired_capacity of this RemoveInstancesRequest.


        :param decrease_desired_capacity: The decrease_desired_capacity of this RemoveInstancesRequest.  # noqa: E501
        :type: bool
        """

        self._decrease_desired_capacity = decrease_desired_capacity

    @property
    def force_delete(self):
        """Gets the force_delete of this RemoveInstancesRequest.  # noqa: E501


        :return: The force_delete of this RemoveInstancesRequest.  # noqa: E501
        :rtype: bool
        """
        return self._force_delete

    @force_delete.setter
    def force_delete(self, force_delete):
        """Sets the force_delete of this RemoveInstancesRequest.


        :param force_delete: The force_delete of this RemoveInstancesRequest.  # noqa: E501
        :type: bool
        """

        self._force_delete = force_delete

    @property
    def instance_ids(self):
        """Gets the instance_ids of this RemoveInstancesRequest.  # noqa: E501


        :return: The instance_ids of this RemoveInstancesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._instance_ids

    @instance_ids.setter
    def instance_ids(self, instance_ids):
        """Sets the instance_ids of this RemoveInstancesRequest.


        :param instance_ids: The instance_ids of this RemoveInstancesRequest.  # noqa: E501
        :type: list[str]
        """

        self._instance_ids = instance_ids

    @property
    def lifecycle_hook(self):
        """Gets the lifecycle_hook of this RemoveInstancesRequest.  # noqa: E501


        :return: The lifecycle_hook of this RemoveInstancesRequest.  # noqa: E501
        :rtype: bool
        """
        return self._lifecycle_hook

    @lifecycle_hook.setter
    def lifecycle_hook(self, lifecycle_hook):
        """Sets the lifecycle_hook of this RemoveInstancesRequest.


        :param lifecycle_hook: The lifecycle_hook of this RemoveInstancesRequest.  # noqa: E501
        :type: bool
        """

        self._lifecycle_hook = lifecycle_hook

    @property
    def remove_mode(self):
        """Gets the remove_mode of this RemoveInstancesRequest.  # noqa: E501


        :return: The remove_mode of this RemoveInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._remove_mode

    @remove_mode.setter
    def remove_mode(self, remove_mode):
        """Sets the remove_mode of this RemoveInstancesRequest.


        :param remove_mode: The remove_mode of this RemoveInstancesRequest.  # noqa: E501
        :type: str
        """

        self._remove_mode = remove_mode

    @property
    def scaling_group_id(self):
        """Gets the scaling_group_id of this RemoveInstancesRequest.  # noqa: E501


        :return: The scaling_group_id of this RemoveInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._scaling_group_id

    @scaling_group_id.setter
    def scaling_group_id(self, scaling_group_id):
        """Sets the scaling_group_id of this RemoveInstancesRequest.


        :param scaling_group_id: The scaling_group_id of this RemoveInstancesRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and scaling_group_id is None:
            raise ValueError("Invalid value for `scaling_group_id`, must not be `None`")  # noqa: E501

        self._scaling_group_id = scaling_group_id

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
        if issubclass(RemoveInstancesRequest, dict):
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
        if not isinstance(other, RemoveInstancesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RemoveInstancesRequest):
            return True

        return self.to_dict() != other.to_dict()
