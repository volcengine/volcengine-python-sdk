# coding: utf-8

"""
    waf

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ReasonForListProhibitionOutput(object):
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
        'black': 'int',
        'bot': 'int',
        'geo_black': 'int',
        'httpflood': 'int',
        'param_abnormal': 'int',
        'route_abnormal': 'int',
        'sensitive_info': 'int',
        'web_vulnerability': 'int'
    }

    attribute_map = {
        'black': 'black',
        'bot': 'bot',
        'geo_black': 'geo_black',
        'httpflood': 'httpflood',
        'param_abnormal': 'param_abnormal',
        'route_abnormal': 'route_abnormal',
        'sensitive_info': 'sensitive_info',
        'web_vulnerability': 'web_vulnerability'
    }

    def __init__(self, black=None, bot=None, geo_black=None, httpflood=None, param_abnormal=None, route_abnormal=None, sensitive_info=None, web_vulnerability=None, _configuration=None):  # noqa: E501
        """ReasonForListProhibitionOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._black = None
        self._bot = None
        self._geo_black = None
        self._httpflood = None
        self._param_abnormal = None
        self._route_abnormal = None
        self._sensitive_info = None
        self._web_vulnerability = None
        self.discriminator = None

        if black is not None:
            self.black = black
        if bot is not None:
            self.bot = bot
        if geo_black is not None:
            self.geo_black = geo_black
        if httpflood is not None:
            self.httpflood = httpflood
        if param_abnormal is not None:
            self.param_abnormal = param_abnormal
        if route_abnormal is not None:
            self.route_abnormal = route_abnormal
        if sensitive_info is not None:
            self.sensitive_info = sensitive_info
        if web_vulnerability is not None:
            self.web_vulnerability = web_vulnerability

    @property
    def black(self):
        """Gets the black of this ReasonForListProhibitionOutput.  # noqa: E501


        :return: The black of this ReasonForListProhibitionOutput.  # noqa: E501
        :rtype: int
        """
        return self._black

    @black.setter
    def black(self, black):
        """Sets the black of this ReasonForListProhibitionOutput.


        :param black: The black of this ReasonForListProhibitionOutput.  # noqa: E501
        :type: int
        """

        self._black = black

    @property
    def bot(self):
        """Gets the bot of this ReasonForListProhibitionOutput.  # noqa: E501


        :return: The bot of this ReasonForListProhibitionOutput.  # noqa: E501
        :rtype: int
        """
        return self._bot

    @bot.setter
    def bot(self, bot):
        """Sets the bot of this ReasonForListProhibitionOutput.


        :param bot: The bot of this ReasonForListProhibitionOutput.  # noqa: E501
        :type: int
        """

        self._bot = bot

    @property
    def geo_black(self):
        """Gets the geo_black of this ReasonForListProhibitionOutput.  # noqa: E501


        :return: The geo_black of this ReasonForListProhibitionOutput.  # noqa: E501
        :rtype: int
        """
        return self._geo_black

    @geo_black.setter
    def geo_black(self, geo_black):
        """Sets the geo_black of this ReasonForListProhibitionOutput.


        :param geo_black: The geo_black of this ReasonForListProhibitionOutput.  # noqa: E501
        :type: int
        """

        self._geo_black = geo_black

    @property
    def httpflood(self):
        """Gets the httpflood of this ReasonForListProhibitionOutput.  # noqa: E501


        :return: The httpflood of this ReasonForListProhibitionOutput.  # noqa: E501
        :rtype: int
        """
        return self._httpflood

    @httpflood.setter
    def httpflood(self, httpflood):
        """Sets the httpflood of this ReasonForListProhibitionOutput.


        :param httpflood: The httpflood of this ReasonForListProhibitionOutput.  # noqa: E501
        :type: int
        """

        self._httpflood = httpflood

    @property
    def param_abnormal(self):
        """Gets the param_abnormal of this ReasonForListProhibitionOutput.  # noqa: E501


        :return: The param_abnormal of this ReasonForListProhibitionOutput.  # noqa: E501
        :rtype: int
        """
        return self._param_abnormal

    @param_abnormal.setter
    def param_abnormal(self, param_abnormal):
        """Sets the param_abnormal of this ReasonForListProhibitionOutput.


        :param param_abnormal: The param_abnormal of this ReasonForListProhibitionOutput.  # noqa: E501
        :type: int
        """

        self._param_abnormal = param_abnormal

    @property
    def route_abnormal(self):
        """Gets the route_abnormal of this ReasonForListProhibitionOutput.  # noqa: E501


        :return: The route_abnormal of this ReasonForListProhibitionOutput.  # noqa: E501
        :rtype: int
        """
        return self._route_abnormal

    @route_abnormal.setter
    def route_abnormal(self, route_abnormal):
        """Sets the route_abnormal of this ReasonForListProhibitionOutput.


        :param route_abnormal: The route_abnormal of this ReasonForListProhibitionOutput.  # noqa: E501
        :type: int
        """

        self._route_abnormal = route_abnormal

    @property
    def sensitive_info(self):
        """Gets the sensitive_info of this ReasonForListProhibitionOutput.  # noqa: E501


        :return: The sensitive_info of this ReasonForListProhibitionOutput.  # noqa: E501
        :rtype: int
        """
        return self._sensitive_info

    @sensitive_info.setter
    def sensitive_info(self, sensitive_info):
        """Sets the sensitive_info of this ReasonForListProhibitionOutput.


        :param sensitive_info: The sensitive_info of this ReasonForListProhibitionOutput.  # noqa: E501
        :type: int
        """

        self._sensitive_info = sensitive_info

    @property
    def web_vulnerability(self):
        """Gets the web_vulnerability of this ReasonForListProhibitionOutput.  # noqa: E501


        :return: The web_vulnerability of this ReasonForListProhibitionOutput.  # noqa: E501
        :rtype: int
        """
        return self._web_vulnerability

    @web_vulnerability.setter
    def web_vulnerability(self, web_vulnerability):
        """Sets the web_vulnerability of this ReasonForListProhibitionOutput.


        :param web_vulnerability: The web_vulnerability of this ReasonForListProhibitionOutput.  # noqa: E501
        :type: int
        """

        self._web_vulnerability = web_vulnerability

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
        if issubclass(ReasonForListProhibitionOutput, dict):
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
        if not isinstance(other, ReasonForListProhibitionOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReasonForListProhibitionOutput):
            return True

        return self.to_dict() != other.to_dict()
