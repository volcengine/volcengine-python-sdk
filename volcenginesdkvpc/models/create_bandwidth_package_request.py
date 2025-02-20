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


class CreateBandwidthPackageRequest(object):
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
        'bandwidth_package_name': 'str',
        'billing_type': 'int',
        'description': 'str',
        'isp': 'str',
        'period': 'int',
        'period_unit': 'int',
        'project_name': 'str',
        'protocol': 'str',
        'security_protection_types': 'list[str]',
        'tags': 'list[TagForCreateBandwidthPackageInput]'
    }

    attribute_map = {
        'bandwidth': 'Bandwidth',
        'bandwidth_package_name': 'BandwidthPackageName',
        'billing_type': 'BillingType',
        'description': 'Description',
        'isp': 'ISP',
        'period': 'Period',
        'period_unit': 'PeriodUnit',
        'project_name': 'ProjectName',
        'protocol': 'Protocol',
        'security_protection_types': 'SecurityProtectionTypes',
        'tags': 'Tags'
    }

    def __init__(self, bandwidth=None, bandwidth_package_name=None, billing_type=None, description=None, isp=None, period=None, period_unit=None, project_name=None, protocol=None, security_protection_types=None, tags=None, _configuration=None):  # noqa: E501
        """CreateBandwidthPackageRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bandwidth = None
        self._bandwidth_package_name = None
        self._billing_type = None
        self._description = None
        self._isp = None
        self._period = None
        self._period_unit = None
        self._project_name = None
        self._protocol = None
        self._security_protection_types = None
        self._tags = None
        self.discriminator = None

        self.bandwidth = bandwidth
        if bandwidth_package_name is not None:
            self.bandwidth_package_name = bandwidth_package_name
        if billing_type is not None:
            self.billing_type = billing_type
        if description is not None:
            self.description = description
        if isp is not None:
            self.isp = isp
        if period is not None:
            self.period = period
        if period_unit is not None:
            self.period_unit = period_unit
        if project_name is not None:
            self.project_name = project_name
        if protocol is not None:
            self.protocol = protocol
        if security_protection_types is not None:
            self.security_protection_types = security_protection_types
        if tags is not None:
            self.tags = tags

    @property
    def bandwidth(self):
        """Gets the bandwidth of this CreateBandwidthPackageRequest.  # noqa: E501


        :return: The bandwidth of this CreateBandwidthPackageRequest.  # noqa: E501
        :rtype: int
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this CreateBandwidthPackageRequest.


        :param bandwidth: The bandwidth of this CreateBandwidthPackageRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and bandwidth is None:
            raise ValueError("Invalid value for `bandwidth`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                bandwidth is not None and bandwidth < 2):  # noqa: E501
            raise ValueError("Invalid value for `bandwidth`, must be a value greater than or equal to `2`")  # noqa: E501

        self._bandwidth = bandwidth

    @property
    def bandwidth_package_name(self):
        """Gets the bandwidth_package_name of this CreateBandwidthPackageRequest.  # noqa: E501


        :return: The bandwidth_package_name of this CreateBandwidthPackageRequest.  # noqa: E501
        :rtype: str
        """
        return self._bandwidth_package_name

    @bandwidth_package_name.setter
    def bandwidth_package_name(self, bandwidth_package_name):
        """Sets the bandwidth_package_name of this CreateBandwidthPackageRequest.


        :param bandwidth_package_name: The bandwidth_package_name of this CreateBandwidthPackageRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                bandwidth_package_name is not None and len(bandwidth_package_name) > 128):
            raise ValueError("Invalid value for `bandwidth_package_name`, length must be less than or equal to `128`")  # noqa: E501
        if (self._configuration.client_side_validation and
                bandwidth_package_name is not None and len(bandwidth_package_name) < 1):
            raise ValueError("Invalid value for `bandwidth_package_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._bandwidth_package_name = bandwidth_package_name

    @property
    def billing_type(self):
        """Gets the billing_type of this CreateBandwidthPackageRequest.  # noqa: E501


        :return: The billing_type of this CreateBandwidthPackageRequest.  # noqa: E501
        :rtype: int
        """
        return self._billing_type

    @billing_type.setter
    def billing_type(self, billing_type):
        """Sets the billing_type of this CreateBandwidthPackageRequest.


        :param billing_type: The billing_type of this CreateBandwidthPackageRequest.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                billing_type is not None and billing_type > 4):  # noqa: E501
            raise ValueError("Invalid value for `billing_type`, must be a value less than or equal to `4`")  # noqa: E501
        if (self._configuration.client_side_validation and
                billing_type is not None and billing_type < 1):  # noqa: E501
            raise ValueError("Invalid value for `billing_type`, must be a value greater than or equal to `1`")  # noqa: E501

        self._billing_type = billing_type

    @property
    def description(self):
        """Gets the description of this CreateBandwidthPackageRequest.  # noqa: E501


        :return: The description of this CreateBandwidthPackageRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateBandwidthPackageRequest.


        :param description: The description of this CreateBandwidthPackageRequest.  # noqa: E501
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
        """Gets the isp of this CreateBandwidthPackageRequest.  # noqa: E501


        :return: The isp of this CreateBandwidthPackageRequest.  # noqa: E501
        :rtype: str
        """
        return self._isp

    @isp.setter
    def isp(self, isp):
        """Sets the isp of this CreateBandwidthPackageRequest.


        :param isp: The isp of this CreateBandwidthPackageRequest.  # noqa: E501
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
    def period(self):
        """Gets the period of this CreateBandwidthPackageRequest.  # noqa: E501


        :return: The period of this CreateBandwidthPackageRequest.  # noqa: E501
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this CreateBandwidthPackageRequest.


        :param period: The period of this CreateBandwidthPackageRequest.  # noqa: E501
        :type: int
        """

        self._period = period

    @property
    def period_unit(self):
        """Gets the period_unit of this CreateBandwidthPackageRequest.  # noqa: E501


        :return: The period_unit of this CreateBandwidthPackageRequest.  # noqa: E501
        :rtype: int
        """
        return self._period_unit

    @period_unit.setter
    def period_unit(self, period_unit):
        """Sets the period_unit of this CreateBandwidthPackageRequest.


        :param period_unit: The period_unit of this CreateBandwidthPackageRequest.  # noqa: E501
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
        """Gets the project_name of this CreateBandwidthPackageRequest.  # noqa: E501


        :return: The project_name of this CreateBandwidthPackageRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this CreateBandwidthPackageRequest.


        :param project_name: The project_name of this CreateBandwidthPackageRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def protocol(self):
        """Gets the protocol of this CreateBandwidthPackageRequest.  # noqa: E501


        :return: The protocol of this CreateBandwidthPackageRequest.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this CreateBandwidthPackageRequest.


        :param protocol: The protocol of this CreateBandwidthPackageRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["IPv4", "Dual-stack", "IPv6"]  # noqa: E501
        if (self._configuration.client_side_validation and
                protocol not in allowed_values):
            raise ValueError(
                "Invalid value for `protocol` ({0}), must be one of {1}"  # noqa: E501
                .format(protocol, allowed_values)
            )

        self._protocol = protocol

    @property
    def security_protection_types(self):
        """Gets the security_protection_types of this CreateBandwidthPackageRequest.  # noqa: E501


        :return: The security_protection_types of this CreateBandwidthPackageRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._security_protection_types

    @security_protection_types.setter
    def security_protection_types(self, security_protection_types):
        """Sets the security_protection_types of this CreateBandwidthPackageRequest.


        :param security_protection_types: The security_protection_types of this CreateBandwidthPackageRequest.  # noqa: E501
        :type: list[str]
        """

        self._security_protection_types = security_protection_types

    @property
    def tags(self):
        """Gets the tags of this CreateBandwidthPackageRequest.  # noqa: E501


        :return: The tags of this CreateBandwidthPackageRequest.  # noqa: E501
        :rtype: list[TagForCreateBandwidthPackageInput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateBandwidthPackageRequest.


        :param tags: The tags of this CreateBandwidthPackageRequest.  # noqa: E501
        :type: list[TagForCreateBandwidthPackageInput]
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
        if issubclass(CreateBandwidthPackageRequest, dict):
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
        if not isinstance(other, CreateBandwidthPackageRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateBandwidthPackageRequest):
            return True

        return self.to_dict() != other.to_dict()
