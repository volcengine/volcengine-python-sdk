# coding: utf-8

"""
    rds_mysql

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ListDatabasesRequest(object):
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
        'db_status': 'str',
        'instance_id': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'db_status': 'DBStatus',
        'instance_id': 'InstanceId',
        'limit': 'Limit',
        'offset': 'Offset'
    }

    def __init__(self, db_status=None, instance_id=None, limit=None, offset=None, _configuration=None):  # noqa: E501
        """ListDatabasesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._db_status = None
        self._instance_id = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if db_status is not None:
            self.db_status = db_status
        if instance_id is not None:
            self.instance_id = instance_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def db_status(self):
        """Gets the db_status of this ListDatabasesRequest.  # noqa: E501


        :return: The db_status of this ListDatabasesRequest.  # noqa: E501
        :rtype: str
        """
        return self._db_status

    @db_status.setter
    def db_status(self, db_status):
        """Sets the db_status of this ListDatabasesRequest.


        :param db_status: The db_status of this ListDatabasesRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["Creating", "Deleting", "Running"]  # noqa: E501
        if (self._configuration.client_side_validation and
                db_status not in allowed_values):
            raise ValueError(
                "Invalid value for `db_status` ({0}), must be one of {1}"  # noqa: E501
                .format(db_status, allowed_values)
            )

        self._db_status = db_status

    @property
    def instance_id(self):
        """Gets the instance_id of this ListDatabasesRequest.  # noqa: E501


        :return: The instance_id of this ListDatabasesRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListDatabasesRequest.


        :param instance_id: The instance_id of this ListDatabasesRequest.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def limit(self):
        """Gets the limit of this ListDatabasesRequest.  # noqa: E501


        :return: The limit of this ListDatabasesRequest.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListDatabasesRequest.


        :param limit: The limit of this ListDatabasesRequest.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListDatabasesRequest.  # noqa: E501


        :return: The offset of this ListDatabasesRequest.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListDatabasesRequest.


        :param offset: The offset of this ListDatabasesRequest.  # noqa: E501
        :type: int
        """

        self._offset = offset

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
        if issubclass(ListDatabasesRequest, dict):
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
        if not isinstance(other, ListDatabasesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListDatabasesRequest):
            return True

        return self.to_dict() != other.to_dict()
