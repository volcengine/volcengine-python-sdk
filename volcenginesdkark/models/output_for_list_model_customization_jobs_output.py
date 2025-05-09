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


class OutputForListModelCustomizationJobsOutput(object):
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
        'custom_model_create_time_unix': 'int',
        'custom_model_id': 'str',
        'index': 'int',
        'name': 'str',
        'status': 'str'
    }

    attribute_map = {
        'custom_model_create_time_unix': 'CustomModelCreateTimeUnix',
        'custom_model_id': 'CustomModelId',
        'index': 'Index',
        'name': 'Name',
        'status': 'Status'
    }

    def __init__(self, custom_model_create_time_unix=None, custom_model_id=None, index=None, name=None, status=None, _configuration=None):  # noqa: E501
        """OutputForListModelCustomizationJobsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._custom_model_create_time_unix = None
        self._custom_model_id = None
        self._index = None
        self._name = None
        self._status = None
        self.discriminator = None

        if custom_model_create_time_unix is not None:
            self.custom_model_create_time_unix = custom_model_create_time_unix
        if custom_model_id is not None:
            self.custom_model_id = custom_model_id
        if index is not None:
            self.index = index
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status

    @property
    def custom_model_create_time_unix(self):
        """Gets the custom_model_create_time_unix of this OutputForListModelCustomizationJobsOutput.  # noqa: E501


        :return: The custom_model_create_time_unix of this OutputForListModelCustomizationJobsOutput.  # noqa: E501
        :rtype: int
        """
        return self._custom_model_create_time_unix

    @custom_model_create_time_unix.setter
    def custom_model_create_time_unix(self, custom_model_create_time_unix):
        """Sets the custom_model_create_time_unix of this OutputForListModelCustomizationJobsOutput.


        :param custom_model_create_time_unix: The custom_model_create_time_unix of this OutputForListModelCustomizationJobsOutput.  # noqa: E501
        :type: int
        """

        self._custom_model_create_time_unix = custom_model_create_time_unix

    @property
    def custom_model_id(self):
        """Gets the custom_model_id of this OutputForListModelCustomizationJobsOutput.  # noqa: E501


        :return: The custom_model_id of this OutputForListModelCustomizationJobsOutput.  # noqa: E501
        :rtype: str
        """
        return self._custom_model_id

    @custom_model_id.setter
    def custom_model_id(self, custom_model_id):
        """Sets the custom_model_id of this OutputForListModelCustomizationJobsOutput.


        :param custom_model_id: The custom_model_id of this OutputForListModelCustomizationJobsOutput.  # noqa: E501
        :type: str
        """

        self._custom_model_id = custom_model_id

    @property
    def index(self):
        """Gets the index of this OutputForListModelCustomizationJobsOutput.  # noqa: E501


        :return: The index of this OutputForListModelCustomizationJobsOutput.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this OutputForListModelCustomizationJobsOutput.


        :param index: The index of this OutputForListModelCustomizationJobsOutput.  # noqa: E501
        :type: int
        """

        self._index = index

    @property
    def name(self):
        """Gets the name of this OutputForListModelCustomizationJobsOutput.  # noqa: E501


        :return: The name of this OutputForListModelCustomizationJobsOutput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OutputForListModelCustomizationJobsOutput.


        :param name: The name of this OutputForListModelCustomizationJobsOutput.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def status(self):
        """Gets the status of this OutputForListModelCustomizationJobsOutput.  # noqa: E501


        :return: The status of this OutputForListModelCustomizationJobsOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this OutputForListModelCustomizationJobsOutput.


        :param status: The status of this OutputForListModelCustomizationJobsOutput.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(OutputForListModelCustomizationJobsOutput, dict):
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
        if not isinstance(other, OutputForListModelCustomizationJobsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OutputForListModelCustomizationJobsOutput):
            return True

        return self.to_dict() != other.to_dict()
