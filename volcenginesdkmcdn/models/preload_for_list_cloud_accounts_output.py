# coding: utf-8

"""
    mcdn

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class PreloadForListCloudAccountsOutput(object):
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
        'enabled': 'bool',
        'query_endpoint': 'str',
        'submit_endpoint': 'str'
    }

    attribute_map = {
        'api_key': 'ApiKey',
        'enabled': 'Enabled',
        'query_endpoint': 'QueryEndpoint',
        'submit_endpoint': 'SubmitEndpoint'
    }

    def __init__(self, api_key=None, enabled=None, query_endpoint=None, submit_endpoint=None, _configuration=None):  # noqa: E501
        """PreloadForListCloudAccountsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._api_key = None
        self._enabled = None
        self._query_endpoint = None
        self._submit_endpoint = None
        self.discriminator = None

        if api_key is not None:
            self.api_key = api_key
        if enabled is not None:
            self.enabled = enabled
        if query_endpoint is not None:
            self.query_endpoint = query_endpoint
        if submit_endpoint is not None:
            self.submit_endpoint = submit_endpoint

    @property
    def api_key(self):
        """Gets the api_key of this PreloadForListCloudAccountsOutput.  # noqa: E501


        :return: The api_key of this PreloadForListCloudAccountsOutput.  # noqa: E501
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """Sets the api_key of this PreloadForListCloudAccountsOutput.


        :param api_key: The api_key of this PreloadForListCloudAccountsOutput.  # noqa: E501
        :type: str
        """

        self._api_key = api_key

    @property
    def enabled(self):
        """Gets the enabled of this PreloadForListCloudAccountsOutput.  # noqa: E501


        :return: The enabled of this PreloadForListCloudAccountsOutput.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this PreloadForListCloudAccountsOutput.


        :param enabled: The enabled of this PreloadForListCloudAccountsOutput.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def query_endpoint(self):
        """Gets the query_endpoint of this PreloadForListCloudAccountsOutput.  # noqa: E501


        :return: The query_endpoint of this PreloadForListCloudAccountsOutput.  # noqa: E501
        :rtype: str
        """
        return self._query_endpoint

    @query_endpoint.setter
    def query_endpoint(self, query_endpoint):
        """Sets the query_endpoint of this PreloadForListCloudAccountsOutput.


        :param query_endpoint: The query_endpoint of this PreloadForListCloudAccountsOutput.  # noqa: E501
        :type: str
        """

        self._query_endpoint = query_endpoint

    @property
    def submit_endpoint(self):
        """Gets the submit_endpoint of this PreloadForListCloudAccountsOutput.  # noqa: E501


        :return: The submit_endpoint of this PreloadForListCloudAccountsOutput.  # noqa: E501
        :rtype: str
        """
        return self._submit_endpoint

    @submit_endpoint.setter
    def submit_endpoint(self, submit_endpoint):
        """Sets the submit_endpoint of this PreloadForListCloudAccountsOutput.


        :param submit_endpoint: The submit_endpoint of this PreloadForListCloudAccountsOutput.  # noqa: E501
        :type: str
        """

        self._submit_endpoint = submit_endpoint

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
        if issubclass(PreloadForListCloudAccountsOutput, dict):
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
        if not isinstance(other, PreloadForListCloudAccountsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PreloadForListCloudAccountsOutput):
            return True

        return self.to_dict() != other.to_dict()
