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


class DeleteIpGroupRequest(object):
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
        'ip_group_ids': 'list[int]',
        'project_name': 'str'
    }

    attribute_map = {
        'ip_group_ids': 'IpGroupIds',
        'project_name': 'ProjectName'
    }

    def __init__(self, ip_group_ids=None, project_name=None, _configuration=None):  # noqa: E501
        """DeleteIpGroupRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._ip_group_ids = None
        self._project_name = None
        self.discriminator = None

        if ip_group_ids is not None:
            self.ip_group_ids = ip_group_ids
        if project_name is not None:
            self.project_name = project_name

    @property
    def ip_group_ids(self):
        """Gets the ip_group_ids of this DeleteIpGroupRequest.  # noqa: E501


        :return: The ip_group_ids of this DeleteIpGroupRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._ip_group_ids

    @ip_group_ids.setter
    def ip_group_ids(self, ip_group_ids):
        """Sets the ip_group_ids of this DeleteIpGroupRequest.


        :param ip_group_ids: The ip_group_ids of this DeleteIpGroupRequest.  # noqa: E501
        :type: list[int]
        """

        self._ip_group_ids = ip_group_ids

    @property
    def project_name(self):
        """Gets the project_name of this DeleteIpGroupRequest.  # noqa: E501


        :return: The project_name of this DeleteIpGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this DeleteIpGroupRequest.


        :param project_name: The project_name of this DeleteIpGroupRequest.  # noqa: E501
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
        if issubclass(DeleteIpGroupRequest, dict):
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
        if not isinstance(other, DeleteIpGroupRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeleteIpGroupRequest):
            return True

        return self.to_dict() != other.to_dict()
