# coding: utf-8

"""
    bio

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ItemForListNotebookServersOutput(object):
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
        'duration': 'int',
        'last_activity_time': 'int',
        'name': 'str',
        'owner_name': 'str',
        'start_time': 'int',
        'status': 'str',
        'storage_capacity': 'int',
        'user_id': 'int',
        'workspace_id': 'str',
        'workspace_name': 'str'
    }

    attribute_map = {
        'duration': 'Duration',
        'last_activity_time': 'LastActivityTime',
        'name': 'Name',
        'owner_name': 'OwnerName',
        'start_time': 'StartTime',
        'status': 'Status',
        'storage_capacity': 'StorageCapacity',
        'user_id': 'UserID',
        'workspace_id': 'WorkspaceID',
        'workspace_name': 'WorkspaceName'
    }

    def __init__(self, duration=None, last_activity_time=None, name=None, owner_name=None, start_time=None, status=None, storage_capacity=None, user_id=None, workspace_id=None, workspace_name=None, _configuration=None):  # noqa: E501
        """ItemForListNotebookServersOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._duration = None
        self._last_activity_time = None
        self._name = None
        self._owner_name = None
        self._start_time = None
        self._status = None
        self._storage_capacity = None
        self._user_id = None
        self._workspace_id = None
        self._workspace_name = None
        self.discriminator = None

        if duration is not None:
            self.duration = duration
        if last_activity_time is not None:
            self.last_activity_time = last_activity_time
        if name is not None:
            self.name = name
        if owner_name is not None:
            self.owner_name = owner_name
        if start_time is not None:
            self.start_time = start_time
        if status is not None:
            self.status = status
        if storage_capacity is not None:
            self.storage_capacity = storage_capacity
        if user_id is not None:
            self.user_id = user_id
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if workspace_name is not None:
            self.workspace_name = workspace_name

    @property
    def duration(self):
        """Gets the duration of this ItemForListNotebookServersOutput.  # noqa: E501


        :return: The duration of this ItemForListNotebookServersOutput.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this ItemForListNotebookServersOutput.


        :param duration: The duration of this ItemForListNotebookServersOutput.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def last_activity_time(self):
        """Gets the last_activity_time of this ItemForListNotebookServersOutput.  # noqa: E501


        :return: The last_activity_time of this ItemForListNotebookServersOutput.  # noqa: E501
        :rtype: int
        """
        return self._last_activity_time

    @last_activity_time.setter
    def last_activity_time(self, last_activity_time):
        """Sets the last_activity_time of this ItemForListNotebookServersOutput.


        :param last_activity_time: The last_activity_time of this ItemForListNotebookServersOutput.  # noqa: E501
        :type: int
        """

        self._last_activity_time = last_activity_time

    @property
    def name(self):
        """Gets the name of this ItemForListNotebookServersOutput.  # noqa: E501


        :return: The name of this ItemForListNotebookServersOutput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ItemForListNotebookServersOutput.


        :param name: The name of this ItemForListNotebookServersOutput.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def owner_name(self):
        """Gets the owner_name of this ItemForListNotebookServersOutput.  # noqa: E501


        :return: The owner_name of this ItemForListNotebookServersOutput.  # noqa: E501
        :rtype: str
        """
        return self._owner_name

    @owner_name.setter
    def owner_name(self, owner_name):
        """Sets the owner_name of this ItemForListNotebookServersOutput.


        :param owner_name: The owner_name of this ItemForListNotebookServersOutput.  # noqa: E501
        :type: str
        """

        self._owner_name = owner_name

    @property
    def start_time(self):
        """Gets the start_time of this ItemForListNotebookServersOutput.  # noqa: E501


        :return: The start_time of this ItemForListNotebookServersOutput.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ItemForListNotebookServersOutput.


        :param start_time: The start_time of this ItemForListNotebookServersOutput.  # noqa: E501
        :type: int
        """

        self._start_time = start_time

    @property
    def status(self):
        """Gets the status of this ItemForListNotebookServersOutput.  # noqa: E501


        :return: The status of this ItemForListNotebookServersOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ItemForListNotebookServersOutput.


        :param status: The status of this ItemForListNotebookServersOutput.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def storage_capacity(self):
        """Gets the storage_capacity of this ItemForListNotebookServersOutput.  # noqa: E501


        :return: The storage_capacity of this ItemForListNotebookServersOutput.  # noqa: E501
        :rtype: int
        """
        return self._storage_capacity

    @storage_capacity.setter
    def storage_capacity(self, storage_capacity):
        """Sets the storage_capacity of this ItemForListNotebookServersOutput.


        :param storage_capacity: The storage_capacity of this ItemForListNotebookServersOutput.  # noqa: E501
        :type: int
        """

        self._storage_capacity = storage_capacity

    @property
    def user_id(self):
        """Gets the user_id of this ItemForListNotebookServersOutput.  # noqa: E501


        :return: The user_id of this ItemForListNotebookServersOutput.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ItemForListNotebookServersOutput.


        :param user_id: The user_id of this ItemForListNotebookServersOutput.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def workspace_id(self):
        """Gets the workspace_id of this ItemForListNotebookServersOutput.  # noqa: E501


        :return: The workspace_id of this ItemForListNotebookServersOutput.  # noqa: E501
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this ItemForListNotebookServersOutput.


        :param workspace_id: The workspace_id of this ItemForListNotebookServersOutput.  # noqa: E501
        :type: str
        """

        self._workspace_id = workspace_id

    @property
    def workspace_name(self):
        """Gets the workspace_name of this ItemForListNotebookServersOutput.  # noqa: E501


        :return: The workspace_name of this ItemForListNotebookServersOutput.  # noqa: E501
        :rtype: str
        """
        return self._workspace_name

    @workspace_name.setter
    def workspace_name(self, workspace_name):
        """Sets the workspace_name of this ItemForListNotebookServersOutput.


        :param workspace_name: The workspace_name of this ItemForListNotebookServersOutput.  # noqa: E501
        :type: str
        """

        self._workspace_name = workspace_name

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
        if issubclass(ItemForListNotebookServersOutput, dict):
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
        if not isinstance(other, ItemForListNotebookServersOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ItemForListNotebookServersOutput):
            return True

        return self.to_dict() != other.to_dict()
