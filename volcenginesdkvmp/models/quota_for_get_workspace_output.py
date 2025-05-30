# coding: utf-8

"""
    vmp

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class QuotaForGetWorkspaceOutput(object):
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
        'active_series': 'int',
        'ingest_samples_per_second': 'int',
        'query_per_second': 'int',
        'scan_samples_per_second': 'int',
        'scan_series_per_second': 'int'
    }

    attribute_map = {
        'active_series': 'ActiveSeries',
        'ingest_samples_per_second': 'IngestSamplesPerSecond',
        'query_per_second': 'QueryPerSecond',
        'scan_samples_per_second': 'ScanSamplesPerSecond',
        'scan_series_per_second': 'ScanSeriesPerSecond'
    }

    def __init__(self, active_series=None, ingest_samples_per_second=None, query_per_second=None, scan_samples_per_second=None, scan_series_per_second=None, _configuration=None):  # noqa: E501
        """QuotaForGetWorkspaceOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._active_series = None
        self._ingest_samples_per_second = None
        self._query_per_second = None
        self._scan_samples_per_second = None
        self._scan_series_per_second = None
        self.discriminator = None

        if active_series is not None:
            self.active_series = active_series
        if ingest_samples_per_second is not None:
            self.ingest_samples_per_second = ingest_samples_per_second
        if query_per_second is not None:
            self.query_per_second = query_per_second
        if scan_samples_per_second is not None:
            self.scan_samples_per_second = scan_samples_per_second
        if scan_series_per_second is not None:
            self.scan_series_per_second = scan_series_per_second

    @property
    def active_series(self):
        """Gets the active_series of this QuotaForGetWorkspaceOutput.  # noqa: E501


        :return: The active_series of this QuotaForGetWorkspaceOutput.  # noqa: E501
        :rtype: int
        """
        return self._active_series

    @active_series.setter
    def active_series(self, active_series):
        """Sets the active_series of this QuotaForGetWorkspaceOutput.


        :param active_series: The active_series of this QuotaForGetWorkspaceOutput.  # noqa: E501
        :type: int
        """

        self._active_series = active_series

    @property
    def ingest_samples_per_second(self):
        """Gets the ingest_samples_per_second of this QuotaForGetWorkspaceOutput.  # noqa: E501


        :return: The ingest_samples_per_second of this QuotaForGetWorkspaceOutput.  # noqa: E501
        :rtype: int
        """
        return self._ingest_samples_per_second

    @ingest_samples_per_second.setter
    def ingest_samples_per_second(self, ingest_samples_per_second):
        """Sets the ingest_samples_per_second of this QuotaForGetWorkspaceOutput.


        :param ingest_samples_per_second: The ingest_samples_per_second of this QuotaForGetWorkspaceOutput.  # noqa: E501
        :type: int
        """

        self._ingest_samples_per_second = ingest_samples_per_second

    @property
    def query_per_second(self):
        """Gets the query_per_second of this QuotaForGetWorkspaceOutput.  # noqa: E501


        :return: The query_per_second of this QuotaForGetWorkspaceOutput.  # noqa: E501
        :rtype: int
        """
        return self._query_per_second

    @query_per_second.setter
    def query_per_second(self, query_per_second):
        """Sets the query_per_second of this QuotaForGetWorkspaceOutput.


        :param query_per_second: The query_per_second of this QuotaForGetWorkspaceOutput.  # noqa: E501
        :type: int
        """

        self._query_per_second = query_per_second

    @property
    def scan_samples_per_second(self):
        """Gets the scan_samples_per_second of this QuotaForGetWorkspaceOutput.  # noqa: E501


        :return: The scan_samples_per_second of this QuotaForGetWorkspaceOutput.  # noqa: E501
        :rtype: int
        """
        return self._scan_samples_per_second

    @scan_samples_per_second.setter
    def scan_samples_per_second(self, scan_samples_per_second):
        """Sets the scan_samples_per_second of this QuotaForGetWorkspaceOutput.


        :param scan_samples_per_second: The scan_samples_per_second of this QuotaForGetWorkspaceOutput.  # noqa: E501
        :type: int
        """

        self._scan_samples_per_second = scan_samples_per_second

    @property
    def scan_series_per_second(self):
        """Gets the scan_series_per_second of this QuotaForGetWorkspaceOutput.  # noqa: E501


        :return: The scan_series_per_second of this QuotaForGetWorkspaceOutput.  # noqa: E501
        :rtype: int
        """
        return self._scan_series_per_second

    @scan_series_per_second.setter
    def scan_series_per_second(self, scan_series_per_second):
        """Sets the scan_series_per_second of this QuotaForGetWorkspaceOutput.


        :param scan_series_per_second: The scan_series_per_second of this QuotaForGetWorkspaceOutput.  # noqa: E501
        :type: int
        """

        self._scan_series_per_second = scan_series_per_second

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
        if issubclass(QuotaForGetWorkspaceOutput, dict):
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
        if not isinstance(other, QuotaForGetWorkspaceOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QuotaForGetWorkspaceOutput):
            return True

        return self.to_dict() != other.to_dict()
