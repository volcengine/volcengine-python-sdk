# coding: utf-8

"""
    livesaas20230801

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class UpdateAreaConfigResponse(object):
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
        'area_id': 'str',
        'area_ip': 'AreaIpForUpdateAreaConfigOutput',
        'area_name': 'str',
        'create_time': 'int',
        'enable_extranet_url': 'bool',
        'enable_office_list': 'list[str]',
        'enable_stream_router_list': 'list[str]',
        'lb_strategy': 'str'
    }

    attribute_map = {
        'area_id': 'AreaId',
        'area_ip': 'AreaIp',
        'area_name': 'AreaName',
        'create_time': 'CreateTime',
        'enable_extranet_url': 'EnableExtranetUrl',
        'enable_office_list': 'EnableOfficeList',
        'enable_stream_router_list': 'EnableStreamRouterList',
        'lb_strategy': 'LBStrategy'
    }

    def __init__(self, area_id=None, area_ip=None, area_name=None, create_time=None, enable_extranet_url=None, enable_office_list=None, enable_stream_router_list=None, lb_strategy=None, _configuration=None):  # noqa: E501
        """UpdateAreaConfigResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._area_id = None
        self._area_ip = None
        self._area_name = None
        self._create_time = None
        self._enable_extranet_url = None
        self._enable_office_list = None
        self._enable_stream_router_list = None
        self._lb_strategy = None
        self.discriminator = None

        if area_id is not None:
            self.area_id = area_id
        if area_ip is not None:
            self.area_ip = area_ip
        if area_name is not None:
            self.area_name = area_name
        if create_time is not None:
            self.create_time = create_time
        if enable_extranet_url is not None:
            self.enable_extranet_url = enable_extranet_url
        if enable_office_list is not None:
            self.enable_office_list = enable_office_list
        if enable_stream_router_list is not None:
            self.enable_stream_router_list = enable_stream_router_list
        if lb_strategy is not None:
            self.lb_strategy = lb_strategy

    @property
    def area_id(self):
        """Gets the area_id of this UpdateAreaConfigResponse.  # noqa: E501


        :return: The area_id of this UpdateAreaConfigResponse.  # noqa: E501
        :rtype: str
        """
        return self._area_id

    @area_id.setter
    def area_id(self, area_id):
        """Sets the area_id of this UpdateAreaConfigResponse.


        :param area_id: The area_id of this UpdateAreaConfigResponse.  # noqa: E501
        :type: str
        """

        self._area_id = area_id

    @property
    def area_ip(self):
        """Gets the area_ip of this UpdateAreaConfigResponse.  # noqa: E501


        :return: The area_ip of this UpdateAreaConfigResponse.  # noqa: E501
        :rtype: AreaIpForUpdateAreaConfigOutput
        """
        return self._area_ip

    @area_ip.setter
    def area_ip(self, area_ip):
        """Sets the area_ip of this UpdateAreaConfigResponse.


        :param area_ip: The area_ip of this UpdateAreaConfigResponse.  # noqa: E501
        :type: AreaIpForUpdateAreaConfigOutput
        """

        self._area_ip = area_ip

    @property
    def area_name(self):
        """Gets the area_name of this UpdateAreaConfigResponse.  # noqa: E501


        :return: The area_name of this UpdateAreaConfigResponse.  # noqa: E501
        :rtype: str
        """
        return self._area_name

    @area_name.setter
    def area_name(self, area_name):
        """Sets the area_name of this UpdateAreaConfigResponse.


        :param area_name: The area_name of this UpdateAreaConfigResponse.  # noqa: E501
        :type: str
        """

        self._area_name = area_name

    @property
    def create_time(self):
        """Gets the create_time of this UpdateAreaConfigResponse.  # noqa: E501


        :return: The create_time of this UpdateAreaConfigResponse.  # noqa: E501
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this UpdateAreaConfigResponse.


        :param create_time: The create_time of this UpdateAreaConfigResponse.  # noqa: E501
        :type: int
        """

        self._create_time = create_time

    @property
    def enable_extranet_url(self):
        """Gets the enable_extranet_url of this UpdateAreaConfigResponse.  # noqa: E501


        :return: The enable_extranet_url of this UpdateAreaConfigResponse.  # noqa: E501
        :rtype: bool
        """
        return self._enable_extranet_url

    @enable_extranet_url.setter
    def enable_extranet_url(self, enable_extranet_url):
        """Sets the enable_extranet_url of this UpdateAreaConfigResponse.


        :param enable_extranet_url: The enable_extranet_url of this UpdateAreaConfigResponse.  # noqa: E501
        :type: bool
        """

        self._enable_extranet_url = enable_extranet_url

    @property
    def enable_office_list(self):
        """Gets the enable_office_list of this UpdateAreaConfigResponse.  # noqa: E501


        :return: The enable_office_list of this UpdateAreaConfigResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._enable_office_list

    @enable_office_list.setter
    def enable_office_list(self, enable_office_list):
        """Sets the enable_office_list of this UpdateAreaConfigResponse.


        :param enable_office_list: The enable_office_list of this UpdateAreaConfigResponse.  # noqa: E501
        :type: list[str]
        """

        self._enable_office_list = enable_office_list

    @property
    def enable_stream_router_list(self):
        """Gets the enable_stream_router_list of this UpdateAreaConfigResponse.  # noqa: E501


        :return: The enable_stream_router_list of this UpdateAreaConfigResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._enable_stream_router_list

    @enable_stream_router_list.setter
    def enable_stream_router_list(self, enable_stream_router_list):
        """Sets the enable_stream_router_list of this UpdateAreaConfigResponse.


        :param enable_stream_router_list: The enable_stream_router_list of this UpdateAreaConfigResponse.  # noqa: E501
        :type: list[str]
        """

        self._enable_stream_router_list = enable_stream_router_list

    @property
    def lb_strategy(self):
        """Gets the lb_strategy of this UpdateAreaConfigResponse.  # noqa: E501


        :return: The lb_strategy of this UpdateAreaConfigResponse.  # noqa: E501
        :rtype: str
        """
        return self._lb_strategy

    @lb_strategy.setter
    def lb_strategy(self, lb_strategy):
        """Sets the lb_strategy of this UpdateAreaConfigResponse.


        :param lb_strategy: The lb_strategy of this UpdateAreaConfigResponse.  # noqa: E501
        :type: str
        """

        self._lb_strategy = lb_strategy

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
        if issubclass(UpdateAreaConfigResponse, dict):
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
        if not isinstance(other, UpdateAreaConfigResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateAreaConfigResponse):
            return True

        return self.to_dict() != other.to_dict()
