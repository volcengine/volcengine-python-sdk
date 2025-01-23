# coding: utf-8

"""
    kms

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class MultiRegionConfigurationForDescribeKeyOutput(object):
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
        'multi_region_key_type': 'str',
        'primary_key': 'PrimaryKeyForDescribeKeyOutput',
        'replica_keys': 'list[ReplicaKeyForDescribeKeyOutput]'
    }

    attribute_map = {
        'multi_region_key_type': 'MultiRegionKeyType',
        'primary_key': 'PrimaryKey',
        'replica_keys': 'ReplicaKeys'
    }

    def __init__(self, multi_region_key_type=None, primary_key=None, replica_keys=None, _configuration=None):  # noqa: E501
        """MultiRegionConfigurationForDescribeKeyOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._multi_region_key_type = None
        self._primary_key = None
        self._replica_keys = None
        self.discriminator = None

        if multi_region_key_type is not None:
            self.multi_region_key_type = multi_region_key_type
        if primary_key is not None:
            self.primary_key = primary_key
        if replica_keys is not None:
            self.replica_keys = replica_keys

    @property
    def multi_region_key_type(self):
        """Gets the multi_region_key_type of this MultiRegionConfigurationForDescribeKeyOutput.  # noqa: E501


        :return: The multi_region_key_type of this MultiRegionConfigurationForDescribeKeyOutput.  # noqa: E501
        :rtype: str
        """
        return self._multi_region_key_type

    @multi_region_key_type.setter
    def multi_region_key_type(self, multi_region_key_type):
        """Sets the multi_region_key_type of this MultiRegionConfigurationForDescribeKeyOutput.


        :param multi_region_key_type: The multi_region_key_type of this MultiRegionConfigurationForDescribeKeyOutput.  # noqa: E501
        :type: str
        """

        self._multi_region_key_type = multi_region_key_type

    @property
    def primary_key(self):
        """Gets the primary_key of this MultiRegionConfigurationForDescribeKeyOutput.  # noqa: E501


        :return: The primary_key of this MultiRegionConfigurationForDescribeKeyOutput.  # noqa: E501
        :rtype: PrimaryKeyForDescribeKeyOutput
        """
        return self._primary_key

    @primary_key.setter
    def primary_key(self, primary_key):
        """Sets the primary_key of this MultiRegionConfigurationForDescribeKeyOutput.


        :param primary_key: The primary_key of this MultiRegionConfigurationForDescribeKeyOutput.  # noqa: E501
        :type: PrimaryKeyForDescribeKeyOutput
        """

        self._primary_key = primary_key

    @property
    def replica_keys(self):
        """Gets the replica_keys of this MultiRegionConfigurationForDescribeKeyOutput.  # noqa: E501


        :return: The replica_keys of this MultiRegionConfigurationForDescribeKeyOutput.  # noqa: E501
        :rtype: list[ReplicaKeyForDescribeKeyOutput]
        """
        return self._replica_keys

    @replica_keys.setter
    def replica_keys(self, replica_keys):
        """Sets the replica_keys of this MultiRegionConfigurationForDescribeKeyOutput.


        :param replica_keys: The replica_keys of this MultiRegionConfigurationForDescribeKeyOutput.  # noqa: E501
        :type: list[ReplicaKeyForDescribeKeyOutput]
        """

        self._replica_keys = replica_keys

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
        if issubclass(MultiRegionConfigurationForDescribeKeyOutput, dict):
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
        if not isinstance(other, MultiRegionConfigurationForDescribeKeyOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MultiRegionConfigurationForDescribeKeyOutput):
            return True

        return self.to_dict() != other.to_dict()
