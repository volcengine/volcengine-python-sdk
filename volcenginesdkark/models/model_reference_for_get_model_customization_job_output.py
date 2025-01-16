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


class ModelReferenceForGetModelCustomizationJobOutput(object):
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
        'custom_model_id': 'str',
        'foundation_model': 'FoundationModelForGetModelCustomizationJobOutput'
    }

    attribute_map = {
        'custom_model_id': 'CustomModelId',
        'foundation_model': 'FoundationModel'
    }

    def __init__(self, custom_model_id=None, foundation_model=None, _configuration=None):  # noqa: E501
        """ModelReferenceForGetModelCustomizationJobOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._custom_model_id = None
        self._foundation_model = None
        self.discriminator = None

        if custom_model_id is not None:
            self.custom_model_id = custom_model_id
        if foundation_model is not None:
            self.foundation_model = foundation_model

    @property
    def custom_model_id(self):
        """Gets the custom_model_id of this ModelReferenceForGetModelCustomizationJobOutput.  # noqa: E501


        :return: The custom_model_id of this ModelReferenceForGetModelCustomizationJobOutput.  # noqa: E501
        :rtype: str
        """
        return self._custom_model_id

    @custom_model_id.setter
    def custom_model_id(self, custom_model_id):
        """Sets the custom_model_id of this ModelReferenceForGetModelCustomizationJobOutput.


        :param custom_model_id: The custom_model_id of this ModelReferenceForGetModelCustomizationJobOutput.  # noqa: E501
        :type: str
        """

        self._custom_model_id = custom_model_id

    @property
    def foundation_model(self):
        """Gets the foundation_model of this ModelReferenceForGetModelCustomizationJobOutput.  # noqa: E501


        :return: The foundation_model of this ModelReferenceForGetModelCustomizationJobOutput.  # noqa: E501
        :rtype: FoundationModelForGetModelCustomizationJobOutput
        """
        return self._foundation_model

    @foundation_model.setter
    def foundation_model(self, foundation_model):
        """Sets the foundation_model of this ModelReferenceForGetModelCustomizationJobOutput.


        :param foundation_model: The foundation_model of this ModelReferenceForGetModelCustomizationJobOutput.  # noqa: E501
        :type: FoundationModelForGetModelCustomizationJobOutput
        """

        self._foundation_model = foundation_model

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
        if issubclass(ModelReferenceForGetModelCustomizationJobOutput, dict):
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
        if not isinstance(other, ModelReferenceForGetModelCustomizationJobOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelReferenceForGetModelCustomizationJobOutput):
            return True

        return self.to_dict() != other.to_dict()
