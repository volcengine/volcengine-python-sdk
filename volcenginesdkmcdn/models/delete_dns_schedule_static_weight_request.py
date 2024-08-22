# coding: utf-8

"""
    mcdn

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DeleteDnsScheduleStaticWeightRequest(object):
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
        'dns_schedule_id': 'str',
        'weight_id': 'str'
    }

    attribute_map = {
        'dns_schedule_id': 'DnsScheduleId',
        'weight_id': 'WeightId'
    }

    def __init__(self, dns_schedule_id=None, weight_id=None, _configuration=None):  # noqa: E501
        """DeleteDnsScheduleStaticWeightRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._dns_schedule_id = None
        self._weight_id = None
        self.discriminator = None

        self.dns_schedule_id = dns_schedule_id
        self.weight_id = weight_id

    @property
    def dns_schedule_id(self):
        """Gets the dns_schedule_id of this DeleteDnsScheduleStaticWeightRequest.  # noqa: E501


        :return: The dns_schedule_id of this DeleteDnsScheduleStaticWeightRequest.  # noqa: E501
        :rtype: str
        """
        return self._dns_schedule_id

    @dns_schedule_id.setter
    def dns_schedule_id(self, dns_schedule_id):
        """Sets the dns_schedule_id of this DeleteDnsScheduleStaticWeightRequest.


        :param dns_schedule_id: The dns_schedule_id of this DeleteDnsScheduleStaticWeightRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and dns_schedule_id is None:
            raise ValueError("Invalid value for `dns_schedule_id`, must not be `None`")  # noqa: E501

        self._dns_schedule_id = dns_schedule_id

    @property
    def weight_id(self):
        """Gets the weight_id of this DeleteDnsScheduleStaticWeightRequest.  # noqa: E501


        :return: The weight_id of this DeleteDnsScheduleStaticWeightRequest.  # noqa: E501
        :rtype: str
        """
        return self._weight_id

    @weight_id.setter
    def weight_id(self, weight_id):
        """Sets the weight_id of this DeleteDnsScheduleStaticWeightRequest.


        :param weight_id: The weight_id of this DeleteDnsScheduleStaticWeightRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and weight_id is None:
            raise ValueError("Invalid value for `weight_id`, must not be `None`")  # noqa: E501

        self._weight_id = weight_id

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
        if issubclass(DeleteDnsScheduleStaticWeightRequest, dict):
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
        if not isinstance(other, DeleteDnsScheduleStaticWeightRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeleteDnsScheduleStaticWeightRequest):
            return True

        return self.to_dict() != other.to_dict()