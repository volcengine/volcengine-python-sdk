# coding: utf-8

"""
    rocketmq

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeGroupsDetailResponse(object):
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
        'create_time': 'str',
        'description': 'str',
        'group_id': 'str',
        'group_type': 'str',
        'is_sub_same': 'bool',
        'message_delay_time': 'str',
        'message_model': 'str',
        'status': 'str',
        'total_consumed_rate': 'str',
        'total_diff': 'int'
    }

    attribute_map = {
        'create_time': 'CreateTime',
        'description': 'Description',
        'group_id': 'GroupId',
        'group_type': 'GroupType',
        'is_sub_same': 'IsSubSame',
        'message_delay_time': 'MessageDelayTime',
        'message_model': 'MessageModel',
        'status': 'Status',
        'total_consumed_rate': 'TotalConsumedRate',
        'total_diff': 'TotalDiff'
    }

    def __init__(self, create_time=None, description=None, group_id=None, group_type=None, is_sub_same=None, message_delay_time=None, message_model=None, status=None, total_consumed_rate=None, total_diff=None, _configuration=None):  # noqa: E501
        """DescribeGroupsDetailResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._create_time = None
        self._description = None
        self._group_id = None
        self._group_type = None
        self._is_sub_same = None
        self._message_delay_time = None
        self._message_model = None
        self._status = None
        self._total_consumed_rate = None
        self._total_diff = None
        self.discriminator = None

        if create_time is not None:
            self.create_time = create_time
        if description is not None:
            self.description = description
        if group_id is not None:
            self.group_id = group_id
        if group_type is not None:
            self.group_type = group_type
        if is_sub_same is not None:
            self.is_sub_same = is_sub_same
        if message_delay_time is not None:
            self.message_delay_time = message_delay_time
        if message_model is not None:
            self.message_model = message_model
        if status is not None:
            self.status = status
        if total_consumed_rate is not None:
            self.total_consumed_rate = total_consumed_rate
        if total_diff is not None:
            self.total_diff = total_diff

    @property
    def create_time(self):
        """Gets the create_time of this DescribeGroupsDetailResponse.  # noqa: E501


        :return: The create_time of this DescribeGroupsDetailResponse.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this DescribeGroupsDetailResponse.


        :param create_time: The create_time of this DescribeGroupsDetailResponse.  # noqa: E501
        :type: str
        """

        self._create_time = create_time

    @property
    def description(self):
        """Gets the description of this DescribeGroupsDetailResponse.  # noqa: E501


        :return: The description of this DescribeGroupsDetailResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DescribeGroupsDetailResponse.


        :param description: The description of this DescribeGroupsDetailResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def group_id(self):
        """Gets the group_id of this DescribeGroupsDetailResponse.  # noqa: E501


        :return: The group_id of this DescribeGroupsDetailResponse.  # noqa: E501
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this DescribeGroupsDetailResponse.


        :param group_id: The group_id of this DescribeGroupsDetailResponse.  # noqa: E501
        :type: str
        """

        self._group_id = group_id

    @property
    def group_type(self):
        """Gets the group_type of this DescribeGroupsDetailResponse.  # noqa: E501


        :return: The group_type of this DescribeGroupsDetailResponse.  # noqa: E501
        :rtype: str
        """
        return self._group_type

    @group_type.setter
    def group_type(self, group_type):
        """Sets the group_type of this DescribeGroupsDetailResponse.


        :param group_type: The group_type of this DescribeGroupsDetailResponse.  # noqa: E501
        :type: str
        """

        self._group_type = group_type

    @property
    def is_sub_same(self):
        """Gets the is_sub_same of this DescribeGroupsDetailResponse.  # noqa: E501


        :return: The is_sub_same of this DescribeGroupsDetailResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_sub_same

    @is_sub_same.setter
    def is_sub_same(self, is_sub_same):
        """Sets the is_sub_same of this DescribeGroupsDetailResponse.


        :param is_sub_same: The is_sub_same of this DescribeGroupsDetailResponse.  # noqa: E501
        :type: bool
        """

        self._is_sub_same = is_sub_same

    @property
    def message_delay_time(self):
        """Gets the message_delay_time of this DescribeGroupsDetailResponse.  # noqa: E501


        :return: The message_delay_time of this DescribeGroupsDetailResponse.  # noqa: E501
        :rtype: str
        """
        return self._message_delay_time

    @message_delay_time.setter
    def message_delay_time(self, message_delay_time):
        """Sets the message_delay_time of this DescribeGroupsDetailResponse.


        :param message_delay_time: The message_delay_time of this DescribeGroupsDetailResponse.  # noqa: E501
        :type: str
        """

        self._message_delay_time = message_delay_time

    @property
    def message_model(self):
        """Gets the message_model of this DescribeGroupsDetailResponse.  # noqa: E501


        :return: The message_model of this DescribeGroupsDetailResponse.  # noqa: E501
        :rtype: str
        """
        return self._message_model

    @message_model.setter
    def message_model(self, message_model):
        """Sets the message_model of this DescribeGroupsDetailResponse.


        :param message_model: The message_model of this DescribeGroupsDetailResponse.  # noqa: E501
        :type: str
        """

        self._message_model = message_model

    @property
    def status(self):
        """Gets the status of this DescribeGroupsDetailResponse.  # noqa: E501


        :return: The status of this DescribeGroupsDetailResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DescribeGroupsDetailResponse.


        :param status: The status of this DescribeGroupsDetailResponse.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def total_consumed_rate(self):
        """Gets the total_consumed_rate of this DescribeGroupsDetailResponse.  # noqa: E501


        :return: The total_consumed_rate of this DescribeGroupsDetailResponse.  # noqa: E501
        :rtype: str
        """
        return self._total_consumed_rate

    @total_consumed_rate.setter
    def total_consumed_rate(self, total_consumed_rate):
        """Sets the total_consumed_rate of this DescribeGroupsDetailResponse.


        :param total_consumed_rate: The total_consumed_rate of this DescribeGroupsDetailResponse.  # noqa: E501
        :type: str
        """

        self._total_consumed_rate = total_consumed_rate

    @property
    def total_diff(self):
        """Gets the total_diff of this DescribeGroupsDetailResponse.  # noqa: E501


        :return: The total_diff of this DescribeGroupsDetailResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_diff

    @total_diff.setter
    def total_diff(self, total_diff):
        """Sets the total_diff of this DescribeGroupsDetailResponse.


        :param total_diff: The total_diff of this DescribeGroupsDetailResponse.  # noqa: E501
        :type: int
        """

        self._total_diff = total_diff

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
        if issubclass(DescribeGroupsDetailResponse, dict):
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
        if not isinstance(other, DescribeGroupsDetailResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeGroupsDetailResponse):
            return True

        return self.to_dict() != other.to_dict()