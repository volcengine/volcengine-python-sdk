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


class ClonePublicWorkspaceRequest(object):
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
        'cover_path': 'str',
        'description': 'str',
        'labels': 'list[str]',
        'name': 'str',
        'workspace_id': 'str'
    }

    attribute_map = {
        'cover_path': 'CoverPath',
        'description': 'Description',
        'labels': 'Labels',
        'name': 'Name',
        'workspace_id': 'WorkspaceID'
    }

    def __init__(self, cover_path=None, description=None, labels=None, name=None, workspace_id=None, _configuration=None):  # noqa: E501
        """ClonePublicWorkspaceRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cover_path = None
        self._description = None
        self._labels = None
        self._name = None
        self._workspace_id = None
        self.discriminator = None

        if cover_path is not None:
            self.cover_path = cover_path
        self.description = description
        if labels is not None:
            self.labels = labels
        self.name = name
        self.workspace_id = workspace_id

    @property
    def cover_path(self):
        """Gets the cover_path of this ClonePublicWorkspaceRequest.  # noqa: E501


        :return: The cover_path of this ClonePublicWorkspaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._cover_path

    @cover_path.setter
    def cover_path(self, cover_path):
        """Sets the cover_path of this ClonePublicWorkspaceRequest.


        :param cover_path: The cover_path of this ClonePublicWorkspaceRequest.  # noqa: E501
        :type: str
        """

        self._cover_path = cover_path

    @property
    def description(self):
        """Gets the description of this ClonePublicWorkspaceRequest.  # noqa: E501


        :return: The description of this ClonePublicWorkspaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ClonePublicWorkspaceRequest.


        :param description: The description of this ClonePublicWorkspaceRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                description is not None and len(description) > 1000):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1000`")  # noqa: E501
        if (self._configuration.client_side_validation and
                description is not None and len(description) < 1):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `1`")  # noqa: E501

        self._description = description

    @property
    def labels(self):
        """Gets the labels of this ClonePublicWorkspaceRequest.  # noqa: E501


        :return: The labels of this ClonePublicWorkspaceRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this ClonePublicWorkspaceRequest.


        :param labels: The labels of this ClonePublicWorkspaceRequest.  # noqa: E501
        :type: list[str]
        """

        self._labels = labels

    @property
    def name(self):
        """Gets the name of this ClonePublicWorkspaceRequest.  # noqa: E501


        :return: The name of this ClonePublicWorkspaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClonePublicWorkspaceRequest.


        :param name: The name of this ClonePublicWorkspaceRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and len(name) > 200):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `200`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def workspace_id(self):
        """Gets the workspace_id of this ClonePublicWorkspaceRequest.  # noqa: E501


        :return: The workspace_id of this ClonePublicWorkspaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this ClonePublicWorkspaceRequest.


        :param workspace_id: The workspace_id of this ClonePublicWorkspaceRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and workspace_id is None:
            raise ValueError("Invalid value for `workspace_id`, must not be `None`")  # noqa: E501

        self._workspace_id = workspace_id

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
        if issubclass(ClonePublicWorkspaceRequest, dict):
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
        if not isinstance(other, ClonePublicWorkspaceRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClonePublicWorkspaceRequest):
            return True

        return self.to_dict() != other.to_dict()
