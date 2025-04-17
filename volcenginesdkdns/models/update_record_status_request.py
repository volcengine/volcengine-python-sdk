# coding: utf-8

"""
    dns

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class UpdateRecordStatusRequest(object):
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
        'enable': 'bool',
        'project_name': 'str',
        'record_id': 'str'
    }

    attribute_map = {
        'enable': 'Enable',
        'project_name': 'ProjectName',
        'record_id': 'RecordID'
    }

    def __init__(self, enable=None, project_name=None, record_id=None, _configuration=None):  # noqa: E501
        """UpdateRecordStatusRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._enable = None
        self._project_name = None
        self._record_id = None
        self.discriminator = None

        if enable is not None:
            self.enable = enable
        if project_name is not None:
            self.project_name = project_name
        self.record_id = record_id

    @property
    def enable(self):
        """Gets the enable of this UpdateRecordStatusRequest.  # noqa: E501


        :return: The enable of this UpdateRecordStatusRequest.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this UpdateRecordStatusRequest.


        :param enable: The enable of this UpdateRecordStatusRequest.  # noqa: E501
        :type: bool
        """

        self._enable = enable

    @property
    def project_name(self):
        """Gets the project_name of this UpdateRecordStatusRequest.  # noqa: E501


        :return: The project_name of this UpdateRecordStatusRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this UpdateRecordStatusRequest.


        :param project_name: The project_name of this UpdateRecordStatusRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def record_id(self):
        """Gets the record_id of this UpdateRecordStatusRequest.  # noqa: E501


        :return: The record_id of this UpdateRecordStatusRequest.  # noqa: E501
        :rtype: str
        """
        return self._record_id

    @record_id.setter
    def record_id(self, record_id):
        """Sets the record_id of this UpdateRecordStatusRequest.


        :param record_id: The record_id of this UpdateRecordStatusRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and record_id is None:
            raise ValueError("Invalid value for `record_id`, must not be `None`")  # noqa: E501

        self._record_id = record_id

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
        if issubclass(UpdateRecordStatusRequest, dict):
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
        if not isinstance(other, UpdateRecordStatusRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateRecordStatusRequest):
            return True

        return self.to_dict() != other.to_dict()
