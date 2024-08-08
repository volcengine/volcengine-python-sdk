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


class GenerateDataKeyRequest(object):
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
        'encryption_context': 'str',
        'key_id': 'str',
        'key_name': 'str',
        'keyring_name': 'str',
        'number_of_bytes': 'int'
    }

    attribute_map = {
        'encryption_context': 'EncryptionContext',
        'key_id': 'KeyID',
        'key_name': 'KeyName',
        'keyring_name': 'KeyringName',
        'number_of_bytes': 'NumberOfBytes'
    }

    def __init__(self, encryption_context=None, key_id=None, key_name=None, keyring_name=None, number_of_bytes=None, _configuration=None):  # noqa: E501
        """GenerateDataKeyRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._encryption_context = None
        self._key_id = None
        self._key_name = None
        self._keyring_name = None
        self._number_of_bytes = None
        self.discriminator = None

        if encryption_context is not None:
            self.encryption_context = encryption_context
        if key_id is not None:
            self.key_id = key_id
        if key_name is not None:
            self.key_name = key_name
        if keyring_name is not None:
            self.keyring_name = keyring_name
        if number_of_bytes is not None:
            self.number_of_bytes = number_of_bytes

    @property
    def encryption_context(self):
        """Gets the encryption_context of this GenerateDataKeyRequest.  # noqa: E501


        :return: The encryption_context of this GenerateDataKeyRequest.  # noqa: E501
        :rtype: str
        """
        return self._encryption_context

    @encryption_context.setter
    def encryption_context(self, encryption_context):
        """Sets the encryption_context of this GenerateDataKeyRequest.


        :param encryption_context: The encryption_context of this GenerateDataKeyRequest.  # noqa: E501
        :type: str
        """

        self._encryption_context = encryption_context

    @property
    def key_id(self):
        """Gets the key_id of this GenerateDataKeyRequest.  # noqa: E501


        :return: The key_id of this GenerateDataKeyRequest.  # noqa: E501
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """Sets the key_id of this GenerateDataKeyRequest.


        :param key_id: The key_id of this GenerateDataKeyRequest.  # noqa: E501
        :type: str
        """

        self._key_id = key_id

    @property
    def key_name(self):
        """Gets the key_name of this GenerateDataKeyRequest.  # noqa: E501


        :return: The key_name of this GenerateDataKeyRequest.  # noqa: E501
        :rtype: str
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name):
        """Sets the key_name of this GenerateDataKeyRequest.


        :param key_name: The key_name of this GenerateDataKeyRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                key_name is not None and len(key_name) > 31):
            raise ValueError("Invalid value for `key_name`, length must be less than or equal to `31`")  # noqa: E501
        if (self._configuration.client_side_validation and
                key_name is not None and len(key_name) < 2):
            raise ValueError("Invalid value for `key_name`, length must be greater than or equal to `2`")  # noqa: E501

        self._key_name = key_name

    @property
    def keyring_name(self):
        """Gets the keyring_name of this GenerateDataKeyRequest.  # noqa: E501


        :return: The keyring_name of this GenerateDataKeyRequest.  # noqa: E501
        :rtype: str
        """
        return self._keyring_name

    @keyring_name.setter
    def keyring_name(self, keyring_name):
        """Sets the keyring_name of this GenerateDataKeyRequest.


        :param keyring_name: The keyring_name of this GenerateDataKeyRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                keyring_name is not None and len(keyring_name) > 31):
            raise ValueError("Invalid value for `keyring_name`, length must be less than or equal to `31`")  # noqa: E501
        if (self._configuration.client_side_validation and
                keyring_name is not None and len(keyring_name) < 2):
            raise ValueError("Invalid value for `keyring_name`, length must be greater than or equal to `2`")  # noqa: E501

        self._keyring_name = keyring_name

    @property
    def number_of_bytes(self):
        """Gets the number_of_bytes of this GenerateDataKeyRequest.  # noqa: E501


        :return: The number_of_bytes of this GenerateDataKeyRequest.  # noqa: E501
        :rtype: int
        """
        return self._number_of_bytes

    @number_of_bytes.setter
    def number_of_bytes(self, number_of_bytes):
        """Sets the number_of_bytes of this GenerateDataKeyRequest.


        :param number_of_bytes: The number_of_bytes of this GenerateDataKeyRequest.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                number_of_bytes is not None and number_of_bytes > 1024):  # noqa: E501
            raise ValueError("Invalid value for `number_of_bytes`, must be a value less than or equal to `1024`")  # noqa: E501
        if (self._configuration.client_side_validation and
                number_of_bytes is not None and number_of_bytes < 1):  # noqa: E501
            raise ValueError("Invalid value for `number_of_bytes`, must be a value greater than or equal to `1`")  # noqa: E501

        self._number_of_bytes = number_of_bytes

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
        if issubclass(GenerateDataKeyRequest, dict):
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
        if not isinstance(other, GenerateDataKeyRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GenerateDataKeyRequest):
            return True

        return self.to_dict() != other.to_dict()
