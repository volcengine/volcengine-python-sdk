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


class TransitRouterRoutePolicyTableForDescribeTransitRouterRoutePolicyTablesOutput(object):
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
        'direction': 'str',
        'status': 'str',
        'transit_router_id': 'str',
        'transit_router_route_policy_table_id': 'str',
        'transit_router_route_policy_table_name': 'str',
        'transit_router_route_table_ids': 'list[str]',
        'update_time': 'str'
    }

    attribute_map = {
        'creation_time': 'CreationTime',
        'description': 'Description',
        'direction': 'Direction',
        'status': 'Status',
        'transit_router_id': 'TransitRouterId',
        'transit_router_route_policy_table_id': 'TransitRouterRoutePolicyTableId',
        'transit_router_route_policy_table_name': 'TransitRouterRoutePolicyTableName',
        'transit_router_route_table_ids': 'TransitRouterRouteTableIds',
        'update_time': 'UpdateTime'
    }

    def __init__(self, creation_time=None, description=None, direction=None, status=None, transit_router_id=None, transit_router_route_policy_table_id=None, transit_router_route_policy_table_name=None, transit_router_route_table_ids=None, update_time=None, _configuration=None):  # noqa: E501
        """TransitRouterRoutePolicyTableForDescribeTransitRouterRoutePolicyTablesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._creation_time = None
        self._description = None
        self._direction = None
        self._status = None
        self._transit_router_id = None
        self._transit_router_route_policy_table_id = None
        self._transit_router_route_policy_table_name = None
        self._transit_router_route_table_ids = None
        self._update_time = None
        self.discriminator = None

        if creation_time is not None:
            self.creation_time = creation_time
        if description is not None:
            self.description = description
        if direction is not None:
            self.direction = direction
        if status is not None:
            self.status = status
        if transit_router_id is not None:
            self.transit_router_id = transit_router_id
        if transit_router_route_policy_table_id is not None:
            self.transit_router_route_policy_table_id = transit_router_route_policy_table_id
        if transit_router_route_policy_table_name is not None:
            self.transit_router_route_policy_table_name = transit_router_route_policy_table_name
        if transit_router_route_table_ids is not None:
            self.transit_router_route_table_ids = transit_router_route_table_ids
        if update_time is not None:
            self.update_time = update_time

    @property
    def creation_time(self):
        """Gets the creation_time of this TransitRouterRoutePolicyTableForDescribeTransitRouterRoutePolicyTablesOutput.  # noqa: E501


        :return: The creation_time of this TransitRouterRoutePolicyTableForDescribeTransitRouterRoutePolicyTablesOutput.  # noqa: E501
        :rtype: str
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this TransitRouterRoutePolicyTableForDescribeTransitRouterRoutePolicyTablesOutput.


        :param creation_time: The creation_time of this TransitRouterRoutePolicyTableForDescribeTransitRouterRoutePolicyTablesOutput.  # noqa: E501
        :type: str
        """

        self._creation_time = creation_time

    @property
    def description(self):
        """Gets the description of this TransitRouterRoutePolicyTableForDescribeTransitRouterRoutePolicyTablesOutput.  # noqa: E501


        :return: The description of this TransitRouterRoutePolicyTableForDescribeTransitRouterRoutePolicyTablesOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TransitRouterRoutePolicyTableForDescribeTransitRouterRoutePolicyTablesOutput.


        :param description: The description of this TransitRouterRoutePolicyTableForDescribeTransitRouterRoutePolicyTablesOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def direction(self):
        """Gets the direction of this TransitRouterRoutePolicyTableForDescribeTransitRouterRoutePolicyTablesOutput.  # noqa: E501


        :return: The direction of this TransitRouterRoutePolicyTableForDescribeTransitRouterRoutePolicyTablesOutput.  # noqa: E501
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this TransitRouterRoutePolicyTableForDescribeTransitRouterRoutePolicyTablesOutput.


        :param direction: The direction of this TransitRouterRoutePolicyTableForDescribeTransitRouterRoutePolicyTablesOutput.  # noqa: E501
        :type: str
        """

        self._direction = direction

    @property
    def status(self):
        """Gets the status of this TransitRouterRoutePolicyTableForDescribeTransitRouterRoutePolicyTablesOutput.  # noqa: E501


        :return: The status of this TransitRouterRoutePolicyTableForDescribeTransitRouterRoutePolicyTablesOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TransitRouterRoutePolicyTableForDescribeTransitRouterRoutePolicyTablesOutput.


        :param status: The status of this TransitRouterRoutePolicyTableForDescribeTransitRouterRoutePolicyTablesOutput.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def transit_router_id(self):
        """Gets the transit_router_id of this TransitRouterRoutePolicyTableForDescribeTransitRouterRoutePolicyTablesOutput.  # noqa: E501


        :return: The transit_router_id of this TransitRouterRoutePolicyTableForDescribeTransitRouterRoutePolicyTablesOutput.  # noqa: E501
        :rtype: str
        """
        return self._transit_router_id

    @transit_router_id.setter
    def transit_router_id(self, transit_router_id):
        """Sets the transit_router_id of this TransitRouterRoutePolicyTableForDescribeTransitRouterRoutePolicyTablesOutput.


        :param transit_router_id: The transit_router_id of this TransitRouterRoutePolicyTableForDescribeTransitRouterRoutePolicyTablesOutput.  # noqa: E501
        :type: str
        """

        self._transit_router_id = transit_router_id

    @property
    def transit_router_route_policy_table_id(self):
        """Gets the transit_router_route_policy_table_id of this TransitRouterRoutePolicyTableForDescribeTransitRouterRoutePolicyTablesOutput.  # noqa: E501


        :return: The transit_router_route_policy_table_id of this TransitRouterRoutePolicyTableForDescribeTransitRouterRoutePolicyTablesOutput.  # noqa: E501
        :rtype: str
        """
        return self._transit_router_route_policy_table_id

    @transit_router_route_policy_table_id.setter
    def transit_router_route_policy_table_id(self, transit_router_route_policy_table_id):
        """Sets the transit_router_route_policy_table_id of this TransitRouterRoutePolicyTableForDescribeTransitRouterRoutePolicyTablesOutput.


        :param transit_router_route_policy_table_id: The transit_router_route_policy_table_id of this TransitRouterRoutePolicyTableForDescribeTransitRouterRoutePolicyTablesOutput.  # noqa: E501
        :type: str
        """

        self._transit_router_route_policy_table_id = transit_router_route_policy_table_id

    @property
    def transit_router_route_policy_table_name(self):
        """Gets the transit_router_route_policy_table_name of this TransitRouterRoutePolicyTableForDescribeTransitRouterRoutePolicyTablesOutput.  # noqa: E501


        :return: The transit_router_route_policy_table_name of this TransitRouterRoutePolicyTableForDescribeTransitRouterRoutePolicyTablesOutput.  # noqa: E501
        :rtype: str
        """
        return self._transit_router_route_policy_table_name

    @transit_router_route_policy_table_name.setter
    def transit_router_route_policy_table_name(self, transit_router_route_policy_table_name):
        """Sets the transit_router_route_policy_table_name of this TransitRouterRoutePolicyTableForDescribeTransitRouterRoutePolicyTablesOutput.


        :param transit_router_route_policy_table_name: The transit_router_route_policy_table_name of this TransitRouterRoutePolicyTableForDescribeTransitRouterRoutePolicyTablesOutput.  # noqa: E501
        :type: str
        """

        self._transit_router_route_policy_table_name = transit_router_route_policy_table_name

    @property
    def transit_router_route_table_ids(self):
        """Gets the transit_router_route_table_ids of this TransitRouterRoutePolicyTableForDescribeTransitRouterRoutePolicyTablesOutput.  # noqa: E501


        :return: The transit_router_route_table_ids of this TransitRouterRoutePolicyTableForDescribeTransitRouterRoutePolicyTablesOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._transit_router_route_table_ids

    @transit_router_route_table_ids.setter
    def transit_router_route_table_ids(self, transit_router_route_table_ids):
        """Sets the transit_router_route_table_ids of this TransitRouterRoutePolicyTableForDescribeTransitRouterRoutePolicyTablesOutput.


        :param transit_router_route_table_ids: The transit_router_route_table_ids of this TransitRouterRoutePolicyTableForDescribeTransitRouterRoutePolicyTablesOutput.  # noqa: E501
        :type: list[str]
        """

        self._transit_router_route_table_ids = transit_router_route_table_ids

    @property
    def update_time(self):
        """Gets the update_time of this TransitRouterRoutePolicyTableForDescribeTransitRouterRoutePolicyTablesOutput.  # noqa: E501


        :return: The update_time of this TransitRouterRoutePolicyTableForDescribeTransitRouterRoutePolicyTablesOutput.  # noqa: E501
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this TransitRouterRoutePolicyTableForDescribeTransitRouterRoutePolicyTablesOutput.


        :param update_time: The update_time of this TransitRouterRoutePolicyTableForDescribeTransitRouterRoutePolicyTablesOutput.  # noqa: E501
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
        if issubclass(TransitRouterRoutePolicyTableForDescribeTransitRouterRoutePolicyTablesOutput, dict):
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
        if not isinstance(other, TransitRouterRoutePolicyTableForDescribeTransitRouterRoutePolicyTablesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransitRouterRoutePolicyTableForDescribeTransitRouterRoutePolicyTablesOutput):
            return True

        return self.to_dict() != other.to_dict()
