# coding: utf-8

"""
    transitrouter

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class RegionForDescribeTransitRouterRegionsOutput(object):
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
        'geographic_region_set_id': 'str',
        'region_id': 'str',
        'region_name': 'str',
        'region_type': 'str'
    }

    attribute_map = {
        'geographic_region_set_id': 'GeographicRegionSetId',
        'region_id': 'RegionId',
        'region_name': 'RegionName',
        'region_type': 'RegionType'
    }

    def __init__(self, geographic_region_set_id=None, region_id=None, region_name=None, region_type=None, _configuration=None):  # noqa: E501
        """RegionForDescribeTransitRouterRegionsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._geographic_region_set_id = None
        self._region_id = None
        self._region_name = None
        self._region_type = None
        self.discriminator = None

        if geographic_region_set_id is not None:
            self.geographic_region_set_id = geographic_region_set_id
        if region_id is not None:
            self.region_id = region_id
        if region_name is not None:
            self.region_name = region_name
        if region_type is not None:
            self.region_type = region_type

    @property
    def geographic_region_set_id(self):
        """Gets the geographic_region_set_id of this RegionForDescribeTransitRouterRegionsOutput.  # noqa: E501


        :return: The geographic_region_set_id of this RegionForDescribeTransitRouterRegionsOutput.  # noqa: E501
        :rtype: str
        """
        return self._geographic_region_set_id

    @geographic_region_set_id.setter
    def geographic_region_set_id(self, geographic_region_set_id):
        """Sets the geographic_region_set_id of this RegionForDescribeTransitRouterRegionsOutput.


        :param geographic_region_set_id: The geographic_region_set_id of this RegionForDescribeTransitRouterRegionsOutput.  # noqa: E501
        :type: str
        """

        self._geographic_region_set_id = geographic_region_set_id

    @property
    def region_id(self):
        """Gets the region_id of this RegionForDescribeTransitRouterRegionsOutput.  # noqa: E501


        :return: The region_id of this RegionForDescribeTransitRouterRegionsOutput.  # noqa: E501
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this RegionForDescribeTransitRouterRegionsOutput.


        :param region_id: The region_id of this RegionForDescribeTransitRouterRegionsOutput.  # noqa: E501
        :type: str
        """

        self._region_id = region_id

    @property
    def region_name(self):
        """Gets the region_name of this RegionForDescribeTransitRouterRegionsOutput.  # noqa: E501


        :return: The region_name of this RegionForDescribeTransitRouterRegionsOutput.  # noqa: E501
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        """Sets the region_name of this RegionForDescribeTransitRouterRegionsOutput.


        :param region_name: The region_name of this RegionForDescribeTransitRouterRegionsOutput.  # noqa: E501
        :type: str
        """

        self._region_name = region_name

    @property
    def region_type(self):
        """Gets the region_type of this RegionForDescribeTransitRouterRegionsOutput.  # noqa: E501


        :return: The region_type of this RegionForDescribeTransitRouterRegionsOutput.  # noqa: E501
        :rtype: str
        """
        return self._region_type

    @region_type.setter
    def region_type(self, region_type):
        """Sets the region_type of this RegionForDescribeTransitRouterRegionsOutput.


        :param region_type: The region_type of this RegionForDescribeTransitRouterRegionsOutput.  # noqa: E501
        :type: str
        """

        self._region_type = region_type

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
        if issubclass(RegionForDescribeTransitRouterRegionsOutput, dict):
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
        if not isinstance(other, RegionForDescribeTransitRouterRegionsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RegionForDescribeTransitRouterRegionsOutput):
            return True

        return self.to_dict() != other.to_dict()
