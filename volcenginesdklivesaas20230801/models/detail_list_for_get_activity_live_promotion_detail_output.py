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


class DetailListForGetActivityLivePromotionDetailOutput(object):
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
        'platform_name': 'str',
        'platform_type': 'str',
        'push_end_time': 'int',
        'push_start_time': 'int',
        'push_status': 'int',
        'use_app_template': 'bool'
    }

    attribute_map = {
        'platform_name': 'PlatformName',
        'platform_type': 'PlatformType',
        'push_end_time': 'PushEndTime',
        'push_start_time': 'PushStartTime',
        'push_status': 'PushStatus',
        'use_app_template': 'UseAppTemplate'
    }

    def __init__(self, platform_name=None, platform_type=None, push_end_time=None, push_start_time=None, push_status=None, use_app_template=None, _configuration=None):  # noqa: E501
        """DetailListForGetActivityLivePromotionDetailOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._platform_name = None
        self._platform_type = None
        self._push_end_time = None
        self._push_start_time = None
        self._push_status = None
        self._use_app_template = None
        self.discriminator = None

        if platform_name is not None:
            self.platform_name = platform_name
        if platform_type is not None:
            self.platform_type = platform_type
        if push_end_time is not None:
            self.push_end_time = push_end_time
        if push_start_time is not None:
            self.push_start_time = push_start_time
        if push_status is not None:
            self.push_status = push_status
        if use_app_template is not None:
            self.use_app_template = use_app_template

    @property
    def platform_name(self):
        """Gets the platform_name of this DetailListForGetActivityLivePromotionDetailOutput.  # noqa: E501


        :return: The platform_name of this DetailListForGetActivityLivePromotionDetailOutput.  # noqa: E501
        :rtype: str
        """
        return self._platform_name

    @platform_name.setter
    def platform_name(self, platform_name):
        """Sets the platform_name of this DetailListForGetActivityLivePromotionDetailOutput.


        :param platform_name: The platform_name of this DetailListForGetActivityLivePromotionDetailOutput.  # noqa: E501
        :type: str
        """

        self._platform_name = platform_name

    @property
    def platform_type(self):
        """Gets the platform_type of this DetailListForGetActivityLivePromotionDetailOutput.  # noqa: E501


        :return: The platform_type of this DetailListForGetActivityLivePromotionDetailOutput.  # noqa: E501
        :rtype: str
        """
        return self._platform_type

    @platform_type.setter
    def platform_type(self, platform_type):
        """Sets the platform_type of this DetailListForGetActivityLivePromotionDetailOutput.


        :param platform_type: The platform_type of this DetailListForGetActivityLivePromotionDetailOutput.  # noqa: E501
        :type: str
        """

        self._platform_type = platform_type

    @property
    def push_end_time(self):
        """Gets the push_end_time of this DetailListForGetActivityLivePromotionDetailOutput.  # noqa: E501


        :return: The push_end_time of this DetailListForGetActivityLivePromotionDetailOutput.  # noqa: E501
        :rtype: int
        """
        return self._push_end_time

    @push_end_time.setter
    def push_end_time(self, push_end_time):
        """Sets the push_end_time of this DetailListForGetActivityLivePromotionDetailOutput.


        :param push_end_time: The push_end_time of this DetailListForGetActivityLivePromotionDetailOutput.  # noqa: E501
        :type: int
        """

        self._push_end_time = push_end_time

    @property
    def push_start_time(self):
        """Gets the push_start_time of this DetailListForGetActivityLivePromotionDetailOutput.  # noqa: E501


        :return: The push_start_time of this DetailListForGetActivityLivePromotionDetailOutput.  # noqa: E501
        :rtype: int
        """
        return self._push_start_time

    @push_start_time.setter
    def push_start_time(self, push_start_time):
        """Sets the push_start_time of this DetailListForGetActivityLivePromotionDetailOutput.


        :param push_start_time: The push_start_time of this DetailListForGetActivityLivePromotionDetailOutput.  # noqa: E501
        :type: int
        """

        self._push_start_time = push_start_time

    @property
    def push_status(self):
        """Gets the push_status of this DetailListForGetActivityLivePromotionDetailOutput.  # noqa: E501


        :return: The push_status of this DetailListForGetActivityLivePromotionDetailOutput.  # noqa: E501
        :rtype: int
        """
        return self._push_status

    @push_status.setter
    def push_status(self, push_status):
        """Sets the push_status of this DetailListForGetActivityLivePromotionDetailOutput.


        :param push_status: The push_status of this DetailListForGetActivityLivePromotionDetailOutput.  # noqa: E501
        :type: int
        """

        self._push_status = push_status

    @property
    def use_app_template(self):
        """Gets the use_app_template of this DetailListForGetActivityLivePromotionDetailOutput.  # noqa: E501


        :return: The use_app_template of this DetailListForGetActivityLivePromotionDetailOutput.  # noqa: E501
        :rtype: bool
        """
        return self._use_app_template

    @use_app_template.setter
    def use_app_template(self, use_app_template):
        """Sets the use_app_template of this DetailListForGetActivityLivePromotionDetailOutput.


        :param use_app_template: The use_app_template of this DetailListForGetActivityLivePromotionDetailOutput.  # noqa: E501
        :type: bool
        """

        self._use_app_template = use_app_template

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
        if issubclass(DetailListForGetActivityLivePromotionDetailOutput, dict):
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
        if not isinstance(other, DetailListForGetActivityLivePromotionDetailOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DetailListForGetActivityLivePromotionDetailOutput):
            return True

        return self.to_dict() != other.to_dict()
