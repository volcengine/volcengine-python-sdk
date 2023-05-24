# coding: utf-8

"""
    alb

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class CreateLoadBalancerResponse(object):
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
        'load_balancer_id': 'str',
        'request_id': 'str'
    }

    attribute_map = {
        'load_balancer_id': 'LoadBalancerId',
        'request_id': 'RequestId'
    }

    def __init__(self, load_balancer_id=None, request_id=None, _configuration=None):  # noqa: E501
        """CreateLoadBalancerResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._load_balancer_id = None
        self._request_id = None
        self.discriminator = None

        if load_balancer_id is not None:
            self.load_balancer_id = load_balancer_id
        if request_id is not None:
            self.request_id = request_id

    @property
    def load_balancer_id(self):
        """Gets the load_balancer_id of this CreateLoadBalancerResponse.  # noqa: E501


        :return: The load_balancer_id of this CreateLoadBalancerResponse.  # noqa: E501
        :rtype: str
        """
        return self._load_balancer_id

    @load_balancer_id.setter
    def load_balancer_id(self, load_balancer_id):
        """Sets the load_balancer_id of this CreateLoadBalancerResponse.


        :param load_balancer_id: The load_balancer_id of this CreateLoadBalancerResponse.  # noqa: E501
        :type: str
        """

        self._load_balancer_id = load_balancer_id

    @property
    def request_id(self):
        """Gets the request_id of this CreateLoadBalancerResponse.  # noqa: E501


        :return: The request_id of this CreateLoadBalancerResponse.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this CreateLoadBalancerResponse.


        :param request_id: The request_id of this CreateLoadBalancerResponse.  # noqa: E501
        :type: str
        """

        self._request_id = request_id

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
        if issubclass(CreateLoadBalancerResponse, dict):
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
        if not isinstance(other, CreateLoadBalancerResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateLoadBalancerResponse):
            return True

        return self.to_dict() != other.to_dict()
