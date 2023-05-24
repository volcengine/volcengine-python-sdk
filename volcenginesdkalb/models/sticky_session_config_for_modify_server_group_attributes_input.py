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


class StickySessionConfigForModifyServerGroupAttributesInput(object):
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
        'cookie': 'str',
        'cookie_timeout': 'str',
        'sticky_session_enabled': 'str',
        'sticky_session_type': 'str'
    }

    attribute_map = {
        'cookie': 'Cookie',
        'cookie_timeout': 'CookieTimeout',
        'sticky_session_enabled': 'StickySessionEnabled',
        'sticky_session_type': 'StickySessionType'
    }

    def __init__(self, cookie=None, cookie_timeout=None, sticky_session_enabled=None, sticky_session_type=None, _configuration=None):  # noqa: E501
        """StickySessionConfigForModifyServerGroupAttributesInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cookie = None
        self._cookie_timeout = None
        self._sticky_session_enabled = None
        self._sticky_session_type = None
        self.discriminator = None

        if cookie is not None:
            self.cookie = cookie
        if cookie_timeout is not None:
            self.cookie_timeout = cookie_timeout
        if sticky_session_enabled is not None:
            self.sticky_session_enabled = sticky_session_enabled
        if sticky_session_type is not None:
            self.sticky_session_type = sticky_session_type

    @property
    def cookie(self):
        """Gets the cookie of this StickySessionConfigForModifyServerGroupAttributesInput.  # noqa: E501


        :return: The cookie of this StickySessionConfigForModifyServerGroupAttributesInput.  # noqa: E501
        :rtype: str
        """
        return self._cookie

    @cookie.setter
    def cookie(self, cookie):
        """Sets the cookie of this StickySessionConfigForModifyServerGroupAttributesInput.


        :param cookie: The cookie of this StickySessionConfigForModifyServerGroupAttributesInput.  # noqa: E501
        :type: str
        """

        self._cookie = cookie

    @property
    def cookie_timeout(self):
        """Gets the cookie_timeout of this StickySessionConfigForModifyServerGroupAttributesInput.  # noqa: E501


        :return: The cookie_timeout of this StickySessionConfigForModifyServerGroupAttributesInput.  # noqa: E501
        :rtype: str
        """
        return self._cookie_timeout

    @cookie_timeout.setter
    def cookie_timeout(self, cookie_timeout):
        """Sets the cookie_timeout of this StickySessionConfigForModifyServerGroupAttributesInput.


        :param cookie_timeout: The cookie_timeout of this StickySessionConfigForModifyServerGroupAttributesInput.  # noqa: E501
        :type: str
        """

        self._cookie_timeout = cookie_timeout

    @property
    def sticky_session_enabled(self):
        """Gets the sticky_session_enabled of this StickySessionConfigForModifyServerGroupAttributesInput.  # noqa: E501


        :return: The sticky_session_enabled of this StickySessionConfigForModifyServerGroupAttributesInput.  # noqa: E501
        :rtype: str
        """
        return self._sticky_session_enabled

    @sticky_session_enabled.setter
    def sticky_session_enabled(self, sticky_session_enabled):
        """Sets the sticky_session_enabled of this StickySessionConfigForModifyServerGroupAttributesInput.


        :param sticky_session_enabled: The sticky_session_enabled of this StickySessionConfigForModifyServerGroupAttributesInput.  # noqa: E501
        :type: str
        """

        self._sticky_session_enabled = sticky_session_enabled

    @property
    def sticky_session_type(self):
        """Gets the sticky_session_type of this StickySessionConfigForModifyServerGroupAttributesInput.  # noqa: E501


        :return: The sticky_session_type of this StickySessionConfigForModifyServerGroupAttributesInput.  # noqa: E501
        :rtype: str
        """
        return self._sticky_session_type

    @sticky_session_type.setter
    def sticky_session_type(self, sticky_session_type):
        """Sets the sticky_session_type of this StickySessionConfigForModifyServerGroupAttributesInput.


        :param sticky_session_type: The sticky_session_type of this StickySessionConfigForModifyServerGroupAttributesInput.  # noqa: E501
        :type: str
        """

        self._sticky_session_type = sticky_session_type

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
        if issubclass(StickySessionConfigForModifyServerGroupAttributesInput, dict):
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
        if not isinstance(other, StickySessionConfigForModifyServerGroupAttributesInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StickySessionConfigForModifyServerGroupAttributesInput):
            return True

        return self.to_dict() != other.to_dict()
