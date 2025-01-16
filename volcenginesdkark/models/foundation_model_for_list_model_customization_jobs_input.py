# coding: utf-8

"""
    ark

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class FoundationModelForListModelCustomizationJobsInput(object):
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
        'model_versions': 'list[str]',
        'name': 'str'
    }

    attribute_map = {
        'model_versions': 'ModelVersions',
        'name': 'Name'
    }

    def __init__(self, model_versions=None, name=None, _configuration=None):  # noqa: E501
        """FoundationModelForListModelCustomizationJobsInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._model_versions = None
        self._name = None
        self.discriminator = None

        if model_versions is not None:
            self.model_versions = model_versions
        if name is not None:
            self.name = name

    @property
    def model_versions(self):
        """Gets the model_versions of this FoundationModelForListModelCustomizationJobsInput.  # noqa: E501


        :return: The model_versions of this FoundationModelForListModelCustomizationJobsInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._model_versions

    @model_versions.setter
    def model_versions(self, model_versions):
        """Sets the model_versions of this FoundationModelForListModelCustomizationJobsInput.


        :param model_versions: The model_versions of this FoundationModelForListModelCustomizationJobsInput.  # noqa: E501
        :type: list[str]
        """

        self._model_versions = model_versions

    @property
    def name(self):
        """Gets the name of this FoundationModelForListModelCustomizationJobsInput.  # noqa: E501


        :return: The name of this FoundationModelForListModelCustomizationJobsInput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FoundationModelForListModelCustomizationJobsInput.


        :param name: The name of this FoundationModelForListModelCustomizationJobsInput.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(FoundationModelForListModelCustomizationJobsInput, dict):
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
        if not isinstance(other, FoundationModelForListModelCustomizationJobsInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FoundationModelForListModelCustomizationJobsInput):
            return True

        return self.to_dict() != other.to_dict()
