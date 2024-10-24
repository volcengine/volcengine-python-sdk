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


class RestoreSecretRequest(object):
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
        'backup_data': 'str',
        'secret_data_key': 'str',
        'signature': 'str'
    }

    attribute_map = {
        'backup_data': 'BackupData',
        'secret_data_key': 'SecretDataKey',
        'signature': 'Signature'
    }

    def __init__(self, backup_data=None, secret_data_key=None, signature=None, _configuration=None):  # noqa: E501
        """RestoreSecretRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._backup_data = None
        self._secret_data_key = None
        self._signature = None
        self.discriminator = None

        self.backup_data = backup_data
        self.secret_data_key = secret_data_key
        self.signature = signature

    @property
    def backup_data(self):
        """Gets the backup_data of this RestoreSecretRequest.  # noqa: E501


        :return: The backup_data of this RestoreSecretRequest.  # noqa: E501
        :rtype: str
        """
        return self._backup_data

    @backup_data.setter
    def backup_data(self, backup_data):
        """Sets the backup_data of this RestoreSecretRequest.


        :param backup_data: The backup_data of this RestoreSecretRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and backup_data is None:
            raise ValueError("Invalid value for `backup_data`, must not be `None`")  # noqa: E501

        self._backup_data = backup_data

    @property
    def secret_data_key(self):
        """Gets the secret_data_key of this RestoreSecretRequest.  # noqa: E501


        :return: The secret_data_key of this RestoreSecretRequest.  # noqa: E501
        :rtype: str
        """
        return self._secret_data_key

    @secret_data_key.setter
    def secret_data_key(self, secret_data_key):
        """Sets the secret_data_key of this RestoreSecretRequest.


        :param secret_data_key: The secret_data_key of this RestoreSecretRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and secret_data_key is None:
            raise ValueError("Invalid value for `secret_data_key`, must not be `None`")  # noqa: E501

        self._secret_data_key = secret_data_key

    @property
    def signature(self):
        """Gets the signature of this RestoreSecretRequest.  # noqa: E501


        :return: The signature of this RestoreSecretRequest.  # noqa: E501
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this RestoreSecretRequest.


        :param signature: The signature of this RestoreSecretRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and signature is None:
            raise ValueError("Invalid value for `signature`, must not be `None`")  # noqa: E501

        self._signature = signature

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
        if issubclass(RestoreSecretRequest, dict):
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
        if not isinstance(other, RestoreSecretRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RestoreSecretRequest):
            return True

        return self.to_dict() != other.to_dict()
