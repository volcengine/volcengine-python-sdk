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


class ListHostAcceleratePackOrderRequest(object):
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
        'page_number': 'int',
        'page_size': 'int',
        'source': 'str',
        'start_time': 'str',
        'status': 'int',
        'uid': 'str'
    }

    attribute_map = {
        'end_time': 'EndTime',
        'page_number': 'PageNumber',
        'page_size': 'PageSize',
        'source': 'Source',
        'start_time': 'StartTime',
        'status': 'Status',
        'uid': 'Uid'
    }

    def __init__(self, end_time=None, page_number=None, page_size=None, source=None, start_time=None, status=None, uid=None, _configuration=None):  # noqa: E501
        """ListHostAcceleratePackOrderRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._end_time = None
        self._page_number = None
        self._page_size = None
        self._source = None
        self._start_time = None
        self._status = None
        self._uid = None
        self.discriminator = None

        if end_time is not None:
            self.end_time = end_time
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if source is not None:
            self.source = source
        if start_time is not None:
            self.start_time = start_time
        if status is not None:
            self.status = status
        if uid is not None:
            self.uid = uid

    @property
    def end_time(self):
        """Gets the end_time of this ListHostAcceleratePackOrderRequest.  # noqa: E501


        :return: The end_time of this ListHostAcceleratePackOrderRequest.  # noqa: E501
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListHostAcceleratePackOrderRequest.


        :param end_time: The end_time of this ListHostAcceleratePackOrderRequest.  # noqa: E501
        :type: str
        """

        self._end_time = end_time

    @property
    def page_number(self):
        """Gets the page_number of this ListHostAcceleratePackOrderRequest.  # noqa: E501


        :return: The page_number of this ListHostAcceleratePackOrderRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this ListHostAcceleratePackOrderRequest.


        :param page_number: The page_number of this ListHostAcceleratePackOrderRequest.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this ListHostAcceleratePackOrderRequest.  # noqa: E501


        :return: The page_size of this ListHostAcceleratePackOrderRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ListHostAcceleratePackOrderRequest.


        :param page_size: The page_size of this ListHostAcceleratePackOrderRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def source(self):
        """Gets the source of this ListHostAcceleratePackOrderRequest.  # noqa: E501


        :return: The source of this ListHostAcceleratePackOrderRequest.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this ListHostAcceleratePackOrderRequest.


        :param source: The source of this ListHostAcceleratePackOrderRequest.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def start_time(self):
        """Gets the start_time of this ListHostAcceleratePackOrderRequest.  # noqa: E501


        :return: The start_time of this ListHostAcceleratePackOrderRequest.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListHostAcceleratePackOrderRequest.


        :param start_time: The start_time of this ListHostAcceleratePackOrderRequest.  # noqa: E501
        :type: str
        """

        self._start_time = start_time

    @property
    def status(self):
        """Gets the status of this ListHostAcceleratePackOrderRequest.  # noqa: E501


        :return: The status of this ListHostAcceleratePackOrderRequest.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListHostAcceleratePackOrderRequest.


        :param status: The status of this ListHostAcceleratePackOrderRequest.  # noqa: E501
        :type: int
        """

        self._status = status

    @property
    def uid(self):
        """Gets the uid of this ListHostAcceleratePackOrderRequest.  # noqa: E501


        :return: The uid of this ListHostAcceleratePackOrderRequest.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this ListHostAcceleratePackOrderRequest.


        :param uid: The uid of this ListHostAcceleratePackOrderRequest.  # noqa: E501
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
        if issubclass(ListHostAcceleratePackOrderRequest, dict):
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
        if not isinstance(other, ListHostAcceleratePackOrderRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListHostAcceleratePackOrderRequest):
            return True

        return self.to_dict() != other.to_dict()
