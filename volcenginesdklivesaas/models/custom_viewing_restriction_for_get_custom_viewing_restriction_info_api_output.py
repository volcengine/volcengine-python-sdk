# coding: utf-8

"""
    livesaas

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class CustomViewingRestrictionForGetCustomViewingRestrictionInfoAPIOutput(object):
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
        'custom_app': 'str',
        'custom_url': 'str',
        'error_redirect_url': 'str',
        'secret_key': 'str',
        'viewing_restriction_type': 'int'
    }

    attribute_map = {
        'custom_app': 'CustomApp',
        'custom_url': 'CustomUrl',
        'error_redirect_url': 'ErrorRedirectUrl',
        'secret_key': 'SecretKey',
        'viewing_restriction_type': 'ViewingRestrictionType'
    }

    def __init__(self, custom_app=None, custom_url=None, error_redirect_url=None, secret_key=None, viewing_restriction_type=None, _configuration=None):  # noqa: E501
        """CustomViewingRestrictionForGetCustomViewingRestrictionInfoAPIOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._custom_app = None
        self._custom_url = None
        self._error_redirect_url = None
        self._secret_key = None
        self._viewing_restriction_type = None
        self.discriminator = None

        if custom_app is not None:
            self.custom_app = custom_app
        if custom_url is not None:
            self.custom_url = custom_url
        if error_redirect_url is not None:
            self.error_redirect_url = error_redirect_url
        if secret_key is not None:
            self.secret_key = secret_key
        if viewing_restriction_type is not None:
            self.viewing_restriction_type = viewing_restriction_type

    @property
    def custom_app(self):
        """Gets the custom_app of this CustomViewingRestrictionForGetCustomViewingRestrictionInfoAPIOutput.  # noqa: E501


        :return: The custom_app of this CustomViewingRestrictionForGetCustomViewingRestrictionInfoAPIOutput.  # noqa: E501
        :rtype: str
        """
        return self._custom_app

    @custom_app.setter
    def custom_app(self, custom_app):
        """Sets the custom_app of this CustomViewingRestrictionForGetCustomViewingRestrictionInfoAPIOutput.


        :param custom_app: The custom_app of this CustomViewingRestrictionForGetCustomViewingRestrictionInfoAPIOutput.  # noqa: E501
        :type: str
        """

        self._custom_app = custom_app

    @property
    def custom_url(self):
        """Gets the custom_url of this CustomViewingRestrictionForGetCustomViewingRestrictionInfoAPIOutput.  # noqa: E501


        :return: The custom_url of this CustomViewingRestrictionForGetCustomViewingRestrictionInfoAPIOutput.  # noqa: E501
        :rtype: str
        """
        return self._custom_url

    @custom_url.setter
    def custom_url(self, custom_url):
        """Sets the custom_url of this CustomViewingRestrictionForGetCustomViewingRestrictionInfoAPIOutput.


        :param custom_url: The custom_url of this CustomViewingRestrictionForGetCustomViewingRestrictionInfoAPIOutput.  # noqa: E501
        :type: str
        """

        self._custom_url = custom_url

    @property
    def error_redirect_url(self):
        """Gets the error_redirect_url of this CustomViewingRestrictionForGetCustomViewingRestrictionInfoAPIOutput.  # noqa: E501


        :return: The error_redirect_url of this CustomViewingRestrictionForGetCustomViewingRestrictionInfoAPIOutput.  # noqa: E501
        :rtype: str
        """
        return self._error_redirect_url

    @error_redirect_url.setter
    def error_redirect_url(self, error_redirect_url):
        """Sets the error_redirect_url of this CustomViewingRestrictionForGetCustomViewingRestrictionInfoAPIOutput.


        :param error_redirect_url: The error_redirect_url of this CustomViewingRestrictionForGetCustomViewingRestrictionInfoAPIOutput.  # noqa: E501
        :type: str
        """

        self._error_redirect_url = error_redirect_url

    @property
    def secret_key(self):
        """Gets the secret_key of this CustomViewingRestrictionForGetCustomViewingRestrictionInfoAPIOutput.  # noqa: E501


        :return: The secret_key of this CustomViewingRestrictionForGetCustomViewingRestrictionInfoAPIOutput.  # noqa: E501
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """Sets the secret_key of this CustomViewingRestrictionForGetCustomViewingRestrictionInfoAPIOutput.


        :param secret_key: The secret_key of this CustomViewingRestrictionForGetCustomViewingRestrictionInfoAPIOutput.  # noqa: E501
        :type: str
        """

        self._secret_key = secret_key

    @property
    def viewing_restriction_type(self):
        """Gets the viewing_restriction_type of this CustomViewingRestrictionForGetCustomViewingRestrictionInfoAPIOutput.  # noqa: E501


        :return: The viewing_restriction_type of this CustomViewingRestrictionForGetCustomViewingRestrictionInfoAPIOutput.  # noqa: E501
        :rtype: int
        """
        return self._viewing_restriction_type

    @viewing_restriction_type.setter
    def viewing_restriction_type(self, viewing_restriction_type):
        """Sets the viewing_restriction_type of this CustomViewingRestrictionForGetCustomViewingRestrictionInfoAPIOutput.


        :param viewing_restriction_type: The viewing_restriction_type of this CustomViewingRestrictionForGetCustomViewingRestrictionInfoAPIOutput.  # noqa: E501
        :type: int
        """

        self._viewing_restriction_type = viewing_restriction_type

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
        if issubclass(CustomViewingRestrictionForGetCustomViewingRestrictionInfoAPIOutput, dict):
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
        if not isinstance(other, CustomViewingRestrictionForGetCustomViewingRestrictionInfoAPIOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CustomViewingRestrictionForGetCustomViewingRestrictionInfoAPIOutput):
            return True

        return self.to_dict() != other.to_dict()
