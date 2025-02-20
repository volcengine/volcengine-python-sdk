# coding: utf-8

"""
    vke

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class NodeConfigForListNodePoolsOutput(object):
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
        'additional_container_storage_enabled': 'bool',
        'auto_renew': 'bool',
        'auto_renew_period': 'int',
        'data_volumes': 'list[DataVolumeForListNodePoolsOutput]',
        'hpc_cluster_ids': 'list[str]',
        'image_id': 'str',
        'initialize_script': 'str',
        'instance_charge_type': 'str',
        'instance_type_ids': 'list[str]',
        'name_prefix': 'str',
        'period': 'int',
        'project_name': 'str',
        'security': 'SecurityForListNodePoolsOutput',
        'subnet_ids': 'list[str]',
        'system_volume': 'SystemVolumeForListNodePoolsOutput',
        'tags': 'list[TagForListNodePoolsOutput]'
    }

    attribute_map = {
        'additional_container_storage_enabled': 'AdditionalContainerStorageEnabled',
        'auto_renew': 'AutoRenew',
        'auto_renew_period': 'AutoRenewPeriod',
        'data_volumes': 'DataVolumes',
        'hpc_cluster_ids': 'HpcClusterIds',
        'image_id': 'ImageId',
        'initialize_script': 'InitializeScript',
        'instance_charge_type': 'InstanceChargeType',
        'instance_type_ids': 'InstanceTypeIds',
        'name_prefix': 'NamePrefix',
        'period': 'Period',
        'project_name': 'ProjectName',
        'security': 'Security',
        'subnet_ids': 'SubnetIds',
        'system_volume': 'SystemVolume',
        'tags': 'Tags'
    }

    def __init__(self, additional_container_storage_enabled=None, auto_renew=None, auto_renew_period=None, data_volumes=None, hpc_cluster_ids=None, image_id=None, initialize_script=None, instance_charge_type=None, instance_type_ids=None, name_prefix=None, period=None, project_name=None, security=None, subnet_ids=None, system_volume=None, tags=None, _configuration=None):  # noqa: E501
        """NodeConfigForListNodePoolsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._additional_container_storage_enabled = None
        self._auto_renew = None
        self._auto_renew_period = None
        self._data_volumes = None
        self._hpc_cluster_ids = None
        self._image_id = None
        self._initialize_script = None
        self._instance_charge_type = None
        self._instance_type_ids = None
        self._name_prefix = None
        self._period = None
        self._project_name = None
        self._security = None
        self._subnet_ids = None
        self._system_volume = None
        self._tags = None
        self.discriminator = None

        if additional_container_storage_enabled is not None:
            self.additional_container_storage_enabled = additional_container_storage_enabled
        if auto_renew is not None:
            self.auto_renew = auto_renew
        if auto_renew_period is not None:
            self.auto_renew_period = auto_renew_period
        if data_volumes is not None:
            self.data_volumes = data_volumes
        if hpc_cluster_ids is not None:
            self.hpc_cluster_ids = hpc_cluster_ids
        if image_id is not None:
            self.image_id = image_id
        if initialize_script is not None:
            self.initialize_script = initialize_script
        if instance_charge_type is not None:
            self.instance_charge_type = instance_charge_type
        if instance_type_ids is not None:
            self.instance_type_ids = instance_type_ids
        if name_prefix is not None:
            self.name_prefix = name_prefix
        if period is not None:
            self.period = period
        if project_name is not None:
            self.project_name = project_name
        if security is not None:
            self.security = security
        if subnet_ids is not None:
            self.subnet_ids = subnet_ids
        if system_volume is not None:
            self.system_volume = system_volume
        if tags is not None:
            self.tags = tags

    @property
    def additional_container_storage_enabled(self):
        """Gets the additional_container_storage_enabled of this NodeConfigForListNodePoolsOutput.  # noqa: E501


        :return: The additional_container_storage_enabled of this NodeConfigForListNodePoolsOutput.  # noqa: E501
        :rtype: bool
        """
        return self._additional_container_storage_enabled

    @additional_container_storage_enabled.setter
    def additional_container_storage_enabled(self, additional_container_storage_enabled):
        """Sets the additional_container_storage_enabled of this NodeConfigForListNodePoolsOutput.


        :param additional_container_storage_enabled: The additional_container_storage_enabled of this NodeConfigForListNodePoolsOutput.  # noqa: E501
        :type: bool
        """

        self._additional_container_storage_enabled = additional_container_storage_enabled

    @property
    def auto_renew(self):
        """Gets the auto_renew of this NodeConfigForListNodePoolsOutput.  # noqa: E501


        :return: The auto_renew of this NodeConfigForListNodePoolsOutput.  # noqa: E501
        :rtype: bool
        """
        return self._auto_renew

    @auto_renew.setter
    def auto_renew(self, auto_renew):
        """Sets the auto_renew of this NodeConfigForListNodePoolsOutput.


        :param auto_renew: The auto_renew of this NodeConfigForListNodePoolsOutput.  # noqa: E501
        :type: bool
        """

        self._auto_renew = auto_renew

    @property
    def auto_renew_period(self):
        """Gets the auto_renew_period of this NodeConfigForListNodePoolsOutput.  # noqa: E501


        :return: The auto_renew_period of this NodeConfigForListNodePoolsOutput.  # noqa: E501
        :rtype: int
        """
        return self._auto_renew_period

    @auto_renew_period.setter
    def auto_renew_period(self, auto_renew_period):
        """Sets the auto_renew_period of this NodeConfigForListNodePoolsOutput.


        :param auto_renew_period: The auto_renew_period of this NodeConfigForListNodePoolsOutput.  # noqa: E501
        :type: int
        """

        self._auto_renew_period = auto_renew_period

    @property
    def data_volumes(self):
        """Gets the data_volumes of this NodeConfigForListNodePoolsOutput.  # noqa: E501


        :return: The data_volumes of this NodeConfigForListNodePoolsOutput.  # noqa: E501
        :rtype: list[DataVolumeForListNodePoolsOutput]
        """
        return self._data_volumes

    @data_volumes.setter
    def data_volumes(self, data_volumes):
        """Sets the data_volumes of this NodeConfigForListNodePoolsOutput.


        :param data_volumes: The data_volumes of this NodeConfigForListNodePoolsOutput.  # noqa: E501
        :type: list[DataVolumeForListNodePoolsOutput]
        """

        self._data_volumes = data_volumes

    @property
    def hpc_cluster_ids(self):
        """Gets the hpc_cluster_ids of this NodeConfigForListNodePoolsOutput.  # noqa: E501


        :return: The hpc_cluster_ids of this NodeConfigForListNodePoolsOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._hpc_cluster_ids

    @hpc_cluster_ids.setter
    def hpc_cluster_ids(self, hpc_cluster_ids):
        """Sets the hpc_cluster_ids of this NodeConfigForListNodePoolsOutput.


        :param hpc_cluster_ids: The hpc_cluster_ids of this NodeConfigForListNodePoolsOutput.  # noqa: E501
        :type: list[str]
        """

        self._hpc_cluster_ids = hpc_cluster_ids

    @property
    def image_id(self):
        """Gets the image_id of this NodeConfigForListNodePoolsOutput.  # noqa: E501


        :return: The image_id of this NodeConfigForListNodePoolsOutput.  # noqa: E501
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this NodeConfigForListNodePoolsOutput.


        :param image_id: The image_id of this NodeConfigForListNodePoolsOutput.  # noqa: E501
        :type: str
        """

        self._image_id = image_id

    @property
    def initialize_script(self):
        """Gets the initialize_script of this NodeConfigForListNodePoolsOutput.  # noqa: E501


        :return: The initialize_script of this NodeConfigForListNodePoolsOutput.  # noqa: E501
        :rtype: str
        """
        return self._initialize_script

    @initialize_script.setter
    def initialize_script(self, initialize_script):
        """Sets the initialize_script of this NodeConfigForListNodePoolsOutput.


        :param initialize_script: The initialize_script of this NodeConfigForListNodePoolsOutput.  # noqa: E501
        :type: str
        """

        self._initialize_script = initialize_script

    @property
    def instance_charge_type(self):
        """Gets the instance_charge_type of this NodeConfigForListNodePoolsOutput.  # noqa: E501


        :return: The instance_charge_type of this NodeConfigForListNodePoolsOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_charge_type

    @instance_charge_type.setter
    def instance_charge_type(self, instance_charge_type):
        """Sets the instance_charge_type of this NodeConfigForListNodePoolsOutput.


        :param instance_charge_type: The instance_charge_type of this NodeConfigForListNodePoolsOutput.  # noqa: E501
        :type: str
        """

        self._instance_charge_type = instance_charge_type

    @property
    def instance_type_ids(self):
        """Gets the instance_type_ids of this NodeConfigForListNodePoolsOutput.  # noqa: E501


        :return: The instance_type_ids of this NodeConfigForListNodePoolsOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._instance_type_ids

    @instance_type_ids.setter
    def instance_type_ids(self, instance_type_ids):
        """Sets the instance_type_ids of this NodeConfigForListNodePoolsOutput.


        :param instance_type_ids: The instance_type_ids of this NodeConfigForListNodePoolsOutput.  # noqa: E501
        :type: list[str]
        """

        self._instance_type_ids = instance_type_ids

    @property
    def name_prefix(self):
        """Gets the name_prefix of this NodeConfigForListNodePoolsOutput.  # noqa: E501


        :return: The name_prefix of this NodeConfigForListNodePoolsOutput.  # noqa: E501
        :rtype: str
        """
        return self._name_prefix

    @name_prefix.setter
    def name_prefix(self, name_prefix):
        """Sets the name_prefix of this NodeConfigForListNodePoolsOutput.


        :param name_prefix: The name_prefix of this NodeConfigForListNodePoolsOutput.  # noqa: E501
        :type: str
        """

        self._name_prefix = name_prefix

    @property
    def period(self):
        """Gets the period of this NodeConfigForListNodePoolsOutput.  # noqa: E501


        :return: The period of this NodeConfigForListNodePoolsOutput.  # noqa: E501
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this NodeConfigForListNodePoolsOutput.


        :param period: The period of this NodeConfigForListNodePoolsOutput.  # noqa: E501
        :type: int
        """

        self._period = period

    @property
    def project_name(self):
        """Gets the project_name of this NodeConfigForListNodePoolsOutput.  # noqa: E501


        :return: The project_name of this NodeConfigForListNodePoolsOutput.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this NodeConfigForListNodePoolsOutput.


        :param project_name: The project_name of this NodeConfigForListNodePoolsOutput.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def security(self):
        """Gets the security of this NodeConfigForListNodePoolsOutput.  # noqa: E501


        :return: The security of this NodeConfigForListNodePoolsOutput.  # noqa: E501
        :rtype: SecurityForListNodePoolsOutput
        """
        return self._security

    @security.setter
    def security(self, security):
        """Sets the security of this NodeConfigForListNodePoolsOutput.


        :param security: The security of this NodeConfigForListNodePoolsOutput.  # noqa: E501
        :type: SecurityForListNodePoolsOutput
        """

        self._security = security

    @property
    def subnet_ids(self):
        """Gets the subnet_ids of this NodeConfigForListNodePoolsOutput.  # noqa: E501


        :return: The subnet_ids of this NodeConfigForListNodePoolsOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._subnet_ids

    @subnet_ids.setter
    def subnet_ids(self, subnet_ids):
        """Sets the subnet_ids of this NodeConfigForListNodePoolsOutput.


        :param subnet_ids: The subnet_ids of this NodeConfigForListNodePoolsOutput.  # noqa: E501
        :type: list[str]
        """

        self._subnet_ids = subnet_ids

    @property
    def system_volume(self):
        """Gets the system_volume of this NodeConfigForListNodePoolsOutput.  # noqa: E501


        :return: The system_volume of this NodeConfigForListNodePoolsOutput.  # noqa: E501
        :rtype: SystemVolumeForListNodePoolsOutput
        """
        return self._system_volume

    @system_volume.setter
    def system_volume(self, system_volume):
        """Sets the system_volume of this NodeConfigForListNodePoolsOutput.


        :param system_volume: The system_volume of this NodeConfigForListNodePoolsOutput.  # noqa: E501
        :type: SystemVolumeForListNodePoolsOutput
        """

        self._system_volume = system_volume

    @property
    def tags(self):
        """Gets the tags of this NodeConfigForListNodePoolsOutput.  # noqa: E501


        :return: The tags of this NodeConfigForListNodePoolsOutput.  # noqa: E501
        :rtype: list[TagForListNodePoolsOutput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this NodeConfigForListNodePoolsOutput.


        :param tags: The tags of this NodeConfigForListNodePoolsOutput.  # noqa: E501
        :type: list[TagForListNodePoolsOutput]
        """

        self._tags = tags

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
        if issubclass(NodeConfigForListNodePoolsOutput, dict):
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
        if not isinstance(other, NodeConfigForListNodePoolsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NodeConfigForListNodePoolsOutput):
            return True

        return self.to_dict() != other.to_dict()
