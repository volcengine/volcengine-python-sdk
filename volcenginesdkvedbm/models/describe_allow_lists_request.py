# coding: utf-8

"""
    vedbm

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeAllowListsRequest(object):
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
        'instance_id': 'str',
        'project_name': 'str',
        'region_id': 'str'
    }

    attribute_map = {
        'instance_id': 'InstanceId',
        'project_name': 'ProjectName',
        'region_id': 'RegionId'
    }

    def __init__(self, instance_id=None, project_name=None, region_id=None, _configuration=None):  # noqa: E501
        """DescribeAllowListsRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._instance_id = None
        self._project_name = None
        self._region_id = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if project_name is not None:
            self.project_name = project_name
        self.region_id = region_id

    @property
    def instance_id(self):
        """Gets the instance_id of this DescribeAllowListsRequest.  # noqa: E501


        :return: The instance_id of this DescribeAllowListsRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this DescribeAllowListsRequest.


        :param instance_id: The instance_id of this DescribeAllowListsRequest.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def project_name(self):
        """Gets the project_name of this DescribeAllowListsRequest.  # noqa: E501


        :return: The project_name of this DescribeAllowListsRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this DescribeAllowListsRequest.


        :param project_name: The project_name of this DescribeAllowListsRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def region_id(self):
        """Gets the region_id of this DescribeAllowListsRequest.  # noqa: E501


        :return: The region_id of this DescribeAllowListsRequest.  # noqa: E501
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this DescribeAllowListsRequest.


        :param region_id: The region_id of this DescribeAllowListsRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and region_id is None:
            raise ValueError("Invalid value for `region_id`, must not be `None`")  # noqa: E501

        self._region_id = region_id

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
        if issubclass(DescribeAllowListsRequest, dict):
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
        if not isinstance(other, DescribeAllowListsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeAllowListsRequest):
            return True

        return self.to_dict() != other.to_dict()
