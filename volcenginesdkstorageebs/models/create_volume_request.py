# coding: utf-8

"""
    storage_ebs

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class CreateVolumeRequest(object):
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
        'description': 'str',
        'kind': 'str',
        'size': 'str',
        'volume_charge_type': 'str',
        'volume_name': 'str',
        'volume_type': 'str',
        'zone_id': 'str'
    }

    attribute_map = {
        'client_token': 'ClientToken',
        'description': 'Description',
        'kind': 'Kind',
        'size': 'Size',
        'volume_charge_type': 'VolumeChargeType',
        'volume_name': 'VolumeName',
        'volume_type': 'VolumeType',
        'zone_id': 'ZoneId'
    }

    def __init__(self, client_token=None, description=None, kind=None, size=None, volume_charge_type=None, volume_name=None, volume_type=None, zone_id=None, _configuration=None):  # noqa: E501
        """CreateVolumeRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._client_token = None
        self._description = None
        self._kind = None
        self._size = None
        self._volume_charge_type = None
        self._volume_name = None
        self._volume_type = None
        self._zone_id = None
        self.discriminator = None

        if client_token is not None:
            self.client_token = client_token
        if description is not None:
            self.description = description
        if kind is not None:
            self.kind = kind
        if size is not None:
            self.size = size
        if volume_charge_type is not None:
            self.volume_charge_type = volume_charge_type
        if volume_name is not None:
            self.volume_name = volume_name
        if volume_type is not None:
            self.volume_type = volume_type
        if zone_id is not None:
            self.zone_id = zone_id

    @property
    def client_token(self):
        """Gets the client_token of this CreateVolumeRequest.  # noqa: E501


        :return: The client_token of this CreateVolumeRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_token

    @client_token.setter
    def client_token(self, client_token):
        """Sets the client_token of this CreateVolumeRequest.


        :param client_token: The client_token of this CreateVolumeRequest.  # noqa: E501
        :type: str
        """

        self._client_token = client_token

    @property
    def description(self):
        """Gets the description of this CreateVolumeRequest.  # noqa: E501


        :return: The description of this CreateVolumeRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateVolumeRequest.


        :param description: The description of this CreateVolumeRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def kind(self):
        """Gets the kind of this CreateVolumeRequest.  # noqa: E501


        :return: The kind of this CreateVolumeRequest.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this CreateVolumeRequest.


        :param kind: The kind of this CreateVolumeRequest.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def size(self):
        """Gets the size of this CreateVolumeRequest.  # noqa: E501


        :return: The size of this CreateVolumeRequest.  # noqa: E501
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this CreateVolumeRequest.


        :param size: The size of this CreateVolumeRequest.  # noqa: E501
        :type: str
        """

        self._size = size

    @property
    def volume_charge_type(self):
        """Gets the volume_charge_type of this CreateVolumeRequest.  # noqa: E501


        :return: The volume_charge_type of this CreateVolumeRequest.  # noqa: E501
        :rtype: str
        """
        return self._volume_charge_type

    @volume_charge_type.setter
    def volume_charge_type(self, volume_charge_type):
        """Sets the volume_charge_type of this CreateVolumeRequest.


        :param volume_charge_type: The volume_charge_type of this CreateVolumeRequest.  # noqa: E501
        :type: str
        """

        self._volume_charge_type = volume_charge_type

    @property
    def volume_name(self):
        """Gets the volume_name of this CreateVolumeRequest.  # noqa: E501


        :return: The volume_name of this CreateVolumeRequest.  # noqa: E501
        :rtype: str
        """
        return self._volume_name

    @volume_name.setter
    def volume_name(self, volume_name):
        """Sets the volume_name of this CreateVolumeRequest.


        :param volume_name: The volume_name of this CreateVolumeRequest.  # noqa: E501
        :type: str
        """

        self._volume_name = volume_name

    @property
    def volume_type(self):
        """Gets the volume_type of this CreateVolumeRequest.  # noqa: E501


        :return: The volume_type of this CreateVolumeRequest.  # noqa: E501
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        """Sets the volume_type of this CreateVolumeRequest.


        :param volume_type: The volume_type of this CreateVolumeRequest.  # noqa: E501
        :type: str
        """

        self._volume_type = volume_type

    @property
    def zone_id(self):
        """Gets the zone_id of this CreateVolumeRequest.  # noqa: E501


        :return: The zone_id of this CreateVolumeRequest.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this CreateVolumeRequest.


        :param zone_id: The zone_id of this CreateVolumeRequest.  # noqa: E501
        :type: str
        """

        self._zone_id = zone_id

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
        if issubclass(CreateVolumeRequest, dict):
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
        if not isinstance(other, CreateVolumeRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateVolumeRequest):
            return True

        return self.to_dict() != other.to_dict()
