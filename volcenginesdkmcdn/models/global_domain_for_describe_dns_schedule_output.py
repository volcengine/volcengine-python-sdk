# coding: utf-8

"""
    mcdn

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class GlobalDomainForDescribeDnsScheduleOutput(object):
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
        'cloud_account_id': 'str',
        'cname': 'str',
        'id': 'str',
        'is_enabled': 'bool',
        'name': 'str',
        'region': 'str',
        'status': 'str',
        'sub_product': 'str',
        'vendor': 'str'
    }

    attribute_map = {
        'cloud_account_id': 'CloudAccountId',
        'cname': 'Cname',
        'id': 'Id',
        'is_enabled': 'IsEnabled',
        'name': 'Name',
        'region': 'Region',
        'status': 'Status',
        'sub_product': 'SubProduct',
        'vendor': 'Vendor'
    }

    def __init__(self, cloud_account_id=None, cname=None, id=None, is_enabled=None, name=None, region=None, status=None, sub_product=None, vendor=None, _configuration=None):  # noqa: E501
        """GlobalDomainForDescribeDnsScheduleOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cloud_account_id = None
        self._cname = None
        self._id = None
        self._is_enabled = None
        self._name = None
        self._region = None
        self._status = None
        self._sub_product = None
        self._vendor = None
        self.discriminator = None

        if cloud_account_id is not None:
            self.cloud_account_id = cloud_account_id
        if cname is not None:
            self.cname = cname
        if id is not None:
            self.id = id
        if is_enabled is not None:
            self.is_enabled = is_enabled
        if name is not None:
            self.name = name
        if region is not None:
            self.region = region
        if status is not None:
            self.status = status
        if sub_product is not None:
            self.sub_product = sub_product
        if vendor is not None:
            self.vendor = vendor

    @property
    def cloud_account_id(self):
        """Gets the cloud_account_id of this GlobalDomainForDescribeDnsScheduleOutput.  # noqa: E501


        :return: The cloud_account_id of this GlobalDomainForDescribeDnsScheduleOutput.  # noqa: E501
        :rtype: str
        """
        return self._cloud_account_id

    @cloud_account_id.setter
    def cloud_account_id(self, cloud_account_id):
        """Sets the cloud_account_id of this GlobalDomainForDescribeDnsScheduleOutput.


        :param cloud_account_id: The cloud_account_id of this GlobalDomainForDescribeDnsScheduleOutput.  # noqa: E501
        :type: str
        """

        self._cloud_account_id = cloud_account_id

    @property
    def cname(self):
        """Gets the cname of this GlobalDomainForDescribeDnsScheduleOutput.  # noqa: E501


        :return: The cname of this GlobalDomainForDescribeDnsScheduleOutput.  # noqa: E501
        :rtype: str
        """
        return self._cname

    @cname.setter
    def cname(self, cname):
        """Sets the cname of this GlobalDomainForDescribeDnsScheduleOutput.


        :param cname: The cname of this GlobalDomainForDescribeDnsScheduleOutput.  # noqa: E501
        :type: str
        """

        self._cname = cname

    @property
    def id(self):
        """Gets the id of this GlobalDomainForDescribeDnsScheduleOutput.  # noqa: E501


        :return: The id of this GlobalDomainForDescribeDnsScheduleOutput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GlobalDomainForDescribeDnsScheduleOutput.


        :param id: The id of this GlobalDomainForDescribeDnsScheduleOutput.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def is_enabled(self):
        """Gets the is_enabled of this GlobalDomainForDescribeDnsScheduleOutput.  # noqa: E501


        :return: The is_enabled of this GlobalDomainForDescribeDnsScheduleOutput.  # noqa: E501
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """Sets the is_enabled of this GlobalDomainForDescribeDnsScheduleOutput.


        :param is_enabled: The is_enabled of this GlobalDomainForDescribeDnsScheduleOutput.  # noqa: E501
        :type: bool
        """

        self._is_enabled = is_enabled

    @property
    def name(self):
        """Gets the name of this GlobalDomainForDescribeDnsScheduleOutput.  # noqa: E501


        :return: The name of this GlobalDomainForDescribeDnsScheduleOutput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GlobalDomainForDescribeDnsScheduleOutput.


        :param name: The name of this GlobalDomainForDescribeDnsScheduleOutput.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def region(self):
        """Gets the region of this GlobalDomainForDescribeDnsScheduleOutput.  # noqa: E501


        :return: The region of this GlobalDomainForDescribeDnsScheduleOutput.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this GlobalDomainForDescribeDnsScheduleOutput.


        :param region: The region of this GlobalDomainForDescribeDnsScheduleOutput.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def status(self):
        """Gets the status of this GlobalDomainForDescribeDnsScheduleOutput.  # noqa: E501


        :return: The status of this GlobalDomainForDescribeDnsScheduleOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GlobalDomainForDescribeDnsScheduleOutput.


        :param status: The status of this GlobalDomainForDescribeDnsScheduleOutput.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def sub_product(self):
        """Gets the sub_product of this GlobalDomainForDescribeDnsScheduleOutput.  # noqa: E501


        :return: The sub_product of this GlobalDomainForDescribeDnsScheduleOutput.  # noqa: E501
        :rtype: str
        """
        return self._sub_product

    @sub_product.setter
    def sub_product(self, sub_product):
        """Sets the sub_product of this GlobalDomainForDescribeDnsScheduleOutput.


        :param sub_product: The sub_product of this GlobalDomainForDescribeDnsScheduleOutput.  # noqa: E501
        :type: str
        """

        self._sub_product = sub_product

    @property
    def vendor(self):
        """Gets the vendor of this GlobalDomainForDescribeDnsScheduleOutput.  # noqa: E501


        :return: The vendor of this GlobalDomainForDescribeDnsScheduleOutput.  # noqa: E501
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this GlobalDomainForDescribeDnsScheduleOutput.


        :param vendor: The vendor of this GlobalDomainForDescribeDnsScheduleOutput.  # noqa: E501
        :type: str
        """

        self._vendor = vendor

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
        if issubclass(GlobalDomainForDescribeDnsScheduleOutput, dict):
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
        if not isinstance(other, GlobalDomainForDescribeDnsScheduleOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GlobalDomainForDescribeDnsScheduleOutput):
            return True

        return self.to_dict() != other.to_dict()