# coding: utf-8

"""
    advdefence20230308

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeAttackFlowResponse(object):
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
        'instance_result': 'list[InstanceResultForDescribeAttackFlowOutput]',
        'overall_result': 'OverallResultForDescribeAttackFlowOutput'
    }

    attribute_map = {
        'instance_result': 'InstanceResult',
        'overall_result': 'OverallResult'
    }

    def __init__(self, instance_result=None, overall_result=None, _configuration=None):  # noqa: E501
        """DescribeAttackFlowResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._instance_result = None
        self._overall_result = None
        self.discriminator = None

        if instance_result is not None:
            self.instance_result = instance_result
        if overall_result is not None:
            self.overall_result = overall_result

    @property
    def instance_result(self):
        """Gets the instance_result of this DescribeAttackFlowResponse.  # noqa: E501


        :return: The instance_result of this DescribeAttackFlowResponse.  # noqa: E501
        :rtype: list[InstanceResultForDescribeAttackFlowOutput]
        """
        return self._instance_result

    @instance_result.setter
    def instance_result(self, instance_result):
        """Sets the instance_result of this DescribeAttackFlowResponse.


        :param instance_result: The instance_result of this DescribeAttackFlowResponse.  # noqa: E501
        :type: list[InstanceResultForDescribeAttackFlowOutput]
        """

        self._instance_result = instance_result

    @property
    def overall_result(self):
        """Gets the overall_result of this DescribeAttackFlowResponse.  # noqa: E501


        :return: The overall_result of this DescribeAttackFlowResponse.  # noqa: E501
        :rtype: OverallResultForDescribeAttackFlowOutput
        """
        return self._overall_result

    @overall_result.setter
    def overall_result(self, overall_result):
        """Sets the overall_result of this DescribeAttackFlowResponse.


        :param overall_result: The overall_result of this DescribeAttackFlowResponse.  # noqa: E501
        :type: OverallResultForDescribeAttackFlowOutput
        """

        self._overall_result = overall_result

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
        if issubclass(DescribeAttackFlowResponse, dict):
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
        if not isinstance(other, DescribeAttackFlowResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeAttackFlowResponse):
            return True

        return self.to_dict() != other.to_dict()