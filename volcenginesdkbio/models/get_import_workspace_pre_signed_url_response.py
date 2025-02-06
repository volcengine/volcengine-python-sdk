# coding: utf-8

"""
    bio

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class GetImportWorkspacePreSignedURLResponse(object):
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
        'pre_signed_url': 'str',
        'schema_key': 'str'
    }

    attribute_map = {
        'pre_signed_url': 'PreSignedURL',
        'schema_key': 'SchemaKey'
    }

    def __init__(self, pre_signed_url=None, schema_key=None, _configuration=None):  # noqa: E501
        """GetImportWorkspacePreSignedURLResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._pre_signed_url = None
        self._schema_key = None
        self.discriminator = None

        if pre_signed_url is not None:
            self.pre_signed_url = pre_signed_url
        if schema_key is not None:
            self.schema_key = schema_key

    @property
    def pre_signed_url(self):
        """Gets the pre_signed_url of this GetImportWorkspacePreSignedURLResponse.  # noqa: E501


        :return: The pre_signed_url of this GetImportWorkspacePreSignedURLResponse.  # noqa: E501
        :rtype: str
        """
        return self._pre_signed_url

    @pre_signed_url.setter
    def pre_signed_url(self, pre_signed_url):
        """Sets the pre_signed_url of this GetImportWorkspacePreSignedURLResponse.


        :param pre_signed_url: The pre_signed_url of this GetImportWorkspacePreSignedURLResponse.  # noqa: E501
        :type: str
        """

        self._pre_signed_url = pre_signed_url

    @property
    def schema_key(self):
        """Gets the schema_key of this GetImportWorkspacePreSignedURLResponse.  # noqa: E501


        :return: The schema_key of this GetImportWorkspacePreSignedURLResponse.  # noqa: E501
        :rtype: str
        """
        return self._schema_key

    @schema_key.setter
    def schema_key(self, schema_key):
        """Sets the schema_key of this GetImportWorkspacePreSignedURLResponse.


        :param schema_key: The schema_key of this GetImportWorkspacePreSignedURLResponse.  # noqa: E501
        :type: str
        """

        self._schema_key = schema_key

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
        if issubclass(GetImportWorkspacePreSignedURLResponse, dict):
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
        if not isinstance(other, GetImportWorkspacePreSignedURLResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetImportWorkspacePreSignedURLResponse):
            return True

        return self.to_dict() != other.to_dict()
