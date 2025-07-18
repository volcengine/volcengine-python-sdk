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


class CreateResultForCreateHostAcceleratePackOrderOutput(object):
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
        'douyin_id': 'str',
        'end_time': 'str',
        'is_renew': 'bool',
        'order_id': 'str',
        'province': 'str',
        'source': 'str',
        'start_time': 'str',
        'status': 'str',
        'uid': 'str'
    }

    attribute_map = {
        'douyin_id': 'DouyinId',
        'end_time': 'EndTime',
        'is_renew': 'IsRenew',
        'order_id': 'OrderId',
        'province': 'Province',
        'source': 'Source',
        'start_time': 'StartTime',
        'status': 'Status',
        'uid': 'Uid'
    }

    def __init__(self, douyin_id=None, end_time=None, is_renew=None, order_id=None, province=None, source=None, start_time=None, status=None, uid=None, _configuration=None):  # noqa: E501
        """CreateResultForCreateHostAcceleratePackOrderOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._douyin_id = None
        self._end_time = None
        self._is_renew = None
        self._order_id = None
        self._province = None
        self._source = None
        self._start_time = None
        self._status = None
        self._uid = None
        self.discriminator = None

        if douyin_id is not None:
            self.douyin_id = douyin_id
        if end_time is not None:
            self.end_time = end_time
        if is_renew is not None:
            self.is_renew = is_renew
        if order_id is not None:
            self.order_id = order_id
        if province is not None:
            self.province = province
        if source is not None:
            self.source = source
        if start_time is not None:
            self.start_time = start_time
        if status is not None:
            self.status = status
        if uid is not None:
            self.uid = uid

    @property
    def douyin_id(self):
        """Gets the douyin_id of this CreateResultForCreateHostAcceleratePackOrderOutput.  # noqa: E501


        :return: The douyin_id of this CreateResultForCreateHostAcceleratePackOrderOutput.  # noqa: E501
        :rtype: str
        """
        return self._douyin_id

    @douyin_id.setter
    def douyin_id(self, douyin_id):
        """Sets the douyin_id of this CreateResultForCreateHostAcceleratePackOrderOutput.


        :param douyin_id: The douyin_id of this CreateResultForCreateHostAcceleratePackOrderOutput.  # noqa: E501
        :type: str
        """

        self._douyin_id = douyin_id

    @property
    def end_time(self):
        """Gets the end_time of this CreateResultForCreateHostAcceleratePackOrderOutput.  # noqa: E501


        :return: The end_time of this CreateResultForCreateHostAcceleratePackOrderOutput.  # noqa: E501
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this CreateResultForCreateHostAcceleratePackOrderOutput.


        :param end_time: The end_time of this CreateResultForCreateHostAcceleratePackOrderOutput.  # noqa: E501
        :type: str
        """

        self._end_time = end_time

    @property
    def is_renew(self):
        """Gets the is_renew of this CreateResultForCreateHostAcceleratePackOrderOutput.  # noqa: E501


        :return: The is_renew of this CreateResultForCreateHostAcceleratePackOrderOutput.  # noqa: E501
        :rtype: bool
        """
        return self._is_renew

    @is_renew.setter
    def is_renew(self, is_renew):
        """Sets the is_renew of this CreateResultForCreateHostAcceleratePackOrderOutput.


        :param is_renew: The is_renew of this CreateResultForCreateHostAcceleratePackOrderOutput.  # noqa: E501
        :type: bool
        """

        self._is_renew = is_renew

    @property
    def order_id(self):
        """Gets the order_id of this CreateResultForCreateHostAcceleratePackOrderOutput.  # noqa: E501


        :return: The order_id of this CreateResultForCreateHostAcceleratePackOrderOutput.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this CreateResultForCreateHostAcceleratePackOrderOutput.


        :param order_id: The order_id of this CreateResultForCreateHostAcceleratePackOrderOutput.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

    @property
    def province(self):
        """Gets the province of this CreateResultForCreateHostAcceleratePackOrderOutput.  # noqa: E501


        :return: The province of this CreateResultForCreateHostAcceleratePackOrderOutput.  # noqa: E501
        :rtype: str
        """
        return self._province

    @province.setter
    def province(self, province):
        """Sets the province of this CreateResultForCreateHostAcceleratePackOrderOutput.


        :param province: The province of this CreateResultForCreateHostAcceleratePackOrderOutput.  # noqa: E501
        :type: str
        """

        self._province = province

    @property
    def source(self):
        """Gets the source of this CreateResultForCreateHostAcceleratePackOrderOutput.  # noqa: E501


        :return: The source of this CreateResultForCreateHostAcceleratePackOrderOutput.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this CreateResultForCreateHostAcceleratePackOrderOutput.


        :param source: The source of this CreateResultForCreateHostAcceleratePackOrderOutput.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def start_time(self):
        """Gets the start_time of this CreateResultForCreateHostAcceleratePackOrderOutput.  # noqa: E501


        :return: The start_time of this CreateResultForCreateHostAcceleratePackOrderOutput.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this CreateResultForCreateHostAcceleratePackOrderOutput.


        :param start_time: The start_time of this CreateResultForCreateHostAcceleratePackOrderOutput.  # noqa: E501
        :type: str
        """

        self._start_time = start_time

    @property
    def status(self):
        """Gets the status of this CreateResultForCreateHostAcceleratePackOrderOutput.  # noqa: E501


        :return: The status of this CreateResultForCreateHostAcceleratePackOrderOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateResultForCreateHostAcceleratePackOrderOutput.


        :param status: The status of this CreateResultForCreateHostAcceleratePackOrderOutput.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def uid(self):
        """Gets the uid of this CreateResultForCreateHostAcceleratePackOrderOutput.  # noqa: E501


        :return: The uid of this CreateResultForCreateHostAcceleratePackOrderOutput.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this CreateResultForCreateHostAcceleratePackOrderOutput.


        :param uid: The uid of this CreateResultForCreateHostAcceleratePackOrderOutput.  # noqa: E501
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
        if issubclass(CreateResultForCreateHostAcceleratePackOrderOutput, dict):
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
        if not isinstance(other, CreateResultForCreateHostAcceleratePackOrderOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateResultForCreateHostAcceleratePackOrderOutput):
            return True

        return self.to_dict() != other.to_dict()
