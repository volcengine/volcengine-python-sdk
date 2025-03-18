# coding: utf-8

"""
    vefaas

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class UpdateFunctionResourceResponse(object):
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
        'id': 'str',
        'max_instance': 'int',
        'min_instance': 'int',
        'reserved_frozen_instance': 'int'
    }

    attribute_map = {
        'id': 'Id',
        'max_instance': 'MaxInstance',
        'min_instance': 'MinInstance',
        'reserved_frozen_instance': 'ReservedFrozenInstance'
    }

    def __init__(self, id=None, max_instance=None, min_instance=None, reserved_frozen_instance=None, _configuration=None):  # noqa: E501
        """UpdateFunctionResourceResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._max_instance = None
        self._min_instance = None
        self._reserved_frozen_instance = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if max_instance is not None:
            self.max_instance = max_instance
        if min_instance is not None:
            self.min_instance = min_instance
        if reserved_frozen_instance is not None:
            self.reserved_frozen_instance = reserved_frozen_instance

    @property
    def id(self):
        """Gets the id of this UpdateFunctionResourceResponse.  # noqa: E501


        :return: The id of this UpdateFunctionResourceResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateFunctionResourceResponse.


        :param id: The id of this UpdateFunctionResourceResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def max_instance(self):
        """Gets the max_instance of this UpdateFunctionResourceResponse.  # noqa: E501


        :return: The max_instance of this UpdateFunctionResourceResponse.  # noqa: E501
        :rtype: int
        """
        return self._max_instance

    @max_instance.setter
    def max_instance(self, max_instance):
        """Sets the max_instance of this UpdateFunctionResourceResponse.


        :param max_instance: The max_instance of this UpdateFunctionResourceResponse.  # noqa: E501
        :type: int
        """

        self._max_instance = max_instance

    @property
    def min_instance(self):
        """Gets the min_instance of this UpdateFunctionResourceResponse.  # noqa: E501


        :return: The min_instance of this UpdateFunctionResourceResponse.  # noqa: E501
        :rtype: int
        """
        return self._min_instance

    @min_instance.setter
    def min_instance(self, min_instance):
        """Sets the min_instance of this UpdateFunctionResourceResponse.


        :param min_instance: The min_instance of this UpdateFunctionResourceResponse.  # noqa: E501
        :type: int
        """

        self._min_instance = min_instance

    @property
    def reserved_frozen_instance(self):
        """Gets the reserved_frozen_instance of this UpdateFunctionResourceResponse.  # noqa: E501


        :return: The reserved_frozen_instance of this UpdateFunctionResourceResponse.  # noqa: E501
        :rtype: int
        """
        return self._reserved_frozen_instance

    @reserved_frozen_instance.setter
    def reserved_frozen_instance(self, reserved_frozen_instance):
        """Sets the reserved_frozen_instance of this UpdateFunctionResourceResponse.


        :param reserved_frozen_instance: The reserved_frozen_instance of this UpdateFunctionResourceResponse.  # noqa: E501
        :type: int
        """

        self._reserved_frozen_instance = reserved_frozen_instance

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
        if issubclass(UpdateFunctionResourceResponse, dict):
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
        if not isinstance(other, UpdateFunctionResourceResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateFunctionResourceResponse):
            return True

        return self.to_dict() != other.to_dict()
