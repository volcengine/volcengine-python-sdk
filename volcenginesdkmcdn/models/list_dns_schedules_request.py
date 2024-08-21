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


class ListDnsSchedulesRequest(object):
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
        'domain_name': 'str',
        'exact_domain_name': 'str',
        'pagination': 'PaginationForListDnsSchedulesInput',
        'region': 'str',
        'schedule_status': 'str',
        'schedule_strategy': 'str',
        'sort_by': 'str',
        'sort_order': 'str'
    }

    attribute_map = {
        'cloud_account_ids': 'CloudAccountIds',
        'domain_name': 'DomainName',
        'exact_domain_name': 'ExactDomainName',
        'pagination': 'Pagination',
        'region': 'Region',
        'schedule_status': 'ScheduleStatus',
        'schedule_strategy': 'ScheduleStrategy',
        'sort_by': 'SortBy',
        'sort_order': 'SortOrder'
    }

    def __init__(self, cloud_account_ids=None, domain_name=None, exact_domain_name=None, pagination=None, region=None, schedule_status=None, schedule_strategy=None, sort_by=None, sort_order=None, _configuration=None):  # noqa: E501
        """ListDnsSchedulesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cloud_account_ids = None
        self._domain_name = None
        self._exact_domain_name = None
        self._pagination = None
        self._region = None
        self._schedule_status = None
        self._schedule_strategy = None
        self._sort_by = None
        self._sort_order = None
        self.discriminator = None

        if cloud_account_ids is not None:
            self.cloud_account_ids = cloud_account_ids
        if domain_name is not None:
            self.domain_name = domain_name
        if exact_domain_name is not None:
            self.exact_domain_name = exact_domain_name
        if pagination is not None:
            self.pagination = pagination
        if region is not None:
            self.region = region
        if schedule_status is not None:
            self.schedule_status = schedule_status
        if schedule_strategy is not None:
            self.schedule_strategy = schedule_strategy
        if sort_by is not None:
            self.sort_by = sort_by
        if sort_order is not None:
            self.sort_order = sort_order

    @property
    def cloud_account_ids(self):
        """Gets the cloud_account_ids of this ListDnsSchedulesRequest.  # noqa: E501


        :return: The cloud_account_ids of this ListDnsSchedulesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._cloud_account_ids

    @cloud_account_ids.setter
    def cloud_account_ids(self, cloud_account_ids):
        """Sets the cloud_account_ids of this ListDnsSchedulesRequest.


        :param cloud_account_ids: The cloud_account_ids of this ListDnsSchedulesRequest.  # noqa: E501
        :type: list[str]
        """

        self._cloud_account_ids = cloud_account_ids

    @property
    def domain_name(self):
        """Gets the domain_name of this ListDnsSchedulesRequest.  # noqa: E501


        :return: The domain_name of this ListDnsSchedulesRequest.  # noqa: E501
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this ListDnsSchedulesRequest.


        :param domain_name: The domain_name of this ListDnsSchedulesRequest.  # noqa: E501
        :type: str
        """

        self._domain_name = domain_name

    @property
    def exact_domain_name(self):
        """Gets the exact_domain_name of this ListDnsSchedulesRequest.  # noqa: E501


        :return: The exact_domain_name of this ListDnsSchedulesRequest.  # noqa: E501
        :rtype: str
        """
        return self._exact_domain_name

    @exact_domain_name.setter
    def exact_domain_name(self, exact_domain_name):
        """Sets the exact_domain_name of this ListDnsSchedulesRequest.


        :param exact_domain_name: The exact_domain_name of this ListDnsSchedulesRequest.  # noqa: E501
        :type: str
        """

        self._exact_domain_name = exact_domain_name

    @property
    def pagination(self):
        """Gets the pagination of this ListDnsSchedulesRequest.  # noqa: E501


        :return: The pagination of this ListDnsSchedulesRequest.  # noqa: E501
        :rtype: PaginationForListDnsSchedulesInput
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this ListDnsSchedulesRequest.


        :param pagination: The pagination of this ListDnsSchedulesRequest.  # noqa: E501
        :type: PaginationForListDnsSchedulesInput
        """

        self._pagination = pagination

    @property
    def region(self):
        """Gets the region of this ListDnsSchedulesRequest.  # noqa: E501


        :return: The region of this ListDnsSchedulesRequest.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ListDnsSchedulesRequest.


        :param region: The region of this ListDnsSchedulesRequest.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def schedule_status(self):
        """Gets the schedule_status of this ListDnsSchedulesRequest.  # noqa: E501


        :return: The schedule_status of this ListDnsSchedulesRequest.  # noqa: E501
        :rtype: str
        """
        return self._schedule_status

    @schedule_status.setter
    def schedule_status(self, schedule_status):
        """Sets the schedule_status of this ListDnsSchedulesRequest.


        :param schedule_status: The schedule_status of this ListDnsSchedulesRequest.  # noqa: E501
        :type: str
        """

        self._schedule_status = schedule_status

    @property
    def schedule_strategy(self):
        """Gets the schedule_strategy of this ListDnsSchedulesRequest.  # noqa: E501


        :return: The schedule_strategy of this ListDnsSchedulesRequest.  # noqa: E501
        :rtype: str
        """
        return self._schedule_strategy

    @schedule_strategy.setter
    def schedule_strategy(self, schedule_strategy):
        """Sets the schedule_strategy of this ListDnsSchedulesRequest.


        :param schedule_strategy: The schedule_strategy of this ListDnsSchedulesRequest.  # noqa: E501
        :type: str
        """

        self._schedule_strategy = schedule_strategy

    @property
    def sort_by(self):
        """Gets the sort_by of this ListDnsSchedulesRequest.  # noqa: E501


        :return: The sort_by of this ListDnsSchedulesRequest.  # noqa: E501
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        """Sets the sort_by of this ListDnsSchedulesRequest.


        :param sort_by: The sort_by of this ListDnsSchedulesRequest.  # noqa: E501
        :type: str
        """

        self._sort_by = sort_by

    @property
    def sort_order(self):
        """Gets the sort_order of this ListDnsSchedulesRequest.  # noqa: E501


        :return: The sort_order of this ListDnsSchedulesRequest.  # noqa: E501
        :rtype: str
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this ListDnsSchedulesRequest.


        :param sort_order: The sort_order of this ListDnsSchedulesRequest.  # noqa: E501
        :type: str
        """

        self._sort_order = sort_order

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
        if issubclass(ListDnsSchedulesRequest, dict):
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
        if not isinstance(other, ListDnsSchedulesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListDnsSchedulesRequest):
            return True

        return self.to_dict() != other.to_dict()
