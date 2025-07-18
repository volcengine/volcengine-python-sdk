# coding: utf-8

"""
    livesaas

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ListMediasAPIRequest(object):
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
        'activity_id': 'int',
        'end_time': 'int',
        'is_need_total_count': 'bool',
        'name': 'str',
        'online_status': 'int',
        'page_item_count': 'int',
        'page_no': 'int',
        'start_time': 'int',
        'vid': 'str'
    }

    attribute_map = {
        'activity_id': 'ActivityId',
        'end_time': 'EndTime',
        'is_need_total_count': 'IsNeedTotalCount',
        'name': 'Name',
        'online_status': 'OnlineStatus',
        'page_item_count': 'PageItemCount',
        'page_no': 'PageNo',
        'start_time': 'StartTime',
        'vid': 'Vid'
    }

    def __init__(self, activity_id=None, end_time=None, is_need_total_count=None, name=None, online_status=None, page_item_count=None, page_no=None, start_time=None, vid=None, _configuration=None):  # noqa: E501
        """ListMediasAPIRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._activity_id = None
        self._end_time = None
        self._is_need_total_count = None
        self._name = None
        self._online_status = None
        self._page_item_count = None
        self._page_no = None
        self._start_time = None
        self._vid = None
        self.discriminator = None

        self.activity_id = activity_id
        if end_time is not None:
            self.end_time = end_time
        if is_need_total_count is not None:
            self.is_need_total_count = is_need_total_count
        if name is not None:
            self.name = name
        if online_status is not None:
            self.online_status = online_status
        if page_item_count is not None:
            self.page_item_count = page_item_count
        if page_no is not None:
            self.page_no = page_no
        if start_time is not None:
            self.start_time = start_time
        if vid is not None:
            self.vid = vid

    @property
    def activity_id(self):
        """Gets the activity_id of this ListMediasAPIRequest.  # noqa: E501


        :return: The activity_id of this ListMediasAPIRequest.  # noqa: E501
        :rtype: int
        """
        return self._activity_id

    @activity_id.setter
    def activity_id(self, activity_id):
        """Sets the activity_id of this ListMediasAPIRequest.


        :param activity_id: The activity_id of this ListMediasAPIRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and activity_id is None:
            raise ValueError("Invalid value for `activity_id`, must not be `None`")  # noqa: E501

        self._activity_id = activity_id

    @property
    def end_time(self):
        """Gets the end_time of this ListMediasAPIRequest.  # noqa: E501


        :return: The end_time of this ListMediasAPIRequest.  # noqa: E501
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListMediasAPIRequest.


        :param end_time: The end_time of this ListMediasAPIRequest.  # noqa: E501
        :type: int
        """

        self._end_time = end_time

    @property
    def is_need_total_count(self):
        """Gets the is_need_total_count of this ListMediasAPIRequest.  # noqa: E501


        :return: The is_need_total_count of this ListMediasAPIRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_need_total_count

    @is_need_total_count.setter
    def is_need_total_count(self, is_need_total_count):
        """Sets the is_need_total_count of this ListMediasAPIRequest.


        :param is_need_total_count: The is_need_total_count of this ListMediasAPIRequest.  # noqa: E501
        :type: bool
        """

        self._is_need_total_count = is_need_total_count

    @property
    def name(self):
        """Gets the name of this ListMediasAPIRequest.  # noqa: E501


        :return: The name of this ListMediasAPIRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListMediasAPIRequest.


        :param name: The name of this ListMediasAPIRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def online_status(self):
        """Gets the online_status of this ListMediasAPIRequest.  # noqa: E501


        :return: The online_status of this ListMediasAPIRequest.  # noqa: E501
        :rtype: int
        """
        return self._online_status

    @online_status.setter
    def online_status(self, online_status):
        """Sets the online_status of this ListMediasAPIRequest.


        :param online_status: The online_status of this ListMediasAPIRequest.  # noqa: E501
        :type: int
        """

        self._online_status = online_status

    @property
    def page_item_count(self):
        """Gets the page_item_count of this ListMediasAPIRequest.  # noqa: E501


        :return: The page_item_count of this ListMediasAPIRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_item_count

    @page_item_count.setter
    def page_item_count(self, page_item_count):
        """Sets the page_item_count of this ListMediasAPIRequest.


        :param page_item_count: The page_item_count of this ListMediasAPIRequest.  # noqa: E501
        :type: int
        """

        self._page_item_count = page_item_count

    @property
    def page_no(self):
        """Gets the page_no of this ListMediasAPIRequest.  # noqa: E501


        :return: The page_no of this ListMediasAPIRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        """Sets the page_no of this ListMediasAPIRequest.


        :param page_no: The page_no of this ListMediasAPIRequest.  # noqa: E501
        :type: int
        """

        self._page_no = page_no

    @property
    def start_time(self):
        """Gets the start_time of this ListMediasAPIRequest.  # noqa: E501


        :return: The start_time of this ListMediasAPIRequest.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListMediasAPIRequest.


        :param start_time: The start_time of this ListMediasAPIRequest.  # noqa: E501
        :type: int
        """

        self._start_time = start_time

    @property
    def vid(self):
        """Gets the vid of this ListMediasAPIRequest.  # noqa: E501


        :return: The vid of this ListMediasAPIRequest.  # noqa: E501
        :rtype: str
        """
        return self._vid

    @vid.setter
    def vid(self, vid):
        """Sets the vid of this ListMediasAPIRequest.


        :param vid: The vid of this ListMediasAPIRequest.  # noqa: E501
        :type: str
        """

        self._vid = vid

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
        if issubclass(ListMediasAPIRequest, dict):
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
        if not isinstance(other, ListMediasAPIRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListMediasAPIRequest):
            return True

        return self.to_dict() != other.to_dict()
