# coding: utf-8

"""
    rabbitmq

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ChargeDetailForDescribeInstanceDetailOutput(object):
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
        'auto_renew': 'bool',
        'charge_end_time': 'str',
        'charge_expire_time': 'str',
        'charge_start_time': 'str',
        'charge_status': 'str',
        'charge_type': 'str',
        'overdue_reclaim_time': 'str',
        'overdue_time': 'str'
    }

    attribute_map = {
        'auto_renew': 'AutoRenew',
        'charge_end_time': 'ChargeEndTime',
        'charge_expire_time': 'ChargeExpireTime',
        'charge_start_time': 'ChargeStartTime',
        'charge_status': 'ChargeStatus',
        'charge_type': 'ChargeType',
        'overdue_reclaim_time': 'OverdueReclaimTime',
        'overdue_time': 'OverdueTime'
    }

    def __init__(self, auto_renew=None, charge_end_time=None, charge_expire_time=None, charge_start_time=None, charge_status=None, charge_type=None, overdue_reclaim_time=None, overdue_time=None, _configuration=None):  # noqa: E501
        """ChargeDetailForDescribeInstanceDetailOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._auto_renew = None
        self._charge_end_time = None
        self._charge_expire_time = None
        self._charge_start_time = None
        self._charge_status = None
        self._charge_type = None
        self._overdue_reclaim_time = None
        self._overdue_time = None
        self.discriminator = None

        if auto_renew is not None:
            self.auto_renew = auto_renew
        if charge_end_time is not None:
            self.charge_end_time = charge_end_time
        if charge_expire_time is not None:
            self.charge_expire_time = charge_expire_time
        if charge_start_time is not None:
            self.charge_start_time = charge_start_time
        if charge_status is not None:
            self.charge_status = charge_status
        if charge_type is not None:
            self.charge_type = charge_type
        if overdue_reclaim_time is not None:
            self.overdue_reclaim_time = overdue_reclaim_time
        if overdue_time is not None:
            self.overdue_time = overdue_time

    @property
    def auto_renew(self):
        """Gets the auto_renew of this ChargeDetailForDescribeInstanceDetailOutput.  # noqa: E501


        :return: The auto_renew of this ChargeDetailForDescribeInstanceDetailOutput.  # noqa: E501
        :rtype: bool
        """
        return self._auto_renew

    @auto_renew.setter
    def auto_renew(self, auto_renew):
        """Sets the auto_renew of this ChargeDetailForDescribeInstanceDetailOutput.


        :param auto_renew: The auto_renew of this ChargeDetailForDescribeInstanceDetailOutput.  # noqa: E501
        :type: bool
        """

        self._auto_renew = auto_renew

    @property
    def charge_end_time(self):
        """Gets the charge_end_time of this ChargeDetailForDescribeInstanceDetailOutput.  # noqa: E501


        :return: The charge_end_time of this ChargeDetailForDescribeInstanceDetailOutput.  # noqa: E501
        :rtype: str
        """
        return self._charge_end_time

    @charge_end_time.setter
    def charge_end_time(self, charge_end_time):
        """Sets the charge_end_time of this ChargeDetailForDescribeInstanceDetailOutput.


        :param charge_end_time: The charge_end_time of this ChargeDetailForDescribeInstanceDetailOutput.  # noqa: E501
        :type: str
        """

        self._charge_end_time = charge_end_time

    @property
    def charge_expire_time(self):
        """Gets the charge_expire_time of this ChargeDetailForDescribeInstanceDetailOutput.  # noqa: E501


        :return: The charge_expire_time of this ChargeDetailForDescribeInstanceDetailOutput.  # noqa: E501
        :rtype: str
        """
        return self._charge_expire_time

    @charge_expire_time.setter
    def charge_expire_time(self, charge_expire_time):
        """Sets the charge_expire_time of this ChargeDetailForDescribeInstanceDetailOutput.


        :param charge_expire_time: The charge_expire_time of this ChargeDetailForDescribeInstanceDetailOutput.  # noqa: E501
        :type: str
        """

        self._charge_expire_time = charge_expire_time

    @property
    def charge_start_time(self):
        """Gets the charge_start_time of this ChargeDetailForDescribeInstanceDetailOutput.  # noqa: E501


        :return: The charge_start_time of this ChargeDetailForDescribeInstanceDetailOutput.  # noqa: E501
        :rtype: str
        """
        return self._charge_start_time

    @charge_start_time.setter
    def charge_start_time(self, charge_start_time):
        """Sets the charge_start_time of this ChargeDetailForDescribeInstanceDetailOutput.


        :param charge_start_time: The charge_start_time of this ChargeDetailForDescribeInstanceDetailOutput.  # noqa: E501
        :type: str
        """

        self._charge_start_time = charge_start_time

    @property
    def charge_status(self):
        """Gets the charge_status of this ChargeDetailForDescribeInstanceDetailOutput.  # noqa: E501


        :return: The charge_status of this ChargeDetailForDescribeInstanceDetailOutput.  # noqa: E501
        :rtype: str
        """
        return self._charge_status

    @charge_status.setter
    def charge_status(self, charge_status):
        """Sets the charge_status of this ChargeDetailForDescribeInstanceDetailOutput.


        :param charge_status: The charge_status of this ChargeDetailForDescribeInstanceDetailOutput.  # noqa: E501
        :type: str
        """

        self._charge_status = charge_status

    @property
    def charge_type(self):
        """Gets the charge_type of this ChargeDetailForDescribeInstanceDetailOutput.  # noqa: E501


        :return: The charge_type of this ChargeDetailForDescribeInstanceDetailOutput.  # noqa: E501
        :rtype: str
        """
        return self._charge_type

    @charge_type.setter
    def charge_type(self, charge_type):
        """Sets the charge_type of this ChargeDetailForDescribeInstanceDetailOutput.


        :param charge_type: The charge_type of this ChargeDetailForDescribeInstanceDetailOutput.  # noqa: E501
        :type: str
        """

        self._charge_type = charge_type

    @property
    def overdue_reclaim_time(self):
        """Gets the overdue_reclaim_time of this ChargeDetailForDescribeInstanceDetailOutput.  # noqa: E501


        :return: The overdue_reclaim_time of this ChargeDetailForDescribeInstanceDetailOutput.  # noqa: E501
        :rtype: str
        """
        return self._overdue_reclaim_time

    @overdue_reclaim_time.setter
    def overdue_reclaim_time(self, overdue_reclaim_time):
        """Sets the overdue_reclaim_time of this ChargeDetailForDescribeInstanceDetailOutput.


        :param overdue_reclaim_time: The overdue_reclaim_time of this ChargeDetailForDescribeInstanceDetailOutput.  # noqa: E501
        :type: str
        """

        self._overdue_reclaim_time = overdue_reclaim_time

    @property
    def overdue_time(self):
        """Gets the overdue_time of this ChargeDetailForDescribeInstanceDetailOutput.  # noqa: E501


        :return: The overdue_time of this ChargeDetailForDescribeInstanceDetailOutput.  # noqa: E501
        :rtype: str
        """
        return self._overdue_time

    @overdue_time.setter
    def overdue_time(self, overdue_time):
        """Sets the overdue_time of this ChargeDetailForDescribeInstanceDetailOutput.


        :param overdue_time: The overdue_time of this ChargeDetailForDescribeInstanceDetailOutput.  # noqa: E501
        :type: str
        """

        self._overdue_time = overdue_time

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
        if issubclass(ChargeDetailForDescribeInstanceDetailOutput, dict):
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
        if not isinstance(other, ChargeDetailForDescribeInstanceDetailOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ChargeDetailForDescribeInstanceDetailOutput):
            return True

        return self.to_dict() != other.to_dict()
