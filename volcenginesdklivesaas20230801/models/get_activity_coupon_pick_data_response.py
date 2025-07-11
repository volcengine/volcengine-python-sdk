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


class GetActivityCouponPickDataResponse(object):
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
        'activity_coupon_pick_data': 'list[ActivityCouponPickDataForGetActivityCouponPickDataOutput]',
        'coupon_id': 'int',
        'id': 'int',
        'name': 'str',
        'send_time': 'int',
        'third_party_id': 'str',
        'total_count': 'int'
    }

    attribute_map = {
        'activity_coupon_pick_data': 'ActivityCouponPickData',
        'coupon_id': 'CouponId',
        'id': 'Id',
        'name': 'Name',
        'send_time': 'SendTime',
        'third_party_id': 'ThirdPartyId',
        'total_count': 'TotalCount'
    }

    def __init__(self, activity_coupon_pick_data=None, coupon_id=None, id=None, name=None, send_time=None, third_party_id=None, total_count=None, _configuration=None):  # noqa: E501
        """GetActivityCouponPickDataResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._activity_coupon_pick_data = None
        self._coupon_id = None
        self._id = None
        self._name = None
        self._send_time = None
        self._third_party_id = None
        self._total_count = None
        self.discriminator = None

        if activity_coupon_pick_data is not None:
            self.activity_coupon_pick_data = activity_coupon_pick_data
        if coupon_id is not None:
            self.coupon_id = coupon_id
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if send_time is not None:
            self.send_time = send_time
        if third_party_id is not None:
            self.third_party_id = third_party_id
        if total_count is not None:
            self.total_count = total_count

    @property
    def activity_coupon_pick_data(self):
        """Gets the activity_coupon_pick_data of this GetActivityCouponPickDataResponse.  # noqa: E501


        :return: The activity_coupon_pick_data of this GetActivityCouponPickDataResponse.  # noqa: E501
        :rtype: list[ActivityCouponPickDataForGetActivityCouponPickDataOutput]
        """
        return self._activity_coupon_pick_data

    @activity_coupon_pick_data.setter
    def activity_coupon_pick_data(self, activity_coupon_pick_data):
        """Sets the activity_coupon_pick_data of this GetActivityCouponPickDataResponse.


        :param activity_coupon_pick_data: The activity_coupon_pick_data of this GetActivityCouponPickDataResponse.  # noqa: E501
        :type: list[ActivityCouponPickDataForGetActivityCouponPickDataOutput]
        """

        self._activity_coupon_pick_data = activity_coupon_pick_data

    @property
    def coupon_id(self):
        """Gets the coupon_id of this GetActivityCouponPickDataResponse.  # noqa: E501


        :return: The coupon_id of this GetActivityCouponPickDataResponse.  # noqa: E501
        :rtype: int
        """
        return self._coupon_id

    @coupon_id.setter
    def coupon_id(self, coupon_id):
        """Sets the coupon_id of this GetActivityCouponPickDataResponse.


        :param coupon_id: The coupon_id of this GetActivityCouponPickDataResponse.  # noqa: E501
        :type: int
        """

        self._coupon_id = coupon_id

    @property
    def id(self):
        """Gets the id of this GetActivityCouponPickDataResponse.  # noqa: E501


        :return: The id of this GetActivityCouponPickDataResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetActivityCouponPickDataResponse.


        :param id: The id of this GetActivityCouponPickDataResponse.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this GetActivityCouponPickDataResponse.  # noqa: E501


        :return: The name of this GetActivityCouponPickDataResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetActivityCouponPickDataResponse.


        :param name: The name of this GetActivityCouponPickDataResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def send_time(self):
        """Gets the send_time of this GetActivityCouponPickDataResponse.  # noqa: E501


        :return: The send_time of this GetActivityCouponPickDataResponse.  # noqa: E501
        :rtype: int
        """
        return self._send_time

    @send_time.setter
    def send_time(self, send_time):
        """Sets the send_time of this GetActivityCouponPickDataResponse.


        :param send_time: The send_time of this GetActivityCouponPickDataResponse.  # noqa: E501
        :type: int
        """

        self._send_time = send_time

    @property
    def third_party_id(self):
        """Gets the third_party_id of this GetActivityCouponPickDataResponse.  # noqa: E501


        :return: The third_party_id of this GetActivityCouponPickDataResponse.  # noqa: E501
        :rtype: str
        """
        return self._third_party_id

    @third_party_id.setter
    def third_party_id(self, third_party_id):
        """Sets the third_party_id of this GetActivityCouponPickDataResponse.


        :param third_party_id: The third_party_id of this GetActivityCouponPickDataResponse.  # noqa: E501
        :type: str
        """

        self._third_party_id = third_party_id

    @property
    def total_count(self):
        """Gets the total_count of this GetActivityCouponPickDataResponse.  # noqa: E501


        :return: The total_count of this GetActivityCouponPickDataResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this GetActivityCouponPickDataResponse.


        :param total_count: The total_count of this GetActivityCouponPickDataResponse.  # noqa: E501
        :type: int
        """

        self._total_count = total_count

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
        if issubclass(GetActivityCouponPickDataResponse, dict):
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
        if not isinstance(other, GetActivityCouponPickDataResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetActivityCouponPickDataResponse):
            return True

        return self.to_dict() != other.to_dict()
