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


class DescribeVpcsRequest(object):
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
        'is_default': 'bool',
        'max_results': 'int',
        'next_token': 'str',
        'page_number': 'int',
        'page_size': 'int',
        'project_name': 'str',
        'tag_filters': 'list[TagFilterForDescribeVpcsInput]',
        'vpc_ids': 'list[str]',
        'vpc_name': 'str'
    }

    attribute_map = {
        'is_default': 'IsDefault',
        'max_results': 'MaxResults',
        'next_token': 'NextToken',
        'page_number': 'PageNumber',
        'page_size': 'PageSize',
        'project_name': 'ProjectName',
        'tag_filters': 'TagFilters',
        'vpc_ids': 'VpcIds',
        'vpc_name': 'VpcName'
    }

    def __init__(self, is_default=None, max_results=None, next_token=None, page_number=None, page_size=None, project_name=None, tag_filters=None, vpc_ids=None, vpc_name=None, _configuration=None):  # noqa: E501
        """DescribeVpcsRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._is_default = None
        self._max_results = None
        self._next_token = None
        self._page_number = None
        self._page_size = None
        self._project_name = None
        self._tag_filters = None
        self._vpc_ids = None
        self._vpc_name = None
        self.discriminator = None

        if is_default is not None:
            self.is_default = is_default
        if max_results is not None:
            self.max_results = max_results
        if next_token is not None:
            self.next_token = next_token
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if project_name is not None:
            self.project_name = project_name
        if tag_filters is not None:
            self.tag_filters = tag_filters
        if vpc_ids is not None:
            self.vpc_ids = vpc_ids
        if vpc_name is not None:
            self.vpc_name = vpc_name

    @property
    def is_default(self):
        """Gets the is_default of this DescribeVpcsRequest.  # noqa: E501


        :return: The is_default of this DescribeVpcsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this DescribeVpcsRequest.


        :param is_default: The is_default of this DescribeVpcsRequest.  # noqa: E501
        :type: bool
        """

        self._is_default = is_default

    @property
    def max_results(self):
        """Gets the max_results of this DescribeVpcsRequest.  # noqa: E501


        :return: The max_results of this DescribeVpcsRequest.  # noqa: E501
        :rtype: int
        """
        return self._max_results

    @max_results.setter
    def max_results(self, max_results):
        """Sets the max_results of this DescribeVpcsRequest.


        :param max_results: The max_results of this DescribeVpcsRequest.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                max_results is not None and max_results > 100):  # noqa: E501
            raise ValueError("Invalid value for `max_results`, must be a value less than or equal to `100`")  # noqa: E501
        if (self._configuration.client_side_validation and
                max_results is not None and max_results < 1):  # noqa: E501
            raise ValueError("Invalid value for `max_results`, must be a value greater than or equal to `1`")  # noqa: E501

        self._max_results = max_results

    @property
    def next_token(self):
        """Gets the next_token of this DescribeVpcsRequest.  # noqa: E501


        :return: The next_token of this DescribeVpcsRequest.  # noqa: E501
        :rtype: str
        """
        return self._next_token

    @next_token.setter
    def next_token(self, next_token):
        """Sets the next_token of this DescribeVpcsRequest.


        :param next_token: The next_token of this DescribeVpcsRequest.  # noqa: E501
        :type: str
        """

        self._next_token = next_token

    @property
    def page_number(self):
        """Gets the page_number of this DescribeVpcsRequest.  # noqa: E501


        :return: The page_number of this DescribeVpcsRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this DescribeVpcsRequest.


        :param page_number: The page_number of this DescribeVpcsRequest.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this DescribeVpcsRequest.  # noqa: E501


        :return: The page_size of this DescribeVpcsRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this DescribeVpcsRequest.


        :param page_size: The page_size of this DescribeVpcsRequest.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                page_size is not None and page_size > 100):  # noqa: E501
            raise ValueError("Invalid value for `page_size`, must be a value less than or equal to `100`")  # noqa: E501

        self._page_size = page_size

    @property
    def project_name(self):
        """Gets the project_name of this DescribeVpcsRequest.  # noqa: E501


        :return: The project_name of this DescribeVpcsRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this DescribeVpcsRequest.


        :param project_name: The project_name of this DescribeVpcsRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def tag_filters(self):
        """Gets the tag_filters of this DescribeVpcsRequest.  # noqa: E501


        :return: The tag_filters of this DescribeVpcsRequest.  # noqa: E501
        :rtype: list[TagFilterForDescribeVpcsInput]
        """
        return self._tag_filters

    @tag_filters.setter
    def tag_filters(self, tag_filters):
        """Sets the tag_filters of this DescribeVpcsRequest.


        :param tag_filters: The tag_filters of this DescribeVpcsRequest.  # noqa: E501
        :type: list[TagFilterForDescribeVpcsInput]
        """

        self._tag_filters = tag_filters

    @property
    def vpc_ids(self):
        """Gets the vpc_ids of this DescribeVpcsRequest.  # noqa: E501


        :return: The vpc_ids of this DescribeVpcsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._vpc_ids

    @vpc_ids.setter
    def vpc_ids(self, vpc_ids):
        """Sets the vpc_ids of this DescribeVpcsRequest.


        :param vpc_ids: The vpc_ids of this DescribeVpcsRequest.  # noqa: E501
        :type: list[str]
        """

        self._vpc_ids = vpc_ids

    @property
    def vpc_name(self):
        """Gets the vpc_name of this DescribeVpcsRequest.  # noqa: E501


        :return: The vpc_name of this DescribeVpcsRequest.  # noqa: E501
        :rtype: str
        """
        return self._vpc_name

    @vpc_name.setter
    def vpc_name(self, vpc_name):
        """Sets the vpc_name of this DescribeVpcsRequest.


        :param vpc_name: The vpc_name of this DescribeVpcsRequest.  # noqa: E501
        :type: str
        """

        self._vpc_name = vpc_name

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
        if issubclass(DescribeVpcsRequest, dict):
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
        if not isinstance(other, DescribeVpcsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeVpcsRequest):
            return True

        return self.to_dict() != other.to_dict()
