# coding: utf-8

"""
    advdefence

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescCertificateResponse(object):
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
        'count': 'int',
        'other_cert_list': 'list[OtherCertListForDescCertificateOutput]',
        'recommend_cert_list': 'list[RecommendCertListForDescCertificateOutput]'
    }

    attribute_map = {
        'count': 'Count',
        'other_cert_list': 'OtherCertList',
        'recommend_cert_list': 'RecommendCertList'
    }

    def __init__(self, count=None, other_cert_list=None, recommend_cert_list=None, _configuration=None):  # noqa: E501
        """DescCertificateResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._count = None
        self._other_cert_list = None
        self._recommend_cert_list = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if other_cert_list is not None:
            self.other_cert_list = other_cert_list
        if recommend_cert_list is not None:
            self.recommend_cert_list = recommend_cert_list

    @property
    def count(self):
        """Gets the count of this DescCertificateResponse.  # noqa: E501


        :return: The count of this DescCertificateResponse.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this DescCertificateResponse.


        :param count: The count of this DescCertificateResponse.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def other_cert_list(self):
        """Gets the other_cert_list of this DescCertificateResponse.  # noqa: E501


        :return: The other_cert_list of this DescCertificateResponse.  # noqa: E501
        :rtype: list[OtherCertListForDescCertificateOutput]
        """
        return self._other_cert_list

    @other_cert_list.setter
    def other_cert_list(self, other_cert_list):
        """Sets the other_cert_list of this DescCertificateResponse.


        :param other_cert_list: The other_cert_list of this DescCertificateResponse.  # noqa: E501
        :type: list[OtherCertListForDescCertificateOutput]
        """

        self._other_cert_list = other_cert_list

    @property
    def recommend_cert_list(self):
        """Gets the recommend_cert_list of this DescCertificateResponse.  # noqa: E501


        :return: The recommend_cert_list of this DescCertificateResponse.  # noqa: E501
        :rtype: list[RecommendCertListForDescCertificateOutput]
        """
        return self._recommend_cert_list

    @recommend_cert_list.setter
    def recommend_cert_list(self, recommend_cert_list):
        """Sets the recommend_cert_list of this DescCertificateResponse.


        :param recommend_cert_list: The recommend_cert_list of this DescCertificateResponse.  # noqa: E501
        :type: list[RecommendCertListForDescCertificateOutput]
        """

        self._recommend_cert_list = recommend_cert_list

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
        if issubclass(DescCertificateResponse, dict):
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
        if not isinstance(other, DescCertificateResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescCertificateResponse):
            return True

        return self.to_dict() != other.to_dict()
