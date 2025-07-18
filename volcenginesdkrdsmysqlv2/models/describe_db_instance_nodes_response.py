# coding: utf-8

"""
    rds_mysql_v2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeDBInstanceNodesResponse(object):
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
        'node_infos': 'list[NodeInfoForDescribeDBInstanceNodesOutput]'
    }

    attribute_map = {
        'node_infos': 'NodeInfos'
    }

    def __init__(self, node_infos=None, _configuration=None):  # noqa: E501
        """DescribeDBInstanceNodesResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._node_infos = None
        self.discriminator = None

        if node_infos is not None:
            self.node_infos = node_infos

    @property
    def node_infos(self):
        """Gets the node_infos of this DescribeDBInstanceNodesResponse.  # noqa: E501


        :return: The node_infos of this DescribeDBInstanceNodesResponse.  # noqa: E501
        :rtype: list[NodeInfoForDescribeDBInstanceNodesOutput]
        """
        return self._node_infos

    @node_infos.setter
    def node_infos(self, node_infos):
        """Sets the node_infos of this DescribeDBInstanceNodesResponse.


        :param node_infos: The node_infos of this DescribeDBInstanceNodesResponse.  # noqa: E501
        :type: list[NodeInfoForDescribeDBInstanceNodesOutput]
        """

        self._node_infos = node_infos

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
        if issubclass(DescribeDBInstanceNodesResponse, dict):
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
        if not isinstance(other, DescribeDBInstanceNodesResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeDBInstanceNodesResponse):
            return True

        return self.to_dict() != other.to_dict()
