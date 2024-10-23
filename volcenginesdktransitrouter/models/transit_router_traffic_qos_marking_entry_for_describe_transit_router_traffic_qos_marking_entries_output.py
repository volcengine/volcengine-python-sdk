# coding: utf-8

"""
    transitrouter

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput(object):
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
        'creation_time': 'str',
        'description': 'str',
        'destination_cidr_block': 'str',
        'destination_port_end': 'int',
        'destination_port_start': 'int',
        'match_dscp': 'int',
        'priority': 'int',
        'protocol': 'str',
        'remarking_dscp': 'int',
        'source_cidr_block': 'str',
        'source_port_end': 'int',
        'source_port_start': 'int',
        'status': 'str',
        'transit_router_traffic_qos_marking_entry_id': 'str',
        'transit_router_traffic_qos_marking_entry_name': 'str',
        'transit_router_traffic_qos_marking_policy_id': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'creation_time': 'CreationTime',
        'description': 'Description',
        'destination_cidr_block': 'DestinationCidrBlock',
        'destination_port_end': 'DestinationPortEnd',
        'destination_port_start': 'DestinationPortStart',
        'match_dscp': 'MatchDscp',
        'priority': 'Priority',
        'protocol': 'Protocol',
        'remarking_dscp': 'RemarkingDscp',
        'source_cidr_block': 'SourceCidrBlock',
        'source_port_end': 'SourcePortEnd',
        'source_port_start': 'SourcePortStart',
        'status': 'Status',
        'transit_router_traffic_qos_marking_entry_id': 'TransitRouterTrafficQosMarkingEntryId',
        'transit_router_traffic_qos_marking_entry_name': 'TransitRouterTrafficQosMarkingEntryName',
        'transit_router_traffic_qos_marking_policy_id': 'TransitRouterTrafficQosMarkingPolicyId',
        'update_time': 'UpdateTime'
    }

    def __init__(self, creation_time=None, description=None, destination_cidr_block=None, destination_port_end=None, destination_port_start=None, match_dscp=None, priority=None, protocol=None, remarking_dscp=None, source_cidr_block=None, source_port_end=None, source_port_start=None, status=None, transit_router_traffic_qos_marking_entry_id=None, transit_router_traffic_qos_marking_entry_name=None, transit_router_traffic_qos_marking_policy_id=None, update_time=None, _configuration=None):  # noqa: E501
        """TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._creation_time = None
        self._description = None
        self._destination_cidr_block = None
        self._destination_port_end = None
        self._destination_port_start = None
        self._match_dscp = None
        self._priority = None
        self._protocol = None
        self._remarking_dscp = None
        self._source_cidr_block = None
        self._source_port_end = None
        self._source_port_start = None
        self._status = None
        self._transit_router_traffic_qos_marking_entry_id = None
        self._transit_router_traffic_qos_marking_entry_name = None
        self._transit_router_traffic_qos_marking_policy_id = None
        self._update_time = None
        self.discriminator = None

        if creation_time is not None:
            self.creation_time = creation_time
        if description is not None:
            self.description = description
        if destination_cidr_block is not None:
            self.destination_cidr_block = destination_cidr_block
        if destination_port_end is not None:
            self.destination_port_end = destination_port_end
        if destination_port_start is not None:
            self.destination_port_start = destination_port_start
        if match_dscp is not None:
            self.match_dscp = match_dscp
        if priority is not None:
            self.priority = priority
        if protocol is not None:
            self.protocol = protocol
        if remarking_dscp is not None:
            self.remarking_dscp = remarking_dscp
        if source_cidr_block is not None:
            self.source_cidr_block = source_cidr_block
        if source_port_end is not None:
            self.source_port_end = source_port_end
        if source_port_start is not None:
            self.source_port_start = source_port_start
        if status is not None:
            self.status = status
        if transit_router_traffic_qos_marking_entry_id is not None:
            self.transit_router_traffic_qos_marking_entry_id = transit_router_traffic_qos_marking_entry_id
        if transit_router_traffic_qos_marking_entry_name is not None:
            self.transit_router_traffic_qos_marking_entry_name = transit_router_traffic_qos_marking_entry_name
        if transit_router_traffic_qos_marking_policy_id is not None:
            self.transit_router_traffic_qos_marking_policy_id = transit_router_traffic_qos_marking_policy_id
        if update_time is not None:
            self.update_time = update_time

    @property
    def creation_time(self):
        """Gets the creation_time of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.  # noqa: E501


        :return: The creation_time of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.  # noqa: E501
        :rtype: str
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.


        :param creation_time: The creation_time of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.  # noqa: E501
        :type: str
        """

        self._creation_time = creation_time

    @property
    def description(self):
        """Gets the description of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.  # noqa: E501


        :return: The description of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.


        :param description: The description of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def destination_cidr_block(self):
        """Gets the destination_cidr_block of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.  # noqa: E501


        :return: The destination_cidr_block of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.  # noqa: E501
        :rtype: str
        """
        return self._destination_cidr_block

    @destination_cidr_block.setter
    def destination_cidr_block(self, destination_cidr_block):
        """Sets the destination_cidr_block of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.


        :param destination_cidr_block: The destination_cidr_block of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.  # noqa: E501
        :type: str
        """

        self._destination_cidr_block = destination_cidr_block

    @property
    def destination_port_end(self):
        """Gets the destination_port_end of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.  # noqa: E501


        :return: The destination_port_end of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.  # noqa: E501
        :rtype: int
        """
        return self._destination_port_end

    @destination_port_end.setter
    def destination_port_end(self, destination_port_end):
        """Sets the destination_port_end of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.


        :param destination_port_end: The destination_port_end of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.  # noqa: E501
        :type: int
        """

        self._destination_port_end = destination_port_end

    @property
    def destination_port_start(self):
        """Gets the destination_port_start of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.  # noqa: E501


        :return: The destination_port_start of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.  # noqa: E501
        :rtype: int
        """
        return self._destination_port_start

    @destination_port_start.setter
    def destination_port_start(self, destination_port_start):
        """Sets the destination_port_start of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.


        :param destination_port_start: The destination_port_start of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.  # noqa: E501
        :type: int
        """

        self._destination_port_start = destination_port_start

    @property
    def match_dscp(self):
        """Gets the match_dscp of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.  # noqa: E501


        :return: The match_dscp of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.  # noqa: E501
        :rtype: int
        """
        return self._match_dscp

    @match_dscp.setter
    def match_dscp(self, match_dscp):
        """Sets the match_dscp of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.


        :param match_dscp: The match_dscp of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.  # noqa: E501
        :type: int
        """

        self._match_dscp = match_dscp

    @property
    def priority(self):
        """Gets the priority of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.  # noqa: E501


        :return: The priority of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.


        :param priority: The priority of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.  # noqa: E501
        :type: int
        """

        self._priority = priority

    @property
    def protocol(self):
        """Gets the protocol of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.  # noqa: E501


        :return: The protocol of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.


        :param protocol: The protocol of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.  # noqa: E501
        :type: str
        """

        self._protocol = protocol

    @property
    def remarking_dscp(self):
        """Gets the remarking_dscp of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.  # noqa: E501


        :return: The remarking_dscp of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.  # noqa: E501
        :rtype: int
        """
        return self._remarking_dscp

    @remarking_dscp.setter
    def remarking_dscp(self, remarking_dscp):
        """Sets the remarking_dscp of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.


        :param remarking_dscp: The remarking_dscp of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.  # noqa: E501
        :type: int
        """

        self._remarking_dscp = remarking_dscp

    @property
    def source_cidr_block(self):
        """Gets the source_cidr_block of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.  # noqa: E501


        :return: The source_cidr_block of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.  # noqa: E501
        :rtype: str
        """
        return self._source_cidr_block

    @source_cidr_block.setter
    def source_cidr_block(self, source_cidr_block):
        """Sets the source_cidr_block of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.


        :param source_cidr_block: The source_cidr_block of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.  # noqa: E501
        :type: str
        """

        self._source_cidr_block = source_cidr_block

    @property
    def source_port_end(self):
        """Gets the source_port_end of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.  # noqa: E501


        :return: The source_port_end of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.  # noqa: E501
        :rtype: int
        """
        return self._source_port_end

    @source_port_end.setter
    def source_port_end(self, source_port_end):
        """Sets the source_port_end of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.


        :param source_port_end: The source_port_end of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.  # noqa: E501
        :type: int
        """

        self._source_port_end = source_port_end

    @property
    def source_port_start(self):
        """Gets the source_port_start of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.  # noqa: E501


        :return: The source_port_start of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.  # noqa: E501
        :rtype: int
        """
        return self._source_port_start

    @source_port_start.setter
    def source_port_start(self, source_port_start):
        """Sets the source_port_start of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.


        :param source_port_start: The source_port_start of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.  # noqa: E501
        :type: int
        """

        self._source_port_start = source_port_start

    @property
    def status(self):
        """Gets the status of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.  # noqa: E501


        :return: The status of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.


        :param status: The status of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def transit_router_traffic_qos_marking_entry_id(self):
        """Gets the transit_router_traffic_qos_marking_entry_id of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.  # noqa: E501


        :return: The transit_router_traffic_qos_marking_entry_id of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.  # noqa: E501
        :rtype: str
        """
        return self._transit_router_traffic_qos_marking_entry_id

    @transit_router_traffic_qos_marking_entry_id.setter
    def transit_router_traffic_qos_marking_entry_id(self, transit_router_traffic_qos_marking_entry_id):
        """Sets the transit_router_traffic_qos_marking_entry_id of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.


        :param transit_router_traffic_qos_marking_entry_id: The transit_router_traffic_qos_marking_entry_id of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.  # noqa: E501
        :type: str
        """

        self._transit_router_traffic_qos_marking_entry_id = transit_router_traffic_qos_marking_entry_id

    @property
    def transit_router_traffic_qos_marking_entry_name(self):
        """Gets the transit_router_traffic_qos_marking_entry_name of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.  # noqa: E501


        :return: The transit_router_traffic_qos_marking_entry_name of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.  # noqa: E501
        :rtype: str
        """
        return self._transit_router_traffic_qos_marking_entry_name

    @transit_router_traffic_qos_marking_entry_name.setter
    def transit_router_traffic_qos_marking_entry_name(self, transit_router_traffic_qos_marking_entry_name):
        """Sets the transit_router_traffic_qos_marking_entry_name of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.


        :param transit_router_traffic_qos_marking_entry_name: The transit_router_traffic_qos_marking_entry_name of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.  # noqa: E501
        :type: str
        """

        self._transit_router_traffic_qos_marking_entry_name = transit_router_traffic_qos_marking_entry_name

    @property
    def transit_router_traffic_qos_marking_policy_id(self):
        """Gets the transit_router_traffic_qos_marking_policy_id of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.  # noqa: E501


        :return: The transit_router_traffic_qos_marking_policy_id of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.  # noqa: E501
        :rtype: str
        """
        return self._transit_router_traffic_qos_marking_policy_id

    @transit_router_traffic_qos_marking_policy_id.setter
    def transit_router_traffic_qos_marking_policy_id(self, transit_router_traffic_qos_marking_policy_id):
        """Sets the transit_router_traffic_qos_marking_policy_id of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.


        :param transit_router_traffic_qos_marking_policy_id: The transit_router_traffic_qos_marking_policy_id of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.  # noqa: E501
        :type: str
        """

        self._transit_router_traffic_qos_marking_policy_id = transit_router_traffic_qos_marking_policy_id

    @property
    def update_time(self):
        """Gets the update_time of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.  # noqa: E501


        :return: The update_time of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.  # noqa: E501
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.


        :param update_time: The update_time of this TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput.  # noqa: E501
        :type: str
        """

        self._update_time = update_time

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
        if issubclass(TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput, dict):
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
        if not isinstance(other, TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransitRouterTrafficQosMarkingEntryForDescribeTransitRouterTrafficQosMarkingEntriesOutput):
            return True

        return self.to_dict() != other.to_dict()
