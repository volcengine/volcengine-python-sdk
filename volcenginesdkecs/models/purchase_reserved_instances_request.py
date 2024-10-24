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


class PurchaseReservedInstancesRequest(object):
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
        'auto_renew': 'bool',
        'auto_renew_period': 'int',
        'client_token': 'str',
        'description': 'str',
        'hpc_cluster_id': 'str',
        'instance_count': 'int',
        'instance_type_id': 'str',
        'period': 'int',
        'period_unit': 'str',
        'project_name': 'str',
        'region_id': 'str',
        'reserved_instance_name': 'str',
        'scope': 'str',
        'tags': 'list[TagForPurchaseReservedInstancesInput]',
        'zone_id': 'str'
    }

    attribute_map = {
        'auto_renew': 'AutoRenew',
        'auto_renew_period': 'AutoRenewPeriod',
        'client_token': 'ClientToken',
        'description': 'Description',
        'hpc_cluster_id': 'HpcClusterId',
        'instance_count': 'InstanceCount',
        'instance_type_id': 'InstanceTypeId',
        'period': 'Period',
        'period_unit': 'PeriodUnit',
        'project_name': 'ProjectName',
        'region_id': 'RegionId',
        'reserved_instance_name': 'ReservedInstanceName',
        'scope': 'Scope',
        'tags': 'Tags',
        'zone_id': 'ZoneId'
    }

    def __init__(self, auto_renew=None, auto_renew_period=None, client_token=None, description=None, hpc_cluster_id=None, instance_count=None, instance_type_id=None, period=None, period_unit=None, project_name=None, region_id=None, reserved_instance_name=None, scope=None, tags=None, zone_id=None, _configuration=None):  # noqa: E501
        """PurchaseReservedInstancesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._auto_renew = None
        self._auto_renew_period = None
        self._client_token = None
        self._description = None
        self._hpc_cluster_id = None
        self._instance_count = None
        self._instance_type_id = None
        self._period = None
        self._period_unit = None
        self._project_name = None
        self._region_id = None
        self._reserved_instance_name = None
        self._scope = None
        self._tags = None
        self._zone_id = None
        self.discriminator = None

        if auto_renew is not None:
            self.auto_renew = auto_renew
        if auto_renew_period is not None:
            self.auto_renew_period = auto_renew_period
        if client_token is not None:
            self.client_token = client_token
        if description is not None:
            self.description = description
        if hpc_cluster_id is not None:
            self.hpc_cluster_id = hpc_cluster_id
        if instance_count is not None:
            self.instance_count = instance_count
        self.instance_type_id = instance_type_id
        if period is not None:
            self.period = period
        if period_unit is not None:
            self.period_unit = period_unit
        if project_name is not None:
            self.project_name = project_name
        if region_id is not None:
            self.region_id = region_id
        self.reserved_instance_name = reserved_instance_name
        if scope is not None:
            self.scope = scope
        if tags is not None:
            self.tags = tags
        if zone_id is not None:
            self.zone_id = zone_id

    @property
    def auto_renew(self):
        """Gets the auto_renew of this PurchaseReservedInstancesRequest.  # noqa: E501


        :return: The auto_renew of this PurchaseReservedInstancesRequest.  # noqa: E501
        :rtype: bool
        """
        return self._auto_renew

    @auto_renew.setter
    def auto_renew(self, auto_renew):
        """Sets the auto_renew of this PurchaseReservedInstancesRequest.


        :param auto_renew: The auto_renew of this PurchaseReservedInstancesRequest.  # noqa: E501
        :type: bool
        """

        self._auto_renew = auto_renew

    @property
    def auto_renew_period(self):
        """Gets the auto_renew_period of this PurchaseReservedInstancesRequest.  # noqa: E501


        :return: The auto_renew_period of this PurchaseReservedInstancesRequest.  # noqa: E501
        :rtype: int
        """
        return self._auto_renew_period

    @auto_renew_period.setter
    def auto_renew_period(self, auto_renew_period):
        """Sets the auto_renew_period of this PurchaseReservedInstancesRequest.


        :param auto_renew_period: The auto_renew_period of this PurchaseReservedInstancesRequest.  # noqa: E501
        :type: int
        """

        self._auto_renew_period = auto_renew_period

    @property
    def client_token(self):
        """Gets the client_token of this PurchaseReservedInstancesRequest.  # noqa: E501


        :return: The client_token of this PurchaseReservedInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_token

    @client_token.setter
    def client_token(self, client_token):
        """Sets the client_token of this PurchaseReservedInstancesRequest.


        :param client_token: The client_token of this PurchaseReservedInstancesRequest.  # noqa: E501
        :type: str
        """

        self._client_token = client_token

    @property
    def description(self):
        """Gets the description of this PurchaseReservedInstancesRequest.  # noqa: E501


        :return: The description of this PurchaseReservedInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PurchaseReservedInstancesRequest.


        :param description: The description of this PurchaseReservedInstancesRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def hpc_cluster_id(self):
        """Gets the hpc_cluster_id of this PurchaseReservedInstancesRequest.  # noqa: E501


        :return: The hpc_cluster_id of this PurchaseReservedInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._hpc_cluster_id

    @hpc_cluster_id.setter
    def hpc_cluster_id(self, hpc_cluster_id):
        """Sets the hpc_cluster_id of this PurchaseReservedInstancesRequest.


        :param hpc_cluster_id: The hpc_cluster_id of this PurchaseReservedInstancesRequest.  # noqa: E501
        :type: str
        """

        self._hpc_cluster_id = hpc_cluster_id

    @property
    def instance_count(self):
        """Gets the instance_count of this PurchaseReservedInstancesRequest.  # noqa: E501


        :return: The instance_count of this PurchaseReservedInstancesRequest.  # noqa: E501
        :rtype: int
        """
        return self._instance_count

    @instance_count.setter
    def instance_count(self, instance_count):
        """Sets the instance_count of this PurchaseReservedInstancesRequest.


        :param instance_count: The instance_count of this PurchaseReservedInstancesRequest.  # noqa: E501
        :type: int
        """

        self._instance_count = instance_count

    @property
    def instance_type_id(self):
        """Gets the instance_type_id of this PurchaseReservedInstancesRequest.  # noqa: E501


        :return: The instance_type_id of this PurchaseReservedInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_type_id

    @instance_type_id.setter
    def instance_type_id(self, instance_type_id):
        """Sets the instance_type_id of this PurchaseReservedInstancesRequest.


        :param instance_type_id: The instance_type_id of this PurchaseReservedInstancesRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and instance_type_id is None:
            raise ValueError("Invalid value for `instance_type_id`, must not be `None`")  # noqa: E501

        self._instance_type_id = instance_type_id

    @property
    def period(self):
        """Gets the period of this PurchaseReservedInstancesRequest.  # noqa: E501


        :return: The period of this PurchaseReservedInstancesRequest.  # noqa: E501
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this PurchaseReservedInstancesRequest.


        :param period: The period of this PurchaseReservedInstancesRequest.  # noqa: E501
        :type: int
        """

        self._period = period

    @property
    def period_unit(self):
        """Gets the period_unit of this PurchaseReservedInstancesRequest.  # noqa: E501


        :return: The period_unit of this PurchaseReservedInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._period_unit

    @period_unit.setter
    def period_unit(self, period_unit):
        """Sets the period_unit of this PurchaseReservedInstancesRequest.


        :param period_unit: The period_unit of this PurchaseReservedInstancesRequest.  # noqa: E501
        :type: str
        """

        self._period_unit = period_unit

    @property
    def project_name(self):
        """Gets the project_name of this PurchaseReservedInstancesRequest.  # noqa: E501


        :return: The project_name of this PurchaseReservedInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this PurchaseReservedInstancesRequest.


        :param project_name: The project_name of this PurchaseReservedInstancesRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def region_id(self):
        """Gets the region_id of this PurchaseReservedInstancesRequest.  # noqa: E501


        :return: The region_id of this PurchaseReservedInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this PurchaseReservedInstancesRequest.


        :param region_id: The region_id of this PurchaseReservedInstancesRequest.  # noqa: E501
        :type: str
        """

        self._region_id = region_id

    @property
    def reserved_instance_name(self):
        """Gets the reserved_instance_name of this PurchaseReservedInstancesRequest.  # noqa: E501


        :return: The reserved_instance_name of this PurchaseReservedInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._reserved_instance_name

    @reserved_instance_name.setter
    def reserved_instance_name(self, reserved_instance_name):
        """Sets the reserved_instance_name of this PurchaseReservedInstancesRequest.


        :param reserved_instance_name: The reserved_instance_name of this PurchaseReservedInstancesRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and reserved_instance_name is None:
            raise ValueError("Invalid value for `reserved_instance_name`, must not be `None`")  # noqa: E501

        self._reserved_instance_name = reserved_instance_name

    @property
    def scope(self):
        """Gets the scope of this PurchaseReservedInstancesRequest.  # noqa: E501


        :return: The scope of this PurchaseReservedInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this PurchaseReservedInstancesRequest.


        :param scope: The scope of this PurchaseReservedInstancesRequest.  # noqa: E501
        :type: str
        """

        self._scope = scope

    @property
    def tags(self):
        """Gets the tags of this PurchaseReservedInstancesRequest.  # noqa: E501


        :return: The tags of this PurchaseReservedInstancesRequest.  # noqa: E501
        :rtype: list[TagForPurchaseReservedInstancesInput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this PurchaseReservedInstancesRequest.


        :param tags: The tags of this PurchaseReservedInstancesRequest.  # noqa: E501
        :type: list[TagForPurchaseReservedInstancesInput]
        """

        self._tags = tags

    @property
    def zone_id(self):
        """Gets the zone_id of this PurchaseReservedInstancesRequest.  # noqa: E501


        :return: The zone_id of this PurchaseReservedInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this PurchaseReservedInstancesRequest.


        :param zone_id: The zone_id of this PurchaseReservedInstancesRequest.  # noqa: E501
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
        if issubclass(PurchaseReservedInstancesRequest, dict):
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
        if not isinstance(other, PurchaseReservedInstancesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PurchaseReservedInstancesRequest):
            return True

        return self.to_dict() != other.to_dict()
