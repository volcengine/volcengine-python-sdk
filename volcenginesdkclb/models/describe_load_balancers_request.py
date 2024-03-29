# coding: utf-8

"""
    clb

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeLoadBalancersRequest(object):
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
        'address_ip_version': 'str',
        'eip_address': 'str',
        'eni_address': 'str',
        'load_balancer_ids': 'list[str]',
        'load_balancer_name': 'str',
        'master_zone_id': 'str',
        'page_number': 'int',
        'page_size': 'int',
        'project_name': 'str',
        'status': 'str',
        'tag_filters': 'list[TagFilterForDescribeLoadBalancersInput]',
        'type': 'str',
        'vpc_id': 'str'
    }

    attribute_map = {
        'address_ip_version': 'AddressIpVersion',
        'eip_address': 'EipAddress',
        'eni_address': 'EniAddress',
        'load_balancer_ids': 'LoadBalancerIds',
        'load_balancer_name': 'LoadBalancerName',
        'master_zone_id': 'MasterZoneId',
        'page_number': 'PageNumber',
        'page_size': 'PageSize',
        'project_name': 'ProjectName',
        'status': 'Status',
        'tag_filters': 'TagFilters',
        'type': 'Type',
        'vpc_id': 'VpcId'
    }

    def __init__(self, address_ip_version=None, eip_address=None, eni_address=None, load_balancer_ids=None, load_balancer_name=None, master_zone_id=None, page_number=None, page_size=None, project_name=None, status=None, tag_filters=None, type=None, vpc_id=None, _configuration=None):  # noqa: E501
        """DescribeLoadBalancersRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._address_ip_version = None
        self._eip_address = None
        self._eni_address = None
        self._load_balancer_ids = None
        self._load_balancer_name = None
        self._master_zone_id = None
        self._page_number = None
        self._page_size = None
        self._project_name = None
        self._status = None
        self._tag_filters = None
        self._type = None
        self._vpc_id = None
        self.discriminator = None

        if address_ip_version is not None:
            self.address_ip_version = address_ip_version
        if eip_address is not None:
            self.eip_address = eip_address
        if eni_address is not None:
            self.eni_address = eni_address
        if load_balancer_ids is not None:
            self.load_balancer_ids = load_balancer_ids
        if load_balancer_name is not None:
            self.load_balancer_name = load_balancer_name
        if master_zone_id is not None:
            self.master_zone_id = master_zone_id
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if project_name is not None:
            self.project_name = project_name
        if status is not None:
            self.status = status
        if tag_filters is not None:
            self.tag_filters = tag_filters
        if type is not None:
            self.type = type
        if vpc_id is not None:
            self.vpc_id = vpc_id

    @property
    def address_ip_version(self):
        """Gets the address_ip_version of this DescribeLoadBalancersRequest.  # noqa: E501


        :return: The address_ip_version of this DescribeLoadBalancersRequest.  # noqa: E501
        :rtype: str
        """
        return self._address_ip_version

    @address_ip_version.setter
    def address_ip_version(self, address_ip_version):
        """Sets the address_ip_version of this DescribeLoadBalancersRequest.


        :param address_ip_version: The address_ip_version of this DescribeLoadBalancersRequest.  # noqa: E501
        :type: str
        """

        self._address_ip_version = address_ip_version

    @property
    def eip_address(self):
        """Gets the eip_address of this DescribeLoadBalancersRequest.  # noqa: E501


        :return: The eip_address of this DescribeLoadBalancersRequest.  # noqa: E501
        :rtype: str
        """
        return self._eip_address

    @eip_address.setter
    def eip_address(self, eip_address):
        """Sets the eip_address of this DescribeLoadBalancersRequest.


        :param eip_address: The eip_address of this DescribeLoadBalancersRequest.  # noqa: E501
        :type: str
        """

        self._eip_address = eip_address

    @property
    def eni_address(self):
        """Gets the eni_address of this DescribeLoadBalancersRequest.  # noqa: E501


        :return: The eni_address of this DescribeLoadBalancersRequest.  # noqa: E501
        :rtype: str
        """
        return self._eni_address

    @eni_address.setter
    def eni_address(self, eni_address):
        """Sets the eni_address of this DescribeLoadBalancersRequest.


        :param eni_address: The eni_address of this DescribeLoadBalancersRequest.  # noqa: E501
        :type: str
        """

        self._eni_address = eni_address

    @property
    def load_balancer_ids(self):
        """Gets the load_balancer_ids of this DescribeLoadBalancersRequest.  # noqa: E501


        :return: The load_balancer_ids of this DescribeLoadBalancersRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._load_balancer_ids

    @load_balancer_ids.setter
    def load_balancer_ids(self, load_balancer_ids):
        """Sets the load_balancer_ids of this DescribeLoadBalancersRequest.


        :param load_balancer_ids: The load_balancer_ids of this DescribeLoadBalancersRequest.  # noqa: E501
        :type: list[str]
        """

        self._load_balancer_ids = load_balancer_ids

    @property
    def load_balancer_name(self):
        """Gets the load_balancer_name of this DescribeLoadBalancersRequest.  # noqa: E501


        :return: The load_balancer_name of this DescribeLoadBalancersRequest.  # noqa: E501
        :rtype: str
        """
        return self._load_balancer_name

    @load_balancer_name.setter
    def load_balancer_name(self, load_balancer_name):
        """Sets the load_balancer_name of this DescribeLoadBalancersRequest.


        :param load_balancer_name: The load_balancer_name of this DescribeLoadBalancersRequest.  # noqa: E501
        :type: str
        """

        self._load_balancer_name = load_balancer_name

    @property
    def master_zone_id(self):
        """Gets the master_zone_id of this DescribeLoadBalancersRequest.  # noqa: E501


        :return: The master_zone_id of this DescribeLoadBalancersRequest.  # noqa: E501
        :rtype: str
        """
        return self._master_zone_id

    @master_zone_id.setter
    def master_zone_id(self, master_zone_id):
        """Sets the master_zone_id of this DescribeLoadBalancersRequest.


        :param master_zone_id: The master_zone_id of this DescribeLoadBalancersRequest.  # noqa: E501
        :type: str
        """

        self._master_zone_id = master_zone_id

    @property
    def page_number(self):
        """Gets the page_number of this DescribeLoadBalancersRequest.  # noqa: E501


        :return: The page_number of this DescribeLoadBalancersRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this DescribeLoadBalancersRequest.


        :param page_number: The page_number of this DescribeLoadBalancersRequest.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this DescribeLoadBalancersRequest.  # noqa: E501


        :return: The page_size of this DescribeLoadBalancersRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this DescribeLoadBalancersRequest.


        :param page_size: The page_size of this DescribeLoadBalancersRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def project_name(self):
        """Gets the project_name of this DescribeLoadBalancersRequest.  # noqa: E501


        :return: The project_name of this DescribeLoadBalancersRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this DescribeLoadBalancersRequest.


        :param project_name: The project_name of this DescribeLoadBalancersRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def status(self):
        """Gets the status of this DescribeLoadBalancersRequest.  # noqa: E501


        :return: The status of this DescribeLoadBalancersRequest.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DescribeLoadBalancersRequest.


        :param status: The status of this DescribeLoadBalancersRequest.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def tag_filters(self):
        """Gets the tag_filters of this DescribeLoadBalancersRequest.  # noqa: E501


        :return: The tag_filters of this DescribeLoadBalancersRequest.  # noqa: E501
        :rtype: list[TagFilterForDescribeLoadBalancersInput]
        """
        return self._tag_filters

    @tag_filters.setter
    def tag_filters(self, tag_filters):
        """Sets the tag_filters of this DescribeLoadBalancersRequest.


        :param tag_filters: The tag_filters of this DescribeLoadBalancersRequest.  # noqa: E501
        :type: list[TagFilterForDescribeLoadBalancersInput]
        """

        self._tag_filters = tag_filters

    @property
    def type(self):
        """Gets the type of this DescribeLoadBalancersRequest.  # noqa: E501


        :return: The type of this DescribeLoadBalancersRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DescribeLoadBalancersRequest.


        :param type: The type of this DescribeLoadBalancersRequest.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def vpc_id(self):
        """Gets the vpc_id of this DescribeLoadBalancersRequest.  # noqa: E501


        :return: The vpc_id of this DescribeLoadBalancersRequest.  # noqa: E501
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this DescribeLoadBalancersRequest.


        :param vpc_id: The vpc_id of this DescribeLoadBalancersRequest.  # noqa: E501
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
        if issubclass(DescribeLoadBalancersRequest, dict):
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
        if not isinstance(other, DescribeLoadBalancersRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeLoadBalancersRequest):
            return True

        return self.to_dict() != other.to_dict()
