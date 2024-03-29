# coding: utf-8

"""
    cr

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class FilterForListRepositoriesInput(object):
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
        'access_levels': 'list[str]',
        'names': 'list[str]',
        'namespaces': 'list[str]'
    }

    attribute_map = {
        'access_levels': 'AccessLevels',
        'names': 'Names',
        'namespaces': 'Namespaces'
    }

    def __init__(self, access_levels=None, names=None, namespaces=None, _configuration=None):  # noqa: E501
        """FilterForListRepositoriesInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._access_levels = None
        self._names = None
        self._namespaces = None
        self.discriminator = None

        if access_levels is not None:
            self.access_levels = access_levels
        if names is not None:
            self.names = names
        if namespaces is not None:
            self.namespaces = namespaces

    @property
    def access_levels(self):
        """Gets the access_levels of this FilterForListRepositoriesInput.  # noqa: E501


        :return: The access_levels of this FilterForListRepositoriesInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._access_levels

    @access_levels.setter
    def access_levels(self, access_levels):
        """Sets the access_levels of this FilterForListRepositoriesInput.


        :param access_levels: The access_levels of this FilterForListRepositoriesInput.  # noqa: E501
        :type: list[str]
        """

        self._access_levels = access_levels

    @property
    def names(self):
        """Gets the names of this FilterForListRepositoriesInput.  # noqa: E501


        :return: The names of this FilterForListRepositoriesInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._names

    @names.setter
    def names(self, names):
        """Sets the names of this FilterForListRepositoriesInput.


        :param names: The names of this FilterForListRepositoriesInput.  # noqa: E501
        :type: list[str]
        """

        self._names = names

    @property
    def namespaces(self):
        """Gets the namespaces of this FilterForListRepositoriesInput.  # noqa: E501


        :return: The namespaces of this FilterForListRepositoriesInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._namespaces

    @namespaces.setter
    def namespaces(self, namespaces):
        """Sets the namespaces of this FilterForListRepositoriesInput.


        :param namespaces: The namespaces of this FilterForListRepositoriesInput.  # noqa: E501
        :type: list[str]
        """

        self._namespaces = namespaces

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
        if issubclass(FilterForListRepositoriesInput, dict):
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
        if not isinstance(other, FilterForListRepositoriesInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FilterForListRepositoriesInput):
            return True

        return self.to_dict() != other.to_dict()
