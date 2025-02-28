# coding: utf-8

"""
    cr

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DeleteTagsRequest(object):
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
        'names': 'list[str]',
        'namespace': 'str',
        'registry': 'str',
        'repository': 'str'
    }

    attribute_map = {
        'names': 'Names',
        'namespace': 'Namespace',
        'registry': 'Registry',
        'repository': 'Repository'
    }

    def __init__(self, names=None, namespace=None, registry=None, repository=None, _configuration=None):  # noqa: E501
        """DeleteTagsRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._names = None
        self._namespace = None
        self._registry = None
        self._repository = None
        self.discriminator = None

        if names is not None:
            self.names = names
        self.namespace = namespace
        self.registry = registry
        self.repository = repository

    @property
    def names(self):
        """Gets the names of this DeleteTagsRequest.  # noqa: E501


        :return: The names of this DeleteTagsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._names

    @names.setter
    def names(self, names):
        """Sets the names of this DeleteTagsRequest.


        :param names: The names of this DeleteTagsRequest.  # noqa: E501
        :type: list[str]
        """

        self._names = names

    @property
    def namespace(self):
        """Gets the namespace of this DeleteTagsRequest.  # noqa: E501


        :return: The namespace of this DeleteTagsRequest.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this DeleteTagsRequest.


        :param namespace: The namespace of this DeleteTagsRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and namespace is None:
            raise ValueError("Invalid value for `namespace`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                namespace is not None and len(namespace) > 90):
            raise ValueError("Invalid value for `namespace`, length must be less than or equal to `90`")  # noqa: E501
        if (self._configuration.client_side_validation and
                namespace is not None and len(namespace) < 2):
            raise ValueError("Invalid value for `namespace`, length must be greater than or equal to `2`")  # noqa: E501

        self._namespace = namespace

    @property
    def registry(self):
        """Gets the registry of this DeleteTagsRequest.  # noqa: E501


        :return: The registry of this DeleteTagsRequest.  # noqa: E501
        :rtype: str
        """
        return self._registry

    @registry.setter
    def registry(self, registry):
        """Sets the registry of this DeleteTagsRequest.


        :param registry: The registry of this DeleteTagsRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and registry is None:
            raise ValueError("Invalid value for `registry`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                registry is not None and len(registry) > 30):
            raise ValueError("Invalid value for `registry`, length must be less than or equal to `30`")  # noqa: E501
        if (self._configuration.client_side_validation and
                registry is not None and len(registry) < 3):
            raise ValueError("Invalid value for `registry`, length must be greater than or equal to `3`")  # noqa: E501

        self._registry = registry

    @property
    def repository(self):
        """Gets the repository of this DeleteTagsRequest.  # noqa: E501


        :return: The repository of this DeleteTagsRequest.  # noqa: E501
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this DeleteTagsRequest.


        :param repository: The repository of this DeleteTagsRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and repository is None:
            raise ValueError("Invalid value for `repository`, must not be `None`")  # noqa: E501

        self._repository = repository

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
        if issubclass(DeleteTagsRequest, dict):
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
        if not isinstance(other, DeleteTagsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeleteTagsRequest):
            return True

        return self.to_dict() != other.to_dict()
