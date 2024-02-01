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


class ListCustomPageRequest(object):
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
        'host': 'str',
        'page': 'str',
        'page_size': 'int'
    }

    attribute_map = {
        'host': 'Host',
        'page': 'Page',
        'page_size': 'PageSize'
    }

    def __init__(self, host=None, page=None, page_size=None, _configuration=None):  # noqa: E501
        """ListCustomPageRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._host = None
        self._page = None
        self._page_size = None
        self.discriminator = None

        self.host = host
        if page is not None:
            self.page = page
        if page_size is not None:
            self.page_size = page_size

    @property
    def host(self):
        """Gets the host of this ListCustomPageRequest.  # noqa: E501


        :return: The host of this ListCustomPageRequest.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this ListCustomPageRequest.


        :param host: The host of this ListCustomPageRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and host is None:
            raise ValueError("Invalid value for `host`, must not be `None`")  # noqa: E501

        self._host = host

    @property
    def page(self):
        """Gets the page of this ListCustomPageRequest.  # noqa: E501


        :return: The page of this ListCustomPageRequest.  # noqa: E501
        :rtype: str
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListCustomPageRequest.


        :param page: The page of this ListCustomPageRequest.  # noqa: E501
        :type: str
        """

        self._page = page

    @property
    def page_size(self):
        """Gets the page_size of this ListCustomPageRequest.  # noqa: E501


        :return: The page_size of this ListCustomPageRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ListCustomPageRequest.


        :param page_size: The page_size of this ListCustomPageRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

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
        if issubclass(ListCustomPageRequest, dict):
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
        if not isinstance(other, ListCustomPageRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListCustomPageRequest):
            return True

        return self.to_dict() != other.to_dict()
