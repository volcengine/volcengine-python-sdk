# coding: utf-8

"""
    dms

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class UrlSourceConfigForCreateDataMigrateTaskInput(object):
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
        'bucket_access_config': 'BucketAccessConfigForCreateDataMigrateTaskInput',
        'is_url_try_range_get': 'bool',
        'url_list_link': 'str',
        'url_list_name': 'str'
    }

    attribute_map = {
        'bucket_access_config': 'BucketAccessConfig',
        'is_url_try_range_get': 'IsUrlTryRangeGet',
        'url_list_link': 'UrlListLink',
        'url_list_name': 'UrlListName'
    }

    def __init__(self, bucket_access_config=None, is_url_try_range_get=None, url_list_link=None, url_list_name=None, _configuration=None):  # noqa: E501
        """UrlSourceConfigForCreateDataMigrateTaskInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bucket_access_config = None
        self._is_url_try_range_get = None
        self._url_list_link = None
        self._url_list_name = None
        self.discriminator = None

        if bucket_access_config is not None:
            self.bucket_access_config = bucket_access_config
        if is_url_try_range_get is not None:
            self.is_url_try_range_get = is_url_try_range_get
        if url_list_link is not None:
            self.url_list_link = url_list_link
        if url_list_name is not None:
            self.url_list_name = url_list_name

    @property
    def bucket_access_config(self):
        """Gets the bucket_access_config of this UrlSourceConfigForCreateDataMigrateTaskInput.  # noqa: E501


        :return: The bucket_access_config of this UrlSourceConfigForCreateDataMigrateTaskInput.  # noqa: E501
        :rtype: BucketAccessConfigForCreateDataMigrateTaskInput
        """
        return self._bucket_access_config

    @bucket_access_config.setter
    def bucket_access_config(self, bucket_access_config):
        """Sets the bucket_access_config of this UrlSourceConfigForCreateDataMigrateTaskInput.


        :param bucket_access_config: The bucket_access_config of this UrlSourceConfigForCreateDataMigrateTaskInput.  # noqa: E501
        :type: BucketAccessConfigForCreateDataMigrateTaskInput
        """

        self._bucket_access_config = bucket_access_config

    @property
    def is_url_try_range_get(self):
        """Gets the is_url_try_range_get of this UrlSourceConfigForCreateDataMigrateTaskInput.  # noqa: E501


        :return: The is_url_try_range_get of this UrlSourceConfigForCreateDataMigrateTaskInput.  # noqa: E501
        :rtype: bool
        """
        return self._is_url_try_range_get

    @is_url_try_range_get.setter
    def is_url_try_range_get(self, is_url_try_range_get):
        """Sets the is_url_try_range_get of this UrlSourceConfigForCreateDataMigrateTaskInput.


        :param is_url_try_range_get: The is_url_try_range_get of this UrlSourceConfigForCreateDataMigrateTaskInput.  # noqa: E501
        :type: bool
        """

        self._is_url_try_range_get = is_url_try_range_get

    @property
    def url_list_link(self):
        """Gets the url_list_link of this UrlSourceConfigForCreateDataMigrateTaskInput.  # noqa: E501


        :return: The url_list_link of this UrlSourceConfigForCreateDataMigrateTaskInput.  # noqa: E501
        :rtype: str
        """
        return self._url_list_link

    @url_list_link.setter
    def url_list_link(self, url_list_link):
        """Sets the url_list_link of this UrlSourceConfigForCreateDataMigrateTaskInput.


        :param url_list_link: The url_list_link of this UrlSourceConfigForCreateDataMigrateTaskInput.  # noqa: E501
        :type: str
        """

        self._url_list_link = url_list_link

    @property
    def url_list_name(self):
        """Gets the url_list_name of this UrlSourceConfigForCreateDataMigrateTaskInput.  # noqa: E501


        :return: The url_list_name of this UrlSourceConfigForCreateDataMigrateTaskInput.  # noqa: E501
        :rtype: str
        """
        return self._url_list_name

    @url_list_name.setter
    def url_list_name(self, url_list_name):
        """Sets the url_list_name of this UrlSourceConfigForCreateDataMigrateTaskInput.


        :param url_list_name: The url_list_name of this UrlSourceConfigForCreateDataMigrateTaskInput.  # noqa: E501
        :type: str
        """

        self._url_list_name = url_list_name

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
        if issubclass(UrlSourceConfigForCreateDataMigrateTaskInput, dict):
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
        if not isinstance(other, UrlSourceConfigForCreateDataMigrateTaskInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UrlSourceConfigForCreateDataMigrateTaskInput):
            return True

        return self.to_dict() != other.to_dict()