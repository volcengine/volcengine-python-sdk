# coding: utf-8

"""
    cdn

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class CreateUsageReportRequest(object):
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
        'aggregate': 'str',
        'billing_code': 'str',
        'billing_region': 'str',
        'calculation_method': 'str',
        'domain': 'str',
        'end_time': 'int',
        'export_type': 'str',
        'free_time_traffic_compute': 'bool',
        'metric': 'str',
        'start_time': 'int',
        'task_name': 'str',
        'time_zone': 'str',
        'tls_topic': 'str'
    }

    attribute_map = {
        'aggregate': 'Aggregate',
        'billing_code': 'BillingCode',
        'billing_region': 'BillingRegion',
        'calculation_method': 'CalculationMethod',
        'domain': 'Domain',
        'end_time': 'EndTime',
        'export_type': 'ExportType',
        'free_time_traffic_compute': 'FreeTimeTrafficCompute',
        'metric': 'Metric',
        'start_time': 'StartTime',
        'task_name': 'TaskName',
        'time_zone': 'TimeZone',
        'tls_topic': 'TlsTopic'
    }

    def __init__(self, aggregate=None, billing_code=None, billing_region=None, calculation_method=None, domain=None, end_time=None, export_type=None, free_time_traffic_compute=None, metric=None, start_time=None, task_name=None, time_zone=None, tls_topic=None, _configuration=None):  # noqa: E501
        """CreateUsageReportRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._aggregate = None
        self._billing_code = None
        self._billing_region = None
        self._calculation_method = None
        self._domain = None
        self._end_time = None
        self._export_type = None
        self._free_time_traffic_compute = None
        self._metric = None
        self._start_time = None
        self._task_name = None
        self._time_zone = None
        self._tls_topic = None
        self.discriminator = None

        if aggregate is not None:
            self.aggregate = aggregate
        if billing_code is not None:
            self.billing_code = billing_code
        self.billing_region = billing_region
        if calculation_method is not None:
            self.calculation_method = calculation_method
        if domain is not None:
            self.domain = domain
        self.end_time = end_time
        self.export_type = export_type
        if free_time_traffic_compute is not None:
            self.free_time_traffic_compute = free_time_traffic_compute
        if metric is not None:
            self.metric = metric
        self.start_time = start_time
        self.task_name = task_name
        if time_zone is not None:
            self.time_zone = time_zone
        if tls_topic is not None:
            self.tls_topic = tls_topic

    @property
    def aggregate(self):
        """Gets the aggregate of this CreateUsageReportRequest.  # noqa: E501


        :return: The aggregate of this CreateUsageReportRequest.  # noqa: E501
        :rtype: str
        """
        return self._aggregate

    @aggregate.setter
    def aggregate(self, aggregate):
        """Sets the aggregate of this CreateUsageReportRequest.


        :param aggregate: The aggregate of this CreateUsageReportRequest.  # noqa: E501
        :type: str
        """

        self._aggregate = aggregate

    @property
    def billing_code(self):
        """Gets the billing_code of this CreateUsageReportRequest.  # noqa: E501


        :return: The billing_code of this CreateUsageReportRequest.  # noqa: E501
        :rtype: str
        """
        return self._billing_code

    @billing_code.setter
    def billing_code(self, billing_code):
        """Sets the billing_code of this CreateUsageReportRequest.


        :param billing_code: The billing_code of this CreateUsageReportRequest.  # noqa: E501
        :type: str
        """

        self._billing_code = billing_code

    @property
    def billing_region(self):
        """Gets the billing_region of this CreateUsageReportRequest.  # noqa: E501


        :return: The billing_region of this CreateUsageReportRequest.  # noqa: E501
        :rtype: str
        """
        return self._billing_region

    @billing_region.setter
    def billing_region(self, billing_region):
        """Sets the billing_region of this CreateUsageReportRequest.


        :param billing_region: The billing_region of this CreateUsageReportRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and billing_region is None:
            raise ValueError("Invalid value for `billing_region`, must not be `None`")  # noqa: E501

        self._billing_region = billing_region

    @property
    def calculation_method(self):
        """Gets the calculation_method of this CreateUsageReportRequest.  # noqa: E501


        :return: The calculation_method of this CreateUsageReportRequest.  # noqa: E501
        :rtype: str
        """
        return self._calculation_method

    @calculation_method.setter
    def calculation_method(self, calculation_method):
        """Sets the calculation_method of this CreateUsageReportRequest.


        :param calculation_method: The calculation_method of this CreateUsageReportRequest.  # noqa: E501
        :type: str
        """

        self._calculation_method = calculation_method

    @property
    def domain(self):
        """Gets the domain of this CreateUsageReportRequest.  # noqa: E501


        :return: The domain of this CreateUsageReportRequest.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this CreateUsageReportRequest.


        :param domain: The domain of this CreateUsageReportRequest.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def end_time(self):
        """Gets the end_time of this CreateUsageReportRequest.  # noqa: E501


        :return: The end_time of this CreateUsageReportRequest.  # noqa: E501
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this CreateUsageReportRequest.


        :param end_time: The end_time of this CreateUsageReportRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and end_time is None:
            raise ValueError("Invalid value for `end_time`, must not be `None`")  # noqa: E501

        self._end_time = end_time

    @property
    def export_type(self):
        """Gets the export_type of this CreateUsageReportRequest.  # noqa: E501


        :return: The export_type of this CreateUsageReportRequest.  # noqa: E501
        :rtype: str
        """
        return self._export_type

    @export_type.setter
    def export_type(self, export_type):
        """Sets the export_type of this CreateUsageReportRequest.


        :param export_type: The export_type of this CreateUsageReportRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and export_type is None:
            raise ValueError("Invalid value for `export_type`, must not be `None`")  # noqa: E501

        self._export_type = export_type

    @property
    def free_time_traffic_compute(self):
        """Gets the free_time_traffic_compute of this CreateUsageReportRequest.  # noqa: E501


        :return: The free_time_traffic_compute of this CreateUsageReportRequest.  # noqa: E501
        :rtype: bool
        """
        return self._free_time_traffic_compute

    @free_time_traffic_compute.setter
    def free_time_traffic_compute(self, free_time_traffic_compute):
        """Sets the free_time_traffic_compute of this CreateUsageReportRequest.


        :param free_time_traffic_compute: The free_time_traffic_compute of this CreateUsageReportRequest.  # noqa: E501
        :type: bool
        """

        self._free_time_traffic_compute = free_time_traffic_compute

    @property
    def metric(self):
        """Gets the metric of this CreateUsageReportRequest.  # noqa: E501


        :return: The metric of this CreateUsageReportRequest.  # noqa: E501
        :rtype: str
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this CreateUsageReportRequest.


        :param metric: The metric of this CreateUsageReportRequest.  # noqa: E501
        :type: str
        """

        self._metric = metric

    @property
    def start_time(self):
        """Gets the start_time of this CreateUsageReportRequest.  # noqa: E501


        :return: The start_time of this CreateUsageReportRequest.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this CreateUsageReportRequest.


        :param start_time: The start_time of this CreateUsageReportRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and start_time is None:
            raise ValueError("Invalid value for `start_time`, must not be `None`")  # noqa: E501

        self._start_time = start_time

    @property
    def task_name(self):
        """Gets the task_name of this CreateUsageReportRequest.  # noqa: E501


        :return: The task_name of this CreateUsageReportRequest.  # noqa: E501
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this CreateUsageReportRequest.


        :param task_name: The task_name of this CreateUsageReportRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and task_name is None:
            raise ValueError("Invalid value for `task_name`, must not be `None`")  # noqa: E501

        self._task_name = task_name

    @property
    def time_zone(self):
        """Gets the time_zone of this CreateUsageReportRequest.  # noqa: E501


        :return: The time_zone of this CreateUsageReportRequest.  # noqa: E501
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this CreateUsageReportRequest.


        :param time_zone: The time_zone of this CreateUsageReportRequest.  # noqa: E501
        :type: str
        """

        self._time_zone = time_zone

    @property
    def tls_topic(self):
        """Gets the tls_topic of this CreateUsageReportRequest.  # noqa: E501


        :return: The tls_topic of this CreateUsageReportRequest.  # noqa: E501
        :rtype: str
        """
        return self._tls_topic

    @tls_topic.setter
    def tls_topic(self, tls_topic):
        """Sets the tls_topic of this CreateUsageReportRequest.


        :param tls_topic: The tls_topic of this CreateUsageReportRequest.  # noqa: E501
        :type: str
        """

        self._tls_topic = tls_topic

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
        if issubclass(CreateUsageReportRequest, dict):
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
        if not isinstance(other, CreateUsageReportRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateUsageReportRequest):
            return True

        return self.to_dict() != other.to_dict()