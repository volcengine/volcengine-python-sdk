# coding: utf-8

"""
    ecs

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeDedicatedHostsRequest(object):
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
        'dedicated_host_cluster_id': 'str',
        'dedicated_host_ids': 'list[str]',
        'dedicated_host_name': 'str',
        'dedicated_host_type_id': 'str',
        'max_results': 'int',
        'next_token': 'str',
        'status': 'str',
        'zone_id': 'str'
    }

    attribute_map = {
        'dedicated_host_cluster_id': 'DedicatedHostClusterId',
        'dedicated_host_ids': 'DedicatedHostIds',
        'dedicated_host_name': 'DedicatedHostName',
        'dedicated_host_type_id': 'DedicatedHostTypeId',
        'max_results': 'MaxResults',
        'next_token': 'NextToken',
        'status': 'Status',
        'zone_id': 'ZoneId'
    }

    def __init__(self, dedicated_host_cluster_id=None, dedicated_host_ids=None, dedicated_host_name=None, dedicated_host_type_id=None, max_results=None, next_token=None, status=None, zone_id=None, _configuration=None):  # noqa: E501
        """DescribeDedicatedHostsRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._dedicated_host_cluster_id = None
        self._dedicated_host_ids = None
        self._dedicated_host_name = None
        self._dedicated_host_type_id = None
        self._max_results = None
        self._next_token = None
        self._status = None
        self._zone_id = None
        self.discriminator = None

        if dedicated_host_cluster_id is not None:
            self.dedicated_host_cluster_id = dedicated_host_cluster_id
        if dedicated_host_ids is not None:
            self.dedicated_host_ids = dedicated_host_ids
        if dedicated_host_name is not None:
            self.dedicated_host_name = dedicated_host_name
        if dedicated_host_type_id is not None:
            self.dedicated_host_type_id = dedicated_host_type_id
        if max_results is not None:
            self.max_results = max_results
        if next_token is not None:
            self.next_token = next_token
        if status is not None:
            self.status = status
        if zone_id is not None:
            self.zone_id = zone_id

    @property
    def dedicated_host_cluster_id(self):
        """Gets the dedicated_host_cluster_id of this DescribeDedicatedHostsRequest.  # noqa: E501


        :return: The dedicated_host_cluster_id of this DescribeDedicatedHostsRequest.  # noqa: E501
        :rtype: str
        """
        return self._dedicated_host_cluster_id

    @dedicated_host_cluster_id.setter
    def dedicated_host_cluster_id(self, dedicated_host_cluster_id):
        """Sets the dedicated_host_cluster_id of this DescribeDedicatedHostsRequest.


        :param dedicated_host_cluster_id: The dedicated_host_cluster_id of this DescribeDedicatedHostsRequest.  # noqa: E501
        :type: str
        """

        self._dedicated_host_cluster_id = dedicated_host_cluster_id

    @property
    def dedicated_host_ids(self):
        """Gets the dedicated_host_ids of this DescribeDedicatedHostsRequest.  # noqa: E501


        :return: The dedicated_host_ids of this DescribeDedicatedHostsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._dedicated_host_ids

    @dedicated_host_ids.setter
    def dedicated_host_ids(self, dedicated_host_ids):
        """Sets the dedicated_host_ids of this DescribeDedicatedHostsRequest.


        :param dedicated_host_ids: The dedicated_host_ids of this DescribeDedicatedHostsRequest.  # noqa: E501
        :type: list[str]
        """

        self._dedicated_host_ids = dedicated_host_ids

    @property
    def dedicated_host_name(self):
        """Gets the dedicated_host_name of this DescribeDedicatedHostsRequest.  # noqa: E501


        :return: The dedicated_host_name of this DescribeDedicatedHostsRequest.  # noqa: E501
        :rtype: str
        """
        return self._dedicated_host_name

    @dedicated_host_name.setter
    def dedicated_host_name(self, dedicated_host_name):
        """Sets the dedicated_host_name of this DescribeDedicatedHostsRequest.


        :param dedicated_host_name: The dedicated_host_name of this DescribeDedicatedHostsRequest.  # noqa: E501
        :type: str
        """

        self._dedicated_host_name = dedicated_host_name

    @property
    def dedicated_host_type_id(self):
        """Gets the dedicated_host_type_id of this DescribeDedicatedHostsRequest.  # noqa: E501


        :return: The dedicated_host_type_id of this DescribeDedicatedHostsRequest.  # noqa: E501
        :rtype: str
        """
        return self._dedicated_host_type_id

    @dedicated_host_type_id.setter
    def dedicated_host_type_id(self, dedicated_host_type_id):
        """Sets the dedicated_host_type_id of this DescribeDedicatedHostsRequest.


        :param dedicated_host_type_id: The dedicated_host_type_id of this DescribeDedicatedHostsRequest.  # noqa: E501
        :type: str
        """

        self._dedicated_host_type_id = dedicated_host_type_id

    @property
    def max_results(self):
        """Gets the max_results of this DescribeDedicatedHostsRequest.  # noqa: E501


        :return: The max_results of this DescribeDedicatedHostsRequest.  # noqa: E501
        :rtype: int
        """
        return self._max_results

    @max_results.setter
    def max_results(self, max_results):
        """Sets the max_results of this DescribeDedicatedHostsRequest.


        :param max_results: The max_results of this DescribeDedicatedHostsRequest.  # noqa: E501
        :type: int
        """

        self._max_results = max_results

    @property
    def next_token(self):
        """Gets the next_token of this DescribeDedicatedHostsRequest.  # noqa: E501


        :return: The next_token of this DescribeDedicatedHostsRequest.  # noqa: E501
        :rtype: str
        """
        return self._next_token

    @next_token.setter
    def next_token(self, next_token):
        """Sets the next_token of this DescribeDedicatedHostsRequest.


        :param next_token: The next_token of this DescribeDedicatedHostsRequest.  # noqa: E501
        :type: str
        """

        self._next_token = next_token

    @property
    def status(self):
        """Gets the status of this DescribeDedicatedHostsRequest.  # noqa: E501


        :return: The status of this DescribeDedicatedHostsRequest.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DescribeDedicatedHostsRequest.


        :param status: The status of this DescribeDedicatedHostsRequest.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def zone_id(self):
        """Gets the zone_id of this DescribeDedicatedHostsRequest.  # noqa: E501


        :return: The zone_id of this DescribeDedicatedHostsRequest.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this DescribeDedicatedHostsRequest.


        :param zone_id: The zone_id of this DescribeDedicatedHostsRequest.  # noqa: E501
        :type: str
        """

        self._zone_id = zone_id

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
        if issubclass(DescribeDedicatedHostsRequest, dict):
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
        if not isinstance(other, DescribeDedicatedHostsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeDedicatedHostsRequest):
            return True

        return self.to_dict() != other.to_dict()