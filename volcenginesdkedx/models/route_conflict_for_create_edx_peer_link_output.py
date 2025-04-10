# coding: utf-8

"""
    edx

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class RouteConflictForCreateEDXPeerLinkOutput(object):
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
        'conflict_instance_id': 'str',
        'conflict_instance_type': 'str',
        'destination_cidr': 'str'
    }

    attribute_map = {
        'conflict_instance_id': 'ConflictInstanceId',
        'conflict_instance_type': 'ConflictInstanceType',
        'destination_cidr': 'DestinationCidr'
    }

    def __init__(self, conflict_instance_id=None, conflict_instance_type=None, destination_cidr=None, _configuration=None):  # noqa: E501
        """RouteConflictForCreateEDXPeerLinkOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._conflict_instance_id = None
        self._conflict_instance_type = None
        self._destination_cidr = None
        self.discriminator = None

        if conflict_instance_id is not None:
            self.conflict_instance_id = conflict_instance_id
        if conflict_instance_type is not None:
            self.conflict_instance_type = conflict_instance_type
        if destination_cidr is not None:
            self.destination_cidr = destination_cidr

    @property
    def conflict_instance_id(self):
        """Gets the conflict_instance_id of this RouteConflictForCreateEDXPeerLinkOutput.  # noqa: E501


        :return: The conflict_instance_id of this RouteConflictForCreateEDXPeerLinkOutput.  # noqa: E501
        :rtype: str
        """
        return self._conflict_instance_id

    @conflict_instance_id.setter
    def conflict_instance_id(self, conflict_instance_id):
        """Sets the conflict_instance_id of this RouteConflictForCreateEDXPeerLinkOutput.


        :param conflict_instance_id: The conflict_instance_id of this RouteConflictForCreateEDXPeerLinkOutput.  # noqa: E501
        :type: str
        """

        self._conflict_instance_id = conflict_instance_id

    @property
    def conflict_instance_type(self):
        """Gets the conflict_instance_type of this RouteConflictForCreateEDXPeerLinkOutput.  # noqa: E501


        :return: The conflict_instance_type of this RouteConflictForCreateEDXPeerLinkOutput.  # noqa: E501
        :rtype: str
        """
        return self._conflict_instance_type

    @conflict_instance_type.setter
    def conflict_instance_type(self, conflict_instance_type):
        """Sets the conflict_instance_type of this RouteConflictForCreateEDXPeerLinkOutput.


        :param conflict_instance_type: The conflict_instance_type of this RouteConflictForCreateEDXPeerLinkOutput.  # noqa: E501
        :type: str
        """

        self._conflict_instance_type = conflict_instance_type

    @property
    def destination_cidr(self):
        """Gets the destination_cidr of this RouteConflictForCreateEDXPeerLinkOutput.  # noqa: E501


        :return: The destination_cidr of this RouteConflictForCreateEDXPeerLinkOutput.  # noqa: E501
        :rtype: str
        """
        return self._destination_cidr

    @destination_cidr.setter
    def destination_cidr(self, destination_cidr):
        """Sets the destination_cidr of this RouteConflictForCreateEDXPeerLinkOutput.


        :param destination_cidr: The destination_cidr of this RouteConflictForCreateEDXPeerLinkOutput.  # noqa: E501
        :type: str
        """

        self._destination_cidr = destination_cidr

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
        if issubclass(RouteConflictForCreateEDXPeerLinkOutput, dict):
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
        if not isinstance(other, RouteConflictForCreateEDXPeerLinkOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RouteConflictForCreateEDXPeerLinkOutput):
            return True

        return self.to_dict() != other.to_dict()
