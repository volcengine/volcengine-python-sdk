# coding: utf-8

"""
    spark

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ResourceForcreateResourcePoolOneStepInput(object):
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
        'basic': 'int',
        'capability': 'int',
        'units': 'str',
        'uri': 'str'
    }

    attribute_map = {
        'basic': 'Basic',
        'capability': 'Capability',
        'units': 'Units',
        'uri': 'Uri'
    }

    def __init__(self, basic=None, capability=None, units=None, uri=None, _configuration=None):  # noqa: E501
        """ResourceForcreateResourcePoolOneStepInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._basic = None
        self._capability = None
        self._units = None
        self._uri = None
        self.discriminator = None

        if basic is not None:
            self.basic = basic
        if capability is not None:
            self.capability = capability
        if units is not None:
            self.units = units
        if uri is not None:
            self.uri = uri

    @property
    def basic(self):
        """Gets the basic of this ResourceForcreateResourcePoolOneStepInput.  # noqa: E501


        :return: The basic of this ResourceForcreateResourcePoolOneStepInput.  # noqa: E501
        :rtype: int
        """
        return self._basic

    @basic.setter
    def basic(self, basic):
        """Sets the basic of this ResourceForcreateResourcePoolOneStepInput.


        :param basic: The basic of this ResourceForcreateResourcePoolOneStepInput.  # noqa: E501
        :type: int
        """

        self._basic = basic

    @property
    def capability(self):
        """Gets the capability of this ResourceForcreateResourcePoolOneStepInput.  # noqa: E501


        :return: The capability of this ResourceForcreateResourcePoolOneStepInput.  # noqa: E501
        :rtype: int
        """
        return self._capability

    @capability.setter
    def capability(self, capability):
        """Sets the capability of this ResourceForcreateResourcePoolOneStepInput.


        :param capability: The capability of this ResourceForcreateResourcePoolOneStepInput.  # noqa: E501
        :type: int
        """

        self._capability = capability

    @property
    def units(self):
        """Gets the units of this ResourceForcreateResourcePoolOneStepInput.  # noqa: E501


        :return: The units of this ResourceForcreateResourcePoolOneStepInput.  # noqa: E501
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this ResourceForcreateResourcePoolOneStepInput.


        :param units: The units of this ResourceForcreateResourcePoolOneStepInput.  # noqa: E501
        :type: str
        """

        self._units = units

    @property
    def uri(self):
        """Gets the uri of this ResourceForcreateResourcePoolOneStepInput.  # noqa: E501


        :return: The uri of this ResourceForcreateResourcePoolOneStepInput.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this ResourceForcreateResourcePoolOneStepInput.


        :param uri: The uri of this ResourceForcreateResourcePoolOneStepInput.  # noqa: E501
        :type: str
        """

        self._uri = uri

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
        if issubclass(ResourceForcreateResourcePoolOneStepInput, dict):
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
        if not isinstance(other, ResourceForcreateResourcePoolOneStepInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResourceForcreateResourcePoolOneStepInput):
            return True

        return self.to_dict() != other.to_dict()