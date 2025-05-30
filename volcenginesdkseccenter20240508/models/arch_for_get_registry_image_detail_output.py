# coding: utf-8

"""
    seccenter20240508

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ArchForGetRegistryImageDetailOutput(object):
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
        'arch': 'str',
        'digest': 'str',
        'os': 'str'
    }

    attribute_map = {
        'arch': 'Arch',
        'digest': 'Digest',
        'os': 'Os'
    }

    def __init__(self, arch=None, digest=None, os=None, _configuration=None):  # noqa: E501
        """ArchForGetRegistryImageDetailOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._arch = None
        self._digest = None
        self._os = None
        self.discriminator = None

        if arch is not None:
            self.arch = arch
        if digest is not None:
            self.digest = digest
        if os is not None:
            self.os = os

    @property
    def arch(self):
        """Gets the arch of this ArchForGetRegistryImageDetailOutput.  # noqa: E501


        :return: The arch of this ArchForGetRegistryImageDetailOutput.  # noqa: E501
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        """Sets the arch of this ArchForGetRegistryImageDetailOutput.


        :param arch: The arch of this ArchForGetRegistryImageDetailOutput.  # noqa: E501
        :type: str
        """

        self._arch = arch

    @property
    def digest(self):
        """Gets the digest of this ArchForGetRegistryImageDetailOutput.  # noqa: E501


        :return: The digest of this ArchForGetRegistryImageDetailOutput.  # noqa: E501
        :rtype: str
        """
        return self._digest

    @digest.setter
    def digest(self, digest):
        """Sets the digest of this ArchForGetRegistryImageDetailOutput.


        :param digest: The digest of this ArchForGetRegistryImageDetailOutput.  # noqa: E501
        :type: str
        """

        self._digest = digest

    @property
    def os(self):
        """Gets the os of this ArchForGetRegistryImageDetailOutput.  # noqa: E501


        :return: The os of this ArchForGetRegistryImageDetailOutput.  # noqa: E501
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this ArchForGetRegistryImageDetailOutput.


        :param os: The os of this ArchForGetRegistryImageDetailOutput.  # noqa: E501
        :type: str
        """

        self._os = os

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
        if issubclass(ArchForGetRegistryImageDetailOutput, dict):
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
        if not isinstance(other, ArchForGetRegistryImageDetailOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ArchForGetRegistryImageDetailOutput):
            return True

        return self.to_dict() != other.to_dict()
