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


class EncryptRequest(object):
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
        'plaintext': 'str'
    }

    attribute_map = {
        'encryption_context': 'EncryptionContext',
        'key_id': 'KeyID',
        'key_name': 'KeyName',
        'keyring_name': 'KeyringName',
        'plaintext': 'Plaintext'
    }

    def __init__(self, encryption_context=None, key_id=None, key_name=None, keyring_name=None, plaintext=None, _configuration=None):  # noqa: E501
        """EncryptRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._encryption_context = None
        self._key_id = None
        self._key_name = None
        self._keyring_name = None
        self._plaintext = None
        self.discriminator = None

        if encryption_context is not None:
            self.encryption_context = encryption_context
        if key_id is not None:
            self.key_id = key_id
        if key_name is not None:
            self.key_name = key_name
        if keyring_name is not None:
            self.keyring_name = keyring_name
        self.plaintext = plaintext

    @property
    def encryption_context(self):
        """Gets the encryption_context of this EncryptRequest.  # noqa: E501


        :return: The encryption_context of this EncryptRequest.  # noqa: E501
        :rtype: str
        """
        return self._encryption_context

    @encryption_context.setter
    def encryption_context(self, encryption_context):
        """Sets the encryption_context of this EncryptRequest.


        :param encryption_context: The encryption_context of this EncryptRequest.  # noqa: E501
        :type: str
        """

        self._encryption_context = encryption_context

    @property
    def key_id(self):
        """Gets the key_id of this EncryptRequest.  # noqa: E501


        :return: The key_id of this EncryptRequest.  # noqa: E501
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """Sets the key_id of this EncryptRequest.


        :param key_id: The key_id of this EncryptRequest.  # noqa: E501
        :type: str
        """

        self._key_id = key_id

    @property
    def key_name(self):
        """Gets the key_name of this EncryptRequest.  # noqa: E501


        :return: The key_name of this EncryptRequest.  # noqa: E501
        :rtype: str
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name):
        """Sets the key_name of this EncryptRequest.


        :param key_name: The key_name of this EncryptRequest.  # noqa: E501
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
        """Gets the keyring_name of this EncryptRequest.  # noqa: E501


        :return: The keyring_name of this EncryptRequest.  # noqa: E501
        :rtype: str
        """
        return self._keyring_name

    @keyring_name.setter
    def keyring_name(self, keyring_name):
        """Sets the keyring_name of this EncryptRequest.


        :param keyring_name: The keyring_name of this EncryptRequest.  # noqa: E501
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
    def plaintext(self):
        """Gets the plaintext of this EncryptRequest.  # noqa: E501


        :return: The plaintext of this EncryptRequest.  # noqa: E501
        :rtype: str
        """
        return self._plaintext

    @plaintext.setter
    def plaintext(self, plaintext):
        """Sets the plaintext of this EncryptRequest.


        :param plaintext: The plaintext of this EncryptRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and plaintext is None:
            raise ValueError("Invalid value for `plaintext`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                plaintext is not None and len(plaintext) > 4096):
            raise ValueError("Invalid value for `plaintext`, length must be less than or equal to `4096`")  # noqa: E501
        if (self._configuration.client_side_validation and
                plaintext is not None and len(plaintext) < 1):
            raise ValueError("Invalid value for `plaintext`, length must be greater than or equal to `1`")  # noqa: E501

        self._plaintext = plaintext

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
        if issubclass(EncryptRequest, dict):
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
        if not isinstance(other, EncryptRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EncryptRequest):
            return True

        return self.to_dict() != other.to_dict()