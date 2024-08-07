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


class ObjectSourceConfigForCreateDataMigrateTaskInput(object):
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
        'key_list_file': 'str',
        'prefix_list': 'list[str]',
        'prefix_list_file': 'str',
        'scan_with_delimiter': 'bool'
    }

    attribute_map = {
        'bucket_access_config': 'BucketAccessConfig',
        'key_list_file': 'KeyListFile',
        'prefix_list': 'PrefixList',
        'prefix_list_file': 'PrefixListFile',
        'scan_with_delimiter': 'ScanWithDelimiter'
    }

    def __init__(self, bucket_access_config=None, key_list_file=None, prefix_list=None, prefix_list_file=None, scan_with_delimiter=None, _configuration=None):  # noqa: E501
        """ObjectSourceConfigForCreateDataMigrateTaskInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bucket_access_config = None
        self._key_list_file = None
        self._prefix_list = None
        self._prefix_list_file = None
        self._scan_with_delimiter = None
        self.discriminator = None

        if bucket_access_config is not None:
            self.bucket_access_config = bucket_access_config
        if key_list_file is not None:
            self.key_list_file = key_list_file
        if prefix_list is not None:
            self.prefix_list = prefix_list
        if prefix_list_file is not None:
            self.prefix_list_file = prefix_list_file
        if scan_with_delimiter is not None:
            self.scan_with_delimiter = scan_with_delimiter

    @property
    def bucket_access_config(self):
        """Gets the bucket_access_config of this ObjectSourceConfigForCreateDataMigrateTaskInput.  # noqa: E501


        :return: The bucket_access_config of this ObjectSourceConfigForCreateDataMigrateTaskInput.  # noqa: E501
        :rtype: BucketAccessConfigForCreateDataMigrateTaskInput
        """
        return self._bucket_access_config

    @bucket_access_config.setter
    def bucket_access_config(self, bucket_access_config):
        """Sets the bucket_access_config of this ObjectSourceConfigForCreateDataMigrateTaskInput.


        :param bucket_access_config: The bucket_access_config of this ObjectSourceConfigForCreateDataMigrateTaskInput.  # noqa: E501
        :type: BucketAccessConfigForCreateDataMigrateTaskInput
        """

        self._bucket_access_config = bucket_access_config

    @property
    def key_list_file(self):
        """Gets the key_list_file of this ObjectSourceConfigForCreateDataMigrateTaskInput.  # noqa: E501


        :return: The key_list_file of this ObjectSourceConfigForCreateDataMigrateTaskInput.  # noqa: E501
        :rtype: str
        """
        return self._key_list_file

    @key_list_file.setter
    def key_list_file(self, key_list_file):
        """Sets the key_list_file of this ObjectSourceConfigForCreateDataMigrateTaskInput.


        :param key_list_file: The key_list_file of this ObjectSourceConfigForCreateDataMigrateTaskInput.  # noqa: E501
        :type: str
        """

        self._key_list_file = key_list_file

    @property
    def prefix_list(self):
        """Gets the prefix_list of this ObjectSourceConfigForCreateDataMigrateTaskInput.  # noqa: E501


        :return: The prefix_list of this ObjectSourceConfigForCreateDataMigrateTaskInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._prefix_list

    @prefix_list.setter
    def prefix_list(self, prefix_list):
        """Sets the prefix_list of this ObjectSourceConfigForCreateDataMigrateTaskInput.


        :param prefix_list: The prefix_list of this ObjectSourceConfigForCreateDataMigrateTaskInput.  # noqa: E501
        :type: list[str]
        """

        self._prefix_list = prefix_list

    @property
    def prefix_list_file(self):
        """Gets the prefix_list_file of this ObjectSourceConfigForCreateDataMigrateTaskInput.  # noqa: E501


        :return: The prefix_list_file of this ObjectSourceConfigForCreateDataMigrateTaskInput.  # noqa: E501
        :rtype: str
        """
        return self._prefix_list_file

    @prefix_list_file.setter
    def prefix_list_file(self, prefix_list_file):
        """Sets the prefix_list_file of this ObjectSourceConfigForCreateDataMigrateTaskInput.


        :param prefix_list_file: The prefix_list_file of this ObjectSourceConfigForCreateDataMigrateTaskInput.  # noqa: E501
        :type: str
        """

        self._prefix_list_file = prefix_list_file

    @property
    def scan_with_delimiter(self):
        """Gets the scan_with_delimiter of this ObjectSourceConfigForCreateDataMigrateTaskInput.  # noqa: E501


        :return: The scan_with_delimiter of this ObjectSourceConfigForCreateDataMigrateTaskInput.  # noqa: E501
        :rtype: bool
        """
        return self._scan_with_delimiter

    @scan_with_delimiter.setter
    def scan_with_delimiter(self, scan_with_delimiter):
        """Sets the scan_with_delimiter of this ObjectSourceConfigForCreateDataMigrateTaskInput.


        :param scan_with_delimiter: The scan_with_delimiter of this ObjectSourceConfigForCreateDataMigrateTaskInput.  # noqa: E501
        :type: bool
        """

        self._scan_with_delimiter = scan_with_delimiter

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
        if issubclass(ObjectSourceConfigForCreateDataMigrateTaskInput, dict):
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
        if not isinstance(other, ObjectSourceConfigForCreateDataMigrateTaskInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ObjectSourceConfigForCreateDataMigrateTaskInput):
            return True

        return self.to_dict() != other.to_dict()
