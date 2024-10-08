# coding: utf-8

"""
    privatelink

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeVpcEndpointsRequest(object):
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
        'endpoint_ids': 'list[str]',
        'endpoint_index': 'int',
        'endpoint_name': 'str',
        'endpoint_type': 'str',
        'page_number': 'int',
        'page_size': 'int',
        'project_name': 'str',
        'service_id': 'str',
        'service_name': 'str',
        'status': 'str',
        'tag_filters': 'list[TagFilterForDescribeVpcEndpointsInput]',
        'vpc_id': 'str'
    }

    attribute_map = {
        'endpoint_ids': 'EndpointIds',
        'endpoint_index': 'EndpointIndex',
        'endpoint_name': 'EndpointName',
        'endpoint_type': 'EndpointType',
        'page_number': 'PageNumber',
        'page_size': 'PageSize',
        'project_name': 'ProjectName',
        'service_id': 'ServiceId',
        'service_name': 'ServiceName',
        'status': 'Status',
        'tag_filters': 'TagFilters',
        'vpc_id': 'VpcId'
    }

    def __init__(self, endpoint_ids=None, endpoint_index=None, endpoint_name=None, endpoint_type=None, page_number=None, page_size=None, project_name=None, service_id=None, service_name=None, status=None, tag_filters=None, vpc_id=None, _configuration=None):  # noqa: E501
        """DescribeVpcEndpointsRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._endpoint_ids = None
        self._endpoint_index = None
        self._endpoint_name = None
        self._endpoint_type = None
        self._page_number = None
        self._page_size = None
        self._project_name = None
        self._service_id = None
        self._service_name = None
        self._status = None
        self._tag_filters = None
        self._vpc_id = None
        self.discriminator = None

        if endpoint_ids is not None:
            self.endpoint_ids = endpoint_ids
        if endpoint_index is not None:
            self.endpoint_index = endpoint_index
        if endpoint_name is not None:
            self.endpoint_name = endpoint_name
        if endpoint_type is not None:
            self.endpoint_type = endpoint_type
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if project_name is not None:
            self.project_name = project_name
        if service_id is not None:
            self.service_id = service_id
        if service_name is not None:
            self.service_name = service_name
        if status is not None:
            self.status = status
        if tag_filters is not None:
            self.tag_filters = tag_filters
        if vpc_id is not None:
            self.vpc_id = vpc_id

    @property
    def endpoint_ids(self):
        """Gets the endpoint_ids of this DescribeVpcEndpointsRequest.  # noqa: E501


        :return: The endpoint_ids of this DescribeVpcEndpointsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._endpoint_ids

    @endpoint_ids.setter
    def endpoint_ids(self, endpoint_ids):
        """Sets the endpoint_ids of this DescribeVpcEndpointsRequest.


        :param endpoint_ids: The endpoint_ids of this DescribeVpcEndpointsRequest.  # noqa: E501
        :type: list[str]
        """

        self._endpoint_ids = endpoint_ids

    @property
    def endpoint_index(self):
        """Gets the endpoint_index of this DescribeVpcEndpointsRequest.  # noqa: E501


        :return: The endpoint_index of this DescribeVpcEndpointsRequest.  # noqa: E501
        :rtype: int
        """
        return self._endpoint_index

    @endpoint_index.setter
    def endpoint_index(self, endpoint_index):
        """Sets the endpoint_index of this DescribeVpcEndpointsRequest.


        :param endpoint_index: The endpoint_index of this DescribeVpcEndpointsRequest.  # noqa: E501
        :type: int
        """

        self._endpoint_index = endpoint_index

    @property
    def endpoint_name(self):
        """Gets the endpoint_name of this DescribeVpcEndpointsRequest.  # noqa: E501


        :return: The endpoint_name of this DescribeVpcEndpointsRequest.  # noqa: E501
        :rtype: str
        """
        return self._endpoint_name

    @endpoint_name.setter
    def endpoint_name(self, endpoint_name):
        """Sets the endpoint_name of this DescribeVpcEndpointsRequest.


        :param endpoint_name: The endpoint_name of this DescribeVpcEndpointsRequest.  # noqa: E501
        :type: str
        """

        self._endpoint_name = endpoint_name

    @property
    def endpoint_type(self):
        """Gets the endpoint_type of this DescribeVpcEndpointsRequest.  # noqa: E501


        :return: The endpoint_type of this DescribeVpcEndpointsRequest.  # noqa: E501
        :rtype: str
        """
        return self._endpoint_type

    @endpoint_type.setter
    def endpoint_type(self, endpoint_type):
        """Sets the endpoint_type of this DescribeVpcEndpointsRequest.


        :param endpoint_type: The endpoint_type of this DescribeVpcEndpointsRequest.  # noqa: E501
        :type: str
        """

        self._endpoint_type = endpoint_type

    @property
    def page_number(self):
        """Gets the page_number of this DescribeVpcEndpointsRequest.  # noqa: E501


        :return: The page_number of this DescribeVpcEndpointsRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this DescribeVpcEndpointsRequest.


        :param page_number: The page_number of this DescribeVpcEndpointsRequest.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this DescribeVpcEndpointsRequest.  # noqa: E501


        :return: The page_size of this DescribeVpcEndpointsRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this DescribeVpcEndpointsRequest.


        :param page_size: The page_size of this DescribeVpcEndpointsRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def project_name(self):
        """Gets the project_name of this DescribeVpcEndpointsRequest.  # noqa: E501


        :return: The project_name of this DescribeVpcEndpointsRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this DescribeVpcEndpointsRequest.


        :param project_name: The project_name of this DescribeVpcEndpointsRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def service_id(self):
        """Gets the service_id of this DescribeVpcEndpointsRequest.  # noqa: E501


        :return: The service_id of this DescribeVpcEndpointsRequest.  # noqa: E501
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this DescribeVpcEndpointsRequest.


        :param service_id: The service_id of this DescribeVpcEndpointsRequest.  # noqa: E501
        :type: str
        """

        self._service_id = service_id

    @property
    def service_name(self):
        """Gets the service_name of this DescribeVpcEndpointsRequest.  # noqa: E501


        :return: The service_name of this DescribeVpcEndpointsRequest.  # noqa: E501
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this DescribeVpcEndpointsRequest.


        :param service_name: The service_name of this DescribeVpcEndpointsRequest.  # noqa: E501
        :type: str
        """

        self._service_name = service_name

    @property
    def status(self):
        """Gets the status of this DescribeVpcEndpointsRequest.  # noqa: E501


        :return: The status of this DescribeVpcEndpointsRequest.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DescribeVpcEndpointsRequest.


        :param status: The status of this DescribeVpcEndpointsRequest.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def tag_filters(self):
        """Gets the tag_filters of this DescribeVpcEndpointsRequest.  # noqa: E501


        :return: The tag_filters of this DescribeVpcEndpointsRequest.  # noqa: E501
        :rtype: list[TagFilterForDescribeVpcEndpointsInput]
        """
        return self._tag_filters

    @tag_filters.setter
    def tag_filters(self, tag_filters):
        """Sets the tag_filters of this DescribeVpcEndpointsRequest.


        :param tag_filters: The tag_filters of this DescribeVpcEndpointsRequest.  # noqa: E501
        :type: list[TagFilterForDescribeVpcEndpointsInput]
        """

        self._tag_filters = tag_filters

    @property
    def vpc_id(self):
        """Gets the vpc_id of this DescribeVpcEndpointsRequest.  # noqa: E501


        :return: The vpc_id of this DescribeVpcEndpointsRequest.  # noqa: E501
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this DescribeVpcEndpointsRequest.


        :param vpc_id: The vpc_id of this DescribeVpcEndpointsRequest.  # noqa: E501
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
        if issubclass(DescribeVpcEndpointsRequest, dict):
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
        if not isinstance(other, DescribeVpcEndpointsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeVpcEndpointsRequest):
            return True

        return self.to_dict() != other.to_dict()
