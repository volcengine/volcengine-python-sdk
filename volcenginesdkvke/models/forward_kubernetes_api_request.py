# coding: utf-8

"""
    vke

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ForwardKubernetesApiRequest(object):
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
        'body': 'str',
        'cluster_id': 'str',
        'headers': 'list[HeaderForForwardKubernetesApiInput]',
        'method': 'str',
        'path': 'str'
    }

    attribute_map = {
        'body': 'Body',
        'cluster_id': 'ClusterId',
        'headers': 'Headers',
        'method': 'Method',
        'path': 'Path'
    }

    def __init__(self, body=None, cluster_id=None, headers=None, method=None, path=None, _configuration=None):  # noqa: E501
        """ForwardKubernetesApiRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._body = None
        self._cluster_id = None
        self._headers = None
        self._method = None
        self._path = None
        self.discriminator = None

        if body is not None:
            self.body = body
        self.cluster_id = cluster_id
        if headers is not None:
            self.headers = headers
        self.method = method
        self.path = path

    @property
    def body(self):
        """Gets the body of this ForwardKubernetesApiRequest.  # noqa: E501


        :return: The body of this ForwardKubernetesApiRequest.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ForwardKubernetesApiRequest.


        :param body: The body of this ForwardKubernetesApiRequest.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ForwardKubernetesApiRequest.  # noqa: E501


        :return: The cluster_id of this ForwardKubernetesApiRequest.  # noqa: E501
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ForwardKubernetesApiRequest.


        :param cluster_id: The cluster_id of this ForwardKubernetesApiRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and cluster_id is None:
            raise ValueError("Invalid value for `cluster_id`, must not be `None`")  # noqa: E501

        self._cluster_id = cluster_id

    @property
    def headers(self):
        """Gets the headers of this ForwardKubernetesApiRequest.  # noqa: E501


        :return: The headers of this ForwardKubernetesApiRequest.  # noqa: E501
        :rtype: list[HeaderForForwardKubernetesApiInput]
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this ForwardKubernetesApiRequest.


        :param headers: The headers of this ForwardKubernetesApiRequest.  # noqa: E501
        :type: list[HeaderForForwardKubernetesApiInput]
        """

        self._headers = headers

    @property
    def method(self):
        """Gets the method of this ForwardKubernetesApiRequest.  # noqa: E501


        :return: The method of this ForwardKubernetesApiRequest.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this ForwardKubernetesApiRequest.


        :param method: The method of this ForwardKubernetesApiRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and method is None:
            raise ValueError("Invalid value for `method`, must not be `None`")  # noqa: E501

        self._method = method

    @property
    def path(self):
        """Gets the path of this ForwardKubernetesApiRequest.  # noqa: E501


        :return: The path of this ForwardKubernetesApiRequest.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ForwardKubernetesApiRequest.


        :param path: The path of this ForwardKubernetesApiRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

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
        if issubclass(ForwardKubernetesApiRequest, dict):
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
        if not isinstance(other, ForwardKubernetesApiRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ForwardKubernetesApiRequest):
            return True

        return self.to_dict() != other.to_dict()
