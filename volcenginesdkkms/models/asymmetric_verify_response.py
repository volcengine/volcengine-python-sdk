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


class AsymmetricVerifyResponse(object):
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
        'key_id': 'str',
        'signature_valid': 'bool'
    }

    attribute_map = {
        'key_id': 'KeyID',
        'signature_valid': 'SignatureValid'
    }

    def __init__(self, key_id=None, signature_valid=None, _configuration=None):  # noqa: E501
        """AsymmetricVerifyResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._key_id = None
        self._signature_valid = None
        self.discriminator = None

        if key_id is not None:
            self.key_id = key_id
        if signature_valid is not None:
            self.signature_valid = signature_valid

    @property
    def key_id(self):
        """Gets the key_id of this AsymmetricVerifyResponse.  # noqa: E501


        :return: The key_id of this AsymmetricVerifyResponse.  # noqa: E501
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """Sets the key_id of this AsymmetricVerifyResponse.


        :param key_id: The key_id of this AsymmetricVerifyResponse.  # noqa: E501
        :type: str
        """

        self._key_id = key_id

    @property
    def signature_valid(self):
        """Gets the signature_valid of this AsymmetricVerifyResponse.  # noqa: E501


        :return: The signature_valid of this AsymmetricVerifyResponse.  # noqa: E501
        :rtype: bool
        """
        return self._signature_valid

    @signature_valid.setter
    def signature_valid(self, signature_valid):
        """Sets the signature_valid of this AsymmetricVerifyResponse.


        :param signature_valid: The signature_valid of this AsymmetricVerifyResponse.  # noqa: E501
        :type: bool
        """

        self._signature_valid = signature_valid

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
        if issubclass(AsymmetricVerifyResponse, dict):
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
        if not isinstance(other, AsymmetricVerifyResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AsymmetricVerifyResponse):
            return True

        return self.to_dict() != other.to_dict()
