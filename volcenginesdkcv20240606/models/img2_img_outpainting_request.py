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


class Img2ImgOutpaintingRequest(object):
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
        'bottom': 'float',
        'custom_prompt': 'str',
        'image_urls': 'list[str]',
        'left': 'float',
        'logo_info': 'LogoInfoForImg2ImgOutpaintingInput',
        'max_height': 'int',
        'max_width': 'int',
        'req_key': 'str',
        'return_url': 'bool',
        'right': 'float',
        'scale': 'float',
        'seed': 'int',
        'steps': 'int',
        'strength': 'float',
        'top': 'float'
    }

    attribute_map = {
        'binary_data_base64': 'binary_data_base64',
        'bottom': 'bottom',
        'custom_prompt': 'custom_prompt',
        'image_urls': 'image_urls',
        'left': 'left',
        'logo_info': 'logo_info',
        'max_height': 'max_height',
        'max_width': 'max_width',
        'req_key': 'req_key',
        'return_url': 'return_url',
        'right': 'right',
        'scale': 'scale',
        'seed': 'seed',
        'steps': 'steps',
        'strength': 'strength',
        'top': 'top'
    }

    def __init__(self, binary_data_base64=None, bottom=None, custom_prompt=None, image_urls=None, left=None, logo_info=None, max_height=None, max_width=None, req_key=None, return_url=None, right=None, scale=None, seed=None, steps=None, strength=None, top=None, _configuration=None):  # noqa: E501
        """Img2ImgOutpaintingRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._binary_data_base64 = None
        self._bottom = None
        self._custom_prompt = None
        self._image_urls = None
        self._left = None
        self._logo_info = None
        self._max_height = None
        self._max_width = None
        self._req_key = None
        self._return_url = None
        self._right = None
        self._scale = None
        self._seed = None
        self._steps = None
        self._strength = None
        self._top = None
        self.discriminator = None

        if binary_data_base64 is not None:
            self.binary_data_base64 = binary_data_base64
        if bottom is not None:
            self.bottom = bottom
        self.custom_prompt = custom_prompt
        if image_urls is not None:
            self.image_urls = image_urls
        if left is not None:
            self.left = left
        if logo_info is not None:
            self.logo_info = logo_info
        if max_height is not None:
            self.max_height = max_height
        if max_width is not None:
            self.max_width = max_width
        self.req_key = req_key
        if return_url is not None:
            self.return_url = return_url
        if right is not None:
            self.right = right
        if scale is not None:
            self.scale = scale
        if seed is not None:
            self.seed = seed
        if steps is not None:
            self.steps = steps
        if strength is not None:
            self.strength = strength
        if top is not None:
            self.top = top

    @property
    def binary_data_base64(self):
        """Gets the binary_data_base64 of this Img2ImgOutpaintingRequest.  # noqa: E501


        :return: The binary_data_base64 of this Img2ImgOutpaintingRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._binary_data_base64

    @binary_data_base64.setter
    def binary_data_base64(self, binary_data_base64):
        """Sets the binary_data_base64 of this Img2ImgOutpaintingRequest.


        :param binary_data_base64: The binary_data_base64 of this Img2ImgOutpaintingRequest.  # noqa: E501
        :type: list[str]
        """

        self._binary_data_base64 = binary_data_base64

    @property
    def bottom(self):
        """Gets the bottom of this Img2ImgOutpaintingRequest.  # noqa: E501


        :return: The bottom of this Img2ImgOutpaintingRequest.  # noqa: E501
        :rtype: float
        """
        return self._bottom

    @bottom.setter
    def bottom(self, bottom):
        """Sets the bottom of this Img2ImgOutpaintingRequest.


        :param bottom: The bottom of this Img2ImgOutpaintingRequest.  # noqa: E501
        :type: float
        """

        self._bottom = bottom

    @property
    def custom_prompt(self):
        """Gets the custom_prompt of this Img2ImgOutpaintingRequest.  # noqa: E501


        :return: The custom_prompt of this Img2ImgOutpaintingRequest.  # noqa: E501
        :rtype: str
        """
        return self._custom_prompt

    @custom_prompt.setter
    def custom_prompt(self, custom_prompt):
        """Sets the custom_prompt of this Img2ImgOutpaintingRequest.


        :param custom_prompt: The custom_prompt of this Img2ImgOutpaintingRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and custom_prompt is None:
            raise ValueError("Invalid value for `custom_prompt`, must not be `None`")  # noqa: E501

        self._custom_prompt = custom_prompt

    @property
    def image_urls(self):
        """Gets the image_urls of this Img2ImgOutpaintingRequest.  # noqa: E501


        :return: The image_urls of this Img2ImgOutpaintingRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._image_urls

    @image_urls.setter
    def image_urls(self, image_urls):
        """Sets the image_urls of this Img2ImgOutpaintingRequest.


        :param image_urls: The image_urls of this Img2ImgOutpaintingRequest.  # noqa: E501
        :type: list[str]
        """

        self._image_urls = image_urls

    @property
    def left(self):
        """Gets the left of this Img2ImgOutpaintingRequest.  # noqa: E501


        :return: The left of this Img2ImgOutpaintingRequest.  # noqa: E501
        :rtype: float
        """
        return self._left

    @left.setter
    def left(self, left):
        """Sets the left of this Img2ImgOutpaintingRequest.


        :param left: The left of this Img2ImgOutpaintingRequest.  # noqa: E501
        :type: float
        """

        self._left = left

    @property
    def logo_info(self):
        """Gets the logo_info of this Img2ImgOutpaintingRequest.  # noqa: E501


        :return: The logo_info of this Img2ImgOutpaintingRequest.  # noqa: E501
        :rtype: LogoInfoForImg2ImgOutpaintingInput
        """
        return self._logo_info

    @logo_info.setter
    def logo_info(self, logo_info):
        """Sets the logo_info of this Img2ImgOutpaintingRequest.


        :param logo_info: The logo_info of this Img2ImgOutpaintingRequest.  # noqa: E501
        :type: LogoInfoForImg2ImgOutpaintingInput
        """

        self._logo_info = logo_info

    @property
    def max_height(self):
        """Gets the max_height of this Img2ImgOutpaintingRequest.  # noqa: E501


        :return: The max_height of this Img2ImgOutpaintingRequest.  # noqa: E501
        :rtype: int
        """
        return self._max_height

    @max_height.setter
    def max_height(self, max_height):
        """Sets the max_height of this Img2ImgOutpaintingRequest.


        :param max_height: The max_height of this Img2ImgOutpaintingRequest.  # noqa: E501
        :type: int
        """

        self._max_height = max_height

    @property
    def max_width(self):
        """Gets the max_width of this Img2ImgOutpaintingRequest.  # noqa: E501


        :return: The max_width of this Img2ImgOutpaintingRequest.  # noqa: E501
        :rtype: int
        """
        return self._max_width

    @max_width.setter
    def max_width(self, max_width):
        """Sets the max_width of this Img2ImgOutpaintingRequest.


        :param max_width: The max_width of this Img2ImgOutpaintingRequest.  # noqa: E501
        :type: int
        """

        self._max_width = max_width

    @property
    def req_key(self):
        """Gets the req_key of this Img2ImgOutpaintingRequest.  # noqa: E501


        :return: The req_key of this Img2ImgOutpaintingRequest.  # noqa: E501
        :rtype: str
        """
        return self._req_key

    @req_key.setter
    def req_key(self, req_key):
        """Sets the req_key of this Img2ImgOutpaintingRequest.


        :param req_key: The req_key of this Img2ImgOutpaintingRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and req_key is None:
            raise ValueError("Invalid value for `req_key`, must not be `None`")  # noqa: E501

        self._req_key = req_key

    @property
    def return_url(self):
        """Gets the return_url of this Img2ImgOutpaintingRequest.  # noqa: E501


        :return: The return_url of this Img2ImgOutpaintingRequest.  # noqa: E501
        :rtype: bool
        """
        return self._return_url

    @return_url.setter
    def return_url(self, return_url):
        """Sets the return_url of this Img2ImgOutpaintingRequest.


        :param return_url: The return_url of this Img2ImgOutpaintingRequest.  # noqa: E501
        :type: bool
        """

        self._return_url = return_url

    @property
    def right(self):
        """Gets the right of this Img2ImgOutpaintingRequest.  # noqa: E501


        :return: The right of this Img2ImgOutpaintingRequest.  # noqa: E501
        :rtype: float
        """
        return self._right

    @right.setter
    def right(self, right):
        """Sets the right of this Img2ImgOutpaintingRequest.


        :param right: The right of this Img2ImgOutpaintingRequest.  # noqa: E501
        :type: float
        """

        self._right = right

    @property
    def scale(self):
        """Gets the scale of this Img2ImgOutpaintingRequest.  # noqa: E501


        :return: The scale of this Img2ImgOutpaintingRequest.  # noqa: E501
        :rtype: float
        """
        return self._scale

    @scale.setter
    def scale(self, scale):
        """Sets the scale of this Img2ImgOutpaintingRequest.


        :param scale: The scale of this Img2ImgOutpaintingRequest.  # noqa: E501
        :type: float
        """

        self._scale = scale

    @property
    def seed(self):
        """Gets the seed of this Img2ImgOutpaintingRequest.  # noqa: E501


        :return: The seed of this Img2ImgOutpaintingRequest.  # noqa: E501
        :rtype: int
        """
        return self._seed

    @seed.setter
    def seed(self, seed):
        """Sets the seed of this Img2ImgOutpaintingRequest.


        :param seed: The seed of this Img2ImgOutpaintingRequest.  # noqa: E501
        :type: int
        """

        self._seed = seed

    @property
    def steps(self):
        """Gets the steps of this Img2ImgOutpaintingRequest.  # noqa: E501


        :return: The steps of this Img2ImgOutpaintingRequest.  # noqa: E501
        :rtype: int
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """Sets the steps of this Img2ImgOutpaintingRequest.


        :param steps: The steps of this Img2ImgOutpaintingRequest.  # noqa: E501
        :type: int
        """

        self._steps = steps

    @property
    def strength(self):
        """Gets the strength of this Img2ImgOutpaintingRequest.  # noqa: E501


        :return: The strength of this Img2ImgOutpaintingRequest.  # noqa: E501
        :rtype: float
        """
        return self._strength

    @strength.setter
    def strength(self, strength):
        """Sets the strength of this Img2ImgOutpaintingRequest.


        :param strength: The strength of this Img2ImgOutpaintingRequest.  # noqa: E501
        :type: float
        """

        self._strength = strength

    @property
    def top(self):
        """Gets the top of this Img2ImgOutpaintingRequest.  # noqa: E501


        :return: The top of this Img2ImgOutpaintingRequest.  # noqa: E501
        :rtype: float
        """
        return self._top

    @top.setter
    def top(self, top):
        """Sets the top of this Img2ImgOutpaintingRequest.


        :param top: The top of this Img2ImgOutpaintingRequest.  # noqa: E501
        :type: float
        """

        self._top = top

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
        if issubclass(Img2ImgOutpaintingRequest, dict):
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
        if not isinstance(other, Img2ImgOutpaintingRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Img2ImgOutpaintingRequest):
            return True

        return self.to_dict() != other.to_dict()