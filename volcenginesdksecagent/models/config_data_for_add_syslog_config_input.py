# coding: utf-8

"""
    sec_agent

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ConfigDataForAddSyslogConfigInput(object):
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
        'api_key': 'str',
        'application_uids': 'list[str]',
        'data_source_name': 'str'
    }

    attribute_map = {
        'api_key': 'APIKey',
        'application_uids': 'ApplicationUIDs',
        'data_source_name': 'DataSourceName'
    }

    def __init__(self, api_key=None, application_uids=None, data_source_name=None, _configuration=None):  # noqa: E501
        """ConfigDataForAddSyslogConfigInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._api_key = None
        self._application_uids = None
        self._data_source_name = None
        self.discriminator = None

        if api_key is not None:
            self.api_key = api_key
        if application_uids is not None:
            self.application_uids = application_uids
        if data_source_name is not None:
            self.data_source_name = data_source_name

    @property
    def api_key(self):
        """Gets the api_key of this ConfigDataForAddSyslogConfigInput.  # noqa: E501


        :return: The api_key of this ConfigDataForAddSyslogConfigInput.  # noqa: E501
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """Sets the api_key of this ConfigDataForAddSyslogConfigInput.


        :param api_key: The api_key of this ConfigDataForAddSyslogConfigInput.  # noqa: E501
        :type: str
        """

        self._api_key = api_key

    @property
    def application_uids(self):
        """Gets the application_uids of this ConfigDataForAddSyslogConfigInput.  # noqa: E501


        :return: The application_uids of this ConfigDataForAddSyslogConfigInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._application_uids

    @application_uids.setter
    def application_uids(self, application_uids):
        """Sets the application_uids of this ConfigDataForAddSyslogConfigInput.


        :param application_uids: The application_uids of this ConfigDataForAddSyslogConfigInput.  # noqa: E501
        :type: list[str]
        """

        self._application_uids = application_uids

    @property
    def data_source_name(self):
        """Gets the data_source_name of this ConfigDataForAddSyslogConfigInput.  # noqa: E501


        :return: The data_source_name of this ConfigDataForAddSyslogConfigInput.  # noqa: E501
        :rtype: str
        """
        return self._data_source_name

    @data_source_name.setter
    def data_source_name(self, data_source_name):
        """Sets the data_source_name of this ConfigDataForAddSyslogConfigInput.


        :param data_source_name: The data_source_name of this ConfigDataForAddSyslogConfigInput.  # noqa: E501
        :type: str
        """

        self._data_source_name = data_source_name

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
        if issubclass(ConfigDataForAddSyslogConfigInput, dict):
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
        if not isinstance(other, ConfigDataForAddSyslogConfigInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConfigDataForAddSyslogConfigInput):
            return True

        return self.to_dict() != other.to_dict()
