# coding: utf-8

"""
    rds_postgresql

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeDBInstancePriceDifferenceRequest(object):
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
        'charge_info': 'ChargeInfoForDescribeDBInstancePriceDifferenceInput',
        'instance_id': 'str',
        'modify_type': 'str',
        'node_info': 'list[NodeInfoForDescribeDBInstancePriceDifferenceInput]',
        'rollback_time': 'str',
        'storage_space': 'int',
        'storage_type': 'str'
    }

    attribute_map = {
        'charge_info': 'ChargeInfo',
        'instance_id': 'InstanceId',
        'modify_type': 'ModifyType',
        'node_info': 'NodeInfo',
        'rollback_time': 'RollbackTime',
        'storage_space': 'StorageSpace',
        'storage_type': 'StorageType'
    }

    def __init__(self, charge_info=None, instance_id=None, modify_type=None, node_info=None, rollback_time=None, storage_space=None, storage_type=None, _configuration=None):  # noqa: E501
        """DescribeDBInstancePriceDifferenceRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._charge_info = None
        self._instance_id = None
        self._modify_type = None
        self._node_info = None
        self._rollback_time = None
        self._storage_space = None
        self._storage_type = None
        self.discriminator = None

        if charge_info is not None:
            self.charge_info = charge_info
        self.instance_id = instance_id
        if modify_type is not None:
            self.modify_type = modify_type
        if node_info is not None:
            self.node_info = node_info
        if rollback_time is not None:
            self.rollback_time = rollback_time
        self.storage_space = storage_space
        self.storage_type = storage_type

    @property
    def charge_info(self):
        """Gets the charge_info of this DescribeDBInstancePriceDifferenceRequest.  # noqa: E501


        :return: The charge_info of this DescribeDBInstancePriceDifferenceRequest.  # noqa: E501
        :rtype: ChargeInfoForDescribeDBInstancePriceDifferenceInput
        """
        return self._charge_info

    @charge_info.setter
    def charge_info(self, charge_info):
        """Sets the charge_info of this DescribeDBInstancePriceDifferenceRequest.


        :param charge_info: The charge_info of this DescribeDBInstancePriceDifferenceRequest.  # noqa: E501
        :type: ChargeInfoForDescribeDBInstancePriceDifferenceInput
        """

        self._charge_info = charge_info

    @property
    def instance_id(self):
        """Gets the instance_id of this DescribeDBInstancePriceDifferenceRequest.  # noqa: E501


        :return: The instance_id of this DescribeDBInstancePriceDifferenceRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this DescribeDBInstancePriceDifferenceRequest.


        :param instance_id: The instance_id of this DescribeDBInstancePriceDifferenceRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and instance_id is None:
            raise ValueError("Invalid value for `instance_id`, must not be `None`")  # noqa: E501

        self._instance_id = instance_id

    @property
    def modify_type(self):
        """Gets the modify_type of this DescribeDBInstancePriceDifferenceRequest.  # noqa: E501


        :return: The modify_type of this DescribeDBInstancePriceDifferenceRequest.  # noqa: E501
        :rtype: str
        """
        return self._modify_type

    @modify_type.setter
    def modify_type(self, modify_type):
        """Sets the modify_type of this DescribeDBInstancePriceDifferenceRequest.


        :param modify_type: The modify_type of this DescribeDBInstancePriceDifferenceRequest.  # noqa: E501
        :type: str
        """

        self._modify_type = modify_type

    @property
    def node_info(self):
        """Gets the node_info of this DescribeDBInstancePriceDifferenceRequest.  # noqa: E501


        :return: The node_info of this DescribeDBInstancePriceDifferenceRequest.  # noqa: E501
        :rtype: list[NodeInfoForDescribeDBInstancePriceDifferenceInput]
        """
        return self._node_info

    @node_info.setter
    def node_info(self, node_info):
        """Sets the node_info of this DescribeDBInstancePriceDifferenceRequest.


        :param node_info: The node_info of this DescribeDBInstancePriceDifferenceRequest.  # noqa: E501
        :type: list[NodeInfoForDescribeDBInstancePriceDifferenceInput]
        """

        self._node_info = node_info

    @property
    def rollback_time(self):
        """Gets the rollback_time of this DescribeDBInstancePriceDifferenceRequest.  # noqa: E501


        :return: The rollback_time of this DescribeDBInstancePriceDifferenceRequest.  # noqa: E501
        :rtype: str
        """
        return self._rollback_time

    @rollback_time.setter
    def rollback_time(self, rollback_time):
        """Sets the rollback_time of this DescribeDBInstancePriceDifferenceRequest.


        :param rollback_time: The rollback_time of this DescribeDBInstancePriceDifferenceRequest.  # noqa: E501
        :type: str
        """

        self._rollback_time = rollback_time

    @property
    def storage_space(self):
        """Gets the storage_space of this DescribeDBInstancePriceDifferenceRequest.  # noqa: E501


        :return: The storage_space of this DescribeDBInstancePriceDifferenceRequest.  # noqa: E501
        :rtype: int
        """
        return self._storage_space

    @storage_space.setter
    def storage_space(self, storage_space):
        """Sets the storage_space of this DescribeDBInstancePriceDifferenceRequest.


        :param storage_space: The storage_space of this DescribeDBInstancePriceDifferenceRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and storage_space is None:
            raise ValueError("Invalid value for `storage_space`, must not be `None`")  # noqa: E501

        self._storage_space = storage_space

    @property
    def storage_type(self):
        """Gets the storage_type of this DescribeDBInstancePriceDifferenceRequest.  # noqa: E501


        :return: The storage_type of this DescribeDBInstancePriceDifferenceRequest.  # noqa: E501
        :rtype: str
        """
        return self._storage_type

    @storage_type.setter
    def storage_type(self, storage_type):
        """Sets the storage_type of this DescribeDBInstancePriceDifferenceRequest.


        :param storage_type: The storage_type of this DescribeDBInstancePriceDifferenceRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and storage_type is None:
            raise ValueError("Invalid value for `storage_type`, must not be `None`")  # noqa: E501

        self._storage_type = storage_type

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
        if issubclass(DescribeDBInstancePriceDifferenceRequest, dict):
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
        if not isinstance(other, DescribeDBInstancePriceDifferenceRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeDBInstancePriceDifferenceRequest):
            return True

        return self.to_dict() != other.to_dict()
