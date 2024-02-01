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


class DatumForListAllowRuleOutput(object):
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
        'action': 'str',
        'add_src': 'int',
        'advanced': 'int',
        'client_ip': 'str',
        'description': 'str',
        'enable': 'int',
        'group_id': 'int',
        'host': 'str',
        'id': 'int',
        'ip_add_type': 'int',
        'ip_group_id': 'int',
        'ip_type': 'int',
        'isolation_id': 'str',
        'js_conf_id': 'int',
        'name': 'str',
        'policy': 'int',
        'rule_tag': 'str',
        'update_time': 'str',
        'url': 'str'
    }

    attribute_map = {
        'action': 'Action',
        'add_src': 'AddSrc',
        'advanced': 'Advanced',
        'client_ip': 'ClientIp',
        'description': 'Description',
        'enable': 'Enable',
        'group_id': 'GroupId',
        'host': 'Host',
        'id': 'Id',
        'ip_add_type': 'IpAddType',
        'ip_group_id': 'IpGroupId',
        'ip_type': 'IpType',
        'isolation_id': 'IsolationId',
        'js_conf_id': 'JsConfId',
        'name': 'Name',
        'policy': 'Policy',
        'rule_tag': 'RuleTag',
        'update_time': 'UpdateTime',
        'url': 'Url'
    }

    def __init__(self, action=None, add_src=None, advanced=None, client_ip=None, description=None, enable=None, group_id=None, host=None, id=None, ip_add_type=None, ip_group_id=None, ip_type=None, isolation_id=None, js_conf_id=None, name=None, policy=None, rule_tag=None, update_time=None, url=None, _configuration=None):  # noqa: E501
        """DatumForListAllowRuleOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._action = None
        self._add_src = None
        self._advanced = None
        self._client_ip = None
        self._description = None
        self._enable = None
        self._group_id = None
        self._host = None
        self._id = None
        self._ip_add_type = None
        self._ip_group_id = None
        self._ip_type = None
        self._isolation_id = None
        self._js_conf_id = None
        self._name = None
        self._policy = None
        self._rule_tag = None
        self._update_time = None
        self._url = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if add_src is not None:
            self.add_src = add_src
        if advanced is not None:
            self.advanced = advanced
        if client_ip is not None:
            self.client_ip = client_ip
        if description is not None:
            self.description = description
        if enable is not None:
            self.enable = enable
        if group_id is not None:
            self.group_id = group_id
        if host is not None:
            self.host = host
        if id is not None:
            self.id = id
        if ip_add_type is not None:
            self.ip_add_type = ip_add_type
        if ip_group_id is not None:
            self.ip_group_id = ip_group_id
        if ip_type is not None:
            self.ip_type = ip_type
        if isolation_id is not None:
            self.isolation_id = isolation_id
        if js_conf_id is not None:
            self.js_conf_id = js_conf_id
        if name is not None:
            self.name = name
        if policy is not None:
            self.policy = policy
        if rule_tag is not None:
            self.rule_tag = rule_tag
        if update_time is not None:
            self.update_time = update_time
        if url is not None:
            self.url = url

    @property
    def action(self):
        """Gets the action of this DatumForListAllowRuleOutput.  # noqa: E501


        :return: The action of this DatumForListAllowRuleOutput.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this DatumForListAllowRuleOutput.


        :param action: The action of this DatumForListAllowRuleOutput.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def add_src(self):
        """Gets the add_src of this DatumForListAllowRuleOutput.  # noqa: E501


        :return: The add_src of this DatumForListAllowRuleOutput.  # noqa: E501
        :rtype: int
        """
        return self._add_src

    @add_src.setter
    def add_src(self, add_src):
        """Sets the add_src of this DatumForListAllowRuleOutput.


        :param add_src: The add_src of this DatumForListAllowRuleOutput.  # noqa: E501
        :type: int
        """

        self._add_src = add_src

    @property
    def advanced(self):
        """Gets the advanced of this DatumForListAllowRuleOutput.  # noqa: E501


        :return: The advanced of this DatumForListAllowRuleOutput.  # noqa: E501
        :rtype: int
        """
        return self._advanced

    @advanced.setter
    def advanced(self, advanced):
        """Sets the advanced of this DatumForListAllowRuleOutput.


        :param advanced: The advanced of this DatumForListAllowRuleOutput.  # noqa: E501
        :type: int
        """

        self._advanced = advanced

    @property
    def client_ip(self):
        """Gets the client_ip of this DatumForListAllowRuleOutput.  # noqa: E501


        :return: The client_ip of this DatumForListAllowRuleOutput.  # noqa: E501
        :rtype: str
        """
        return self._client_ip

    @client_ip.setter
    def client_ip(self, client_ip):
        """Sets the client_ip of this DatumForListAllowRuleOutput.


        :param client_ip: The client_ip of this DatumForListAllowRuleOutput.  # noqa: E501
        :type: str
        """

        self._client_ip = client_ip

    @property
    def description(self):
        """Gets the description of this DatumForListAllowRuleOutput.  # noqa: E501


        :return: The description of this DatumForListAllowRuleOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DatumForListAllowRuleOutput.


        :param description: The description of this DatumForListAllowRuleOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def enable(self):
        """Gets the enable of this DatumForListAllowRuleOutput.  # noqa: E501


        :return: The enable of this DatumForListAllowRuleOutput.  # noqa: E501
        :rtype: int
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this DatumForListAllowRuleOutput.


        :param enable: The enable of this DatumForListAllowRuleOutput.  # noqa: E501
        :type: int
        """

        self._enable = enable

    @property
    def group_id(self):
        """Gets the group_id of this DatumForListAllowRuleOutput.  # noqa: E501


        :return: The group_id of this DatumForListAllowRuleOutput.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this DatumForListAllowRuleOutput.


        :param group_id: The group_id of this DatumForListAllowRuleOutput.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    @property
    def host(self):
        """Gets the host of this DatumForListAllowRuleOutput.  # noqa: E501


        :return: The host of this DatumForListAllowRuleOutput.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this DatumForListAllowRuleOutput.


        :param host: The host of this DatumForListAllowRuleOutput.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def id(self):
        """Gets the id of this DatumForListAllowRuleOutput.  # noqa: E501


        :return: The id of this DatumForListAllowRuleOutput.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DatumForListAllowRuleOutput.


        :param id: The id of this DatumForListAllowRuleOutput.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def ip_add_type(self):
        """Gets the ip_add_type of this DatumForListAllowRuleOutput.  # noqa: E501


        :return: The ip_add_type of this DatumForListAllowRuleOutput.  # noqa: E501
        :rtype: int
        """
        return self._ip_add_type

    @ip_add_type.setter
    def ip_add_type(self, ip_add_type):
        """Sets the ip_add_type of this DatumForListAllowRuleOutput.


        :param ip_add_type: The ip_add_type of this DatumForListAllowRuleOutput.  # noqa: E501
        :type: int
        """

        self._ip_add_type = ip_add_type

    @property
    def ip_group_id(self):
        """Gets the ip_group_id of this DatumForListAllowRuleOutput.  # noqa: E501


        :return: The ip_group_id of this DatumForListAllowRuleOutput.  # noqa: E501
        :rtype: int
        """
        return self._ip_group_id

    @ip_group_id.setter
    def ip_group_id(self, ip_group_id):
        """Sets the ip_group_id of this DatumForListAllowRuleOutput.


        :param ip_group_id: The ip_group_id of this DatumForListAllowRuleOutput.  # noqa: E501
        :type: int
        """

        self._ip_group_id = ip_group_id

    @property
    def ip_type(self):
        """Gets the ip_type of this DatumForListAllowRuleOutput.  # noqa: E501


        :return: The ip_type of this DatumForListAllowRuleOutput.  # noqa: E501
        :rtype: int
        """
        return self._ip_type

    @ip_type.setter
    def ip_type(self, ip_type):
        """Sets the ip_type of this DatumForListAllowRuleOutput.


        :param ip_type: The ip_type of this DatumForListAllowRuleOutput.  # noqa: E501
        :type: int
        """

        self._ip_type = ip_type

    @property
    def isolation_id(self):
        """Gets the isolation_id of this DatumForListAllowRuleOutput.  # noqa: E501


        :return: The isolation_id of this DatumForListAllowRuleOutput.  # noqa: E501
        :rtype: str
        """
        return self._isolation_id

    @isolation_id.setter
    def isolation_id(self, isolation_id):
        """Sets the isolation_id of this DatumForListAllowRuleOutput.


        :param isolation_id: The isolation_id of this DatumForListAllowRuleOutput.  # noqa: E501
        :type: str
        """

        self._isolation_id = isolation_id

    @property
    def js_conf_id(self):
        """Gets the js_conf_id of this DatumForListAllowRuleOutput.  # noqa: E501


        :return: The js_conf_id of this DatumForListAllowRuleOutput.  # noqa: E501
        :rtype: int
        """
        return self._js_conf_id

    @js_conf_id.setter
    def js_conf_id(self, js_conf_id):
        """Sets the js_conf_id of this DatumForListAllowRuleOutput.


        :param js_conf_id: The js_conf_id of this DatumForListAllowRuleOutput.  # noqa: E501
        :type: int
        """

        self._js_conf_id = js_conf_id

    @property
    def name(self):
        """Gets the name of this DatumForListAllowRuleOutput.  # noqa: E501


        :return: The name of this DatumForListAllowRuleOutput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DatumForListAllowRuleOutput.


        :param name: The name of this DatumForListAllowRuleOutput.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def policy(self):
        """Gets the policy of this DatumForListAllowRuleOutput.  # noqa: E501


        :return: The policy of this DatumForListAllowRuleOutput.  # noqa: E501
        :rtype: int
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this DatumForListAllowRuleOutput.


        :param policy: The policy of this DatumForListAllowRuleOutput.  # noqa: E501
        :type: int
        """

        self._policy = policy

    @property
    def rule_tag(self):
        """Gets the rule_tag of this DatumForListAllowRuleOutput.  # noqa: E501


        :return: The rule_tag of this DatumForListAllowRuleOutput.  # noqa: E501
        :rtype: str
        """
        return self._rule_tag

    @rule_tag.setter
    def rule_tag(self, rule_tag):
        """Sets the rule_tag of this DatumForListAllowRuleOutput.


        :param rule_tag: The rule_tag of this DatumForListAllowRuleOutput.  # noqa: E501
        :type: str
        """

        self._rule_tag = rule_tag

    @property
    def update_time(self):
        """Gets the update_time of this DatumForListAllowRuleOutput.  # noqa: E501


        :return: The update_time of this DatumForListAllowRuleOutput.  # noqa: E501
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this DatumForListAllowRuleOutput.


        :param update_time: The update_time of this DatumForListAllowRuleOutput.  # noqa: E501
        :type: str
        """

        self._update_time = update_time

    @property
    def url(self):
        """Gets the url of this DatumForListAllowRuleOutput.  # noqa: E501


        :return: The url of this DatumForListAllowRuleOutput.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this DatumForListAllowRuleOutput.


        :param url: The url of this DatumForListAllowRuleOutput.  # noqa: E501
        :type: str
        """

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
        if issubclass(DatumForListAllowRuleOutput, dict):
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
        if not isinstance(other, DatumForListAllowRuleOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DatumForListAllowRuleOutput):
            return True

        return self.to_dict() != other.to_dict()
