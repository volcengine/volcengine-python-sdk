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


class ControlnetArgForImg2ImgXLSftInput(object):
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
        'binary_data_index': 'int',
        'strength': 'float',
        'type': 'str'
    }

    attribute_map = {
        'binary_data_index': 'binary_data_index',
        'strength': 'strength',
        'type': 'type'
    }

    def __init__(self, binary_data_index=None, strength=None, type=None, _configuration=None):  # noqa: E501
        """ControlnetArgForImg2ImgXLSftInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._binary_data_index = None
        self._strength = None
        self._type = None
        self.discriminator = None

        if binary_data_index is not None:
            self.binary_data_index = binary_data_index
        if strength is not None:
            self.strength = strength
        if type is not None:
            self.type = type

    @property
    def binary_data_index(self):
        """Gets the binary_data_index of this ControlnetArgForImg2ImgXLSftInput.  # noqa: E501


        :return: The binary_data_index of this ControlnetArgForImg2ImgXLSftInput.  # noqa: E501
        :rtype: int
        """
        return self._binary_data_index

    @binary_data_index.setter
    def binary_data_index(self, binary_data_index):
        """Sets the binary_data_index of this ControlnetArgForImg2ImgXLSftInput.


        :param binary_data_index: The binary_data_index of this ControlnetArgForImg2ImgXLSftInput.  # noqa: E501
        :type: int
        """

        self._binary_data_index = binary_data_index

    @property
    def strength(self):
        """Gets the strength of this ControlnetArgForImg2ImgXLSftInput.  # noqa: E501


        :return: The strength of this ControlnetArgForImg2ImgXLSftInput.  # noqa: E501
        :rtype: float
        """
        return self._strength

    @strength.setter
    def strength(self, strength):
        """Sets the strength of this ControlnetArgForImg2ImgXLSftInput.


        :param strength: The strength of this ControlnetArgForImg2ImgXLSftInput.  # noqa: E501
        :type: float
        """

        self._strength = strength

    @property
    def type(self):
        """Gets the type of this ControlnetArgForImg2ImgXLSftInput.  # noqa: E501


        :return: The type of this ControlnetArgForImg2ImgXLSftInput.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ControlnetArgForImg2ImgXLSftInput.


        :param type: The type of this ControlnetArgForImg2ImgXLSftInput.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(ControlnetArgForImg2ImgXLSftInput, dict):
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
        if not isinstance(other, ControlnetArgForImg2ImgXLSftInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ControlnetArgForImg2ImgXLSftInput):
            return True

        return self.to_dict() != other.to_dict()
