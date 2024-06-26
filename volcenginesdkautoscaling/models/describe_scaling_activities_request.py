# coding: utf-8

"""
    auto_scaling

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeScalingActivitiesRequest(object):
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
        'scaling_activity_ids': 'list[str]',
        'scaling_group_id': 'str',
        'start_time': 'str',
        'status_code': 'str'
    }

    attribute_map = {
        'end_time': 'EndTime',
        'page_number': 'PageNumber',
        'page_size': 'PageSize',
        'scaling_activity_ids': 'ScalingActivityIds',
        'scaling_group_id': 'ScalingGroupId',
        'start_time': 'StartTime',
        'status_code': 'StatusCode'
    }

    def __init__(self, end_time=None, page_number=None, page_size=None, scaling_activity_ids=None, scaling_group_id=None, start_time=None, status_code=None, _configuration=None):  # noqa: E501
        """DescribeScalingActivitiesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._end_time = None
        self._page_number = None
        self._page_size = None
        self._scaling_activity_ids = None
        self._scaling_group_id = None
        self._start_time = None
        self._status_code = None
        self.discriminator = None

        if end_time is not None:
            self.end_time = end_time
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if scaling_activity_ids is not None:
            self.scaling_activity_ids = scaling_activity_ids
        self.scaling_group_id = scaling_group_id
        if start_time is not None:
            self.start_time = start_time
        if status_code is not None:
            self.status_code = status_code

    @property
    def end_time(self):
        """Gets the end_time of this DescribeScalingActivitiesRequest.  # noqa: E501


        :return: The end_time of this DescribeScalingActivitiesRequest.  # noqa: E501
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this DescribeScalingActivitiesRequest.


        :param end_time: The end_time of this DescribeScalingActivitiesRequest.  # noqa: E501
        :type: str
        """

        self._end_time = end_time

    @property
    def page_number(self):
        """Gets the page_number of this DescribeScalingActivitiesRequest.  # noqa: E501


        :return: The page_number of this DescribeScalingActivitiesRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this DescribeScalingActivitiesRequest.


        :param page_number: The page_number of this DescribeScalingActivitiesRequest.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this DescribeScalingActivitiesRequest.  # noqa: E501


        :return: The page_size of this DescribeScalingActivitiesRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this DescribeScalingActivitiesRequest.


        :param page_size: The page_size of this DescribeScalingActivitiesRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def scaling_activity_ids(self):
        """Gets the scaling_activity_ids of this DescribeScalingActivitiesRequest.  # noqa: E501


        :return: The scaling_activity_ids of this DescribeScalingActivitiesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._scaling_activity_ids

    @scaling_activity_ids.setter
    def scaling_activity_ids(self, scaling_activity_ids):
        """Sets the scaling_activity_ids of this DescribeScalingActivitiesRequest.


        :param scaling_activity_ids: The scaling_activity_ids of this DescribeScalingActivitiesRequest.  # noqa: E501
        :type: list[str]
        """

        self._scaling_activity_ids = scaling_activity_ids

    @property
    def scaling_group_id(self):
        """Gets the scaling_group_id of this DescribeScalingActivitiesRequest.  # noqa: E501


        :return: The scaling_group_id of this DescribeScalingActivitiesRequest.  # noqa: E501
        :rtype: str
        """
        return self._scaling_group_id

    @scaling_group_id.setter
    def scaling_group_id(self, scaling_group_id):
        """Sets the scaling_group_id of this DescribeScalingActivitiesRequest.


        :param scaling_group_id: The scaling_group_id of this DescribeScalingActivitiesRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and scaling_group_id is None:
            raise ValueError("Invalid value for `scaling_group_id`, must not be `None`")  # noqa: E501

        self._scaling_group_id = scaling_group_id

    @property
    def start_time(self):
        """Gets the start_time of this DescribeScalingActivitiesRequest.  # noqa: E501


        :return: The start_time of this DescribeScalingActivitiesRequest.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this DescribeScalingActivitiesRequest.


        :param start_time: The start_time of this DescribeScalingActivitiesRequest.  # noqa: E501
        :type: str
        """

        self._start_time = start_time

    @property
    def status_code(self):
        """Gets the status_code of this DescribeScalingActivitiesRequest.  # noqa: E501


        :return: The status_code of this DescribeScalingActivitiesRequest.  # noqa: E501
        :rtype: str
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this DescribeScalingActivitiesRequest.


        :param status_code: The status_code of this DescribeScalingActivitiesRequest.  # noqa: E501
        :type: str
        """

        self._status_code = status_code

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
        if issubclass(DescribeScalingActivitiesRequest, dict):
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
        if not isinstance(other, DescribeScalingActivitiesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeScalingActivitiesRequest):
            return True

        return self.to_dict() != other.to_dict()
