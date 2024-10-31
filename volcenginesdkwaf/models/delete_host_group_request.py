# coding: utf-8

"""
    waf

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DeleteHostGroupRequest(object):
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
        'host_group_ids': 'list[int]',
        'project_name': 'str'
    }

    attribute_map = {
        'host_group_ids': 'HostGroupIds',
        'project_name': 'ProjectName'
    }

    def __init__(self, host_group_ids=None, project_name=None, _configuration=None):  # noqa: E501
        """DeleteHostGroupRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._host_group_ids = None
        self._project_name = None
        self.discriminator = None

        if host_group_ids is not None:
            self.host_group_ids = host_group_ids
        if project_name is not None:
            self.project_name = project_name

    @property
    def host_group_ids(self):
        """Gets the host_group_ids of this DeleteHostGroupRequest.  # noqa: E501


        :return: The host_group_ids of this DeleteHostGroupRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._host_group_ids

    @host_group_ids.setter
    def host_group_ids(self, host_group_ids):
        """Sets the host_group_ids of this DeleteHostGroupRequest.


        :param host_group_ids: The host_group_ids of this DeleteHostGroupRequest.  # noqa: E501
        :type: list[int]
        """

        self._host_group_ids = host_group_ids

    @property
    def project_name(self):
        """Gets the project_name of this DeleteHostGroupRequest.  # noqa: E501


        :return: The project_name of this DeleteHostGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this DeleteHostGroupRequest.


        :param project_name: The project_name of this DeleteHostGroupRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

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
        if issubclass(DeleteHostGroupRequest, dict):
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
        if not isinstance(other, DeleteHostGroupRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeleteHostGroupRequest):
            return True

        return self.to_dict() != other.to_dict()