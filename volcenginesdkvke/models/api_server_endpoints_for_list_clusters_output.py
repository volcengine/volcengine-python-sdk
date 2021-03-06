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


class ApiServerEndpointsForListClustersOutput(object):
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
        'private_ip': 'PrivateIpForListClustersOutput',
        'public_ip': 'PublicIpForListClustersOutput'
    }

    attribute_map = {
        'private_ip': 'PrivateIp',
        'public_ip': 'PublicIp'
    }

    def __init__(self, private_ip=None, public_ip=None, _configuration=None):  # noqa: E501
        """ApiServerEndpointsForListClustersOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._private_ip = None
        self._public_ip = None
        self.discriminator = None

        if private_ip is not None:
            self.private_ip = private_ip
        if public_ip is not None:
            self.public_ip = public_ip

    @property
    def private_ip(self):
        """Gets the private_ip of this ApiServerEndpointsForListClustersOutput.  # noqa: E501


        :return: The private_ip of this ApiServerEndpointsForListClustersOutput.  # noqa: E501
        :rtype: PrivateIpForListClustersOutput
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """Sets the private_ip of this ApiServerEndpointsForListClustersOutput.


        :param private_ip: The private_ip of this ApiServerEndpointsForListClustersOutput.  # noqa: E501
        :type: PrivateIpForListClustersOutput
        """

        self._private_ip = private_ip

    @property
    def public_ip(self):
        """Gets the public_ip of this ApiServerEndpointsForListClustersOutput.  # noqa: E501


        :return: The public_ip of this ApiServerEndpointsForListClustersOutput.  # noqa: E501
        :rtype: PublicIpForListClustersOutput
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Sets the public_ip of this ApiServerEndpointsForListClustersOutput.


        :param public_ip: The public_ip of this ApiServerEndpointsForListClustersOutput.  # noqa: E501
        :type: PublicIpForListClustersOutput
        """

        self._public_ip = public_ip

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
        if issubclass(ApiServerEndpointsForListClustersOutput, dict):
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
        if not isinstance(other, ApiServerEndpointsForListClustersOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApiServerEndpointsForListClustersOutput):
            return True

        return self.to_dict() != other.to_dict()
