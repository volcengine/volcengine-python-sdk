# coding: utf-8

"""
    vmp

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class GetContactResponse(object):
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
        'contact_group_ids': 'list[str]',
        'create_time': 'str',
        'ding_talk_bot_webhook': 'DingTalkBotWebhookForGetContactOutput',
        'email': 'str',
        'email_active': 'bool',
        'id': 'str',
        'lark_bot_webhook': 'LarkBotWebhookForGetContactOutput',
        'name': 'str',
        'we_com_bot_webhook': 'WeComBotWebhookForGetContactOutput',
        'webhook': 'WebhookForGetContactOutput'
    }

    attribute_map = {
        'contact_group_ids': 'ContactGroupIds',
        'create_time': 'CreateTime',
        'ding_talk_bot_webhook': 'DingTalkBotWebhook',
        'email': 'Email',
        'email_active': 'EmailActive',
        'id': 'Id',
        'lark_bot_webhook': 'LarkBotWebhook',
        'name': 'Name',
        'we_com_bot_webhook': 'WeComBotWebhook',
        'webhook': 'Webhook'
    }

    def __init__(self, contact_group_ids=None, create_time=None, ding_talk_bot_webhook=None, email=None, email_active=None, id=None, lark_bot_webhook=None, name=None, we_com_bot_webhook=None, webhook=None, _configuration=None):  # noqa: E501
        """GetContactResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._contact_group_ids = None
        self._create_time = None
        self._ding_talk_bot_webhook = None
        self._email = None
        self._email_active = None
        self._id = None
        self._lark_bot_webhook = None
        self._name = None
        self._we_com_bot_webhook = None
        self._webhook = None
        self.discriminator = None

        if contact_group_ids is not None:
            self.contact_group_ids = contact_group_ids
        if create_time is not None:
            self.create_time = create_time
        if ding_talk_bot_webhook is not None:
            self.ding_talk_bot_webhook = ding_talk_bot_webhook
        if email is not None:
            self.email = email
        if email_active is not None:
            self.email_active = email_active
        if id is not None:
            self.id = id
        if lark_bot_webhook is not None:
            self.lark_bot_webhook = lark_bot_webhook
        if name is not None:
            self.name = name
        if we_com_bot_webhook is not None:
            self.we_com_bot_webhook = we_com_bot_webhook
        if webhook is not None:
            self.webhook = webhook

    @property
    def contact_group_ids(self):
        """Gets the contact_group_ids of this GetContactResponse.  # noqa: E501


        :return: The contact_group_ids of this GetContactResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._contact_group_ids

    @contact_group_ids.setter
    def contact_group_ids(self, contact_group_ids):
        """Sets the contact_group_ids of this GetContactResponse.


        :param contact_group_ids: The contact_group_ids of this GetContactResponse.  # noqa: E501
        :type: list[str]
        """

        self._contact_group_ids = contact_group_ids

    @property
    def create_time(self):
        """Gets the create_time of this GetContactResponse.  # noqa: E501


        :return: The create_time of this GetContactResponse.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this GetContactResponse.


        :param create_time: The create_time of this GetContactResponse.  # noqa: E501
        :type: str
        """

        self._create_time = create_time

    @property
    def ding_talk_bot_webhook(self):
        """Gets the ding_talk_bot_webhook of this GetContactResponse.  # noqa: E501


        :return: The ding_talk_bot_webhook of this GetContactResponse.  # noqa: E501
        :rtype: DingTalkBotWebhookForGetContactOutput
        """
        return self._ding_talk_bot_webhook

    @ding_talk_bot_webhook.setter
    def ding_talk_bot_webhook(self, ding_talk_bot_webhook):
        """Sets the ding_talk_bot_webhook of this GetContactResponse.


        :param ding_talk_bot_webhook: The ding_talk_bot_webhook of this GetContactResponse.  # noqa: E501
        :type: DingTalkBotWebhookForGetContactOutput
        """

        self._ding_talk_bot_webhook = ding_talk_bot_webhook

    @property
    def email(self):
        """Gets the email of this GetContactResponse.  # noqa: E501


        :return: The email of this GetContactResponse.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this GetContactResponse.


        :param email: The email of this GetContactResponse.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def email_active(self):
        """Gets the email_active of this GetContactResponse.  # noqa: E501


        :return: The email_active of this GetContactResponse.  # noqa: E501
        :rtype: bool
        """
        return self._email_active

    @email_active.setter
    def email_active(self, email_active):
        """Sets the email_active of this GetContactResponse.


        :param email_active: The email_active of this GetContactResponse.  # noqa: E501
        :type: bool
        """

        self._email_active = email_active

    @property
    def id(self):
        """Gets the id of this GetContactResponse.  # noqa: E501


        :return: The id of this GetContactResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetContactResponse.


        :param id: The id of this GetContactResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def lark_bot_webhook(self):
        """Gets the lark_bot_webhook of this GetContactResponse.  # noqa: E501


        :return: The lark_bot_webhook of this GetContactResponse.  # noqa: E501
        :rtype: LarkBotWebhookForGetContactOutput
        """
        return self._lark_bot_webhook

    @lark_bot_webhook.setter
    def lark_bot_webhook(self, lark_bot_webhook):
        """Sets the lark_bot_webhook of this GetContactResponse.


        :param lark_bot_webhook: The lark_bot_webhook of this GetContactResponse.  # noqa: E501
        :type: LarkBotWebhookForGetContactOutput
        """

        self._lark_bot_webhook = lark_bot_webhook

    @property
    def name(self):
        """Gets the name of this GetContactResponse.  # noqa: E501


        :return: The name of this GetContactResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetContactResponse.


        :param name: The name of this GetContactResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def we_com_bot_webhook(self):
        """Gets the we_com_bot_webhook of this GetContactResponse.  # noqa: E501


        :return: The we_com_bot_webhook of this GetContactResponse.  # noqa: E501
        :rtype: WeComBotWebhookForGetContactOutput
        """
        return self._we_com_bot_webhook

    @we_com_bot_webhook.setter
    def we_com_bot_webhook(self, we_com_bot_webhook):
        """Sets the we_com_bot_webhook of this GetContactResponse.


        :param we_com_bot_webhook: The we_com_bot_webhook of this GetContactResponse.  # noqa: E501
        :type: WeComBotWebhookForGetContactOutput
        """

        self._we_com_bot_webhook = we_com_bot_webhook

    @property
    def webhook(self):
        """Gets the webhook of this GetContactResponse.  # noqa: E501


        :return: The webhook of this GetContactResponse.  # noqa: E501
        :rtype: WebhookForGetContactOutput
        """
        return self._webhook

    @webhook.setter
    def webhook(self, webhook):
        """Sets the webhook of this GetContactResponse.


        :param webhook: The webhook of this GetContactResponse.  # noqa: E501
        :type: WebhookForGetContactOutput
        """

        self._webhook = webhook

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
        if issubclass(GetContactResponse, dict):
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
        if not isinstance(other, GetContactResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetContactResponse):
            return True

        return self.to_dict() != other.to_dict()
