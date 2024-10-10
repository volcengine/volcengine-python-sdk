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


class AllocateEipAddressRequest(object):
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
        'billing_type': 'int',
        'client_token': 'str',
        'description': 'str',
        'isp': 'str',
        'ip_address': 'str',
        'ip_address_pool_id': 'str',
        'name': 'str',
        'period': 'int',
        'period_unit': 'int',
        'project_name': 'str',
        'renew_period_times': 'int',
        'renew_type': 'int',
        'security_protection_instance_id': 'int',
        'security_protection_types': 'list[str]',
        'tags': 'list[TagForAllocateEipAddressInput]'
    }

    attribute_map = {
        'bandwidth': 'Bandwidth',
        'bandwidth_package_id': 'BandwidthPackageId',
        'billing_type': 'BillingType',
        'client_token': 'ClientToken',
        'description': 'Description',
        'isp': 'ISP',
        'ip_address': 'IpAddress',
        'ip_address_pool_id': 'IpAddressPoolId',
        'name': 'Name',
        'period': 'Period',
        'period_unit': 'PeriodUnit',
        'project_name': 'ProjectName',
        'renew_period_times': 'RenewPeriodTimes',
        'renew_type': 'RenewType',
        'security_protection_instance_id': 'SecurityProtectionInstanceId',
        'security_protection_types': 'SecurityProtectionTypes',
        'tags': 'Tags'
    }

    def __init__(self, bandwidth=None, bandwidth_package_id=None, billing_type=None, client_token=None, description=None, isp=None, ip_address=None, ip_address_pool_id=None, name=None, period=None, period_unit=None, project_name=None, renew_period_times=None, renew_type=None, security_protection_instance_id=None, security_protection_types=None, tags=None, _configuration=None):  # noqa: E501
        """AllocateEipAddressRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bandwidth = None
        self._bandwidth_package_id = None
        self._billing_type = None
        self._client_token = None
        self._description = None
        self._isp = None
        self._ip_address = None
        self._ip_address_pool_id = None
        self._name = None
        self._period = None
        self._period_unit = None
        self._project_name = None
        self._renew_period_times = None
        self._renew_type = None
        self._security_protection_instance_id = None
        self._security_protection_types = None
        self._tags = None
        self.discriminator = None

        if bandwidth is not None:
            self.bandwidth = bandwidth
        if bandwidth_package_id is not None:
            self.bandwidth_package_id = bandwidth_package_id
        if billing_type is not None:
            self.billing_type = billing_type
        if client_token is not None:
            self.client_token = client_token
        if description is not None:
            self.description = description
        if isp is not None:
            self.isp = isp
        if ip_address is not None:
            self.ip_address = ip_address
        if ip_address_pool_id is not None:
            self.ip_address_pool_id = ip_address_pool_id
        if name is not None:
            self.name = name
        if period is not None:
            self.period = period
        if period_unit is not None:
            self.period_unit = period_unit
        if project_name is not None:
            self.project_name = project_name
        if renew_period_times is not None:
            self.renew_period_times = renew_period_times
        if renew_type is not None:
            self.renew_type = renew_type
        if security_protection_instance_id is not None:
            self.security_protection_instance_id = security_protection_instance_id
        if security_protection_types is not None:
            self.security_protection_types = security_protection_types
        if tags is not None:
            self.tags = tags

    @property
    def bandwidth(self):
        """Gets the bandwidth of this AllocateEipAddressRequest.  # noqa: E501


        :return: The bandwidth of this AllocateEipAddressRequest.  # noqa: E501
        :rtype: int
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this AllocateEipAddressRequest.


        :param bandwidth: The bandwidth of this AllocateEipAddressRequest.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                bandwidth is not None and bandwidth < 1):  # noqa: E501
            raise ValueError("Invalid value for `bandwidth`, must be a value greater than or equal to `1`")  # noqa: E501

        self._bandwidth = bandwidth

    @property
    def bandwidth_package_id(self):
        """Gets the bandwidth_package_id of this AllocateEipAddressRequest.  # noqa: E501


        :return: The bandwidth_package_id of this AllocateEipAddressRequest.  # noqa: E501
        :rtype: str
        """
        return self._bandwidth_package_id

    @bandwidth_package_id.setter
    def bandwidth_package_id(self, bandwidth_package_id):
        """Sets the bandwidth_package_id of this AllocateEipAddressRequest.


        :param bandwidth_package_id: The bandwidth_package_id of this AllocateEipAddressRequest.  # noqa: E501
        :type: str
        """

        self._bandwidth_package_id = bandwidth_package_id

    @property
    def billing_type(self):
        """Gets the billing_type of this AllocateEipAddressRequest.  # noqa: E501


        :return: The billing_type of this AllocateEipAddressRequest.  # noqa: E501
        :rtype: int
        """
        return self._billing_type

    @billing_type.setter
    def billing_type(self, billing_type):
        """Sets the billing_type of this AllocateEipAddressRequest.


        :param billing_type: The billing_type of this AllocateEipAddressRequest.  # noqa: E501
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
    def client_token(self):
        """Gets the client_token of this AllocateEipAddressRequest.  # noqa: E501


        :return: The client_token of this AllocateEipAddressRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_token

    @client_token.setter
    def client_token(self, client_token):
        """Sets the client_token of this AllocateEipAddressRequest.


        :param client_token: The client_token of this AllocateEipAddressRequest.  # noqa: E501
        :type: str
        """

        self._client_token = client_token

    @property
    def description(self):
        """Gets the description of this AllocateEipAddressRequest.  # noqa: E501


        :return: The description of this AllocateEipAddressRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AllocateEipAddressRequest.


        :param description: The description of this AllocateEipAddressRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                description is not None and len(description) > 255):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                description is not None and len(description) < 1):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `1`")  # noqa: E501

        self._description = description

    @property
    def isp(self):
        """Gets the isp of this AllocateEipAddressRequest.  # noqa: E501


        :return: The isp of this AllocateEipAddressRequest.  # noqa: E501
        :rtype: str
        """
        return self._isp

    @isp.setter
    def isp(self, isp):
        """Sets the isp of this AllocateEipAddressRequest.


        :param isp: The isp of this AllocateEipAddressRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["BGP", "SingleLine_BGP", "Static_BGP", "Fusion_BGP", "ChinaMobile", "ChinaUnicom", "ChinaTelecom", "ChinaMobile_Value", "ChinaUnicom_Value", "ChinaTelecom_Value"]  # noqa: E501
        if (self._configuration.client_side_validation and
                isp not in allowed_values):
            raise ValueError(
                "Invalid value for `isp` ({0}), must be one of {1}"  # noqa: E501
                .format(isp, allowed_values)
            )

        self._isp = isp

    @property
    def ip_address(self):
        """Gets the ip_address of this AllocateEipAddressRequest.  # noqa: E501


        :return: The ip_address of this AllocateEipAddressRequest.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this AllocateEipAddressRequest.


        :param ip_address: The ip_address of this AllocateEipAddressRequest.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

    @property
    def ip_address_pool_id(self):
        """Gets the ip_address_pool_id of this AllocateEipAddressRequest.  # noqa: E501


        :return: The ip_address_pool_id of this AllocateEipAddressRequest.  # noqa: E501
        :rtype: str
        """
        return self._ip_address_pool_id

    @ip_address_pool_id.setter
    def ip_address_pool_id(self, ip_address_pool_id):
        """Sets the ip_address_pool_id of this AllocateEipAddressRequest.


        :param ip_address_pool_id: The ip_address_pool_id of this AllocateEipAddressRequest.  # noqa: E501
        :type: str
        """

        self._ip_address_pool_id = ip_address_pool_id

    @property
    def name(self):
        """Gets the name of this AllocateEipAddressRequest.  # noqa: E501


        :return: The name of this AllocateEipAddressRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AllocateEipAddressRequest.


        :param name: The name of this AllocateEipAddressRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                name is not None and len(name) > 128):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `128`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def period(self):
        """Gets the period of this AllocateEipAddressRequest.  # noqa: E501


        :return: The period of this AllocateEipAddressRequest.  # noqa: E501
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this AllocateEipAddressRequest.


        :param period: The period of this AllocateEipAddressRequest.  # noqa: E501
        :type: int
        """

        self._period = period

    @property
    def period_unit(self):
        """Gets the period_unit of this AllocateEipAddressRequest.  # noqa: E501


        :return: The period_unit of this AllocateEipAddressRequest.  # noqa: E501
        :rtype: int
        """
        return self._period_unit

    @period_unit.setter
    def period_unit(self, period_unit):
        """Sets the period_unit of this AllocateEipAddressRequest.


        :param period_unit: The period_unit of this AllocateEipAddressRequest.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                period_unit is not None and period_unit > 2):  # noqa: E501
            raise ValueError("Invalid value for `period_unit`, must be a value less than or equal to `2`")  # noqa: E501
        if (self._configuration.client_side_validation and
                period_unit is not None and period_unit < 1):  # noqa: E501
            raise ValueError("Invalid value for `period_unit`, must be a value greater than or equal to `1`")  # noqa: E501

        self._period_unit = period_unit

    @property
    def project_name(self):
        """Gets the project_name of this AllocateEipAddressRequest.  # noqa: E501


        :return: The project_name of this AllocateEipAddressRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this AllocateEipAddressRequest.


        :param project_name: The project_name of this AllocateEipAddressRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def renew_period_times(self):
        """Gets the renew_period_times of this AllocateEipAddressRequest.  # noqa: E501


        :return: The renew_period_times of this AllocateEipAddressRequest.  # noqa: E501
        :rtype: int
        """
        return self._renew_period_times

    @renew_period_times.setter
    def renew_period_times(self, renew_period_times):
        """Sets the renew_period_times of this AllocateEipAddressRequest.


        :param renew_period_times: The renew_period_times of this AllocateEipAddressRequest.  # noqa: E501
        :type: int
        """

        self._renew_period_times = renew_period_times

    @property
    def renew_type(self):
        """Gets the renew_type of this AllocateEipAddressRequest.  # noqa: E501


        :return: The renew_type of this AllocateEipAddressRequest.  # noqa: E501
        :rtype: int
        """
        return self._renew_type

    @renew_type.setter
    def renew_type(self, renew_type):
        """Sets the renew_type of this AllocateEipAddressRequest.


        :param renew_type: The renew_type of this AllocateEipAddressRequest.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                renew_type is not None and renew_type > 3):  # noqa: E501
            raise ValueError("Invalid value for `renew_type`, must be a value less than or equal to `3`")  # noqa: E501
        if (self._configuration.client_side_validation and
                renew_type is not None and renew_type < 1):  # noqa: E501
            raise ValueError("Invalid value for `renew_type`, must be a value greater than or equal to `1`")  # noqa: E501

        self._renew_type = renew_type

    @property
    def security_protection_instance_id(self):
        """Gets the security_protection_instance_id of this AllocateEipAddressRequest.  # noqa: E501


        :return: The security_protection_instance_id of this AllocateEipAddressRequest.  # noqa: E501
        :rtype: int
        """
        return self._security_protection_instance_id

    @security_protection_instance_id.setter
    def security_protection_instance_id(self, security_protection_instance_id):
        """Sets the security_protection_instance_id of this AllocateEipAddressRequest.


        :param security_protection_instance_id: The security_protection_instance_id of this AllocateEipAddressRequest.  # noqa: E501
        :type: int
        """

        self._security_protection_instance_id = security_protection_instance_id

    @property
    def security_protection_types(self):
        """Gets the security_protection_types of this AllocateEipAddressRequest.  # noqa: E501


        :return: The security_protection_types of this AllocateEipAddressRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._security_protection_types

    @security_protection_types.setter
    def security_protection_types(self, security_protection_types):
        """Sets the security_protection_types of this AllocateEipAddressRequest.


        :param security_protection_types: The security_protection_types of this AllocateEipAddressRequest.  # noqa: E501
        :type: list[str]
        """

        self._security_protection_types = security_protection_types

    @property
    def tags(self):
        """Gets the tags of this AllocateEipAddressRequest.  # noqa: E501


        :return: The tags of this AllocateEipAddressRequest.  # noqa: E501
        :rtype: list[TagForAllocateEipAddressInput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this AllocateEipAddressRequest.


        :param tags: The tags of this AllocateEipAddressRequest.  # noqa: E501
        :type: list[TagForAllocateEipAddressInput]
        """

        self._tags = tags

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
        if issubclass(AllocateEipAddressRequest, dict):
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
        if not isinstance(other, AllocateEipAddressRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AllocateEipAddressRequest):
            return True

        return self.to_dict() != other.to_dict()
