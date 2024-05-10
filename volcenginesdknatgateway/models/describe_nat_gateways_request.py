# coding: utf-8

"""
    natgateway

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeNatGatewaysRequest(object):
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
        'description': 'str',
        'nat_gateway_ids': 'list[str]',
        'nat_gateway_name': 'str',
        'page_number': 'int',
        'page_size': 'int',
        'project_name': 'str',
        'spec': 'str',
        'subnet_id': 'str',
        'tag_filters': 'list[TagFilterForDescribeNatGatewaysInput]',
        'vpc_id': 'str'
    }

    attribute_map = {
        'description': 'Description',
        'nat_gateway_ids': 'NatGatewayIds',
        'nat_gateway_name': 'NatGatewayName',
        'page_number': 'PageNumber',
        'page_size': 'PageSize',
        'project_name': 'ProjectName',
        'spec': 'Spec',
        'subnet_id': 'SubnetId',
        'tag_filters': 'TagFilters',
        'vpc_id': 'VpcId'
    }

    def __init__(self, description=None, nat_gateway_ids=None, nat_gateway_name=None, page_number=None, page_size=None, project_name=None, spec=None, subnet_id=None, tag_filters=None, vpc_id=None, _configuration=None):  # noqa: E501
        """DescribeNatGatewaysRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._description = None
        self._nat_gateway_ids = None
        self._nat_gateway_name = None
        self._page_number = None
        self._page_size = None
        self._project_name = None
        self._spec = None
        self._subnet_id = None
        self._tag_filters = None
        self._vpc_id = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if nat_gateway_ids is not None:
            self.nat_gateway_ids = nat_gateway_ids
        if nat_gateway_name is not None:
            self.nat_gateway_name = nat_gateway_name
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if project_name is not None:
            self.project_name = project_name
        if spec is not None:
            self.spec = spec
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if tag_filters is not None:
            self.tag_filters = tag_filters
        if vpc_id is not None:
            self.vpc_id = vpc_id

    @property
    def description(self):
        """Gets the description of this DescribeNatGatewaysRequest.  # noqa: E501


        :return: The description of this DescribeNatGatewaysRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DescribeNatGatewaysRequest.


        :param description: The description of this DescribeNatGatewaysRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def nat_gateway_ids(self):
        """Gets the nat_gateway_ids of this DescribeNatGatewaysRequest.  # noqa: E501


        :return: The nat_gateway_ids of this DescribeNatGatewaysRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._nat_gateway_ids

    @nat_gateway_ids.setter
    def nat_gateway_ids(self, nat_gateway_ids):
        """Sets the nat_gateway_ids of this DescribeNatGatewaysRequest.


        :param nat_gateway_ids: The nat_gateway_ids of this DescribeNatGatewaysRequest.  # noqa: E501
        :type: list[str]
        """

        self._nat_gateway_ids = nat_gateway_ids

    @property
    def nat_gateway_name(self):
        """Gets the nat_gateway_name of this DescribeNatGatewaysRequest.  # noqa: E501


        :return: The nat_gateway_name of this DescribeNatGatewaysRequest.  # noqa: E501
        :rtype: str
        """
        return self._nat_gateway_name

    @nat_gateway_name.setter
    def nat_gateway_name(self, nat_gateway_name):
        """Sets the nat_gateway_name of this DescribeNatGatewaysRequest.


        :param nat_gateway_name: The nat_gateway_name of this DescribeNatGatewaysRequest.  # noqa: E501
        :type: str
        """

        self._nat_gateway_name = nat_gateway_name

    @property
    def page_number(self):
        """Gets the page_number of this DescribeNatGatewaysRequest.  # noqa: E501


        :return: The page_number of this DescribeNatGatewaysRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this DescribeNatGatewaysRequest.


        :param page_number: The page_number of this DescribeNatGatewaysRequest.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this DescribeNatGatewaysRequest.  # noqa: E501


        :return: The page_size of this DescribeNatGatewaysRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this DescribeNatGatewaysRequest.


        :param page_size: The page_size of this DescribeNatGatewaysRequest.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                page_size is not None and page_size > 100):  # noqa: E501
            raise ValueError("Invalid value for `page_size`, must be a value less than or equal to `100`")  # noqa: E501

        self._page_size = page_size

    @property
    def project_name(self):
        """Gets the project_name of this DescribeNatGatewaysRequest.  # noqa: E501


        :return: The project_name of this DescribeNatGatewaysRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this DescribeNatGatewaysRequest.


        :param project_name: The project_name of this DescribeNatGatewaysRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def spec(self):
        """Gets the spec of this DescribeNatGatewaysRequest.  # noqa: E501


        :return: The spec of this DescribeNatGatewaysRequest.  # noqa: E501
        :rtype: str
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this DescribeNatGatewaysRequest.


        :param spec: The spec of this DescribeNatGatewaysRequest.  # noqa: E501
        :type: str
        """

        self._spec = spec

    @property
    def subnet_id(self):
        """Gets the subnet_id of this DescribeNatGatewaysRequest.  # noqa: E501


        :return: The subnet_id of this DescribeNatGatewaysRequest.  # noqa: E501
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this DescribeNatGatewaysRequest.


        :param subnet_id: The subnet_id of this DescribeNatGatewaysRequest.  # noqa: E501
        :type: str
        """

        self._subnet_id = subnet_id

    @property
    def tag_filters(self):
        """Gets the tag_filters of this DescribeNatGatewaysRequest.  # noqa: E501


        :return: The tag_filters of this DescribeNatGatewaysRequest.  # noqa: E501
        :rtype: list[TagFilterForDescribeNatGatewaysInput]
        """
        return self._tag_filters

    @tag_filters.setter
    def tag_filters(self, tag_filters):
        """Sets the tag_filters of this DescribeNatGatewaysRequest.


        :param tag_filters: The tag_filters of this DescribeNatGatewaysRequest.  # noqa: E501
        :type: list[TagFilterForDescribeNatGatewaysInput]
        """

        self._tag_filters = tag_filters

    @property
    def vpc_id(self):
        """Gets the vpc_id of this DescribeNatGatewaysRequest.  # noqa: E501


        :return: The vpc_id of this DescribeNatGatewaysRequest.  # noqa: E501
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this DescribeNatGatewaysRequest.


        :param vpc_id: The vpc_id of this DescribeNatGatewaysRequest.  # noqa: E501
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
        if issubclass(DescribeNatGatewaysRequest, dict):
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
        if not isinstance(other, DescribeNatGatewaysRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeNatGatewaysRequest):
            return True

        return self.to_dict() != other.to_dict()
