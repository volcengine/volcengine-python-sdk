# coding: utf-8

"""
    waf

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ListProhibitionRequest(object):
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
        'end_time': 'int',
        'host': 'str',
        'ip': 'str',
        'letter_order_by': 'str',
        'page': 'int',
        'page_size': 'int',
        'path_order_by': 'str',
        'project_name': 'str',
        'reason': 'list[str]',
        'start_time': 'int',
        'status': 'list[int]',
        'time_order_by': 'str'
    }

    attribute_map = {
        'end_time': 'EndTime',
        'host': 'Host',
        'ip': 'Ip',
        'letter_order_by': 'LetterOrderBy',
        'page': 'Page',
        'page_size': 'PageSize',
        'path_order_by': 'PathOrderBy',
        'project_name': 'ProjectName',
        'reason': 'Reason',
        'start_time': 'StartTime',
        'status': 'Status',
        'time_order_by': 'TimeOrderBy'
    }

    def __init__(self, end_time=None, host=None, ip=None, letter_order_by=None, page=None, page_size=None, path_order_by=None, project_name=None, reason=None, start_time=None, status=None, time_order_by=None, _configuration=None):  # noqa: E501
        """ListProhibitionRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._end_time = None
        self._host = None
        self._ip = None
        self._letter_order_by = None
        self._page = None
        self._page_size = None
        self._path_order_by = None
        self._project_name = None
        self._reason = None
        self._start_time = None
        self._status = None
        self._time_order_by = None
        self.discriminator = None

        self.end_time = end_time
        self.host = host
        if ip is not None:
            self.ip = ip
        if letter_order_by is not None:
            self.letter_order_by = letter_order_by
        if page is not None:
            self.page = page
        if page_size is not None:
            self.page_size = page_size
        if path_order_by is not None:
            self.path_order_by = path_order_by
        if project_name is not None:
            self.project_name = project_name
        if reason is not None:
            self.reason = reason
        self.start_time = start_time
        if status is not None:
            self.status = status
        if time_order_by is not None:
            self.time_order_by = time_order_by

    @property
    def end_time(self):
        """Gets the end_time of this ListProhibitionRequest.  # noqa: E501


        :return: The end_time of this ListProhibitionRequest.  # noqa: E501
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListProhibitionRequest.


        :param end_time: The end_time of this ListProhibitionRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and end_time is None:
            raise ValueError("Invalid value for `end_time`, must not be `None`")  # noqa: E501

        self._end_time = end_time

    @property
    def host(self):
        """Gets the host of this ListProhibitionRequest.  # noqa: E501


        :return: The host of this ListProhibitionRequest.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this ListProhibitionRequest.


        :param host: The host of this ListProhibitionRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and host is None:
            raise ValueError("Invalid value for `host`, must not be `None`")  # noqa: E501

        self._host = host

    @property
    def ip(self):
        """Gets the ip of this ListProhibitionRequest.  # noqa: E501


        :return: The ip of this ListProhibitionRequest.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this ListProhibitionRequest.


        :param ip: The ip of this ListProhibitionRequest.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def letter_order_by(self):
        """Gets the letter_order_by of this ListProhibitionRequest.  # noqa: E501


        :return: The letter_order_by of this ListProhibitionRequest.  # noqa: E501
        :rtype: str
        """
        return self._letter_order_by

    @letter_order_by.setter
    def letter_order_by(self, letter_order_by):
        """Sets the letter_order_by of this ListProhibitionRequest.


        :param letter_order_by: The letter_order_by of this ListProhibitionRequest.  # noqa: E501
        :type: str
        """

        self._letter_order_by = letter_order_by

    @property
    def page(self):
        """Gets the page of this ListProhibitionRequest.  # noqa: E501


        :return: The page of this ListProhibitionRequest.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListProhibitionRequest.


        :param page: The page of this ListProhibitionRequest.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def page_size(self):
        """Gets the page_size of this ListProhibitionRequest.  # noqa: E501


        :return: The page_size of this ListProhibitionRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ListProhibitionRequest.


        :param page_size: The page_size of this ListProhibitionRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def path_order_by(self):
        """Gets the path_order_by of this ListProhibitionRequest.  # noqa: E501


        :return: The path_order_by of this ListProhibitionRequest.  # noqa: E501
        :rtype: str
        """
        return self._path_order_by

    @path_order_by.setter
    def path_order_by(self, path_order_by):
        """Sets the path_order_by of this ListProhibitionRequest.


        :param path_order_by: The path_order_by of this ListProhibitionRequest.  # noqa: E501
        :type: str
        """

        self._path_order_by = path_order_by

    @property
    def project_name(self):
        """Gets the project_name of this ListProhibitionRequest.  # noqa: E501


        :return: The project_name of this ListProhibitionRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this ListProhibitionRequest.


        :param project_name: The project_name of this ListProhibitionRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def reason(self):
        """Gets the reason of this ListProhibitionRequest.  # noqa: E501


        :return: The reason of this ListProhibitionRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this ListProhibitionRequest.


        :param reason: The reason of this ListProhibitionRequest.  # noqa: E501
        :type: list[str]
        """

        self._reason = reason

    @property
    def start_time(self):
        """Gets the start_time of this ListProhibitionRequest.  # noqa: E501


        :return: The start_time of this ListProhibitionRequest.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListProhibitionRequest.


        :param start_time: The start_time of this ListProhibitionRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and start_time is None:
            raise ValueError("Invalid value for `start_time`, must not be `None`")  # noqa: E501

        self._start_time = start_time

    @property
    def status(self):
        """Gets the status of this ListProhibitionRequest.  # noqa: E501


        :return: The status of this ListProhibitionRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListProhibitionRequest.


        :param status: The status of this ListProhibitionRequest.  # noqa: E501
        :type: list[int]
        """

        self._status = status

    @property
    def time_order_by(self):
        """Gets the time_order_by of this ListProhibitionRequest.  # noqa: E501


        :return: The time_order_by of this ListProhibitionRequest.  # noqa: E501
        :rtype: str
        """
        return self._time_order_by

    @time_order_by.setter
    def time_order_by(self, time_order_by):
        """Sets the time_order_by of this ListProhibitionRequest.


        :param time_order_by: The time_order_by of this ListProhibitionRequest.  # noqa: E501
        :type: str
        """

        self._time_order_by = time_order_by

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
        if issubclass(ListProhibitionRequest, dict):
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
        if not isinstance(other, ListProhibitionRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListProhibitionRequest):
            return True

        return self.to_dict() != other.to_dict()
