# coding: utf-8

"""
    rds_mysql_v2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class TemplateParamForModifyParameterTemplateInput(object):
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
        'description': 'str',
        'name': 'str',
        'running_value': 'str'
    }

    attribute_map = {
        'description': 'Description',
        'name': 'Name',
        'running_value': 'RunningValue'
    }

    def __init__(self, description=None, name=None, running_value=None, _configuration=None):  # noqa: E501
        """TemplateParamForModifyParameterTemplateInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._description = None
        self._name = None
        self._running_value = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if running_value is not None:
            self.running_value = running_value

    @property
    def description(self):
        """Gets the description of this TemplateParamForModifyParameterTemplateInput.  # noqa: E501


        :return: The description of this TemplateParamForModifyParameterTemplateInput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TemplateParamForModifyParameterTemplateInput.


        :param description: The description of this TemplateParamForModifyParameterTemplateInput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this TemplateParamForModifyParameterTemplateInput.  # noqa: E501


        :return: The name of this TemplateParamForModifyParameterTemplateInput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TemplateParamForModifyParameterTemplateInput.


        :param name: The name of this TemplateParamForModifyParameterTemplateInput.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def running_value(self):
        """Gets the running_value of this TemplateParamForModifyParameterTemplateInput.  # noqa: E501


        :return: The running_value of this TemplateParamForModifyParameterTemplateInput.  # noqa: E501
        :rtype: str
        """
        return self._running_value

    @running_value.setter
    def running_value(self, running_value):
        """Sets the running_value of this TemplateParamForModifyParameterTemplateInput.


        :param running_value: The running_value of this TemplateParamForModifyParameterTemplateInput.  # noqa: E501
        :type: str
        """

        self._running_value = running_value

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
        if issubclass(TemplateParamForModifyParameterTemplateInput, dict):
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
        if not isinstance(other, TemplateParamForModifyParameterTemplateInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TemplateParamForModifyParameterTemplateInput):
            return True

        return self.to_dict() != other.to_dict()
