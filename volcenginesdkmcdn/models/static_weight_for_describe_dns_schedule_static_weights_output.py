# coding: utf-8

"""
    mcdn

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class StaticWeightForDescribeDnsScheduleStaticWeightsOutput(object):
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
        'country': 'str',
        'id': 'str',
        'isp': 'str',
        'province': 'str',
        'weight_items': 'list[WeightItemForDescribeDnsScheduleStaticWeightsOutput]'
    }

    attribute_map = {
        'country': 'Country',
        'id': 'Id',
        'isp': 'Isp',
        'province': 'Province',
        'weight_items': 'WeightItems'
    }

    def __init__(self, country=None, id=None, isp=None, province=None, weight_items=None, _configuration=None):  # noqa: E501
        """StaticWeightForDescribeDnsScheduleStaticWeightsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._country = None
        self._id = None
        self._isp = None
        self._province = None
        self._weight_items = None
        self.discriminator = None

        if country is not None:
            self.country = country
        if id is not None:
            self.id = id
        if isp is not None:
            self.isp = isp
        if province is not None:
            self.province = province
        if weight_items is not None:
            self.weight_items = weight_items

    @property
    def country(self):
        """Gets the country of this StaticWeightForDescribeDnsScheduleStaticWeightsOutput.  # noqa: E501


        :return: The country of this StaticWeightForDescribeDnsScheduleStaticWeightsOutput.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this StaticWeightForDescribeDnsScheduleStaticWeightsOutput.


        :param country: The country of this StaticWeightForDescribeDnsScheduleStaticWeightsOutput.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def id(self):
        """Gets the id of this StaticWeightForDescribeDnsScheduleStaticWeightsOutput.  # noqa: E501


        :return: The id of this StaticWeightForDescribeDnsScheduleStaticWeightsOutput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StaticWeightForDescribeDnsScheduleStaticWeightsOutput.


        :param id: The id of this StaticWeightForDescribeDnsScheduleStaticWeightsOutput.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def isp(self):
        """Gets the isp of this StaticWeightForDescribeDnsScheduleStaticWeightsOutput.  # noqa: E501


        :return: The isp of this StaticWeightForDescribeDnsScheduleStaticWeightsOutput.  # noqa: E501
        :rtype: str
        """
        return self._isp

    @isp.setter
    def isp(self, isp):
        """Sets the isp of this StaticWeightForDescribeDnsScheduleStaticWeightsOutput.


        :param isp: The isp of this StaticWeightForDescribeDnsScheduleStaticWeightsOutput.  # noqa: E501
        :type: str
        """

        self._isp = isp

    @property
    def province(self):
        """Gets the province of this StaticWeightForDescribeDnsScheduleStaticWeightsOutput.  # noqa: E501


        :return: The province of this StaticWeightForDescribeDnsScheduleStaticWeightsOutput.  # noqa: E501
        :rtype: str
        """
        return self._province

    @province.setter
    def province(self, province):
        """Sets the province of this StaticWeightForDescribeDnsScheduleStaticWeightsOutput.


        :param province: The province of this StaticWeightForDescribeDnsScheduleStaticWeightsOutput.  # noqa: E501
        :type: str
        """

        self._province = province

    @property
    def weight_items(self):
        """Gets the weight_items of this StaticWeightForDescribeDnsScheduleStaticWeightsOutput.  # noqa: E501


        :return: The weight_items of this StaticWeightForDescribeDnsScheduleStaticWeightsOutput.  # noqa: E501
        :rtype: list[WeightItemForDescribeDnsScheduleStaticWeightsOutput]
        """
        return self._weight_items

    @weight_items.setter
    def weight_items(self, weight_items):
        """Sets the weight_items of this StaticWeightForDescribeDnsScheduleStaticWeightsOutput.


        :param weight_items: The weight_items of this StaticWeightForDescribeDnsScheduleStaticWeightsOutput.  # noqa: E501
        :type: list[WeightItemForDescribeDnsScheduleStaticWeightsOutput]
        """

        self._weight_items = weight_items

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
        if issubclass(StaticWeightForDescribeDnsScheduleStaticWeightsOutput, dict):
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
        if not isinstance(other, StaticWeightForDescribeDnsScheduleStaticWeightsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StaticWeightForDescribeDnsScheduleStaticWeightsOutput):
            return True

        return self.to_dict() != other.to_dict()