# coding: utf-8

"""
    vei_api

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class CreateSNInOneStepRequest(object):
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
        'auto_renew': 'bool',
        'count_of_month': 'int',
        'type': 'int'
    }

    attribute_map = {
        'auto_renew': 'auto_renew',
        'count_of_month': 'count_of_month',
        'type': 'type'
    }

    def __init__(self, auto_renew=None, count_of_month=None, type=None, _configuration=None):  # noqa: E501
        """CreateSNInOneStepRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._auto_renew = None
        self._count_of_month = None
        self._type = None
        self.discriminator = None

        if auto_renew is not None:
            self.auto_renew = auto_renew
        self.count_of_month = count_of_month
        self.type = type

    @property
    def auto_renew(self):
        """Gets the auto_renew of this CreateSNInOneStepRequest.  # noqa: E501


        :return: The auto_renew of this CreateSNInOneStepRequest.  # noqa: E501
        :rtype: bool
        """
        return self._auto_renew

    @auto_renew.setter
    def auto_renew(self, auto_renew):
        """Sets the auto_renew of this CreateSNInOneStepRequest.


        :param auto_renew: The auto_renew of this CreateSNInOneStepRequest.  # noqa: E501
        :type: bool
        """

        self._auto_renew = auto_renew

    @property
    def count_of_month(self):
        """Gets the count_of_month of this CreateSNInOneStepRequest.  # noqa: E501


        :return: The count_of_month of this CreateSNInOneStepRequest.  # noqa: E501
        :rtype: int
        """
        return self._count_of_month

    @count_of_month.setter
    def count_of_month(self, count_of_month):
        """Sets the count_of_month of this CreateSNInOneStepRequest.


        :param count_of_month: The count_of_month of this CreateSNInOneStepRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and count_of_month is None:
            raise ValueError("Invalid value for `count_of_month`, must not be `None`")  # noqa: E501

        self._count_of_month = count_of_month

    @property
    def type(self):
        """Gets the type of this CreateSNInOneStepRequest.  # noqa: E501


        :return: The type of this CreateSNInOneStepRequest.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateSNInOneStepRequest.


        :param type: The type of this CreateSNInOneStepRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

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
        if issubclass(CreateSNInOneStepRequest, dict):
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
        if not isinstance(other, CreateSNInOneStepRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateSNInOneStepRequest):
            return True

        return self.to_dict() != other.to_dict()
