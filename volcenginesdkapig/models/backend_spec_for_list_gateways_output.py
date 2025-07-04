# coding: utf-8

"""
    apig

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class BackendSpecForListGatewaysOutput(object):
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
        'is_vke_with_flannel_cni_supported': 'bool',
        'vke_pod_cidr': 'str'
    }

    attribute_map = {
        'is_vke_with_flannel_cni_supported': 'IsVkeWithFlannelCNISupported',
        'vke_pod_cidr': 'VkePodCidr'
    }

    def __init__(self, is_vke_with_flannel_cni_supported=None, vke_pod_cidr=None, _configuration=None):  # noqa: E501
        """BackendSpecForListGatewaysOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._is_vke_with_flannel_cni_supported = None
        self._vke_pod_cidr = None
        self.discriminator = None

        if is_vke_with_flannel_cni_supported is not None:
            self.is_vke_with_flannel_cni_supported = is_vke_with_flannel_cni_supported
        if vke_pod_cidr is not None:
            self.vke_pod_cidr = vke_pod_cidr

    @property
    def is_vke_with_flannel_cni_supported(self):
        """Gets the is_vke_with_flannel_cni_supported of this BackendSpecForListGatewaysOutput.  # noqa: E501


        :return: The is_vke_with_flannel_cni_supported of this BackendSpecForListGatewaysOutput.  # noqa: E501
        :rtype: bool
        """
        return self._is_vke_with_flannel_cni_supported

    @is_vke_with_flannel_cni_supported.setter
    def is_vke_with_flannel_cni_supported(self, is_vke_with_flannel_cni_supported):
        """Sets the is_vke_with_flannel_cni_supported of this BackendSpecForListGatewaysOutput.


        :param is_vke_with_flannel_cni_supported: The is_vke_with_flannel_cni_supported of this BackendSpecForListGatewaysOutput.  # noqa: E501
        :type: bool
        """

        self._is_vke_with_flannel_cni_supported = is_vke_with_flannel_cni_supported

    @property
    def vke_pod_cidr(self):
        """Gets the vke_pod_cidr of this BackendSpecForListGatewaysOutput.  # noqa: E501


        :return: The vke_pod_cidr of this BackendSpecForListGatewaysOutput.  # noqa: E501
        :rtype: str
        """
        return self._vke_pod_cidr

    @vke_pod_cidr.setter
    def vke_pod_cidr(self, vke_pod_cidr):
        """Sets the vke_pod_cidr of this BackendSpecForListGatewaysOutput.


        :param vke_pod_cidr: The vke_pod_cidr of this BackendSpecForListGatewaysOutput.  # noqa: E501
        :type: str
        """

        self._vke_pod_cidr = vke_pod_cidr

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
        if issubclass(BackendSpecForListGatewaysOutput, dict):
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
        if not isinstance(other, BackendSpecForListGatewaysOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BackendSpecForListGatewaysOutput):
            return True

        return self.to_dict() != other.to_dict()
