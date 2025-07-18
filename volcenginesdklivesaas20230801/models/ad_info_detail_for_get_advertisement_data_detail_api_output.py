# coding: utf-8

"""
    livesaas20230801

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class AdInfoDetailForGetAdvertisementDataDetailAPIOutput(object):
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
        'click_time': 'int',
        'content': 'str',
        'external_user_id': 'str',
        'link': 'str',
        'nick_name': 'str',
        'page_advertise_type': 'int',
        'title': 'str',
        'user_id': 'int',
        'user_tel': 'str'
    }

    attribute_map = {
        'click_time': 'ClickTime',
        'content': 'Content',
        'external_user_id': 'ExternalUserId',
        'link': 'Link',
        'nick_name': 'NickName',
        'page_advertise_type': 'PageAdvertiseType',
        'title': 'Title',
        'user_id': 'UserId',
        'user_tel': 'UserTel'
    }

    def __init__(self, click_time=None, content=None, external_user_id=None, link=None, nick_name=None, page_advertise_type=None, title=None, user_id=None, user_tel=None, _configuration=None):  # noqa: E501
        """AdInfoDetailForGetAdvertisementDataDetailAPIOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._click_time = None
        self._content = None
        self._external_user_id = None
        self._link = None
        self._nick_name = None
        self._page_advertise_type = None
        self._title = None
        self._user_id = None
        self._user_tel = None
        self.discriminator = None

        if click_time is not None:
            self.click_time = click_time
        if content is not None:
            self.content = content
        if external_user_id is not None:
            self.external_user_id = external_user_id
        if link is not None:
            self.link = link
        if nick_name is not None:
            self.nick_name = nick_name
        if page_advertise_type is not None:
            self.page_advertise_type = page_advertise_type
        if title is not None:
            self.title = title
        if user_id is not None:
            self.user_id = user_id
        if user_tel is not None:
            self.user_tel = user_tel

    @property
    def click_time(self):
        """Gets the click_time of this AdInfoDetailForGetAdvertisementDataDetailAPIOutput.  # noqa: E501


        :return: The click_time of this AdInfoDetailForGetAdvertisementDataDetailAPIOutput.  # noqa: E501
        :rtype: int
        """
        return self._click_time

    @click_time.setter
    def click_time(self, click_time):
        """Sets the click_time of this AdInfoDetailForGetAdvertisementDataDetailAPIOutput.


        :param click_time: The click_time of this AdInfoDetailForGetAdvertisementDataDetailAPIOutput.  # noqa: E501
        :type: int
        """

        self._click_time = click_time

    @property
    def content(self):
        """Gets the content of this AdInfoDetailForGetAdvertisementDataDetailAPIOutput.  # noqa: E501


        :return: The content of this AdInfoDetailForGetAdvertisementDataDetailAPIOutput.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this AdInfoDetailForGetAdvertisementDataDetailAPIOutput.


        :param content: The content of this AdInfoDetailForGetAdvertisementDataDetailAPIOutput.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def external_user_id(self):
        """Gets the external_user_id of this AdInfoDetailForGetAdvertisementDataDetailAPIOutput.  # noqa: E501


        :return: The external_user_id of this AdInfoDetailForGetAdvertisementDataDetailAPIOutput.  # noqa: E501
        :rtype: str
        """
        return self._external_user_id

    @external_user_id.setter
    def external_user_id(self, external_user_id):
        """Sets the external_user_id of this AdInfoDetailForGetAdvertisementDataDetailAPIOutput.


        :param external_user_id: The external_user_id of this AdInfoDetailForGetAdvertisementDataDetailAPIOutput.  # noqa: E501
        :type: str
        """

        self._external_user_id = external_user_id

    @property
    def link(self):
        """Gets the link of this AdInfoDetailForGetAdvertisementDataDetailAPIOutput.  # noqa: E501


        :return: The link of this AdInfoDetailForGetAdvertisementDataDetailAPIOutput.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this AdInfoDetailForGetAdvertisementDataDetailAPIOutput.


        :param link: The link of this AdInfoDetailForGetAdvertisementDataDetailAPIOutput.  # noqa: E501
        :type: str
        """

        self._link = link

    @property
    def nick_name(self):
        """Gets the nick_name of this AdInfoDetailForGetAdvertisementDataDetailAPIOutput.  # noqa: E501


        :return: The nick_name of this AdInfoDetailForGetAdvertisementDataDetailAPIOutput.  # noqa: E501
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        """Sets the nick_name of this AdInfoDetailForGetAdvertisementDataDetailAPIOutput.


        :param nick_name: The nick_name of this AdInfoDetailForGetAdvertisementDataDetailAPIOutput.  # noqa: E501
        :type: str
        """

        self._nick_name = nick_name

    @property
    def page_advertise_type(self):
        """Gets the page_advertise_type of this AdInfoDetailForGetAdvertisementDataDetailAPIOutput.  # noqa: E501


        :return: The page_advertise_type of this AdInfoDetailForGetAdvertisementDataDetailAPIOutput.  # noqa: E501
        :rtype: int
        """
        return self._page_advertise_type

    @page_advertise_type.setter
    def page_advertise_type(self, page_advertise_type):
        """Sets the page_advertise_type of this AdInfoDetailForGetAdvertisementDataDetailAPIOutput.


        :param page_advertise_type: The page_advertise_type of this AdInfoDetailForGetAdvertisementDataDetailAPIOutput.  # noqa: E501
        :type: int
        """

        self._page_advertise_type = page_advertise_type

    @property
    def title(self):
        """Gets the title of this AdInfoDetailForGetAdvertisementDataDetailAPIOutput.  # noqa: E501


        :return: The title of this AdInfoDetailForGetAdvertisementDataDetailAPIOutput.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this AdInfoDetailForGetAdvertisementDataDetailAPIOutput.


        :param title: The title of this AdInfoDetailForGetAdvertisementDataDetailAPIOutput.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def user_id(self):
        """Gets the user_id of this AdInfoDetailForGetAdvertisementDataDetailAPIOutput.  # noqa: E501


        :return: The user_id of this AdInfoDetailForGetAdvertisementDataDetailAPIOutput.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this AdInfoDetailForGetAdvertisementDataDetailAPIOutput.


        :param user_id: The user_id of this AdInfoDetailForGetAdvertisementDataDetailAPIOutput.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def user_tel(self):
        """Gets the user_tel of this AdInfoDetailForGetAdvertisementDataDetailAPIOutput.  # noqa: E501


        :return: The user_tel of this AdInfoDetailForGetAdvertisementDataDetailAPIOutput.  # noqa: E501
        :rtype: str
        """
        return self._user_tel

    @user_tel.setter
    def user_tel(self, user_tel):
        """Sets the user_tel of this AdInfoDetailForGetAdvertisementDataDetailAPIOutput.


        :param user_tel: The user_tel of this AdInfoDetailForGetAdvertisementDataDetailAPIOutput.  # noqa: E501
        :type: str
        """

        self._user_tel = user_tel

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
        if issubclass(AdInfoDetailForGetAdvertisementDataDetailAPIOutput, dict):
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
        if not isinstance(other, AdInfoDetailForGetAdvertisementDataDetailAPIOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AdInfoDetailForGetAdvertisementDataDetailAPIOutput):
            return True

        return self.to_dict() != other.to_dict()
