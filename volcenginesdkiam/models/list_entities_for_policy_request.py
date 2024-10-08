# coding: utf-8

"""
    iam

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ListEntitiesForPolicyRequest(object):
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
        'entity_filter': 'str',
        'limit': 'int',
        'offset': 'int',
        'policy_name': 'str',
        'policy_type': 'str'
    }

    attribute_map = {
        'entity_filter': 'EntityFilter',
        'limit': 'Limit',
        'offset': 'Offset',
        'policy_name': 'PolicyName',
        'policy_type': 'PolicyType'
    }

    def __init__(self, entity_filter=None, limit=None, offset=None, policy_name=None, policy_type=None, _configuration=None):  # noqa: E501
        """ListEntitiesForPolicyRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._entity_filter = None
        self._limit = None
        self._offset = None
        self._policy_name = None
        self._policy_type = None
        self.discriminator = None

        if entity_filter is not None:
            self.entity_filter = entity_filter
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        self.policy_name = policy_name
        self.policy_type = policy_type

    @property
    def entity_filter(self):
        """Gets the entity_filter of this ListEntitiesForPolicyRequest.  # noqa: E501


        :return: The entity_filter of this ListEntitiesForPolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._entity_filter

    @entity_filter.setter
    def entity_filter(self, entity_filter):
        """Sets the entity_filter of this ListEntitiesForPolicyRequest.


        :param entity_filter: The entity_filter of this ListEntitiesForPolicyRequest.  # noqa: E501
        :type: str
        """

        self._entity_filter = entity_filter

    @property
    def limit(self):
        """Gets the limit of this ListEntitiesForPolicyRequest.  # noqa: E501


        :return: The limit of this ListEntitiesForPolicyRequest.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListEntitiesForPolicyRequest.


        :param limit: The limit of this ListEntitiesForPolicyRequest.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListEntitiesForPolicyRequest.  # noqa: E501


        :return: The offset of this ListEntitiesForPolicyRequest.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListEntitiesForPolicyRequest.


        :param offset: The offset of this ListEntitiesForPolicyRequest.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def policy_name(self):
        """Gets the policy_name of this ListEntitiesForPolicyRequest.  # noqa: E501


        :return: The policy_name of this ListEntitiesForPolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        """Sets the policy_name of this ListEntitiesForPolicyRequest.


        :param policy_name: The policy_name of this ListEntitiesForPolicyRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and policy_name is None:
            raise ValueError("Invalid value for `policy_name`, must not be `None`")  # noqa: E501

        self._policy_name = policy_name

    @property
    def policy_type(self):
        """Gets the policy_type of this ListEntitiesForPolicyRequest.  # noqa: E501


        :return: The policy_type of this ListEntitiesForPolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._policy_type

    @policy_type.setter
    def policy_type(self, policy_type):
        """Sets the policy_type of this ListEntitiesForPolicyRequest.


        :param policy_type: The policy_type of this ListEntitiesForPolicyRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and policy_type is None:
            raise ValueError("Invalid value for `policy_type`, must not be `None`")  # noqa: E501
        allowed_values = ["System", "Custom"]  # noqa: E501
        if (self._configuration.client_side_validation and
                policy_type not in allowed_values):
            raise ValueError(
                "Invalid value for `policy_type` ({0}), must be one of {1}"  # noqa: E501
                .format(policy_type, allowed_values)
            )

        self._policy_type = policy_type

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
        if issubclass(ListEntitiesForPolicyRequest, dict):
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
        if not isinstance(other, ListEntitiesForPolicyRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListEntitiesForPolicyRequest):
            return True

        return self.to_dict() != other.to_dict()
