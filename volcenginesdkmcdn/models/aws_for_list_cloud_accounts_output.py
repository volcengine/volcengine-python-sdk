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


class AwsForListCloudAccountsOutput(object):
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
        'preload': 'PreloadForListCloudAccountsOutput'
    }

    attribute_map = {
        'preload': 'Preload'
    }

    def __init__(self, preload=None, _configuration=None):  # noqa: E501
        """AwsForListCloudAccountsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._preload = None
        self.discriminator = None

        if preload is not None:
            self.preload = preload

    @property
    def preload(self):
        """Gets the preload of this AwsForListCloudAccountsOutput.  # noqa: E501


        :return: The preload of this AwsForListCloudAccountsOutput.  # noqa: E501
        :rtype: PreloadForListCloudAccountsOutput
        """
        return self._preload

    @preload.setter
    def preload(self, preload):
        """Sets the preload of this AwsForListCloudAccountsOutput.


        :param preload: The preload of this AwsForListCloudAccountsOutput.  # noqa: E501
        :type: PreloadForListCloudAccountsOutput
        """

        self._preload = preload

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
        if issubclass(AwsForListCloudAccountsOutput, dict):
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
        if not isinstance(other, AwsForListCloudAccountsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AwsForListCloudAccountsOutput):
            return True

        return self.to_dict() != other.to_dict()
