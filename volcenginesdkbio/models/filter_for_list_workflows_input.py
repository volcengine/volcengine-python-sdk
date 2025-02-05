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


class FilterForListWorkflowsInput(object):
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
        'ids': 'list[str]',
        'keyword': 'str'
    }

    attribute_map = {
        'ids': 'IDs',
        'keyword': 'Keyword'
    }

    def __init__(self, ids=None, keyword=None, _configuration=None):  # noqa: E501
        """FilterForListWorkflowsInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._ids = None
        self._keyword = None
        self.discriminator = None

        if ids is not None:
            self.ids = ids
        if keyword is not None:
            self.keyword = keyword

    @property
    def ids(self):
        """Gets the ids of this FilterForListWorkflowsInput.  # noqa: E501


        :return: The ids of this FilterForListWorkflowsInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this FilterForListWorkflowsInput.


        :param ids: The ids of this FilterForListWorkflowsInput.  # noqa: E501
        :type: list[str]
        """

        self._ids = ids

    @property
    def keyword(self):
        """Gets the keyword of this FilterForListWorkflowsInput.  # noqa: E501


        :return: The keyword of this FilterForListWorkflowsInput.  # noqa: E501
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        """Sets the keyword of this FilterForListWorkflowsInput.


        :param keyword: The keyword of this FilterForListWorkflowsInput.  # noqa: E501
        :type: str
        """

        self._keyword = keyword

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
        if issubclass(FilterForListWorkflowsInput, dict):
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
        if not isinstance(other, FilterForListWorkflowsInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FilterForListWorkflowsInput):
            return True

        return self.to_dict() != other.to_dict()
