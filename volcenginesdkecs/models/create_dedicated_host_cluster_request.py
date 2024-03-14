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


class CreateDedicatedHostClusterRequest(object):
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
        'dedicated_host_cluster_name': 'str',
        'description': 'str',
        'zone_id': 'str'
    }

    attribute_map = {
        'client_token': 'ClientToken',
        'dedicated_host_cluster_name': 'DedicatedHostClusterName',
        'description': 'Description',
        'zone_id': 'ZoneId'
    }

    def __init__(self, client_token=None, dedicated_host_cluster_name=None, description=None, zone_id=None, _configuration=None):  # noqa: E501
        """CreateDedicatedHostClusterRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._client_token = None
        self._dedicated_host_cluster_name = None
        self._description = None
        self._zone_id = None
        self.discriminator = None

        if client_token is not None:
            self.client_token = client_token
        self.dedicated_host_cluster_name = dedicated_host_cluster_name
        if description is not None:
            self.description = description
        self.zone_id = zone_id

    @property
    def client_token(self):
        """Gets the client_token of this CreateDedicatedHostClusterRequest.  # noqa: E501


        :return: The client_token of this CreateDedicatedHostClusterRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_token

    @client_token.setter
    def client_token(self, client_token):
        """Sets the client_token of this CreateDedicatedHostClusterRequest.


        :param client_token: The client_token of this CreateDedicatedHostClusterRequest.  # noqa: E501
        :type: str
        """

        self._client_token = client_token

    @property
    def dedicated_host_cluster_name(self):
        """Gets the dedicated_host_cluster_name of this CreateDedicatedHostClusterRequest.  # noqa: E501


        :return: The dedicated_host_cluster_name of this CreateDedicatedHostClusterRequest.  # noqa: E501
        :rtype: str
        """
        return self._dedicated_host_cluster_name

    @dedicated_host_cluster_name.setter
    def dedicated_host_cluster_name(self, dedicated_host_cluster_name):
        """Sets the dedicated_host_cluster_name of this CreateDedicatedHostClusterRequest.


        :param dedicated_host_cluster_name: The dedicated_host_cluster_name of this CreateDedicatedHostClusterRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and dedicated_host_cluster_name is None:
            raise ValueError("Invalid value for `dedicated_host_cluster_name`, must not be `None`")  # noqa: E501

        self._dedicated_host_cluster_name = dedicated_host_cluster_name

    @property
    def description(self):
        """Gets the description of this CreateDedicatedHostClusterRequest.  # noqa: E501


        :return: The description of this CreateDedicatedHostClusterRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateDedicatedHostClusterRequest.


        :param description: The description of this CreateDedicatedHostClusterRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def zone_id(self):
        """Gets the zone_id of this CreateDedicatedHostClusterRequest.  # noqa: E501


        :return: The zone_id of this CreateDedicatedHostClusterRequest.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this CreateDedicatedHostClusterRequest.


        :param zone_id: The zone_id of this CreateDedicatedHostClusterRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and zone_id is None:
            raise ValueError("Invalid value for `zone_id`, must not be `None`")  # noqa: E501

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
        if issubclass(CreateDedicatedHostClusterRequest, dict):
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
        if not isinstance(other, CreateDedicatedHostClusterRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateDedicatedHostClusterRequest):
            return True

        return self.to_dict() != other.to_dict()
