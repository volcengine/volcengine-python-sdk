# coding: utf-8

"""
    filenas

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ImportPolicyForCreateDataFlowTaskInput(object):
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
        'filter_info': 'FilterInfoForCreateDataFlowTaskInput',
        'status': 'str',
        'type': 'str'
    }

    attribute_map = {
        'filter_info': 'FilterInfo',
        'status': 'Status',
        'type': 'Type'
    }

    def __init__(self, filter_info=None, status=None, type=None, _configuration=None):  # noqa: E501
        """ImportPolicyForCreateDataFlowTaskInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._filter_info = None
        self._status = None
        self._type = None
        self.discriminator = None

        if filter_info is not None:
            self.filter_info = filter_info
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type

    @property
    def filter_info(self):
        """Gets the filter_info of this ImportPolicyForCreateDataFlowTaskInput.  # noqa: E501


        :return: The filter_info of this ImportPolicyForCreateDataFlowTaskInput.  # noqa: E501
        :rtype: FilterInfoForCreateDataFlowTaskInput
        """
        return self._filter_info

    @filter_info.setter
    def filter_info(self, filter_info):
        """Sets the filter_info of this ImportPolicyForCreateDataFlowTaskInput.


        :param filter_info: The filter_info of this ImportPolicyForCreateDataFlowTaskInput.  # noqa: E501
        :type: FilterInfoForCreateDataFlowTaskInput
        """

        self._filter_info = filter_info

    @property
    def status(self):
        """Gets the status of this ImportPolicyForCreateDataFlowTaskInput.  # noqa: E501


        :return: The status of this ImportPolicyForCreateDataFlowTaskInput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ImportPolicyForCreateDataFlowTaskInput.


        :param status: The status of this ImportPolicyForCreateDataFlowTaskInput.  # noqa: E501
        :type: str
        """
        allowed_values = ["Starting", "Running", "Stopping", "Stopped", "Error"]  # noqa: E501
        if (self._configuration.client_side_validation and
                status not in allowed_values):
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def type(self):
        """Gets the type of this ImportPolicyForCreateDataFlowTaskInput.  # noqa: E501


        :return: The type of this ImportPolicyForCreateDataFlowTaskInput.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ImportPolicyForCreateDataFlowTaskInput.


        :param type: The type of this ImportPolicyForCreateDataFlowTaskInput.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "Metadata", "MetaAndData"]  # noqa: E501
        if (self._configuration.client_side_validation and
                type not in allowed_values):
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(ImportPolicyForCreateDataFlowTaskInput, dict):
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
        if not isinstance(other, ImportPolicyForCreateDataFlowTaskInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ImportPolicyForCreateDataFlowTaskInput):
            return True

        return self.to_dict() != other.to_dict()
