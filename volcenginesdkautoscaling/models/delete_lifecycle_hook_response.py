# coding: utf-8

"""
    auto_scaling

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DeleteLifecycleHookResponse(object):
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
        'lifecycle_hook_id': 'str'
    }

    attribute_map = {
        'lifecycle_hook_id': 'LifecycleHookId'
    }

    def __init__(self, lifecycle_hook_id=None, _configuration=None):  # noqa: E501
        """DeleteLifecycleHookResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._lifecycle_hook_id = None
        self.discriminator = None

        if lifecycle_hook_id is not None:
            self.lifecycle_hook_id = lifecycle_hook_id

    @property
    def lifecycle_hook_id(self):
        """Gets the lifecycle_hook_id of this DeleteLifecycleHookResponse.  # noqa: E501


        :return: The lifecycle_hook_id of this DeleteLifecycleHookResponse.  # noqa: E501
        :rtype: str
        """
        return self._lifecycle_hook_id

    @lifecycle_hook_id.setter
    def lifecycle_hook_id(self, lifecycle_hook_id):
        """Sets the lifecycle_hook_id of this DeleteLifecycleHookResponse.


        :param lifecycle_hook_id: The lifecycle_hook_id of this DeleteLifecycleHookResponse.  # noqa: E501
        :type: str
        """

        self._lifecycle_hook_id = lifecycle_hook_id

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
        if issubclass(DeleteLifecycleHookResponse, dict):
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
        if not isinstance(other, DeleteLifecycleHookResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeleteLifecycleHookResponse):
            return True

        return self.to_dict() != other.to_dict()
