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


class CreateEnterpriseDBInstanceRequest(object):
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
        'configure_nodes': 'list[ConfigureNodeForCreateEnterpriseDBInstanceInput]',
        'data_layout': 'str',
        'deletion_protection': 'str',
        'flash_per_shard': 'int',
        'instance_name': 'str',
        'modules': 'list[str]',
        'multi_az': 'str',
        'password': 'str',
        'project_name': 'str',
        'purchase_months': 'int',
        'ram_per_shard': 'int',
        'region_id': 'str',
        'shard_number': 'int',
        'subnet_id': 'str',
        'tags': 'list[TagForCreateEnterpriseDBInstanceInput]',
        'vpc_id': 'str'
    }

    attribute_map = {
        'allow_list_ids': 'AllowListIds',
        'auto_renew': 'AutoRenew',
        'charge_type': 'ChargeType',
        'client_token': 'ClientToken',
        'configure_nodes': 'ConfigureNodes',
        'data_layout': 'DataLayout',
        'deletion_protection': 'DeletionProtection',
        'flash_per_shard': 'FlashPerShard',
        'instance_name': 'InstanceName',
        'modules': 'Modules',
        'multi_az': 'MultiAZ',
        'password': 'Password',
        'project_name': 'ProjectName',
        'purchase_months': 'PurchaseMonths',
        'ram_per_shard': 'RamPerShard',
        'region_id': 'RegionId',
        'shard_number': 'ShardNumber',
        'subnet_id': 'SubnetId',
        'tags': 'Tags',
        'vpc_id': 'VpcId'
    }

    def __init__(self, allow_list_ids=None, auto_renew=None, charge_type=None, client_token=None, configure_nodes=None, data_layout=None, deletion_protection=None, flash_per_shard=None, instance_name=None, modules=None, multi_az=None, password=None, project_name=None, purchase_months=None, ram_per_shard=None, region_id=None, shard_number=None, subnet_id=None, tags=None, vpc_id=None, _configuration=None):  # noqa: E501
        """CreateEnterpriseDBInstanceRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._allow_list_ids = None
        self._auto_renew = None
        self._charge_type = None
        self._client_token = None
        self._configure_nodes = None
        self._data_layout = None
        self._deletion_protection = None
        self._flash_per_shard = None
        self._instance_name = None
        self._modules = None
        self._multi_az = None
        self._password = None
        self._project_name = None
        self._purchase_months = None
        self._ram_per_shard = None
        self._region_id = None
        self._shard_number = None
        self._subnet_id = None
        self._tags = None
        self._vpc_id = None
        self.discriminator = None

        if allow_list_ids is not None:
            self.allow_list_ids = allow_list_ids
        if auto_renew is not None:
            self.auto_renew = auto_renew
        self.charge_type = charge_type
        if client_token is not None:
            self.client_token = client_token
        if configure_nodes is not None:
            self.configure_nodes = configure_nodes
        self.data_layout = data_layout
        if deletion_protection is not None:
            self.deletion_protection = deletion_protection
        self.flash_per_shard = flash_per_shard
        if instance_name is not None:
            self.instance_name = instance_name
        if modules is not None:
            self.modules = modules
        if multi_az is not None:
            self.multi_az = multi_az
        if password is not None:
            self.password = password
        if project_name is not None:
            self.project_name = project_name
        if purchase_months is not None:
            self.purchase_months = purchase_months
        self.ram_per_shard = ram_per_shard
        self.region_id = region_id
        self.shard_number = shard_number
        self.subnet_id = subnet_id
        if tags is not None:
            self.tags = tags
        self.vpc_id = vpc_id

    @property
    def allow_list_ids(self):
        """Gets the allow_list_ids of this CreateEnterpriseDBInstanceRequest.  # noqa: E501


        :return: The allow_list_ids of this CreateEnterpriseDBInstanceRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._allow_list_ids

    @allow_list_ids.setter
    def allow_list_ids(self, allow_list_ids):
        """Sets the allow_list_ids of this CreateEnterpriseDBInstanceRequest.


        :param allow_list_ids: The allow_list_ids of this CreateEnterpriseDBInstanceRequest.  # noqa: E501
        :type: list[str]
        """

        self._allow_list_ids = allow_list_ids

    @property
    def auto_renew(self):
        """Gets the auto_renew of this CreateEnterpriseDBInstanceRequest.  # noqa: E501


        :return: The auto_renew of this CreateEnterpriseDBInstanceRequest.  # noqa: E501
        :rtype: bool
        """
        return self._auto_renew

    @auto_renew.setter
    def auto_renew(self, auto_renew):
        """Sets the auto_renew of this CreateEnterpriseDBInstanceRequest.


        :param auto_renew: The auto_renew of this CreateEnterpriseDBInstanceRequest.  # noqa: E501
        :type: bool
        """

        self._auto_renew = auto_renew

    @property
    def charge_type(self):
        """Gets the charge_type of this CreateEnterpriseDBInstanceRequest.  # noqa: E501


        :return: The charge_type of this CreateEnterpriseDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._charge_type

    @charge_type.setter
    def charge_type(self, charge_type):
        """Sets the charge_type of this CreateEnterpriseDBInstanceRequest.


        :param charge_type: The charge_type of this CreateEnterpriseDBInstanceRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and charge_type is None:
            raise ValueError("Invalid value for `charge_type`, must not be `None`")  # noqa: E501

        self._charge_type = charge_type

    @property
    def client_token(self):
        """Gets the client_token of this CreateEnterpriseDBInstanceRequest.  # noqa: E501


        :return: The client_token of this CreateEnterpriseDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_token

    @client_token.setter
    def client_token(self, client_token):
        """Sets the client_token of this CreateEnterpriseDBInstanceRequest.


        :param client_token: The client_token of this CreateEnterpriseDBInstanceRequest.  # noqa: E501
        :type: str
        """

        self._client_token = client_token

    @property
    def configure_nodes(self):
        """Gets the configure_nodes of this CreateEnterpriseDBInstanceRequest.  # noqa: E501


        :return: The configure_nodes of this CreateEnterpriseDBInstanceRequest.  # noqa: E501
        :rtype: list[ConfigureNodeForCreateEnterpriseDBInstanceInput]
        """
        return self._configure_nodes

    @configure_nodes.setter
    def configure_nodes(self, configure_nodes):
        """Sets the configure_nodes of this CreateEnterpriseDBInstanceRequest.


        :param configure_nodes: The configure_nodes of this CreateEnterpriseDBInstanceRequest.  # noqa: E501
        :type: list[ConfigureNodeForCreateEnterpriseDBInstanceInput]
        """

        self._configure_nodes = configure_nodes

    @property
    def data_layout(self):
        """Gets the data_layout of this CreateEnterpriseDBInstanceRequest.  # noqa: E501


        :return: The data_layout of this CreateEnterpriseDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._data_layout

    @data_layout.setter
    def data_layout(self, data_layout):
        """Sets the data_layout of this CreateEnterpriseDBInstanceRequest.


        :param data_layout: The data_layout of this CreateEnterpriseDBInstanceRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and data_layout is None:
            raise ValueError("Invalid value for `data_layout`, must not be `None`")  # noqa: E501

        self._data_layout = data_layout

    @property
    def deletion_protection(self):
        """Gets the deletion_protection of this CreateEnterpriseDBInstanceRequest.  # noqa: E501


        :return: The deletion_protection of this CreateEnterpriseDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._deletion_protection

    @deletion_protection.setter
    def deletion_protection(self, deletion_protection):
        """Sets the deletion_protection of this CreateEnterpriseDBInstanceRequest.


        :param deletion_protection: The deletion_protection of this CreateEnterpriseDBInstanceRequest.  # noqa: E501
        :type: str
        """

        self._deletion_protection = deletion_protection

    @property
    def flash_per_shard(self):
        """Gets the flash_per_shard of this CreateEnterpriseDBInstanceRequest.  # noqa: E501


        :return: The flash_per_shard of this CreateEnterpriseDBInstanceRequest.  # noqa: E501
        :rtype: int
        """
        return self._flash_per_shard

    @flash_per_shard.setter
    def flash_per_shard(self, flash_per_shard):
        """Sets the flash_per_shard of this CreateEnterpriseDBInstanceRequest.


        :param flash_per_shard: The flash_per_shard of this CreateEnterpriseDBInstanceRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and flash_per_shard is None:
            raise ValueError("Invalid value for `flash_per_shard`, must not be `None`")  # noqa: E501

        self._flash_per_shard = flash_per_shard

    @property
    def instance_name(self):
        """Gets the instance_name of this CreateEnterpriseDBInstanceRequest.  # noqa: E501


        :return: The instance_name of this CreateEnterpriseDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this CreateEnterpriseDBInstanceRequest.


        :param instance_name: The instance_name of this CreateEnterpriseDBInstanceRequest.  # noqa: E501
        :type: str
        """

        self._instance_name = instance_name

    @property
    def modules(self):
        """Gets the modules of this CreateEnterpriseDBInstanceRequest.  # noqa: E501


        :return: The modules of this CreateEnterpriseDBInstanceRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._modules

    @modules.setter
    def modules(self, modules):
        """Sets the modules of this CreateEnterpriseDBInstanceRequest.


        :param modules: The modules of this CreateEnterpriseDBInstanceRequest.  # noqa: E501
        :type: list[str]
        """

        self._modules = modules

    @property
    def multi_az(self):
        """Gets the multi_az of this CreateEnterpriseDBInstanceRequest.  # noqa: E501


        :return: The multi_az of this CreateEnterpriseDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._multi_az

    @multi_az.setter
    def multi_az(self, multi_az):
        """Sets the multi_az of this CreateEnterpriseDBInstanceRequest.


        :param multi_az: The multi_az of this CreateEnterpriseDBInstanceRequest.  # noqa: E501
        :type: str
        """

        self._multi_az = multi_az

    @property
    def password(self):
        """Gets the password of this CreateEnterpriseDBInstanceRequest.  # noqa: E501


        :return: The password of this CreateEnterpriseDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this CreateEnterpriseDBInstanceRequest.


        :param password: The password of this CreateEnterpriseDBInstanceRequest.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def project_name(self):
        """Gets the project_name of this CreateEnterpriseDBInstanceRequest.  # noqa: E501


        :return: The project_name of this CreateEnterpriseDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this CreateEnterpriseDBInstanceRequest.


        :param project_name: The project_name of this CreateEnterpriseDBInstanceRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def purchase_months(self):
        """Gets the purchase_months of this CreateEnterpriseDBInstanceRequest.  # noqa: E501


        :return: The purchase_months of this CreateEnterpriseDBInstanceRequest.  # noqa: E501
        :rtype: int
        """
        return self._purchase_months

    @purchase_months.setter
    def purchase_months(self, purchase_months):
        """Sets the purchase_months of this CreateEnterpriseDBInstanceRequest.


        :param purchase_months: The purchase_months of this CreateEnterpriseDBInstanceRequest.  # noqa: E501
        :type: int
        """

        self._purchase_months = purchase_months

    @property
    def ram_per_shard(self):
        """Gets the ram_per_shard of this CreateEnterpriseDBInstanceRequest.  # noqa: E501


        :return: The ram_per_shard of this CreateEnterpriseDBInstanceRequest.  # noqa: E501
        :rtype: int
        """
        return self._ram_per_shard

    @ram_per_shard.setter
    def ram_per_shard(self, ram_per_shard):
        """Sets the ram_per_shard of this CreateEnterpriseDBInstanceRequest.


        :param ram_per_shard: The ram_per_shard of this CreateEnterpriseDBInstanceRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and ram_per_shard is None:
            raise ValueError("Invalid value for `ram_per_shard`, must not be `None`")  # noqa: E501

        self._ram_per_shard = ram_per_shard

    @property
    def region_id(self):
        """Gets the region_id of this CreateEnterpriseDBInstanceRequest.  # noqa: E501


        :return: The region_id of this CreateEnterpriseDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this CreateEnterpriseDBInstanceRequest.


        :param region_id: The region_id of this CreateEnterpriseDBInstanceRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and region_id is None:
            raise ValueError("Invalid value for `region_id`, must not be `None`")  # noqa: E501

        self._region_id = region_id

    @property
    def shard_number(self):
        """Gets the shard_number of this CreateEnterpriseDBInstanceRequest.  # noqa: E501


        :return: The shard_number of this CreateEnterpriseDBInstanceRequest.  # noqa: E501
        :rtype: int
        """
        return self._shard_number

    @shard_number.setter
    def shard_number(self, shard_number):
        """Sets the shard_number of this CreateEnterpriseDBInstanceRequest.


        :param shard_number: The shard_number of this CreateEnterpriseDBInstanceRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and shard_number is None:
            raise ValueError("Invalid value for `shard_number`, must not be `None`")  # noqa: E501

        self._shard_number = shard_number

    @property
    def subnet_id(self):
        """Gets the subnet_id of this CreateEnterpriseDBInstanceRequest.  # noqa: E501


        :return: The subnet_id of this CreateEnterpriseDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this CreateEnterpriseDBInstanceRequest.


        :param subnet_id: The subnet_id of this CreateEnterpriseDBInstanceRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and subnet_id is None:
            raise ValueError("Invalid value for `subnet_id`, must not be `None`")  # noqa: E501

        self._subnet_id = subnet_id

    @property
    def tags(self):
        """Gets the tags of this CreateEnterpriseDBInstanceRequest.  # noqa: E501


        :return: The tags of this CreateEnterpriseDBInstanceRequest.  # noqa: E501
        :rtype: list[TagForCreateEnterpriseDBInstanceInput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateEnterpriseDBInstanceRequest.


        :param tags: The tags of this CreateEnterpriseDBInstanceRequest.  # noqa: E501
        :type: list[TagForCreateEnterpriseDBInstanceInput]
        """

        self._tags = tags

    @property
    def vpc_id(self):
        """Gets the vpc_id of this CreateEnterpriseDBInstanceRequest.  # noqa: E501


        :return: The vpc_id of this CreateEnterpriseDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this CreateEnterpriseDBInstanceRequest.


        :param vpc_id: The vpc_id of this CreateEnterpriseDBInstanceRequest.  # noqa: E501
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
        if issubclass(CreateEnterpriseDBInstanceRequest, dict):
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
        if not isinstance(other, CreateEnterpriseDBInstanceRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateEnterpriseDBInstanceRequest):
            return True

        return self.to_dict() != other.to_dict()
