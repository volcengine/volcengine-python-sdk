# coding: utf-8

"""
    private_zone

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ListRecordsRequest(object):
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
        'host': 'str',
        'last_operator': 'str',
        'line': 'str',
        'name': 'str',
        'page_number': 'int',
        'page_size': 'str',
        'project_name': 'str',
        'record_ids': 'str',
        'search_mode': 'str',
        'type': 'str',
        'value': 'str',
        'zid': 'int'
    }

    attribute_map = {
        'host': 'Host',
        'last_operator': 'LastOperator',
        'line': 'Line',
        'name': 'Name',
        'page_number': 'PageNumber',
        'page_size': 'PageSize',
        'project_name': 'ProjectName',
        'record_ids': 'RecordIDs',
        'search_mode': 'SearchMode',
        'type': 'Type',
        'value': 'Value',
        'zid': 'ZID'
    }

    def __init__(self, host=None, last_operator=None, line=None, name=None, page_number=None, page_size=None, project_name=None, record_ids=None, search_mode=None, type=None, value=None, zid=None, _configuration=None):  # noqa: E501
        """ListRecordsRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._host = None
        self._last_operator = None
        self._line = None
        self._name = None
        self._page_number = None
        self._page_size = None
        self._project_name = None
        self._record_ids = None
        self._search_mode = None
        self._type = None
        self._value = None
        self._zid = None
        self.discriminator = None

        if host is not None:
            self.host = host
        if last_operator is not None:
            self.last_operator = last_operator
        if line is not None:
            self.line = line
        if name is not None:
            self.name = name
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if project_name is not None:
            self.project_name = project_name
        if record_ids is not None:
            self.record_ids = record_ids
        if search_mode is not None:
            self.search_mode = search_mode
        if type is not None:
            self.type = type
        if value is not None:
            self.value = value
        if zid is not None:
            self.zid = zid

    @property
    def host(self):
        """Gets the host of this ListRecordsRequest.  # noqa: E501


        :return: The host of this ListRecordsRequest.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this ListRecordsRequest.


        :param host: The host of this ListRecordsRequest.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def last_operator(self):
        """Gets the last_operator of this ListRecordsRequest.  # noqa: E501


        :return: The last_operator of this ListRecordsRequest.  # noqa: E501
        :rtype: str
        """
        return self._last_operator

    @last_operator.setter
    def last_operator(self, last_operator):
        """Sets the last_operator of this ListRecordsRequest.


        :param last_operator: The last_operator of this ListRecordsRequest.  # noqa: E501
        :type: str
        """

        self._last_operator = last_operator

    @property
    def line(self):
        """Gets the line of this ListRecordsRequest.  # noqa: E501


        :return: The line of this ListRecordsRequest.  # noqa: E501
        :rtype: str
        """
        return self._line

    @line.setter
    def line(self, line):
        """Sets the line of this ListRecordsRequest.


        :param line: The line of this ListRecordsRequest.  # noqa: E501
        :type: str
        """

        self._line = line

    @property
    def name(self):
        """Gets the name of this ListRecordsRequest.  # noqa: E501


        :return: The name of this ListRecordsRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListRecordsRequest.


        :param name: The name of this ListRecordsRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def page_number(self):
        """Gets the page_number of this ListRecordsRequest.  # noqa: E501


        :return: The page_number of this ListRecordsRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this ListRecordsRequest.


        :param page_number: The page_number of this ListRecordsRequest.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this ListRecordsRequest.  # noqa: E501


        :return: The page_size of this ListRecordsRequest.  # noqa: E501
        :rtype: str
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ListRecordsRequest.


        :param page_size: The page_size of this ListRecordsRequest.  # noqa: E501
        :type: str
        """

        self._page_size = page_size

    @property
    def project_name(self):
        """Gets the project_name of this ListRecordsRequest.  # noqa: E501


        :return: The project_name of this ListRecordsRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this ListRecordsRequest.


        :param project_name: The project_name of this ListRecordsRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def record_ids(self):
        """Gets the record_ids of this ListRecordsRequest.  # noqa: E501


        :return: The record_ids of this ListRecordsRequest.  # noqa: E501
        :rtype: str
        """
        return self._record_ids

    @record_ids.setter
    def record_ids(self, record_ids):
        """Sets the record_ids of this ListRecordsRequest.


        :param record_ids: The record_ids of this ListRecordsRequest.  # noqa: E501
        :type: str
        """

        self._record_ids = record_ids

    @property
    def search_mode(self):
        """Gets the search_mode of this ListRecordsRequest.  # noqa: E501


        :return: The search_mode of this ListRecordsRequest.  # noqa: E501
        :rtype: str
        """
        return self._search_mode

    @search_mode.setter
    def search_mode(self, search_mode):
        """Sets the search_mode of this ListRecordsRequest.


        :param search_mode: The search_mode of this ListRecordsRequest.  # noqa: E501
        :type: str
        """

        self._search_mode = search_mode

    @property
    def type(self):
        """Gets the type of this ListRecordsRequest.  # noqa: E501


        :return: The type of this ListRecordsRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListRecordsRequest.


        :param type: The type of this ListRecordsRequest.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def value(self):
        """Gets the value of this ListRecordsRequest.  # noqa: E501


        :return: The value of this ListRecordsRequest.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ListRecordsRequest.


        :param value: The value of this ListRecordsRequest.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def zid(self):
        """Gets the zid of this ListRecordsRequest.  # noqa: E501


        :return: The zid of this ListRecordsRequest.  # noqa: E501
        :rtype: int
        """
        return self._zid

    @zid.setter
    def zid(self, zid):
        """Sets the zid of this ListRecordsRequest.


        :param zid: The zid of this ListRecordsRequest.  # noqa: E501
        :type: int
        """

        self._zid = zid

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
        if issubclass(ListRecordsRequest, dict):
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
        if not isinstance(other, ListRecordsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListRecordsRequest):
            return True

        return self.to_dict() != other.to_dict()
