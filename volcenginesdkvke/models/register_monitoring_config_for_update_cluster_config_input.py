# coding: utf-8

"""
    vke

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class RegisterMonitoringConfigForUpdateClusterConfigInput(object):
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
        'query_url': 'str',
        'remote_write_url': 'str',
        'workspace_id': 'str'
    }

    attribute_map = {
        'query_url': 'QueryUrl',
        'remote_write_url': 'RemoteWriteUrl',
        'workspace_id': 'WorkspaceId'
    }

    def __init__(self, query_url=None, remote_write_url=None, workspace_id=None, _configuration=None):  # noqa: E501
        """RegisterMonitoringConfigForUpdateClusterConfigInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._query_url = None
        self._remote_write_url = None
        self._workspace_id = None
        self.discriminator = None

        if query_url is not None:
            self.query_url = query_url
        if remote_write_url is not None:
            self.remote_write_url = remote_write_url
        if workspace_id is not None:
            self.workspace_id = workspace_id

    @property
    def query_url(self):
        """Gets the query_url of this RegisterMonitoringConfigForUpdateClusterConfigInput.  # noqa: E501


        :return: The query_url of this RegisterMonitoringConfigForUpdateClusterConfigInput.  # noqa: E501
        :rtype: str
        """
        return self._query_url

    @query_url.setter
    def query_url(self, query_url):
        """Sets the query_url of this RegisterMonitoringConfigForUpdateClusterConfigInput.


        :param query_url: The query_url of this RegisterMonitoringConfigForUpdateClusterConfigInput.  # noqa: E501
        :type: str
        """

        self._query_url = query_url

    @property
    def remote_write_url(self):
        """Gets the remote_write_url of this RegisterMonitoringConfigForUpdateClusterConfigInput.  # noqa: E501


        :return: The remote_write_url of this RegisterMonitoringConfigForUpdateClusterConfigInput.  # noqa: E501
        :rtype: str
        """
        return self._remote_write_url

    @remote_write_url.setter
    def remote_write_url(self, remote_write_url):
        """Sets the remote_write_url of this RegisterMonitoringConfigForUpdateClusterConfigInput.


        :param remote_write_url: The remote_write_url of this RegisterMonitoringConfigForUpdateClusterConfigInput.  # noqa: E501
        :type: str
        """

        self._remote_write_url = remote_write_url

    @property
    def workspace_id(self):
        """Gets the workspace_id of this RegisterMonitoringConfigForUpdateClusterConfigInput.  # noqa: E501


        :return: The workspace_id of this RegisterMonitoringConfigForUpdateClusterConfigInput.  # noqa: E501
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this RegisterMonitoringConfigForUpdateClusterConfigInput.


        :param workspace_id: The workspace_id of this RegisterMonitoringConfigForUpdateClusterConfigInput.  # noqa: E501
        :type: str
        """

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
        if issubclass(RegisterMonitoringConfigForUpdateClusterConfigInput, dict):
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
        if not isinstance(other, RegisterMonitoringConfigForUpdateClusterConfigInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RegisterMonitoringConfigForUpdateClusterConfigInput):
            return True

        return self.to_dict() != other.to_dict()
