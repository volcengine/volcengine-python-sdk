# coding: utf-8

"""
    privatelink

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class EnableVpcEndpointConnectionRequest(object):
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
        'endpoint_id': 'str',
        'resources_allocate': 'list[ResourcesAllocateForEnableVpcEndpointConnectionInput]',
        'service_id': 'str',
        'zone_id': 'str'
    }

    attribute_map = {
        'endpoint_id': 'EndpointId',
        'resources_allocate': 'ResourcesAllocate',
        'service_id': 'ServiceId',
        'zone_id': 'ZoneId'
    }

    def __init__(self, endpoint_id=None, resources_allocate=None, service_id=None, zone_id=None, _configuration=None):  # noqa: E501
        """EnableVpcEndpointConnectionRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._endpoint_id = None
        self._resources_allocate = None
        self._service_id = None
        self._zone_id = None
        self.discriminator = None

        self.endpoint_id = endpoint_id
        if resources_allocate is not None:
            self.resources_allocate = resources_allocate
        self.service_id = service_id
        if zone_id is not None:
            self.zone_id = zone_id

    @property
    def endpoint_id(self):
        """Gets the endpoint_id of this EnableVpcEndpointConnectionRequest.  # noqa: E501


        :return: The endpoint_id of this EnableVpcEndpointConnectionRequest.  # noqa: E501
        :rtype: str
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        """Sets the endpoint_id of this EnableVpcEndpointConnectionRequest.


        :param endpoint_id: The endpoint_id of this EnableVpcEndpointConnectionRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and endpoint_id is None:
            raise ValueError("Invalid value for `endpoint_id`, must not be `None`")  # noqa: E501

        self._endpoint_id = endpoint_id

    @property
    def resources_allocate(self):
        """Gets the resources_allocate of this EnableVpcEndpointConnectionRequest.  # noqa: E501


        :return: The resources_allocate of this EnableVpcEndpointConnectionRequest.  # noqa: E501
        :rtype: list[ResourcesAllocateForEnableVpcEndpointConnectionInput]
        """
        return self._resources_allocate

    @resources_allocate.setter
    def resources_allocate(self, resources_allocate):
        """Sets the resources_allocate of this EnableVpcEndpointConnectionRequest.


        :param resources_allocate: The resources_allocate of this EnableVpcEndpointConnectionRequest.  # noqa: E501
        :type: list[ResourcesAllocateForEnableVpcEndpointConnectionInput]
        """

        self._resources_allocate = resources_allocate

    @property
    def service_id(self):
        """Gets the service_id of this EnableVpcEndpointConnectionRequest.  # noqa: E501


        :return: The service_id of this EnableVpcEndpointConnectionRequest.  # noqa: E501
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this EnableVpcEndpointConnectionRequest.


        :param service_id: The service_id of this EnableVpcEndpointConnectionRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and service_id is None:
            raise ValueError("Invalid value for `service_id`, must not be `None`")  # noqa: E501

        self._service_id = service_id

    @property
    def zone_id(self):
        """Gets the zone_id of this EnableVpcEndpointConnectionRequest.  # noqa: E501


        :return: The zone_id of this EnableVpcEndpointConnectionRequest.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this EnableVpcEndpointConnectionRequest.


        :param zone_id: The zone_id of this EnableVpcEndpointConnectionRequest.  # noqa: E501
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
        if issubclass(EnableVpcEndpointConnectionRequest, dict):
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
        if not isinstance(other, EnableVpcEndpointConnectionRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EnableVpcEndpointConnectionRequest):
            return True

        return self.to_dict() != other.to_dict()
