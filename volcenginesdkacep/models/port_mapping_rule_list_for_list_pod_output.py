# coding: utf-8

"""
    acep

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class PortMappingRuleListForListPodOutput(object):
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
        'port_mapping_rule_id': 'str',
        'protocol': 'str',
        'public_ip': 'str',
        'public_port': 'int',
        'public_port_info_list': 'list[PublicPortInfoListForListPodOutput]',
        'source_port': 'int',
        'status': 'int'
    }

    attribute_map = {
        'port_mapping_rule_id': 'PortMappingRuleId',
        'protocol': 'Protocol',
        'public_ip': 'PublicIp',
        'public_port': 'PublicPort',
        'public_port_info_list': 'PublicPortInfoList',
        'source_port': 'SourcePort',
        'status': 'Status'
    }

    def __init__(self, port_mapping_rule_id=None, protocol=None, public_ip=None, public_port=None, public_port_info_list=None, source_port=None, status=None, _configuration=None):  # noqa: E501
        """PortMappingRuleListForListPodOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._port_mapping_rule_id = None
        self._protocol = None
        self._public_ip = None
        self._public_port = None
        self._public_port_info_list = None
        self._source_port = None
        self._status = None
        self.discriminator = None

        if port_mapping_rule_id is not None:
            self.port_mapping_rule_id = port_mapping_rule_id
        if protocol is not None:
            self.protocol = protocol
        if public_ip is not None:
            self.public_ip = public_ip
        if public_port is not None:
            self.public_port = public_port
        if public_port_info_list is not None:
            self.public_port_info_list = public_port_info_list
        if source_port is not None:
            self.source_port = source_port
        if status is not None:
            self.status = status

    @property
    def port_mapping_rule_id(self):
        """Gets the port_mapping_rule_id of this PortMappingRuleListForListPodOutput.  # noqa: E501


        :return: The port_mapping_rule_id of this PortMappingRuleListForListPodOutput.  # noqa: E501
        :rtype: str
        """
        return self._port_mapping_rule_id

    @port_mapping_rule_id.setter
    def port_mapping_rule_id(self, port_mapping_rule_id):
        """Sets the port_mapping_rule_id of this PortMappingRuleListForListPodOutput.


        :param port_mapping_rule_id: The port_mapping_rule_id of this PortMappingRuleListForListPodOutput.  # noqa: E501
        :type: str
        """

        self._port_mapping_rule_id = port_mapping_rule_id

    @property
    def protocol(self):
        """Gets the protocol of this PortMappingRuleListForListPodOutput.  # noqa: E501


        :return: The protocol of this PortMappingRuleListForListPodOutput.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this PortMappingRuleListForListPodOutput.


        :param protocol: The protocol of this PortMappingRuleListForListPodOutput.  # noqa: E501
        :type: str
        """

        self._protocol = protocol

    @property
    def public_ip(self):
        """Gets the public_ip of this PortMappingRuleListForListPodOutput.  # noqa: E501


        :return: The public_ip of this PortMappingRuleListForListPodOutput.  # noqa: E501
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Sets the public_ip of this PortMappingRuleListForListPodOutput.


        :param public_ip: The public_ip of this PortMappingRuleListForListPodOutput.  # noqa: E501
        :type: str
        """

        self._public_ip = public_ip

    @property
    def public_port(self):
        """Gets the public_port of this PortMappingRuleListForListPodOutput.  # noqa: E501


        :return: The public_port of this PortMappingRuleListForListPodOutput.  # noqa: E501
        :rtype: int
        """
        return self._public_port

    @public_port.setter
    def public_port(self, public_port):
        """Sets the public_port of this PortMappingRuleListForListPodOutput.


        :param public_port: The public_port of this PortMappingRuleListForListPodOutput.  # noqa: E501
        :type: int
        """

        self._public_port = public_port

    @property
    def public_port_info_list(self):
        """Gets the public_port_info_list of this PortMappingRuleListForListPodOutput.  # noqa: E501


        :return: The public_port_info_list of this PortMappingRuleListForListPodOutput.  # noqa: E501
        :rtype: list[PublicPortInfoListForListPodOutput]
        """
        return self._public_port_info_list

    @public_port_info_list.setter
    def public_port_info_list(self, public_port_info_list):
        """Sets the public_port_info_list of this PortMappingRuleListForListPodOutput.


        :param public_port_info_list: The public_port_info_list of this PortMappingRuleListForListPodOutput.  # noqa: E501
        :type: list[PublicPortInfoListForListPodOutput]
        """

        self._public_port_info_list = public_port_info_list

    @property
    def source_port(self):
        """Gets the source_port of this PortMappingRuleListForListPodOutput.  # noqa: E501


        :return: The source_port of this PortMappingRuleListForListPodOutput.  # noqa: E501
        :rtype: int
        """
        return self._source_port

    @source_port.setter
    def source_port(self, source_port):
        """Sets the source_port of this PortMappingRuleListForListPodOutput.


        :param source_port: The source_port of this PortMappingRuleListForListPodOutput.  # noqa: E501
        :type: int
        """

        self._source_port = source_port

    @property
    def status(self):
        """Gets the status of this PortMappingRuleListForListPodOutput.  # noqa: E501


        :return: The status of this PortMappingRuleListForListPodOutput.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PortMappingRuleListForListPodOutput.


        :param status: The status of this PortMappingRuleListForListPodOutput.  # noqa: E501
        :type: int
        """

        self._status = status

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
        if issubclass(PortMappingRuleListForListPodOutput, dict):
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
        if not isinstance(other, PortMappingRuleListForListPodOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PortMappingRuleListForListPodOutput):
            return True

        return self.to_dict() != other.to_dict()
