# coding: utf-8

"""
    mcs

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class PostApiV1OverviewDescribeAssetInfoRequest(object):
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
        'resource_cloud_account_list': 'list[ResourceCloudAccountListForPostApiV1OverviewDescribeAssetInfoInput]',
        'resource_vendor': 'list[str]'
    }

    attribute_map = {
        'resource_cloud_account_list': 'resource_cloud_account_list',
        'resource_vendor': 'resource_vendor'
    }

    def __init__(self, resource_cloud_account_list=None, resource_vendor=None, _configuration=None):  # noqa: E501
        """PostApiV1OverviewDescribeAssetInfoRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._resource_cloud_account_list = None
        self._resource_vendor = None
        self.discriminator = None

        if resource_cloud_account_list is not None:
            self.resource_cloud_account_list = resource_cloud_account_list
        if resource_vendor is not None:
            self.resource_vendor = resource_vendor

    @property
    def resource_cloud_account_list(self):
        """Gets the resource_cloud_account_list of this PostApiV1OverviewDescribeAssetInfoRequest.  # noqa: E501


        :return: The resource_cloud_account_list of this PostApiV1OverviewDescribeAssetInfoRequest.  # noqa: E501
        :rtype: list[ResourceCloudAccountListForPostApiV1OverviewDescribeAssetInfoInput]
        """
        return self._resource_cloud_account_list

    @resource_cloud_account_list.setter
    def resource_cloud_account_list(self, resource_cloud_account_list):
        """Sets the resource_cloud_account_list of this PostApiV1OverviewDescribeAssetInfoRequest.


        :param resource_cloud_account_list: The resource_cloud_account_list of this PostApiV1OverviewDescribeAssetInfoRequest.  # noqa: E501
        :type: list[ResourceCloudAccountListForPostApiV1OverviewDescribeAssetInfoInput]
        """

        self._resource_cloud_account_list = resource_cloud_account_list

    @property
    def resource_vendor(self):
        """Gets the resource_vendor of this PostApiV1OverviewDescribeAssetInfoRequest.  # noqa: E501


        :return: The resource_vendor of this PostApiV1OverviewDescribeAssetInfoRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._resource_vendor

    @resource_vendor.setter
    def resource_vendor(self, resource_vendor):
        """Sets the resource_vendor of this PostApiV1OverviewDescribeAssetInfoRequest.


        :param resource_vendor: The resource_vendor of this PostApiV1OverviewDescribeAssetInfoRequest.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["volcengine", "aliyun", "huaweicloud", "tencent"]  # noqa: E501
        if (self._configuration.client_side_validation and
                not set(resource_vendor).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `resource_vendor` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(resource_vendor) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._resource_vendor = resource_vendor

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
        if issubclass(PostApiV1OverviewDescribeAssetInfoRequest, dict):
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
        if not isinstance(other, PostApiV1OverviewDescribeAssetInfoRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PostApiV1OverviewDescribeAssetInfoRequest):
            return True

        return self.to_dict() != other.to_dict()
