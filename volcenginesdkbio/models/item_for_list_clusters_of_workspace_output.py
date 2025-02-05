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


class ItemForListClustersOfWorkspaceOutput(object):
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
        'bind_time': 'int',
        'cluster_info': 'ClusterInfoForListClustersOfWorkspaceOutput',
        'type': 'str'
    }

    attribute_map = {
        'bind_time': 'BindTime',
        'cluster_info': 'ClusterInfo',
        'type': 'Type'
    }

    def __init__(self, bind_time=None, cluster_info=None, type=None, _configuration=None):  # noqa: E501
        """ItemForListClustersOfWorkspaceOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bind_time = None
        self._cluster_info = None
        self._type = None
        self.discriminator = None

        if bind_time is not None:
            self.bind_time = bind_time
        if cluster_info is not None:
            self.cluster_info = cluster_info
        if type is not None:
            self.type = type

    @property
    def bind_time(self):
        """Gets the bind_time of this ItemForListClustersOfWorkspaceOutput.  # noqa: E501


        :return: The bind_time of this ItemForListClustersOfWorkspaceOutput.  # noqa: E501
        :rtype: int
        """
        return self._bind_time

    @bind_time.setter
    def bind_time(self, bind_time):
        """Sets the bind_time of this ItemForListClustersOfWorkspaceOutput.


        :param bind_time: The bind_time of this ItemForListClustersOfWorkspaceOutput.  # noqa: E501
        :type: int
        """

        self._bind_time = bind_time

    @property
    def cluster_info(self):
        """Gets the cluster_info of this ItemForListClustersOfWorkspaceOutput.  # noqa: E501


        :return: The cluster_info of this ItemForListClustersOfWorkspaceOutput.  # noqa: E501
        :rtype: ClusterInfoForListClustersOfWorkspaceOutput
        """
        return self._cluster_info

    @cluster_info.setter
    def cluster_info(self, cluster_info):
        """Sets the cluster_info of this ItemForListClustersOfWorkspaceOutput.


        :param cluster_info: The cluster_info of this ItemForListClustersOfWorkspaceOutput.  # noqa: E501
        :type: ClusterInfoForListClustersOfWorkspaceOutput
        """

        self._cluster_info = cluster_info

    @property
    def type(self):
        """Gets the type of this ItemForListClustersOfWorkspaceOutput.  # noqa: E501


        :return: The type of this ItemForListClustersOfWorkspaceOutput.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ItemForListClustersOfWorkspaceOutput.


        :param type: The type of this ItemForListClustersOfWorkspaceOutput.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(ItemForListClustersOfWorkspaceOutput, dict):
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
        if not isinstance(other, ItemForListClustersOfWorkspaceOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ItemForListClustersOfWorkspaceOutput):
            return True

        return self.to_dict() != other.to_dict()
