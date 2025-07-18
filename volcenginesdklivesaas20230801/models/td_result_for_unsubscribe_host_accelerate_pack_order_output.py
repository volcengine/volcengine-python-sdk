# coding: utf-8

"""
    livesaas20230801

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class TDResultForUnsubscribeHostAcceleratePackOrderOutput(object):
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
        'end_time': 'str',
        'order_id': 'str',
        'status': 'int',
        'uid': 'str'
    }

    attribute_map = {
        'end_time': 'EndTime',
        'order_id': 'OrderId',
        'status': 'Status',
        'uid': 'Uid'
    }

    def __init__(self, end_time=None, order_id=None, status=None, uid=None, _configuration=None):  # noqa: E501
        """TDResultForUnsubscribeHostAcceleratePackOrderOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._end_time = None
        self._order_id = None
        self._status = None
        self._uid = None
        self.discriminator = None

        if end_time is not None:
            self.end_time = end_time
        if order_id is not None:
            self.order_id = order_id
        if status is not None:
            self.status = status
        if uid is not None:
            self.uid = uid

    @property
    def end_time(self):
        """Gets the end_time of this TDResultForUnsubscribeHostAcceleratePackOrderOutput.  # noqa: E501


        :return: The end_time of this TDResultForUnsubscribeHostAcceleratePackOrderOutput.  # noqa: E501
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this TDResultForUnsubscribeHostAcceleratePackOrderOutput.


        :param end_time: The end_time of this TDResultForUnsubscribeHostAcceleratePackOrderOutput.  # noqa: E501
        :type: str
        """

        self._end_time = end_time

    @property
    def order_id(self):
        """Gets the order_id of this TDResultForUnsubscribeHostAcceleratePackOrderOutput.  # noqa: E501


        :return: The order_id of this TDResultForUnsubscribeHostAcceleratePackOrderOutput.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this TDResultForUnsubscribeHostAcceleratePackOrderOutput.


        :param order_id: The order_id of this TDResultForUnsubscribeHostAcceleratePackOrderOutput.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

    @property
    def status(self):
        """Gets the status of this TDResultForUnsubscribeHostAcceleratePackOrderOutput.  # noqa: E501


        :return: The status of this TDResultForUnsubscribeHostAcceleratePackOrderOutput.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TDResultForUnsubscribeHostAcceleratePackOrderOutput.


        :param status: The status of this TDResultForUnsubscribeHostAcceleratePackOrderOutput.  # noqa: E501
        :type: int
        """

        self._status = status

    @property
    def uid(self):
        """Gets the uid of this TDResultForUnsubscribeHostAcceleratePackOrderOutput.  # noqa: E501


        :return: The uid of this TDResultForUnsubscribeHostAcceleratePackOrderOutput.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this TDResultForUnsubscribeHostAcceleratePackOrderOutput.


        :param uid: The uid of this TDResultForUnsubscribeHostAcceleratePackOrderOutput.  # noqa: E501
        :type: str
        """

        self._uid = uid

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
        if issubclass(TDResultForUnsubscribeHostAcceleratePackOrderOutput, dict):
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
        if not isinstance(other, TDResultForUnsubscribeHostAcceleratePackOrderOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TDResultForUnsubscribeHostAcceleratePackOrderOutput):
            return True

        return self.to_dict() != other.to_dict()
