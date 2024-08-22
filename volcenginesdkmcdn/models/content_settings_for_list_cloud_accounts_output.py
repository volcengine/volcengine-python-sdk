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


class ContentSettingsForListCloudAccountsOutput(object):
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
        'aws': 'AwsForListCloudAccountsOutput'
    }

    attribute_map = {
        'aws': 'Aws'
    }

    def __init__(self, aws=None, _configuration=None):  # noqa: E501
        """ContentSettingsForListCloudAccountsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._aws = None
        self.discriminator = None

        if aws is not None:
            self.aws = aws

    @property
    def aws(self):
        """Gets the aws of this ContentSettingsForListCloudAccountsOutput.  # noqa: E501


        :return: The aws of this ContentSettingsForListCloudAccountsOutput.  # noqa: E501
        :rtype: AwsForListCloudAccountsOutput
        """
        return self._aws

    @aws.setter
    def aws(self, aws):
        """Sets the aws of this ContentSettingsForListCloudAccountsOutput.


        :param aws: The aws of this ContentSettingsForListCloudAccountsOutput.  # noqa: E501
        :type: AwsForListCloudAccountsOutput
        """

        self._aws = aws

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
        if issubclass(ContentSettingsForListCloudAccountsOutput, dict):
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
        if not isinstance(other, ContentSettingsForListCloudAccountsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ContentSettingsForListCloudAccountsOutput):
            return True

        return self.to_dict() != other.to_dict()
