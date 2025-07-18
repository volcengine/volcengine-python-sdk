# coding: utf-8

"""
    livesaas

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class GetWebPushLiveClientAPIResponse(object):
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
        'expire_time': 'int',
        'tmp_url': 'str',
        'url': 'str'
    }

    attribute_map = {
        'expire_time': 'ExpireTime',
        'tmp_url': 'TmpUrl',
        'url': 'Url'
    }

    def __init__(self, expire_time=None, tmp_url=None, url=None, _configuration=None):  # noqa: E501
        """GetWebPushLiveClientAPIResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._expire_time = None
        self._tmp_url = None
        self._url = None
        self.discriminator = None

        if expire_time is not None:
            self.expire_time = expire_time
        if tmp_url is not None:
            self.tmp_url = tmp_url
        if url is not None:
            self.url = url

    @property
    def expire_time(self):
        """Gets the expire_time of this GetWebPushLiveClientAPIResponse.  # noqa: E501


        :return: The expire_time of this GetWebPushLiveClientAPIResponse.  # noqa: E501
        :rtype: int
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this GetWebPushLiveClientAPIResponse.


        :param expire_time: The expire_time of this GetWebPushLiveClientAPIResponse.  # noqa: E501
        :type: int
        """

        self._expire_time = expire_time

    @property
    def tmp_url(self):
        """Gets the tmp_url of this GetWebPushLiveClientAPIResponse.  # noqa: E501


        :return: The tmp_url of this GetWebPushLiveClientAPIResponse.  # noqa: E501
        :rtype: str
        """
        return self._tmp_url

    @tmp_url.setter
    def tmp_url(self, tmp_url):
        """Sets the tmp_url of this GetWebPushLiveClientAPIResponse.


        :param tmp_url: The tmp_url of this GetWebPushLiveClientAPIResponse.  # noqa: E501
        :type: str
        """

        self._tmp_url = tmp_url

    @property
    def url(self):
        """Gets the url of this GetWebPushLiveClientAPIResponse.  # noqa: E501


        :return: The url of this GetWebPushLiveClientAPIResponse.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this GetWebPushLiveClientAPIResponse.


        :param url: The url of this GetWebPushLiveClientAPIResponse.  # noqa: E501
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
        if issubclass(GetWebPushLiveClientAPIResponse, dict):
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
        if not isinstance(other, GetWebPushLiveClientAPIResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetWebPushLiveClientAPIResponse):
            return True

        return self.to_dict() != other.to_dict()
