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


class DescribeDBInstancesRequest(object):
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
        'charge_type': 'str',
        'data_layout': 'str',
        'engine_version': 'str',
        'instance_id': 'str',
        'instance_name': 'str',
        'page_number': 'int',
        'page_size': 'int',
        'project_name': 'str',
        'region_id': 'str',
        'service_type': 'str',
        'sharded_cluster': 'int',
        'status': 'str',
        'tag_filters': 'list[TagFilterForDescribeDBInstancesInput]',
        'vpc_id': 'str',
        'zone_id': 'str'
    }

    attribute_map = {
        'charge_type': 'ChargeType',
        'data_layout': 'DataLayout',
        'engine_version': 'EngineVersion',
        'instance_id': 'InstanceId',
        'instance_name': 'InstanceName',
        'page_number': 'PageNumber',
        'page_size': 'PageSize',
        'project_name': 'ProjectName',
        'region_id': 'RegionId',
        'service_type': 'ServiceType',
        'sharded_cluster': 'ShardedCluster',
        'status': 'Status',
        'tag_filters': 'TagFilters',
        'vpc_id': 'VpcId',
        'zone_id': 'ZoneId'
    }

    def __init__(self, charge_type=None, data_layout=None, engine_version=None, instance_id=None, instance_name=None, page_number=None, page_size=None, project_name=None, region_id=None, service_type=None, sharded_cluster=None, status=None, tag_filters=None, vpc_id=None, zone_id=None, _configuration=None):  # noqa: E501
        """DescribeDBInstancesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._charge_type = None
        self._data_layout = None
        self._engine_version = None
        self._instance_id = None
        self._instance_name = None
        self._page_number = None
        self._page_size = None
        self._project_name = None
        self._region_id = None
        self._service_type = None
        self._sharded_cluster = None
        self._status = None
        self._tag_filters = None
        self._vpc_id = None
        self._zone_id = None
        self.discriminator = None

        if charge_type is not None:
            self.charge_type = charge_type
        if data_layout is not None:
            self.data_layout = data_layout
        if engine_version is not None:
            self.engine_version = engine_version
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        self.page_number = page_number
        self.page_size = page_size
        if project_name is not None:
            self.project_name = project_name
        self.region_id = region_id
        if service_type is not None:
            self.service_type = service_type
        if sharded_cluster is not None:
            self.sharded_cluster = sharded_cluster
        if status is not None:
            self.status = status
        if tag_filters is not None:
            self.tag_filters = tag_filters
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if zone_id is not None:
            self.zone_id = zone_id

    @property
    def charge_type(self):
        """Gets the charge_type of this DescribeDBInstancesRequest.  # noqa: E501


        :return: The charge_type of this DescribeDBInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._charge_type

    @charge_type.setter
    def charge_type(self, charge_type):
        """Sets the charge_type of this DescribeDBInstancesRequest.


        :param charge_type: The charge_type of this DescribeDBInstancesRequest.  # noqa: E501
        :type: str
        """

        self._charge_type = charge_type

    @property
    def data_layout(self):
        """Gets the data_layout of this DescribeDBInstancesRequest.  # noqa: E501


        :return: The data_layout of this DescribeDBInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._data_layout

    @data_layout.setter
    def data_layout(self, data_layout):
        """Sets the data_layout of this DescribeDBInstancesRequest.


        :param data_layout: The data_layout of this DescribeDBInstancesRequest.  # noqa: E501
        :type: str
        """

        self._data_layout = data_layout

    @property
    def engine_version(self):
        """Gets the engine_version of this DescribeDBInstancesRequest.  # noqa: E501


        :return: The engine_version of this DescribeDBInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        """Sets the engine_version of this DescribeDBInstancesRequest.


        :param engine_version: The engine_version of this DescribeDBInstancesRequest.  # noqa: E501
        :type: str
        """

        self._engine_version = engine_version

    @property
    def instance_id(self):
        """Gets the instance_id of this DescribeDBInstancesRequest.  # noqa: E501


        :return: The instance_id of this DescribeDBInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this DescribeDBInstancesRequest.


        :param instance_id: The instance_id of this DescribeDBInstancesRequest.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def instance_name(self):
        """Gets the instance_name of this DescribeDBInstancesRequest.  # noqa: E501


        :return: The instance_name of this DescribeDBInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this DescribeDBInstancesRequest.


        :param instance_name: The instance_name of this DescribeDBInstancesRequest.  # noqa: E501
        :type: str
        """

        self._instance_name = instance_name

    @property
    def page_number(self):
        """Gets the page_number of this DescribeDBInstancesRequest.  # noqa: E501


        :return: The page_number of this DescribeDBInstancesRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this DescribeDBInstancesRequest.


        :param page_number: The page_number of this DescribeDBInstancesRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and page_number is None:
            raise ValueError("Invalid value for `page_number`, must not be `None`")  # noqa: E501

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this DescribeDBInstancesRequest.  # noqa: E501


        :return: The page_size of this DescribeDBInstancesRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this DescribeDBInstancesRequest.


        :param page_size: The page_size of this DescribeDBInstancesRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and page_size is None:
            raise ValueError("Invalid value for `page_size`, must not be `None`")  # noqa: E501

        self._page_size = page_size

    @property
    def project_name(self):
        """Gets the project_name of this DescribeDBInstancesRequest.  # noqa: E501


        :return: The project_name of this DescribeDBInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this DescribeDBInstancesRequest.


        :param project_name: The project_name of this DescribeDBInstancesRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def region_id(self):
        """Gets the region_id of this DescribeDBInstancesRequest.  # noqa: E501


        :return: The region_id of this DescribeDBInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this DescribeDBInstancesRequest.


        :param region_id: The region_id of this DescribeDBInstancesRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and region_id is None:
            raise ValueError("Invalid value for `region_id`, must not be `None`")  # noqa: E501

        self._region_id = region_id

    @property
    def service_type(self):
        """Gets the service_type of this DescribeDBInstancesRequest.  # noqa: E501


        :return: The service_type of this DescribeDBInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this DescribeDBInstancesRequest.


        :param service_type: The service_type of this DescribeDBInstancesRequest.  # noqa: E501
        :type: str
        """

        self._service_type = service_type

    @property
    def sharded_cluster(self):
        """Gets the sharded_cluster of this DescribeDBInstancesRequest.  # noqa: E501


        :return: The sharded_cluster of this DescribeDBInstancesRequest.  # noqa: E501
        :rtype: int
        """
        return self._sharded_cluster

    @sharded_cluster.setter
    def sharded_cluster(self, sharded_cluster):
        """Sets the sharded_cluster of this DescribeDBInstancesRequest.


        :param sharded_cluster: The sharded_cluster of this DescribeDBInstancesRequest.  # noqa: E501
        :type: int
        """

        self._sharded_cluster = sharded_cluster

    @property
    def status(self):
        """Gets the status of this DescribeDBInstancesRequest.  # noqa: E501


        :return: The status of this DescribeDBInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DescribeDBInstancesRequest.


        :param status: The status of this DescribeDBInstancesRequest.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def tag_filters(self):
        """Gets the tag_filters of this DescribeDBInstancesRequest.  # noqa: E501


        :return: The tag_filters of this DescribeDBInstancesRequest.  # noqa: E501
        :rtype: list[TagFilterForDescribeDBInstancesInput]
        """
        return self._tag_filters

    @tag_filters.setter
    def tag_filters(self, tag_filters):
        """Sets the tag_filters of this DescribeDBInstancesRequest.


        :param tag_filters: The tag_filters of this DescribeDBInstancesRequest.  # noqa: E501
        :type: list[TagFilterForDescribeDBInstancesInput]
        """

        self._tag_filters = tag_filters

    @property
    def vpc_id(self):
        """Gets the vpc_id of this DescribeDBInstancesRequest.  # noqa: E501


        :return: The vpc_id of this DescribeDBInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this DescribeDBInstancesRequest.


        :param vpc_id: The vpc_id of this DescribeDBInstancesRequest.  # noqa: E501
        :type: str
        """

        self._vpc_id = vpc_id

    @property
    def zone_id(self):
        """Gets the zone_id of this DescribeDBInstancesRequest.  # noqa: E501


        :return: The zone_id of this DescribeDBInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this DescribeDBInstancesRequest.


        :param zone_id: The zone_id of this DescribeDBInstancesRequest.  # noqa: E501
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
        if issubclass(DescribeDBInstancesRequest, dict):
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
        if not isinstance(other, DescribeDBInstancesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeDBInstancesRequest):
            return True

        return self.to_dict() != other.to_dict()
