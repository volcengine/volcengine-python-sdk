# coding: utf-8

"""
    smc

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class InstanceInfoForDescribeMigrationSourcesOutput(object):
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
        'blk_none_can_install': 'bool',
        'blk_none_install': 'bool',
        'inner_instance': 'bool',
        'instance_id': 'str',
        'region_id': 'str',
        'virtio11_can_install': 'bool',
        'virtio11_install': 'bool'
    }

    attribute_map = {
        'blk_none_can_install': 'BlkNoneCanInstall',
        'blk_none_install': 'BlkNoneInstall',
        'inner_instance': 'InnerInstance',
        'instance_id': 'InstanceId',
        'region_id': 'RegionId',
        'virtio11_can_install': 'Virtio11CanInstall',
        'virtio11_install': 'Virtio11Install'
    }

    def __init__(self, blk_none_can_install=None, blk_none_install=None, inner_instance=None, instance_id=None, region_id=None, virtio11_can_install=None, virtio11_install=None, _configuration=None):  # noqa: E501
        """InstanceInfoForDescribeMigrationSourcesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._blk_none_can_install = None
        self._blk_none_install = None
        self._inner_instance = None
        self._instance_id = None
        self._region_id = None
        self._virtio11_can_install = None
        self._virtio11_install = None
        self.discriminator = None

        if blk_none_can_install is not None:
            self.blk_none_can_install = blk_none_can_install
        if blk_none_install is not None:
            self.blk_none_install = blk_none_install
        if inner_instance is not None:
            self.inner_instance = inner_instance
        if instance_id is not None:
            self.instance_id = instance_id
        if region_id is not None:
            self.region_id = region_id
        if virtio11_can_install is not None:
            self.virtio11_can_install = virtio11_can_install
        if virtio11_install is not None:
            self.virtio11_install = virtio11_install

    @property
    def blk_none_can_install(self):
        """Gets the blk_none_can_install of this InstanceInfoForDescribeMigrationSourcesOutput.  # noqa: E501


        :return: The blk_none_can_install of this InstanceInfoForDescribeMigrationSourcesOutput.  # noqa: E501
        :rtype: bool
        """
        return self._blk_none_can_install

    @blk_none_can_install.setter
    def blk_none_can_install(self, blk_none_can_install):
        """Sets the blk_none_can_install of this InstanceInfoForDescribeMigrationSourcesOutput.


        :param blk_none_can_install: The blk_none_can_install of this InstanceInfoForDescribeMigrationSourcesOutput.  # noqa: E501
        :type: bool
        """

        self._blk_none_can_install = blk_none_can_install

    @property
    def blk_none_install(self):
        """Gets the blk_none_install of this InstanceInfoForDescribeMigrationSourcesOutput.  # noqa: E501


        :return: The blk_none_install of this InstanceInfoForDescribeMigrationSourcesOutput.  # noqa: E501
        :rtype: bool
        """
        return self._blk_none_install

    @blk_none_install.setter
    def blk_none_install(self, blk_none_install):
        """Sets the blk_none_install of this InstanceInfoForDescribeMigrationSourcesOutput.


        :param blk_none_install: The blk_none_install of this InstanceInfoForDescribeMigrationSourcesOutput.  # noqa: E501
        :type: bool
        """

        self._blk_none_install = blk_none_install

    @property
    def inner_instance(self):
        """Gets the inner_instance of this InstanceInfoForDescribeMigrationSourcesOutput.  # noqa: E501


        :return: The inner_instance of this InstanceInfoForDescribeMigrationSourcesOutput.  # noqa: E501
        :rtype: bool
        """
        return self._inner_instance

    @inner_instance.setter
    def inner_instance(self, inner_instance):
        """Sets the inner_instance of this InstanceInfoForDescribeMigrationSourcesOutput.


        :param inner_instance: The inner_instance of this InstanceInfoForDescribeMigrationSourcesOutput.  # noqa: E501
        :type: bool
        """

        self._inner_instance = inner_instance

    @property
    def instance_id(self):
        """Gets the instance_id of this InstanceInfoForDescribeMigrationSourcesOutput.  # noqa: E501


        :return: The instance_id of this InstanceInfoForDescribeMigrationSourcesOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this InstanceInfoForDescribeMigrationSourcesOutput.


        :param instance_id: The instance_id of this InstanceInfoForDescribeMigrationSourcesOutput.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def region_id(self):
        """Gets the region_id of this InstanceInfoForDescribeMigrationSourcesOutput.  # noqa: E501


        :return: The region_id of this InstanceInfoForDescribeMigrationSourcesOutput.  # noqa: E501
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this InstanceInfoForDescribeMigrationSourcesOutput.


        :param region_id: The region_id of this InstanceInfoForDescribeMigrationSourcesOutput.  # noqa: E501
        :type: str
        """

        self._region_id = region_id

    @property
    def virtio11_can_install(self):
        """Gets the virtio11_can_install of this InstanceInfoForDescribeMigrationSourcesOutput.  # noqa: E501


        :return: The virtio11_can_install of this InstanceInfoForDescribeMigrationSourcesOutput.  # noqa: E501
        :rtype: bool
        """
        return self._virtio11_can_install

    @virtio11_can_install.setter
    def virtio11_can_install(self, virtio11_can_install):
        """Sets the virtio11_can_install of this InstanceInfoForDescribeMigrationSourcesOutput.


        :param virtio11_can_install: The virtio11_can_install of this InstanceInfoForDescribeMigrationSourcesOutput.  # noqa: E501
        :type: bool
        """

        self._virtio11_can_install = virtio11_can_install

    @property
    def virtio11_install(self):
        """Gets the virtio11_install of this InstanceInfoForDescribeMigrationSourcesOutput.  # noqa: E501


        :return: The virtio11_install of this InstanceInfoForDescribeMigrationSourcesOutput.  # noqa: E501
        :rtype: bool
        """
        return self._virtio11_install

    @virtio11_install.setter
    def virtio11_install(self, virtio11_install):
        """Sets the virtio11_install of this InstanceInfoForDescribeMigrationSourcesOutput.


        :param virtio11_install: The virtio11_install of this InstanceInfoForDescribeMigrationSourcesOutput.  # noqa: E501
        :type: bool
        """

        self._virtio11_install = virtio11_install

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
        if issubclass(InstanceInfoForDescribeMigrationSourcesOutput, dict):
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
        if not isinstance(other, InstanceInfoForDescribeMigrationSourcesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InstanceInfoForDescribeMigrationSourcesOutput):
            return True

        return self.to_dict() != other.to_dict()
