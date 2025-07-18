# coding: utf-8

"""
    livesaas20230801

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class GetVideoLibraryFolderTreeResponse(object):
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
        'folder_node': 'FolderNodeForGetVideoLibraryFolderTreeOutput'
    }

    attribute_map = {
        'folder_node': 'FolderNode'
    }

    def __init__(self, folder_node=None, _configuration=None):  # noqa: E501
        """GetVideoLibraryFolderTreeResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._folder_node = None
        self.discriminator = None

        if folder_node is not None:
            self.folder_node = folder_node

    @property
    def folder_node(self):
        """Gets the folder_node of this GetVideoLibraryFolderTreeResponse.  # noqa: E501


        :return: The folder_node of this GetVideoLibraryFolderTreeResponse.  # noqa: E501
        :rtype: FolderNodeForGetVideoLibraryFolderTreeOutput
        """
        return self._folder_node

    @folder_node.setter
    def folder_node(self, folder_node):
        """Sets the folder_node of this GetVideoLibraryFolderTreeResponse.


        :param folder_node: The folder_node of this GetVideoLibraryFolderTreeResponse.  # noqa: E501
        :type: FolderNodeForGetVideoLibraryFolderTreeOutput
        """

        self._folder_node = folder_node

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
        if issubclass(GetVideoLibraryFolderTreeResponse, dict):
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
        if not isinstance(other, GetVideoLibraryFolderTreeResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetVideoLibraryFolderTreeResponse):
            return True

        return self.to_dict() != other.to_dict()
