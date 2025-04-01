# coding: utf-8

"""
    edx

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class EnableRouteAggregationRequest(object):
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
        'aggregation_cidr': 'str',
        'direction': 'str',
        'vif_instance_id': 'str'
    }

    attribute_map = {
        'aggregation_cidr': 'AggregationCidr',
        'direction': 'Direction',
        'vif_instance_id': 'VIFInstanceId'
    }

    def __init__(self, aggregation_cidr=None, direction=None, vif_instance_id=None, _configuration=None):  # noqa: E501
        """EnableRouteAggregationRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._aggregation_cidr = None
        self._direction = None
        self._vif_instance_id = None
        self.discriminator = None

        self.aggregation_cidr = aggregation_cidr
        self.direction = direction
        self.vif_instance_id = vif_instance_id

    @property
    def aggregation_cidr(self):
        """Gets the aggregation_cidr of this EnableRouteAggregationRequest.  # noqa: E501


        :return: The aggregation_cidr of this EnableRouteAggregationRequest.  # noqa: E501
        :rtype: str
        """
        return self._aggregation_cidr

    @aggregation_cidr.setter
    def aggregation_cidr(self, aggregation_cidr):
        """Sets the aggregation_cidr of this EnableRouteAggregationRequest.


        :param aggregation_cidr: The aggregation_cidr of this EnableRouteAggregationRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and aggregation_cidr is None:
            raise ValueError("Invalid value for `aggregation_cidr`, must not be `None`")  # noqa: E501

        self._aggregation_cidr = aggregation_cidr

    @property
    def direction(self):
        """Gets the direction of this EnableRouteAggregationRequest.  # noqa: E501


        :return: The direction of this EnableRouteAggregationRequest.  # noqa: E501
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this EnableRouteAggregationRequest.


        :param direction: The direction of this EnableRouteAggregationRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and direction is None:
            raise ValueError("Invalid value for `direction`, must not be `None`")  # noqa: E501

        self._direction = direction

    @property
    def vif_instance_id(self):
        """Gets the vif_instance_id of this EnableRouteAggregationRequest.  # noqa: E501


        :return: The vif_instance_id of this EnableRouteAggregationRequest.  # noqa: E501
        :rtype: str
        """
        return self._vif_instance_id

    @vif_instance_id.setter
    def vif_instance_id(self, vif_instance_id):
        """Sets the vif_instance_id of this EnableRouteAggregationRequest.


        :param vif_instance_id: The vif_instance_id of this EnableRouteAggregationRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and vif_instance_id is None:
            raise ValueError("Invalid value for `vif_instance_id`, must not be `None`")  # noqa: E501

        self._vif_instance_id = vif_instance_id

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
        if issubclass(EnableRouteAggregationRequest, dict):
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
        if not isinstance(other, EnableRouteAggregationRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EnableRouteAggregationRequest):
            return True

        return self.to_dict() != other.to_dict()
