# coding: utf-8

"""
    advdefence

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class SetDefSwitchRequest(object):
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
        'cc_enable': 'int',
        'host': 'str'
    }

    attribute_map = {
        'cc_enable': 'CcEnable',
        'host': 'Host'
    }

    def __init__(self, cc_enable=None, host=None, _configuration=None):  # noqa: E501
        """SetDefSwitchRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cc_enable = None
        self._host = None
        self.discriminator = None

        self.cc_enable = cc_enable
        self.host = host

    @property
    def cc_enable(self):
        """Gets the cc_enable of this SetDefSwitchRequest.  # noqa: E501


        :return: The cc_enable of this SetDefSwitchRequest.  # noqa: E501
        :rtype: int
        """
        return self._cc_enable

    @cc_enable.setter
    def cc_enable(self, cc_enable):
        """Sets the cc_enable of this SetDefSwitchRequest.


        :param cc_enable: The cc_enable of this SetDefSwitchRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and cc_enable is None:
            raise ValueError("Invalid value for `cc_enable`, must not be `None`")  # noqa: E501

        self._cc_enable = cc_enable

    @property
    def host(self):
        """Gets the host of this SetDefSwitchRequest.  # noqa: E501


        :return: The host of this SetDefSwitchRequest.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this SetDefSwitchRequest.


        :param host: The host of this SetDefSwitchRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and host is None:
            raise ValueError("Invalid value for `host`, must not be `None`")  # noqa: E501

        self._host = host

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
        if issubclass(SetDefSwitchRequest, dict):
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
        if not isinstance(other, SetDefSwitchRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SetDefSwitchRequest):
            return True

        return self.to_dict() != other.to_dict()
