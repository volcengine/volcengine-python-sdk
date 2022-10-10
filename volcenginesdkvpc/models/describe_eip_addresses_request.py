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


class DescribeEipAddressesRequest(object):
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
        'allocation_ids': 'list[str]',
        'associated_instance_id': 'str',
        'associated_instance_type': 'str',
        'billing_type': 'int',
        'eip_addresses': 'list[str]',
        'isp': 'str',
        'name': 'str',
        'page_number': 'int',
        'page_size': 'int',
        'project_name': 'str',
        'security_protection_enabled': 'bool',
        'status': 'str',
        'tag_filters': 'list[TagFilterForDescribeEipAddressesInput]'
    }

    attribute_map = {
        'allocation_ids': 'AllocationIds',
        'associated_instance_id': 'AssociatedInstanceId',
        'associated_instance_type': 'AssociatedInstanceType',
        'billing_type': 'BillingType',
        'eip_addresses': 'EipAddresses',
        'isp': 'ISP',
        'name': 'Name',
        'page_number': 'PageNumber',
        'page_size': 'PageSize',
        'project_name': 'ProjectName',
        'security_protection_enabled': 'SecurityProtectionEnabled',
        'status': 'Status',
        'tag_filters': 'TagFilters'
    }

    def __init__(self, allocation_ids=None, associated_instance_id=None, associated_instance_type=None, billing_type=None, eip_addresses=None, isp=None, name=None, page_number=None, page_size=None, project_name=None, security_protection_enabled=None, status=None, tag_filters=None, _configuration=None):  # noqa: E501
        """DescribeEipAddressesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._allocation_ids = None
        self._associated_instance_id = None
        self._associated_instance_type = None
        self._billing_type = None
        self._eip_addresses = None
        self._isp = None
        self._name = None
        self._page_number = None
        self._page_size = None
        self._project_name = None
        self._security_protection_enabled = None
        self._status = None
        self._tag_filters = None
        self.discriminator = None

        if allocation_ids is not None:
            self.allocation_ids = allocation_ids
        if associated_instance_id is not None:
            self.associated_instance_id = associated_instance_id
        if associated_instance_type is not None:
            self.associated_instance_type = associated_instance_type
        if billing_type is not None:
            self.billing_type = billing_type
        if eip_addresses is not None:
            self.eip_addresses = eip_addresses
        if isp is not None:
            self.isp = isp
        if name is not None:
            self.name = name
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if project_name is not None:
            self.project_name = project_name
        if security_protection_enabled is not None:
            self.security_protection_enabled = security_protection_enabled
        if status is not None:
            self.status = status
        if tag_filters is not None:
            self.tag_filters = tag_filters

    @property
    def allocation_ids(self):
        """Gets the allocation_ids of this DescribeEipAddressesRequest.  # noqa: E501


        :return: The allocation_ids of this DescribeEipAddressesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._allocation_ids

    @allocation_ids.setter
    def allocation_ids(self, allocation_ids):
        """Sets the allocation_ids of this DescribeEipAddressesRequest.


        :param allocation_ids: The allocation_ids of this DescribeEipAddressesRequest.  # noqa: E501
        :type: list[str]
        """

        self._allocation_ids = allocation_ids

    @property
    def associated_instance_id(self):
        """Gets the associated_instance_id of this DescribeEipAddressesRequest.  # noqa: E501


        :return: The associated_instance_id of this DescribeEipAddressesRequest.  # noqa: E501
        :rtype: str
        """
        return self._associated_instance_id

    @associated_instance_id.setter
    def associated_instance_id(self, associated_instance_id):
        """Sets the associated_instance_id of this DescribeEipAddressesRequest.


        :param associated_instance_id: The associated_instance_id of this DescribeEipAddressesRequest.  # noqa: E501
        :type: str
        """

        self._associated_instance_id = associated_instance_id

    @property
    def associated_instance_type(self):
        """Gets the associated_instance_type of this DescribeEipAddressesRequest.  # noqa: E501


        :return: The associated_instance_type of this DescribeEipAddressesRequest.  # noqa: E501
        :rtype: str
        """
        return self._associated_instance_type

    @associated_instance_type.setter
    def associated_instance_type(self, associated_instance_type):
        """Sets the associated_instance_type of this DescribeEipAddressesRequest.


        :param associated_instance_type: The associated_instance_type of this DescribeEipAddressesRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["Nat", "EcsInstance", "NetworkInterface", "ClbInstance", "AlbInstance"]  # noqa: E501
        if (self._configuration.client_side_validation and
                associated_instance_type not in allowed_values):
            raise ValueError(
                "Invalid value for `associated_instance_type` ({0}), must be one of {1}"  # noqa: E501
                .format(associated_instance_type, allowed_values)
            )

        self._associated_instance_type = associated_instance_type

    @property
    def billing_type(self):
        """Gets the billing_type of this DescribeEipAddressesRequest.  # noqa: E501


        :return: The billing_type of this DescribeEipAddressesRequest.  # noqa: E501
        :rtype: int
        """
        return self._billing_type

    @billing_type.setter
    def billing_type(self, billing_type):
        """Sets the billing_type of this DescribeEipAddressesRequest.


        :param billing_type: The billing_type of this DescribeEipAddressesRequest.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                billing_type is not None and billing_type > 3):  # noqa: E501
            raise ValueError("Invalid value for `billing_type`, must be a value less than or equal to `3`")  # noqa: E501
        if (self._configuration.client_side_validation and
                billing_type is not None and billing_type < 1):  # noqa: E501
            raise ValueError("Invalid value for `billing_type`, must be a value greater than or equal to `1`")  # noqa: E501

        self._billing_type = billing_type

    @property
    def eip_addresses(self):
        """Gets the eip_addresses of this DescribeEipAddressesRequest.  # noqa: E501


        :return: The eip_addresses of this DescribeEipAddressesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._eip_addresses

    @eip_addresses.setter
    def eip_addresses(self, eip_addresses):
        """Sets the eip_addresses of this DescribeEipAddressesRequest.


        :param eip_addresses: The eip_addresses of this DescribeEipAddressesRequest.  # noqa: E501
        :type: list[str]
        """

        self._eip_addresses = eip_addresses

    @property
    def isp(self):
        """Gets the isp of this DescribeEipAddressesRequest.  # noqa: E501


        :return: The isp of this DescribeEipAddressesRequest.  # noqa: E501
        :rtype: str
        """
        return self._isp

    @isp.setter
    def isp(self, isp):
        """Sets the isp of this DescribeEipAddressesRequest.


        :param isp: The isp of this DescribeEipAddressesRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["BGP", "ChinaMobile", "ChinaUnicom", "ChinaTelecom"]  # noqa: E501
        if (self._configuration.client_side_validation and
                isp not in allowed_values):
            raise ValueError(
                "Invalid value for `isp` ({0}), must be one of {1}"  # noqa: E501
                .format(isp, allowed_values)
            )

        self._isp = isp

    @property
    def name(self):
        """Gets the name of this DescribeEipAddressesRequest.  # noqa: E501


        :return: The name of this DescribeEipAddressesRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DescribeEipAddressesRequest.


        :param name: The name of this DescribeEipAddressesRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def page_number(self):
        """Gets the page_number of this DescribeEipAddressesRequest.  # noqa: E501


        :return: The page_number of this DescribeEipAddressesRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this DescribeEipAddressesRequest.


        :param page_number: The page_number of this DescribeEipAddressesRequest.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this DescribeEipAddressesRequest.  # noqa: E501


        :return: The page_size of this DescribeEipAddressesRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this DescribeEipAddressesRequest.


        :param page_size: The page_size of this DescribeEipAddressesRequest.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                page_size is not None and page_size > 100):  # noqa: E501
            raise ValueError("Invalid value for `page_size`, must be a value less than or equal to `100`")  # noqa: E501

        self._page_size = page_size

    @property
    def project_name(self):
        """Gets the project_name of this DescribeEipAddressesRequest.  # noqa: E501


        :return: The project_name of this DescribeEipAddressesRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this DescribeEipAddressesRequest.


        :param project_name: The project_name of this DescribeEipAddressesRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def security_protection_enabled(self):
        """Gets the security_protection_enabled of this DescribeEipAddressesRequest.  # noqa: E501


        :return: The security_protection_enabled of this DescribeEipAddressesRequest.  # noqa: E501
        :rtype: bool
        """
        return self._security_protection_enabled

    @security_protection_enabled.setter
    def security_protection_enabled(self, security_protection_enabled):
        """Sets the security_protection_enabled of this DescribeEipAddressesRequest.


        :param security_protection_enabled: The security_protection_enabled of this DescribeEipAddressesRequest.  # noqa: E501
        :type: bool
        """

        self._security_protection_enabled = security_protection_enabled

    @property
    def status(self):
        """Gets the status of this DescribeEipAddressesRequest.  # noqa: E501


        :return: The status of this DescribeEipAddressesRequest.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DescribeEipAddressesRequest.


        :param status: The status of this DescribeEipAddressesRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["Attaching", "Detaching", "Attached", "Available"]  # noqa: E501
        if (self._configuration.client_side_validation and
                status not in allowed_values):
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def tag_filters(self):
        """Gets the tag_filters of this DescribeEipAddressesRequest.  # noqa: E501


        :return: The tag_filters of this DescribeEipAddressesRequest.  # noqa: E501
        :rtype: list[TagFilterForDescribeEipAddressesInput]
        """
        return self._tag_filters

    @tag_filters.setter
    def tag_filters(self, tag_filters):
        """Sets the tag_filters of this DescribeEipAddressesRequest.


        :param tag_filters: The tag_filters of this DescribeEipAddressesRequest.  # noqa: E501
        :type: list[TagFilterForDescribeEipAddressesInput]
        """

        self._tag_filters = tag_filters

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
        if issubclass(DescribeEipAddressesRequest, dict):
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
        if not isinstance(other, DescribeEipAddressesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeEipAddressesRequest):
            return True

        return self.to_dict() != other.to_dict()
