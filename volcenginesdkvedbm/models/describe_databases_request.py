# coding: utf-8

"""
    vedbm

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeDatabasesRequest(object):
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
        'db_name': 'str',
        'instance_id': 'str',
        'page_number': 'int',
        'page_size': 'int'
    }

    attribute_map = {
        'db_name': 'DBName',
        'instance_id': 'InstanceId',
        'page_number': 'PageNumber',
        'page_size': 'PageSize'
    }

    def __init__(self, db_name=None, instance_id=None, page_number=None, page_size=None, _configuration=None):  # noqa: E501
        """DescribeDatabasesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._db_name = None
        self._instance_id = None
        self._page_number = None
        self._page_size = None
        self.discriminator = None

        if db_name is not None:
            self.db_name = db_name
        self.instance_id = instance_id
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size

    @property
    def db_name(self):
        """Gets the db_name of this DescribeDatabasesRequest.  # noqa: E501


        :return: The db_name of this DescribeDatabasesRequest.  # noqa: E501
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """Sets the db_name of this DescribeDatabasesRequest.


        :param db_name: The db_name of this DescribeDatabasesRequest.  # noqa: E501
        :type: str
        """

        self._db_name = db_name

    @property
    def instance_id(self):
        """Gets the instance_id of this DescribeDatabasesRequest.  # noqa: E501


        :return: The instance_id of this DescribeDatabasesRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this DescribeDatabasesRequest.


        :param instance_id: The instance_id of this DescribeDatabasesRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and instance_id is None:
            raise ValueError("Invalid value for `instance_id`, must not be `None`")  # noqa: E501

        self._instance_id = instance_id

    @property
    def page_number(self):
        """Gets the page_number of this DescribeDatabasesRequest.  # noqa: E501


        :return: The page_number of this DescribeDatabasesRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this DescribeDatabasesRequest.


        :param page_number: The page_number of this DescribeDatabasesRequest.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this DescribeDatabasesRequest.  # noqa: E501


        :return: The page_size of this DescribeDatabasesRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this DescribeDatabasesRequest.


        :param page_size: The page_size of this DescribeDatabasesRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

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
        if issubclass(DescribeDatabasesRequest, dict):
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
        if not isinstance(other, DescribeDatabasesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeDatabasesRequest):
            return True

        return self.to_dict() != other.to_dict()
