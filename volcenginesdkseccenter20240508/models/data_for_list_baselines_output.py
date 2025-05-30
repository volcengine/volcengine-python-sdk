# coding: utf-8

"""
    seccenter20240508

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DataForListBaselinesOutput(object):
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
        'baseline_list': 'list[BaselineListForListBaselinesOutput]',
        'detect_status': 'str'
    }

    attribute_map = {
        'baseline_list': 'BaselineList',
        'detect_status': 'DetectStatus'
    }

    def __init__(self, baseline_list=None, detect_status=None, _configuration=None):  # noqa: E501
        """DataForListBaselinesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._baseline_list = None
        self._detect_status = None
        self.discriminator = None

        if baseline_list is not None:
            self.baseline_list = baseline_list
        if detect_status is not None:
            self.detect_status = detect_status

    @property
    def baseline_list(self):
        """Gets the baseline_list of this DataForListBaselinesOutput.  # noqa: E501


        :return: The baseline_list of this DataForListBaselinesOutput.  # noqa: E501
        :rtype: list[BaselineListForListBaselinesOutput]
        """
        return self._baseline_list

    @baseline_list.setter
    def baseline_list(self, baseline_list):
        """Sets the baseline_list of this DataForListBaselinesOutput.


        :param baseline_list: The baseline_list of this DataForListBaselinesOutput.  # noqa: E501
        :type: list[BaselineListForListBaselinesOutput]
        """

        self._baseline_list = baseline_list

    @property
    def detect_status(self):
        """Gets the detect_status of this DataForListBaselinesOutput.  # noqa: E501


        :return: The detect_status of this DataForListBaselinesOutput.  # noqa: E501
        :rtype: str
        """
        return self._detect_status

    @detect_status.setter
    def detect_status(self, detect_status):
        """Sets the detect_status of this DataForListBaselinesOutput.


        :param detect_status: The detect_status of this DataForListBaselinesOutput.  # noqa: E501
        :type: str
        """

        self._detect_status = detect_status

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
        if issubclass(DataForListBaselinesOutput, dict):
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
        if not isinstance(other, DataForListBaselinesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataForListBaselinesOutput):
            return True

        return self.to_dict() != other.to_dict()
