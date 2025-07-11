# coding: utf-8

"""
    ecs

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class InstanceConfigForDescribeScheduledInstancesOutput(object):
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
        'description': 'str',
        'eip_address': 'EipAddressForDescribeScheduledInstancesOutput',
        'host_name': 'str',
        'hpc_cluster_id': 'str',
        'image_id': 'str',
        'instance_name': 'str',
        'instance_type_id': 'str',
        'key_pair_name': 'str',
        'network_interfaces_res': 'list[NetworkInterfacesReForDescribeScheduledInstancesOutput]',
        'project_name': 'str',
        'tags': 'list[TagForDescribeScheduledInstancesOutput]',
        'volumes': 'list[VolumeForDescribeScheduledInstancesOutput]',
        'zone_id': 'str'
    }

    attribute_map = {
        'description': 'Description',
        'eip_address': 'EipAddress',
        'host_name': 'HostName',
        'hpc_cluster_id': 'HpcClusterId',
        'image_id': 'ImageId',
        'instance_name': 'InstanceName',
        'instance_type_id': 'InstanceTypeId',
        'key_pair_name': 'KeyPairName',
        'network_interfaces_res': 'NetworkInterfacesRes',
        'project_name': 'ProjectName',
        'tags': 'Tags',
        'volumes': 'Volumes',
        'zone_id': 'ZoneId'
    }

    def __init__(self, description=None, eip_address=None, host_name=None, hpc_cluster_id=None, image_id=None, instance_name=None, instance_type_id=None, key_pair_name=None, network_interfaces_res=None, project_name=None, tags=None, volumes=None, zone_id=None, _configuration=None):  # noqa: E501
        """InstanceConfigForDescribeScheduledInstancesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._description = None
        self._eip_address = None
        self._host_name = None
        self._hpc_cluster_id = None
        self._image_id = None
        self._instance_name = None
        self._instance_type_id = None
        self._key_pair_name = None
        self._network_interfaces_res = None
        self._project_name = None
        self._tags = None
        self._volumes = None
        self._zone_id = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if eip_address is not None:
            self.eip_address = eip_address
        if host_name is not None:
            self.host_name = host_name
        if hpc_cluster_id is not None:
            self.hpc_cluster_id = hpc_cluster_id
        if image_id is not None:
            self.image_id = image_id
        if instance_name is not None:
            self.instance_name = instance_name
        if instance_type_id is not None:
            self.instance_type_id = instance_type_id
        if key_pair_name is not None:
            self.key_pair_name = key_pair_name
        if network_interfaces_res is not None:
            self.network_interfaces_res = network_interfaces_res
        if project_name is not None:
            self.project_name = project_name
        if tags is not None:
            self.tags = tags
        if volumes is not None:
            self.volumes = volumes
        if zone_id is not None:
            self.zone_id = zone_id

    @property
    def description(self):
        """Gets the description of this InstanceConfigForDescribeScheduledInstancesOutput.  # noqa: E501


        :return: The description of this InstanceConfigForDescribeScheduledInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InstanceConfigForDescribeScheduledInstancesOutput.


        :param description: The description of this InstanceConfigForDescribeScheduledInstancesOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def eip_address(self):
        """Gets the eip_address of this InstanceConfigForDescribeScheduledInstancesOutput.  # noqa: E501


        :return: The eip_address of this InstanceConfigForDescribeScheduledInstancesOutput.  # noqa: E501
        :rtype: EipAddressForDescribeScheduledInstancesOutput
        """
        return self._eip_address

    @eip_address.setter
    def eip_address(self, eip_address):
        """Sets the eip_address of this InstanceConfigForDescribeScheduledInstancesOutput.


        :param eip_address: The eip_address of this InstanceConfigForDescribeScheduledInstancesOutput.  # noqa: E501
        :type: EipAddressForDescribeScheduledInstancesOutput
        """

        self._eip_address = eip_address

    @property
    def host_name(self):
        """Gets the host_name of this InstanceConfigForDescribeScheduledInstancesOutput.  # noqa: E501


        :return: The host_name of this InstanceConfigForDescribeScheduledInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this InstanceConfigForDescribeScheduledInstancesOutput.


        :param host_name: The host_name of this InstanceConfigForDescribeScheduledInstancesOutput.  # noqa: E501
        :type: str
        """

        self._host_name = host_name

    @property
    def hpc_cluster_id(self):
        """Gets the hpc_cluster_id of this InstanceConfigForDescribeScheduledInstancesOutput.  # noqa: E501


        :return: The hpc_cluster_id of this InstanceConfigForDescribeScheduledInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._hpc_cluster_id

    @hpc_cluster_id.setter
    def hpc_cluster_id(self, hpc_cluster_id):
        """Sets the hpc_cluster_id of this InstanceConfigForDescribeScheduledInstancesOutput.


        :param hpc_cluster_id: The hpc_cluster_id of this InstanceConfigForDescribeScheduledInstancesOutput.  # noqa: E501
        :type: str
        """

        self._hpc_cluster_id = hpc_cluster_id

    @property
    def image_id(self):
        """Gets the image_id of this InstanceConfigForDescribeScheduledInstancesOutput.  # noqa: E501


        :return: The image_id of this InstanceConfigForDescribeScheduledInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this InstanceConfigForDescribeScheduledInstancesOutput.


        :param image_id: The image_id of this InstanceConfigForDescribeScheduledInstancesOutput.  # noqa: E501
        :type: str
        """

        self._image_id = image_id

    @property
    def instance_name(self):
        """Gets the instance_name of this InstanceConfigForDescribeScheduledInstancesOutput.  # noqa: E501


        :return: The instance_name of this InstanceConfigForDescribeScheduledInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this InstanceConfigForDescribeScheduledInstancesOutput.


        :param instance_name: The instance_name of this InstanceConfigForDescribeScheduledInstancesOutput.  # noqa: E501
        :type: str
        """

        self._instance_name = instance_name

    @property
    def instance_type_id(self):
        """Gets the instance_type_id of this InstanceConfigForDescribeScheduledInstancesOutput.  # noqa: E501


        :return: The instance_type_id of this InstanceConfigForDescribeScheduledInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_type_id

    @instance_type_id.setter
    def instance_type_id(self, instance_type_id):
        """Sets the instance_type_id of this InstanceConfigForDescribeScheduledInstancesOutput.


        :param instance_type_id: The instance_type_id of this InstanceConfigForDescribeScheduledInstancesOutput.  # noqa: E501
        :type: str
        """

        self._instance_type_id = instance_type_id

    @property
    def key_pair_name(self):
        """Gets the key_pair_name of this InstanceConfigForDescribeScheduledInstancesOutput.  # noqa: E501


        :return: The key_pair_name of this InstanceConfigForDescribeScheduledInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._key_pair_name

    @key_pair_name.setter
    def key_pair_name(self, key_pair_name):
        """Sets the key_pair_name of this InstanceConfigForDescribeScheduledInstancesOutput.


        :param key_pair_name: The key_pair_name of this InstanceConfigForDescribeScheduledInstancesOutput.  # noqa: E501
        :type: str
        """

        self._key_pair_name = key_pair_name

    @property
    def network_interfaces_res(self):
        """Gets the network_interfaces_res of this InstanceConfigForDescribeScheduledInstancesOutput.  # noqa: E501


        :return: The network_interfaces_res of this InstanceConfigForDescribeScheduledInstancesOutput.  # noqa: E501
        :rtype: list[NetworkInterfacesReForDescribeScheduledInstancesOutput]
        """
        return self._network_interfaces_res

    @network_interfaces_res.setter
    def network_interfaces_res(self, network_interfaces_res):
        """Sets the network_interfaces_res of this InstanceConfigForDescribeScheduledInstancesOutput.


        :param network_interfaces_res: The network_interfaces_res of this InstanceConfigForDescribeScheduledInstancesOutput.  # noqa: E501
        :type: list[NetworkInterfacesReForDescribeScheduledInstancesOutput]
        """

        self._network_interfaces_res = network_interfaces_res

    @property
    def project_name(self):
        """Gets the project_name of this InstanceConfigForDescribeScheduledInstancesOutput.  # noqa: E501


        :return: The project_name of this InstanceConfigForDescribeScheduledInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this InstanceConfigForDescribeScheduledInstancesOutput.


        :param project_name: The project_name of this InstanceConfigForDescribeScheduledInstancesOutput.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def tags(self):
        """Gets the tags of this InstanceConfigForDescribeScheduledInstancesOutput.  # noqa: E501


        :return: The tags of this InstanceConfigForDescribeScheduledInstancesOutput.  # noqa: E501
        :rtype: list[TagForDescribeScheduledInstancesOutput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this InstanceConfigForDescribeScheduledInstancesOutput.


        :param tags: The tags of this InstanceConfigForDescribeScheduledInstancesOutput.  # noqa: E501
        :type: list[TagForDescribeScheduledInstancesOutput]
        """

        self._tags = tags

    @property
    def volumes(self):
        """Gets the volumes of this InstanceConfigForDescribeScheduledInstancesOutput.  # noqa: E501


        :return: The volumes of this InstanceConfigForDescribeScheduledInstancesOutput.  # noqa: E501
        :rtype: list[VolumeForDescribeScheduledInstancesOutput]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this InstanceConfigForDescribeScheduledInstancesOutput.


        :param volumes: The volumes of this InstanceConfigForDescribeScheduledInstancesOutput.  # noqa: E501
        :type: list[VolumeForDescribeScheduledInstancesOutput]
        """

        self._volumes = volumes

    @property
    def zone_id(self):
        """Gets the zone_id of this InstanceConfigForDescribeScheduledInstancesOutput.  # noqa: E501


        :return: The zone_id of this InstanceConfigForDescribeScheduledInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this InstanceConfigForDescribeScheduledInstancesOutput.


        :param zone_id: The zone_id of this InstanceConfigForDescribeScheduledInstancesOutput.  # noqa: E501
        :type: str
        """

        self._zone_id = zone_id

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
        if issubclass(InstanceConfigForDescribeScheduledInstancesOutput, dict):
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
        if not isinstance(other, InstanceConfigForDescribeScheduledInstancesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InstanceConfigForDescribeScheduledInstancesOutput):
            return True

        return self.to_dict() != other.to_dict()
