# coding: utf-8

"""
    waf

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class QueryFlowOverviewLbResponse(object):
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
        'back_source_count_peak': 'float',
        'back_source_qps_peak': 'float',
        'req_bandwidth_peak': 'float',
        'req_count_peak': 'float',
        'req_qps_peak': 'float'
    }

    attribute_map = {
        'back_source_count_peak': 'BackSourceCountPeak',
        'back_source_qps_peak': 'BackSourceQPSPeak',
        'req_bandwidth_peak': 'ReqBandwidthPeak',
        'req_count_peak': 'ReqCountPeak',
        'req_qps_peak': 'ReqQPSPeak'
    }

    def __init__(self, back_source_count_peak=None, back_source_qps_peak=None, req_bandwidth_peak=None, req_count_peak=None, req_qps_peak=None, _configuration=None):  # noqa: E501
        """QueryFlowOverviewLbResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._back_source_count_peak = None
        self._back_source_qps_peak = None
        self._req_bandwidth_peak = None
        self._req_count_peak = None
        self._req_qps_peak = None
        self.discriminator = None

        if back_source_count_peak is not None:
            self.back_source_count_peak = back_source_count_peak
        if back_source_qps_peak is not None:
            self.back_source_qps_peak = back_source_qps_peak
        if req_bandwidth_peak is not None:
            self.req_bandwidth_peak = req_bandwidth_peak
        if req_count_peak is not None:
            self.req_count_peak = req_count_peak
        if req_qps_peak is not None:
            self.req_qps_peak = req_qps_peak

    @property
    def back_source_count_peak(self):
        """Gets the back_source_count_peak of this QueryFlowOverviewLbResponse.  # noqa: E501


        :return: The back_source_count_peak of this QueryFlowOverviewLbResponse.  # noqa: E501
        :rtype: float
        """
        return self._back_source_count_peak

    @back_source_count_peak.setter
    def back_source_count_peak(self, back_source_count_peak):
        """Sets the back_source_count_peak of this QueryFlowOverviewLbResponse.


        :param back_source_count_peak: The back_source_count_peak of this QueryFlowOverviewLbResponse.  # noqa: E501
        :type: float
        """

        self._back_source_count_peak = back_source_count_peak

    @property
    def back_source_qps_peak(self):
        """Gets the back_source_qps_peak of this QueryFlowOverviewLbResponse.  # noqa: E501


        :return: The back_source_qps_peak of this QueryFlowOverviewLbResponse.  # noqa: E501
        :rtype: float
        """
        return self._back_source_qps_peak

    @back_source_qps_peak.setter
    def back_source_qps_peak(self, back_source_qps_peak):
        """Sets the back_source_qps_peak of this QueryFlowOverviewLbResponse.


        :param back_source_qps_peak: The back_source_qps_peak of this QueryFlowOverviewLbResponse.  # noqa: E501
        :type: float
        """

        self._back_source_qps_peak = back_source_qps_peak

    @property
    def req_bandwidth_peak(self):
        """Gets the req_bandwidth_peak of this QueryFlowOverviewLbResponse.  # noqa: E501


        :return: The req_bandwidth_peak of this QueryFlowOverviewLbResponse.  # noqa: E501
        :rtype: float
        """
        return self._req_bandwidth_peak

    @req_bandwidth_peak.setter
    def req_bandwidth_peak(self, req_bandwidth_peak):
        """Sets the req_bandwidth_peak of this QueryFlowOverviewLbResponse.


        :param req_bandwidth_peak: The req_bandwidth_peak of this QueryFlowOverviewLbResponse.  # noqa: E501
        :type: float
        """

        self._req_bandwidth_peak = req_bandwidth_peak

    @property
    def req_count_peak(self):
        """Gets the req_count_peak of this QueryFlowOverviewLbResponse.  # noqa: E501


        :return: The req_count_peak of this QueryFlowOverviewLbResponse.  # noqa: E501
        :rtype: float
        """
        return self._req_count_peak

    @req_count_peak.setter
    def req_count_peak(self, req_count_peak):
        """Sets the req_count_peak of this QueryFlowOverviewLbResponse.


        :param req_count_peak: The req_count_peak of this QueryFlowOverviewLbResponse.  # noqa: E501
        :type: float
        """

        self._req_count_peak = req_count_peak

    @property
    def req_qps_peak(self):
        """Gets the req_qps_peak of this QueryFlowOverviewLbResponse.  # noqa: E501


        :return: The req_qps_peak of this QueryFlowOverviewLbResponse.  # noqa: E501
        :rtype: float
        """
        return self._req_qps_peak

    @req_qps_peak.setter
    def req_qps_peak(self, req_qps_peak):
        """Sets the req_qps_peak of this QueryFlowOverviewLbResponse.


        :param req_qps_peak: The req_qps_peak of this QueryFlowOverviewLbResponse.  # noqa: E501
        :type: float
        """

        self._req_qps_peak = req_qps_peak

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
        if issubclass(QueryFlowOverviewLbResponse, dict):
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
        if not isinstance(other, QueryFlowOverviewLbResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QueryFlowOverviewLbResponse):
            return True

        return self.to_dict() != other.to_dict()