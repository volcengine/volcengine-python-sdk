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


class ScheduledInstanceStockForDescribeScheduledInstanceStockOutput(object):
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
        'end_delivery_at': 'str',
        'release_status': 'str',
        'start_delivery_at': 'str',
        'status': 'str'
    }

    attribute_map = {
        'end_delivery_at': 'EndDeliveryAt',
        'release_status': 'ReleaseStatus',
        'start_delivery_at': 'StartDeliveryAt',
        'status': 'Status'
    }

    def __init__(self, end_delivery_at=None, release_status=None, start_delivery_at=None, status=None, _configuration=None):  # noqa: E501
        """ScheduledInstanceStockForDescribeScheduledInstanceStockOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._end_delivery_at = None
        self._release_status = None
        self._start_delivery_at = None
        self._status = None
        self.discriminator = None

        if end_delivery_at is not None:
            self.end_delivery_at = end_delivery_at
        if release_status is not None:
            self.release_status = release_status
        if start_delivery_at is not None:
            self.start_delivery_at = start_delivery_at
        if status is not None:
            self.status = status

    @property
    def end_delivery_at(self):
        """Gets the end_delivery_at of this ScheduledInstanceStockForDescribeScheduledInstanceStockOutput.  # noqa: E501


        :return: The end_delivery_at of this ScheduledInstanceStockForDescribeScheduledInstanceStockOutput.  # noqa: E501
        :rtype: str
        """
        return self._end_delivery_at

    @end_delivery_at.setter
    def end_delivery_at(self, end_delivery_at):
        """Sets the end_delivery_at of this ScheduledInstanceStockForDescribeScheduledInstanceStockOutput.


        :param end_delivery_at: The end_delivery_at of this ScheduledInstanceStockForDescribeScheduledInstanceStockOutput.  # noqa: E501
        :type: str
        """

        self._end_delivery_at = end_delivery_at

    @property
    def release_status(self):
        """Gets the release_status of this ScheduledInstanceStockForDescribeScheduledInstanceStockOutput.  # noqa: E501


        :return: The release_status of this ScheduledInstanceStockForDescribeScheduledInstanceStockOutput.  # noqa: E501
        :rtype: str
        """
        return self._release_status

    @release_status.setter
    def release_status(self, release_status):
        """Sets the release_status of this ScheduledInstanceStockForDescribeScheduledInstanceStockOutput.


        :param release_status: The release_status of this ScheduledInstanceStockForDescribeScheduledInstanceStockOutput.  # noqa: E501
        :type: str
        """

        self._release_status = release_status

    @property
    def start_delivery_at(self):
        """Gets the start_delivery_at of this ScheduledInstanceStockForDescribeScheduledInstanceStockOutput.  # noqa: E501


        :return: The start_delivery_at of this ScheduledInstanceStockForDescribeScheduledInstanceStockOutput.  # noqa: E501
        :rtype: str
        """
        return self._start_delivery_at

    @start_delivery_at.setter
    def start_delivery_at(self, start_delivery_at):
        """Sets the start_delivery_at of this ScheduledInstanceStockForDescribeScheduledInstanceStockOutput.


        :param start_delivery_at: The start_delivery_at of this ScheduledInstanceStockForDescribeScheduledInstanceStockOutput.  # noqa: E501
        :type: str
        """

        self._start_delivery_at = start_delivery_at

    @property
    def status(self):
        """Gets the status of this ScheduledInstanceStockForDescribeScheduledInstanceStockOutput.  # noqa: E501


        :return: The status of this ScheduledInstanceStockForDescribeScheduledInstanceStockOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ScheduledInstanceStockForDescribeScheduledInstanceStockOutput.


        :param status: The status of this ScheduledInstanceStockForDescribeScheduledInstanceStockOutput.  # noqa: E501
        :type: str
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
        if issubclass(ScheduledInstanceStockForDescribeScheduledInstanceStockOutput, dict):
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
        if not isinstance(other, ScheduledInstanceStockForDescribeScheduledInstanceStockOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ScheduledInstanceStockForDescribeScheduledInstanceStockOutput):
            return True

        return self.to_dict() != other.to_dict()
