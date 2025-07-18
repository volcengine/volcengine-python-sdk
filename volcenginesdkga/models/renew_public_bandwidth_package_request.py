# coding: utf-8

"""
    ga

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class RenewPublicBandwidthPackageRequest(object):
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
        'bandwidth_package_id': 'str',
        'duration': 'int'
    }

    attribute_map = {
        'bandwidth_package_id': 'BandwidthPackageId',
        'duration': 'Duration'
    }

    def __init__(self, bandwidth_package_id=None, duration=None, _configuration=None):  # noqa: E501
        """RenewPublicBandwidthPackageRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bandwidth_package_id = None
        self._duration = None
        self.discriminator = None

        self.bandwidth_package_id = bandwidth_package_id
        self.duration = duration

    @property
    def bandwidth_package_id(self):
        """Gets the bandwidth_package_id of this RenewPublicBandwidthPackageRequest.  # noqa: E501


        :return: The bandwidth_package_id of this RenewPublicBandwidthPackageRequest.  # noqa: E501
        :rtype: str
        """
        return self._bandwidth_package_id

    @bandwidth_package_id.setter
    def bandwidth_package_id(self, bandwidth_package_id):
        """Sets the bandwidth_package_id of this RenewPublicBandwidthPackageRequest.


        :param bandwidth_package_id: The bandwidth_package_id of this RenewPublicBandwidthPackageRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and bandwidth_package_id is None:
            raise ValueError("Invalid value for `bandwidth_package_id`, must not be `None`")  # noqa: E501

        self._bandwidth_package_id = bandwidth_package_id

    @property
    def duration(self):
        """Gets the duration of this RenewPublicBandwidthPackageRequest.  # noqa: E501


        :return: The duration of this RenewPublicBandwidthPackageRequest.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this RenewPublicBandwidthPackageRequest.


        :param duration: The duration of this RenewPublicBandwidthPackageRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and duration is None:
            raise ValueError("Invalid value for `duration`, must not be `None`")  # noqa: E501

        self._duration = duration

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
        if issubclass(RenewPublicBandwidthPackageRequest, dict):
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
        if not isinstance(other, RenewPublicBandwidthPackageRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RenewPublicBandwidthPackageRequest):
            return True

        return self.to_dict() != other.to_dict()
