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


class DataForGetModelCustomizationJobOutput(object):
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
        'encryption_keyring_type': 'str',
        'kms_trn': 'str',
        'training_set': 'TrainingSetForGetModelCustomizationJobOutput',
        'validation_percentage': 'int',
        'validation_set': 'ValidationSetForGetModelCustomizationJobOutput'
    }

    attribute_map = {
        'encryption_keyring_type': 'EncryptionKeyringType',
        'kms_trn': 'KMSTrn',
        'training_set': 'TrainingSet',
        'validation_percentage': 'ValidationPercentage',
        'validation_set': 'ValidationSet'
    }

    def __init__(self, encryption_keyring_type=None, kms_trn=None, training_set=None, validation_percentage=None, validation_set=None, _configuration=None):  # noqa: E501
        """DataForGetModelCustomizationJobOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._encryption_keyring_type = None
        self._kms_trn = None
        self._training_set = None
        self._validation_percentage = None
        self._validation_set = None
        self.discriminator = None

        if encryption_keyring_type is not None:
            self.encryption_keyring_type = encryption_keyring_type
        if kms_trn is not None:
            self.kms_trn = kms_trn
        if training_set is not None:
            self.training_set = training_set
        if validation_percentage is not None:
            self.validation_percentage = validation_percentage
        if validation_set is not None:
            self.validation_set = validation_set

    @property
    def encryption_keyring_type(self):
        """Gets the encryption_keyring_type of this DataForGetModelCustomizationJobOutput.  # noqa: E501


        :return: The encryption_keyring_type of this DataForGetModelCustomizationJobOutput.  # noqa: E501
        :rtype: str
        """
        return self._encryption_keyring_type

    @encryption_keyring_type.setter
    def encryption_keyring_type(self, encryption_keyring_type):
        """Sets the encryption_keyring_type of this DataForGetModelCustomizationJobOutput.


        :param encryption_keyring_type: The encryption_keyring_type of this DataForGetModelCustomizationJobOutput.  # noqa: E501
        :type: str
        """

        self._encryption_keyring_type = encryption_keyring_type

    @property
    def kms_trn(self):
        """Gets the kms_trn of this DataForGetModelCustomizationJobOutput.  # noqa: E501


        :return: The kms_trn of this DataForGetModelCustomizationJobOutput.  # noqa: E501
        :rtype: str
        """
        return self._kms_trn

    @kms_trn.setter
    def kms_trn(self, kms_trn):
        """Sets the kms_trn of this DataForGetModelCustomizationJobOutput.


        :param kms_trn: The kms_trn of this DataForGetModelCustomizationJobOutput.  # noqa: E501
        :type: str
        """

        self._kms_trn = kms_trn

    @property
    def training_set(self):
        """Gets the training_set of this DataForGetModelCustomizationJobOutput.  # noqa: E501


        :return: The training_set of this DataForGetModelCustomizationJobOutput.  # noqa: E501
        :rtype: TrainingSetForGetModelCustomizationJobOutput
        """
        return self._training_set

    @training_set.setter
    def training_set(self, training_set):
        """Sets the training_set of this DataForGetModelCustomizationJobOutput.


        :param training_set: The training_set of this DataForGetModelCustomizationJobOutput.  # noqa: E501
        :type: TrainingSetForGetModelCustomizationJobOutput
        """

        self._training_set = training_set

    @property
    def validation_percentage(self):
        """Gets the validation_percentage of this DataForGetModelCustomizationJobOutput.  # noqa: E501


        :return: The validation_percentage of this DataForGetModelCustomizationJobOutput.  # noqa: E501
        :rtype: int
        """
        return self._validation_percentage

    @validation_percentage.setter
    def validation_percentage(self, validation_percentage):
        """Sets the validation_percentage of this DataForGetModelCustomizationJobOutput.


        :param validation_percentage: The validation_percentage of this DataForGetModelCustomizationJobOutput.  # noqa: E501
        :type: int
        """

        self._validation_percentage = validation_percentage

    @property
    def validation_set(self):
        """Gets the validation_set of this DataForGetModelCustomizationJobOutput.  # noqa: E501


        :return: The validation_set of this DataForGetModelCustomizationJobOutput.  # noqa: E501
        :rtype: ValidationSetForGetModelCustomizationJobOutput
        """
        return self._validation_set

    @validation_set.setter
    def validation_set(self, validation_set):
        """Sets the validation_set of this DataForGetModelCustomizationJobOutput.


        :param validation_set: The validation_set of this DataForGetModelCustomizationJobOutput.  # noqa: E501
        :type: ValidationSetForGetModelCustomizationJobOutput
        """

        self._validation_set = validation_set

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
        if issubclass(DataForGetModelCustomizationJobOutput, dict):
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
        if not isinstance(other, DataForGetModelCustomizationJobOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataForGetModelCustomizationJobOutput):
            return True

        return self.to_dict() != other.to_dict()
