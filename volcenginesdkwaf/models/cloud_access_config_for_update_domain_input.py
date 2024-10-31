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


class CloudAccessConfigForUpdateDomainInput(object):
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
        'defence_mode': 'int',
        'instance_id': 'str',
        'instance_name': 'str',
        'listener_id': 'str',
        'lost_association_from_alb': 'int',
        'port': 'str',
        'protocol': 'str'
    }

    attribute_map = {
        'access_protocol': 'AccessProtocol',
        'defence_mode': 'DefenceMode',
        'instance_id': 'InstanceID',
        'instance_name': 'InstanceName',
        'listener_id': 'ListenerID',
        'lost_association_from_alb': 'LostAssociationFromALB',
        'port': 'Port',
        'protocol': 'Protocol'
    }

    def __init__(self, access_protocol=None, defence_mode=None, instance_id=None, instance_name=None, listener_id=None, lost_association_from_alb=None, port=None, protocol=None, _configuration=None):  # noqa: E501
        """CloudAccessConfigForUpdateDomainInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._access_protocol = None
        self._defence_mode = None
        self._instance_id = None
        self._instance_name = None
        self._listener_id = None
        self._lost_association_from_alb = None
        self._port = None
        self._protocol = None
        self.discriminator = None

        if access_protocol is not None:
            self.access_protocol = access_protocol
        if defence_mode is not None:
            self.defence_mode = defence_mode
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if listener_id is not None:
            self.listener_id = listener_id
        if lost_association_from_alb is not None:
            self.lost_association_from_alb = lost_association_from_alb
        if port is not None:
            self.port = port
        if protocol is not None:
            self.protocol = protocol

    @property
    def access_protocol(self):
        """Gets the access_protocol of this CloudAccessConfigForUpdateDomainInput.  # noqa: E501


        :return: The access_protocol of this CloudAccessConfigForUpdateDomainInput.  # noqa: E501
        :rtype: str
        """
        return self._access_protocol

    @access_protocol.setter
    def access_protocol(self, access_protocol):
        """Sets the access_protocol of this CloudAccessConfigForUpdateDomainInput.


        :param access_protocol: The access_protocol of this CloudAccessConfigForUpdateDomainInput.  # noqa: E501
        :type: str
        """

        self._access_protocol = access_protocol

    @property
    def defence_mode(self):
        """Gets the defence_mode of this CloudAccessConfigForUpdateDomainInput.  # noqa: E501


        :return: The defence_mode of this CloudAccessConfigForUpdateDomainInput.  # noqa: E501
        :rtype: int
        """
        return self._defence_mode

    @defence_mode.setter
    def defence_mode(self, defence_mode):
        """Sets the defence_mode of this CloudAccessConfigForUpdateDomainInput.


        :param defence_mode: The defence_mode of this CloudAccessConfigForUpdateDomainInput.  # noqa: E501
        :type: int
        """

        self._defence_mode = defence_mode

    @property
    def instance_id(self):
        """Gets the instance_id of this CloudAccessConfigForUpdateDomainInput.  # noqa: E501


        :return: The instance_id of this CloudAccessConfigForUpdateDomainInput.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this CloudAccessConfigForUpdateDomainInput.


        :param instance_id: The instance_id of this CloudAccessConfigForUpdateDomainInput.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def instance_name(self):
        """Gets the instance_name of this CloudAccessConfigForUpdateDomainInput.  # noqa: E501


        :return: The instance_name of this CloudAccessConfigForUpdateDomainInput.  # noqa: E501
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this CloudAccessConfigForUpdateDomainInput.


        :param instance_name: The instance_name of this CloudAccessConfigForUpdateDomainInput.  # noqa: E501
        :type: str
        """

        self._instance_name = instance_name

    @property
    def listener_id(self):
        """Gets the listener_id of this CloudAccessConfigForUpdateDomainInput.  # noqa: E501


        :return: The listener_id of this CloudAccessConfigForUpdateDomainInput.  # noqa: E501
        :rtype: str
        """
        return self._listener_id

    @listener_id.setter
    def listener_id(self, listener_id):
        """Sets the listener_id of this CloudAccessConfigForUpdateDomainInput.


        :param listener_id: The listener_id of this CloudAccessConfigForUpdateDomainInput.  # noqa: E501
        :type: str
        """

        self._listener_id = listener_id

    @property
    def lost_association_from_alb(self):
        """Gets the lost_association_from_alb of this CloudAccessConfigForUpdateDomainInput.  # noqa: E501


        :return: The lost_association_from_alb of this CloudAccessConfigForUpdateDomainInput.  # noqa: E501
        :rtype: int
        """
        return self._lost_association_from_alb

    @lost_association_from_alb.setter
    def lost_association_from_alb(self, lost_association_from_alb):
        """Sets the lost_association_from_alb of this CloudAccessConfigForUpdateDomainInput.


        :param lost_association_from_alb: The lost_association_from_alb of this CloudAccessConfigForUpdateDomainInput.  # noqa: E501
        :type: int
        """

        self._lost_association_from_alb = lost_association_from_alb

    @property
    def port(self):
        """Gets the port of this CloudAccessConfigForUpdateDomainInput.  # noqa: E501


        :return: The port of this CloudAccessConfigForUpdateDomainInput.  # noqa: E501
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this CloudAccessConfigForUpdateDomainInput.


        :param port: The port of this CloudAccessConfigForUpdateDomainInput.  # noqa: E501
        :type: str
        """

        self._port = port

    @property
    def protocol(self):
        """Gets the protocol of this CloudAccessConfigForUpdateDomainInput.  # noqa: E501


        :return: The protocol of this CloudAccessConfigForUpdateDomainInput.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this CloudAccessConfigForUpdateDomainInput.


        :param protocol: The protocol of this CloudAccessConfigForUpdateDomainInput.  # noqa: E501
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
        if issubclass(CloudAccessConfigForUpdateDomainInput, dict):
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
        if not isinstance(other, CloudAccessConfigForUpdateDomainInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CloudAccessConfigForUpdateDomainInput):
            return True

        return self.to_dict() != other.to_dict()
