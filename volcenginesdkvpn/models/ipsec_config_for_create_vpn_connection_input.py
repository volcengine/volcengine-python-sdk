# coding: utf-8

"""
    vpn

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class IpsecConfigForCreateVpnConnectionInput(object):
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
        'auth_alg': 'str',
        'dh_group': 'str',
        'enc_alg': 'str',
        'lifetime': 'int'
    }

    attribute_map = {
        'auth_alg': 'AuthAlg',
        'dh_group': 'DhGroup',
        'enc_alg': 'EncAlg',
        'lifetime': 'Lifetime'
    }

    def __init__(self, auth_alg=None, dh_group=None, enc_alg=None, lifetime=None, _configuration=None):  # noqa: E501
        """IpsecConfigForCreateVpnConnectionInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._auth_alg = None
        self._dh_group = None
        self._enc_alg = None
        self._lifetime = None
        self.discriminator = None

        if auth_alg is not None:
            self.auth_alg = auth_alg
        if dh_group is not None:
            self.dh_group = dh_group
        if enc_alg is not None:
            self.enc_alg = enc_alg
        if lifetime is not None:
            self.lifetime = lifetime

    @property
    def auth_alg(self):
        """Gets the auth_alg of this IpsecConfigForCreateVpnConnectionInput.  # noqa: E501


        :return: The auth_alg of this IpsecConfigForCreateVpnConnectionInput.  # noqa: E501
        :rtype: str
        """
        return self._auth_alg

    @auth_alg.setter
    def auth_alg(self, auth_alg):
        """Sets the auth_alg of this IpsecConfigForCreateVpnConnectionInput.


        :param auth_alg: The auth_alg of this IpsecConfigForCreateVpnConnectionInput.  # noqa: E501
        :type: str
        """

        self._auth_alg = auth_alg

    @property
    def dh_group(self):
        """Gets the dh_group of this IpsecConfigForCreateVpnConnectionInput.  # noqa: E501


        :return: The dh_group of this IpsecConfigForCreateVpnConnectionInput.  # noqa: E501
        :rtype: str
        """
        return self._dh_group

    @dh_group.setter
    def dh_group(self, dh_group):
        """Sets the dh_group of this IpsecConfigForCreateVpnConnectionInput.


        :param dh_group: The dh_group of this IpsecConfigForCreateVpnConnectionInput.  # noqa: E501
        :type: str
        """

        self._dh_group = dh_group

    @property
    def enc_alg(self):
        """Gets the enc_alg of this IpsecConfigForCreateVpnConnectionInput.  # noqa: E501


        :return: The enc_alg of this IpsecConfigForCreateVpnConnectionInput.  # noqa: E501
        :rtype: str
        """
        return self._enc_alg

    @enc_alg.setter
    def enc_alg(self, enc_alg):
        """Sets the enc_alg of this IpsecConfigForCreateVpnConnectionInput.


        :param enc_alg: The enc_alg of this IpsecConfigForCreateVpnConnectionInput.  # noqa: E501
        :type: str
        """

        self._enc_alg = enc_alg

    @property
    def lifetime(self):
        """Gets the lifetime of this IpsecConfigForCreateVpnConnectionInput.  # noqa: E501


        :return: The lifetime of this IpsecConfigForCreateVpnConnectionInput.  # noqa: E501
        :rtype: int
        """
        return self._lifetime

    @lifetime.setter
    def lifetime(self, lifetime):
        """Sets the lifetime of this IpsecConfigForCreateVpnConnectionInput.


        :param lifetime: The lifetime of this IpsecConfigForCreateVpnConnectionInput.  # noqa: E501
        :type: int
        """

        self._lifetime = lifetime

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
        if issubclass(IpsecConfigForCreateVpnConnectionInput, dict):
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
        if not isinstance(other, IpsecConfigForCreateVpnConnectionInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IpsecConfigForCreateVpnConnectionInput):
            return True

        return self.to_dict() != other.to_dict()