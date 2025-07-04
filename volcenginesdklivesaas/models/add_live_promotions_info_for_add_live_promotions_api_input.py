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


class AddLivePromotionsInfoForAddLivePromotionsAPIInput(object):
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
        'name': 'str',
        'push_url': 'str'
    }

    attribute_map = {
        'name': 'Name',
        'push_url': 'PushUrl'
    }

    def __init__(self, name=None, push_url=None, _configuration=None):  # noqa: E501
        """AddLivePromotionsInfoForAddLivePromotionsAPIInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._push_url = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if push_url is not None:
            self.push_url = push_url

    @property
    def name(self):
        """Gets the name of this AddLivePromotionsInfoForAddLivePromotionsAPIInput.  # noqa: E501


        :return: The name of this AddLivePromotionsInfoForAddLivePromotionsAPIInput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AddLivePromotionsInfoForAddLivePromotionsAPIInput.


        :param name: The name of this AddLivePromotionsInfoForAddLivePromotionsAPIInput.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def push_url(self):
        """Gets the push_url of this AddLivePromotionsInfoForAddLivePromotionsAPIInput.  # noqa: E501


        :return: The push_url of this AddLivePromotionsInfoForAddLivePromotionsAPIInput.  # noqa: E501
        :rtype: str
        """
        return self._push_url

    @push_url.setter
    def push_url(self, push_url):
        """Sets the push_url of this AddLivePromotionsInfoForAddLivePromotionsAPIInput.


        :param push_url: The push_url of this AddLivePromotionsInfoForAddLivePromotionsAPIInput.  # noqa: E501
        :type: str
        """

        self._push_url = push_url

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
        if issubclass(AddLivePromotionsInfoForAddLivePromotionsAPIInput, dict):
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
        if not isinstance(other, AddLivePromotionsInfoForAddLivePromotionsAPIInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddLivePromotionsInfoForAddLivePromotionsAPIInput):
            return True

        return self.to_dict() != other.to_dict()
