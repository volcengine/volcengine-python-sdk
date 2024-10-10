# coding: utf-8

"""
    vpc

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ModifyEipAddressAttributesRequest(object):
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
        'allocation_id': 'str',
        'bandwidth': 'int',
        'description': 'str',
        'name': 'str',
        'release_with_instance': 'bool'
    }

    attribute_map = {
        'allocation_id': 'AllocationId',
        'bandwidth': 'Bandwidth',
        'description': 'Description',
        'name': 'Name',
        'release_with_instance': 'ReleaseWithInstance'
    }

    def __init__(self, allocation_id=None, bandwidth=None, description=None, name=None, release_with_instance=None, _configuration=None):  # noqa: E501
        """ModifyEipAddressAttributesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._allocation_id = None
        self._bandwidth = None
        self._description = None
        self._name = None
        self._release_with_instance = None
        self.discriminator = None

        self.allocation_id = allocation_id
        if bandwidth is not None:
            self.bandwidth = bandwidth
        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if release_with_instance is not None:
            self.release_with_instance = release_with_instance

    @property
    def allocation_id(self):
        """Gets the allocation_id of this ModifyEipAddressAttributesRequest.  # noqa: E501


        :return: The allocation_id of this ModifyEipAddressAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._allocation_id

    @allocation_id.setter
    def allocation_id(self, allocation_id):
        """Sets the allocation_id of this ModifyEipAddressAttributesRequest.


        :param allocation_id: The allocation_id of this ModifyEipAddressAttributesRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and allocation_id is None:
            raise ValueError("Invalid value for `allocation_id`, must not be `None`")  # noqa: E501

        self._allocation_id = allocation_id

    @property
    def bandwidth(self):
        """Gets the bandwidth of this ModifyEipAddressAttributesRequest.  # noqa: E501


        :return: The bandwidth of this ModifyEipAddressAttributesRequest.  # noqa: E501
        :rtype: int
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this ModifyEipAddressAttributesRequest.


        :param bandwidth: The bandwidth of this ModifyEipAddressAttributesRequest.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                bandwidth is not None and bandwidth < 1):  # noqa: E501
            raise ValueError("Invalid value for `bandwidth`, must be a value greater than or equal to `1`")  # noqa: E501

        self._bandwidth = bandwidth

    @property
    def description(self):
        """Gets the description of this ModifyEipAddressAttributesRequest.  # noqa: E501


        :return: The description of this ModifyEipAddressAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ModifyEipAddressAttributesRequest.


        :param description: The description of this ModifyEipAddressAttributesRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                description is not None and len(description) > 255):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                description is not None and len(description) < 1):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `1`")  # noqa: E501

        self._description = description

    @property
    def name(self):
        """Gets the name of this ModifyEipAddressAttributesRequest.  # noqa: E501


        :return: The name of this ModifyEipAddressAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModifyEipAddressAttributesRequest.


        :param name: The name of this ModifyEipAddressAttributesRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                name is not None and len(name) > 128):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `128`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def release_with_instance(self):
        """Gets the release_with_instance of this ModifyEipAddressAttributesRequest.  # noqa: E501


        :return: The release_with_instance of this ModifyEipAddressAttributesRequest.  # noqa: E501
        :rtype: bool
        """
        return self._release_with_instance

    @release_with_instance.setter
    def release_with_instance(self, release_with_instance):
        """Sets the release_with_instance of this ModifyEipAddressAttributesRequest.


        :param release_with_instance: The release_with_instance of this ModifyEipAddressAttributesRequest.  # noqa: E501
        :type: bool
        """

        self._release_with_instance = release_with_instance

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
        if issubclass(ModifyEipAddressAttributesRequest, dict):
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
        if not isinstance(other, ModifyEipAddressAttributesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModifyEipAddressAttributesRequest):
            return True

        return self.to_dict() != other.to_dict()
