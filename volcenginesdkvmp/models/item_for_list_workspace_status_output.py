# coding: utf-8

"""
    vmp

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ItemForListWorkspaceStatusOutput(object):
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
        'id': 'str',
        'instance_type_id': 'str',
        'name': 'str',
        'status': 'str',
        'usage': 'UsageForListWorkspaceStatusOutput'
    }

    attribute_map = {
        'id': 'Id',
        'instance_type_id': 'InstanceTypeId',
        'name': 'Name',
        'status': 'Status',
        'usage': 'Usage'
    }

    def __init__(self, id=None, instance_type_id=None, name=None, status=None, usage=None, _configuration=None):  # noqa: E501
        """ItemForListWorkspaceStatusOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._instance_type_id = None
        self._name = None
        self._status = None
        self._usage = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if instance_type_id is not None:
            self.instance_type_id = instance_type_id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if usage is not None:
            self.usage = usage

    @property
    def id(self):
        """Gets the id of this ItemForListWorkspaceStatusOutput.  # noqa: E501


        :return: The id of this ItemForListWorkspaceStatusOutput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ItemForListWorkspaceStatusOutput.


        :param id: The id of this ItemForListWorkspaceStatusOutput.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def instance_type_id(self):
        """Gets the instance_type_id of this ItemForListWorkspaceStatusOutput.  # noqa: E501


        :return: The instance_type_id of this ItemForListWorkspaceStatusOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_type_id

    @instance_type_id.setter
    def instance_type_id(self, instance_type_id):
        """Sets the instance_type_id of this ItemForListWorkspaceStatusOutput.


        :param instance_type_id: The instance_type_id of this ItemForListWorkspaceStatusOutput.  # noqa: E501
        :type: str
        """

        self._instance_type_id = instance_type_id

    @property
    def name(self):
        """Gets the name of this ItemForListWorkspaceStatusOutput.  # noqa: E501


        :return: The name of this ItemForListWorkspaceStatusOutput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ItemForListWorkspaceStatusOutput.


        :param name: The name of this ItemForListWorkspaceStatusOutput.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def status(self):
        """Gets the status of this ItemForListWorkspaceStatusOutput.  # noqa: E501


        :return: The status of this ItemForListWorkspaceStatusOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ItemForListWorkspaceStatusOutput.


        :param status: The status of this ItemForListWorkspaceStatusOutput.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def usage(self):
        """Gets the usage of this ItemForListWorkspaceStatusOutput.  # noqa: E501


        :return: The usage of this ItemForListWorkspaceStatusOutput.  # noqa: E501
        :rtype: UsageForListWorkspaceStatusOutput
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this ItemForListWorkspaceStatusOutput.


        :param usage: The usage of this ItemForListWorkspaceStatusOutput.  # noqa: E501
        :type: UsageForListWorkspaceStatusOutput
        """

        self._usage = usage

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
        if issubclass(ItemForListWorkspaceStatusOutput, dict):
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
        if not isinstance(other, ItemForListWorkspaceStatusOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ItemForListWorkspaceStatusOutput):
            return True

        return self.to_dict() != other.to_dict()
