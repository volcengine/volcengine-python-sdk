# coding: utf-8

"""
    kms

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class GetSecretValueResponse(object):
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
        'creation_date': 'int',
        'secret_value': 'str',
        'version_id': 'str',
        'version_stage': 'str'
    }

    attribute_map = {
        'creation_date': 'CreationDate',
        'secret_value': 'SecretValue',
        'version_id': 'VersionID',
        'version_stage': 'VersionStage'
    }

    def __init__(self, creation_date=None, secret_value=None, version_id=None, version_stage=None, _configuration=None):  # noqa: E501
        """GetSecretValueResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._creation_date = None
        self._secret_value = None
        self._version_id = None
        self._version_stage = None
        self.discriminator = None

        if creation_date is not None:
            self.creation_date = creation_date
        if secret_value is not None:
            self.secret_value = secret_value
        if version_id is not None:
            self.version_id = version_id
        if version_stage is not None:
            self.version_stage = version_stage

    @property
    def creation_date(self):
        """Gets the creation_date of this GetSecretValueResponse.  # noqa: E501


        :return: The creation_date of this GetSecretValueResponse.  # noqa: E501
        :rtype: int
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this GetSecretValueResponse.


        :param creation_date: The creation_date of this GetSecretValueResponse.  # noqa: E501
        :type: int
        """

        self._creation_date = creation_date

    @property
    def secret_value(self):
        """Gets the secret_value of this GetSecretValueResponse.  # noqa: E501


        :return: The secret_value of this GetSecretValueResponse.  # noqa: E501
        :rtype: str
        """
        return self._secret_value

    @secret_value.setter
    def secret_value(self, secret_value):
        """Sets the secret_value of this GetSecretValueResponse.


        :param secret_value: The secret_value of this GetSecretValueResponse.  # noqa: E501
        :type: str
        """

        self._secret_value = secret_value

    @property
    def version_id(self):
        """Gets the version_id of this GetSecretValueResponse.  # noqa: E501


        :return: The version_id of this GetSecretValueResponse.  # noqa: E501
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this GetSecretValueResponse.


        :param version_id: The version_id of this GetSecretValueResponse.  # noqa: E501
        :type: str
        """

        self._version_id = version_id

    @property
    def version_stage(self):
        """Gets the version_stage of this GetSecretValueResponse.  # noqa: E501


        :return: The version_stage of this GetSecretValueResponse.  # noqa: E501
        :rtype: str
        """
        return self._version_stage

    @version_stage.setter
    def version_stage(self, version_stage):
        """Sets the version_stage of this GetSecretValueResponse.


        :param version_stage: The version_stage of this GetSecretValueResponse.  # noqa: E501
        :type: str
        """

        self._version_stage = version_stage

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
        if issubclass(GetSecretValueResponse, dict):
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
        if not isinstance(other, GetSecretValueResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetSecretValueResponse):
            return True

        return self.to_dict() != other.to_dict()