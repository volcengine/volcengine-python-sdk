# coding: utf-8

"""
    seccenter20240508

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ListWeakPasswordCheckDetailRequest(object):
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
        'agent_id': 'str',
        'baseline_id': 'int',
        'check_name': 'str',
        'cloud_providers': 'list[str]',
        'hostname': 'str',
        'ip': 'str',
        'leaf_group_ids': 'list[str]',
        'page_number': 'int',
        'page_size': 'int',
        'sort_by': 'str',
        'sort_order': 'str',
        'tag': 'list[str]',
        'top_group_id': 'str'
    }

    attribute_map = {
        'agent_id': 'AgentID',
        'baseline_id': 'BaselineID',
        'check_name': 'CheckName',
        'cloud_providers': 'CloudProviders',
        'hostname': 'Hostname',
        'ip': 'IP',
        'leaf_group_ids': 'LeafGroupIDs',
        'page_number': 'PageNumber',
        'page_size': 'PageSize',
        'sort_by': 'SortBy',
        'sort_order': 'SortOrder',
        'tag': 'Tag',
        'top_group_id': 'TopGroupID'
    }

    def __init__(self, agent_id=None, baseline_id=None, check_name=None, cloud_providers=None, hostname=None, ip=None, leaf_group_ids=None, page_number=None, page_size=None, sort_by=None, sort_order=None, tag=None, top_group_id=None, _configuration=None):  # noqa: E501
        """ListWeakPasswordCheckDetailRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._agent_id = None
        self._baseline_id = None
        self._check_name = None
        self._cloud_providers = None
        self._hostname = None
        self._ip = None
        self._leaf_group_ids = None
        self._page_number = None
        self._page_size = None
        self._sort_by = None
        self._sort_order = None
        self._tag = None
        self._top_group_id = None
        self.discriminator = None

        if agent_id is not None:
            self.agent_id = agent_id
        self.baseline_id = baseline_id
        if check_name is not None:
            self.check_name = check_name
        if cloud_providers is not None:
            self.cloud_providers = cloud_providers
        if hostname is not None:
            self.hostname = hostname
        if ip is not None:
            self.ip = ip
        if leaf_group_ids is not None:
            self.leaf_group_ids = leaf_group_ids
        self.page_number = page_number
        self.page_size = page_size
        if sort_by is not None:
            self.sort_by = sort_by
        if sort_order is not None:
            self.sort_order = sort_order
        if tag is not None:
            self.tag = tag
        if top_group_id is not None:
            self.top_group_id = top_group_id

    @property
    def agent_id(self):
        """Gets the agent_id of this ListWeakPasswordCheckDetailRequest.  # noqa: E501


        :return: The agent_id of this ListWeakPasswordCheckDetailRequest.  # noqa: E501
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """Sets the agent_id of this ListWeakPasswordCheckDetailRequest.


        :param agent_id: The agent_id of this ListWeakPasswordCheckDetailRequest.  # noqa: E501
        :type: str
        """

        self._agent_id = agent_id

    @property
    def baseline_id(self):
        """Gets the baseline_id of this ListWeakPasswordCheckDetailRequest.  # noqa: E501


        :return: The baseline_id of this ListWeakPasswordCheckDetailRequest.  # noqa: E501
        :rtype: int
        """
        return self._baseline_id

    @baseline_id.setter
    def baseline_id(self, baseline_id):
        """Sets the baseline_id of this ListWeakPasswordCheckDetailRequest.


        :param baseline_id: The baseline_id of this ListWeakPasswordCheckDetailRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and baseline_id is None:
            raise ValueError("Invalid value for `baseline_id`, must not be `None`")  # noqa: E501

        self._baseline_id = baseline_id

    @property
    def check_name(self):
        """Gets the check_name of this ListWeakPasswordCheckDetailRequest.  # noqa: E501


        :return: The check_name of this ListWeakPasswordCheckDetailRequest.  # noqa: E501
        :rtype: str
        """
        return self._check_name

    @check_name.setter
    def check_name(self, check_name):
        """Sets the check_name of this ListWeakPasswordCheckDetailRequest.


        :param check_name: The check_name of this ListWeakPasswordCheckDetailRequest.  # noqa: E501
        :type: str
        """

        self._check_name = check_name

    @property
    def cloud_providers(self):
        """Gets the cloud_providers of this ListWeakPasswordCheckDetailRequest.  # noqa: E501


        :return: The cloud_providers of this ListWeakPasswordCheckDetailRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._cloud_providers

    @cloud_providers.setter
    def cloud_providers(self, cloud_providers):
        """Sets the cloud_providers of this ListWeakPasswordCheckDetailRequest.


        :param cloud_providers: The cloud_providers of this ListWeakPasswordCheckDetailRequest.  # noqa: E501
        :type: list[str]
        """

        self._cloud_providers = cloud_providers

    @property
    def hostname(self):
        """Gets the hostname of this ListWeakPasswordCheckDetailRequest.  # noqa: E501


        :return: The hostname of this ListWeakPasswordCheckDetailRequest.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this ListWeakPasswordCheckDetailRequest.


        :param hostname: The hostname of this ListWeakPasswordCheckDetailRequest.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def ip(self):
        """Gets the ip of this ListWeakPasswordCheckDetailRequest.  # noqa: E501


        :return: The ip of this ListWeakPasswordCheckDetailRequest.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this ListWeakPasswordCheckDetailRequest.


        :param ip: The ip of this ListWeakPasswordCheckDetailRequest.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def leaf_group_ids(self):
        """Gets the leaf_group_ids of this ListWeakPasswordCheckDetailRequest.  # noqa: E501


        :return: The leaf_group_ids of this ListWeakPasswordCheckDetailRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._leaf_group_ids

    @leaf_group_ids.setter
    def leaf_group_ids(self, leaf_group_ids):
        """Sets the leaf_group_ids of this ListWeakPasswordCheckDetailRequest.


        :param leaf_group_ids: The leaf_group_ids of this ListWeakPasswordCheckDetailRequest.  # noqa: E501
        :type: list[str]
        """

        self._leaf_group_ids = leaf_group_ids

    @property
    def page_number(self):
        """Gets the page_number of this ListWeakPasswordCheckDetailRequest.  # noqa: E501


        :return: The page_number of this ListWeakPasswordCheckDetailRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this ListWeakPasswordCheckDetailRequest.


        :param page_number: The page_number of this ListWeakPasswordCheckDetailRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and page_number is None:
            raise ValueError("Invalid value for `page_number`, must not be `None`")  # noqa: E501

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this ListWeakPasswordCheckDetailRequest.  # noqa: E501


        :return: The page_size of this ListWeakPasswordCheckDetailRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ListWeakPasswordCheckDetailRequest.


        :param page_size: The page_size of this ListWeakPasswordCheckDetailRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and page_size is None:
            raise ValueError("Invalid value for `page_size`, must not be `None`")  # noqa: E501

        self._page_size = page_size

    @property
    def sort_by(self):
        """Gets the sort_by of this ListWeakPasswordCheckDetailRequest.  # noqa: E501


        :return: The sort_by of this ListWeakPasswordCheckDetailRequest.  # noqa: E501
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        """Sets the sort_by of this ListWeakPasswordCheckDetailRequest.


        :param sort_by: The sort_by of this ListWeakPasswordCheckDetailRequest.  # noqa: E501
        :type: str
        """

        self._sort_by = sort_by

    @property
    def sort_order(self):
        """Gets the sort_order of this ListWeakPasswordCheckDetailRequest.  # noqa: E501


        :return: The sort_order of this ListWeakPasswordCheckDetailRequest.  # noqa: E501
        :rtype: str
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this ListWeakPasswordCheckDetailRequest.


        :param sort_order: The sort_order of this ListWeakPasswordCheckDetailRequest.  # noqa: E501
        :type: str
        """

        self._sort_order = sort_order

    @property
    def tag(self):
        """Gets the tag of this ListWeakPasswordCheckDetailRequest.  # noqa: E501


        :return: The tag of this ListWeakPasswordCheckDetailRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this ListWeakPasswordCheckDetailRequest.


        :param tag: The tag of this ListWeakPasswordCheckDetailRequest.  # noqa: E501
        :type: list[str]
        """

        self._tag = tag

    @property
    def top_group_id(self):
        """Gets the top_group_id of this ListWeakPasswordCheckDetailRequest.  # noqa: E501


        :return: The top_group_id of this ListWeakPasswordCheckDetailRequest.  # noqa: E501
        :rtype: str
        """
        return self._top_group_id

    @top_group_id.setter
    def top_group_id(self, top_group_id):
        """Sets the top_group_id of this ListWeakPasswordCheckDetailRequest.


        :param top_group_id: The top_group_id of this ListWeakPasswordCheckDetailRequest.  # noqa: E501
        :type: str
        """

        self._top_group_id = top_group_id

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
        if issubclass(ListWeakPasswordCheckDetailRequest, dict):
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
        if not isinstance(other, ListWeakPasswordCheckDetailRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListWeakPasswordCheckDetailRequest):
            return True

        return self.to_dict() != other.to_dict()
