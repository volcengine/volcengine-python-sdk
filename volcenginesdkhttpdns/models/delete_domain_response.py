# coding: utf-8

"""
    httpdns

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DeleteDomainResponse(object):
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
        'domain': 'str',
        'id': 'int'
    }

    attribute_map = {
        'domain': 'Domain',
        'id': 'Id'
    }

    def __init__(self, domain=None, id=None, _configuration=None):  # noqa: E501
        """DeleteDomainResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._domain = None
        self._id = None
        self.discriminator = None

        if domain is not None:
            self.domain = domain
        if id is not None:
            self.id = id

    @property
    def domain(self):
        """Gets the domain of this DeleteDomainResponse.  # noqa: E501


        :return: The domain of this DeleteDomainResponse.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this DeleteDomainResponse.


        :param domain: The domain of this DeleteDomainResponse.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def id(self):
        """Gets the id of this DeleteDomainResponse.  # noqa: E501


        :return: The id of this DeleteDomainResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeleteDomainResponse.


        :param id: The id of this DeleteDomainResponse.  # noqa: E501
        :type: int
        """

        self._id = id

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
        if issubclass(DeleteDomainResponse, dict):
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
        if not isinstance(other, DeleteDomainResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeleteDomainResponse):
            return True

        return self.to_dict() != other.to_dict()
