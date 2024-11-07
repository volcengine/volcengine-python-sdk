# coding: utf-8

"""
    escloud

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class InstanceConfigurationForDescribeInstanceOutput(object):
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
        'admin_user_name': 'str',
        'charge_type': 'str',
        'cold_node_number': 'int',
        'cold_node_resource_spec': 'ColdNodeResourceSpecForDescribeInstanceOutput',
        'cold_node_storage_spec': 'ColdNodeStorageSpecForDescribeInstanceOutput',
        'coordinator_node_number': 'int',
        'coordinator_node_resource_spec': 'CoordinatorNodeResourceSpecForDescribeInstanceOutput',
        'coordinator_node_storage_spec': 'CoordinatorNodeStorageSpecForDescribeInstanceOutput',
        'enable_https': 'bool',
        'enable_pure_master': 'bool',
        'hot_node_number': 'int',
        'hot_node_resource_spec': 'HotNodeResourceSpecForDescribeInstanceOutput',
        'hot_node_storage_spec': 'HotNodeStorageSpecForDescribeInstanceOutput',
        'instance_name': 'str',
        'kibana_node_number': 'int',
        'kibana_node_resource_spec': 'KibanaNodeResourceSpecForDescribeInstanceOutput',
        'master_node_number': 'int',
        'master_node_resource_spec': 'MasterNodeResourceSpecForDescribeInstanceOutput',
        'master_node_storage_spec': 'MasterNodeStorageSpecForDescribeInstanceOutput',
        'project_name': 'str',
        'region_id': 'str',
        'subnet': 'SubnetForDescribeInstanceOutput',
        'vpc': 'VPCForDescribeInstanceOutput',
        'version': 'str',
        'warm_node_number': 'int',
        'warm_node_resource_spec': 'WarmNodeResourceSpecForDescribeInstanceOutput',
        'warm_node_storage_spec': 'WarmNodeStorageSpecForDescribeInstanceOutput',
        'zone_id': 'str',
        'zone_number': 'int'
    }

    attribute_map = {
        'admin_user_name': 'AdminUserName',
        'charge_type': 'ChargeType',
        'cold_node_number': 'ColdNodeNumber',
        'cold_node_resource_spec': 'ColdNodeResourceSpec',
        'cold_node_storage_spec': 'ColdNodeStorageSpec',
        'coordinator_node_number': 'CoordinatorNodeNumber',
        'coordinator_node_resource_spec': 'CoordinatorNodeResourceSpec',
        'coordinator_node_storage_spec': 'CoordinatorNodeStorageSpec',
        'enable_https': 'EnableHttps',
        'enable_pure_master': 'EnablePureMaster',
        'hot_node_number': 'HotNodeNumber',
        'hot_node_resource_spec': 'HotNodeResourceSpec',
        'hot_node_storage_spec': 'HotNodeStorageSpec',
        'instance_name': 'InstanceName',
        'kibana_node_number': 'KibanaNodeNumber',
        'kibana_node_resource_spec': 'KibanaNodeResourceSpec',
        'master_node_number': 'MasterNodeNumber',
        'master_node_resource_spec': 'MasterNodeResourceSpec',
        'master_node_storage_spec': 'MasterNodeStorageSpec',
        'project_name': 'ProjectName',
        'region_id': 'RegionId',
        'subnet': 'Subnet',
        'vpc': 'VPC',
        'version': 'Version',
        'warm_node_number': 'WarmNodeNumber',
        'warm_node_resource_spec': 'WarmNodeResourceSpec',
        'warm_node_storage_spec': 'WarmNodeStorageSpec',
        'zone_id': 'ZoneId',
        'zone_number': 'ZoneNumber'
    }

    def __init__(self, admin_user_name=None, charge_type=None, cold_node_number=None, cold_node_resource_spec=None, cold_node_storage_spec=None, coordinator_node_number=None, coordinator_node_resource_spec=None, coordinator_node_storage_spec=None, enable_https=None, enable_pure_master=None, hot_node_number=None, hot_node_resource_spec=None, hot_node_storage_spec=None, instance_name=None, kibana_node_number=None, kibana_node_resource_spec=None, master_node_number=None, master_node_resource_spec=None, master_node_storage_spec=None, project_name=None, region_id=None, subnet=None, vpc=None, version=None, warm_node_number=None, warm_node_resource_spec=None, warm_node_storage_spec=None, zone_id=None, zone_number=None, _configuration=None):  # noqa: E501
        """InstanceConfigurationForDescribeInstanceOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._admin_user_name = None
        self._charge_type = None
        self._cold_node_number = None
        self._cold_node_resource_spec = None
        self._cold_node_storage_spec = None
        self._coordinator_node_number = None
        self._coordinator_node_resource_spec = None
        self._coordinator_node_storage_spec = None
        self._enable_https = None
        self._enable_pure_master = None
        self._hot_node_number = None
        self._hot_node_resource_spec = None
        self._hot_node_storage_spec = None
        self._instance_name = None
        self._kibana_node_number = None
        self._kibana_node_resource_spec = None
        self._master_node_number = None
        self._master_node_resource_spec = None
        self._master_node_storage_spec = None
        self._project_name = None
        self._region_id = None
        self._subnet = None
        self._vpc = None
        self._version = None
        self._warm_node_number = None
        self._warm_node_resource_spec = None
        self._warm_node_storage_spec = None
        self._zone_id = None
        self._zone_number = None
        self.discriminator = None

        if admin_user_name is not None:
            self.admin_user_name = admin_user_name
        if charge_type is not None:
            self.charge_type = charge_type
        if cold_node_number is not None:
            self.cold_node_number = cold_node_number
        if cold_node_resource_spec is not None:
            self.cold_node_resource_spec = cold_node_resource_spec
        if cold_node_storage_spec is not None:
            self.cold_node_storage_spec = cold_node_storage_spec
        if coordinator_node_number is not None:
            self.coordinator_node_number = coordinator_node_number
        if coordinator_node_resource_spec is not None:
            self.coordinator_node_resource_spec = coordinator_node_resource_spec
        if coordinator_node_storage_spec is not None:
            self.coordinator_node_storage_spec = coordinator_node_storage_spec
        if enable_https is not None:
            self.enable_https = enable_https
        if enable_pure_master is not None:
            self.enable_pure_master = enable_pure_master
        if hot_node_number is not None:
            self.hot_node_number = hot_node_number
        if hot_node_resource_spec is not None:
            self.hot_node_resource_spec = hot_node_resource_spec
        if hot_node_storage_spec is not None:
            self.hot_node_storage_spec = hot_node_storage_spec
        if instance_name is not None:
            self.instance_name = instance_name
        if kibana_node_number is not None:
            self.kibana_node_number = kibana_node_number
        if kibana_node_resource_spec is not None:
            self.kibana_node_resource_spec = kibana_node_resource_spec
        if master_node_number is not None:
            self.master_node_number = master_node_number
        if master_node_resource_spec is not None:
            self.master_node_resource_spec = master_node_resource_spec
        if master_node_storage_spec is not None:
            self.master_node_storage_spec = master_node_storage_spec
        if project_name is not None:
            self.project_name = project_name
        if region_id is not None:
            self.region_id = region_id
        if subnet is not None:
            self.subnet = subnet
        if vpc is not None:
            self.vpc = vpc
        if version is not None:
            self.version = version
        if warm_node_number is not None:
            self.warm_node_number = warm_node_number
        if warm_node_resource_spec is not None:
            self.warm_node_resource_spec = warm_node_resource_spec
        if warm_node_storage_spec is not None:
            self.warm_node_storage_spec = warm_node_storage_spec
        if zone_id is not None:
            self.zone_id = zone_id
        if zone_number is not None:
            self.zone_number = zone_number

    @property
    def admin_user_name(self):
        """Gets the admin_user_name of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501


        :return: The admin_user_name of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :rtype: str
        """
        return self._admin_user_name

    @admin_user_name.setter
    def admin_user_name(self, admin_user_name):
        """Sets the admin_user_name of this InstanceConfigurationForDescribeInstanceOutput.


        :param admin_user_name: The admin_user_name of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :type: str
        """

        self._admin_user_name = admin_user_name

    @property
    def charge_type(self):
        """Gets the charge_type of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501


        :return: The charge_type of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :rtype: str
        """
        return self._charge_type

    @charge_type.setter
    def charge_type(self, charge_type):
        """Sets the charge_type of this InstanceConfigurationForDescribeInstanceOutput.


        :param charge_type: The charge_type of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :type: str
        """

        self._charge_type = charge_type

    @property
    def cold_node_number(self):
        """Gets the cold_node_number of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501


        :return: The cold_node_number of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :rtype: int
        """
        return self._cold_node_number

    @cold_node_number.setter
    def cold_node_number(self, cold_node_number):
        """Sets the cold_node_number of this InstanceConfigurationForDescribeInstanceOutput.


        :param cold_node_number: The cold_node_number of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :type: int
        """

        self._cold_node_number = cold_node_number

    @property
    def cold_node_resource_spec(self):
        """Gets the cold_node_resource_spec of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501


        :return: The cold_node_resource_spec of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :rtype: ColdNodeResourceSpecForDescribeInstanceOutput
        """
        return self._cold_node_resource_spec

    @cold_node_resource_spec.setter
    def cold_node_resource_spec(self, cold_node_resource_spec):
        """Sets the cold_node_resource_spec of this InstanceConfigurationForDescribeInstanceOutput.


        :param cold_node_resource_spec: The cold_node_resource_spec of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :type: ColdNodeResourceSpecForDescribeInstanceOutput
        """

        self._cold_node_resource_spec = cold_node_resource_spec

    @property
    def cold_node_storage_spec(self):
        """Gets the cold_node_storage_spec of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501


        :return: The cold_node_storage_spec of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :rtype: ColdNodeStorageSpecForDescribeInstanceOutput
        """
        return self._cold_node_storage_spec

    @cold_node_storage_spec.setter
    def cold_node_storage_spec(self, cold_node_storage_spec):
        """Sets the cold_node_storage_spec of this InstanceConfigurationForDescribeInstanceOutput.


        :param cold_node_storage_spec: The cold_node_storage_spec of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :type: ColdNodeStorageSpecForDescribeInstanceOutput
        """

        self._cold_node_storage_spec = cold_node_storage_spec

    @property
    def coordinator_node_number(self):
        """Gets the coordinator_node_number of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501


        :return: The coordinator_node_number of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :rtype: int
        """
        return self._coordinator_node_number

    @coordinator_node_number.setter
    def coordinator_node_number(self, coordinator_node_number):
        """Sets the coordinator_node_number of this InstanceConfigurationForDescribeInstanceOutput.


        :param coordinator_node_number: The coordinator_node_number of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :type: int
        """

        self._coordinator_node_number = coordinator_node_number

    @property
    def coordinator_node_resource_spec(self):
        """Gets the coordinator_node_resource_spec of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501


        :return: The coordinator_node_resource_spec of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :rtype: CoordinatorNodeResourceSpecForDescribeInstanceOutput
        """
        return self._coordinator_node_resource_spec

    @coordinator_node_resource_spec.setter
    def coordinator_node_resource_spec(self, coordinator_node_resource_spec):
        """Sets the coordinator_node_resource_spec of this InstanceConfigurationForDescribeInstanceOutput.


        :param coordinator_node_resource_spec: The coordinator_node_resource_spec of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :type: CoordinatorNodeResourceSpecForDescribeInstanceOutput
        """

        self._coordinator_node_resource_spec = coordinator_node_resource_spec

    @property
    def coordinator_node_storage_spec(self):
        """Gets the coordinator_node_storage_spec of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501


        :return: The coordinator_node_storage_spec of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :rtype: CoordinatorNodeStorageSpecForDescribeInstanceOutput
        """
        return self._coordinator_node_storage_spec

    @coordinator_node_storage_spec.setter
    def coordinator_node_storage_spec(self, coordinator_node_storage_spec):
        """Sets the coordinator_node_storage_spec of this InstanceConfigurationForDescribeInstanceOutput.


        :param coordinator_node_storage_spec: The coordinator_node_storage_spec of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :type: CoordinatorNodeStorageSpecForDescribeInstanceOutput
        """

        self._coordinator_node_storage_spec = coordinator_node_storage_spec

    @property
    def enable_https(self):
        """Gets the enable_https of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501


        :return: The enable_https of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :rtype: bool
        """
        return self._enable_https

    @enable_https.setter
    def enable_https(self, enable_https):
        """Sets the enable_https of this InstanceConfigurationForDescribeInstanceOutput.


        :param enable_https: The enable_https of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :type: bool
        """

        self._enable_https = enable_https

    @property
    def enable_pure_master(self):
        """Gets the enable_pure_master of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501


        :return: The enable_pure_master of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :rtype: bool
        """
        return self._enable_pure_master

    @enable_pure_master.setter
    def enable_pure_master(self, enable_pure_master):
        """Sets the enable_pure_master of this InstanceConfigurationForDescribeInstanceOutput.


        :param enable_pure_master: The enable_pure_master of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :type: bool
        """

        self._enable_pure_master = enable_pure_master

    @property
    def hot_node_number(self):
        """Gets the hot_node_number of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501


        :return: The hot_node_number of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :rtype: int
        """
        return self._hot_node_number

    @hot_node_number.setter
    def hot_node_number(self, hot_node_number):
        """Sets the hot_node_number of this InstanceConfigurationForDescribeInstanceOutput.


        :param hot_node_number: The hot_node_number of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :type: int
        """

        self._hot_node_number = hot_node_number

    @property
    def hot_node_resource_spec(self):
        """Gets the hot_node_resource_spec of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501


        :return: The hot_node_resource_spec of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :rtype: HotNodeResourceSpecForDescribeInstanceOutput
        """
        return self._hot_node_resource_spec

    @hot_node_resource_spec.setter
    def hot_node_resource_spec(self, hot_node_resource_spec):
        """Sets the hot_node_resource_spec of this InstanceConfigurationForDescribeInstanceOutput.


        :param hot_node_resource_spec: The hot_node_resource_spec of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :type: HotNodeResourceSpecForDescribeInstanceOutput
        """

        self._hot_node_resource_spec = hot_node_resource_spec

    @property
    def hot_node_storage_spec(self):
        """Gets the hot_node_storage_spec of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501


        :return: The hot_node_storage_spec of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :rtype: HotNodeStorageSpecForDescribeInstanceOutput
        """
        return self._hot_node_storage_spec

    @hot_node_storage_spec.setter
    def hot_node_storage_spec(self, hot_node_storage_spec):
        """Sets the hot_node_storage_spec of this InstanceConfigurationForDescribeInstanceOutput.


        :param hot_node_storage_spec: The hot_node_storage_spec of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :type: HotNodeStorageSpecForDescribeInstanceOutput
        """

        self._hot_node_storage_spec = hot_node_storage_spec

    @property
    def instance_name(self):
        """Gets the instance_name of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501


        :return: The instance_name of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this InstanceConfigurationForDescribeInstanceOutput.


        :param instance_name: The instance_name of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :type: str
        """

        self._instance_name = instance_name

    @property
    def kibana_node_number(self):
        """Gets the kibana_node_number of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501


        :return: The kibana_node_number of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :rtype: int
        """
        return self._kibana_node_number

    @kibana_node_number.setter
    def kibana_node_number(self, kibana_node_number):
        """Sets the kibana_node_number of this InstanceConfigurationForDescribeInstanceOutput.


        :param kibana_node_number: The kibana_node_number of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :type: int
        """

        self._kibana_node_number = kibana_node_number

    @property
    def kibana_node_resource_spec(self):
        """Gets the kibana_node_resource_spec of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501


        :return: The kibana_node_resource_spec of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :rtype: KibanaNodeResourceSpecForDescribeInstanceOutput
        """
        return self._kibana_node_resource_spec

    @kibana_node_resource_spec.setter
    def kibana_node_resource_spec(self, kibana_node_resource_spec):
        """Sets the kibana_node_resource_spec of this InstanceConfigurationForDescribeInstanceOutput.


        :param kibana_node_resource_spec: The kibana_node_resource_spec of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :type: KibanaNodeResourceSpecForDescribeInstanceOutput
        """

        self._kibana_node_resource_spec = kibana_node_resource_spec

    @property
    def master_node_number(self):
        """Gets the master_node_number of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501


        :return: The master_node_number of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :rtype: int
        """
        return self._master_node_number

    @master_node_number.setter
    def master_node_number(self, master_node_number):
        """Sets the master_node_number of this InstanceConfigurationForDescribeInstanceOutput.


        :param master_node_number: The master_node_number of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :type: int
        """

        self._master_node_number = master_node_number

    @property
    def master_node_resource_spec(self):
        """Gets the master_node_resource_spec of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501


        :return: The master_node_resource_spec of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :rtype: MasterNodeResourceSpecForDescribeInstanceOutput
        """
        return self._master_node_resource_spec

    @master_node_resource_spec.setter
    def master_node_resource_spec(self, master_node_resource_spec):
        """Sets the master_node_resource_spec of this InstanceConfigurationForDescribeInstanceOutput.


        :param master_node_resource_spec: The master_node_resource_spec of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :type: MasterNodeResourceSpecForDescribeInstanceOutput
        """

        self._master_node_resource_spec = master_node_resource_spec

    @property
    def master_node_storage_spec(self):
        """Gets the master_node_storage_spec of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501


        :return: The master_node_storage_spec of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :rtype: MasterNodeStorageSpecForDescribeInstanceOutput
        """
        return self._master_node_storage_spec

    @master_node_storage_spec.setter
    def master_node_storage_spec(self, master_node_storage_spec):
        """Sets the master_node_storage_spec of this InstanceConfigurationForDescribeInstanceOutput.


        :param master_node_storage_spec: The master_node_storage_spec of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :type: MasterNodeStorageSpecForDescribeInstanceOutput
        """

        self._master_node_storage_spec = master_node_storage_spec

    @property
    def project_name(self):
        """Gets the project_name of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501


        :return: The project_name of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this InstanceConfigurationForDescribeInstanceOutput.


        :param project_name: The project_name of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def region_id(self):
        """Gets the region_id of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501


        :return: The region_id of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this InstanceConfigurationForDescribeInstanceOutput.


        :param region_id: The region_id of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :type: str
        """

        self._region_id = region_id

    @property
    def subnet(self):
        """Gets the subnet of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501


        :return: The subnet of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :rtype: SubnetForDescribeInstanceOutput
        """
        return self._subnet

    @subnet.setter
    def subnet(self, subnet):
        """Sets the subnet of this InstanceConfigurationForDescribeInstanceOutput.


        :param subnet: The subnet of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :type: SubnetForDescribeInstanceOutput
        """

        self._subnet = subnet

    @property
    def vpc(self):
        """Gets the vpc of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501


        :return: The vpc of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :rtype: VPCForDescribeInstanceOutput
        """
        return self._vpc

    @vpc.setter
    def vpc(self, vpc):
        """Sets the vpc of this InstanceConfigurationForDescribeInstanceOutput.


        :param vpc: The vpc of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :type: VPCForDescribeInstanceOutput
        """

        self._vpc = vpc

    @property
    def version(self):
        """Gets the version of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501


        :return: The version of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this InstanceConfigurationForDescribeInstanceOutput.


        :param version: The version of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def warm_node_number(self):
        """Gets the warm_node_number of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501


        :return: The warm_node_number of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :rtype: int
        """
        return self._warm_node_number

    @warm_node_number.setter
    def warm_node_number(self, warm_node_number):
        """Sets the warm_node_number of this InstanceConfigurationForDescribeInstanceOutput.


        :param warm_node_number: The warm_node_number of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :type: int
        """

        self._warm_node_number = warm_node_number

    @property
    def warm_node_resource_spec(self):
        """Gets the warm_node_resource_spec of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501


        :return: The warm_node_resource_spec of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :rtype: WarmNodeResourceSpecForDescribeInstanceOutput
        """
        return self._warm_node_resource_spec

    @warm_node_resource_spec.setter
    def warm_node_resource_spec(self, warm_node_resource_spec):
        """Sets the warm_node_resource_spec of this InstanceConfigurationForDescribeInstanceOutput.


        :param warm_node_resource_spec: The warm_node_resource_spec of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :type: WarmNodeResourceSpecForDescribeInstanceOutput
        """

        self._warm_node_resource_spec = warm_node_resource_spec

    @property
    def warm_node_storage_spec(self):
        """Gets the warm_node_storage_spec of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501


        :return: The warm_node_storage_spec of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :rtype: WarmNodeStorageSpecForDescribeInstanceOutput
        """
        return self._warm_node_storage_spec

    @warm_node_storage_spec.setter
    def warm_node_storage_spec(self, warm_node_storage_spec):
        """Sets the warm_node_storage_spec of this InstanceConfigurationForDescribeInstanceOutput.


        :param warm_node_storage_spec: The warm_node_storage_spec of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :type: WarmNodeStorageSpecForDescribeInstanceOutput
        """

        self._warm_node_storage_spec = warm_node_storage_spec

    @property
    def zone_id(self):
        """Gets the zone_id of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501


        :return: The zone_id of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this InstanceConfigurationForDescribeInstanceOutput.


        :param zone_id: The zone_id of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :type: str
        """

        self._zone_id = zone_id

    @property
    def zone_number(self):
        """Gets the zone_number of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501


        :return: The zone_number of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :rtype: int
        """
        return self._zone_number

    @zone_number.setter
    def zone_number(self, zone_number):
        """Sets the zone_number of this InstanceConfigurationForDescribeInstanceOutput.


        :param zone_number: The zone_number of this InstanceConfigurationForDescribeInstanceOutput.  # noqa: E501
        :type: int
        """

        self._zone_number = zone_number

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
        if issubclass(InstanceConfigurationForDescribeInstanceOutput, dict):
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
        if not isinstance(other, InstanceConfigurationForDescribeInstanceOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InstanceConfigurationForDescribeInstanceOutput):
            return True

        return self.to_dict() != other.to_dict()
