# coding: utf-8

"""
    cloud_detect

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class UDPDetailForGetTaskResultOutput(object):
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
        'diagnose_detail': 'DiagnoseDetailForGetTaskResultOutput',
        'udp_response': 'str',
        'udp_time_dns': 'int',
        'udp_time_receive': 'int',
        'udp_time_total': 'int',
        'udp_time_wait': 'int'
    }

    attribute_map = {
        'diagnose_detail': 'DiagnoseDetail',
        'udp_response': 'UDPResponse',
        'udp_time_dns': 'UDPTimeDNS',
        'udp_time_receive': 'UDPTimeReceive',
        'udp_time_total': 'UDPTimeTotal',
        'udp_time_wait': 'UDPTimeWait'
    }

    def __init__(self, diagnose_detail=None, udp_response=None, udp_time_dns=None, udp_time_receive=None, udp_time_total=None, udp_time_wait=None, _configuration=None):  # noqa: E501
        """UDPDetailForGetTaskResultOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._diagnose_detail = None
        self._udp_response = None
        self._udp_time_dns = None
        self._udp_time_receive = None
        self._udp_time_total = None
        self._udp_time_wait = None
        self.discriminator = None

        if diagnose_detail is not None:
            self.diagnose_detail = diagnose_detail
        if udp_response is not None:
            self.udp_response = udp_response
        if udp_time_dns is not None:
            self.udp_time_dns = udp_time_dns
        if udp_time_receive is not None:
            self.udp_time_receive = udp_time_receive
        if udp_time_total is not None:
            self.udp_time_total = udp_time_total
        if udp_time_wait is not None:
            self.udp_time_wait = udp_time_wait

    @property
    def diagnose_detail(self):
        """Gets the diagnose_detail of this UDPDetailForGetTaskResultOutput.  # noqa: E501


        :return: The diagnose_detail of this UDPDetailForGetTaskResultOutput.  # noqa: E501
        :rtype: DiagnoseDetailForGetTaskResultOutput
        """
        return self._diagnose_detail

    @diagnose_detail.setter
    def diagnose_detail(self, diagnose_detail):
        """Sets the diagnose_detail of this UDPDetailForGetTaskResultOutput.


        :param diagnose_detail: The diagnose_detail of this UDPDetailForGetTaskResultOutput.  # noqa: E501
        :type: DiagnoseDetailForGetTaskResultOutput
        """

        self._diagnose_detail = diagnose_detail

    @property
    def udp_response(self):
        """Gets the udp_response of this UDPDetailForGetTaskResultOutput.  # noqa: E501


        :return: The udp_response of this UDPDetailForGetTaskResultOutput.  # noqa: E501
        :rtype: str
        """
        return self._udp_response

    @udp_response.setter
    def udp_response(self, udp_response):
        """Sets the udp_response of this UDPDetailForGetTaskResultOutput.


        :param udp_response: The udp_response of this UDPDetailForGetTaskResultOutput.  # noqa: E501
        :type: str
        """

        self._udp_response = udp_response

    @property
    def udp_time_dns(self):
        """Gets the udp_time_dns of this UDPDetailForGetTaskResultOutput.  # noqa: E501


        :return: The udp_time_dns of this UDPDetailForGetTaskResultOutput.  # noqa: E501
        :rtype: int
        """
        return self._udp_time_dns

    @udp_time_dns.setter
    def udp_time_dns(self, udp_time_dns):
        """Sets the udp_time_dns of this UDPDetailForGetTaskResultOutput.


        :param udp_time_dns: The udp_time_dns of this UDPDetailForGetTaskResultOutput.  # noqa: E501
        :type: int
        """

        self._udp_time_dns = udp_time_dns

    @property
    def udp_time_receive(self):
        """Gets the udp_time_receive of this UDPDetailForGetTaskResultOutput.  # noqa: E501


        :return: The udp_time_receive of this UDPDetailForGetTaskResultOutput.  # noqa: E501
        :rtype: int
        """
        return self._udp_time_receive

    @udp_time_receive.setter
    def udp_time_receive(self, udp_time_receive):
        """Sets the udp_time_receive of this UDPDetailForGetTaskResultOutput.


        :param udp_time_receive: The udp_time_receive of this UDPDetailForGetTaskResultOutput.  # noqa: E501
        :type: int
        """

        self._udp_time_receive = udp_time_receive

    @property
    def udp_time_total(self):
        """Gets the udp_time_total of this UDPDetailForGetTaskResultOutput.  # noqa: E501


        :return: The udp_time_total of this UDPDetailForGetTaskResultOutput.  # noqa: E501
        :rtype: int
        """
        return self._udp_time_total

    @udp_time_total.setter
    def udp_time_total(self, udp_time_total):
        """Sets the udp_time_total of this UDPDetailForGetTaskResultOutput.


        :param udp_time_total: The udp_time_total of this UDPDetailForGetTaskResultOutput.  # noqa: E501
        :type: int
        """

        self._udp_time_total = udp_time_total

    @property
    def udp_time_wait(self):
        """Gets the udp_time_wait of this UDPDetailForGetTaskResultOutput.  # noqa: E501


        :return: The udp_time_wait of this UDPDetailForGetTaskResultOutput.  # noqa: E501
        :rtype: int
        """
        return self._udp_time_wait

    @udp_time_wait.setter
    def udp_time_wait(self, udp_time_wait):
        """Sets the udp_time_wait of this UDPDetailForGetTaskResultOutput.


        :param udp_time_wait: The udp_time_wait of this UDPDetailForGetTaskResultOutput.  # noqa: E501
        :type: int
        """

        self._udp_time_wait = udp_time_wait

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
        if issubclass(UDPDetailForGetTaskResultOutput, dict):
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
        if not isinstance(other, UDPDetailForGetTaskResultOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UDPDetailForGetTaskResultOutput):
            return True

        return self.to_dict() != other.to_dict()
