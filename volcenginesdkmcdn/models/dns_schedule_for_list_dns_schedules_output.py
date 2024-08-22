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


class DnsScheduleForListDnsSchedulesOutput(object):
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
        'cloud_account_ids': 'list[str]',
        'created_at': 'int',
        'domain_name': 'str',
        'id': 'str',
        'region': 'str',
        'schedule_cname': 'str',
        'schedule_status': 'str',
        'schedule_strategies': 'list[str]',
        'updated_at': 'int'
    }

    attribute_map = {
        'cloud_account_ids': 'CloudAccountIds',
        'created_at': 'CreatedAt',
        'domain_name': 'DomainName',
        'id': 'Id',
        'region': 'Region',
        'schedule_cname': 'ScheduleCname',
        'schedule_status': 'ScheduleStatus',
        'schedule_strategies': 'ScheduleStrategies',
        'updated_at': 'UpdatedAt'
    }

    def __init__(self, cloud_account_ids=None, created_at=None, domain_name=None, id=None, region=None, schedule_cname=None, schedule_status=None, schedule_strategies=None, updated_at=None, _configuration=None):  # noqa: E501
        """DnsScheduleForListDnsSchedulesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cloud_account_ids = None
        self._created_at = None
        self._domain_name = None
        self._id = None
        self._region = None
        self._schedule_cname = None
        self._schedule_status = None
        self._schedule_strategies = None
        self._updated_at = None
        self.discriminator = None

        if cloud_account_ids is not None:
            self.cloud_account_ids = cloud_account_ids
        if created_at is not None:
            self.created_at = created_at
        if domain_name is not None:
            self.domain_name = domain_name
        if id is not None:
            self.id = id
        if region is not None:
            self.region = region
        if schedule_cname is not None:
            self.schedule_cname = schedule_cname
        if schedule_status is not None:
            self.schedule_status = schedule_status
        if schedule_strategies is not None:
            self.schedule_strategies = schedule_strategies
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def cloud_account_ids(self):
        """Gets the cloud_account_ids of this DnsScheduleForListDnsSchedulesOutput.  # noqa: E501


        :return: The cloud_account_ids of this DnsScheduleForListDnsSchedulesOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._cloud_account_ids

    @cloud_account_ids.setter
    def cloud_account_ids(self, cloud_account_ids):
        """Sets the cloud_account_ids of this DnsScheduleForListDnsSchedulesOutput.


        :param cloud_account_ids: The cloud_account_ids of this DnsScheduleForListDnsSchedulesOutput.  # noqa: E501
        :type: list[str]
        """

        self._cloud_account_ids = cloud_account_ids

    @property
    def created_at(self):
        """Gets the created_at of this DnsScheduleForListDnsSchedulesOutput.  # noqa: E501


        :return: The created_at of this DnsScheduleForListDnsSchedulesOutput.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this DnsScheduleForListDnsSchedulesOutput.


        :param created_at: The created_at of this DnsScheduleForListDnsSchedulesOutput.  # noqa: E501
        :type: int
        """

        self._created_at = created_at

    @property
    def domain_name(self):
        """Gets the domain_name of this DnsScheduleForListDnsSchedulesOutput.  # noqa: E501


        :return: The domain_name of this DnsScheduleForListDnsSchedulesOutput.  # noqa: E501
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this DnsScheduleForListDnsSchedulesOutput.


        :param domain_name: The domain_name of this DnsScheduleForListDnsSchedulesOutput.  # noqa: E501
        :type: str
        """

        self._domain_name = domain_name

    @property
    def id(self):
        """Gets the id of this DnsScheduleForListDnsSchedulesOutput.  # noqa: E501


        :return: The id of this DnsScheduleForListDnsSchedulesOutput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DnsScheduleForListDnsSchedulesOutput.


        :param id: The id of this DnsScheduleForListDnsSchedulesOutput.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def region(self):
        """Gets the region of this DnsScheduleForListDnsSchedulesOutput.  # noqa: E501


        :return: The region of this DnsScheduleForListDnsSchedulesOutput.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this DnsScheduleForListDnsSchedulesOutput.


        :param region: The region of this DnsScheduleForListDnsSchedulesOutput.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def schedule_cname(self):
        """Gets the schedule_cname of this DnsScheduleForListDnsSchedulesOutput.  # noqa: E501


        :return: The schedule_cname of this DnsScheduleForListDnsSchedulesOutput.  # noqa: E501
        :rtype: str
        """
        return self._schedule_cname

    @schedule_cname.setter
    def schedule_cname(self, schedule_cname):
        """Sets the schedule_cname of this DnsScheduleForListDnsSchedulesOutput.


        :param schedule_cname: The schedule_cname of this DnsScheduleForListDnsSchedulesOutput.  # noqa: E501
        :type: str
        """

        self._schedule_cname = schedule_cname

    @property
    def schedule_status(self):
        """Gets the schedule_status of this DnsScheduleForListDnsSchedulesOutput.  # noqa: E501


        :return: The schedule_status of this DnsScheduleForListDnsSchedulesOutput.  # noqa: E501
        :rtype: str
        """
        return self._schedule_status

    @schedule_status.setter
    def schedule_status(self, schedule_status):
        """Sets the schedule_status of this DnsScheduleForListDnsSchedulesOutput.


        :param schedule_status: The schedule_status of this DnsScheduleForListDnsSchedulesOutput.  # noqa: E501
        :type: str
        """

        self._schedule_status = schedule_status

    @property
    def schedule_strategies(self):
        """Gets the schedule_strategies of this DnsScheduleForListDnsSchedulesOutput.  # noqa: E501


        :return: The schedule_strategies of this DnsScheduleForListDnsSchedulesOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._schedule_strategies

    @schedule_strategies.setter
    def schedule_strategies(self, schedule_strategies):
        """Sets the schedule_strategies of this DnsScheduleForListDnsSchedulesOutput.


        :param schedule_strategies: The schedule_strategies of this DnsScheduleForListDnsSchedulesOutput.  # noqa: E501
        :type: list[str]
        """

        self._schedule_strategies = schedule_strategies

    @property
    def updated_at(self):
        """Gets the updated_at of this DnsScheduleForListDnsSchedulesOutput.  # noqa: E501


        :return: The updated_at of this DnsScheduleForListDnsSchedulesOutput.  # noqa: E501
        :rtype: int
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this DnsScheduleForListDnsSchedulesOutput.


        :param updated_at: The updated_at of this DnsScheduleForListDnsSchedulesOutput.  # noqa: E501
        :type: int
        """

        self._updated_at = updated_at

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
        if issubclass(DnsScheduleForListDnsSchedulesOutput, dict):
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
        if not isinstance(other, DnsScheduleForListDnsSchedulesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DnsScheduleForListDnsSchedulesOutput):
            return True

        return self.to_dict() != other.to_dict()