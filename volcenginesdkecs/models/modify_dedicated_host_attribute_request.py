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


class ModifyDedicatedHostAttributeRequest(object):
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
        'auto_placement': 'str',
        'client_token': 'str',
        'cpu_overcommit_ratio': 'float',
        'dedicated_host_cluster_id': 'str',
        'dedicated_host_id': 'str',
        'dedicated_host_name': 'str',
        'dedicated_host_recovery': 'str',
        'description': 'str'
    }

    attribute_map = {
        'auto_placement': 'AutoPlacement',
        'client_token': 'ClientToken',
        'cpu_overcommit_ratio': 'CpuOvercommitRatio',
        'dedicated_host_cluster_id': 'DedicatedHostClusterId',
        'dedicated_host_id': 'DedicatedHostId',
        'dedicated_host_name': 'DedicatedHostName',
        'dedicated_host_recovery': 'DedicatedHostRecovery',
        'description': 'Description'
    }

    def __init__(self, auto_placement=None, client_token=None, cpu_overcommit_ratio=None, dedicated_host_cluster_id=None, dedicated_host_id=None, dedicated_host_name=None, dedicated_host_recovery=None, description=None, _configuration=None):  # noqa: E501
        """ModifyDedicatedHostAttributeRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._auto_placement = None
        self._client_token = None
        self._cpu_overcommit_ratio = None
        self._dedicated_host_cluster_id = None
        self._dedicated_host_id = None
        self._dedicated_host_name = None
        self._dedicated_host_recovery = None
        self._description = None
        self.discriminator = None

        if auto_placement is not None:
            self.auto_placement = auto_placement
        if client_token is not None:
            self.client_token = client_token
        if cpu_overcommit_ratio is not None:
            self.cpu_overcommit_ratio = cpu_overcommit_ratio
        if dedicated_host_cluster_id is not None:
            self.dedicated_host_cluster_id = dedicated_host_cluster_id
        if dedicated_host_id is not None:
            self.dedicated_host_id = dedicated_host_id
        if dedicated_host_name is not None:
            self.dedicated_host_name = dedicated_host_name
        if dedicated_host_recovery is not None:
            self.dedicated_host_recovery = dedicated_host_recovery
        if description is not None:
            self.description = description

    @property
    def auto_placement(self):
        """Gets the auto_placement of this ModifyDedicatedHostAttributeRequest.  # noqa: E501


        :return: The auto_placement of this ModifyDedicatedHostAttributeRequest.  # noqa: E501
        :rtype: str
        """
        return self._auto_placement

    @auto_placement.setter
    def auto_placement(self, auto_placement):
        """Sets the auto_placement of this ModifyDedicatedHostAttributeRequest.


        :param auto_placement: The auto_placement of this ModifyDedicatedHostAttributeRequest.  # noqa: E501
        :type: str
        """

        self._auto_placement = auto_placement

    @property
    def client_token(self):
        """Gets the client_token of this ModifyDedicatedHostAttributeRequest.  # noqa: E501


        :return: The client_token of this ModifyDedicatedHostAttributeRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_token

    @client_token.setter
    def client_token(self, client_token):
        """Sets the client_token of this ModifyDedicatedHostAttributeRequest.


        :param client_token: The client_token of this ModifyDedicatedHostAttributeRequest.  # noqa: E501
        :type: str
        """

        self._client_token = client_token

    @property
    def cpu_overcommit_ratio(self):
        """Gets the cpu_overcommit_ratio of this ModifyDedicatedHostAttributeRequest.  # noqa: E501


        :return: The cpu_overcommit_ratio of this ModifyDedicatedHostAttributeRequest.  # noqa: E501
        :rtype: float
        """
        return self._cpu_overcommit_ratio

    @cpu_overcommit_ratio.setter
    def cpu_overcommit_ratio(self, cpu_overcommit_ratio):
        """Sets the cpu_overcommit_ratio of this ModifyDedicatedHostAttributeRequest.


        :param cpu_overcommit_ratio: The cpu_overcommit_ratio of this ModifyDedicatedHostAttributeRequest.  # noqa: E501
        :type: float
        """

        self._cpu_overcommit_ratio = cpu_overcommit_ratio

    @property
    def dedicated_host_cluster_id(self):
        """Gets the dedicated_host_cluster_id of this ModifyDedicatedHostAttributeRequest.  # noqa: E501


        :return: The dedicated_host_cluster_id of this ModifyDedicatedHostAttributeRequest.  # noqa: E501
        :rtype: str
        """
        return self._dedicated_host_cluster_id

    @dedicated_host_cluster_id.setter
    def dedicated_host_cluster_id(self, dedicated_host_cluster_id):
        """Sets the dedicated_host_cluster_id of this ModifyDedicatedHostAttributeRequest.


        :param dedicated_host_cluster_id: The dedicated_host_cluster_id of this ModifyDedicatedHostAttributeRequest.  # noqa: E501
        :type: str
        """

        self._dedicated_host_cluster_id = dedicated_host_cluster_id

    @property
    def dedicated_host_id(self):
        """Gets the dedicated_host_id of this ModifyDedicatedHostAttributeRequest.  # noqa: E501


        :return: The dedicated_host_id of this ModifyDedicatedHostAttributeRequest.  # noqa: E501
        :rtype: str
        """
        return self._dedicated_host_id

    @dedicated_host_id.setter
    def dedicated_host_id(self, dedicated_host_id):
        """Sets the dedicated_host_id of this ModifyDedicatedHostAttributeRequest.


        :param dedicated_host_id: The dedicated_host_id of this ModifyDedicatedHostAttributeRequest.  # noqa: E501
        :type: str
        """

        self._dedicated_host_id = dedicated_host_id

    @property
    def dedicated_host_name(self):
        """Gets the dedicated_host_name of this ModifyDedicatedHostAttributeRequest.  # noqa: E501


        :return: The dedicated_host_name of this ModifyDedicatedHostAttributeRequest.  # noqa: E501
        :rtype: str
        """
        return self._dedicated_host_name

    @dedicated_host_name.setter
    def dedicated_host_name(self, dedicated_host_name):
        """Sets the dedicated_host_name of this ModifyDedicatedHostAttributeRequest.


        :param dedicated_host_name: The dedicated_host_name of this ModifyDedicatedHostAttributeRequest.  # noqa: E501
        :type: str
        """

        self._dedicated_host_name = dedicated_host_name

    @property
    def dedicated_host_recovery(self):
        """Gets the dedicated_host_recovery of this ModifyDedicatedHostAttributeRequest.  # noqa: E501


        :return: The dedicated_host_recovery of this ModifyDedicatedHostAttributeRequest.  # noqa: E501
        :rtype: str
        """
        return self._dedicated_host_recovery

    @dedicated_host_recovery.setter
    def dedicated_host_recovery(self, dedicated_host_recovery):
        """Sets the dedicated_host_recovery of this ModifyDedicatedHostAttributeRequest.


        :param dedicated_host_recovery: The dedicated_host_recovery of this ModifyDedicatedHostAttributeRequest.  # noqa: E501
        :type: str
        """

        self._dedicated_host_recovery = dedicated_host_recovery

    @property
    def description(self):
        """Gets the description of this ModifyDedicatedHostAttributeRequest.  # noqa: E501


        :return: The description of this ModifyDedicatedHostAttributeRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ModifyDedicatedHostAttributeRequest.


        :param description: The description of this ModifyDedicatedHostAttributeRequest.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if issubclass(ModifyDedicatedHostAttributeRequest, dict):
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
        if not isinstance(other, ModifyDedicatedHostAttributeRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModifyDedicatedHostAttributeRequest):
            return True

        return self.to_dict() != other.to_dict()