# coding: utf-8

"""
    privatelink

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class VpcEndpointServiceForDescribeVpcEndpointServicesOutput(object):
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
        'auto_accept_enabled': 'bool',
        'creation_time': 'str',
        'description': 'str',
        'private_dns_enabled': 'bool',
        'private_dns_name': 'str',
        'private_dns_name_configuration': 'PrivateDNSNameConfigurationForDescribeVpcEndpointServicesOutput',
        'project_name': 'str',
        'service_domain': 'str',
        'service_id': 'str',
        'service_name': 'str',
        'service_resource_type': 'str',
        'service_type': 'str',
        'status': 'str',
        'tags': 'list[TagForDescribeVpcEndpointServicesOutput]',
        'update_time': 'str',
        'wildcard_domain_enabled': 'str',
        'zone_ids': 'list[str]'
    }

    attribute_map = {
        'auto_accept_enabled': 'AutoAcceptEnabled',
        'creation_time': 'CreationTime',
        'description': 'Description',
        'private_dns_enabled': 'PrivateDNSEnabled',
        'private_dns_name': 'PrivateDNSName',
        'private_dns_name_configuration': 'PrivateDNSNameConfiguration',
        'project_name': 'ProjectName',
        'service_domain': 'ServiceDomain',
        'service_id': 'ServiceId',
        'service_name': 'ServiceName',
        'service_resource_type': 'ServiceResourceType',
        'service_type': 'ServiceType',
        'status': 'Status',
        'tags': 'Tags',
        'update_time': 'UpdateTime',
        'wildcard_domain_enabled': 'WildcardDomainEnabled',
        'zone_ids': 'ZoneIds'
    }

    def __init__(self, auto_accept_enabled=None, creation_time=None, description=None, private_dns_enabled=None, private_dns_name=None, private_dns_name_configuration=None, project_name=None, service_domain=None, service_id=None, service_name=None, service_resource_type=None, service_type=None, status=None, tags=None, update_time=None, wildcard_domain_enabled=None, zone_ids=None, _configuration=None):  # noqa: E501
        """VpcEndpointServiceForDescribeVpcEndpointServicesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._auto_accept_enabled = None
        self._creation_time = None
        self._description = None
        self._private_dns_enabled = None
        self._private_dns_name = None
        self._private_dns_name_configuration = None
        self._project_name = None
        self._service_domain = None
        self._service_id = None
        self._service_name = None
        self._service_resource_type = None
        self._service_type = None
        self._status = None
        self._tags = None
        self._update_time = None
        self._wildcard_domain_enabled = None
        self._zone_ids = None
        self.discriminator = None

        if auto_accept_enabled is not None:
            self.auto_accept_enabled = auto_accept_enabled
        if creation_time is not None:
            self.creation_time = creation_time
        if description is not None:
            self.description = description
        if private_dns_enabled is not None:
            self.private_dns_enabled = private_dns_enabled
        if private_dns_name is not None:
            self.private_dns_name = private_dns_name
        if private_dns_name_configuration is not None:
            self.private_dns_name_configuration = private_dns_name_configuration
        if project_name is not None:
            self.project_name = project_name
        if service_domain is not None:
            self.service_domain = service_domain
        if service_id is not None:
            self.service_id = service_id
        if service_name is not None:
            self.service_name = service_name
        if service_resource_type is not None:
            self.service_resource_type = service_resource_type
        if service_type is not None:
            self.service_type = service_type
        if status is not None:
            self.status = status
        if tags is not None:
            self.tags = tags
        if update_time is not None:
            self.update_time = update_time
        if wildcard_domain_enabled is not None:
            self.wildcard_domain_enabled = wildcard_domain_enabled
        if zone_ids is not None:
            self.zone_ids = zone_ids

    @property
    def auto_accept_enabled(self):
        """Gets the auto_accept_enabled of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.  # noqa: E501


        :return: The auto_accept_enabled of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.  # noqa: E501
        :rtype: bool
        """
        return self._auto_accept_enabled

    @auto_accept_enabled.setter
    def auto_accept_enabled(self, auto_accept_enabled):
        """Sets the auto_accept_enabled of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.


        :param auto_accept_enabled: The auto_accept_enabled of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.  # noqa: E501
        :type: bool
        """

        self._auto_accept_enabled = auto_accept_enabled

    @property
    def creation_time(self):
        """Gets the creation_time of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.  # noqa: E501


        :return: The creation_time of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.  # noqa: E501
        :rtype: str
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.


        :param creation_time: The creation_time of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.  # noqa: E501
        :type: str
        """

        self._creation_time = creation_time

    @property
    def description(self):
        """Gets the description of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.  # noqa: E501


        :return: The description of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.


        :param description: The description of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def private_dns_enabled(self):
        """Gets the private_dns_enabled of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.  # noqa: E501


        :return: The private_dns_enabled of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.  # noqa: E501
        :rtype: bool
        """
        return self._private_dns_enabled

    @private_dns_enabled.setter
    def private_dns_enabled(self, private_dns_enabled):
        """Sets the private_dns_enabled of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.


        :param private_dns_enabled: The private_dns_enabled of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.  # noqa: E501
        :type: bool
        """

        self._private_dns_enabled = private_dns_enabled

    @property
    def private_dns_name(self):
        """Gets the private_dns_name of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.  # noqa: E501


        :return: The private_dns_name of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.  # noqa: E501
        :rtype: str
        """
        return self._private_dns_name

    @private_dns_name.setter
    def private_dns_name(self, private_dns_name):
        """Sets the private_dns_name of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.


        :param private_dns_name: The private_dns_name of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.  # noqa: E501
        :type: str
        """

        self._private_dns_name = private_dns_name

    @property
    def private_dns_name_configuration(self):
        """Gets the private_dns_name_configuration of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.  # noqa: E501


        :return: The private_dns_name_configuration of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.  # noqa: E501
        :rtype: PrivateDNSNameConfigurationForDescribeVpcEndpointServicesOutput
        """
        return self._private_dns_name_configuration

    @private_dns_name_configuration.setter
    def private_dns_name_configuration(self, private_dns_name_configuration):
        """Sets the private_dns_name_configuration of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.


        :param private_dns_name_configuration: The private_dns_name_configuration of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.  # noqa: E501
        :type: PrivateDNSNameConfigurationForDescribeVpcEndpointServicesOutput
        """

        self._private_dns_name_configuration = private_dns_name_configuration

    @property
    def project_name(self):
        """Gets the project_name of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.  # noqa: E501


        :return: The project_name of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.


        :param project_name: The project_name of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def service_domain(self):
        """Gets the service_domain of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.  # noqa: E501


        :return: The service_domain of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.  # noqa: E501
        :rtype: str
        """
        return self._service_domain

    @service_domain.setter
    def service_domain(self, service_domain):
        """Sets the service_domain of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.


        :param service_domain: The service_domain of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.  # noqa: E501
        :type: str
        """

        self._service_domain = service_domain

    @property
    def service_id(self):
        """Gets the service_id of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.  # noqa: E501


        :return: The service_id of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.  # noqa: E501
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.


        :param service_id: The service_id of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.  # noqa: E501
        :type: str
        """

        self._service_id = service_id

    @property
    def service_name(self):
        """Gets the service_name of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.  # noqa: E501


        :return: The service_name of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.  # noqa: E501
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.


        :param service_name: The service_name of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.  # noqa: E501
        :type: str
        """

        self._service_name = service_name

    @property
    def service_resource_type(self):
        """Gets the service_resource_type of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.  # noqa: E501


        :return: The service_resource_type of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.  # noqa: E501
        :rtype: str
        """
        return self._service_resource_type

    @service_resource_type.setter
    def service_resource_type(self, service_resource_type):
        """Sets the service_resource_type of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.


        :param service_resource_type: The service_resource_type of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.  # noqa: E501
        :type: str
        """

        self._service_resource_type = service_resource_type

    @property
    def service_type(self):
        """Gets the service_type of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.  # noqa: E501


        :return: The service_type of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.  # noqa: E501
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.


        :param service_type: The service_type of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.  # noqa: E501
        :type: str
        """

        self._service_type = service_type

    @property
    def status(self):
        """Gets the status of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.  # noqa: E501


        :return: The status of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.


        :param status: The status of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def tags(self):
        """Gets the tags of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.  # noqa: E501


        :return: The tags of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.  # noqa: E501
        :rtype: list[TagForDescribeVpcEndpointServicesOutput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.


        :param tags: The tags of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.  # noqa: E501
        :type: list[TagForDescribeVpcEndpointServicesOutput]
        """

        self._tags = tags

    @property
    def update_time(self):
        """Gets the update_time of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.  # noqa: E501


        :return: The update_time of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.  # noqa: E501
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.


        :param update_time: The update_time of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.  # noqa: E501
        :type: str
        """

        self._update_time = update_time

    @property
    def wildcard_domain_enabled(self):
        """Gets the wildcard_domain_enabled of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.  # noqa: E501


        :return: The wildcard_domain_enabled of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.  # noqa: E501
        :rtype: str
        """
        return self._wildcard_domain_enabled

    @wildcard_domain_enabled.setter
    def wildcard_domain_enabled(self, wildcard_domain_enabled):
        """Sets the wildcard_domain_enabled of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.


        :param wildcard_domain_enabled: The wildcard_domain_enabled of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.  # noqa: E501
        :type: str
        """

        self._wildcard_domain_enabled = wildcard_domain_enabled

    @property
    def zone_ids(self):
        """Gets the zone_ids of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.  # noqa: E501


        :return: The zone_ids of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._zone_ids

    @zone_ids.setter
    def zone_ids(self, zone_ids):
        """Sets the zone_ids of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.


        :param zone_ids: The zone_ids of this VpcEndpointServiceForDescribeVpcEndpointServicesOutput.  # noqa: E501
        :type: list[str]
        """

        self._zone_ids = zone_ids

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
        if issubclass(VpcEndpointServiceForDescribeVpcEndpointServicesOutput, dict):
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
        if not isinstance(other, VpcEndpointServiceForDescribeVpcEndpointServicesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VpcEndpointServiceForDescribeVpcEndpointServicesOutput):
            return True

        return self.to_dict() != other.to_dict()
