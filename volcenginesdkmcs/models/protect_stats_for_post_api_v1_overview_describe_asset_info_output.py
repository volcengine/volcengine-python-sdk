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


class ProtectStatsForPostApiV1OverviewDescribeAssetInfoOutput(object):
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
        'not_protect': 'int',
        'protect': 'int',
        'protect_exception': 'int',
        'unknown': 'int'
    }

    attribute_map = {
        'not_protect': 'not_protect',
        'protect': 'protect',
        'protect_exception': 'protect_exception',
        'unknown': 'unknown'
    }

    def __init__(self, not_protect=None, protect=None, protect_exception=None, unknown=None, _configuration=None):  # noqa: E501
        """ProtectStatsForPostApiV1OverviewDescribeAssetInfoOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._not_protect = None
        self._protect = None
        self._protect_exception = None
        self._unknown = None
        self.discriminator = None

        if not_protect is not None:
            self.not_protect = not_protect
        if protect is not None:
            self.protect = protect
        if protect_exception is not None:
            self.protect_exception = protect_exception
        if unknown is not None:
            self.unknown = unknown

    @property
    def not_protect(self):
        """Gets the not_protect of this ProtectStatsForPostApiV1OverviewDescribeAssetInfoOutput.  # noqa: E501


        :return: The not_protect of this ProtectStatsForPostApiV1OverviewDescribeAssetInfoOutput.  # noqa: E501
        :rtype: int
        """
        return self._not_protect

    @not_protect.setter
    def not_protect(self, not_protect):
        """Sets the not_protect of this ProtectStatsForPostApiV1OverviewDescribeAssetInfoOutput.


        :param not_protect: The not_protect of this ProtectStatsForPostApiV1OverviewDescribeAssetInfoOutput.  # noqa: E501
        :type: int
        """

        self._not_protect = not_protect

    @property
    def protect(self):
        """Gets the protect of this ProtectStatsForPostApiV1OverviewDescribeAssetInfoOutput.  # noqa: E501


        :return: The protect of this ProtectStatsForPostApiV1OverviewDescribeAssetInfoOutput.  # noqa: E501
        :rtype: int
        """
        return self._protect

    @protect.setter
    def protect(self, protect):
        """Sets the protect of this ProtectStatsForPostApiV1OverviewDescribeAssetInfoOutput.


        :param protect: The protect of this ProtectStatsForPostApiV1OverviewDescribeAssetInfoOutput.  # noqa: E501
        :type: int
        """

        self._protect = protect

    @property
    def protect_exception(self):
        """Gets the protect_exception of this ProtectStatsForPostApiV1OverviewDescribeAssetInfoOutput.  # noqa: E501


        :return: The protect_exception of this ProtectStatsForPostApiV1OverviewDescribeAssetInfoOutput.  # noqa: E501
        :rtype: int
        """
        return self._protect_exception

    @protect_exception.setter
    def protect_exception(self, protect_exception):
        """Sets the protect_exception of this ProtectStatsForPostApiV1OverviewDescribeAssetInfoOutput.


        :param protect_exception: The protect_exception of this ProtectStatsForPostApiV1OverviewDescribeAssetInfoOutput.  # noqa: E501
        :type: int
        """

        self._protect_exception = protect_exception

    @property
    def unknown(self):
        """Gets the unknown of this ProtectStatsForPostApiV1OverviewDescribeAssetInfoOutput.  # noqa: E501


        :return: The unknown of this ProtectStatsForPostApiV1OverviewDescribeAssetInfoOutput.  # noqa: E501
        :rtype: int
        """
        return self._unknown

    @unknown.setter
    def unknown(self, unknown):
        """Sets the unknown of this ProtectStatsForPostApiV1OverviewDescribeAssetInfoOutput.


        :param unknown: The unknown of this ProtectStatsForPostApiV1OverviewDescribeAssetInfoOutput.  # noqa: E501
        :type: int
        """

        self._unknown = unknown

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
        if issubclass(ProtectStatsForPostApiV1OverviewDescribeAssetInfoOutput, dict):
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
        if not isinstance(other, ProtectStatsForPostApiV1OverviewDescribeAssetInfoOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProtectStatsForPostApiV1OverviewDescribeAssetInfoOutput):
            return True

        return self.to_dict() != other.to_dict()
