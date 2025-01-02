# coding: utf-8

"""
    waf

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class UpdateAclRuleRequest(object):
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
        'accurate_group': 'AccurateGroupForUpdateAclRuleInput',
        'acl_type': 'str',
        'action': 'str',
        'advanced': 'int',
        'description': 'str',
        'enable': 'int',
        'host_add_type': 'int',
        'host_group_id': 'list[int]',
        'host_list': 'list[str]',
        'id': 'int',
        'ip_add_type': 'int',
        'ip_group_id': 'list[int]',
        'ip_list': 'list[str]',
        'ip_location_country': 'list[str]',
        'ip_location_subregion': 'list[str]',
        'name': 'str',
        'prefix_switch': 'int',
        'project_name': 'str',
        'url': 'str'
    }

    attribute_map = {
        'accurate_group': 'AccurateGroup',
        'acl_type': 'AclType',
        'action': 'Action',
        'advanced': 'Advanced',
        'description': 'Description',
        'enable': 'Enable',
        'host_add_type': 'HostAddType',
        'host_group_id': 'HostGroupId',
        'host_list': 'HostList',
        'id': 'ID',
        'ip_add_type': 'IpAddType',
        'ip_group_id': 'IpGroupId',
        'ip_list': 'IpList',
        'ip_location_country': 'IpLocationCountry',
        'ip_location_subregion': 'IpLocationSubregion',
        'name': 'Name',
        'prefix_switch': 'PrefixSwitch',
        'project_name': 'ProjectName',
        'url': 'Url'
    }

    def __init__(self, accurate_group=None, acl_type=None, action=None, advanced=None, description=None, enable=None, host_add_type=None, host_group_id=None, host_list=None, id=None, ip_add_type=None, ip_group_id=None, ip_list=None, ip_location_country=None, ip_location_subregion=None, name=None, prefix_switch=None, project_name=None, url=None, _configuration=None):  # noqa: E501
        """UpdateAclRuleRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._accurate_group = None
        self._acl_type = None
        self._action = None
        self._advanced = None
        self._description = None
        self._enable = None
        self._host_add_type = None
        self._host_group_id = None
        self._host_list = None
        self._id = None
        self._ip_add_type = None
        self._ip_group_id = None
        self._ip_list = None
        self._ip_location_country = None
        self._ip_location_subregion = None
        self._name = None
        self._prefix_switch = None
        self._project_name = None
        self._url = None
        self.discriminator = None

        if accurate_group is not None:
            self.accurate_group = accurate_group
        self.acl_type = acl_type
        if action is not None:
            self.action = action
        if advanced is not None:
            self.advanced = advanced
        if description is not None:
            self.description = description
        self.enable = enable
        self.host_add_type = host_add_type
        if host_group_id is not None:
            self.host_group_id = host_group_id
        if host_list is not None:
            self.host_list = host_list
        self.id = id
        self.ip_add_type = ip_add_type
        if ip_group_id is not None:
            self.ip_group_id = ip_group_id
        if ip_list is not None:
            self.ip_list = ip_list
        if ip_location_country is not None:
            self.ip_location_country = ip_location_country
        if ip_location_subregion is not None:
            self.ip_location_subregion = ip_location_subregion
        self.name = name
        if prefix_switch is not None:
            self.prefix_switch = prefix_switch
        if project_name is not None:
            self.project_name = project_name
        self.url = url

    @property
    def accurate_group(self):
        """Gets the accurate_group of this UpdateAclRuleRequest.  # noqa: E501


        :return: The accurate_group of this UpdateAclRuleRequest.  # noqa: E501
        :rtype: AccurateGroupForUpdateAclRuleInput
        """
        return self._accurate_group

    @accurate_group.setter
    def accurate_group(self, accurate_group):
        """Sets the accurate_group of this UpdateAclRuleRequest.


        :param accurate_group: The accurate_group of this UpdateAclRuleRequest.  # noqa: E501
        :type: AccurateGroupForUpdateAclRuleInput
        """

        self._accurate_group = accurate_group

    @property
    def acl_type(self):
        """Gets the acl_type of this UpdateAclRuleRequest.  # noqa: E501


        :return: The acl_type of this UpdateAclRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._acl_type

    @acl_type.setter
    def acl_type(self, acl_type):
        """Sets the acl_type of this UpdateAclRuleRequest.


        :param acl_type: The acl_type of this UpdateAclRuleRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and acl_type is None:
            raise ValueError("Invalid value for `acl_type`, must not be `None`")  # noqa: E501

        self._acl_type = acl_type

    @property
    def action(self):
        """Gets the action of this UpdateAclRuleRequest.  # noqa: E501


        :return: The action of this UpdateAclRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this UpdateAclRuleRequest.


        :param action: The action of this UpdateAclRuleRequest.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def advanced(self):
        """Gets the advanced of this UpdateAclRuleRequest.  # noqa: E501


        :return: The advanced of this UpdateAclRuleRequest.  # noqa: E501
        :rtype: int
        """
        return self._advanced

    @advanced.setter
    def advanced(self, advanced):
        """Sets the advanced of this UpdateAclRuleRequest.


        :param advanced: The advanced of this UpdateAclRuleRequest.  # noqa: E501
        :type: int
        """

        self._advanced = advanced

    @property
    def description(self):
        """Gets the description of this UpdateAclRuleRequest.  # noqa: E501


        :return: The description of this UpdateAclRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateAclRuleRequest.


        :param description: The description of this UpdateAclRuleRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def enable(self):
        """Gets the enable of this UpdateAclRuleRequest.  # noqa: E501


        :return: The enable of this UpdateAclRuleRequest.  # noqa: E501
        :rtype: int
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this UpdateAclRuleRequest.


        :param enable: The enable of this UpdateAclRuleRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and enable is None:
            raise ValueError("Invalid value for `enable`, must not be `None`")  # noqa: E501

        self._enable = enable

    @property
    def host_add_type(self):
        """Gets the host_add_type of this UpdateAclRuleRequest.  # noqa: E501


        :return: The host_add_type of this UpdateAclRuleRequest.  # noqa: E501
        :rtype: int
        """
        return self._host_add_type

    @host_add_type.setter
    def host_add_type(self, host_add_type):
        """Sets the host_add_type of this UpdateAclRuleRequest.


        :param host_add_type: The host_add_type of this UpdateAclRuleRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and host_add_type is None:
            raise ValueError("Invalid value for `host_add_type`, must not be `None`")  # noqa: E501

        self._host_add_type = host_add_type

    @property
    def host_group_id(self):
        """Gets the host_group_id of this UpdateAclRuleRequest.  # noqa: E501


        :return: The host_group_id of this UpdateAclRuleRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._host_group_id

    @host_group_id.setter
    def host_group_id(self, host_group_id):
        """Sets the host_group_id of this UpdateAclRuleRequest.


        :param host_group_id: The host_group_id of this UpdateAclRuleRequest.  # noqa: E501
        :type: list[int]
        """

        self._host_group_id = host_group_id

    @property
    def host_list(self):
        """Gets the host_list of this UpdateAclRuleRequest.  # noqa: E501


        :return: The host_list of this UpdateAclRuleRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._host_list

    @host_list.setter
    def host_list(self, host_list):
        """Sets the host_list of this UpdateAclRuleRequest.


        :param host_list: The host_list of this UpdateAclRuleRequest.  # noqa: E501
        :type: list[str]
        """

        self._host_list = host_list

    @property
    def id(self):
        """Gets the id of this UpdateAclRuleRequest.  # noqa: E501


        :return: The id of this UpdateAclRuleRequest.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateAclRuleRequest.


        :param id: The id of this UpdateAclRuleRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def ip_add_type(self):
        """Gets the ip_add_type of this UpdateAclRuleRequest.  # noqa: E501


        :return: The ip_add_type of this UpdateAclRuleRequest.  # noqa: E501
        :rtype: int
        """
        return self._ip_add_type

    @ip_add_type.setter
    def ip_add_type(self, ip_add_type):
        """Sets the ip_add_type of this UpdateAclRuleRequest.


        :param ip_add_type: The ip_add_type of this UpdateAclRuleRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and ip_add_type is None:
            raise ValueError("Invalid value for `ip_add_type`, must not be `None`")  # noqa: E501

        self._ip_add_type = ip_add_type

    @property
    def ip_group_id(self):
        """Gets the ip_group_id of this UpdateAclRuleRequest.  # noqa: E501


        :return: The ip_group_id of this UpdateAclRuleRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._ip_group_id

    @ip_group_id.setter
    def ip_group_id(self, ip_group_id):
        """Sets the ip_group_id of this UpdateAclRuleRequest.


        :param ip_group_id: The ip_group_id of this UpdateAclRuleRequest.  # noqa: E501
        :type: list[int]
        """

        self._ip_group_id = ip_group_id

    @property
    def ip_list(self):
        """Gets the ip_list of this UpdateAclRuleRequest.  # noqa: E501


        :return: The ip_list of this UpdateAclRuleRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._ip_list

    @ip_list.setter
    def ip_list(self, ip_list):
        """Sets the ip_list of this UpdateAclRuleRequest.


        :param ip_list: The ip_list of this UpdateAclRuleRequest.  # noqa: E501
        :type: list[str]
        """

        self._ip_list = ip_list

    @property
    def ip_location_country(self):
        """Gets the ip_location_country of this UpdateAclRuleRequest.  # noqa: E501


        :return: The ip_location_country of this UpdateAclRuleRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._ip_location_country

    @ip_location_country.setter
    def ip_location_country(self, ip_location_country):
        """Sets the ip_location_country of this UpdateAclRuleRequest.


        :param ip_location_country: The ip_location_country of this UpdateAclRuleRequest.  # noqa: E501
        :type: list[str]
        """

        self._ip_location_country = ip_location_country

    @property
    def ip_location_subregion(self):
        """Gets the ip_location_subregion of this UpdateAclRuleRequest.  # noqa: E501


        :return: The ip_location_subregion of this UpdateAclRuleRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._ip_location_subregion

    @ip_location_subregion.setter
    def ip_location_subregion(self, ip_location_subregion):
        """Sets the ip_location_subregion of this UpdateAclRuleRequest.


        :param ip_location_subregion: The ip_location_subregion of this UpdateAclRuleRequest.  # noqa: E501
        :type: list[str]
        """

        self._ip_location_subregion = ip_location_subregion

    @property
    def name(self):
        """Gets the name of this UpdateAclRuleRequest.  # noqa: E501


        :return: The name of this UpdateAclRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateAclRuleRequest.


        :param name: The name of this UpdateAclRuleRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def prefix_switch(self):
        """Gets the prefix_switch of this UpdateAclRuleRequest.  # noqa: E501


        :return: The prefix_switch of this UpdateAclRuleRequest.  # noqa: E501
        :rtype: int
        """
        return self._prefix_switch

    @prefix_switch.setter
    def prefix_switch(self, prefix_switch):
        """Sets the prefix_switch of this UpdateAclRuleRequest.


        :param prefix_switch: The prefix_switch of this UpdateAclRuleRequest.  # noqa: E501
        :type: int
        """

        self._prefix_switch = prefix_switch

    @property
    def project_name(self):
        """Gets the project_name of this UpdateAclRuleRequest.  # noqa: E501


        :return: The project_name of this UpdateAclRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this UpdateAclRuleRequest.


        :param project_name: The project_name of this UpdateAclRuleRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def url(self):
        """Gets the url of this UpdateAclRuleRequest.  # noqa: E501


        :return: The url of this UpdateAclRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this UpdateAclRuleRequest.


        :param url: The url of this UpdateAclRuleRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

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
        if issubclass(UpdateAclRuleRequest, dict):
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
        if not isinstance(other, UpdateAclRuleRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateAclRuleRequest):
            return True

        return self.to_dict() != other.to_dict()
