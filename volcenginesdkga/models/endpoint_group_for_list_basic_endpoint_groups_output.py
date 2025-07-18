# coding: utf-8

"""
    ga

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class EndpointGroupForListBasicEndpointGroupsOutput(object):
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
        'accelerator_id': 'str',
        'endpoint_group_id': 'str',
        'endpoints': 'list[EndpointForListBasicEndpointGroupsOutput]',
        'exist_bound_endpoint': 'bool',
        'name': 'str',
        'region': 'str',
        'state': 'str'
    }

    attribute_map = {
        'accelerator_id': 'AcceleratorId',
        'endpoint_group_id': 'EndpointGroupId',
        'endpoints': 'Endpoints',
        'exist_bound_endpoint': 'ExistBoundEndpoint',
        'name': 'Name',
        'region': 'Region',
        'state': 'State'
    }

    def __init__(self, accelerator_id=None, endpoint_group_id=None, endpoints=None, exist_bound_endpoint=None, name=None, region=None, state=None, _configuration=None):  # noqa: E501
        """EndpointGroupForListBasicEndpointGroupsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._accelerator_id = None
        self._endpoint_group_id = None
        self._endpoints = None
        self._exist_bound_endpoint = None
        self._name = None
        self._region = None
        self._state = None
        self.discriminator = None

        if accelerator_id is not None:
            self.accelerator_id = accelerator_id
        if endpoint_group_id is not None:
            self.endpoint_group_id = endpoint_group_id
        if endpoints is not None:
            self.endpoints = endpoints
        if exist_bound_endpoint is not None:
            self.exist_bound_endpoint = exist_bound_endpoint
        if name is not None:
            self.name = name
        if region is not None:
            self.region = region
        if state is not None:
            self.state = state

    @property
    def accelerator_id(self):
        """Gets the accelerator_id of this EndpointGroupForListBasicEndpointGroupsOutput.  # noqa: E501


        :return: The accelerator_id of this EndpointGroupForListBasicEndpointGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._accelerator_id

    @accelerator_id.setter
    def accelerator_id(self, accelerator_id):
        """Sets the accelerator_id of this EndpointGroupForListBasicEndpointGroupsOutput.


        :param accelerator_id: The accelerator_id of this EndpointGroupForListBasicEndpointGroupsOutput.  # noqa: E501
        :type: str
        """

        self._accelerator_id = accelerator_id

    @property
    def endpoint_group_id(self):
        """Gets the endpoint_group_id of this EndpointGroupForListBasicEndpointGroupsOutput.  # noqa: E501


        :return: The endpoint_group_id of this EndpointGroupForListBasicEndpointGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._endpoint_group_id

    @endpoint_group_id.setter
    def endpoint_group_id(self, endpoint_group_id):
        """Sets the endpoint_group_id of this EndpointGroupForListBasicEndpointGroupsOutput.


        :param endpoint_group_id: The endpoint_group_id of this EndpointGroupForListBasicEndpointGroupsOutput.  # noqa: E501
        :type: str
        """

        self._endpoint_group_id = endpoint_group_id

    @property
    def endpoints(self):
        """Gets the endpoints of this EndpointGroupForListBasicEndpointGroupsOutput.  # noqa: E501


        :return: The endpoints of this EndpointGroupForListBasicEndpointGroupsOutput.  # noqa: E501
        :rtype: list[EndpointForListBasicEndpointGroupsOutput]
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        """Sets the endpoints of this EndpointGroupForListBasicEndpointGroupsOutput.


        :param endpoints: The endpoints of this EndpointGroupForListBasicEndpointGroupsOutput.  # noqa: E501
        :type: list[EndpointForListBasicEndpointGroupsOutput]
        """

        self._endpoints = endpoints

    @property
    def exist_bound_endpoint(self):
        """Gets the exist_bound_endpoint of this EndpointGroupForListBasicEndpointGroupsOutput.  # noqa: E501


        :return: The exist_bound_endpoint of this EndpointGroupForListBasicEndpointGroupsOutput.  # noqa: E501
        :rtype: bool
        """
        return self._exist_bound_endpoint

    @exist_bound_endpoint.setter
    def exist_bound_endpoint(self, exist_bound_endpoint):
        """Sets the exist_bound_endpoint of this EndpointGroupForListBasicEndpointGroupsOutput.


        :param exist_bound_endpoint: The exist_bound_endpoint of this EndpointGroupForListBasicEndpointGroupsOutput.  # noqa: E501
        :type: bool
        """

        self._exist_bound_endpoint = exist_bound_endpoint

    @property
    def name(self):
        """Gets the name of this EndpointGroupForListBasicEndpointGroupsOutput.  # noqa: E501


        :return: The name of this EndpointGroupForListBasicEndpointGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EndpointGroupForListBasicEndpointGroupsOutput.


        :param name: The name of this EndpointGroupForListBasicEndpointGroupsOutput.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def region(self):
        """Gets the region of this EndpointGroupForListBasicEndpointGroupsOutput.  # noqa: E501


        :return: The region of this EndpointGroupForListBasicEndpointGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this EndpointGroupForListBasicEndpointGroupsOutput.


        :param region: The region of this EndpointGroupForListBasicEndpointGroupsOutput.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def state(self):
        """Gets the state of this EndpointGroupForListBasicEndpointGroupsOutput.  # noqa: E501


        :return: The state of this EndpointGroupForListBasicEndpointGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this EndpointGroupForListBasicEndpointGroupsOutput.


        :param state: The state of this EndpointGroupForListBasicEndpointGroupsOutput.  # noqa: E501
        :type: str
        """

        self._state = state

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
        if issubclass(EndpointGroupForListBasicEndpointGroupsOutput, dict):
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
        if not isinstance(other, EndpointGroupForListBasicEndpointGroupsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EndpointGroupForListBasicEndpointGroupsOutput):
            return True

        return self.to_dict() != other.to_dict()
