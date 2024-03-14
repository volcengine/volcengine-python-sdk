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


class DescribeDatabasesResponse(object):
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
        'databases': 'list[DatabaseForDescribeDatabasesOutput]',
        'total': 'int'
    }

    attribute_map = {
        'databases': 'Databases',
        'total': 'Total'
    }

    def __init__(self, databases=None, total=None, _configuration=None):  # noqa: E501
        """DescribeDatabasesResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._databases = None
        self._total = None
        self.discriminator = None

        if databases is not None:
            self.databases = databases
        if total is not None:
            self.total = total

    @property
    def databases(self):
        """Gets the databases of this DescribeDatabasesResponse.  # noqa: E501


        :return: The databases of this DescribeDatabasesResponse.  # noqa: E501
        :rtype: list[DatabaseForDescribeDatabasesOutput]
        """
        return self._databases

    @databases.setter
    def databases(self, databases):
        """Sets the databases of this DescribeDatabasesResponse.


        :param databases: The databases of this DescribeDatabasesResponse.  # noqa: E501
        :type: list[DatabaseForDescribeDatabasesOutput]
        """

        self._databases = databases

    @property
    def total(self):
        """Gets the total of this DescribeDatabasesResponse.  # noqa: E501


        :return: The total of this DescribeDatabasesResponse.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this DescribeDatabasesResponse.


        :param total: The total of this DescribeDatabasesResponse.  # noqa: E501
        :type: int
        """

        self._total = total

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
        if issubclass(DescribeDatabasesResponse, dict):
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
        if not isinstance(other, DescribeDatabasesResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeDatabasesResponse):
            return True

        return self.to_dict() != other.to_dict()
