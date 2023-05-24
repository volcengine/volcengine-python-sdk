# coding: utf-8

"""
    alb

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ListenerForDescribeAclAttributesOutput(object):
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
        'acl_type': 'str',
        'listener_id': 'str',
        'listener_name': 'str',
        'port': 'int',
        'protocol': 'str'
    }

    attribute_map = {
        'acl_type': 'AclType',
        'listener_id': 'ListenerId',
        'listener_name': 'ListenerName',
        'port': 'Port',
        'protocol': 'Protocol'
    }

    def __init__(self, acl_type=None, listener_id=None, listener_name=None, port=None, protocol=None, _configuration=None):  # noqa: E501
        """ListenerForDescribeAclAttributesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._acl_type = None
        self._listener_id = None
        self._listener_name = None
        self._port = None
        self._protocol = None
        self.discriminator = None

        if acl_type is not None:
            self.acl_type = acl_type
        if listener_id is not None:
            self.listener_id = listener_id
        if listener_name is not None:
            self.listener_name = listener_name
        if port is not None:
            self.port = port
        if protocol is not None:
            self.protocol = protocol

    @property
    def acl_type(self):
        """Gets the acl_type of this ListenerForDescribeAclAttributesOutput.  # noqa: E501


        :return: The acl_type of this ListenerForDescribeAclAttributesOutput.  # noqa: E501
        :rtype: str
        """
        return self._acl_type

    @acl_type.setter
    def acl_type(self, acl_type):
        """Sets the acl_type of this ListenerForDescribeAclAttributesOutput.


        :param acl_type: The acl_type of this ListenerForDescribeAclAttributesOutput.  # noqa: E501
        :type: str
        """

        self._acl_type = acl_type

    @property
    def listener_id(self):
        """Gets the listener_id of this ListenerForDescribeAclAttributesOutput.  # noqa: E501


        :return: The listener_id of this ListenerForDescribeAclAttributesOutput.  # noqa: E501
        :rtype: str
        """
        return self._listener_id

    @listener_id.setter
    def listener_id(self, listener_id):
        """Sets the listener_id of this ListenerForDescribeAclAttributesOutput.


        :param listener_id: The listener_id of this ListenerForDescribeAclAttributesOutput.  # noqa: E501
        :type: str
        """

        self._listener_id = listener_id

    @property
    def listener_name(self):
        """Gets the listener_name of this ListenerForDescribeAclAttributesOutput.  # noqa: E501


        :return: The listener_name of this ListenerForDescribeAclAttributesOutput.  # noqa: E501
        :rtype: str
        """
        return self._listener_name

    @listener_name.setter
    def listener_name(self, listener_name):
        """Sets the listener_name of this ListenerForDescribeAclAttributesOutput.


        :param listener_name: The listener_name of this ListenerForDescribeAclAttributesOutput.  # noqa: E501
        :type: str
        """

        self._listener_name = listener_name

    @property
    def port(self):
        """Gets the port of this ListenerForDescribeAclAttributesOutput.  # noqa: E501


        :return: The port of this ListenerForDescribeAclAttributesOutput.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ListenerForDescribeAclAttributesOutput.


        :param port: The port of this ListenerForDescribeAclAttributesOutput.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def protocol(self):
        """Gets the protocol of this ListenerForDescribeAclAttributesOutput.  # noqa: E501


        :return: The protocol of this ListenerForDescribeAclAttributesOutput.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ListenerForDescribeAclAttributesOutput.


        :param protocol: The protocol of this ListenerForDescribeAclAttributesOutput.  # noqa: E501
        :type: str
        """

        self._protocol = protocol

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
        if issubclass(ListenerForDescribeAclAttributesOutput, dict):
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
        if not isinstance(other, ListenerForDescribeAclAttributesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListenerForDescribeAclAttributesOutput):
            return True

        return self.to_dict() != other.to_dict()
