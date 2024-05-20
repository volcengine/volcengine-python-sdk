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


class CreateSnapshotGroupRequest(object):
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
        'client_token': 'str',
        'description': 'str',
        'instance_id': 'str',
        'name': 'str',
        'project_name': 'str',
        'tags': 'list[TagForCreateSnapshotGroupInput]',
        'volume_ids': 'list[str]'
    }

    attribute_map = {
        'client_token': 'ClientToken',
        'description': 'Description',
        'instance_id': 'InstanceId',
        'name': 'Name',
        'project_name': 'ProjectName',
        'tags': 'Tags',
        'volume_ids': 'VolumeIds'
    }

    def __init__(self, client_token=None, description=None, instance_id=None, name=None, project_name=None, tags=None, volume_ids=None, _configuration=None):  # noqa: E501
        """CreateSnapshotGroupRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._client_token = None
        self._description = None
        self._instance_id = None
        self._name = None
        self._project_name = None
        self._tags = None
        self._volume_ids = None
        self.discriminator = None

        if client_token is not None:
            self.client_token = client_token
        if description is not None:
            self.description = description
        if instance_id is not None:
            self.instance_id = instance_id
        if name is not None:
            self.name = name
        if project_name is not None:
            self.project_name = project_name
        if tags is not None:
            self.tags = tags
        if volume_ids is not None:
            self.volume_ids = volume_ids

    @property
    def client_token(self):
        """Gets the client_token of this CreateSnapshotGroupRequest.  # noqa: E501


        :return: The client_token of this CreateSnapshotGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_token

    @client_token.setter
    def client_token(self, client_token):
        """Sets the client_token of this CreateSnapshotGroupRequest.


        :param client_token: The client_token of this CreateSnapshotGroupRequest.  # noqa: E501
        :type: str
        """

        self._client_token = client_token

    @property
    def description(self):
        """Gets the description of this CreateSnapshotGroupRequest.  # noqa: E501


        :return: The description of this CreateSnapshotGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateSnapshotGroupRequest.


        :param description: The description of this CreateSnapshotGroupRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def instance_id(self):
        """Gets the instance_id of this CreateSnapshotGroupRequest.  # noqa: E501


        :return: The instance_id of this CreateSnapshotGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this CreateSnapshotGroupRequest.


        :param instance_id: The instance_id of this CreateSnapshotGroupRequest.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def name(self):
        """Gets the name of this CreateSnapshotGroupRequest.  # noqa: E501


        :return: The name of this CreateSnapshotGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateSnapshotGroupRequest.


        :param name: The name of this CreateSnapshotGroupRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def project_name(self):
        """Gets the project_name of this CreateSnapshotGroupRequest.  # noqa: E501


        :return: The project_name of this CreateSnapshotGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this CreateSnapshotGroupRequest.


        :param project_name: The project_name of this CreateSnapshotGroupRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def tags(self):
        """Gets the tags of this CreateSnapshotGroupRequest.  # noqa: E501


        :return: The tags of this CreateSnapshotGroupRequest.  # noqa: E501
        :rtype: list[TagForCreateSnapshotGroupInput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateSnapshotGroupRequest.


        :param tags: The tags of this CreateSnapshotGroupRequest.  # noqa: E501
        :type: list[TagForCreateSnapshotGroupInput]
        """

        self._tags = tags

    @property
    def volume_ids(self):
        """Gets the volume_ids of this CreateSnapshotGroupRequest.  # noqa: E501


        :return: The volume_ids of this CreateSnapshotGroupRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._volume_ids

    @volume_ids.setter
    def volume_ids(self, volume_ids):
        """Sets the volume_ids of this CreateSnapshotGroupRequest.


        :param volume_ids: The volume_ids of this CreateSnapshotGroupRequest.  # noqa: E501
        :type: list[str]
        """

        self._volume_ids = volume_ids

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
        if issubclass(CreateSnapshotGroupRequest, dict):
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
        if not isinstance(other, CreateSnapshotGroupRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateSnapshotGroupRequest):
            return True

        return self.to_dict() != other.to_dict()