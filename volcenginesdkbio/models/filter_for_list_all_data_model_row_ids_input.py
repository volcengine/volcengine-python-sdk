# coding: utf-8

"""
    bio

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class FilterForListAllDataModelRowIDsInput(object):
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
        'in_set_ids': 'list[str]',
        'keyword': 'str',
        'row_ids': 'list[str]'
    }

    attribute_map = {
        'in_set_ids': 'InSetIDs',
        'keyword': 'Keyword',
        'row_ids': 'RowIDs'
    }

    def __init__(self, in_set_ids=None, keyword=None, row_ids=None, _configuration=None):  # noqa: E501
        """FilterForListAllDataModelRowIDsInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._in_set_ids = None
        self._keyword = None
        self._row_ids = None
        self.discriminator = None

        if in_set_ids is not None:
            self.in_set_ids = in_set_ids
        if keyword is not None:
            self.keyword = keyword
        if row_ids is not None:
            self.row_ids = row_ids

    @property
    def in_set_ids(self):
        """Gets the in_set_ids of this FilterForListAllDataModelRowIDsInput.  # noqa: E501


        :return: The in_set_ids of this FilterForListAllDataModelRowIDsInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._in_set_ids

    @in_set_ids.setter
    def in_set_ids(self, in_set_ids):
        """Sets the in_set_ids of this FilterForListAllDataModelRowIDsInput.


        :param in_set_ids: The in_set_ids of this FilterForListAllDataModelRowIDsInput.  # noqa: E501
        :type: list[str]
        """

        self._in_set_ids = in_set_ids

    @property
    def keyword(self):
        """Gets the keyword of this FilterForListAllDataModelRowIDsInput.  # noqa: E501


        :return: The keyword of this FilterForListAllDataModelRowIDsInput.  # noqa: E501
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        """Sets the keyword of this FilterForListAllDataModelRowIDsInput.


        :param keyword: The keyword of this FilterForListAllDataModelRowIDsInput.  # noqa: E501
        :type: str
        """

        self._keyword = keyword

    @property
    def row_ids(self):
        """Gets the row_ids of this FilterForListAllDataModelRowIDsInput.  # noqa: E501


        :return: The row_ids of this FilterForListAllDataModelRowIDsInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._row_ids

    @row_ids.setter
    def row_ids(self, row_ids):
        """Sets the row_ids of this FilterForListAllDataModelRowIDsInput.


        :param row_ids: The row_ids of this FilterForListAllDataModelRowIDsInput.  # noqa: E501
        :type: list[str]
        """

        self._row_ids = row_ids

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
        if issubclass(FilterForListAllDataModelRowIDsInput, dict):
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
        if not isinstance(other, FilterForListAllDataModelRowIDsInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FilterForListAllDataModelRowIDsInput):
            return True

        return self.to_dict() != other.to_dict()
