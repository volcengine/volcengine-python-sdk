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


class CompressionActionForUpdateCdnConfigInput(object):
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
        'compression_format': 'str',
        'compression_target': 'str',
        'compression_type': 'list[str]',
        'max_file_size_kb': 'int',
        'min_file_size_kb': 'int'
    }

    attribute_map = {
        'compression_format': 'CompressionFormat',
        'compression_target': 'CompressionTarget',
        'compression_type': 'CompressionType',
        'max_file_size_kb': 'MaxFileSizeKB',
        'min_file_size_kb': 'MinFileSizeKB'
    }

    def __init__(self, compression_format=None, compression_target=None, compression_type=None, max_file_size_kb=None, min_file_size_kb=None, _configuration=None):  # noqa: E501
        """CompressionActionForUpdateCdnConfigInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._compression_format = None
        self._compression_target = None
        self._compression_type = None
        self._max_file_size_kb = None
        self._min_file_size_kb = None
        self.discriminator = None

        if compression_format is not None:
            self.compression_format = compression_format
        if compression_target is not None:
            self.compression_target = compression_target
        if compression_type is not None:
            self.compression_type = compression_type
        if max_file_size_kb is not None:
            self.max_file_size_kb = max_file_size_kb
        if min_file_size_kb is not None:
            self.min_file_size_kb = min_file_size_kb

    @property
    def compression_format(self):
        """Gets the compression_format of this CompressionActionForUpdateCdnConfigInput.  # noqa: E501


        :return: The compression_format of this CompressionActionForUpdateCdnConfigInput.  # noqa: E501
        :rtype: str
        """
        return self._compression_format

    @compression_format.setter
    def compression_format(self, compression_format):
        """Sets the compression_format of this CompressionActionForUpdateCdnConfigInput.


        :param compression_format: The compression_format of this CompressionActionForUpdateCdnConfigInput.  # noqa: E501
        :type: str
        """

        self._compression_format = compression_format

    @property
    def compression_target(self):
        """Gets the compression_target of this CompressionActionForUpdateCdnConfigInput.  # noqa: E501


        :return: The compression_target of this CompressionActionForUpdateCdnConfigInput.  # noqa: E501
        :rtype: str
        """
        return self._compression_target

    @compression_target.setter
    def compression_target(self, compression_target):
        """Sets the compression_target of this CompressionActionForUpdateCdnConfigInput.


        :param compression_target: The compression_target of this CompressionActionForUpdateCdnConfigInput.  # noqa: E501
        :type: str
        """

        self._compression_target = compression_target

    @property
    def compression_type(self):
        """Gets the compression_type of this CompressionActionForUpdateCdnConfigInput.  # noqa: E501


        :return: The compression_type of this CompressionActionForUpdateCdnConfigInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._compression_type

    @compression_type.setter
    def compression_type(self, compression_type):
        """Sets the compression_type of this CompressionActionForUpdateCdnConfigInput.


        :param compression_type: The compression_type of this CompressionActionForUpdateCdnConfigInput.  # noqa: E501
        :type: list[str]
        """

        self._compression_type = compression_type

    @property
    def max_file_size_kb(self):
        """Gets the max_file_size_kb of this CompressionActionForUpdateCdnConfigInput.  # noqa: E501


        :return: The max_file_size_kb of this CompressionActionForUpdateCdnConfigInput.  # noqa: E501
        :rtype: int
        """
        return self._max_file_size_kb

    @max_file_size_kb.setter
    def max_file_size_kb(self, max_file_size_kb):
        """Sets the max_file_size_kb of this CompressionActionForUpdateCdnConfigInput.


        :param max_file_size_kb: The max_file_size_kb of this CompressionActionForUpdateCdnConfigInput.  # noqa: E501
        :type: int
        """

        self._max_file_size_kb = max_file_size_kb

    @property
    def min_file_size_kb(self):
        """Gets the min_file_size_kb of this CompressionActionForUpdateCdnConfigInput.  # noqa: E501


        :return: The min_file_size_kb of this CompressionActionForUpdateCdnConfigInput.  # noqa: E501
        :rtype: int
        """
        return self._min_file_size_kb

    @min_file_size_kb.setter
    def min_file_size_kb(self, min_file_size_kb):
        """Sets the min_file_size_kb of this CompressionActionForUpdateCdnConfigInput.


        :param min_file_size_kb: The min_file_size_kb of this CompressionActionForUpdateCdnConfigInput.  # noqa: E501
        :type: int
        """

        self._min_file_size_kb = min_file_size_kb

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
        if issubclass(CompressionActionForUpdateCdnConfigInput, dict):
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
        if not isinstance(other, CompressionActionForUpdateCdnConfigInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CompressionActionForUpdateCdnConfigInput):
            return True

        return self.to_dict() != other.to_dict()
