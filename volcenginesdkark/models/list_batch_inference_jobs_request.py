# coding: utf-8

"""
    ark

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ListBatchInferenceJobsRequest(object):
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
        'filter': 'FilterForListBatchInferenceJobsInput',
        'page_number': 'int',
        'page_size': 'int',
        'project_name': 'str',
        'sort_by': 'str',
        'sort_order': 'str',
        'tag_filters': 'list[TagFilterForListBatchInferenceJobsInput]'
    }

    attribute_map = {
        'filter': 'Filter',
        'page_number': 'PageNumber',
        'page_size': 'PageSize',
        'project_name': 'ProjectName',
        'sort_by': 'SortBy',
        'sort_order': 'SortOrder',
        'tag_filters': 'TagFilters'
    }

    def __init__(self, filter=None, page_number=None, page_size=None, project_name=None, sort_by=None, sort_order=None, tag_filters=None, _configuration=None):  # noqa: E501
        """ListBatchInferenceJobsRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._filter = None
        self._page_number = None
        self._page_size = None
        self._project_name = None
        self._sort_by = None
        self._sort_order = None
        self._tag_filters = None
        self.discriminator = None

        if filter is not None:
            self.filter = filter
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if project_name is not None:
            self.project_name = project_name
        if sort_by is not None:
            self.sort_by = sort_by
        if sort_order is not None:
            self.sort_order = sort_order
        if tag_filters is not None:
            self.tag_filters = tag_filters

    @property
    def filter(self):
        """Gets the filter of this ListBatchInferenceJobsRequest.  # noqa: E501


        :return: The filter of this ListBatchInferenceJobsRequest.  # noqa: E501
        :rtype: FilterForListBatchInferenceJobsInput
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this ListBatchInferenceJobsRequest.


        :param filter: The filter of this ListBatchInferenceJobsRequest.  # noqa: E501
        :type: FilterForListBatchInferenceJobsInput
        """

        self._filter = filter

    @property
    def page_number(self):
        """Gets the page_number of this ListBatchInferenceJobsRequest.  # noqa: E501


        :return: The page_number of this ListBatchInferenceJobsRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this ListBatchInferenceJobsRequest.


        :param page_number: The page_number of this ListBatchInferenceJobsRequest.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this ListBatchInferenceJobsRequest.  # noqa: E501


        :return: The page_size of this ListBatchInferenceJobsRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ListBatchInferenceJobsRequest.


        :param page_size: The page_size of this ListBatchInferenceJobsRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def project_name(self):
        """Gets the project_name of this ListBatchInferenceJobsRequest.  # noqa: E501


        :return: The project_name of this ListBatchInferenceJobsRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this ListBatchInferenceJobsRequest.


        :param project_name: The project_name of this ListBatchInferenceJobsRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def sort_by(self):
        """Gets the sort_by of this ListBatchInferenceJobsRequest.  # noqa: E501


        :return: The sort_by of this ListBatchInferenceJobsRequest.  # noqa: E501
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        """Sets the sort_by of this ListBatchInferenceJobsRequest.


        :param sort_by: The sort_by of this ListBatchInferenceJobsRequest.  # noqa: E501
        :type: str
        """

        self._sort_by = sort_by

    @property
    def sort_order(self):
        """Gets the sort_order of this ListBatchInferenceJobsRequest.  # noqa: E501


        :return: The sort_order of this ListBatchInferenceJobsRequest.  # noqa: E501
        :rtype: str
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this ListBatchInferenceJobsRequest.


        :param sort_order: The sort_order of this ListBatchInferenceJobsRequest.  # noqa: E501
        :type: str
        """

        self._sort_order = sort_order

    @property
    def tag_filters(self):
        """Gets the tag_filters of this ListBatchInferenceJobsRequest.  # noqa: E501


        :return: The tag_filters of this ListBatchInferenceJobsRequest.  # noqa: E501
        :rtype: list[TagFilterForListBatchInferenceJobsInput]
        """
        return self._tag_filters

    @tag_filters.setter
    def tag_filters(self, tag_filters):
        """Sets the tag_filters of this ListBatchInferenceJobsRequest.


        :param tag_filters: The tag_filters of this ListBatchInferenceJobsRequest.  # noqa: E501
        :type: list[TagFilterForListBatchInferenceJobsInput]
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
        if issubclass(ListBatchInferenceJobsRequest, dict):
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
        if not isinstance(other, ListBatchInferenceJobsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListBatchInferenceJobsRequest):
            return True

        return self.to_dict() != other.to_dict()
