# coding: utf-8

"""
    waf

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class AccurateRuleForCreateAclRuleInput(object):
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
        'http_obj': 'str',
        'obj_type': 'int',
        'opretar': 'int',
        '_property': 'int',
        'value_string': 'str'
    }

    attribute_map = {
        'http_obj': 'HttpObj',
        'obj_type': 'ObjType',
        'opretar': 'Opretar',
        '_property': 'Property',
        'value_string': 'ValueString'
    }

    def __init__(self, http_obj=None, obj_type=None, opretar=None, _property=None, value_string=None, _configuration=None):  # noqa: E501
        """AccurateRuleForCreateAclRuleInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._http_obj = None
        self._obj_type = None
        self._opretar = None
        self.__property = None
        self._value_string = None
        self.discriminator = None

        if http_obj is not None:
            self.http_obj = http_obj
        if obj_type is not None:
            self.obj_type = obj_type
        if opretar is not None:
            self.opretar = opretar
        if _property is not None:
            self._property = _property
        if value_string is not None:
            self.value_string = value_string

    @property
    def http_obj(self):
        """Gets the http_obj of this AccurateRuleForCreateAclRuleInput.  # noqa: E501


        :return: The http_obj of this AccurateRuleForCreateAclRuleInput.  # noqa: E501
        :rtype: str
        """
        return self._http_obj

    @http_obj.setter
    def http_obj(self, http_obj):
        """Sets the http_obj of this AccurateRuleForCreateAclRuleInput.


        :param http_obj: The http_obj of this AccurateRuleForCreateAclRuleInput.  # noqa: E501
        :type: str
        """

        self._http_obj = http_obj

    @property
    def obj_type(self):
        """Gets the obj_type of this AccurateRuleForCreateAclRuleInput.  # noqa: E501


        :return: The obj_type of this AccurateRuleForCreateAclRuleInput.  # noqa: E501
        :rtype: int
        """
        return self._obj_type

    @obj_type.setter
    def obj_type(self, obj_type):
        """Sets the obj_type of this AccurateRuleForCreateAclRuleInput.


        :param obj_type: The obj_type of this AccurateRuleForCreateAclRuleInput.  # noqa: E501
        :type: int
        """

        self._obj_type = obj_type

    @property
    def opretar(self):
        """Gets the opretar of this AccurateRuleForCreateAclRuleInput.  # noqa: E501


        :return: The opretar of this AccurateRuleForCreateAclRuleInput.  # noqa: E501
        :rtype: int
        """
        return self._opretar

    @opretar.setter
    def opretar(self, opretar):
        """Sets the opretar of this AccurateRuleForCreateAclRuleInput.


        :param opretar: The opretar of this AccurateRuleForCreateAclRuleInput.  # noqa: E501
        :type: int
        """

        self._opretar = opretar

    @property
    def _property(self):
        """Gets the _property of this AccurateRuleForCreateAclRuleInput.  # noqa: E501


        :return: The _property of this AccurateRuleForCreateAclRuleInput.  # noqa: E501
        :rtype: int
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """Sets the _property of this AccurateRuleForCreateAclRuleInput.


        :param _property: The _property of this AccurateRuleForCreateAclRuleInput.  # noqa: E501
        :type: int
        """

        self.__property = _property

    @property
    def value_string(self):
        """Gets the value_string of this AccurateRuleForCreateAclRuleInput.  # noqa: E501


        :return: The value_string of this AccurateRuleForCreateAclRuleInput.  # noqa: E501
        :rtype: str
        """
        return self._value_string

    @value_string.setter
    def value_string(self, value_string):
        """Sets the value_string of this AccurateRuleForCreateAclRuleInput.


        :param value_string: The value_string of this AccurateRuleForCreateAclRuleInput.  # noqa: E501
        :type: str
        """

        self._value_string = value_string

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
        if issubclass(AccurateRuleForCreateAclRuleInput, dict):
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
        if not isinstance(other, AccurateRuleForCreateAclRuleInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccurateRuleForCreateAclRuleInput):
            return True

        return self.to_dict() != other.to_dict()
