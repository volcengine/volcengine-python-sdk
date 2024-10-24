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


class TransitRouterTrafficQosQueuePolicyForDescribeTransitRouterTrafficQosQueuePoliciesOutput(object):
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
        'status': 'str',
        'transit_router_traffic_qos_queue_policy_id': 'str',
        'transit_router_traffic_qos_queue_policy_name': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'creation_time': 'CreationTime',
        'description': 'Description',
        'status': 'Status',
        'transit_router_traffic_qos_queue_policy_id': 'TransitRouterTrafficQosQueuePolicyId',
        'transit_router_traffic_qos_queue_policy_name': 'TransitRouterTrafficQosQueuePolicyName',
        'update_time': 'UpdateTime'
    }

    def __init__(self, creation_time=None, description=None, status=None, transit_router_traffic_qos_queue_policy_id=None, transit_router_traffic_qos_queue_policy_name=None, update_time=None, _configuration=None):  # noqa: E501
        """TransitRouterTrafficQosQueuePolicyForDescribeTransitRouterTrafficQosQueuePoliciesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._creation_time = None
        self._description = None
        self._status = None
        self._transit_router_traffic_qos_queue_policy_id = None
        self._transit_router_traffic_qos_queue_policy_name = None
        self._update_time = None
        self.discriminator = None

        if creation_time is not None:
            self.creation_time = creation_time
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if transit_router_traffic_qos_queue_policy_id is not None:
            self.transit_router_traffic_qos_queue_policy_id = transit_router_traffic_qos_queue_policy_id
        if transit_router_traffic_qos_queue_policy_name is not None:
            self.transit_router_traffic_qos_queue_policy_name = transit_router_traffic_qos_queue_policy_name
        if update_time is not None:
            self.update_time = update_time

    @property
    def creation_time(self):
        """Gets the creation_time of this TransitRouterTrafficQosQueuePolicyForDescribeTransitRouterTrafficQosQueuePoliciesOutput.  # noqa: E501


        :return: The creation_time of this TransitRouterTrafficQosQueuePolicyForDescribeTransitRouterTrafficQosQueuePoliciesOutput.  # noqa: E501
        :rtype: str
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this TransitRouterTrafficQosQueuePolicyForDescribeTransitRouterTrafficQosQueuePoliciesOutput.


        :param creation_time: The creation_time of this TransitRouterTrafficQosQueuePolicyForDescribeTransitRouterTrafficQosQueuePoliciesOutput.  # noqa: E501
        :type: str
        """

        self._creation_time = creation_time

    @property
    def description(self):
        """Gets the description of this TransitRouterTrafficQosQueuePolicyForDescribeTransitRouterTrafficQosQueuePoliciesOutput.  # noqa: E501


        :return: The description of this TransitRouterTrafficQosQueuePolicyForDescribeTransitRouterTrafficQosQueuePoliciesOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TransitRouterTrafficQosQueuePolicyForDescribeTransitRouterTrafficQosQueuePoliciesOutput.


        :param description: The description of this TransitRouterTrafficQosQueuePolicyForDescribeTransitRouterTrafficQosQueuePoliciesOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def status(self):
        """Gets the status of this TransitRouterTrafficQosQueuePolicyForDescribeTransitRouterTrafficQosQueuePoliciesOutput.  # noqa: E501


        :return: The status of this TransitRouterTrafficQosQueuePolicyForDescribeTransitRouterTrafficQosQueuePoliciesOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TransitRouterTrafficQosQueuePolicyForDescribeTransitRouterTrafficQosQueuePoliciesOutput.


        :param status: The status of this TransitRouterTrafficQosQueuePolicyForDescribeTransitRouterTrafficQosQueuePoliciesOutput.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def transit_router_traffic_qos_queue_policy_id(self):
        """Gets the transit_router_traffic_qos_queue_policy_id of this TransitRouterTrafficQosQueuePolicyForDescribeTransitRouterTrafficQosQueuePoliciesOutput.  # noqa: E501


        :return: The transit_router_traffic_qos_queue_policy_id of this TransitRouterTrafficQosQueuePolicyForDescribeTransitRouterTrafficQosQueuePoliciesOutput.  # noqa: E501
        :rtype: str
        """
        return self._transit_router_traffic_qos_queue_policy_id

    @transit_router_traffic_qos_queue_policy_id.setter
    def transit_router_traffic_qos_queue_policy_id(self, transit_router_traffic_qos_queue_policy_id):
        """Sets the transit_router_traffic_qos_queue_policy_id of this TransitRouterTrafficQosQueuePolicyForDescribeTransitRouterTrafficQosQueuePoliciesOutput.


        :param transit_router_traffic_qos_queue_policy_id: The transit_router_traffic_qos_queue_policy_id of this TransitRouterTrafficQosQueuePolicyForDescribeTransitRouterTrafficQosQueuePoliciesOutput.  # noqa: E501
        :type: str
        """

        self._transit_router_traffic_qos_queue_policy_id = transit_router_traffic_qos_queue_policy_id

    @property
    def transit_router_traffic_qos_queue_policy_name(self):
        """Gets the transit_router_traffic_qos_queue_policy_name of this TransitRouterTrafficQosQueuePolicyForDescribeTransitRouterTrafficQosQueuePoliciesOutput.  # noqa: E501


        :return: The transit_router_traffic_qos_queue_policy_name of this TransitRouterTrafficQosQueuePolicyForDescribeTransitRouterTrafficQosQueuePoliciesOutput.  # noqa: E501
        :rtype: str
        """
        return self._transit_router_traffic_qos_queue_policy_name

    @transit_router_traffic_qos_queue_policy_name.setter
    def transit_router_traffic_qos_queue_policy_name(self, transit_router_traffic_qos_queue_policy_name):
        """Sets the transit_router_traffic_qos_queue_policy_name of this TransitRouterTrafficQosQueuePolicyForDescribeTransitRouterTrafficQosQueuePoliciesOutput.


        :param transit_router_traffic_qos_queue_policy_name: The transit_router_traffic_qos_queue_policy_name of this TransitRouterTrafficQosQueuePolicyForDescribeTransitRouterTrafficQosQueuePoliciesOutput.  # noqa: E501
        :type: str
        """

        self._transit_router_traffic_qos_queue_policy_name = transit_router_traffic_qos_queue_policy_name

    @property
    def update_time(self):
        """Gets the update_time of this TransitRouterTrafficQosQueuePolicyForDescribeTransitRouterTrafficQosQueuePoliciesOutput.  # noqa: E501


        :return: The update_time of this TransitRouterTrafficQosQueuePolicyForDescribeTransitRouterTrafficQosQueuePoliciesOutput.  # noqa: E501
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this TransitRouterTrafficQosQueuePolicyForDescribeTransitRouterTrafficQosQueuePoliciesOutput.


        :param update_time: The update_time of this TransitRouterTrafficQosQueuePolicyForDescribeTransitRouterTrafficQosQueuePoliciesOutput.  # noqa: E501
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
        if issubclass(TransitRouterTrafficQosQueuePolicyForDescribeTransitRouterTrafficQosQueuePoliciesOutput, dict):
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
        if not isinstance(other, TransitRouterTrafficQosQueuePolicyForDescribeTransitRouterTrafficQosQueuePoliciesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransitRouterTrafficQosQueuePolicyForDescribeTransitRouterTrafficQosQueuePoliciesOutput):
            return True

        return self.to_dict() != other.to_dict()
