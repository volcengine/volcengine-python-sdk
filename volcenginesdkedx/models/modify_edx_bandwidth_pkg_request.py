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


class ModifyEDXBandwidthPkgRequest(object):
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
        'bandwidth_pkg_id': 'str',
        'name': 'str',
        'total_bandwidth': 'int'
    }

    attribute_map = {
        'bandwidth_pkg_id': 'BandwidthPkgId',
        'name': 'Name',
        'total_bandwidth': 'TotalBandwidth'
    }

    def __init__(self, bandwidth_pkg_id=None, name=None, total_bandwidth=None, _configuration=None):  # noqa: E501
        """ModifyEDXBandwidthPkgRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bandwidth_pkg_id = None
        self._name = None
        self._total_bandwidth = None
        self.discriminator = None

        self.bandwidth_pkg_id = bandwidth_pkg_id
        if name is not None:
            self.name = name
        if total_bandwidth is not None:
            self.total_bandwidth = total_bandwidth

    @property
    def bandwidth_pkg_id(self):
        """Gets the bandwidth_pkg_id of this ModifyEDXBandwidthPkgRequest.  # noqa: E501


        :return: The bandwidth_pkg_id of this ModifyEDXBandwidthPkgRequest.  # noqa: E501
        :rtype: str
        """
        return self._bandwidth_pkg_id

    @bandwidth_pkg_id.setter
    def bandwidth_pkg_id(self, bandwidth_pkg_id):
        """Sets the bandwidth_pkg_id of this ModifyEDXBandwidthPkgRequest.


        :param bandwidth_pkg_id: The bandwidth_pkg_id of this ModifyEDXBandwidthPkgRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and bandwidth_pkg_id is None:
            raise ValueError("Invalid value for `bandwidth_pkg_id`, must not be `None`")  # noqa: E501

        self._bandwidth_pkg_id = bandwidth_pkg_id

    @property
    def name(self):
        """Gets the name of this ModifyEDXBandwidthPkgRequest.  # noqa: E501


        :return: The name of this ModifyEDXBandwidthPkgRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModifyEDXBandwidthPkgRequest.


        :param name: The name of this ModifyEDXBandwidthPkgRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def total_bandwidth(self):
        """Gets the total_bandwidth of this ModifyEDXBandwidthPkgRequest.  # noqa: E501


        :return: The total_bandwidth of this ModifyEDXBandwidthPkgRequest.  # noqa: E501
        :rtype: int
        """
        return self._total_bandwidth

    @total_bandwidth.setter
    def total_bandwidth(self, total_bandwidth):
        """Sets the total_bandwidth of this ModifyEDXBandwidthPkgRequest.


        :param total_bandwidth: The total_bandwidth of this ModifyEDXBandwidthPkgRequest.  # noqa: E501
        :type: int
        """

        self._total_bandwidth = total_bandwidth

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
        if issubclass(ModifyEDXBandwidthPkgRequest, dict):
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
        if not isinstance(other, ModifyEDXBandwidthPkgRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModifyEDXBandwidthPkgRequest):
            return True

        return self.to_dict() != other.to_dict()
