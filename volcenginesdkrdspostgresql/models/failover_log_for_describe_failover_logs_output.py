# coding: utf-8

"""
    rds_postgresql

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class FailoverLogForDescribeFailoverLogsOutput(object):
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
        'failover_time': 'str',
        'failover_type': 'str',
        'new_master_node_id': 'str',
        'old_master_node_id': 'str'
    }

    attribute_map = {
        'failover_time': 'FailoverTime',
        'failover_type': 'FailoverType',
        'new_master_node_id': 'NewMasterNodeId',
        'old_master_node_id': 'OldMasterNodeId'
    }

    def __init__(self, failover_time=None, failover_type=None, new_master_node_id=None, old_master_node_id=None, _configuration=None):  # noqa: E501
        """FailoverLogForDescribeFailoverLogsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._failover_time = None
        self._failover_type = None
        self._new_master_node_id = None
        self._old_master_node_id = None
        self.discriminator = None

        if failover_time is not None:
            self.failover_time = failover_time
        if failover_type is not None:
            self.failover_type = failover_type
        if new_master_node_id is not None:
            self.new_master_node_id = new_master_node_id
        if old_master_node_id is not None:
            self.old_master_node_id = old_master_node_id

    @property
    def failover_time(self):
        """Gets the failover_time of this FailoverLogForDescribeFailoverLogsOutput.  # noqa: E501


        :return: The failover_time of this FailoverLogForDescribeFailoverLogsOutput.  # noqa: E501
        :rtype: str
        """
        return self._failover_time

    @failover_time.setter
    def failover_time(self, failover_time):
        """Sets the failover_time of this FailoverLogForDescribeFailoverLogsOutput.


        :param failover_time: The failover_time of this FailoverLogForDescribeFailoverLogsOutput.  # noqa: E501
        :type: str
        """

        self._failover_time = failover_time

    @property
    def failover_type(self):
        """Gets the failover_type of this FailoverLogForDescribeFailoverLogsOutput.  # noqa: E501


        :return: The failover_type of this FailoverLogForDescribeFailoverLogsOutput.  # noqa: E501
        :rtype: str
        """
        return self._failover_type

    @failover_type.setter
    def failover_type(self, failover_type):
        """Sets the failover_type of this FailoverLogForDescribeFailoverLogsOutput.


        :param failover_type: The failover_type of this FailoverLogForDescribeFailoverLogsOutput.  # noqa: E501
        :type: str
        """

        self._failover_type = failover_type

    @property
    def new_master_node_id(self):
        """Gets the new_master_node_id of this FailoverLogForDescribeFailoverLogsOutput.  # noqa: E501


        :return: The new_master_node_id of this FailoverLogForDescribeFailoverLogsOutput.  # noqa: E501
        :rtype: str
        """
        return self._new_master_node_id

    @new_master_node_id.setter
    def new_master_node_id(self, new_master_node_id):
        """Sets the new_master_node_id of this FailoverLogForDescribeFailoverLogsOutput.


        :param new_master_node_id: The new_master_node_id of this FailoverLogForDescribeFailoverLogsOutput.  # noqa: E501
        :type: str
        """

        self._new_master_node_id = new_master_node_id

    @property
    def old_master_node_id(self):
        """Gets the old_master_node_id of this FailoverLogForDescribeFailoverLogsOutput.  # noqa: E501


        :return: The old_master_node_id of this FailoverLogForDescribeFailoverLogsOutput.  # noqa: E501
        :rtype: str
        """
        return self._old_master_node_id

    @old_master_node_id.setter
    def old_master_node_id(self, old_master_node_id):
        """Sets the old_master_node_id of this FailoverLogForDescribeFailoverLogsOutput.


        :param old_master_node_id: The old_master_node_id of this FailoverLogForDescribeFailoverLogsOutput.  # noqa: E501
        :type: str
        """

        self._old_master_node_id = old_master_node_id

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
        if issubclass(FailoverLogForDescribeFailoverLogsOutput, dict):
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
        if not isinstance(other, FailoverLogForDescribeFailoverLogsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FailoverLogForDescribeFailoverLogsOutput):
            return True

        return self.to_dict() != other.to_dict()
