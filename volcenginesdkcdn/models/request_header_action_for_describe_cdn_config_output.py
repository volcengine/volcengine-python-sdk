# coding: utf-8

"""
    cdn

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class RequestHeaderActionForDescribeCdnConfigOutput(object):
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
        'request_header_instances': 'list[RequestHeaderInstanceForDescribeCdnConfigOutput]'
    }

    attribute_map = {
        'request_header_instances': 'RequestHeaderInstances'
    }

    def __init__(self, request_header_instances=None, _configuration=None):  # noqa: E501
        """RequestHeaderActionForDescribeCdnConfigOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._request_header_instances = None
        self.discriminator = None

        if request_header_instances is not None:
            self.request_header_instances = request_header_instances

    @property
    def request_header_instances(self):
        """Gets the request_header_instances of this RequestHeaderActionForDescribeCdnConfigOutput.  # noqa: E501


        :return: The request_header_instances of this RequestHeaderActionForDescribeCdnConfigOutput.  # noqa: E501
        :rtype: list[RequestHeaderInstanceForDescribeCdnConfigOutput]
        """
        return self._request_header_instances

    @request_header_instances.setter
    def request_header_instances(self, request_header_instances):
        """Sets the request_header_instances of this RequestHeaderActionForDescribeCdnConfigOutput.


        :param request_header_instances: The request_header_instances of this RequestHeaderActionForDescribeCdnConfigOutput.  # noqa: E501
        :type: list[RequestHeaderInstanceForDescribeCdnConfigOutput]
        """

        self._request_header_instances = request_header_instances

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
        if issubclass(RequestHeaderActionForDescribeCdnConfigOutput, dict):
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
        if not isinstance(other, RequestHeaderActionForDescribeCdnConfigOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RequestHeaderActionForDescribeCdnConfigOutput):
            return True

        return self.to_dict() != other.to_dict()