# coding: utf-8

"""
    smc

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeMigrationSourcesRequest(object):
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
        'order': 'str',
        'order_by_column': 'str',
        'page_number': 'int',
        'page_size': 'int',
        'project_name': 'str',
        'source_id': 'str',
        'source_name': 'str',
        'source_state': 'str',
        'source_type': 'str',
        'tag_filters': 'list[TagFilterForDescribeMigrationSourcesInput]'
    }

    attribute_map = {
        'order': 'Order',
        'order_by_column': 'OrderByColumn',
        'page_number': 'PageNumber',
        'page_size': 'PageSize',
        'project_name': 'ProjectName',
        'source_id': 'SourceId',
        'source_name': 'SourceName',
        'source_state': 'SourceState',
        'source_type': 'SourceType',
        'tag_filters': 'TagFilters'
    }

    def __init__(self, order=None, order_by_column=None, page_number=None, page_size=None, project_name=None, source_id=None, source_name=None, source_state=None, source_type=None, tag_filters=None, _configuration=None):  # noqa: E501
        """DescribeMigrationSourcesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._order = None
        self._order_by_column = None
        self._page_number = None
        self._page_size = None
        self._project_name = None
        self._source_id = None
        self._source_name = None
        self._source_state = None
        self._source_type = None
        self._tag_filters = None
        self.discriminator = None

        if order is not None:
            self.order = order
        if order_by_column is not None:
            self.order_by_column = order_by_column
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if project_name is not None:
            self.project_name = project_name
        if source_id is not None:
            self.source_id = source_id
        if source_name is not None:
            self.source_name = source_name
        if source_state is not None:
            self.source_state = source_state
        if source_type is not None:
            self.source_type = source_type
        if tag_filters is not None:
            self.tag_filters = tag_filters

    @property
    def order(self):
        """Gets the order of this DescribeMigrationSourcesRequest.  # noqa: E501


        :return: The order of this DescribeMigrationSourcesRequest.  # noqa: E501
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this DescribeMigrationSourcesRequest.


        :param order: The order of this DescribeMigrationSourcesRequest.  # noqa: E501
        :type: str
        """

        self._order = order

    @property
    def order_by_column(self):
        """Gets the order_by_column of this DescribeMigrationSourcesRequest.  # noqa: E501


        :return: The order_by_column of this DescribeMigrationSourcesRequest.  # noqa: E501
        :rtype: str
        """
        return self._order_by_column

    @order_by_column.setter
    def order_by_column(self, order_by_column):
        """Sets the order_by_column of this DescribeMigrationSourcesRequest.


        :param order_by_column: The order_by_column of this DescribeMigrationSourcesRequest.  # noqa: E501
        :type: str
        """

        self._order_by_column = order_by_column

    @property
    def page_number(self):
        """Gets the page_number of this DescribeMigrationSourcesRequest.  # noqa: E501


        :return: The page_number of this DescribeMigrationSourcesRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this DescribeMigrationSourcesRequest.


        :param page_number: The page_number of this DescribeMigrationSourcesRequest.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this DescribeMigrationSourcesRequest.  # noqa: E501


        :return: The page_size of this DescribeMigrationSourcesRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this DescribeMigrationSourcesRequest.


        :param page_size: The page_size of this DescribeMigrationSourcesRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def project_name(self):
        """Gets the project_name of this DescribeMigrationSourcesRequest.  # noqa: E501


        :return: The project_name of this DescribeMigrationSourcesRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this DescribeMigrationSourcesRequest.


        :param project_name: The project_name of this DescribeMigrationSourcesRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def source_id(self):
        """Gets the source_id of this DescribeMigrationSourcesRequest.  # noqa: E501


        :return: The source_id of this DescribeMigrationSourcesRequest.  # noqa: E501
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this DescribeMigrationSourcesRequest.


        :param source_id: The source_id of this DescribeMigrationSourcesRequest.  # noqa: E501
        :type: str
        """

        self._source_id = source_id

    @property
    def source_name(self):
        """Gets the source_name of this DescribeMigrationSourcesRequest.  # noqa: E501


        :return: The source_name of this DescribeMigrationSourcesRequest.  # noqa: E501
        :rtype: str
        """
        return self._source_name

    @source_name.setter
    def source_name(self, source_name):
        """Sets the source_name of this DescribeMigrationSourcesRequest.


        :param source_name: The source_name of this DescribeMigrationSourcesRequest.  # noqa: E501
        :type: str
        """

        self._source_name = source_name

    @property
    def source_state(self):
        """Gets the source_state of this DescribeMigrationSourcesRequest.  # noqa: E501


        :return: The source_state of this DescribeMigrationSourcesRequest.  # noqa: E501
        :rtype: str
        """
        return self._source_state

    @source_state.setter
    def source_state(self, source_state):
        """Sets the source_state of this DescribeMigrationSourcesRequest.


        :param source_state: The source_state of this DescribeMigrationSourcesRequest.  # noqa: E501
        :type: str
        """

        self._source_state = source_state

    @property
    def source_type(self):
        """Gets the source_type of this DescribeMigrationSourcesRequest.  # noqa: E501


        :return: The source_type of this DescribeMigrationSourcesRequest.  # noqa: E501
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this DescribeMigrationSourcesRequest.


        :param source_type: The source_type of this DescribeMigrationSourcesRequest.  # noqa: E501
        :type: str
        """

        self._source_type = source_type

    @property
    def tag_filters(self):
        """Gets the tag_filters of this DescribeMigrationSourcesRequest.  # noqa: E501


        :return: The tag_filters of this DescribeMigrationSourcesRequest.  # noqa: E501
        :rtype: list[TagFilterForDescribeMigrationSourcesInput]
        """
        return self._tag_filters

    @tag_filters.setter
    def tag_filters(self, tag_filters):
        """Sets the tag_filters of this DescribeMigrationSourcesRequest.


        :param tag_filters: The tag_filters of this DescribeMigrationSourcesRequest.  # noqa: E501
        :type: list[TagFilterForDescribeMigrationSourcesInput]
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
        if issubclass(DescribeMigrationSourcesRequest, dict):
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
        if not isinstance(other, DescribeMigrationSourcesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeMigrationSourcesRequest):
            return True

        return self.to_dict() != other.to_dict()
