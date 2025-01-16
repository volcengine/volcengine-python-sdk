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


class TrainingSetForGetModelCustomizationJobOutput(object):
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
        'datasets': 'list[DatasetForGetModelCustomizationJobOutput]',
        'preset_data': 'str',
        'preset_data_percentage': 'int',
        'preset_datasets': 'list[PresetDatasetForGetModelCustomizationJobOutput]',
        'tos_bucket': 'str',
        'tos_paths': 'list[str]'
    }

    attribute_map = {
        'datasets': 'Datasets',
        'preset_data': 'PresetData',
        'preset_data_percentage': 'PresetDataPercentage',
        'preset_datasets': 'PresetDatasets',
        'tos_bucket': 'TosBucket',
        'tos_paths': 'TosPaths'
    }

    def __init__(self, datasets=None, preset_data=None, preset_data_percentage=None, preset_datasets=None, tos_bucket=None, tos_paths=None, _configuration=None):  # noqa: E501
        """TrainingSetForGetModelCustomizationJobOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._datasets = None
        self._preset_data = None
        self._preset_data_percentage = None
        self._preset_datasets = None
        self._tos_bucket = None
        self._tos_paths = None
        self.discriminator = None

        if datasets is not None:
            self.datasets = datasets
        if preset_data is not None:
            self.preset_data = preset_data
        if preset_data_percentage is not None:
            self.preset_data_percentage = preset_data_percentage
        if preset_datasets is not None:
            self.preset_datasets = preset_datasets
        if tos_bucket is not None:
            self.tos_bucket = tos_bucket
        if tos_paths is not None:
            self.tos_paths = tos_paths

    @property
    def datasets(self):
        """Gets the datasets of this TrainingSetForGetModelCustomizationJobOutput.  # noqa: E501


        :return: The datasets of this TrainingSetForGetModelCustomizationJobOutput.  # noqa: E501
        :rtype: list[DatasetForGetModelCustomizationJobOutput]
        """
        return self._datasets

    @datasets.setter
    def datasets(self, datasets):
        """Sets the datasets of this TrainingSetForGetModelCustomizationJobOutput.


        :param datasets: The datasets of this TrainingSetForGetModelCustomizationJobOutput.  # noqa: E501
        :type: list[DatasetForGetModelCustomizationJobOutput]
        """

        self._datasets = datasets

    @property
    def preset_data(self):
        """Gets the preset_data of this TrainingSetForGetModelCustomizationJobOutput.  # noqa: E501


        :return: The preset_data of this TrainingSetForGetModelCustomizationJobOutput.  # noqa: E501
        :rtype: str
        """
        return self._preset_data

    @preset_data.setter
    def preset_data(self, preset_data):
        """Sets the preset_data of this TrainingSetForGetModelCustomizationJobOutput.


        :param preset_data: The preset_data of this TrainingSetForGetModelCustomizationJobOutput.  # noqa: E501
        :type: str
        """

        self._preset_data = preset_data

    @property
    def preset_data_percentage(self):
        """Gets the preset_data_percentage of this TrainingSetForGetModelCustomizationJobOutput.  # noqa: E501


        :return: The preset_data_percentage of this TrainingSetForGetModelCustomizationJobOutput.  # noqa: E501
        :rtype: int
        """
        return self._preset_data_percentage

    @preset_data_percentage.setter
    def preset_data_percentage(self, preset_data_percentage):
        """Sets the preset_data_percentage of this TrainingSetForGetModelCustomizationJobOutput.


        :param preset_data_percentage: The preset_data_percentage of this TrainingSetForGetModelCustomizationJobOutput.  # noqa: E501
        :type: int
        """

        self._preset_data_percentage = preset_data_percentage

    @property
    def preset_datasets(self):
        """Gets the preset_datasets of this TrainingSetForGetModelCustomizationJobOutput.  # noqa: E501


        :return: The preset_datasets of this TrainingSetForGetModelCustomizationJobOutput.  # noqa: E501
        :rtype: list[PresetDatasetForGetModelCustomizationJobOutput]
        """
        return self._preset_datasets

    @preset_datasets.setter
    def preset_datasets(self, preset_datasets):
        """Sets the preset_datasets of this TrainingSetForGetModelCustomizationJobOutput.


        :param preset_datasets: The preset_datasets of this TrainingSetForGetModelCustomizationJobOutput.  # noqa: E501
        :type: list[PresetDatasetForGetModelCustomizationJobOutput]
        """

        self._preset_datasets = preset_datasets

    @property
    def tos_bucket(self):
        """Gets the tos_bucket of this TrainingSetForGetModelCustomizationJobOutput.  # noqa: E501


        :return: The tos_bucket of this TrainingSetForGetModelCustomizationJobOutput.  # noqa: E501
        :rtype: str
        """
        return self._tos_bucket

    @tos_bucket.setter
    def tos_bucket(self, tos_bucket):
        """Sets the tos_bucket of this TrainingSetForGetModelCustomizationJobOutput.


        :param tos_bucket: The tos_bucket of this TrainingSetForGetModelCustomizationJobOutput.  # noqa: E501
        :type: str
        """

        self._tos_bucket = tos_bucket

    @property
    def tos_paths(self):
        """Gets the tos_paths of this TrainingSetForGetModelCustomizationJobOutput.  # noqa: E501


        :return: The tos_paths of this TrainingSetForGetModelCustomizationJobOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._tos_paths

    @tos_paths.setter
    def tos_paths(self, tos_paths):
        """Sets the tos_paths of this TrainingSetForGetModelCustomizationJobOutput.


        :param tos_paths: The tos_paths of this TrainingSetForGetModelCustomizationJobOutput.  # noqa: E501
        :type: list[str]
        """

        self._tos_paths = tos_paths

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
        if issubclass(TrainingSetForGetModelCustomizationJobOutput, dict):
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
        if not isinstance(other, TrainingSetForGetModelCustomizationJobOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TrainingSetForGetModelCustomizationJobOutput):
            return True

        return self.to_dict() != other.to_dict()
