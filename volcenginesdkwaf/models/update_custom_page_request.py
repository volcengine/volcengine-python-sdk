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


class UpdateCustomPageRequest(object):
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
        'accurate': 'AccurateForUpdateCustomPageInput',
        'advanced': 'int',
        'body': 'str',
        'client_ip': 'str',
        'code': 'int',
        'content_type': 'str',
        'description': 'str',
        'enable': 'int',
        'group_id': 'int',
        'host': 'str',
        'id': 'int',
        'name': 'str',
        'page_mode': 'int',
        'policy': 'int',
        'redirect_url': 'str',
        'url': 'str'
    }

    attribute_map = {
        'accurate': 'Accurate',
        'advanced': 'Advanced',
        'body': 'Body',
        'client_ip': 'ClientIp',
        'code': 'Code',
        'content_type': 'ContentType',
        'description': 'Description',
        'enable': 'Enable',
        'group_id': 'GroupId',
        'host': 'Host',
        'id': 'Id',
        'name': 'Name',
        'page_mode': 'PageMode',
        'policy': 'Policy',
        'redirect_url': 'RedirectUrl',
        'url': 'Url'
    }

    def __init__(self, accurate=None, advanced=None, body=None, client_ip=None, code=None, content_type=None, description=None, enable=None, group_id=None, host=None, id=None, name=None, page_mode=None, policy=None, redirect_url=None, url=None, _configuration=None):  # noqa: E501
        """UpdateCustomPageRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._accurate = None
        self._advanced = None
        self._body = None
        self._client_ip = None
        self._code = None
        self._content_type = None
        self._description = None
        self._enable = None
        self._group_id = None
        self._host = None
        self._id = None
        self._name = None
        self._page_mode = None
        self._policy = None
        self._redirect_url = None
        self._url = None
        self.discriminator = None

        if accurate is not None:
            self.accurate = accurate
        if advanced is not None:
            self.advanced = advanced
        if body is not None:
            self.body = body
        self.client_ip = client_ip
        self.code = code
        if content_type is not None:
            self.content_type = content_type
        if description is not None:
            self.description = description
        self.enable = enable
        if group_id is not None:
            self.group_id = group_id
        self.host = host
        self.id = id
        self.name = name
        self.page_mode = page_mode
        self.policy = policy
        if redirect_url is not None:
            self.redirect_url = redirect_url
        self.url = url

    @property
    def accurate(self):
        """Gets the accurate of this UpdateCustomPageRequest.  # noqa: E501


        :return: The accurate of this UpdateCustomPageRequest.  # noqa: E501
        :rtype: AccurateForUpdateCustomPageInput
        """
        return self._accurate

    @accurate.setter
    def accurate(self, accurate):
        """Sets the accurate of this UpdateCustomPageRequest.


        :param accurate: The accurate of this UpdateCustomPageRequest.  # noqa: E501
        :type: AccurateForUpdateCustomPageInput
        """

        self._accurate = accurate

    @property
    def advanced(self):
        """Gets the advanced of this UpdateCustomPageRequest.  # noqa: E501


        :return: The advanced of this UpdateCustomPageRequest.  # noqa: E501
        :rtype: int
        """
        return self._advanced

    @advanced.setter
    def advanced(self, advanced):
        """Sets the advanced of this UpdateCustomPageRequest.


        :param advanced: The advanced of this UpdateCustomPageRequest.  # noqa: E501
        :type: int
        """

        self._advanced = advanced

    @property
    def body(self):
        """Gets the body of this UpdateCustomPageRequest.  # noqa: E501


        :return: The body of this UpdateCustomPageRequest.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateCustomPageRequest.


        :param body: The body of this UpdateCustomPageRequest.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def client_ip(self):
        """Gets the client_ip of this UpdateCustomPageRequest.  # noqa: E501


        :return: The client_ip of this UpdateCustomPageRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_ip

    @client_ip.setter
    def client_ip(self, client_ip):
        """Sets the client_ip of this UpdateCustomPageRequest.


        :param client_ip: The client_ip of this UpdateCustomPageRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and client_ip is None:
            raise ValueError("Invalid value for `client_ip`, must not be `None`")  # noqa: E501

        self._client_ip = client_ip

    @property
    def code(self):
        """Gets the code of this UpdateCustomPageRequest.  # noqa: E501


        :return: The code of this UpdateCustomPageRequest.  # noqa: E501
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this UpdateCustomPageRequest.


        :param code: The code of this UpdateCustomPageRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def content_type(self):
        """Gets the content_type of this UpdateCustomPageRequest.  # noqa: E501


        :return: The content_type of this UpdateCustomPageRequest.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this UpdateCustomPageRequest.


        :param content_type: The content_type of this UpdateCustomPageRequest.  # noqa: E501
        :type: str
        """

        self._content_type = content_type

    @property
    def description(self):
        """Gets the description of this UpdateCustomPageRequest.  # noqa: E501


        :return: The description of this UpdateCustomPageRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateCustomPageRequest.


        :param description: The description of this UpdateCustomPageRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def enable(self):
        """Gets the enable of this UpdateCustomPageRequest.  # noqa: E501


        :return: The enable of this UpdateCustomPageRequest.  # noqa: E501
        :rtype: int
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this UpdateCustomPageRequest.


        :param enable: The enable of this UpdateCustomPageRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and enable is None:
            raise ValueError("Invalid value for `enable`, must not be `None`")  # noqa: E501

        self._enable = enable

    @property
    def group_id(self):
        """Gets the group_id of this UpdateCustomPageRequest.  # noqa: E501


        :return: The group_id of this UpdateCustomPageRequest.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this UpdateCustomPageRequest.


        :param group_id: The group_id of this UpdateCustomPageRequest.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    @property
    def host(self):
        """Gets the host of this UpdateCustomPageRequest.  # noqa: E501


        :return: The host of this UpdateCustomPageRequest.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this UpdateCustomPageRequest.


        :param host: The host of this UpdateCustomPageRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and host is None:
            raise ValueError("Invalid value for `host`, must not be `None`")  # noqa: E501

        self._host = host

    @property
    def id(self):
        """Gets the id of this UpdateCustomPageRequest.  # noqa: E501


        :return: The id of this UpdateCustomPageRequest.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateCustomPageRequest.


        :param id: The id of this UpdateCustomPageRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this UpdateCustomPageRequest.  # noqa: E501


        :return: The name of this UpdateCustomPageRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateCustomPageRequest.


        :param name: The name of this UpdateCustomPageRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def page_mode(self):
        """Gets the page_mode of this UpdateCustomPageRequest.  # noqa: E501


        :return: The page_mode of this UpdateCustomPageRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_mode

    @page_mode.setter
    def page_mode(self, page_mode):
        """Sets the page_mode of this UpdateCustomPageRequest.


        :param page_mode: The page_mode of this UpdateCustomPageRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and page_mode is None:
            raise ValueError("Invalid value for `page_mode`, must not be `None`")  # noqa: E501

        self._page_mode = page_mode

    @property
    def policy(self):
        """Gets the policy of this UpdateCustomPageRequest.  # noqa: E501


        :return: The policy of this UpdateCustomPageRequest.  # noqa: E501
        :rtype: int
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this UpdateCustomPageRequest.


        :param policy: The policy of this UpdateCustomPageRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and policy is None:
            raise ValueError("Invalid value for `policy`, must not be `None`")  # noqa: E501

        self._policy = policy

    @property
    def redirect_url(self):
        """Gets the redirect_url of this UpdateCustomPageRequest.  # noqa: E501


        :return: The redirect_url of this UpdateCustomPageRequest.  # noqa: E501
        :rtype: str
        """
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, redirect_url):
        """Sets the redirect_url of this UpdateCustomPageRequest.


        :param redirect_url: The redirect_url of this UpdateCustomPageRequest.  # noqa: E501
        :type: str
        """

        self._redirect_url = redirect_url

    @property
    def url(self):
        """Gets the url of this UpdateCustomPageRequest.  # noqa: E501


        :return: The url of this UpdateCustomPageRequest.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this UpdateCustomPageRequest.


        :param url: The url of this UpdateCustomPageRequest.  # noqa: E501
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
        if issubclass(UpdateCustomPageRequest, dict):
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
        if not isinstance(other, UpdateCustomPageRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateCustomPageRequest):
            return True

        return self.to_dict() != other.to_dict()
