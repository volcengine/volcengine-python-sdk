# coding: utf-8

"""
    vefaas

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class GetFunctionInstanceLogsRequest(object):
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
        'function_id': 'str',
        'limit': 'int',
        'name': 'str'
    }

    attribute_map = {
        'function_id': 'FunctionId',
        'limit': 'Limit',
        'name': 'Name'
    }

    def __init__(self, function_id=None, limit=None, name=None, _configuration=None):  # noqa: E501
        """GetFunctionInstanceLogsRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._function_id = None
        self._limit = None
        self._name = None
        self.discriminator = None

        self.function_id = function_id
        if limit is not None:
            self.limit = limit
        self.name = name

    @property
    def function_id(self):
        """Gets the function_id of this GetFunctionInstanceLogsRequest.  # noqa: E501


        :return: The function_id of this GetFunctionInstanceLogsRequest.  # noqa: E501
        :rtype: str
        """
        return self._function_id

    @function_id.setter
    def function_id(self, function_id):
        """Sets the function_id of this GetFunctionInstanceLogsRequest.


        :param function_id: The function_id of this GetFunctionInstanceLogsRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and function_id is None:
            raise ValueError("Invalid value for `function_id`, must not be `None`")  # noqa: E501

        self._function_id = function_id

    @property
    def limit(self):
        """Gets the limit of this GetFunctionInstanceLogsRequest.  # noqa: E501


        :return: The limit of this GetFunctionInstanceLogsRequest.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this GetFunctionInstanceLogsRequest.


        :param limit: The limit of this GetFunctionInstanceLogsRequest.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def name(self):
        """Gets the name of this GetFunctionInstanceLogsRequest.  # noqa: E501


        :return: The name of this GetFunctionInstanceLogsRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetFunctionInstanceLogsRequest.


        :param name: The name of this GetFunctionInstanceLogsRequest.  # noqa: E501
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
        if issubclass(GetFunctionInstanceLogsRequest, dict):
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
        if not isinstance(other, GetFunctionInstanceLogsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetFunctionInstanceLogsRequest):
            return True

        return self.to_dict() != other.to_dict()