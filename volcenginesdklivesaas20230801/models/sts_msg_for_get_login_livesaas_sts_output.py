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


class StsMsgForGetLoginLivesaasStsOutput(object):
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
        'access_key_id': 'str',
        'expired_time': 'str',
        'secret_access_key': 'str',
        'session_token': 'str'
    }

    attribute_map = {
        'access_key_id': 'AccessKeyId',
        'expired_time': 'ExpiredTime',
        'secret_access_key': 'SecretAccessKey',
        'session_token': 'SessionToken'
    }

    def __init__(self, access_key_id=None, expired_time=None, secret_access_key=None, session_token=None, _configuration=None):  # noqa: E501
        """StsMsgForGetLoginLivesaasStsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._access_key_id = None
        self._expired_time = None
        self._secret_access_key = None
        self._session_token = None
        self.discriminator = None

        if access_key_id is not None:
            self.access_key_id = access_key_id
        if expired_time is not None:
            self.expired_time = expired_time
        if secret_access_key is not None:
            self.secret_access_key = secret_access_key
        if session_token is not None:
            self.session_token = session_token

    @property
    def access_key_id(self):
        """Gets the access_key_id of this StsMsgForGetLoginLivesaasStsOutput.  # noqa: E501


        :return: The access_key_id of this StsMsgForGetLoginLivesaasStsOutput.  # noqa: E501
        :rtype: str
        """
        return self._access_key_id

    @access_key_id.setter
    def access_key_id(self, access_key_id):
        """Sets the access_key_id of this StsMsgForGetLoginLivesaasStsOutput.


        :param access_key_id: The access_key_id of this StsMsgForGetLoginLivesaasStsOutput.  # noqa: E501
        :type: str
        """

        self._access_key_id = access_key_id

    @property
    def expired_time(self):
        """Gets the expired_time of this StsMsgForGetLoginLivesaasStsOutput.  # noqa: E501


        :return: The expired_time of this StsMsgForGetLoginLivesaasStsOutput.  # noqa: E501
        :rtype: str
        """
        return self._expired_time

    @expired_time.setter
    def expired_time(self, expired_time):
        """Sets the expired_time of this StsMsgForGetLoginLivesaasStsOutput.


        :param expired_time: The expired_time of this StsMsgForGetLoginLivesaasStsOutput.  # noqa: E501
        :type: str
        """

        self._expired_time = expired_time

    @property
    def secret_access_key(self):
        """Gets the secret_access_key of this StsMsgForGetLoginLivesaasStsOutput.  # noqa: E501


        :return: The secret_access_key of this StsMsgForGetLoginLivesaasStsOutput.  # noqa: E501
        :rtype: str
        """
        return self._secret_access_key

    @secret_access_key.setter
    def secret_access_key(self, secret_access_key):
        """Sets the secret_access_key of this StsMsgForGetLoginLivesaasStsOutput.


        :param secret_access_key: The secret_access_key of this StsMsgForGetLoginLivesaasStsOutput.  # noqa: E501
        :type: str
        """

        self._secret_access_key = secret_access_key

    @property
    def session_token(self):
        """Gets the session_token of this StsMsgForGetLoginLivesaasStsOutput.  # noqa: E501


        :return: The session_token of this StsMsgForGetLoginLivesaasStsOutput.  # noqa: E501
        :rtype: str
        """
        return self._session_token

    @session_token.setter
    def session_token(self, session_token):
        """Sets the session_token of this StsMsgForGetLoginLivesaasStsOutput.


        :param session_token: The session_token of this StsMsgForGetLoginLivesaasStsOutput.  # noqa: E501
        :type: str
        """

        self._session_token = session_token

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
        if issubclass(StsMsgForGetLoginLivesaasStsOutput, dict):
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
        if not isinstance(other, StsMsgForGetLoginLivesaasStsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StsMsgForGetLoginLivesaasStsOutput):
            return True

        return self.to_dict() != other.to_dict()
