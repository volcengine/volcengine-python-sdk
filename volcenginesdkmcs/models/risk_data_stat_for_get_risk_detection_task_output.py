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


class RiskDataStatForGetRiskDetectionTaskOutput(object):
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
        'critical': 'int',
        'high': 'int',
        'low': 'int',
        'medium': 'int',
        'security': 'int',
        'total': 'int'
    }

    attribute_map = {
        'critical': 'critical',
        'high': 'high',
        'low': 'low',
        'medium': 'medium',
        'security': 'security',
        'total': 'total'
    }

    def __init__(self, critical=None, high=None, low=None, medium=None, security=None, total=None, _configuration=None):  # noqa: E501
        """RiskDataStatForGetRiskDetectionTaskOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._critical = None
        self._high = None
        self._low = None
        self._medium = None
        self._security = None
        self._total = None
        self.discriminator = None

        if critical is not None:
            self.critical = critical
        if high is not None:
            self.high = high
        if low is not None:
            self.low = low
        if medium is not None:
            self.medium = medium
        if security is not None:
            self.security = security
        if total is not None:
            self.total = total

    @property
    def critical(self):
        """Gets the critical of this RiskDataStatForGetRiskDetectionTaskOutput.  # noqa: E501


        :return: The critical of this RiskDataStatForGetRiskDetectionTaskOutput.  # noqa: E501
        :rtype: int
        """
        return self._critical

    @critical.setter
    def critical(self, critical):
        """Sets the critical of this RiskDataStatForGetRiskDetectionTaskOutput.


        :param critical: The critical of this RiskDataStatForGetRiskDetectionTaskOutput.  # noqa: E501
        :type: int
        """

        self._critical = critical

    @property
    def high(self):
        """Gets the high of this RiskDataStatForGetRiskDetectionTaskOutput.  # noqa: E501


        :return: The high of this RiskDataStatForGetRiskDetectionTaskOutput.  # noqa: E501
        :rtype: int
        """
        return self._high

    @high.setter
    def high(self, high):
        """Sets the high of this RiskDataStatForGetRiskDetectionTaskOutput.


        :param high: The high of this RiskDataStatForGetRiskDetectionTaskOutput.  # noqa: E501
        :type: int
        """

        self._high = high

    @property
    def low(self):
        """Gets the low of this RiskDataStatForGetRiskDetectionTaskOutput.  # noqa: E501


        :return: The low of this RiskDataStatForGetRiskDetectionTaskOutput.  # noqa: E501
        :rtype: int
        """
        return self._low

    @low.setter
    def low(self, low):
        """Sets the low of this RiskDataStatForGetRiskDetectionTaskOutput.


        :param low: The low of this RiskDataStatForGetRiskDetectionTaskOutput.  # noqa: E501
        :type: int
        """

        self._low = low

    @property
    def medium(self):
        """Gets the medium of this RiskDataStatForGetRiskDetectionTaskOutput.  # noqa: E501


        :return: The medium of this RiskDataStatForGetRiskDetectionTaskOutput.  # noqa: E501
        :rtype: int
        """
        return self._medium

    @medium.setter
    def medium(self, medium):
        """Sets the medium of this RiskDataStatForGetRiskDetectionTaskOutput.


        :param medium: The medium of this RiskDataStatForGetRiskDetectionTaskOutput.  # noqa: E501
        :type: int
        """

        self._medium = medium

    @property
    def security(self):
        """Gets the security of this RiskDataStatForGetRiskDetectionTaskOutput.  # noqa: E501


        :return: The security of this RiskDataStatForGetRiskDetectionTaskOutput.  # noqa: E501
        :rtype: int
        """
        return self._security

    @security.setter
    def security(self, security):
        """Sets the security of this RiskDataStatForGetRiskDetectionTaskOutput.


        :param security: The security of this RiskDataStatForGetRiskDetectionTaskOutput.  # noqa: E501
        :type: int
        """

        self._security = security

    @property
    def total(self):
        """Gets the total of this RiskDataStatForGetRiskDetectionTaskOutput.  # noqa: E501


        :return: The total of this RiskDataStatForGetRiskDetectionTaskOutput.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this RiskDataStatForGetRiskDetectionTaskOutput.


        :param total: The total of this RiskDataStatForGetRiskDetectionTaskOutput.  # noqa: E501
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
        if issubclass(RiskDataStatForGetRiskDetectionTaskOutput, dict):
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
        if not isinstance(other, RiskDataStatForGetRiskDetectionTaskOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RiskDataStatForGetRiskDetectionTaskOutput):
            return True

        return self.to_dict() != other.to_dict()
