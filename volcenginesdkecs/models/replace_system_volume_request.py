# coding: utf-8

"""
    ecs

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ReplaceSystemVolumeRequest(object):
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
        'client_token': 'str',
        'image_id': 'str',
        'instance_id': 'str',
        'keep_image_credential': 'bool',
        'key_pair_name': 'str',
        'password': 'str',
        'size': 'str',
        'user_data': 'str'
    }

    attribute_map = {
        'client_token': 'ClientToken',
        'image_id': 'ImageId',
        'instance_id': 'InstanceId',
        'keep_image_credential': 'KeepImageCredential',
        'key_pair_name': 'KeyPairName',
        'password': 'Password',
        'size': 'Size',
        'user_data': 'UserData'
    }

    def __init__(self, client_token=None, image_id=None, instance_id=None, keep_image_credential=None, key_pair_name=None, password=None, size=None, user_data=None, _configuration=None):  # noqa: E501
        """ReplaceSystemVolumeRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._client_token = None
        self._image_id = None
        self._instance_id = None
        self._keep_image_credential = None
        self._key_pair_name = None
        self._password = None
        self._size = None
        self._user_data = None
        self.discriminator = None

        if client_token is not None:
            self.client_token = client_token
        if image_id is not None:
            self.image_id = image_id
        if instance_id is not None:
            self.instance_id = instance_id
        if keep_image_credential is not None:
            self.keep_image_credential = keep_image_credential
        if key_pair_name is not None:
            self.key_pair_name = key_pair_name
        if password is not None:
            self.password = password
        if size is not None:
            self.size = size
        if user_data is not None:
            self.user_data = user_data

    @property
    def client_token(self):
        """Gets the client_token of this ReplaceSystemVolumeRequest.  # noqa: E501


        :return: The client_token of this ReplaceSystemVolumeRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_token

    @client_token.setter
    def client_token(self, client_token):
        """Sets the client_token of this ReplaceSystemVolumeRequest.


        :param client_token: The client_token of this ReplaceSystemVolumeRequest.  # noqa: E501
        :type: str
        """

        self._client_token = client_token

    @property
    def image_id(self):
        """Gets the image_id of this ReplaceSystemVolumeRequest.  # noqa: E501


        :return: The image_id of this ReplaceSystemVolumeRequest.  # noqa: E501
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this ReplaceSystemVolumeRequest.


        :param image_id: The image_id of this ReplaceSystemVolumeRequest.  # noqa: E501
        :type: str
        """

        self._image_id = image_id

    @property
    def instance_id(self):
        """Gets the instance_id of this ReplaceSystemVolumeRequest.  # noqa: E501


        :return: The instance_id of this ReplaceSystemVolumeRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ReplaceSystemVolumeRequest.


        :param instance_id: The instance_id of this ReplaceSystemVolumeRequest.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def keep_image_credential(self):
        """Gets the keep_image_credential of this ReplaceSystemVolumeRequest.  # noqa: E501


        :return: The keep_image_credential of this ReplaceSystemVolumeRequest.  # noqa: E501
        :rtype: bool
        """
        return self._keep_image_credential

    @keep_image_credential.setter
    def keep_image_credential(self, keep_image_credential):
        """Sets the keep_image_credential of this ReplaceSystemVolumeRequest.


        :param keep_image_credential: The keep_image_credential of this ReplaceSystemVolumeRequest.  # noqa: E501
        :type: bool
        """

        self._keep_image_credential = keep_image_credential

    @property
    def key_pair_name(self):
        """Gets the key_pair_name of this ReplaceSystemVolumeRequest.  # noqa: E501


        :return: The key_pair_name of this ReplaceSystemVolumeRequest.  # noqa: E501
        :rtype: str
        """
        return self._key_pair_name

    @key_pair_name.setter
    def key_pair_name(self, key_pair_name):
        """Sets the key_pair_name of this ReplaceSystemVolumeRequest.


        :param key_pair_name: The key_pair_name of this ReplaceSystemVolumeRequest.  # noqa: E501
        :type: str
        """

        self._key_pair_name = key_pair_name

    @property
    def password(self):
        """Gets the password of this ReplaceSystemVolumeRequest.  # noqa: E501


        :return: The password of this ReplaceSystemVolumeRequest.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this ReplaceSystemVolumeRequest.


        :param password: The password of this ReplaceSystemVolumeRequest.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def size(self):
        """Gets the size of this ReplaceSystemVolumeRequest.  # noqa: E501


        :return: The size of this ReplaceSystemVolumeRequest.  # noqa: E501
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ReplaceSystemVolumeRequest.


        :param size: The size of this ReplaceSystemVolumeRequest.  # noqa: E501
        :type: str
        """

        self._size = size

    @property
    def user_data(self):
        """Gets the user_data of this ReplaceSystemVolumeRequest.  # noqa: E501


        :return: The user_data of this ReplaceSystemVolumeRequest.  # noqa: E501
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this ReplaceSystemVolumeRequest.


        :param user_data: The user_data of this ReplaceSystemVolumeRequest.  # noqa: E501
        :type: str
        """

        self._user_data = user_data

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
        if issubclass(ReplaceSystemVolumeRequest, dict):
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
        if not isinstance(other, ReplaceSystemVolumeRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReplaceSystemVolumeRequest):
            return True

        return self.to_dict() != other.to_dict()
