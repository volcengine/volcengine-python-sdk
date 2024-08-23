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


class VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput(object):
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
        'billing_type': 'int',
        'business_status': 'str',
        'creation_time': 'str',
        'description': 'str',
        'ip_address_versions': 'list[str]',
        'payer': 'str',
        'private_dns_enabled': 'bool',
        'private_dns_name': 'str',
        'private_dns_name_configuration': 'PrivateDNSNameConfigurationForDescribeVpcEndpointServicesByEndUserOutput',
        'private_dns_type': 'str',
        'project_name': 'str',
        'service_domain': 'str',
        'service_id': 'str',
        'service_name': 'str',
        'service_owner': 'str',
        'service_resource_type': 'str',
        'service_type': 'str',
        'status': 'str',
        'tags': 'list[TagForDescribeVpcEndpointServicesByEndUserOutput]',
        'update_time': 'str',
        'wildcard_domain_enabled': 'str',
        'zone_ids': 'list[str]'
    }

    attribute_map = {
        'auto_accept_enabled': 'AutoAcceptEnabled',
        'billing_type': 'BillingType',
        'business_status': 'BusinessStatus',
        'creation_time': 'CreationTime',
        'description': 'Description',
        'ip_address_versions': 'IpAddressVersions',
        'payer': 'Payer',
        'private_dns_enabled': 'PrivateDNSEnabled',
        'private_dns_name': 'PrivateDNSName',
        'private_dns_name_configuration': 'PrivateDNSNameConfiguration',
        'private_dns_type': 'PrivateDNSType',
        'project_name': 'ProjectName',
        'service_domain': 'ServiceDomain',
        'service_id': 'ServiceId',
        'service_name': 'ServiceName',
        'service_owner': 'ServiceOwner',
        'service_resource_type': 'ServiceResourceType',
        'service_type': 'ServiceType',
        'status': 'Status',
        'tags': 'Tags',
        'update_time': 'UpdateTime',
        'wildcard_domain_enabled': 'WildcardDomainEnabled',
        'zone_ids': 'ZoneIds'
    }

    def __init__(self, auto_accept_enabled=None, billing_type=None, business_status=None, creation_time=None, description=None, ip_address_versions=None, payer=None, private_dns_enabled=None, private_dns_name=None, private_dns_name_configuration=None, private_dns_type=None, project_name=None, service_domain=None, service_id=None, service_name=None, service_owner=None, service_resource_type=None, service_type=None, status=None, tags=None, update_time=None, wildcard_domain_enabled=None, zone_ids=None, _configuration=None):  # noqa: E501
        """VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._auto_accept_enabled = None
        self._billing_type = None
        self._business_status = None
        self._creation_time = None
        self._description = None
        self._ip_address_versions = None
        self._payer = None
        self._private_dns_enabled = None
        self._private_dns_name = None
        self._private_dns_name_configuration = None
        self._private_dns_type = None
        self._project_name = None
        self._service_domain = None
        self._service_id = None
        self._service_name = None
        self._service_owner = None
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
        if billing_type is not None:
            self.billing_type = billing_type
        if business_status is not None:
            self.business_status = business_status
        if creation_time is not None:
            self.creation_time = creation_time
        if description is not None:
            self.description = description
        if ip_address_versions is not None:
            self.ip_address_versions = ip_address_versions
        if payer is not None:
            self.payer = payer
        if private_dns_enabled is not None:
            self.private_dns_enabled = private_dns_enabled
        if private_dns_name is not None:
            self.private_dns_name = private_dns_name
        if private_dns_name_configuration is not None:
            self.private_dns_name_configuration = private_dns_name_configuration
        if private_dns_type is not None:
            self.private_dns_type = private_dns_type
        if project_name is not None:
            self.project_name = project_name
        if service_domain is not None:
            self.service_domain = service_domain
        if service_id is not None:
            self.service_id = service_id
        if service_name is not None:
            self.service_name = service_name
        if service_owner is not None:
            self.service_owner = service_owner
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
        """Gets the auto_accept_enabled of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501


        :return: The auto_accept_enabled of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
        :rtype: bool
        """
        return self._auto_accept_enabled

    @auto_accept_enabled.setter
    def auto_accept_enabled(self, auto_accept_enabled):
        """Sets the auto_accept_enabled of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.


        :param auto_accept_enabled: The auto_accept_enabled of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
        :type: bool
        """

        self._auto_accept_enabled = auto_accept_enabled

    @property
    def billing_type(self):
        """Gets the billing_type of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501


        :return: The billing_type of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
        :rtype: int
        """
        return self._billing_type

    @billing_type.setter
    def billing_type(self, billing_type):
        """Sets the billing_type of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.


        :param billing_type: The billing_type of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
        :type: int
        """

        self._billing_type = billing_type

    @property
    def business_status(self):
        """Gets the business_status of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501


        :return: The business_status of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
        :rtype: str
        """
        return self._business_status

    @business_status.setter
    def business_status(self, business_status):
        """Sets the business_status of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.


        :param business_status: The business_status of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
        :type: str
        """

        self._business_status = business_status

    @property
    def creation_time(self):
        """Gets the creation_time of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501


        :return: The creation_time of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
        :rtype: str
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.


        :param creation_time: The creation_time of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
        :type: str
        """

        self._creation_time = creation_time

    @property
    def description(self):
        """Gets the description of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501


        :return: The description of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.


        :param description: The description of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def ip_address_versions(self):
        """Gets the ip_address_versions of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501


        :return: The ip_address_versions of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._ip_address_versions

    @ip_address_versions.setter
    def ip_address_versions(self, ip_address_versions):
        """Sets the ip_address_versions of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.


        :param ip_address_versions: The ip_address_versions of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
        :type: list[str]
        """

        self._ip_address_versions = ip_address_versions

    @property
    def payer(self):
        """Gets the payer of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501


        :return: The payer of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
        :rtype: str
        """
        return self._payer

    @payer.setter
    def payer(self, payer):
        """Sets the payer of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.


        :param payer: The payer of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
        :type: str
        """

        self._payer = payer

    @property
    def private_dns_enabled(self):
        """Gets the private_dns_enabled of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501


        :return: The private_dns_enabled of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
        :rtype: bool
        """
        return self._private_dns_enabled

    @private_dns_enabled.setter
    def private_dns_enabled(self, private_dns_enabled):
        """Sets the private_dns_enabled of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.


        :param private_dns_enabled: The private_dns_enabled of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
        :type: bool
        """

        self._private_dns_enabled = private_dns_enabled

    @property
    def private_dns_name(self):
        """Gets the private_dns_name of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501


        :return: The private_dns_name of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
        :rtype: str
        """
        return self._private_dns_name

    @private_dns_name.setter
    def private_dns_name(self, private_dns_name):
        """Sets the private_dns_name of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.


        :param private_dns_name: The private_dns_name of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
        :type: str
        """

        self._private_dns_name = private_dns_name

    @property
    def private_dns_name_configuration(self):
        """Gets the private_dns_name_configuration of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501


        :return: The private_dns_name_configuration of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
        :rtype: PrivateDNSNameConfigurationForDescribeVpcEndpointServicesByEndUserOutput
        """
        return self._private_dns_name_configuration

    @private_dns_name_configuration.setter
    def private_dns_name_configuration(self, private_dns_name_configuration):
        """Sets the private_dns_name_configuration of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.


        :param private_dns_name_configuration: The private_dns_name_configuration of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
        :type: PrivateDNSNameConfigurationForDescribeVpcEndpointServicesByEndUserOutput
        """

        self._private_dns_name_configuration = private_dns_name_configuration

    @property
    def private_dns_type(self):
        """Gets the private_dns_type of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501


        :return: The private_dns_type of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
        :rtype: str
        """
        return self._private_dns_type

    @private_dns_type.setter
    def private_dns_type(self, private_dns_type):
        """Sets the private_dns_type of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.


        :param private_dns_type: The private_dns_type of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
        :type: str
        """

        self._private_dns_type = private_dns_type

    @property
    def project_name(self):
        """Gets the project_name of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501


        :return: The project_name of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.


        :param project_name: The project_name of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def service_domain(self):
        """Gets the service_domain of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501


        :return: The service_domain of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
        :rtype: str
        """
        return self._service_domain

    @service_domain.setter
    def service_domain(self, service_domain):
        """Sets the service_domain of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.


        :param service_domain: The service_domain of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
        :type: str
        """

        self._service_domain = service_domain

    @property
    def service_id(self):
        """Gets the service_id of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501


        :return: The service_id of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.


        :param service_id: The service_id of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
        :type: str
        """

        self._service_id = service_id

    @property
    def service_name(self):
        """Gets the service_name of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501


        :return: The service_name of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.


        :param service_name: The service_name of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
        :type: str
        """

        self._service_name = service_name

    @property
    def service_owner(self):
        """Gets the service_owner of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501


        :return: The service_owner of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
        :rtype: str
        """
        return self._service_owner

    @service_owner.setter
    def service_owner(self, service_owner):
        """Sets the service_owner of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.


        :param service_owner: The service_owner of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
        :type: str
        """

        self._service_owner = service_owner

    @property
    def service_resource_type(self):
        """Gets the service_resource_type of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501


        :return: The service_resource_type of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
        :rtype: str
        """
        return self._service_resource_type

    @service_resource_type.setter
    def service_resource_type(self, service_resource_type):
        """Sets the service_resource_type of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.


        :param service_resource_type: The service_resource_type of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
        :type: str
        """

        self._service_resource_type = service_resource_type

    @property
    def service_type(self):
        """Gets the service_type of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501


        :return: The service_type of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.


        :param service_type: The service_type of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
        :type: str
        """

        self._service_type = service_type

    @property
    def status(self):
        """Gets the status of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501


        :return: The status of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.


        :param status: The status of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def tags(self):
        """Gets the tags of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501


        :return: The tags of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
        :rtype: list[TagForDescribeVpcEndpointServicesByEndUserOutput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.


        :param tags: The tags of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
        :type: list[TagForDescribeVpcEndpointServicesByEndUserOutput]
        """

        self._tags = tags

    @property
    def update_time(self):
        """Gets the update_time of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501


        :return: The update_time of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.


        :param update_time: The update_time of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
        :type: str
        """

        self._update_time = update_time

    @property
    def wildcard_domain_enabled(self):
        """Gets the wildcard_domain_enabled of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501


        :return: The wildcard_domain_enabled of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
        :rtype: str
        """
        return self._wildcard_domain_enabled

    @wildcard_domain_enabled.setter
    def wildcard_domain_enabled(self, wildcard_domain_enabled):
        """Sets the wildcard_domain_enabled of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.


        :param wildcard_domain_enabled: The wildcard_domain_enabled of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
        :type: str
        """

        self._wildcard_domain_enabled = wildcard_domain_enabled

    @property
    def zone_ids(self):
        """Gets the zone_ids of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501


        :return: The zone_ids of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._zone_ids

    @zone_ids.setter
    def zone_ids(self, zone_ids):
        """Sets the zone_ids of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.


        :param zone_ids: The zone_ids of this VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput.  # noqa: E501
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
        if issubclass(VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput, dict):
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
        if not isinstance(other, VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VpcEndpointServiceForDescribeVpcEndpointServicesByEndUserOutput):
            return True

        return self.to_dict() != other.to_dict()
