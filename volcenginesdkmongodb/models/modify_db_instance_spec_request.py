# coding: utf-8

"""
    mongodb

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ModifyDBInstanceSpecRequest(object):
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
        'instance_id': 'str',
        'instance_type': 'str',
        'mongos_node_spec': 'str',
        'node_spec': 'str',
        'storage_space_gb': 'int'
    }

    attribute_map = {
        'instance_id': 'InstanceId',
        'instance_type': 'InstanceType',
        'mongos_node_spec': 'MongosNodeSpec',
        'node_spec': 'NodeSpec',
        'storage_space_gb': 'StorageSpaceGB'
    }

    def __init__(self, instance_id=None, instance_type=None, mongos_node_spec=None, node_spec=None, storage_space_gb=None, _configuration=None):  # noqa: E501
        """ModifyDBInstanceSpecRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._instance_id = None
        self._instance_type = None
        self._mongos_node_spec = None
        self._node_spec = None
        self._storage_space_gb = None
        self.discriminator = None

        self.instance_id = instance_id
        if instance_type is not None:
            self.instance_type = instance_type
        if mongos_node_spec is not None:
            self.mongos_node_spec = mongos_node_spec
        if node_spec is not None:
            self.node_spec = node_spec
        if storage_space_gb is not None:
            self.storage_space_gb = storage_space_gb

    @property
    def instance_id(self):
        """Gets the instance_id of this ModifyDBInstanceSpecRequest.  # noqa: E501


        :return: The instance_id of this ModifyDBInstanceSpecRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ModifyDBInstanceSpecRequest.


        :param instance_id: The instance_id of this ModifyDBInstanceSpecRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and instance_id is None:
            raise ValueError("Invalid value for `instance_id`, must not be `None`")  # noqa: E501

        self._instance_id = instance_id

    @property
    def instance_type(self):
        """Gets the instance_type of this ModifyDBInstanceSpecRequest.  # noqa: E501


        :return: The instance_type of this ModifyDBInstanceSpecRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this ModifyDBInstanceSpecRequest.


        :param instance_type: The instance_type of this ModifyDBInstanceSpecRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["ReplicaSet", "ShardedCluster"]  # noqa: E501
        if (self._configuration.client_side_validation and
                instance_type not in allowed_values):
            raise ValueError(
                "Invalid value for `instance_type` ({0}), must be one of {1}"  # noqa: E501
                .format(instance_type, allowed_values)
            )

        self._instance_type = instance_type

    @property
    def mongos_node_spec(self):
        """Gets the mongos_node_spec of this ModifyDBInstanceSpecRequest.  # noqa: E501


        :return: The mongos_node_spec of this ModifyDBInstanceSpecRequest.  # noqa: E501
        :rtype: str
        """
        return self._mongos_node_spec

    @mongos_node_spec.setter
    def mongos_node_spec(self, mongos_node_spec):
        """Sets the mongos_node_spec of this ModifyDBInstanceSpecRequest.


        :param mongos_node_spec: The mongos_node_spec of this ModifyDBInstanceSpecRequest.  # noqa: E501
        :type: str
        """

        self._mongos_node_spec = mongos_node_spec

    @property
    def node_spec(self):
        """Gets the node_spec of this ModifyDBInstanceSpecRequest.  # noqa: E501


        :return: The node_spec of this ModifyDBInstanceSpecRequest.  # noqa: E501
        :rtype: str
        """
        return self._node_spec

    @node_spec.setter
    def node_spec(self, node_spec):
        """Sets the node_spec of this ModifyDBInstanceSpecRequest.


        :param node_spec: The node_spec of this ModifyDBInstanceSpecRequest.  # noqa: E501
        :type: str
        """

        self._node_spec = node_spec

    @property
    def storage_space_gb(self):
        """Gets the storage_space_gb of this ModifyDBInstanceSpecRequest.  # noqa: E501


        :return: The storage_space_gb of this ModifyDBInstanceSpecRequest.  # noqa: E501
        :rtype: int
        """
        return self._storage_space_gb

    @storage_space_gb.setter
    def storage_space_gb(self, storage_space_gb):
        """Sets the storage_space_gb of this ModifyDBInstanceSpecRequest.


        :param storage_space_gb: The storage_space_gb of this ModifyDBInstanceSpecRequest.  # noqa: E501
        :type: int
        """

        self._storage_space_gb = storage_space_gb

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
        if issubclass(ModifyDBInstanceSpecRequest, dict):
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
        if not isinstance(other, ModifyDBInstanceSpecRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModifyDBInstanceSpecRequest):
            return True

        return self.to_dict() != other.to_dict()
