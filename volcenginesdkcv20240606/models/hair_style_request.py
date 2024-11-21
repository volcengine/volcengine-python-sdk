# coding: utf-8

"""
    cv20240606

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class HairStyleRequest(object):
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
        'binary_data_base64': 'list[str]',
        'hair_type': 'int',
        'image_urls': 'list[str]',
        'logo_info': 'LogoInfoForHairStyleInput',
        'req_key': 'str',
        'return_url': 'bool'
    }

    attribute_map = {
        'binary_data_base64': 'binary_data_base64',
        'hair_type': 'hair_type',
        'image_urls': 'image_urls',
        'logo_info': 'logo_info',
        'req_key': 'req_key',
        'return_url': 'return_url'
    }

    def __init__(self, binary_data_base64=None, hair_type=None, image_urls=None, logo_info=None, req_key=None, return_url=None, _configuration=None):  # noqa: E501
        """HairStyleRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._binary_data_base64 = None
        self._hair_type = None
        self._image_urls = None
        self._logo_info = None
        self._req_key = None
        self._return_url = None
        self.discriminator = None

        if binary_data_base64 is not None:
            self.binary_data_base64 = binary_data_base64
        if hair_type is not None:
            self.hair_type = hair_type
        if image_urls is not None:
            self.image_urls = image_urls
        if logo_info is not None:
            self.logo_info = logo_info
        self.req_key = req_key
        if return_url is not None:
            self.return_url = return_url

    @property
    def binary_data_base64(self):
        """Gets the binary_data_base64 of this HairStyleRequest.  # noqa: E501


        :return: The binary_data_base64 of this HairStyleRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._binary_data_base64

    @binary_data_base64.setter
    def binary_data_base64(self, binary_data_base64):
        """Sets the binary_data_base64 of this HairStyleRequest.


        :param binary_data_base64: The binary_data_base64 of this HairStyleRequest.  # noqa: E501
        :type: list[str]
        """

        self._binary_data_base64 = binary_data_base64

    @property
    def hair_type(self):
        """Gets the hair_type of this HairStyleRequest.  # noqa: E501


        :return: The hair_type of this HairStyleRequest.  # noqa: E501
        :rtype: int
        """
        return self._hair_type

    @hair_type.setter
    def hair_type(self, hair_type):
        """Sets the hair_type of this HairStyleRequest.


        :param hair_type: The hair_type of this HairStyleRequest.  # noqa: E501
        :type: int
        """

        self._hair_type = hair_type

    @property
    def image_urls(self):
        """Gets the image_urls of this HairStyleRequest.  # noqa: E501


        :return: The image_urls of this HairStyleRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._image_urls

    @image_urls.setter
    def image_urls(self, image_urls):
        """Sets the image_urls of this HairStyleRequest.


        :param image_urls: The image_urls of this HairStyleRequest.  # noqa: E501
        :type: list[str]
        """

        self._image_urls = image_urls

    @property
    def logo_info(self):
        """Gets the logo_info of this HairStyleRequest.  # noqa: E501


        :return: The logo_info of this HairStyleRequest.  # noqa: E501
        :rtype: LogoInfoForHairStyleInput
        """
        return self._logo_info

    @logo_info.setter
    def logo_info(self, logo_info):
        """Sets the logo_info of this HairStyleRequest.


        :param logo_info: The logo_info of this HairStyleRequest.  # noqa: E501
        :type: LogoInfoForHairStyleInput
        """

        self._logo_info = logo_info

    @property
    def req_key(self):
        """Gets the req_key of this HairStyleRequest.  # noqa: E501


        :return: The req_key of this HairStyleRequest.  # noqa: E501
        :rtype: str
        """
        return self._req_key

    @req_key.setter
    def req_key(self, req_key):
        """Sets the req_key of this HairStyleRequest.


        :param req_key: The req_key of this HairStyleRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and req_key is None:
            raise ValueError("Invalid value for `req_key`, must not be `None`")  # noqa: E501

        self._req_key = req_key

    @property
    def return_url(self):
        """Gets the return_url of this HairStyleRequest.  # noqa: E501


        :return: The return_url of this HairStyleRequest.  # noqa: E501
        :rtype: bool
        """
        return self._return_url

    @return_url.setter
    def return_url(self, return_url):
        """Sets the return_url of this HairStyleRequest.


        :param return_url: The return_url of this HairStyleRequest.  # noqa: E501
        :type: bool
        """

        self._return_url = return_url

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
        if issubclass(HairStyleRequest, dict):
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
        if not isinstance(other, HairStyleRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HairStyleRequest):
            return True

        return self.to_dict() != other.to_dict()
