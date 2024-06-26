# coding: utf-8

"""
    iam

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ChangeSecureContactInfoRequest(object):
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
        'code': 'str',
        'new_email': 'str',
        'new_mobile_phone': 'str'
    }

    attribute_map = {
        'code': 'Code',
        'new_email': 'NewEmail',
        'new_mobile_phone': 'NewMobilePhone'
    }

    def __init__(self, code=None, new_email=None, new_mobile_phone=None, _configuration=None):  # noqa: E501
        """ChangeSecureContactInfoRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._code = None
        self._new_email = None
        self._new_mobile_phone = None
        self.discriminator = None

        self.code = code
        if new_email is not None:
            self.new_email = new_email
        if new_mobile_phone is not None:
            self.new_mobile_phone = new_mobile_phone

    @property
    def code(self):
        """Gets the code of this ChangeSecureContactInfoRequest.  # noqa: E501


        :return: The code of this ChangeSecureContactInfoRequest.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ChangeSecureContactInfoRequest.


        :param code: The code of this ChangeSecureContactInfoRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def new_email(self):
        """Gets the new_email of this ChangeSecureContactInfoRequest.  # noqa: E501


        :return: The new_email of this ChangeSecureContactInfoRequest.  # noqa: E501
        :rtype: str
        """
        return self._new_email

    @new_email.setter
    def new_email(self, new_email):
        """Sets the new_email of this ChangeSecureContactInfoRequest.


        :param new_email: The new_email of this ChangeSecureContactInfoRequest.  # noqa: E501
        :type: str
        """

        self._new_email = new_email

    @property
    def new_mobile_phone(self):
        """Gets the new_mobile_phone of this ChangeSecureContactInfoRequest.  # noqa: E501


        :return: The new_mobile_phone of this ChangeSecureContactInfoRequest.  # noqa: E501
        :rtype: str
        """
        return self._new_mobile_phone

    @new_mobile_phone.setter
    def new_mobile_phone(self, new_mobile_phone):
        """Sets the new_mobile_phone of this ChangeSecureContactInfoRequest.


        :param new_mobile_phone: The new_mobile_phone of this ChangeSecureContactInfoRequest.  # noqa: E501
        :type: str
        """

        self._new_mobile_phone = new_mobile_phone

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
        if issubclass(ChangeSecureContactInfoRequest, dict):
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
        if not isinstance(other, ChangeSecureContactInfoRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ChangeSecureContactInfoRequest):
            return True

        return self.to_dict() != other.to_dict()
