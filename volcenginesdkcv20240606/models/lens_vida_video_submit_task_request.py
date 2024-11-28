# coding: utf-8

"""
    cv20240606

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class LensVidaVideoSubmitTaskRequest(object):
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
        'req_key': 'str',
        'url': 'str',
        'vida_mode': 'str'
    }

    attribute_map = {
        'req_key': 'req_key',
        'url': 'url',
        'vida_mode': 'vida_mode'
    }

    def __init__(self, req_key=None, url=None, vida_mode=None, _configuration=None):  # noqa: E501
        """LensVidaVideoSubmitTaskRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._req_key = None
        self._url = None
        self._vida_mode = None
        self.discriminator = None

        self.req_key = req_key
        self.url = url
        self.vida_mode = vida_mode

    @property
    def req_key(self):
        """Gets the req_key of this LensVidaVideoSubmitTaskRequest.  # noqa: E501


        :return: The req_key of this LensVidaVideoSubmitTaskRequest.  # noqa: E501
        :rtype: str
        """
        return self._req_key

    @req_key.setter
    def req_key(self, req_key):
        """Sets the req_key of this LensVidaVideoSubmitTaskRequest.


        :param req_key: The req_key of this LensVidaVideoSubmitTaskRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and req_key is None:
            raise ValueError("Invalid value for `req_key`, must not be `None`")  # noqa: E501

        self._req_key = req_key

    @property
    def url(self):
        """Gets the url of this LensVidaVideoSubmitTaskRequest.  # noqa: E501


        :return: The url of this LensVidaVideoSubmitTaskRequest.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this LensVidaVideoSubmitTaskRequest.


        :param url: The url of this LensVidaVideoSubmitTaskRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def vida_mode(self):
        """Gets the vida_mode of this LensVidaVideoSubmitTaskRequest.  # noqa: E501


        :return: The vida_mode of this LensVidaVideoSubmitTaskRequest.  # noqa: E501
        :rtype: str
        """
        return self._vida_mode

    @vida_mode.setter
    def vida_mode(self, vida_mode):
        """Sets the vida_mode of this LensVidaVideoSubmitTaskRequest.


        :param vida_mode: The vida_mode of this LensVidaVideoSubmitTaskRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and vida_mode is None:
            raise ValueError("Invalid value for `vida_mode`, must not be `None`")  # noqa: E501

        self._vida_mode = vida_mode

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
        if issubclass(LensVidaVideoSubmitTaskRequest, dict):
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
        if not isinstance(other, LensVidaVideoSubmitTaskRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LensVidaVideoSubmitTaskRequest):
            return True

        return self.to_dict() != other.to_dict()
