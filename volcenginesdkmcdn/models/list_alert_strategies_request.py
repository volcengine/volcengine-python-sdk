# coding: utf-8

"""
    mcdn

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ListAlertStrategiesRequest(object):
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
        'level': 'str',
        'name': 'str',
        'pagination': 'PaginationForListAlertStrategiesInput',
        'status': 'str'
    }

    attribute_map = {
        'level': 'Level',
        'name': 'Name',
        'pagination': 'Pagination',
        'status': 'Status'
    }

    def __init__(self, level=None, name=None, pagination=None, status=None, _configuration=None):  # noqa: E501
        """ListAlertStrategiesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._level = None
        self._name = None
        self._pagination = None
        self._status = None
        self.discriminator = None

        if level is not None:
            self.level = level
        if name is not None:
            self.name = name
        if pagination is not None:
            self.pagination = pagination
        if status is not None:
            self.status = status

    @property
    def level(self):
        """Gets the level of this ListAlertStrategiesRequest.  # noqa: E501


        :return: The level of this ListAlertStrategiesRequest.  # noqa: E501
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this ListAlertStrategiesRequest.


        :param level: The level of this ListAlertStrategiesRequest.  # noqa: E501
        :type: str
        """

        self._level = level

    @property
    def name(self):
        """Gets the name of this ListAlertStrategiesRequest.  # noqa: E501


        :return: The name of this ListAlertStrategiesRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListAlertStrategiesRequest.


        :param name: The name of this ListAlertStrategiesRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def pagination(self):
        """Gets the pagination of this ListAlertStrategiesRequest.  # noqa: E501


        :return: The pagination of this ListAlertStrategiesRequest.  # noqa: E501
        :rtype: PaginationForListAlertStrategiesInput
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this ListAlertStrategiesRequest.


        :param pagination: The pagination of this ListAlertStrategiesRequest.  # noqa: E501
        :type: PaginationForListAlertStrategiesInput
        """

        self._pagination = pagination

    @property
    def status(self):
        """Gets the status of this ListAlertStrategiesRequest.  # noqa: E501


        :return: The status of this ListAlertStrategiesRequest.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListAlertStrategiesRequest.


        :param status: The status of this ListAlertStrategiesRequest.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(ListAlertStrategiesRequest, dict):
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
        if not isinstance(other, ListAlertStrategiesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListAlertStrategiesRequest):
            return True

        return self.to_dict() != other.to_dict()
