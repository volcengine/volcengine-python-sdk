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


class ModifyScalingConfigurationRequest(object):
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
        'eip': 'EipForModifyScalingConfigurationInput',
        'host_name': 'str',
        'hpc_cluster_id': 'str',
        'image_id': 'str',
        'instance_description': 'str',
        'instance_name': 'str',
        'instance_types': 'list[str]',
        'ipv6_address_count': 'int',
        'key_pair_name': 'str',
        'password': 'str',
        'project_name': 'str',
        'scaling_configuration_id': 'str',
        'scaling_configuration_name': 'str',
        'security_enhancement_strategy': 'str',
        'security_group_ids': 'list[str]',
        'spot_strategy': 'str',
        'tags': 'str',
        'user_data': 'str',
        'volumes': 'list[VolumeForModifyScalingConfigurationInput]',
        'zone_id': 'str'
    }

    attribute_map = {
        'eip': 'Eip',
        'host_name': 'HostName',
        'hpc_cluster_id': 'HpcClusterId',
        'image_id': 'ImageId',
        'instance_description': 'InstanceDescription',
        'instance_name': 'InstanceName',
        'instance_types': 'InstanceTypes',
        'ipv6_address_count': 'Ipv6AddressCount',
        'key_pair_name': 'KeyPairName',
        'password': 'Password',
        'project_name': 'ProjectName',
        'scaling_configuration_id': 'ScalingConfigurationId',
        'scaling_configuration_name': 'ScalingConfigurationName',
        'security_enhancement_strategy': 'SecurityEnhancementStrategy',
        'security_group_ids': 'SecurityGroupIds',
        'spot_strategy': 'SpotStrategy',
        'tags': 'Tags',
        'user_data': 'UserData',
        'volumes': 'Volumes',
        'zone_id': 'ZoneId'
    }

    def __init__(self, eip=None, host_name=None, hpc_cluster_id=None, image_id=None, instance_description=None, instance_name=None, instance_types=None, ipv6_address_count=None, key_pair_name=None, password=None, project_name=None, scaling_configuration_id=None, scaling_configuration_name=None, security_enhancement_strategy=None, security_group_ids=None, spot_strategy=None, tags=None, user_data=None, volumes=None, zone_id=None, _configuration=None):  # noqa: E501
        """ModifyScalingConfigurationRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._eip = None
        self._host_name = None
        self._hpc_cluster_id = None
        self._image_id = None
        self._instance_description = None
        self._instance_name = None
        self._instance_types = None
        self._ipv6_address_count = None
        self._key_pair_name = None
        self._password = None
        self._project_name = None
        self._scaling_configuration_id = None
        self._scaling_configuration_name = None
        self._security_enhancement_strategy = None
        self._security_group_ids = None
        self._spot_strategy = None
        self._tags = None
        self._user_data = None
        self._volumes = None
        self._zone_id = None
        self.discriminator = None

        if eip is not None:
            self.eip = eip
        if host_name is not None:
            self.host_name = host_name
        if hpc_cluster_id is not None:
            self.hpc_cluster_id = hpc_cluster_id
        if image_id is not None:
            self.image_id = image_id
        if instance_description is not None:
            self.instance_description = instance_description
        if instance_name is not None:
            self.instance_name = instance_name
        if instance_types is not None:
            self.instance_types = instance_types
        if ipv6_address_count is not None:
            self.ipv6_address_count = ipv6_address_count
        if key_pair_name is not None:
            self.key_pair_name = key_pair_name
        if password is not None:
            self.password = password
        if project_name is not None:
            self.project_name = project_name
        if scaling_configuration_id is not None:
            self.scaling_configuration_id = scaling_configuration_id
        if scaling_configuration_name is not None:
            self.scaling_configuration_name = scaling_configuration_name
        if security_enhancement_strategy is not None:
            self.security_enhancement_strategy = security_enhancement_strategy
        if security_group_ids is not None:
            self.security_group_ids = security_group_ids
        if spot_strategy is not None:
            self.spot_strategy = spot_strategy
        if tags is not None:
            self.tags = tags
        if user_data is not None:
            self.user_data = user_data
        if volumes is not None:
            self.volumes = volumes
        if zone_id is not None:
            self.zone_id = zone_id

    @property
    def eip(self):
        """Gets the eip of this ModifyScalingConfigurationRequest.  # noqa: E501


        :return: The eip of this ModifyScalingConfigurationRequest.  # noqa: E501
        :rtype: EipForModifyScalingConfigurationInput
        """
        return self._eip

    @eip.setter
    def eip(self, eip):
        """Sets the eip of this ModifyScalingConfigurationRequest.


        :param eip: The eip of this ModifyScalingConfigurationRequest.  # noqa: E501
        :type: EipForModifyScalingConfigurationInput
        """

        self._eip = eip

    @property
    def host_name(self):
        """Gets the host_name of this ModifyScalingConfigurationRequest.  # noqa: E501


        :return: The host_name of this ModifyScalingConfigurationRequest.  # noqa: E501
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this ModifyScalingConfigurationRequest.


        :param host_name: The host_name of this ModifyScalingConfigurationRequest.  # noqa: E501
        :type: str
        """

        self._host_name = host_name

    @property
    def hpc_cluster_id(self):
        """Gets the hpc_cluster_id of this ModifyScalingConfigurationRequest.  # noqa: E501


        :return: The hpc_cluster_id of this ModifyScalingConfigurationRequest.  # noqa: E501
        :rtype: str
        """
        return self._hpc_cluster_id

    @hpc_cluster_id.setter
    def hpc_cluster_id(self, hpc_cluster_id):
        """Sets the hpc_cluster_id of this ModifyScalingConfigurationRequest.


        :param hpc_cluster_id: The hpc_cluster_id of this ModifyScalingConfigurationRequest.  # noqa: E501
        :type: str
        """

        self._hpc_cluster_id = hpc_cluster_id

    @property
    def image_id(self):
        """Gets the image_id of this ModifyScalingConfigurationRequest.  # noqa: E501


        :return: The image_id of this ModifyScalingConfigurationRequest.  # noqa: E501
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this ModifyScalingConfigurationRequest.


        :param image_id: The image_id of this ModifyScalingConfigurationRequest.  # noqa: E501
        :type: str
        """

        self._image_id = image_id

    @property
    def instance_description(self):
        """Gets the instance_description of this ModifyScalingConfigurationRequest.  # noqa: E501


        :return: The instance_description of this ModifyScalingConfigurationRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_description

    @instance_description.setter
    def instance_description(self, instance_description):
        """Sets the instance_description of this ModifyScalingConfigurationRequest.


        :param instance_description: The instance_description of this ModifyScalingConfigurationRequest.  # noqa: E501
        :type: str
        """

        self._instance_description = instance_description

    @property
    def instance_name(self):
        """Gets the instance_name of this ModifyScalingConfigurationRequest.  # noqa: E501


        :return: The instance_name of this ModifyScalingConfigurationRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this ModifyScalingConfigurationRequest.


        :param instance_name: The instance_name of this ModifyScalingConfigurationRequest.  # noqa: E501
        :type: str
        """

        self._instance_name = instance_name

    @property
    def instance_types(self):
        """Gets the instance_types of this ModifyScalingConfigurationRequest.  # noqa: E501


        :return: The instance_types of this ModifyScalingConfigurationRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._instance_types

    @instance_types.setter
    def instance_types(self, instance_types):
        """Sets the instance_types of this ModifyScalingConfigurationRequest.


        :param instance_types: The instance_types of this ModifyScalingConfigurationRequest.  # noqa: E501
        :type: list[str]
        """

        self._instance_types = instance_types

    @property
    def ipv6_address_count(self):
        """Gets the ipv6_address_count of this ModifyScalingConfigurationRequest.  # noqa: E501


        :return: The ipv6_address_count of this ModifyScalingConfigurationRequest.  # noqa: E501
        :rtype: int
        """
        return self._ipv6_address_count

    @ipv6_address_count.setter
    def ipv6_address_count(self, ipv6_address_count):
        """Sets the ipv6_address_count of this ModifyScalingConfigurationRequest.


        :param ipv6_address_count: The ipv6_address_count of this ModifyScalingConfigurationRequest.  # noqa: E501
        :type: int
        """

        self._ipv6_address_count = ipv6_address_count

    @property
    def key_pair_name(self):
        """Gets the key_pair_name of this ModifyScalingConfigurationRequest.  # noqa: E501


        :return: The key_pair_name of this ModifyScalingConfigurationRequest.  # noqa: E501
        :rtype: str
        """
        return self._key_pair_name

    @key_pair_name.setter
    def key_pair_name(self, key_pair_name):
        """Sets the key_pair_name of this ModifyScalingConfigurationRequest.


        :param key_pair_name: The key_pair_name of this ModifyScalingConfigurationRequest.  # noqa: E501
        :type: str
        """

        self._key_pair_name = key_pair_name

    @property
    def password(self):
        """Gets the password of this ModifyScalingConfigurationRequest.  # noqa: E501


        :return: The password of this ModifyScalingConfigurationRequest.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this ModifyScalingConfigurationRequest.


        :param password: The password of this ModifyScalingConfigurationRequest.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def project_name(self):
        """Gets the project_name of this ModifyScalingConfigurationRequest.  # noqa: E501


        :return: The project_name of this ModifyScalingConfigurationRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this ModifyScalingConfigurationRequest.


        :param project_name: The project_name of this ModifyScalingConfigurationRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def scaling_configuration_id(self):
        """Gets the scaling_configuration_id of this ModifyScalingConfigurationRequest.  # noqa: E501


        :return: The scaling_configuration_id of this ModifyScalingConfigurationRequest.  # noqa: E501
        :rtype: str
        """
        return self._scaling_configuration_id

    @scaling_configuration_id.setter
    def scaling_configuration_id(self, scaling_configuration_id):
        """Sets the scaling_configuration_id of this ModifyScalingConfigurationRequest.


        :param scaling_configuration_id: The scaling_configuration_id of this ModifyScalingConfigurationRequest.  # noqa: E501
        :type: str
        """

        self._scaling_configuration_id = scaling_configuration_id

    @property
    def scaling_configuration_name(self):
        """Gets the scaling_configuration_name of this ModifyScalingConfigurationRequest.  # noqa: E501


        :return: The scaling_configuration_name of this ModifyScalingConfigurationRequest.  # noqa: E501
        :rtype: str
        """
        return self._scaling_configuration_name

    @scaling_configuration_name.setter
    def scaling_configuration_name(self, scaling_configuration_name):
        """Sets the scaling_configuration_name of this ModifyScalingConfigurationRequest.


        :param scaling_configuration_name: The scaling_configuration_name of this ModifyScalingConfigurationRequest.  # noqa: E501
        :type: str
        """

        self._scaling_configuration_name = scaling_configuration_name

    @property
    def security_enhancement_strategy(self):
        """Gets the security_enhancement_strategy of this ModifyScalingConfigurationRequest.  # noqa: E501


        :return: The security_enhancement_strategy of this ModifyScalingConfigurationRequest.  # noqa: E501
        :rtype: str
        """
        return self._security_enhancement_strategy

    @security_enhancement_strategy.setter
    def security_enhancement_strategy(self, security_enhancement_strategy):
        """Sets the security_enhancement_strategy of this ModifyScalingConfigurationRequest.


        :param security_enhancement_strategy: The security_enhancement_strategy of this ModifyScalingConfigurationRequest.  # noqa: E501
        :type: str
        """

        self._security_enhancement_strategy = security_enhancement_strategy

    @property
    def security_group_ids(self):
        """Gets the security_group_ids of this ModifyScalingConfigurationRequest.  # noqa: E501


        :return: The security_group_ids of this ModifyScalingConfigurationRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._security_group_ids

    @security_group_ids.setter
    def security_group_ids(self, security_group_ids):
        """Sets the security_group_ids of this ModifyScalingConfigurationRequest.


        :param security_group_ids: The security_group_ids of this ModifyScalingConfigurationRequest.  # noqa: E501
        :type: list[str]
        """

        self._security_group_ids = security_group_ids

    @property
    def spot_strategy(self):
        """Gets the spot_strategy of this ModifyScalingConfigurationRequest.  # noqa: E501


        :return: The spot_strategy of this ModifyScalingConfigurationRequest.  # noqa: E501
        :rtype: str
        """
        return self._spot_strategy

    @spot_strategy.setter
    def spot_strategy(self, spot_strategy):
        """Sets the spot_strategy of this ModifyScalingConfigurationRequest.


        :param spot_strategy: The spot_strategy of this ModifyScalingConfigurationRequest.  # noqa: E501
        :type: str
        """

        self._spot_strategy = spot_strategy

    @property
    def tags(self):
        """Gets the tags of this ModifyScalingConfigurationRequest.  # noqa: E501


        :return: The tags of this ModifyScalingConfigurationRequest.  # noqa: E501
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ModifyScalingConfigurationRequest.


        :param tags: The tags of this ModifyScalingConfigurationRequest.  # noqa: E501
        :type: str
        """

        self._tags = tags

    @property
    def user_data(self):
        """Gets the user_data of this ModifyScalingConfigurationRequest.  # noqa: E501


        :return: The user_data of this ModifyScalingConfigurationRequest.  # noqa: E501
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this ModifyScalingConfigurationRequest.


        :param user_data: The user_data of this ModifyScalingConfigurationRequest.  # noqa: E501
        :type: str
        """

        self._user_data = user_data

    @property
    def volumes(self):
        """Gets the volumes of this ModifyScalingConfigurationRequest.  # noqa: E501


        :return: The volumes of this ModifyScalingConfigurationRequest.  # noqa: E501
        :rtype: list[VolumeForModifyScalingConfigurationInput]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this ModifyScalingConfigurationRequest.


        :param volumes: The volumes of this ModifyScalingConfigurationRequest.  # noqa: E501
        :type: list[VolumeForModifyScalingConfigurationInput]
        """

        self._volumes = volumes

    @property
    def zone_id(self):
        """Gets the zone_id of this ModifyScalingConfigurationRequest.  # noqa: E501


        :return: The zone_id of this ModifyScalingConfigurationRequest.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this ModifyScalingConfigurationRequest.


        :param zone_id: The zone_id of this ModifyScalingConfigurationRequest.  # noqa: E501
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
        if issubclass(ModifyScalingConfigurationRequest, dict):
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
        if not isinstance(other, ModifyScalingConfigurationRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModifyScalingConfigurationRequest):
            return True

        return self.to_dict() != other.to_dict()
