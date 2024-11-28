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


class LensNnsr2PicCommonRequest(object):
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
        'image_urls': 'list[str]',
        'jpg_quality': 'int',
        'logo_info': 'LogoInfoForLensNnsr2PicCommonInput',
        'model_quality': 'str',
        'req_key': 'str',
        'result_format': 'int',
        'return_url': 'bool'
    }

    attribute_map = {
        'binary_data_base64': 'binary_data_base64',
        'image_urls': 'image_urls',
        'jpg_quality': 'jpg_quality',
        'logo_info': 'logo_info',
        'model_quality': 'model_quality',
        'req_key': 'req_key',
        'result_format': 'result_format',
        'return_url': 'return_url'
    }

    def __init__(self, binary_data_base64=None, image_urls=None, jpg_quality=None, logo_info=None, model_quality=None, req_key=None, result_format=None, return_url=None, _configuration=None):  # noqa: E501
        """LensNnsr2PicCommonRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._binary_data_base64 = None
        self._image_urls = None
        self._jpg_quality = None
        self._logo_info = None
        self._model_quality = None
        self._req_key = None
        self._result_format = None
        self._return_url = None
        self.discriminator = None

        if binary_data_base64 is not None:
            self.binary_data_base64 = binary_data_base64
        if image_urls is not None:
            self.image_urls = image_urls
        if jpg_quality is not None:
            self.jpg_quality = jpg_quality
        if logo_info is not None:
            self.logo_info = logo_info
        self.model_quality = model_quality
        self.req_key = req_key
        if result_format is not None:
            self.result_format = result_format
        if return_url is not None:
            self.return_url = return_url

    @property
    def binary_data_base64(self):
        """Gets the binary_data_base64 of this LensNnsr2PicCommonRequest.  # noqa: E501


        :return: The binary_data_base64 of this LensNnsr2PicCommonRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._binary_data_base64

    @binary_data_base64.setter
    def binary_data_base64(self, binary_data_base64):
        """Sets the binary_data_base64 of this LensNnsr2PicCommonRequest.


        :param binary_data_base64: The binary_data_base64 of this LensNnsr2PicCommonRequest.  # noqa: E501
        :type: list[str]
        """

        self._binary_data_base64 = binary_data_base64

    @property
    def image_urls(self):
        """Gets the image_urls of this LensNnsr2PicCommonRequest.  # noqa: E501


        :return: The image_urls of this LensNnsr2PicCommonRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._image_urls

    @image_urls.setter
    def image_urls(self, image_urls):
        """Sets the image_urls of this LensNnsr2PicCommonRequest.


        :param image_urls: The image_urls of this LensNnsr2PicCommonRequest.  # noqa: E501
        :type: list[str]
        """

        self._image_urls = image_urls

    @property
    def jpg_quality(self):
        """Gets the jpg_quality of this LensNnsr2PicCommonRequest.  # noqa: E501


        :return: The jpg_quality of this LensNnsr2PicCommonRequest.  # noqa: E501
        :rtype: int
        """
        return self._jpg_quality

    @jpg_quality.setter
    def jpg_quality(self, jpg_quality):
        """Sets the jpg_quality of this LensNnsr2PicCommonRequest.


        :param jpg_quality: The jpg_quality of this LensNnsr2PicCommonRequest.  # noqa: E501
        :type: int
        """

        self._jpg_quality = jpg_quality

    @property
    def logo_info(self):
        """Gets the logo_info of this LensNnsr2PicCommonRequest.  # noqa: E501


        :return: The logo_info of this LensNnsr2PicCommonRequest.  # noqa: E501
        :rtype: LogoInfoForLensNnsr2PicCommonInput
        """
        return self._logo_info

    @logo_info.setter
    def logo_info(self, logo_info):
        """Sets the logo_info of this LensNnsr2PicCommonRequest.


        :param logo_info: The logo_info of this LensNnsr2PicCommonRequest.  # noqa: E501
        :type: LogoInfoForLensNnsr2PicCommonInput
        """

        self._logo_info = logo_info

    @property
    def model_quality(self):
        """Gets the model_quality of this LensNnsr2PicCommonRequest.  # noqa: E501


        :return: The model_quality of this LensNnsr2PicCommonRequest.  # noqa: E501
        :rtype: str
        """
        return self._model_quality

    @model_quality.setter
    def model_quality(self, model_quality):
        """Sets the model_quality of this LensNnsr2PicCommonRequest.


        :param model_quality: The model_quality of this LensNnsr2PicCommonRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and model_quality is None:
            raise ValueError("Invalid value for `model_quality`, must not be `None`")  # noqa: E501

        self._model_quality = model_quality

    @property
    def req_key(self):
        """Gets the req_key of this LensNnsr2PicCommonRequest.  # noqa: E501


        :return: The req_key of this LensNnsr2PicCommonRequest.  # noqa: E501
        :rtype: str
        """
        return self._req_key

    @req_key.setter
    def req_key(self, req_key):
        """Sets the req_key of this LensNnsr2PicCommonRequest.


        :param req_key: The req_key of this LensNnsr2PicCommonRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and req_key is None:
            raise ValueError("Invalid value for `req_key`, must not be `None`")  # noqa: E501

        self._req_key = req_key

    @property
    def result_format(self):
        """Gets the result_format of this LensNnsr2PicCommonRequest.  # noqa: E501


        :return: The result_format of this LensNnsr2PicCommonRequest.  # noqa: E501
        :rtype: int
        """
        return self._result_format

    @result_format.setter
    def result_format(self, result_format):
        """Sets the result_format of this LensNnsr2PicCommonRequest.


        :param result_format: The result_format of this LensNnsr2PicCommonRequest.  # noqa: E501
        :type: int
        """

        self._result_format = result_format

    @property
    def return_url(self):
        """Gets the return_url of this LensNnsr2PicCommonRequest.  # noqa: E501


        :return: The return_url of this LensNnsr2PicCommonRequest.  # noqa: E501
        :rtype: bool
        """
        return self._return_url

    @return_url.setter
    def return_url(self, return_url):
        """Sets the return_url of this LensNnsr2PicCommonRequest.


        :param return_url: The return_url of this LensNnsr2PicCommonRequest.  # noqa: E501
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
        if issubclass(LensNnsr2PicCommonRequest, dict):
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
        if not isinstance(other, LensNnsr2PicCommonRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LensNnsr2PicCommonRequest):
            return True

        return self.to_dict() != other.to_dict()
