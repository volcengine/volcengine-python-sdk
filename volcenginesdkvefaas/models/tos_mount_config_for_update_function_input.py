# coding: utf-8

"""
    vefaas

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class TosMountConfigForUpdateFunctionInput(object):
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
        'credentials': 'CredentialsForUpdateFunctionInput',
        'enable_tos': 'bool',
        'mount_points': 'list[MountPointForUpdateFunctionInput]'
    }

    attribute_map = {
        'credentials': 'Credentials',
        'enable_tos': 'EnableTos',
        'mount_points': 'MountPoints'
    }

    def __init__(self, credentials=None, enable_tos=None, mount_points=None, _configuration=None):  # noqa: E501
        """TosMountConfigForUpdateFunctionInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._credentials = None
        self._enable_tos = None
        self._mount_points = None
        self.discriminator = None

        if credentials is not None:
            self.credentials = credentials
        if enable_tos is not None:
            self.enable_tos = enable_tos
        if mount_points is not None:
            self.mount_points = mount_points

    @property
    def credentials(self):
        """Gets the credentials of this TosMountConfigForUpdateFunctionInput.  # noqa: E501


        :return: The credentials of this TosMountConfigForUpdateFunctionInput.  # noqa: E501
        :rtype: CredentialsForUpdateFunctionInput
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this TosMountConfigForUpdateFunctionInput.


        :param credentials: The credentials of this TosMountConfigForUpdateFunctionInput.  # noqa: E501
        :type: CredentialsForUpdateFunctionInput
        """

        self._credentials = credentials

    @property
    def enable_tos(self):
        """Gets the enable_tos of this TosMountConfigForUpdateFunctionInput.  # noqa: E501


        :return: The enable_tos of this TosMountConfigForUpdateFunctionInput.  # noqa: E501
        :rtype: bool
        """
        return self._enable_tos

    @enable_tos.setter
    def enable_tos(self, enable_tos):
        """Sets the enable_tos of this TosMountConfigForUpdateFunctionInput.


        :param enable_tos: The enable_tos of this TosMountConfigForUpdateFunctionInput.  # noqa: E501
        :type: bool
        """

        self._enable_tos = enable_tos

    @property
    def mount_points(self):
        """Gets the mount_points of this TosMountConfigForUpdateFunctionInput.  # noqa: E501


        :return: The mount_points of this TosMountConfigForUpdateFunctionInput.  # noqa: E501
        :rtype: list[MountPointForUpdateFunctionInput]
        """
        return self._mount_points

    @mount_points.setter
    def mount_points(self, mount_points):
        """Sets the mount_points of this TosMountConfigForUpdateFunctionInput.


        :param mount_points: The mount_points of this TosMountConfigForUpdateFunctionInput.  # noqa: E501
        :type: list[MountPointForUpdateFunctionInput]
        """

        self._mount_points = mount_points

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
        if issubclass(TosMountConfigForUpdateFunctionInput, dict):
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
        if not isinstance(other, TosMountConfigForUpdateFunctionInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TosMountConfigForUpdateFunctionInput):
            return True

        return self.to_dict() != other.to_dict()
