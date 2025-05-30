# coding: utf-8

"""
    redis

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class CreateDBInstanceRequest(object):
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
        'allow_list_ids': 'list[str]',
        'auto_renew': 'bool',
        'charge_type': 'str',
        'client_token': 'str',
        'configure_nodes': 'list[ConfigureNodeForCreateDBInstanceInput]',
        'deletion_protection': 'str',
        'engine_version': 'str',
        'instance_name': 'str',
        'multi_az': 'str',
        'no_auth_mode': 'str',
        'node_number': 'int',
        'parameter_group_id': 'str',
        'password': 'str',
        'port': 'int',
        'project_name': 'str',
        'purchase_months': 'int',
        'region_id': 'str',
        'shard_capacity': 'int',
        'shard_number': 'int',
        'sharded_cluster': 'int',
        'subnet_id': 'str',
        'tags': 'list[TagForCreateDBInstanceInput]',
        'vpc_id': 'str'
    }

    attribute_map = {
        'allow_list_ids': 'AllowListIds',
        'auto_renew': 'AutoRenew',
        'charge_type': 'ChargeType',
        'client_token': 'ClientToken',
        'configure_nodes': 'ConfigureNodes',
        'deletion_protection': 'DeletionProtection',
        'engine_version': 'EngineVersion',
        'instance_name': 'InstanceName',
        'multi_az': 'MultiAZ',
        'no_auth_mode': 'NoAuthMode',
        'node_number': 'NodeNumber',
        'parameter_group_id': 'ParameterGroupId',
        'password': 'Password',
        'port': 'Port',
        'project_name': 'ProjectName',
        'purchase_months': 'PurchaseMonths',
        'region_id': 'RegionId',
        'shard_capacity': 'ShardCapacity',
        'shard_number': 'ShardNumber',
        'sharded_cluster': 'ShardedCluster',
        'subnet_id': 'SubnetId',
        'tags': 'Tags',
        'vpc_id': 'VpcId'
    }

    def __init__(self, allow_list_ids=None, auto_renew=None, charge_type=None, client_token=None, configure_nodes=None, deletion_protection=None, engine_version=None, instance_name=None, multi_az=None, no_auth_mode=None, node_number=None, parameter_group_id=None, password=None, port=None, project_name=None, purchase_months=None, region_id=None, shard_capacity=None, shard_number=None, sharded_cluster=None, subnet_id=None, tags=None, vpc_id=None, _configuration=None):  # noqa: E501
        """CreateDBInstanceRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._allow_list_ids = None
        self._auto_renew = None
        self._charge_type = None
        self._client_token = None
        self._configure_nodes = None
        self._deletion_protection = None
        self._engine_version = None
        self._instance_name = None
        self._multi_az = None
        self._no_auth_mode = None
        self._node_number = None
        self._parameter_group_id = None
        self._password = None
        self._port = None
        self._project_name = None
        self._purchase_months = None
        self._region_id = None
        self._shard_capacity = None
        self._shard_number = None
        self._sharded_cluster = None
        self._subnet_id = None
        self._tags = None
        self._vpc_id = None
        self.discriminator = None

        if allow_list_ids is not None:
            self.allow_list_ids = allow_list_ids
        if auto_renew is not None:
            self.auto_renew = auto_renew
        if charge_type is not None:
            self.charge_type = charge_type
        if client_token is not None:
            self.client_token = client_token
        if configure_nodes is not None:
            self.configure_nodes = configure_nodes
        if deletion_protection is not None:
            self.deletion_protection = deletion_protection
        self.engine_version = engine_version
        if instance_name is not None:
            self.instance_name = instance_name
        self.multi_az = multi_az
        if no_auth_mode is not None:
            self.no_auth_mode = no_auth_mode
        self.node_number = node_number
        if parameter_group_id is not None:
            self.parameter_group_id = parameter_group_id
        if password is not None:
            self.password = password
        if port is not None:
            self.port = port
        if project_name is not None:
            self.project_name = project_name
        if purchase_months is not None:
            self.purchase_months = purchase_months
        self.region_id = region_id
        self.shard_capacity = shard_capacity
        if shard_number is not None:
            self.shard_number = shard_number
        self.sharded_cluster = sharded_cluster
        self.subnet_id = subnet_id
        if tags is not None:
            self.tags = tags
        self.vpc_id = vpc_id

    @property
    def allow_list_ids(self):
        """Gets the allow_list_ids of this CreateDBInstanceRequest.  # noqa: E501


        :return: The allow_list_ids of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._allow_list_ids

    @allow_list_ids.setter
    def allow_list_ids(self, allow_list_ids):
        """Sets the allow_list_ids of this CreateDBInstanceRequest.


        :param allow_list_ids: The allow_list_ids of this CreateDBInstanceRequest.  # noqa: E501
        :type: list[str]
        """

        self._allow_list_ids = allow_list_ids

    @property
    def auto_renew(self):
        """Gets the auto_renew of this CreateDBInstanceRequest.  # noqa: E501


        :return: The auto_renew of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: bool
        """
        return self._auto_renew

    @auto_renew.setter
    def auto_renew(self, auto_renew):
        """Sets the auto_renew of this CreateDBInstanceRequest.


        :param auto_renew: The auto_renew of this CreateDBInstanceRequest.  # noqa: E501
        :type: bool
        """

        self._auto_renew = auto_renew

    @property
    def charge_type(self):
        """Gets the charge_type of this CreateDBInstanceRequest.  # noqa: E501


        :return: The charge_type of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._charge_type

    @charge_type.setter
    def charge_type(self, charge_type):
        """Sets the charge_type of this CreateDBInstanceRequest.


        :param charge_type: The charge_type of this CreateDBInstanceRequest.  # noqa: E501
        :type: str
        """

        self._charge_type = charge_type

    @property
    def client_token(self):
        """Gets the client_token of this CreateDBInstanceRequest.  # noqa: E501


        :return: The client_token of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_token

    @client_token.setter
    def client_token(self, client_token):
        """Sets the client_token of this CreateDBInstanceRequest.


        :param client_token: The client_token of this CreateDBInstanceRequest.  # noqa: E501
        :type: str
        """

        self._client_token = client_token

    @property
    def configure_nodes(self):
        """Gets the configure_nodes of this CreateDBInstanceRequest.  # noqa: E501


        :return: The configure_nodes of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: list[ConfigureNodeForCreateDBInstanceInput]
        """
        return self._configure_nodes

    @configure_nodes.setter
    def configure_nodes(self, configure_nodes):
        """Sets the configure_nodes of this CreateDBInstanceRequest.


        :param configure_nodes: The configure_nodes of this CreateDBInstanceRequest.  # noqa: E501
        :type: list[ConfigureNodeForCreateDBInstanceInput]
        """

        self._configure_nodes = configure_nodes

    @property
    def deletion_protection(self):
        """Gets the deletion_protection of this CreateDBInstanceRequest.  # noqa: E501


        :return: The deletion_protection of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._deletion_protection

    @deletion_protection.setter
    def deletion_protection(self, deletion_protection):
        """Sets the deletion_protection of this CreateDBInstanceRequest.


        :param deletion_protection: The deletion_protection of this CreateDBInstanceRequest.  # noqa: E501
        :type: str
        """

        self._deletion_protection = deletion_protection

    @property
    def engine_version(self):
        """Gets the engine_version of this CreateDBInstanceRequest.  # noqa: E501


        :return: The engine_version of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        """Sets the engine_version of this CreateDBInstanceRequest.


        :param engine_version: The engine_version of this CreateDBInstanceRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and engine_version is None:
            raise ValueError("Invalid value for `engine_version`, must not be `None`")  # noqa: E501

        self._engine_version = engine_version

    @property
    def instance_name(self):
        """Gets the instance_name of this CreateDBInstanceRequest.  # noqa: E501


        :return: The instance_name of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this CreateDBInstanceRequest.


        :param instance_name: The instance_name of this CreateDBInstanceRequest.  # noqa: E501
        :type: str
        """

        self._instance_name = instance_name

    @property
    def multi_az(self):
        """Gets the multi_az of this CreateDBInstanceRequest.  # noqa: E501


        :return: The multi_az of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._multi_az

    @multi_az.setter
    def multi_az(self, multi_az):
        """Sets the multi_az of this CreateDBInstanceRequest.


        :param multi_az: The multi_az of this CreateDBInstanceRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and multi_az is None:
            raise ValueError("Invalid value for `multi_az`, must not be `None`")  # noqa: E501

        self._multi_az = multi_az

    @property
    def no_auth_mode(self):
        """Gets the no_auth_mode of this CreateDBInstanceRequest.  # noqa: E501


        :return: The no_auth_mode of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._no_auth_mode

    @no_auth_mode.setter
    def no_auth_mode(self, no_auth_mode):
        """Sets the no_auth_mode of this CreateDBInstanceRequest.


        :param no_auth_mode: The no_auth_mode of this CreateDBInstanceRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["Invalid", "open", "close"]  # noqa: E501
        if (self._configuration.client_side_validation and
                no_auth_mode not in allowed_values):
            raise ValueError(
                "Invalid value for `no_auth_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(no_auth_mode, allowed_values)
            )

        self._no_auth_mode = no_auth_mode

    @property
    def node_number(self):
        """Gets the node_number of this CreateDBInstanceRequest.  # noqa: E501


        :return: The node_number of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: int
        """
        return self._node_number

    @node_number.setter
    def node_number(self, node_number):
        """Sets the node_number of this CreateDBInstanceRequest.


        :param node_number: The node_number of this CreateDBInstanceRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and node_number is None:
            raise ValueError("Invalid value for `node_number`, must not be `None`")  # noqa: E501

        self._node_number = node_number

    @property
    def parameter_group_id(self):
        """Gets the parameter_group_id of this CreateDBInstanceRequest.  # noqa: E501


        :return: The parameter_group_id of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._parameter_group_id

    @parameter_group_id.setter
    def parameter_group_id(self, parameter_group_id):
        """Sets the parameter_group_id of this CreateDBInstanceRequest.


        :param parameter_group_id: The parameter_group_id of this CreateDBInstanceRequest.  # noqa: E501
        :type: str
        """

        self._parameter_group_id = parameter_group_id

    @property
    def password(self):
        """Gets the password of this CreateDBInstanceRequest.  # noqa: E501


        :return: The password of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this CreateDBInstanceRequest.


        :param password: The password of this CreateDBInstanceRequest.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def port(self):
        """Gets the port of this CreateDBInstanceRequest.  # noqa: E501


        :return: The port of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this CreateDBInstanceRequest.


        :param port: The port of this CreateDBInstanceRequest.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def project_name(self):
        """Gets the project_name of this CreateDBInstanceRequest.  # noqa: E501


        :return: The project_name of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this CreateDBInstanceRequest.


        :param project_name: The project_name of this CreateDBInstanceRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def purchase_months(self):
        """Gets the purchase_months of this CreateDBInstanceRequest.  # noqa: E501


        :return: The purchase_months of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: int
        """
        return self._purchase_months

    @purchase_months.setter
    def purchase_months(self, purchase_months):
        """Sets the purchase_months of this CreateDBInstanceRequest.


        :param purchase_months: The purchase_months of this CreateDBInstanceRequest.  # noqa: E501
        :type: int
        """

        self._purchase_months = purchase_months

    @property
    def region_id(self):
        """Gets the region_id of this CreateDBInstanceRequest.  # noqa: E501


        :return: The region_id of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this CreateDBInstanceRequest.


        :param region_id: The region_id of this CreateDBInstanceRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and region_id is None:
            raise ValueError("Invalid value for `region_id`, must not be `None`")  # noqa: E501

        self._region_id = region_id

    @property
    def shard_capacity(self):
        """Gets the shard_capacity of this CreateDBInstanceRequest.  # noqa: E501


        :return: The shard_capacity of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: int
        """
        return self._shard_capacity

    @shard_capacity.setter
    def shard_capacity(self, shard_capacity):
        """Sets the shard_capacity of this CreateDBInstanceRequest.


        :param shard_capacity: The shard_capacity of this CreateDBInstanceRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and shard_capacity is None:
            raise ValueError("Invalid value for `shard_capacity`, must not be `None`")  # noqa: E501

        self._shard_capacity = shard_capacity

    @property
    def shard_number(self):
        """Gets the shard_number of this CreateDBInstanceRequest.  # noqa: E501


        :return: The shard_number of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: int
        """
        return self._shard_number

    @shard_number.setter
    def shard_number(self, shard_number):
        """Sets the shard_number of this CreateDBInstanceRequest.


        :param shard_number: The shard_number of this CreateDBInstanceRequest.  # noqa: E501
        :type: int
        """

        self._shard_number = shard_number

    @property
    def sharded_cluster(self):
        """Gets the sharded_cluster of this CreateDBInstanceRequest.  # noqa: E501


        :return: The sharded_cluster of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: int
        """
        return self._sharded_cluster

    @sharded_cluster.setter
    def sharded_cluster(self, sharded_cluster):
        """Sets the sharded_cluster of this CreateDBInstanceRequest.


        :param sharded_cluster: The sharded_cluster of this CreateDBInstanceRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and sharded_cluster is None:
            raise ValueError("Invalid value for `sharded_cluster`, must not be `None`")  # noqa: E501

        self._sharded_cluster = sharded_cluster

    @property
    def subnet_id(self):
        """Gets the subnet_id of this CreateDBInstanceRequest.  # noqa: E501


        :return: The subnet_id of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this CreateDBInstanceRequest.


        :param subnet_id: The subnet_id of this CreateDBInstanceRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and subnet_id is None:
            raise ValueError("Invalid value for `subnet_id`, must not be `None`")  # noqa: E501

        self._subnet_id = subnet_id

    @property
    def tags(self):
        """Gets the tags of this CreateDBInstanceRequest.  # noqa: E501


        :return: The tags of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: list[TagForCreateDBInstanceInput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateDBInstanceRequest.


        :param tags: The tags of this CreateDBInstanceRequest.  # noqa: E501
        :type: list[TagForCreateDBInstanceInput]
        """

        self._tags = tags

    @property
    def vpc_id(self):
        """Gets the vpc_id of this CreateDBInstanceRequest.  # noqa: E501


        :return: The vpc_id of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this CreateDBInstanceRequest.


        :param vpc_id: The vpc_id of this CreateDBInstanceRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and vpc_id is None:
            raise ValueError("Invalid value for `vpc_id`, must not be `None`")  # noqa: E501

        self._vpc_id = vpc_id

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
        if issubclass(CreateDBInstanceRequest, dict):
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
        if not isinstance(other, CreateDBInstanceRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateDBInstanceRequest):
            return True

        return self.to_dict() != other.to_dict()
