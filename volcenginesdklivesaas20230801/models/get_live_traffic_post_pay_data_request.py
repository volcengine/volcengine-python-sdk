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


class GetLiveTrafficPostPayDataRequest(object):
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
        'activity_creator': 'ActivityCreatorForGetLiveTrafficPostPayDataInput',
        'activity_ids': 'list[int]',
        'end_day': 'str',
        'start_day': 'str'
    }

    attribute_map = {
        'activity_creator': 'ActivityCreator',
        'activity_ids': 'ActivityIds',
        'end_day': 'EndDay',
        'start_day': 'StartDay'
    }

    def __init__(self, activity_creator=None, activity_ids=None, end_day=None, start_day=None, _configuration=None):  # noqa: E501
        """GetLiveTrafficPostPayDataRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._activity_creator = None
        self._activity_ids = None
        self._end_day = None
        self._start_day = None
        self.discriminator = None

        if activity_creator is not None:
            self.activity_creator = activity_creator
        if activity_ids is not None:
            self.activity_ids = activity_ids
        self.end_day = end_day
        self.start_day = start_day

    @property
    def activity_creator(self):
        """Gets the activity_creator of this GetLiveTrafficPostPayDataRequest.  # noqa: E501


        :return: The activity_creator of this GetLiveTrafficPostPayDataRequest.  # noqa: E501
        :rtype: ActivityCreatorForGetLiveTrafficPostPayDataInput
        """
        return self._activity_creator

    @activity_creator.setter
    def activity_creator(self, activity_creator):
        """Sets the activity_creator of this GetLiveTrafficPostPayDataRequest.


        :param activity_creator: The activity_creator of this GetLiveTrafficPostPayDataRequest.  # noqa: E501
        :type: ActivityCreatorForGetLiveTrafficPostPayDataInput
        """

        self._activity_creator = activity_creator

    @property
    def activity_ids(self):
        """Gets the activity_ids of this GetLiveTrafficPostPayDataRequest.  # noqa: E501


        :return: The activity_ids of this GetLiveTrafficPostPayDataRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._activity_ids

    @activity_ids.setter
    def activity_ids(self, activity_ids):
        """Sets the activity_ids of this GetLiveTrafficPostPayDataRequest.


        :param activity_ids: The activity_ids of this GetLiveTrafficPostPayDataRequest.  # noqa: E501
        :type: list[int]
        """

        self._activity_ids = activity_ids

    @property
    def end_day(self):
        """Gets the end_day of this GetLiveTrafficPostPayDataRequest.  # noqa: E501


        :return: The end_day of this GetLiveTrafficPostPayDataRequest.  # noqa: E501
        :rtype: str
        """
        return self._end_day

    @end_day.setter
    def end_day(self, end_day):
        """Sets the end_day of this GetLiveTrafficPostPayDataRequest.


        :param end_day: The end_day of this GetLiveTrafficPostPayDataRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and end_day is None:
            raise ValueError("Invalid value for `end_day`, must not be `None`")  # noqa: E501

        self._end_day = end_day

    @property
    def start_day(self):
        """Gets the start_day of this GetLiveTrafficPostPayDataRequest.  # noqa: E501


        :return: The start_day of this GetLiveTrafficPostPayDataRequest.  # noqa: E501
        :rtype: str
        """
        return self._start_day

    @start_day.setter
    def start_day(self, start_day):
        """Sets the start_day of this GetLiveTrafficPostPayDataRequest.


        :param start_day: The start_day of this GetLiveTrafficPostPayDataRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and start_day is None:
            raise ValueError("Invalid value for `start_day`, must not be `None`")  # noqa: E501

        self._start_day = start_day

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
        if issubclass(GetLiveTrafficPostPayDataRequest, dict):
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
        if not isinstance(other, GetLiveTrafficPostPayDataRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetLiveTrafficPostPayDataRequest):
            return True

        return self.to_dict() != other.to_dict()
