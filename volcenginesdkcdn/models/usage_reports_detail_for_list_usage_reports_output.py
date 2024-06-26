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


class UsageReportsDetailForListUsageReportsOutput(object):
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
        'account_id': 'str',
        'billing_code': 'str',
        'billing_region': 'str',
        'calculation_method': 'str',
        'create_time': 'int',
        'down_load_url': 'str',
        'end_time': 'int',
        'export_type': 'str',
        'metric': 'str',
        'start_time': 'int',
        'status': 'int',
        'task_id': 'str',
        'task_name': 'str',
        'time_zone': 'str'
    }

    attribute_map = {
        'account_id': 'AccountId',
        'billing_code': 'BillingCode',
        'billing_region': 'BillingRegion',
        'calculation_method': 'CalculationMethod',
        'create_time': 'CreateTime',
        'down_load_url': 'DownLoadUrl',
        'end_time': 'EndTime',
        'export_type': 'ExportType',
        'metric': 'Metric',
        'start_time': 'StartTime',
        'status': 'Status',
        'task_id': 'TaskId',
        'task_name': 'TaskName',
        'time_zone': 'TimeZone'
    }

    def __init__(self, account_id=None, billing_code=None, billing_region=None, calculation_method=None, create_time=None, down_load_url=None, end_time=None, export_type=None, metric=None, start_time=None, status=None, task_id=None, task_name=None, time_zone=None, _configuration=None):  # noqa: E501
        """UsageReportsDetailForListUsageReportsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_id = None
        self._billing_code = None
        self._billing_region = None
        self._calculation_method = None
        self._create_time = None
        self._down_load_url = None
        self._end_time = None
        self._export_type = None
        self._metric = None
        self._start_time = None
        self._status = None
        self._task_id = None
        self._task_name = None
        self._time_zone = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if billing_code is not None:
            self.billing_code = billing_code
        if billing_region is not None:
            self.billing_region = billing_region
        if calculation_method is not None:
            self.calculation_method = calculation_method
        if create_time is not None:
            self.create_time = create_time
        if down_load_url is not None:
            self.down_load_url = down_load_url
        if end_time is not None:
            self.end_time = end_time
        if export_type is not None:
            self.export_type = export_type
        if metric is not None:
            self.metric = metric
        if start_time is not None:
            self.start_time = start_time
        if status is not None:
            self.status = status
        if task_id is not None:
            self.task_id = task_id
        if task_name is not None:
            self.task_name = task_name
        if time_zone is not None:
            self.time_zone = time_zone

    @property
    def account_id(self):
        """Gets the account_id of this UsageReportsDetailForListUsageReportsOutput.  # noqa: E501


        :return: The account_id of this UsageReportsDetailForListUsageReportsOutput.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this UsageReportsDetailForListUsageReportsOutput.


        :param account_id: The account_id of this UsageReportsDetailForListUsageReportsOutput.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def billing_code(self):
        """Gets the billing_code of this UsageReportsDetailForListUsageReportsOutput.  # noqa: E501


        :return: The billing_code of this UsageReportsDetailForListUsageReportsOutput.  # noqa: E501
        :rtype: str
        """
        return self._billing_code

    @billing_code.setter
    def billing_code(self, billing_code):
        """Sets the billing_code of this UsageReportsDetailForListUsageReportsOutput.


        :param billing_code: The billing_code of this UsageReportsDetailForListUsageReportsOutput.  # noqa: E501
        :type: str
        """

        self._billing_code = billing_code

    @property
    def billing_region(self):
        """Gets the billing_region of this UsageReportsDetailForListUsageReportsOutput.  # noqa: E501


        :return: The billing_region of this UsageReportsDetailForListUsageReportsOutput.  # noqa: E501
        :rtype: str
        """
        return self._billing_region

    @billing_region.setter
    def billing_region(self, billing_region):
        """Sets the billing_region of this UsageReportsDetailForListUsageReportsOutput.


        :param billing_region: The billing_region of this UsageReportsDetailForListUsageReportsOutput.  # noqa: E501
        :type: str
        """

        self._billing_region = billing_region

    @property
    def calculation_method(self):
        """Gets the calculation_method of this UsageReportsDetailForListUsageReportsOutput.  # noqa: E501


        :return: The calculation_method of this UsageReportsDetailForListUsageReportsOutput.  # noqa: E501
        :rtype: str
        """
        return self._calculation_method

    @calculation_method.setter
    def calculation_method(self, calculation_method):
        """Sets the calculation_method of this UsageReportsDetailForListUsageReportsOutput.


        :param calculation_method: The calculation_method of this UsageReportsDetailForListUsageReportsOutput.  # noqa: E501
        :type: str
        """

        self._calculation_method = calculation_method

    @property
    def create_time(self):
        """Gets the create_time of this UsageReportsDetailForListUsageReportsOutput.  # noqa: E501


        :return: The create_time of this UsageReportsDetailForListUsageReportsOutput.  # noqa: E501
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this UsageReportsDetailForListUsageReportsOutput.


        :param create_time: The create_time of this UsageReportsDetailForListUsageReportsOutput.  # noqa: E501
        :type: int
        """

        self._create_time = create_time

    @property
    def down_load_url(self):
        """Gets the down_load_url of this UsageReportsDetailForListUsageReportsOutput.  # noqa: E501


        :return: The down_load_url of this UsageReportsDetailForListUsageReportsOutput.  # noqa: E501
        :rtype: str
        """
        return self._down_load_url

    @down_load_url.setter
    def down_load_url(self, down_load_url):
        """Sets the down_load_url of this UsageReportsDetailForListUsageReportsOutput.


        :param down_load_url: The down_load_url of this UsageReportsDetailForListUsageReportsOutput.  # noqa: E501
        :type: str
        """

        self._down_load_url = down_load_url

    @property
    def end_time(self):
        """Gets the end_time of this UsageReportsDetailForListUsageReportsOutput.  # noqa: E501


        :return: The end_time of this UsageReportsDetailForListUsageReportsOutput.  # noqa: E501
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this UsageReportsDetailForListUsageReportsOutput.


        :param end_time: The end_time of this UsageReportsDetailForListUsageReportsOutput.  # noqa: E501
        :type: int
        """

        self._end_time = end_time

    @property
    def export_type(self):
        """Gets the export_type of this UsageReportsDetailForListUsageReportsOutput.  # noqa: E501


        :return: The export_type of this UsageReportsDetailForListUsageReportsOutput.  # noqa: E501
        :rtype: str
        """
        return self._export_type

    @export_type.setter
    def export_type(self, export_type):
        """Sets the export_type of this UsageReportsDetailForListUsageReportsOutput.


        :param export_type: The export_type of this UsageReportsDetailForListUsageReportsOutput.  # noqa: E501
        :type: str
        """

        self._export_type = export_type

    @property
    def metric(self):
        """Gets the metric of this UsageReportsDetailForListUsageReportsOutput.  # noqa: E501


        :return: The metric of this UsageReportsDetailForListUsageReportsOutput.  # noqa: E501
        :rtype: str
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this UsageReportsDetailForListUsageReportsOutput.


        :param metric: The metric of this UsageReportsDetailForListUsageReportsOutput.  # noqa: E501
        :type: str
        """

        self._metric = metric

    @property
    def start_time(self):
        """Gets the start_time of this UsageReportsDetailForListUsageReportsOutput.  # noqa: E501


        :return: The start_time of this UsageReportsDetailForListUsageReportsOutput.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this UsageReportsDetailForListUsageReportsOutput.


        :param start_time: The start_time of this UsageReportsDetailForListUsageReportsOutput.  # noqa: E501
        :type: int
        """

        self._start_time = start_time

    @property
    def status(self):
        """Gets the status of this UsageReportsDetailForListUsageReportsOutput.  # noqa: E501


        :return: The status of this UsageReportsDetailForListUsageReportsOutput.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UsageReportsDetailForListUsageReportsOutput.


        :param status: The status of this UsageReportsDetailForListUsageReportsOutput.  # noqa: E501
        :type: int
        """

        self._status = status

    @property
    def task_id(self):
        """Gets the task_id of this UsageReportsDetailForListUsageReportsOutput.  # noqa: E501


        :return: The task_id of this UsageReportsDetailForListUsageReportsOutput.  # noqa: E501
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this UsageReportsDetailForListUsageReportsOutput.


        :param task_id: The task_id of this UsageReportsDetailForListUsageReportsOutput.  # noqa: E501
        :type: str
        """

        self._task_id = task_id

    @property
    def task_name(self):
        """Gets the task_name of this UsageReportsDetailForListUsageReportsOutput.  # noqa: E501


        :return: The task_name of this UsageReportsDetailForListUsageReportsOutput.  # noqa: E501
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this UsageReportsDetailForListUsageReportsOutput.


        :param task_name: The task_name of this UsageReportsDetailForListUsageReportsOutput.  # noqa: E501
        :type: str
        """

        self._task_name = task_name

    @property
    def time_zone(self):
        """Gets the time_zone of this UsageReportsDetailForListUsageReportsOutput.  # noqa: E501


        :return: The time_zone of this UsageReportsDetailForListUsageReportsOutput.  # noqa: E501
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this UsageReportsDetailForListUsageReportsOutput.


        :param time_zone: The time_zone of this UsageReportsDetailForListUsageReportsOutput.  # noqa: E501
        :type: str
        """

        self._time_zone = time_zone

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
        if issubclass(UsageReportsDetailForListUsageReportsOutput, dict):
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
        if not isinstance(other, UsageReportsDetailForListUsageReportsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UsageReportsDetailForListUsageReportsOutput):
            return True

        return self.to_dict() != other.to_dict()
