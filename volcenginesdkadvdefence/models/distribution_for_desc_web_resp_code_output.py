# coding: utf-8

"""
    advdefence

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DistributionForDescWebRespCodeOutput(object):
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
        'percentage': 'float',
        'resp_code': 'str',
        'total_qps': 'float'
    }

    attribute_map = {
        'percentage': 'Percentage',
        'resp_code': 'RespCode',
        'total_qps': 'TotalQps'
    }

    def __init__(self, percentage=None, resp_code=None, total_qps=None, _configuration=None):  # noqa: E501
        """DistributionForDescWebRespCodeOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._percentage = None
        self._resp_code = None
        self._total_qps = None
        self.discriminator = None

        if percentage is not None:
            self.percentage = percentage
        if resp_code is not None:
            self.resp_code = resp_code
        if total_qps is not None:
            self.total_qps = total_qps

    @property
    def percentage(self):
        """Gets the percentage of this DistributionForDescWebRespCodeOutput.  # noqa: E501


        :return: The percentage of this DistributionForDescWebRespCodeOutput.  # noqa: E501
        :rtype: float
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this DistributionForDescWebRespCodeOutput.


        :param percentage: The percentage of this DistributionForDescWebRespCodeOutput.  # noqa: E501
        :type: float
        """

        self._percentage = percentage

    @property
    def resp_code(self):
        """Gets the resp_code of this DistributionForDescWebRespCodeOutput.  # noqa: E501


        :return: The resp_code of this DistributionForDescWebRespCodeOutput.  # noqa: E501
        :rtype: str
        """
        return self._resp_code

    @resp_code.setter
    def resp_code(self, resp_code):
        """Sets the resp_code of this DistributionForDescWebRespCodeOutput.


        :param resp_code: The resp_code of this DistributionForDescWebRespCodeOutput.  # noqa: E501
        :type: str
        """

        self._resp_code = resp_code

    @property
    def total_qps(self):
        """Gets the total_qps of this DistributionForDescWebRespCodeOutput.  # noqa: E501


        :return: The total_qps of this DistributionForDescWebRespCodeOutput.  # noqa: E501
        :rtype: float
        """
        return self._total_qps

    @total_qps.setter
    def total_qps(self, total_qps):
        """Sets the total_qps of this DistributionForDescWebRespCodeOutput.


        :param total_qps: The total_qps of this DistributionForDescWebRespCodeOutput.  # noqa: E501
        :type: float
        """

        self._total_qps = total_qps

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
        if issubclass(DistributionForDescWebRespCodeOutput, dict):
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
        if not isinstance(other, DistributionForDescWebRespCodeOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DistributionForDescWebRespCodeOutput):
            return True

        return self.to_dict() != other.to_dict()
