# coding: utf-8

"""
    rds_mssql

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class CreateTosRestoreRequest(object):
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
        'databases': 'list[DatabaseForCreateTosRestoreInput]',
        'is_online': 'bool',
        'is_replace': 'bool',
        'restore_type': 'str',
        'target_db_instance_id': 'str',
        'tos_object_positions': 'str'
    }

    attribute_map = {
        'databases': 'Databases',
        'is_online': 'IsOnline',
        'is_replace': 'IsReplace',
        'restore_type': 'RestoreType',
        'target_db_instance_id': 'TargetDBInstanceId',
        'tos_object_positions': 'TosObjectPositions'
    }

    def __init__(self, databases=None, is_online=None, is_replace=None, restore_type=None, target_db_instance_id=None, tos_object_positions=None, _configuration=None):  # noqa: E501
        """CreateTosRestoreRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._databases = None
        self._is_online = None
        self._is_replace = None
        self._restore_type = None
        self._target_db_instance_id = None
        self._tos_object_positions = None
        self.discriminator = None

        if databases is not None:
            self.databases = databases
        if is_online is not None:
            self.is_online = is_online
        if is_replace is not None:
            self.is_replace = is_replace
        if restore_type is not None:
            self.restore_type = restore_type
        self.target_db_instance_id = target_db_instance_id
        self.tos_object_positions = tos_object_positions

    @property
    def databases(self):
        """Gets the databases of this CreateTosRestoreRequest.  # noqa: E501


        :return: The databases of this CreateTosRestoreRequest.  # noqa: E501
        :rtype: list[DatabaseForCreateTosRestoreInput]
        """
        return self._databases

    @databases.setter
    def databases(self, databases):
        """Sets the databases of this CreateTosRestoreRequest.


        :param databases: The databases of this CreateTosRestoreRequest.  # noqa: E501
        :type: list[DatabaseForCreateTosRestoreInput]
        """

        self._databases = databases

    @property
    def is_online(self):
        """Gets the is_online of this CreateTosRestoreRequest.  # noqa: E501


        :return: The is_online of this CreateTosRestoreRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_online

    @is_online.setter
    def is_online(self, is_online):
        """Sets the is_online of this CreateTosRestoreRequest.


        :param is_online: The is_online of this CreateTosRestoreRequest.  # noqa: E501
        :type: bool
        """

        self._is_online = is_online

    @property
    def is_replace(self):
        """Gets the is_replace of this CreateTosRestoreRequest.  # noqa: E501


        :return: The is_replace of this CreateTosRestoreRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_replace

    @is_replace.setter
    def is_replace(self, is_replace):
        """Sets the is_replace of this CreateTosRestoreRequest.


        :param is_replace: The is_replace of this CreateTosRestoreRequest.  # noqa: E501
        :type: bool
        """

        self._is_replace = is_replace

    @property
    def restore_type(self):
        """Gets the restore_type of this CreateTosRestoreRequest.  # noqa: E501


        :return: The restore_type of this CreateTosRestoreRequest.  # noqa: E501
        :rtype: str
        """
        return self._restore_type

    @restore_type.setter
    def restore_type(self, restore_type):
        """Sets the restore_type of this CreateTosRestoreRequest.


        :param restore_type: The restore_type of this CreateTosRestoreRequest.  # noqa: E501
        :type: str
        """

        self._restore_type = restore_type

    @property
    def target_db_instance_id(self):
        """Gets the target_db_instance_id of this CreateTosRestoreRequest.  # noqa: E501


        :return: The target_db_instance_id of this CreateTosRestoreRequest.  # noqa: E501
        :rtype: str
        """
        return self._target_db_instance_id

    @target_db_instance_id.setter
    def target_db_instance_id(self, target_db_instance_id):
        """Sets the target_db_instance_id of this CreateTosRestoreRequest.


        :param target_db_instance_id: The target_db_instance_id of this CreateTosRestoreRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and target_db_instance_id is None:
            raise ValueError("Invalid value for `target_db_instance_id`, must not be `None`")  # noqa: E501

        self._target_db_instance_id = target_db_instance_id

    @property
    def tos_object_positions(self):
        """Gets the tos_object_positions of this CreateTosRestoreRequest.  # noqa: E501


        :return: The tos_object_positions of this CreateTosRestoreRequest.  # noqa: E501
        :rtype: str
        """
        return self._tos_object_positions

    @tos_object_positions.setter
    def tos_object_positions(self, tos_object_positions):
        """Sets the tos_object_positions of this CreateTosRestoreRequest.


        :param tos_object_positions: The tos_object_positions of this CreateTosRestoreRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and tos_object_positions is None:
            raise ValueError("Invalid value for `tos_object_positions`, must not be `None`")  # noqa: E501

        self._tos_object_positions = tos_object_positions

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
        if issubclass(CreateTosRestoreRequest, dict):
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
        if not isinstance(other, CreateTosRestoreRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateTosRestoreRequest):
            return True

        return self.to_dict() != other.to_dict()
