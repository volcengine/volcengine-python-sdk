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


class HighAesGeneralV14Request(object):
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
        'ddim_steps': 'int',
        'height': 'int',
        'logo_info': 'LogoInfoForHighAesGeneralV14Input',
        'model_version': 'str',
        'prompt': 'str',
        'req_key': 'str',
        'return_url': 'bool',
        'scale': 'float',
        'seed': 'int',
        'use_predict_tags': 'bool',
        'use_rephraser': 'bool',
        'width': 'int'
    }

    attribute_map = {
        'ddim_steps': 'ddim_steps',
        'height': 'height',
        'logo_info': 'logo_info',
        'model_version': 'model_version',
        'prompt': 'prompt',
        'req_key': 'req_key',
        'return_url': 'return_url',
        'scale': 'scale',
        'seed': 'seed',
        'use_predict_tags': 'use_predict_tags',
        'use_rephraser': 'use_rephraser',
        'width': 'width'
    }

    def __init__(self, ddim_steps=None, height=None, logo_info=None, model_version=None, prompt=None, req_key=None, return_url=None, scale=None, seed=None, use_predict_tags=None, use_rephraser=None, width=None, _configuration=None):  # noqa: E501
        """HighAesGeneralV14Request - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._ddim_steps = None
        self._height = None
        self._logo_info = None
        self._model_version = None
        self._prompt = None
        self._req_key = None
        self._return_url = None
        self._scale = None
        self._seed = None
        self._use_predict_tags = None
        self._use_rephraser = None
        self._width = None
        self.discriminator = None

        if ddim_steps is not None:
            self.ddim_steps = ddim_steps
        if height is not None:
            self.height = height
        if logo_info is not None:
            self.logo_info = logo_info
        self.model_version = model_version
        self.prompt = prompt
        self.req_key = req_key
        if return_url is not None:
            self.return_url = return_url
        if scale is not None:
            self.scale = scale
        if seed is not None:
            self.seed = seed
        if use_predict_tags is not None:
            self.use_predict_tags = use_predict_tags
        if use_rephraser is not None:
            self.use_rephraser = use_rephraser
        if width is not None:
            self.width = width

    @property
    def ddim_steps(self):
        """Gets the ddim_steps of this HighAesGeneralV14Request.  # noqa: E501


        :return: The ddim_steps of this HighAesGeneralV14Request.  # noqa: E501
        :rtype: int
        """
        return self._ddim_steps

    @ddim_steps.setter
    def ddim_steps(self, ddim_steps):
        """Sets the ddim_steps of this HighAesGeneralV14Request.


        :param ddim_steps: The ddim_steps of this HighAesGeneralV14Request.  # noqa: E501
        :type: int
        """

        self._ddim_steps = ddim_steps

    @property
    def height(self):
        """Gets the height of this HighAesGeneralV14Request.  # noqa: E501


        :return: The height of this HighAesGeneralV14Request.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this HighAesGeneralV14Request.


        :param height: The height of this HighAesGeneralV14Request.  # noqa: E501
        :type: int
        """

        self._height = height

    @property
    def logo_info(self):
        """Gets the logo_info of this HighAesGeneralV14Request.  # noqa: E501


        :return: The logo_info of this HighAesGeneralV14Request.  # noqa: E501
        :rtype: LogoInfoForHighAesGeneralV14Input
        """
        return self._logo_info

    @logo_info.setter
    def logo_info(self, logo_info):
        """Sets the logo_info of this HighAesGeneralV14Request.


        :param logo_info: The logo_info of this HighAesGeneralV14Request.  # noqa: E501
        :type: LogoInfoForHighAesGeneralV14Input
        """

        self._logo_info = logo_info

    @property
    def model_version(self):
        """Gets the model_version of this HighAesGeneralV14Request.  # noqa: E501


        :return: The model_version of this HighAesGeneralV14Request.  # noqa: E501
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """Sets the model_version of this HighAesGeneralV14Request.


        :param model_version: The model_version of this HighAesGeneralV14Request.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and model_version is None:
            raise ValueError("Invalid value for `model_version`, must not be `None`")  # noqa: E501

        self._model_version = model_version

    @property
    def prompt(self):
        """Gets the prompt of this HighAesGeneralV14Request.  # noqa: E501


        :return: The prompt of this HighAesGeneralV14Request.  # noqa: E501
        :rtype: str
        """
        return self._prompt

    @prompt.setter
    def prompt(self, prompt):
        """Sets the prompt of this HighAesGeneralV14Request.


        :param prompt: The prompt of this HighAesGeneralV14Request.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and prompt is None:
            raise ValueError("Invalid value for `prompt`, must not be `None`")  # noqa: E501

        self._prompt = prompt

    @property
    def req_key(self):
        """Gets the req_key of this HighAesGeneralV14Request.  # noqa: E501


        :return: The req_key of this HighAesGeneralV14Request.  # noqa: E501
        :rtype: str
        """
        return self._req_key

    @req_key.setter
    def req_key(self, req_key):
        """Sets the req_key of this HighAesGeneralV14Request.


        :param req_key: The req_key of this HighAesGeneralV14Request.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and req_key is None:
            raise ValueError("Invalid value for `req_key`, must not be `None`")  # noqa: E501

        self._req_key = req_key

    @property
    def return_url(self):
        """Gets the return_url of this HighAesGeneralV14Request.  # noqa: E501


        :return: The return_url of this HighAesGeneralV14Request.  # noqa: E501
        :rtype: bool
        """
        return self._return_url

    @return_url.setter
    def return_url(self, return_url):
        """Sets the return_url of this HighAesGeneralV14Request.


        :param return_url: The return_url of this HighAesGeneralV14Request.  # noqa: E501
        :type: bool
        """

        self._return_url = return_url

    @property
    def scale(self):
        """Gets the scale of this HighAesGeneralV14Request.  # noqa: E501


        :return: The scale of this HighAesGeneralV14Request.  # noqa: E501
        :rtype: float
        """
        return self._scale

    @scale.setter
    def scale(self, scale):
        """Sets the scale of this HighAesGeneralV14Request.


        :param scale: The scale of this HighAesGeneralV14Request.  # noqa: E501
        :type: float
        """

        self._scale = scale

    @property
    def seed(self):
        """Gets the seed of this HighAesGeneralV14Request.  # noqa: E501


        :return: The seed of this HighAesGeneralV14Request.  # noqa: E501
        :rtype: int
        """
        return self._seed

    @seed.setter
    def seed(self, seed):
        """Sets the seed of this HighAesGeneralV14Request.


        :param seed: The seed of this HighAesGeneralV14Request.  # noqa: E501
        :type: int
        """

        self._seed = seed

    @property
    def use_predict_tags(self):
        """Gets the use_predict_tags of this HighAesGeneralV14Request.  # noqa: E501


        :return: The use_predict_tags of this HighAesGeneralV14Request.  # noqa: E501
        :rtype: bool
        """
        return self._use_predict_tags

    @use_predict_tags.setter
    def use_predict_tags(self, use_predict_tags):
        """Sets the use_predict_tags of this HighAesGeneralV14Request.


        :param use_predict_tags: The use_predict_tags of this HighAesGeneralV14Request.  # noqa: E501
        :type: bool
        """

        self._use_predict_tags = use_predict_tags

    @property
    def use_rephraser(self):
        """Gets the use_rephraser of this HighAesGeneralV14Request.  # noqa: E501


        :return: The use_rephraser of this HighAesGeneralV14Request.  # noqa: E501
        :rtype: bool
        """
        return self._use_rephraser

    @use_rephraser.setter
    def use_rephraser(self, use_rephraser):
        """Sets the use_rephraser of this HighAesGeneralV14Request.


        :param use_rephraser: The use_rephraser of this HighAesGeneralV14Request.  # noqa: E501
        :type: bool
        """

        self._use_rephraser = use_rephraser

    @property
    def width(self):
        """Gets the width of this HighAesGeneralV14Request.  # noqa: E501


        :return: The width of this HighAesGeneralV14Request.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this HighAesGeneralV14Request.


        :param width: The width of this HighAesGeneralV14Request.  # noqa: E501
        :type: int
        """

        self._width = width

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
        if issubclass(HighAesGeneralV14Request, dict):
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
        if not isinstance(other, HighAesGeneralV14Request):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HighAesGeneralV14Request):
            return True

        return self.to_dict() != other.to_dict()
