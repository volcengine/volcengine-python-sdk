# coding: utf-8

"""
    quota

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DimensionForListProductQuotaDimensionsOutput(object):
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
        'dimension_code': 'str',
        'dimension_name': 'str',
        'dimension_values': 'list[DimensionValueForListProductQuotaDimensionsOutput]'
    }

    attribute_map = {
        'dimension_code': 'DimensionCode',
        'dimension_name': 'DimensionName',
        'dimension_values': 'DimensionValues'
    }

    def __init__(self, dimension_code=None, dimension_name=None, dimension_values=None, _configuration=None):  # noqa: E501
        """DimensionForListProductQuotaDimensionsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._dimension_code = None
        self._dimension_name = None
        self._dimension_values = None
        self.discriminator = None

        if dimension_code is not None:
            self.dimension_code = dimension_code
        if dimension_name is not None:
            self.dimension_name = dimension_name
        if dimension_values is not None:
            self.dimension_values = dimension_values

    @property
    def dimension_code(self):
        """Gets the dimension_code of this DimensionForListProductQuotaDimensionsOutput.  # noqa: E501


        :return: The dimension_code of this DimensionForListProductQuotaDimensionsOutput.  # noqa: E501
        :rtype: str
        """
        return self._dimension_code

    @dimension_code.setter
    def dimension_code(self, dimension_code):
        """Sets the dimension_code of this DimensionForListProductQuotaDimensionsOutput.


        :param dimension_code: The dimension_code of this DimensionForListProductQuotaDimensionsOutput.  # noqa: E501
        :type: str
        """

        self._dimension_code = dimension_code

    @property
    def dimension_name(self):
        """Gets the dimension_name of this DimensionForListProductQuotaDimensionsOutput.  # noqa: E501


        :return: The dimension_name of this DimensionForListProductQuotaDimensionsOutput.  # noqa: E501
        :rtype: str
        """
        return self._dimension_name

    @dimension_name.setter
    def dimension_name(self, dimension_name):
        """Sets the dimension_name of this DimensionForListProductQuotaDimensionsOutput.


        :param dimension_name: The dimension_name of this DimensionForListProductQuotaDimensionsOutput.  # noqa: E501
        :type: str
        """

        self._dimension_name = dimension_name

    @property
    def dimension_values(self):
        """Gets the dimension_values of this DimensionForListProductQuotaDimensionsOutput.  # noqa: E501


        :return: The dimension_values of this DimensionForListProductQuotaDimensionsOutput.  # noqa: E501
        :rtype: list[DimensionValueForListProductQuotaDimensionsOutput]
        """
        return self._dimension_values

    @dimension_values.setter
    def dimension_values(self, dimension_values):
        """Sets the dimension_values of this DimensionForListProductQuotaDimensionsOutput.


        :param dimension_values: The dimension_values of this DimensionForListProductQuotaDimensionsOutput.  # noqa: E501
        :type: list[DimensionValueForListProductQuotaDimensionsOutput]
        """

        self._dimension_values = dimension_values

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
        if issubclass(DimensionForListProductQuotaDimensionsOutput, dict):
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
        if not isinstance(other, DimensionForListProductQuotaDimensionsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DimensionForListProductQuotaDimensionsOutput):
            return True

        return self.to_dict() != other.to_dict()
