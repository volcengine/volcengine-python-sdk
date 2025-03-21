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


class GlobalAcceleratorForModifyLoadBalancerAttributesInput(object):
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
        'accelerator_id': 'str',
        'accelerator_listener_id': 'str',
        'endpoint_group_id': 'str',
        'weight': 'int'
    }

    attribute_map = {
        'accelerator_id': 'AcceleratorId',
        'accelerator_listener_id': 'AcceleratorListenerId',
        'endpoint_group_id': 'EndpointGroupId',
        'weight': 'Weight'
    }

    def __init__(self, accelerator_id=None, accelerator_listener_id=None, endpoint_group_id=None, weight=None, _configuration=None):  # noqa: E501
        """GlobalAcceleratorForModifyLoadBalancerAttributesInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._accelerator_id = None
        self._accelerator_listener_id = None
        self._endpoint_group_id = None
        self._weight = None
        self.discriminator = None

        if accelerator_id is not None:
            self.accelerator_id = accelerator_id
        if accelerator_listener_id is not None:
            self.accelerator_listener_id = accelerator_listener_id
        if endpoint_group_id is not None:
            self.endpoint_group_id = endpoint_group_id
        if weight is not None:
            self.weight = weight

    @property
    def accelerator_id(self):
        """Gets the accelerator_id of this GlobalAcceleratorForModifyLoadBalancerAttributesInput.  # noqa: E501


        :return: The accelerator_id of this GlobalAcceleratorForModifyLoadBalancerAttributesInput.  # noqa: E501
        :rtype: str
        """
        return self._accelerator_id

    @accelerator_id.setter
    def accelerator_id(self, accelerator_id):
        """Sets the accelerator_id of this GlobalAcceleratorForModifyLoadBalancerAttributesInput.


        :param accelerator_id: The accelerator_id of this GlobalAcceleratorForModifyLoadBalancerAttributesInput.  # noqa: E501
        :type: str
        """

        self._accelerator_id = accelerator_id

    @property
    def accelerator_listener_id(self):
        """Gets the accelerator_listener_id of this GlobalAcceleratorForModifyLoadBalancerAttributesInput.  # noqa: E501


        :return: The accelerator_listener_id of this GlobalAcceleratorForModifyLoadBalancerAttributesInput.  # noqa: E501
        :rtype: str
        """
        return self._accelerator_listener_id

    @accelerator_listener_id.setter
    def accelerator_listener_id(self, accelerator_listener_id):
        """Sets the accelerator_listener_id of this GlobalAcceleratorForModifyLoadBalancerAttributesInput.


        :param accelerator_listener_id: The accelerator_listener_id of this GlobalAcceleratorForModifyLoadBalancerAttributesInput.  # noqa: E501
        :type: str
        """

        self._accelerator_listener_id = accelerator_listener_id

    @property
    def endpoint_group_id(self):
        """Gets the endpoint_group_id of this GlobalAcceleratorForModifyLoadBalancerAttributesInput.  # noqa: E501


        :return: The endpoint_group_id of this GlobalAcceleratorForModifyLoadBalancerAttributesInput.  # noqa: E501
        :rtype: str
        """
        return self._endpoint_group_id

    @endpoint_group_id.setter
    def endpoint_group_id(self, endpoint_group_id):
        """Sets the endpoint_group_id of this GlobalAcceleratorForModifyLoadBalancerAttributesInput.


        :param endpoint_group_id: The endpoint_group_id of this GlobalAcceleratorForModifyLoadBalancerAttributesInput.  # noqa: E501
        :type: str
        """

        self._endpoint_group_id = endpoint_group_id

    @property
    def weight(self):
        """Gets the weight of this GlobalAcceleratorForModifyLoadBalancerAttributesInput.  # noqa: E501


        :return: The weight of this GlobalAcceleratorForModifyLoadBalancerAttributesInput.  # noqa: E501
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this GlobalAcceleratorForModifyLoadBalancerAttributesInput.


        :param weight: The weight of this GlobalAcceleratorForModifyLoadBalancerAttributesInput.  # noqa: E501
        :type: int
        """

        self._weight = weight

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
        if issubclass(GlobalAcceleratorForModifyLoadBalancerAttributesInput, dict):
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
        if not isinstance(other, GlobalAcceleratorForModifyLoadBalancerAttributesInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GlobalAcceleratorForModifyLoadBalancerAttributesInput):
            return True

        return self.to_dict() != other.to_dict()
