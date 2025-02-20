# coding: utf-8

"""
    vpc

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class BandwidthPackageForDescribeBandwidthPackagesOutput(object):
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
        'bandwidth': 'int',
        'bandwidth_package_id': 'str',
        'bandwidth_package_name': 'str',
        'billing_type': 'int',
        'business_status': 'str',
        'creation_time': 'str',
        'deleted_time': 'str',
        'description': 'str',
        'eip_addresses': 'list[EipAddressForDescribeBandwidthPackagesOutput]',
        'expired_time': 'str',
        'isp': 'str',
        'overdue_time': 'str',
        'project_name': 'str',
        'protocol': 'str',
        'ratio': 'int',
        'security_protection_types': 'list[str]',
        'status': 'str',
        'tags': 'list[TagForDescribeBandwidthPackagesOutput]',
        'update_time': 'str'
    }

    attribute_map = {
        'bandwidth': 'Bandwidth',
        'bandwidth_package_id': 'BandwidthPackageId',
        'bandwidth_package_name': 'BandwidthPackageName',
        'billing_type': 'BillingType',
        'business_status': 'BusinessStatus',
        'creation_time': 'CreationTime',
        'deleted_time': 'DeletedTime',
        'description': 'Description',
        'eip_addresses': 'EipAddresses',
        'expired_time': 'ExpiredTime',
        'isp': 'ISP',
        'overdue_time': 'OverdueTime',
        'project_name': 'ProjectName',
        'protocol': 'Protocol',
        'ratio': 'Ratio',
        'security_protection_types': 'SecurityProtectionTypes',
        'status': 'Status',
        'tags': 'Tags',
        'update_time': 'UpdateTime'
    }

    def __init__(self, bandwidth=None, bandwidth_package_id=None, bandwidth_package_name=None, billing_type=None, business_status=None, creation_time=None, deleted_time=None, description=None, eip_addresses=None, expired_time=None, isp=None, overdue_time=None, project_name=None, protocol=None, ratio=None, security_protection_types=None, status=None, tags=None, update_time=None, _configuration=None):  # noqa: E501
        """BandwidthPackageForDescribeBandwidthPackagesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bandwidth = None
        self._bandwidth_package_id = None
        self._bandwidth_package_name = None
        self._billing_type = None
        self._business_status = None
        self._creation_time = None
        self._deleted_time = None
        self._description = None
        self._eip_addresses = None
        self._expired_time = None
        self._isp = None
        self._overdue_time = None
        self._project_name = None
        self._protocol = None
        self._ratio = None
        self._security_protection_types = None
        self._status = None
        self._tags = None
        self._update_time = None
        self.discriminator = None

        if bandwidth is not None:
            self.bandwidth = bandwidth
        if bandwidth_package_id is not None:
            self.bandwidth_package_id = bandwidth_package_id
        if bandwidth_package_name is not None:
            self.bandwidth_package_name = bandwidth_package_name
        if billing_type is not None:
            self.billing_type = billing_type
        if business_status is not None:
            self.business_status = business_status
        if creation_time is not None:
            self.creation_time = creation_time
        if deleted_time is not None:
            self.deleted_time = deleted_time
        if description is not None:
            self.description = description
        if eip_addresses is not None:
            self.eip_addresses = eip_addresses
        if expired_time is not None:
            self.expired_time = expired_time
        if isp is not None:
            self.isp = isp
        if overdue_time is not None:
            self.overdue_time = overdue_time
        if project_name is not None:
            self.project_name = project_name
        if protocol is not None:
            self.protocol = protocol
        if ratio is not None:
            self.ratio = ratio
        if security_protection_types is not None:
            self.security_protection_types = security_protection_types
        if status is not None:
            self.status = status
        if tags is not None:
            self.tags = tags
        if update_time is not None:
            self.update_time = update_time

    @property
    def bandwidth(self):
        """Gets the bandwidth of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501


        :return: The bandwidth of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501
        :rtype: int
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this BandwidthPackageForDescribeBandwidthPackagesOutput.


        :param bandwidth: The bandwidth of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501
        :type: int
        """

        self._bandwidth = bandwidth

    @property
    def bandwidth_package_id(self):
        """Gets the bandwidth_package_id of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501


        :return: The bandwidth_package_id of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501
        :rtype: str
        """
        return self._bandwidth_package_id

    @bandwidth_package_id.setter
    def bandwidth_package_id(self, bandwidth_package_id):
        """Sets the bandwidth_package_id of this BandwidthPackageForDescribeBandwidthPackagesOutput.


        :param bandwidth_package_id: The bandwidth_package_id of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501
        :type: str
        """

        self._bandwidth_package_id = bandwidth_package_id

    @property
    def bandwidth_package_name(self):
        """Gets the bandwidth_package_name of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501


        :return: The bandwidth_package_name of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501
        :rtype: str
        """
        return self._bandwidth_package_name

    @bandwidth_package_name.setter
    def bandwidth_package_name(self, bandwidth_package_name):
        """Sets the bandwidth_package_name of this BandwidthPackageForDescribeBandwidthPackagesOutput.


        :param bandwidth_package_name: The bandwidth_package_name of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501
        :type: str
        """

        self._bandwidth_package_name = bandwidth_package_name

    @property
    def billing_type(self):
        """Gets the billing_type of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501


        :return: The billing_type of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501
        :rtype: int
        """
        return self._billing_type

    @billing_type.setter
    def billing_type(self, billing_type):
        """Sets the billing_type of this BandwidthPackageForDescribeBandwidthPackagesOutput.


        :param billing_type: The billing_type of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501
        :type: int
        """

        self._billing_type = billing_type

    @property
    def business_status(self):
        """Gets the business_status of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501


        :return: The business_status of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501
        :rtype: str
        """
        return self._business_status

    @business_status.setter
    def business_status(self, business_status):
        """Sets the business_status of this BandwidthPackageForDescribeBandwidthPackagesOutput.


        :param business_status: The business_status of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501
        :type: str
        """

        self._business_status = business_status

    @property
    def creation_time(self):
        """Gets the creation_time of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501


        :return: The creation_time of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501
        :rtype: str
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this BandwidthPackageForDescribeBandwidthPackagesOutput.


        :param creation_time: The creation_time of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501
        :type: str
        """

        self._creation_time = creation_time

    @property
    def deleted_time(self):
        """Gets the deleted_time of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501


        :return: The deleted_time of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501
        :rtype: str
        """
        return self._deleted_time

    @deleted_time.setter
    def deleted_time(self, deleted_time):
        """Sets the deleted_time of this BandwidthPackageForDescribeBandwidthPackagesOutput.


        :param deleted_time: The deleted_time of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501
        :type: str
        """

        self._deleted_time = deleted_time

    @property
    def description(self):
        """Gets the description of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501


        :return: The description of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BandwidthPackageForDescribeBandwidthPackagesOutput.


        :param description: The description of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def eip_addresses(self):
        """Gets the eip_addresses of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501


        :return: The eip_addresses of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501
        :rtype: list[EipAddressForDescribeBandwidthPackagesOutput]
        """
        return self._eip_addresses

    @eip_addresses.setter
    def eip_addresses(self, eip_addresses):
        """Sets the eip_addresses of this BandwidthPackageForDescribeBandwidthPackagesOutput.


        :param eip_addresses: The eip_addresses of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501
        :type: list[EipAddressForDescribeBandwidthPackagesOutput]
        """

        self._eip_addresses = eip_addresses

    @property
    def expired_time(self):
        """Gets the expired_time of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501


        :return: The expired_time of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501
        :rtype: str
        """
        return self._expired_time

    @expired_time.setter
    def expired_time(self, expired_time):
        """Sets the expired_time of this BandwidthPackageForDescribeBandwidthPackagesOutput.


        :param expired_time: The expired_time of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501
        :type: str
        """

        self._expired_time = expired_time

    @property
    def isp(self):
        """Gets the isp of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501


        :return: The isp of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501
        :rtype: str
        """
        return self._isp

    @isp.setter
    def isp(self, isp):
        """Sets the isp of this BandwidthPackageForDescribeBandwidthPackagesOutput.


        :param isp: The isp of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501
        :type: str
        """

        self._isp = isp

    @property
    def overdue_time(self):
        """Gets the overdue_time of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501


        :return: The overdue_time of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501
        :rtype: str
        """
        return self._overdue_time

    @overdue_time.setter
    def overdue_time(self, overdue_time):
        """Sets the overdue_time of this BandwidthPackageForDescribeBandwidthPackagesOutput.


        :param overdue_time: The overdue_time of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501
        :type: str
        """

        self._overdue_time = overdue_time

    @property
    def project_name(self):
        """Gets the project_name of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501


        :return: The project_name of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this BandwidthPackageForDescribeBandwidthPackagesOutput.


        :param project_name: The project_name of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def protocol(self):
        """Gets the protocol of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501


        :return: The protocol of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this BandwidthPackageForDescribeBandwidthPackagesOutput.


        :param protocol: The protocol of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501
        :type: str
        """

        self._protocol = protocol

    @property
    def ratio(self):
        """Gets the ratio of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501


        :return: The ratio of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501
        :rtype: int
        """
        return self._ratio

    @ratio.setter
    def ratio(self, ratio):
        """Sets the ratio of this BandwidthPackageForDescribeBandwidthPackagesOutput.


        :param ratio: The ratio of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501
        :type: int
        """

        self._ratio = ratio

    @property
    def security_protection_types(self):
        """Gets the security_protection_types of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501


        :return: The security_protection_types of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._security_protection_types

    @security_protection_types.setter
    def security_protection_types(self, security_protection_types):
        """Sets the security_protection_types of this BandwidthPackageForDescribeBandwidthPackagesOutput.


        :param security_protection_types: The security_protection_types of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501
        :type: list[str]
        """

        self._security_protection_types = security_protection_types

    @property
    def status(self):
        """Gets the status of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501


        :return: The status of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BandwidthPackageForDescribeBandwidthPackagesOutput.


        :param status: The status of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def tags(self):
        """Gets the tags of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501


        :return: The tags of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501
        :rtype: list[TagForDescribeBandwidthPackagesOutput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this BandwidthPackageForDescribeBandwidthPackagesOutput.


        :param tags: The tags of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501
        :type: list[TagForDescribeBandwidthPackagesOutput]
        """

        self._tags = tags

    @property
    def update_time(self):
        """Gets the update_time of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501


        :return: The update_time of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this BandwidthPackageForDescribeBandwidthPackagesOutput.


        :param update_time: The update_time of this BandwidthPackageForDescribeBandwidthPackagesOutput.  # noqa: E501
        :type: str
        """

        self._update_time = update_time

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
        if issubclass(BandwidthPackageForDescribeBandwidthPackagesOutput, dict):
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
        if not isinstance(other, BandwidthPackageForDescribeBandwidthPackagesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BandwidthPackageForDescribeBandwidthPackagesOutput):
            return True

        return self.to_dict() != other.to_dict()
