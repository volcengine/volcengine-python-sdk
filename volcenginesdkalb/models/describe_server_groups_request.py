# coding: utf-8

"""
    alb

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeServerGroupsRequest(object):
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
        'page_number': 'int',
        'page_size': 'int',
        'project_name': 'str',
        'server_group_ids': 'list[str]',
        'server_group_names': 'list[str]',
        'server_group_type': 'str',
        'tag_filters': 'list[TagFilterForDescribeServerGroupsInput]',
        'vpc_id': 'str'
    }

    attribute_map = {
        'page_number': 'PageNumber',
        'page_size': 'PageSize',
        'project_name': 'ProjectName',
        'server_group_ids': 'ServerGroupIds',
        'server_group_names': 'ServerGroupNames',
        'server_group_type': 'ServerGroupType',
        'tag_filters': 'TagFilters',
        'vpc_id': 'VpcID'
    }

    def __init__(self, page_number=None, page_size=None, project_name=None, server_group_ids=None, server_group_names=None, server_group_type=None, tag_filters=None, vpc_id=None, _configuration=None):  # noqa: E501
        """DescribeServerGroupsRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._page_number = None
        self._page_size = None
        self._project_name = None
        self._server_group_ids = None
        self._server_group_names = None
        self._server_group_type = None
        self._tag_filters = None
        self._vpc_id = None
        self.discriminator = None

        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if project_name is not None:
            self.project_name = project_name
        if server_group_ids is not None:
            self.server_group_ids = server_group_ids
        if server_group_names is not None:
            self.server_group_names = server_group_names
        if server_group_type is not None:
            self.server_group_type = server_group_type
        if tag_filters is not None:
            self.tag_filters = tag_filters
        if vpc_id is not None:
            self.vpc_id = vpc_id

    @property
    def page_number(self):
        """Gets the page_number of this DescribeServerGroupsRequest.  # noqa: E501


        :return: The page_number of this DescribeServerGroupsRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this DescribeServerGroupsRequest.


        :param page_number: The page_number of this DescribeServerGroupsRequest.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this DescribeServerGroupsRequest.  # noqa: E501


        :return: The page_size of this DescribeServerGroupsRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this DescribeServerGroupsRequest.


        :param page_size: The page_size of this DescribeServerGroupsRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def project_name(self):
        """Gets the project_name of this DescribeServerGroupsRequest.  # noqa: E501


        :return: The project_name of this DescribeServerGroupsRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this DescribeServerGroupsRequest.


        :param project_name: The project_name of this DescribeServerGroupsRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def server_group_ids(self):
        """Gets the server_group_ids of this DescribeServerGroupsRequest.  # noqa: E501


        :return: The server_group_ids of this DescribeServerGroupsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._server_group_ids

    @server_group_ids.setter
    def server_group_ids(self, server_group_ids):
        """Sets the server_group_ids of this DescribeServerGroupsRequest.


        :param server_group_ids: The server_group_ids of this DescribeServerGroupsRequest.  # noqa: E501
        :type: list[str]
        """

        self._server_group_ids = server_group_ids

    @property
    def server_group_names(self):
        """Gets the server_group_names of this DescribeServerGroupsRequest.  # noqa: E501


        :return: The server_group_names of this DescribeServerGroupsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._server_group_names

    @server_group_names.setter
    def server_group_names(self, server_group_names):
        """Sets the server_group_names of this DescribeServerGroupsRequest.


        :param server_group_names: The server_group_names of this DescribeServerGroupsRequest.  # noqa: E501
        :type: list[str]
        """

        self._server_group_names = server_group_names

    @property
    def server_group_type(self):
        """Gets the server_group_type of this DescribeServerGroupsRequest.  # noqa: E501


        :return: The server_group_type of this DescribeServerGroupsRequest.  # noqa: E501
        :rtype: str
        """
        return self._server_group_type

    @server_group_type.setter
    def server_group_type(self, server_group_type):
        """Sets the server_group_type of this DescribeServerGroupsRequest.


        :param server_group_type: The server_group_type of this DescribeServerGroupsRequest.  # noqa: E501
        :type: str
        """

        self._server_group_type = server_group_type

    @property
    def tag_filters(self):
        """Gets the tag_filters of this DescribeServerGroupsRequest.  # noqa: E501


        :return: The tag_filters of this DescribeServerGroupsRequest.  # noqa: E501
        :rtype: list[TagFilterForDescribeServerGroupsInput]
        """
        return self._tag_filters

    @tag_filters.setter
    def tag_filters(self, tag_filters):
        """Sets the tag_filters of this DescribeServerGroupsRequest.


        :param tag_filters: The tag_filters of this DescribeServerGroupsRequest.  # noqa: E501
        :type: list[TagFilterForDescribeServerGroupsInput]
        """

        self._tag_filters = tag_filters

    @property
    def vpc_id(self):
        """Gets the vpc_id of this DescribeServerGroupsRequest.  # noqa: E501


        :return: The vpc_id of this DescribeServerGroupsRequest.  # noqa: E501
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this DescribeServerGroupsRequest.


        :param vpc_id: The vpc_id of this DescribeServerGroupsRequest.  # noqa: E501
        :type: str
        """

        self._vpc_id = vpc_id

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
        if issubclass(DescribeServerGroupsRequest, dict):
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
        if not isinstance(other, DescribeServerGroupsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeServerGroupsRequest):
            return True

        return self.to_dict() != other.to_dict()
