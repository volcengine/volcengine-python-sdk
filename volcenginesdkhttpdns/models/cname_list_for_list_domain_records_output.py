# coding: utf-8

"""
    httpdns

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class CnameListForListDomainRecordsOutput(object):
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
        'line': 'str',
        'records': 'list[RecordForListDomainRecordsOutput]'
    }

    attribute_map = {
        'line': 'Line',
        'records': 'Records'
    }

    def __init__(self, line=None, records=None, _configuration=None):  # noqa: E501
        """CnameListForListDomainRecordsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._line = None
        self._records = None
        self.discriminator = None

        if line is not None:
            self.line = line
        if records is not None:
            self.records = records

    @property
    def line(self):
        """Gets the line of this CnameListForListDomainRecordsOutput.  # noqa: E501


        :return: The line of this CnameListForListDomainRecordsOutput.  # noqa: E501
        :rtype: str
        """
        return self._line

    @line.setter
    def line(self, line):
        """Sets the line of this CnameListForListDomainRecordsOutput.


        :param line: The line of this CnameListForListDomainRecordsOutput.  # noqa: E501
        :type: str
        """

        self._line = line

    @property
    def records(self):
        """Gets the records of this CnameListForListDomainRecordsOutput.  # noqa: E501


        :return: The records of this CnameListForListDomainRecordsOutput.  # noqa: E501
        :rtype: list[RecordForListDomainRecordsOutput]
        """
        return self._records

    @records.setter
    def records(self, records):
        """Sets the records of this CnameListForListDomainRecordsOutput.


        :param records: The records of this CnameListForListDomainRecordsOutput.  # noqa: E501
        :type: list[RecordForListDomainRecordsOutput]
        """

        self._records = records

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
        if issubclass(CnameListForListDomainRecordsOutput, dict):
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
        if not isinstance(other, CnameListForListDomainRecordsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CnameListForListDomainRecordsOutput):
            return True

        return self.to_dict() != other.to_dict()
