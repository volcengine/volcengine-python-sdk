# coding: utf-8

"""
    waf

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class CloudAccessConfigForListDomainOutput(object):
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
        'access_protocol': 'str',
        'instance_id': 'str',
        'listener_id': 'str',
        'port': 'str',
        'protocol': 'str'
    }

    attribute_map = {
        'access_protocol': 'AccessProtocol',
        'instance_id': 'InstanceID',
        'listener_id': 'ListenerID',
        'port': 'Port',
        'protocol': 'Protocol'
    }

    def __init__(self, access_protocol=None, instance_id=None, listener_id=None, port=None, protocol=None, _configuration=None):  # noqa: E501
        """CloudAccessConfigForListDomainOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._access_protocol = None
        self._instance_id = None
        self._listener_id = None
        self._port = None
        self._protocol = None
        self.discriminator = None

        if access_protocol is not None:
            self.access_protocol = access_protocol
        if instance_id is not None:
            self.instance_id = instance_id
        if listener_id is not None:
            self.listener_id = listener_id
        if port is not None:
            self.port = port
        if protocol is not None:
            self.protocol = protocol

    @property
    def access_protocol(self):
        """Gets the access_protocol of this CloudAccessConfigForListDomainOutput.  # noqa: E501


        :return: The access_protocol of this CloudAccessConfigForListDomainOutput.  # noqa: E501
        :rtype: str
        """
        return self._access_protocol

    @access_protocol.setter
    def access_protocol(self, access_protocol):
        """Sets the access_protocol of this CloudAccessConfigForListDomainOutput.


        :param access_protocol: The access_protocol of this CloudAccessConfigForListDomainOutput.  # noqa: E501
        :type: str
        """

        self._access_protocol = access_protocol

    @property
    def instance_id(self):
        """Gets the instance_id of this CloudAccessConfigForListDomainOutput.  # noqa: E501


        :return: The instance_id of this CloudAccessConfigForListDomainOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this CloudAccessConfigForListDomainOutput.


        :param instance_id: The instance_id of this CloudAccessConfigForListDomainOutput.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def listener_id(self):
        """Gets the listener_id of this CloudAccessConfigForListDomainOutput.  # noqa: E501


        :return: The listener_id of this CloudAccessConfigForListDomainOutput.  # noqa: E501
        :rtype: str
        """
        return self._listener_id

    @listener_id.setter
    def listener_id(self, listener_id):
        """Sets the listener_id of this CloudAccessConfigForListDomainOutput.


        :param listener_id: The listener_id of this CloudAccessConfigForListDomainOutput.  # noqa: E501
        :type: str
        """

        self._listener_id = listener_id

    @property
    def port(self):
        """Gets the port of this CloudAccessConfigForListDomainOutput.  # noqa: E501


        :return: The port of this CloudAccessConfigForListDomainOutput.  # noqa: E501
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this CloudAccessConfigForListDomainOutput.


        :param port: The port of this CloudAccessConfigForListDomainOutput.  # noqa: E501
        :type: str
        """

        self._port = port

    @property
    def protocol(self):
        """Gets the protocol of this CloudAccessConfigForListDomainOutput.  # noqa: E501


        :return: The protocol of this CloudAccessConfigForListDomainOutput.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this CloudAccessConfigForListDomainOutput.


        :param protocol: The protocol of this CloudAccessConfigForListDomainOutput.  # noqa: E501
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
        if issubclass(CloudAccessConfigForListDomainOutput, dict):
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
        if not isinstance(other, CloudAccessConfigForListDomainOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CloudAccessConfigForListDomainOutput):
            return True

        return self.to_dict() != other.to_dict()
