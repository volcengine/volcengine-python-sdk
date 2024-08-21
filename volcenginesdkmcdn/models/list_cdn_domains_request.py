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


class ListCdnDomainsRequest(object):
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
        'biz_node_ids': 'list[str]',
        'cdn_type': 'list[str]',
        'cloud_account_id': 'str',
        'exact_name': 'str',
        'name': 'str',
        'pagination': 'PaginationForListCdnDomainsInput',
        'region': 'list[str]',
        'schedule_created': 'bool',
        'sort_by': 'str',
        'sort_order': 'str',
        'status': 'list[str]',
        'tag_filters': 'list[TagFilterForListCdnDomainsInput]',
        'vendor': 'list[str]'
    }

    attribute_map = {
        'biz_node_ids': 'BizNodeIds',
        'cdn_type': 'CdnType',
        'cloud_account_id': 'CloudAccountId',
        'exact_name': 'ExactName',
        'name': 'Name',
        'pagination': 'Pagination',
        'region': 'Region',
        'schedule_created': 'ScheduleCreated',
        'sort_by': 'SortBy',
        'sort_order': 'SortOrder',
        'status': 'Status',
        'tag_filters': 'TagFilters',
        'vendor': 'Vendor'
    }

    def __init__(self, biz_node_ids=None, cdn_type=None, cloud_account_id=None, exact_name=None, name=None, pagination=None, region=None, schedule_created=None, sort_by=None, sort_order=None, status=None, tag_filters=None, vendor=None, _configuration=None):  # noqa: E501
        """ListCdnDomainsRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._biz_node_ids = None
        self._cdn_type = None
        self._cloud_account_id = None
        self._exact_name = None
        self._name = None
        self._pagination = None
        self._region = None
        self._schedule_created = None
        self._sort_by = None
        self._sort_order = None
        self._status = None
        self._tag_filters = None
        self._vendor = None
        self.discriminator = None

        if biz_node_ids is not None:
            self.biz_node_ids = biz_node_ids
        if cdn_type is not None:
            self.cdn_type = cdn_type
        if cloud_account_id is not None:
            self.cloud_account_id = cloud_account_id
        if exact_name is not None:
            self.exact_name = exact_name
        if name is not None:
            self.name = name
        if pagination is not None:
            self.pagination = pagination
        if region is not None:
            self.region = region
        if schedule_created is not None:
            self.schedule_created = schedule_created
        if sort_by is not None:
            self.sort_by = sort_by
        if sort_order is not None:
            self.sort_order = sort_order
        if status is not None:
            self.status = status
        if tag_filters is not None:
            self.tag_filters = tag_filters
        if vendor is not None:
            self.vendor = vendor

    @property
    def biz_node_ids(self):
        """Gets the biz_node_ids of this ListCdnDomainsRequest.  # noqa: E501


        :return: The biz_node_ids of this ListCdnDomainsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._biz_node_ids

    @biz_node_ids.setter
    def biz_node_ids(self, biz_node_ids):
        """Sets the biz_node_ids of this ListCdnDomainsRequest.


        :param biz_node_ids: The biz_node_ids of this ListCdnDomainsRequest.  # noqa: E501
        :type: list[str]
        """

        self._biz_node_ids = biz_node_ids

    @property
    def cdn_type(self):
        """Gets the cdn_type of this ListCdnDomainsRequest.  # noqa: E501


        :return: The cdn_type of this ListCdnDomainsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._cdn_type

    @cdn_type.setter
    def cdn_type(self, cdn_type):
        """Sets the cdn_type of this ListCdnDomainsRequest.


        :param cdn_type: The cdn_type of this ListCdnDomainsRequest.  # noqa: E501
        :type: list[str]
        """

        self._cdn_type = cdn_type

    @property
    def cloud_account_id(self):
        """Gets the cloud_account_id of this ListCdnDomainsRequest.  # noqa: E501


        :return: The cloud_account_id of this ListCdnDomainsRequest.  # noqa: E501
        :rtype: str
        """
        return self._cloud_account_id

    @cloud_account_id.setter
    def cloud_account_id(self, cloud_account_id):
        """Sets the cloud_account_id of this ListCdnDomainsRequest.


        :param cloud_account_id: The cloud_account_id of this ListCdnDomainsRequest.  # noqa: E501
        :type: str
        """

        self._cloud_account_id = cloud_account_id

    @property
    def exact_name(self):
        """Gets the exact_name of this ListCdnDomainsRequest.  # noqa: E501


        :return: The exact_name of this ListCdnDomainsRequest.  # noqa: E501
        :rtype: str
        """
        return self._exact_name

    @exact_name.setter
    def exact_name(self, exact_name):
        """Sets the exact_name of this ListCdnDomainsRequest.


        :param exact_name: The exact_name of this ListCdnDomainsRequest.  # noqa: E501
        :type: str
        """

        self._exact_name = exact_name

    @property
    def name(self):
        """Gets the name of this ListCdnDomainsRequest.  # noqa: E501


        :return: The name of this ListCdnDomainsRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListCdnDomainsRequest.


        :param name: The name of this ListCdnDomainsRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def pagination(self):
        """Gets the pagination of this ListCdnDomainsRequest.  # noqa: E501


        :return: The pagination of this ListCdnDomainsRequest.  # noqa: E501
        :rtype: PaginationForListCdnDomainsInput
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this ListCdnDomainsRequest.


        :param pagination: The pagination of this ListCdnDomainsRequest.  # noqa: E501
        :type: PaginationForListCdnDomainsInput
        """

        self._pagination = pagination

    @property
    def region(self):
        """Gets the region of this ListCdnDomainsRequest.  # noqa: E501


        :return: The region of this ListCdnDomainsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ListCdnDomainsRequest.


        :param region: The region of this ListCdnDomainsRequest.  # noqa: E501
        :type: list[str]
        """

        self._region = region

    @property
    def schedule_created(self):
        """Gets the schedule_created of this ListCdnDomainsRequest.  # noqa: E501


        :return: The schedule_created of this ListCdnDomainsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._schedule_created

    @schedule_created.setter
    def schedule_created(self, schedule_created):
        """Sets the schedule_created of this ListCdnDomainsRequest.


        :param schedule_created: The schedule_created of this ListCdnDomainsRequest.  # noqa: E501
        :type: bool
        """

        self._schedule_created = schedule_created

    @property
    def sort_by(self):
        """Gets the sort_by of this ListCdnDomainsRequest.  # noqa: E501


        :return: The sort_by of this ListCdnDomainsRequest.  # noqa: E501
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        """Sets the sort_by of this ListCdnDomainsRequest.


        :param sort_by: The sort_by of this ListCdnDomainsRequest.  # noqa: E501
        :type: str
        """

        self._sort_by = sort_by

    @property
    def sort_order(self):
        """Gets the sort_order of this ListCdnDomainsRequest.  # noqa: E501


        :return: The sort_order of this ListCdnDomainsRequest.  # noqa: E501
        :rtype: str
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this ListCdnDomainsRequest.


        :param sort_order: The sort_order of this ListCdnDomainsRequest.  # noqa: E501
        :type: str
        """

        self._sort_order = sort_order

    @property
    def status(self):
        """Gets the status of this ListCdnDomainsRequest.  # noqa: E501


        :return: The status of this ListCdnDomainsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListCdnDomainsRequest.


        :param status: The status of this ListCdnDomainsRequest.  # noqa: E501
        :type: list[str]
        """

        self._status = status

    @property
    def tag_filters(self):
        """Gets the tag_filters of this ListCdnDomainsRequest.  # noqa: E501


        :return: The tag_filters of this ListCdnDomainsRequest.  # noqa: E501
        :rtype: list[TagFilterForListCdnDomainsInput]
        """
        return self._tag_filters

    @tag_filters.setter
    def tag_filters(self, tag_filters):
        """Sets the tag_filters of this ListCdnDomainsRequest.


        :param tag_filters: The tag_filters of this ListCdnDomainsRequest.  # noqa: E501
        :type: list[TagFilterForListCdnDomainsInput]
        """

        self._tag_filters = tag_filters

    @property
    def vendor(self):
        """Gets the vendor of this ListCdnDomainsRequest.  # noqa: E501


        :return: The vendor of this ListCdnDomainsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this ListCdnDomainsRequest.


        :param vendor: The vendor of this ListCdnDomainsRequest.  # noqa: E501
        :type: list[str]
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
        if issubclass(ListCdnDomainsRequest, dict):
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
        if not isinstance(other, ListCdnDomainsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListCdnDomainsRequest):
            return True

        return self.to_dict() != other.to_dict()
