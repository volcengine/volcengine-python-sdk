# coding: utf-8

"""
    vke

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class StatusForListNodePoolsInput(object):
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
        'conditions_type': 'str',
        'phase': 'str'
    }

    attribute_map = {
        'conditions_type': 'Conditions.Type',
        'phase': 'Phase'
    }

    def __init__(self, conditions_type=None, phase=None, _configuration=None):  # noqa: E501
        """StatusForListNodePoolsInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._conditions_type = None
        self._phase = None
        self.discriminator = None

        if conditions_type is not None:
            self.conditions_type = conditions_type
        if phase is not None:
            self.phase = phase

    @property
    def conditions_type(self):
        """Gets the conditions_type of this StatusForListNodePoolsInput.  # noqa: E501


        :return: The conditions_type of this StatusForListNodePoolsInput.  # noqa: E501
        :rtype: str
        """
        return self._conditions_type

    @conditions_type.setter
    def conditions_type(self, conditions_type):
        """Sets the conditions_type of this StatusForListNodePoolsInput.


        :param conditions_type: The conditions_type of this StatusForListNodePoolsInput.  # noqa: E501
        :type: str
        """
        allowed_values = ["Ok", "StockOut", "LimitedByQuota", "Balance", "VersionPartlyUpgraded", "ResourceCleanupFailed", "ClusterNotRunning", "Unknown", "Progressing", "ClusterVersionUpgrading"]  # noqa: E501
        if (self._configuration.client_side_validation and
                conditions_type not in allowed_values):
            raise ValueError(
                "Invalid value for `conditions_type` ({0}), must be one of {1}"  # noqa: E501
                .format(conditions_type, allowed_values)
            )

        self._conditions_type = conditions_type

    @property
    def phase(self):
        """Gets the phase of this StatusForListNodePoolsInput.  # noqa: E501


        :return: The phase of this StatusForListNodePoolsInput.  # noqa: E501
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this StatusForListNodePoolsInput.


        :param phase: The phase of this StatusForListNodePoolsInput.  # noqa: E501
        :type: str
        """
        allowed_values = ["Creating", "Running", "Updating", "Scaling", "Deleting", "Failed"]  # noqa: E501
        if (self._configuration.client_side_validation and
                phase not in allowed_values):
            raise ValueError(
                "Invalid value for `phase` ({0}), must be one of {1}"  # noqa: E501
                .format(phase, allowed_values)
            )

        self._phase = phase

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
        if issubclass(StatusForListNodePoolsInput, dict):
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
        if not isinstance(other, StatusForListNodePoolsInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StatusForListNodePoolsInput):
            return True

        return self.to_dict() != other.to_dict()
