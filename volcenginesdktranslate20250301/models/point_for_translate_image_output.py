# coding: utf-8

"""
    translate20250301

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class PointForTranslateImageOutput(object):
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
        'x': 'int',
        'y': 'int'
    }

    attribute_map = {
        'x': 'X',
        'y': 'Y'
    }

    def __init__(self, x=None, y=None, _configuration=None):  # noqa: E501
        """PointForTranslateImageOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._x = None
        self._y = None
        self.discriminator = None

        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    @property
    def x(self):
        """Gets the x of this PointForTranslateImageOutput.  # noqa: E501


        :return: The x of this PointForTranslateImageOutput.  # noqa: E501
        :rtype: int
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this PointForTranslateImageOutput.


        :param x: The x of this PointForTranslateImageOutput.  # noqa: E501
        :type: int
        """

        self._x = x

    @property
    def y(self):
        """Gets the y of this PointForTranslateImageOutput.  # noqa: E501


        :return: The y of this PointForTranslateImageOutput.  # noqa: E501
        :rtype: int
        """
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y of this PointForTranslateImageOutput.


        :param y: The y of this PointForTranslateImageOutput.  # noqa: E501
        :type: int
        """

        self._y = y

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
        if issubclass(PointForTranslateImageOutput, dict):
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
        if not isinstance(other, PointForTranslateImageOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PointForTranslateImageOutput):
            return True

        return self.to_dict() != other.to_dict()
