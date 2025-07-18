# coding: utf-8

"""
    aiotvideo

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class AlertNotificationForGetDeviceOutput(object):
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
        'device': 'bool',
        'device_fault': 'bool',
        'enabled': 'bool',
        'gps': 'bool',
        'other': 'bool',
        'phone': 'bool',
        'sms': 'bool',
        'video': 'bool'
    }

    attribute_map = {
        'device': 'Device',
        'device_fault': 'DeviceFault',
        'enabled': 'Enabled',
        'gps': 'GPS',
        'other': 'Other',
        'phone': 'Phone',
        'sms': 'SMS',
        'video': 'Video'
    }

    def __init__(self, device=None, device_fault=None, enabled=None, gps=None, other=None, phone=None, sms=None, video=None, _configuration=None):  # noqa: E501
        """AlertNotificationForGetDeviceOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._device = None
        self._device_fault = None
        self._enabled = None
        self._gps = None
        self._other = None
        self._phone = None
        self._sms = None
        self._video = None
        self.discriminator = None

        if device is not None:
            self.device = device
        if device_fault is not None:
            self.device_fault = device_fault
        if enabled is not None:
            self.enabled = enabled
        if gps is not None:
            self.gps = gps
        if other is not None:
            self.other = other
        if phone is not None:
            self.phone = phone
        if sms is not None:
            self.sms = sms
        if video is not None:
            self.video = video

    @property
    def device(self):
        """Gets the device of this AlertNotificationForGetDeviceOutput.  # noqa: E501


        :return: The device of this AlertNotificationForGetDeviceOutput.  # noqa: E501
        :rtype: bool
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this AlertNotificationForGetDeviceOutput.


        :param device: The device of this AlertNotificationForGetDeviceOutput.  # noqa: E501
        :type: bool
        """

        self._device = device

    @property
    def device_fault(self):
        """Gets the device_fault of this AlertNotificationForGetDeviceOutput.  # noqa: E501


        :return: The device_fault of this AlertNotificationForGetDeviceOutput.  # noqa: E501
        :rtype: bool
        """
        return self._device_fault

    @device_fault.setter
    def device_fault(self, device_fault):
        """Sets the device_fault of this AlertNotificationForGetDeviceOutput.


        :param device_fault: The device_fault of this AlertNotificationForGetDeviceOutput.  # noqa: E501
        :type: bool
        """

        self._device_fault = device_fault

    @property
    def enabled(self):
        """Gets the enabled of this AlertNotificationForGetDeviceOutput.  # noqa: E501


        :return: The enabled of this AlertNotificationForGetDeviceOutput.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this AlertNotificationForGetDeviceOutput.


        :param enabled: The enabled of this AlertNotificationForGetDeviceOutput.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def gps(self):
        """Gets the gps of this AlertNotificationForGetDeviceOutput.  # noqa: E501


        :return: The gps of this AlertNotificationForGetDeviceOutput.  # noqa: E501
        :rtype: bool
        """
        return self._gps

    @gps.setter
    def gps(self, gps):
        """Sets the gps of this AlertNotificationForGetDeviceOutput.


        :param gps: The gps of this AlertNotificationForGetDeviceOutput.  # noqa: E501
        :type: bool
        """

        self._gps = gps

    @property
    def other(self):
        """Gets the other of this AlertNotificationForGetDeviceOutput.  # noqa: E501


        :return: The other of this AlertNotificationForGetDeviceOutput.  # noqa: E501
        :rtype: bool
        """
        return self._other

    @other.setter
    def other(self, other):
        """Sets the other of this AlertNotificationForGetDeviceOutput.


        :param other: The other of this AlertNotificationForGetDeviceOutput.  # noqa: E501
        :type: bool
        """

        self._other = other

    @property
    def phone(self):
        """Gets the phone of this AlertNotificationForGetDeviceOutput.  # noqa: E501


        :return: The phone of this AlertNotificationForGetDeviceOutput.  # noqa: E501
        :rtype: bool
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this AlertNotificationForGetDeviceOutput.


        :param phone: The phone of this AlertNotificationForGetDeviceOutput.  # noqa: E501
        :type: bool
        """

        self._phone = phone

    @property
    def sms(self):
        """Gets the sms of this AlertNotificationForGetDeviceOutput.  # noqa: E501


        :return: The sms of this AlertNotificationForGetDeviceOutput.  # noqa: E501
        :rtype: bool
        """
        return self._sms

    @sms.setter
    def sms(self, sms):
        """Sets the sms of this AlertNotificationForGetDeviceOutput.


        :param sms: The sms of this AlertNotificationForGetDeviceOutput.  # noqa: E501
        :type: bool
        """

        self._sms = sms

    @property
    def video(self):
        """Gets the video of this AlertNotificationForGetDeviceOutput.  # noqa: E501


        :return: The video of this AlertNotificationForGetDeviceOutput.  # noqa: E501
        :rtype: bool
        """
        return self._video

    @video.setter
    def video(self, video):
        """Sets the video of this AlertNotificationForGetDeviceOutput.


        :param video: The video of this AlertNotificationForGetDeviceOutput.  # noqa: E501
        :type: bool
        """

        self._video = video

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
        if issubclass(AlertNotificationForGetDeviceOutput, dict):
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
        if not isinstance(other, AlertNotificationForGetDeviceOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AlertNotificationForGetDeviceOutput):
            return True

        return self.to_dict() != other.to_dict()
