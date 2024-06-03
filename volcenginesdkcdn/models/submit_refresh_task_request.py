# coding: utf-8

"""
    cdn

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class SubmitRefreshTaskRequest(object):
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
        'delete': 'bool',
        'prefix': 'bool',
        'type': 'str',
        'urls': 'str'
    }

    attribute_map = {
        'delete': 'Delete',
        'prefix': 'Prefix',
        'type': 'Type',
        'urls': 'Urls'
    }

    def __init__(self, delete=None, prefix=None, type=None, urls=None, _configuration=None):  # noqa: E501
        """SubmitRefreshTaskRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._delete = None
        self._prefix = None
        self._type = None
        self._urls = None
        self.discriminator = None

        if delete is not None:
            self.delete = delete
        if prefix is not None:
            self.prefix = prefix
        if type is not None:
            self.type = type
        self.urls = urls

    @property
    def delete(self):
        """Gets the delete of this SubmitRefreshTaskRequest.  # noqa: E501


        :return: The delete of this SubmitRefreshTaskRequest.  # noqa: E501
        :rtype: bool
        """
        return self._delete

    @delete.setter
    def delete(self, delete):
        """Sets the delete of this SubmitRefreshTaskRequest.


        :param delete: The delete of this SubmitRefreshTaskRequest.  # noqa: E501
        :type: bool
        """

        self._delete = delete

    @property
    def prefix(self):
        """Gets the prefix of this SubmitRefreshTaskRequest.  # noqa: E501


        :return: The prefix of this SubmitRefreshTaskRequest.  # noqa: E501
        :rtype: bool
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this SubmitRefreshTaskRequest.


        :param prefix: The prefix of this SubmitRefreshTaskRequest.  # noqa: E501
        :type: bool
        """

        self._prefix = prefix

    @property
    def type(self):
        """Gets the type of this SubmitRefreshTaskRequest.  # noqa: E501


        :return: The type of this SubmitRefreshTaskRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SubmitRefreshTaskRequest.


        :param type: The type of this SubmitRefreshTaskRequest.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def urls(self):
        """Gets the urls of this SubmitRefreshTaskRequest.  # noqa: E501


        :return: The urls of this SubmitRefreshTaskRequest.  # noqa: E501
        :rtype: str
        """
        return self._urls

    @urls.setter
    def urls(self, urls):
        """Sets the urls of this SubmitRefreshTaskRequest.


        :param urls: The urls of this SubmitRefreshTaskRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and urls is None:
            raise ValueError("Invalid value for `urls`, must not be `None`")  # noqa: E501

        self._urls = urls

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
        if issubclass(SubmitRefreshTaskRequest, dict):
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
        if not isinstance(other, SubmitRefreshTaskRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SubmitRefreshTaskRequest):
            return True

        return self.to_dict() != other.to_dict()