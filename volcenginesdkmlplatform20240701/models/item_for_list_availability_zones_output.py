# coding: utf-8

"""
    ml_platform20240701

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ItemForListAvailabilityZonesOutput(object):
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
        'english_name': 'str',
        'id': 'str',
        'is_default': 'bool',
        'name': 'str',
        'region_id': 'str'
    }

    attribute_map = {
        'english_name': 'EnglishName',
        'id': 'Id',
        'is_default': 'IsDefault',
        'name': 'Name',
        'region_id': 'RegionId'
    }

    def __init__(self, english_name=None, id=None, is_default=None, name=None, region_id=None, _configuration=None):  # noqa: E501
        """ItemForListAvailabilityZonesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._english_name = None
        self._id = None
        self._is_default = None
        self._name = None
        self._region_id = None
        self.discriminator = None

        if english_name is not None:
            self.english_name = english_name
        if id is not None:
            self.id = id
        if is_default is not None:
            self.is_default = is_default
        if name is not None:
            self.name = name
        if region_id is not None:
            self.region_id = region_id

    @property
    def english_name(self):
        """Gets the english_name of this ItemForListAvailabilityZonesOutput.  # noqa: E501


        :return: The english_name of this ItemForListAvailabilityZonesOutput.  # noqa: E501
        :rtype: str
        """
        return self._english_name

    @english_name.setter
    def english_name(self, english_name):
        """Sets the english_name of this ItemForListAvailabilityZonesOutput.


        :param english_name: The english_name of this ItemForListAvailabilityZonesOutput.  # noqa: E501
        :type: str
        """

        self._english_name = english_name

    @property
    def id(self):
        """Gets the id of this ItemForListAvailabilityZonesOutput.  # noqa: E501


        :return: The id of this ItemForListAvailabilityZonesOutput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ItemForListAvailabilityZonesOutput.


        :param id: The id of this ItemForListAvailabilityZonesOutput.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def is_default(self):
        """Gets the is_default of this ItemForListAvailabilityZonesOutput.  # noqa: E501


        :return: The is_default of this ItemForListAvailabilityZonesOutput.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this ItemForListAvailabilityZonesOutput.


        :param is_default: The is_default of this ItemForListAvailabilityZonesOutput.  # noqa: E501
        :type: bool
        """

        self._is_default = is_default

    @property
    def name(self):
        """Gets the name of this ItemForListAvailabilityZonesOutput.  # noqa: E501


        :return: The name of this ItemForListAvailabilityZonesOutput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ItemForListAvailabilityZonesOutput.


        :param name: The name of this ItemForListAvailabilityZonesOutput.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def region_id(self):
        """Gets the region_id of this ItemForListAvailabilityZonesOutput.  # noqa: E501


        :return: The region_id of this ItemForListAvailabilityZonesOutput.  # noqa: E501
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this ItemForListAvailabilityZonesOutput.


        :param region_id: The region_id of this ItemForListAvailabilityZonesOutput.  # noqa: E501
        :type: str
        """

        self._region_id = region_id

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
        if issubclass(ItemForListAvailabilityZonesOutput, dict):
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
        if not isinstance(other, ItemForListAvailabilityZonesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ItemForListAvailabilityZonesOutput):
            return True

        return self.to_dict() != other.to_dict()
