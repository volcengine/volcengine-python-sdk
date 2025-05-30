# coding: utf-8

"""
    edx

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class CreateEDXRequest(object):
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
        'as_number': 'str',
        'area': 'str',
        'description': 'str',
        'name': 'str'
    }

    attribute_map = {
        'as_number': 'ASNumber',
        'area': 'Area',
        'description': 'Description',
        'name': 'Name'
    }

    def __init__(self, as_number=None, area=None, description=None, name=None, _configuration=None):  # noqa: E501
        """CreateEDXRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._as_number = None
        self._area = None
        self._description = None
        self._name = None
        self.discriminator = None

        self.as_number = as_number
        self.area = area
        self.description = description
        self.name = name

    @property
    def as_number(self):
        """Gets the as_number of this CreateEDXRequest.  # noqa: E501


        :return: The as_number of this CreateEDXRequest.  # noqa: E501
        :rtype: str
        """
        return self._as_number

    @as_number.setter
    def as_number(self, as_number):
        """Sets the as_number of this CreateEDXRequest.


        :param as_number: The as_number of this CreateEDXRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and as_number is None:
            raise ValueError("Invalid value for `as_number`, must not be `None`")  # noqa: E501

        self._as_number = as_number

    @property
    def area(self):
        """Gets the area of this CreateEDXRequest.  # noqa: E501


        :return: The area of this CreateEDXRequest.  # noqa: E501
        :rtype: str
        """
        return self._area

    @area.setter
    def area(self, area):
        """Sets the area of this CreateEDXRequest.


        :param area: The area of this CreateEDXRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and area is None:
            raise ValueError("Invalid value for `area`, must not be `None`")  # noqa: E501

        self._area = area

    @property
    def description(self):
        """Gets the description of this CreateEDXRequest.  # noqa: E501


        :return: The description of this CreateEDXRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateEDXRequest.


        :param description: The description of this CreateEDXRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def name(self):
        """Gets the name of this CreateEDXRequest.  # noqa: E501


        :return: The name of this CreateEDXRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateEDXRequest.


        :param name: The name of this CreateEDXRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if issubclass(CreateEDXRequest, dict):
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
        if not isinstance(other, CreateEDXRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateEDXRequest):
            return True

        return self.to_dict() != other.to_dict()
