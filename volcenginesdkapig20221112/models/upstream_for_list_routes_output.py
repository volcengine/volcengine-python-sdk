# coding: utf-8

"""
    apig20221112

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class UpstreamForListRoutesOutput(object):
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
        'type': 'str',
        'upstream_id': 'str',
        'version': 'str'
    }

    attribute_map = {
        'type': 'Type',
        'upstream_id': 'UpstreamId',
        'version': 'Version'
    }

    def __init__(self, type=None, upstream_id=None, version=None, _configuration=None):  # noqa: E501
        """UpstreamForListRoutesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._type = None
        self._upstream_id = None
        self._version = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if upstream_id is not None:
            self.upstream_id = upstream_id
        if version is not None:
            self.version = version

    @property
    def type(self):
        """Gets the type of this UpstreamForListRoutesOutput.  # noqa: E501


        :return: The type of this UpstreamForListRoutesOutput.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UpstreamForListRoutesOutput.


        :param type: The type of this UpstreamForListRoutesOutput.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def upstream_id(self):
        """Gets the upstream_id of this UpstreamForListRoutesOutput.  # noqa: E501


        :return: The upstream_id of this UpstreamForListRoutesOutput.  # noqa: E501
        :rtype: str
        """
        return self._upstream_id

    @upstream_id.setter
    def upstream_id(self, upstream_id):
        """Sets the upstream_id of this UpstreamForListRoutesOutput.


        :param upstream_id: The upstream_id of this UpstreamForListRoutesOutput.  # noqa: E501
        :type: str
        """

        self._upstream_id = upstream_id

    @property
    def version(self):
        """Gets the version of this UpstreamForListRoutesOutput.  # noqa: E501


        :return: The version of this UpstreamForListRoutesOutput.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this UpstreamForListRoutesOutput.


        :param version: The version of this UpstreamForListRoutesOutput.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if issubclass(UpstreamForListRoutesOutput, dict):
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
        if not isinstance(other, UpstreamForListRoutesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpstreamForListRoutesOutput):
            return True

        return self.to_dict() != other.to_dict()
