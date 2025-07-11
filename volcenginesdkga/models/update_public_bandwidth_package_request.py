# coding: utf-8

"""
    ga

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class UpdatePublicBandwidthPackageRequest(object):
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
        'bandwidth_package_id': 'str',
        'project_name': 'str',
        'volume': 'int'
    }

    attribute_map = {
        'bandwidth_package_id': 'BandwidthPackageId',
        'project_name': 'ProjectName',
        'volume': 'Volume'
    }

    def __init__(self, bandwidth_package_id=None, project_name=None, volume=None, _configuration=None):  # noqa: E501
        """UpdatePublicBandwidthPackageRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bandwidth_package_id = None
        self._project_name = None
        self._volume = None
        self.discriminator = None

        self.bandwidth_package_id = bandwidth_package_id
        if project_name is not None:
            self.project_name = project_name
        if volume is not None:
            self.volume = volume

    @property
    def bandwidth_package_id(self):
        """Gets the bandwidth_package_id of this UpdatePublicBandwidthPackageRequest.  # noqa: E501


        :return: The bandwidth_package_id of this UpdatePublicBandwidthPackageRequest.  # noqa: E501
        :rtype: str
        """
        return self._bandwidth_package_id

    @bandwidth_package_id.setter
    def bandwidth_package_id(self, bandwidth_package_id):
        """Sets the bandwidth_package_id of this UpdatePublicBandwidthPackageRequest.


        :param bandwidth_package_id: The bandwidth_package_id of this UpdatePublicBandwidthPackageRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and bandwidth_package_id is None:
            raise ValueError("Invalid value for `bandwidth_package_id`, must not be `None`")  # noqa: E501

        self._bandwidth_package_id = bandwidth_package_id

    @property
    def project_name(self):
        """Gets the project_name of this UpdatePublicBandwidthPackageRequest.  # noqa: E501


        :return: The project_name of this UpdatePublicBandwidthPackageRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this UpdatePublicBandwidthPackageRequest.


        :param project_name: The project_name of this UpdatePublicBandwidthPackageRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def volume(self):
        """Gets the volume of this UpdatePublicBandwidthPackageRequest.  # noqa: E501


        :return: The volume of this UpdatePublicBandwidthPackageRequest.  # noqa: E501
        :rtype: int
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this UpdatePublicBandwidthPackageRequest.


        :param volume: The volume of this UpdatePublicBandwidthPackageRequest.  # noqa: E501
        :type: int
        """

        self._volume = volume

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
        if issubclass(UpdatePublicBandwidthPackageRequest, dict):
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
        if not isinstance(other, UpdatePublicBandwidthPackageRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdatePublicBandwidthPackageRequest):
            return True

        return self.to_dict() != other.to_dict()
