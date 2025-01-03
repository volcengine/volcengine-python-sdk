# coding: utf-8

"""
    vmp

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class UsageForListWorkspaceStatusOutput(object):
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
        'active_series': 'int',
        'ingested_samples_per_second': 'float'
    }

    attribute_map = {
        'active_series': 'ActiveSeries',
        'ingested_samples_per_second': 'IngestedSamplesPerSecond'
    }

    def __init__(self, active_series=None, ingested_samples_per_second=None, _configuration=None):  # noqa: E501
        """UsageForListWorkspaceStatusOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._active_series = None
        self._ingested_samples_per_second = None
        self.discriminator = None

        if active_series is not None:
            self.active_series = active_series
        if ingested_samples_per_second is not None:
            self.ingested_samples_per_second = ingested_samples_per_second

    @property
    def active_series(self):
        """Gets the active_series of this UsageForListWorkspaceStatusOutput.  # noqa: E501


        :return: The active_series of this UsageForListWorkspaceStatusOutput.  # noqa: E501
        :rtype: int
        """
        return self._active_series

    @active_series.setter
    def active_series(self, active_series):
        """Sets the active_series of this UsageForListWorkspaceStatusOutput.


        :param active_series: The active_series of this UsageForListWorkspaceStatusOutput.  # noqa: E501
        :type: int
        """

        self._active_series = active_series

    @property
    def ingested_samples_per_second(self):
        """Gets the ingested_samples_per_second of this UsageForListWorkspaceStatusOutput.  # noqa: E501


        :return: The ingested_samples_per_second of this UsageForListWorkspaceStatusOutput.  # noqa: E501
        :rtype: float
        """
        return self._ingested_samples_per_second

    @ingested_samples_per_second.setter
    def ingested_samples_per_second(self, ingested_samples_per_second):
        """Sets the ingested_samples_per_second of this UsageForListWorkspaceStatusOutput.


        :param ingested_samples_per_second: The ingested_samples_per_second of this UsageForListWorkspaceStatusOutput.  # noqa: E501
        :type: float
        """

        self._ingested_samples_per_second = ingested_samples_per_second

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
        if issubclass(UsageForListWorkspaceStatusOutput, dict):
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
        if not isinstance(other, UsageForListWorkspaceStatusOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UsageForListWorkspaceStatusOutput):
            return True

        return self.to_dict() != other.to_dict()
