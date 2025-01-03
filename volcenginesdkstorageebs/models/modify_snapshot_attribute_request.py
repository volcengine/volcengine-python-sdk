# coding: utf-8

"""
    storage_ebs

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ModifySnapshotAttributeRequest(object):
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
        'retention_days': 'int',
        'snapshot_id': 'str',
        'snapshot_name': 'str'
    }

    attribute_map = {
        'description': 'Description',
        'retention_days': 'RetentionDays',
        'snapshot_id': 'SnapshotId',
        'snapshot_name': 'SnapshotName'
    }

    def __init__(self, description=None, retention_days=None, snapshot_id=None, snapshot_name=None, _configuration=None):  # noqa: E501
        """ModifySnapshotAttributeRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._description = None
        self._retention_days = None
        self._snapshot_id = None
        self._snapshot_name = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if retention_days is not None:
            self.retention_days = retention_days
        self.snapshot_id = snapshot_id
        if snapshot_name is not None:
            self.snapshot_name = snapshot_name

    @property
    def description(self):
        """Gets the description of this ModifySnapshotAttributeRequest.  # noqa: E501


        :return: The description of this ModifySnapshotAttributeRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ModifySnapshotAttributeRequest.


        :param description: The description of this ModifySnapshotAttributeRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def retention_days(self):
        """Gets the retention_days of this ModifySnapshotAttributeRequest.  # noqa: E501


        :return: The retention_days of this ModifySnapshotAttributeRequest.  # noqa: E501
        :rtype: int
        """
        return self._retention_days

    @retention_days.setter
    def retention_days(self, retention_days):
        """Sets the retention_days of this ModifySnapshotAttributeRequest.


        :param retention_days: The retention_days of this ModifySnapshotAttributeRequest.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                retention_days is not None and retention_days > 65536):  # noqa: E501
            raise ValueError("Invalid value for `retention_days`, must be a value less than or equal to `65536`")  # noqa: E501
        if (self._configuration.client_side_validation and
                retention_days is not None and retention_days < 1):  # noqa: E501
            raise ValueError("Invalid value for `retention_days`, must be a value greater than or equal to `1`")  # noqa: E501

        self._retention_days = retention_days

    @property
    def snapshot_id(self):
        """Gets the snapshot_id of this ModifySnapshotAttributeRequest.  # noqa: E501


        :return: The snapshot_id of this ModifySnapshotAttributeRequest.  # noqa: E501
        :rtype: str
        """
        return self._snapshot_id

    @snapshot_id.setter
    def snapshot_id(self, snapshot_id):
        """Sets the snapshot_id of this ModifySnapshotAttributeRequest.


        :param snapshot_id: The snapshot_id of this ModifySnapshotAttributeRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and snapshot_id is None:
            raise ValueError("Invalid value for `snapshot_id`, must not be `None`")  # noqa: E501

        self._snapshot_id = snapshot_id

    @property
    def snapshot_name(self):
        """Gets the snapshot_name of this ModifySnapshotAttributeRequest.  # noqa: E501


        :return: The snapshot_name of this ModifySnapshotAttributeRequest.  # noqa: E501
        :rtype: str
        """
        return self._snapshot_name

    @snapshot_name.setter
    def snapshot_name(self, snapshot_name):
        """Sets the snapshot_name of this ModifySnapshotAttributeRequest.


        :param snapshot_name: The snapshot_name of this ModifySnapshotAttributeRequest.  # noqa: E501
        :type: str
        """

        self._snapshot_name = snapshot_name

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
        if issubclass(ModifySnapshotAttributeRequest, dict):
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
        if not isinstance(other, ModifySnapshotAttributeRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModifySnapshotAttributeRequest):
            return True

        return self.to_dict() != other.to_dict()
