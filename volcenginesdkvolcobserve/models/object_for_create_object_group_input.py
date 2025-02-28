# coding: utf-8

"""
    volc_observe

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ObjectForCreateObjectGroupInput(object):
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
        'dimension_conditions': 'DimensionConditionsForCreateObjectGroupInput',
        'dimensions': 'dict(str, list[str])',
        'namespace': 'str',
        'region': 'str',
        'type': 'str'
    }

    attribute_map = {
        'dimension_conditions': 'DimensionConditions',
        'dimensions': 'Dimensions',
        'namespace': 'Namespace',
        'region': 'Region',
        'type': 'Type'
    }

    def __init__(self, dimension_conditions=None, dimensions=None, namespace=None, region=None, type=None, _configuration=None):  # noqa: E501
        """ObjectForCreateObjectGroupInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._dimension_conditions = None
        self._dimensions = None
        self._namespace = None
        self._region = None
        self._type = None
        self.discriminator = None

        if dimension_conditions is not None:
            self.dimension_conditions = dimension_conditions
        if dimensions is not None:
            self.dimensions = dimensions
        if namespace is not None:
            self.namespace = namespace
        if region is not None:
            self.region = region
        if type is not None:
            self.type = type

    @property
    def dimension_conditions(self):
        """Gets the dimension_conditions of this ObjectForCreateObjectGroupInput.  # noqa: E501


        :return: The dimension_conditions of this ObjectForCreateObjectGroupInput.  # noqa: E501
        :rtype: DimensionConditionsForCreateObjectGroupInput
        """
        return self._dimension_conditions

    @dimension_conditions.setter
    def dimension_conditions(self, dimension_conditions):
        """Sets the dimension_conditions of this ObjectForCreateObjectGroupInput.


        :param dimension_conditions: The dimension_conditions of this ObjectForCreateObjectGroupInput.  # noqa: E501
        :type: DimensionConditionsForCreateObjectGroupInput
        """

        self._dimension_conditions = dimension_conditions

    @property
    def dimensions(self):
        """Gets the dimensions of this ObjectForCreateObjectGroupInput.  # noqa: E501


        :return: The dimensions of this ObjectForCreateObjectGroupInput.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """Sets the dimensions of this ObjectForCreateObjectGroupInput.


        :param dimensions: The dimensions of this ObjectForCreateObjectGroupInput.  # noqa: E501
        :type: dict(str, list[str])
        """

        self._dimensions = dimensions

    @property
    def namespace(self):
        """Gets the namespace of this ObjectForCreateObjectGroupInput.  # noqa: E501


        :return: The namespace of this ObjectForCreateObjectGroupInput.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this ObjectForCreateObjectGroupInput.


        :param namespace: The namespace of this ObjectForCreateObjectGroupInput.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def region(self):
        """Gets the region of this ObjectForCreateObjectGroupInput.  # noqa: E501


        :return: The region of this ObjectForCreateObjectGroupInput.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ObjectForCreateObjectGroupInput.


        :param region: The region of this ObjectForCreateObjectGroupInput.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def type(self):
        """Gets the type of this ObjectForCreateObjectGroupInput.  # noqa: E501


        :return: The type of this ObjectForCreateObjectGroupInput.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ObjectForCreateObjectGroupInput.


        :param type: The type of this ObjectForCreateObjectGroupInput.  # noqa: E501
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
        if issubclass(ObjectForCreateObjectGroupInput, dict):
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
        if not isinstance(other, ObjectForCreateObjectGroupInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ObjectForCreateObjectGroupInput):
            return True

        return self.to_dict() != other.to_dict()
