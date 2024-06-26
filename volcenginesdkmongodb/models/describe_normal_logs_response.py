# coding: utf-8

"""
    mongodb

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeNormalLogsResponse(object):
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
        'context': 'str',
        'datas': 'list[DataForDescribeNormalLogsOutput]',
        'list_over': 'bool',
        'total': 'int'
    }

    attribute_map = {
        'context': 'Context',
        'datas': 'Datas',
        'list_over': 'ListOver',
        'total': 'Total'
    }

    def __init__(self, context=None, datas=None, list_over=None, total=None, _configuration=None):  # noqa: E501
        """DescribeNormalLogsResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._context = None
        self._datas = None
        self._list_over = None
        self._total = None
        self.discriminator = None

        if context is not None:
            self.context = context
        if datas is not None:
            self.datas = datas
        if list_over is not None:
            self.list_over = list_over
        if total is not None:
            self.total = total

    @property
    def context(self):
        """Gets the context of this DescribeNormalLogsResponse.  # noqa: E501


        :return: The context of this DescribeNormalLogsResponse.  # noqa: E501
        :rtype: str
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this DescribeNormalLogsResponse.


        :param context: The context of this DescribeNormalLogsResponse.  # noqa: E501
        :type: str
        """

        self._context = context

    @property
    def datas(self):
        """Gets the datas of this DescribeNormalLogsResponse.  # noqa: E501


        :return: The datas of this DescribeNormalLogsResponse.  # noqa: E501
        :rtype: list[DataForDescribeNormalLogsOutput]
        """
        return self._datas

    @datas.setter
    def datas(self, datas):
        """Sets the datas of this DescribeNormalLogsResponse.


        :param datas: The datas of this DescribeNormalLogsResponse.  # noqa: E501
        :type: list[DataForDescribeNormalLogsOutput]
        """

        self._datas = datas

    @property
    def list_over(self):
        """Gets the list_over of this DescribeNormalLogsResponse.  # noqa: E501


        :return: The list_over of this DescribeNormalLogsResponse.  # noqa: E501
        :rtype: bool
        """
        return self._list_over

    @list_over.setter
    def list_over(self, list_over):
        """Sets the list_over of this DescribeNormalLogsResponse.


        :param list_over: The list_over of this DescribeNormalLogsResponse.  # noqa: E501
        :type: bool
        """

        self._list_over = list_over

    @property
    def total(self):
        """Gets the total of this DescribeNormalLogsResponse.  # noqa: E501


        :return: The total of this DescribeNormalLogsResponse.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this DescribeNormalLogsResponse.


        :param total: The total of this DescribeNormalLogsResponse.  # noqa: E501
        :type: int
        """

        self._total = total

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
        if issubclass(DescribeNormalLogsResponse, dict):
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
        if not isinstance(other, DescribeNormalLogsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeNormalLogsResponse):
            return True

        return self.to_dict() != other.to_dict()
