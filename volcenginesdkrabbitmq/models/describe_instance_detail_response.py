# coding: utf-8

"""
    rabbitmq

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeInstanceDetailResponse(object):
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
        'basic_instance_info': 'BasicInstanceInfoForDescribeInstanceDetailOutput',
        'endpoints': 'list[EndpointForDescribeInstanceDetailOutput]'
    }

    attribute_map = {
        'basic_instance_info': 'BasicInstanceInfo',
        'endpoints': 'Endpoints'
    }

    def __init__(self, basic_instance_info=None, endpoints=None, _configuration=None):  # noqa: E501
        """DescribeInstanceDetailResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._basic_instance_info = None
        self._endpoints = None
        self.discriminator = None

        if basic_instance_info is not None:
            self.basic_instance_info = basic_instance_info
        if endpoints is not None:
            self.endpoints = endpoints

    @property
    def basic_instance_info(self):
        """Gets the basic_instance_info of this DescribeInstanceDetailResponse.  # noqa: E501


        :return: The basic_instance_info of this DescribeInstanceDetailResponse.  # noqa: E501
        :rtype: BasicInstanceInfoForDescribeInstanceDetailOutput
        """
        return self._basic_instance_info

    @basic_instance_info.setter
    def basic_instance_info(self, basic_instance_info):
        """Sets the basic_instance_info of this DescribeInstanceDetailResponse.


        :param basic_instance_info: The basic_instance_info of this DescribeInstanceDetailResponse.  # noqa: E501
        :type: BasicInstanceInfoForDescribeInstanceDetailOutput
        """

        self._basic_instance_info = basic_instance_info

    @property
    def endpoints(self):
        """Gets the endpoints of this DescribeInstanceDetailResponse.  # noqa: E501


        :return: The endpoints of this DescribeInstanceDetailResponse.  # noqa: E501
        :rtype: list[EndpointForDescribeInstanceDetailOutput]
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        """Sets the endpoints of this DescribeInstanceDetailResponse.


        :param endpoints: The endpoints of this DescribeInstanceDetailResponse.  # noqa: E501
        :type: list[EndpointForDescribeInstanceDetailOutput]
        """

        self._endpoints = endpoints

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
        if issubclass(DescribeInstanceDetailResponse, dict):
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
        if not isinstance(other, DescribeInstanceDetailResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeInstanceDetailResponse):
            return True

        return self.to_dict() != other.to_dict()
