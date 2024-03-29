# coding: utf-8

"""
    volc_observe

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class GetTopDataRequest(object):
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
        'asc': 'bool',
        'end_time': 'int',
        'group_by': 'list[str]',
        'instances': 'list[InstanceForGetTopDataInput]',
        'metric_names': 'list[str]',
        'namespace': 'str',
        'order_by_metric_name': 'str',
        'start_time': 'int',
        'sub_namespace': 'str',
        'top_n': 'int'
    }

    attribute_map = {
        'asc': 'Asc',
        'end_time': 'EndTime',
        'group_by': 'GroupBy',
        'instances': 'Instances',
        'metric_names': 'MetricNames',
        'namespace': 'Namespace',
        'order_by_metric_name': 'OrderByMetricName',
        'start_time': 'StartTime',
        'sub_namespace': 'SubNamespace',
        'top_n': 'TopN'
    }

    def __init__(self, asc=None, end_time=None, group_by=None, instances=None, metric_names=None, namespace=None, order_by_metric_name=None, start_time=None, sub_namespace=None, top_n=None, _configuration=None):  # noqa: E501
        """GetTopDataRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._asc = None
        self._end_time = None
        self._group_by = None
        self._instances = None
        self._metric_names = None
        self._namespace = None
        self._order_by_metric_name = None
        self._start_time = None
        self._sub_namespace = None
        self._top_n = None
        self.discriminator = None

        if asc is not None:
            self.asc = asc
        if end_time is not None:
            self.end_time = end_time
        if group_by is not None:
            self.group_by = group_by
        if instances is not None:
            self.instances = instances
        if metric_names is not None:
            self.metric_names = metric_names
        if namespace is not None:
            self.namespace = namespace
        if order_by_metric_name is not None:
            self.order_by_metric_name = order_by_metric_name
        if start_time is not None:
            self.start_time = start_time
        if sub_namespace is not None:
            self.sub_namespace = sub_namespace
        if top_n is not None:
            self.top_n = top_n

    @property
    def asc(self):
        """Gets the asc of this GetTopDataRequest.  # noqa: E501


        :return: The asc of this GetTopDataRequest.  # noqa: E501
        :rtype: bool
        """
        return self._asc

    @asc.setter
    def asc(self, asc):
        """Sets the asc of this GetTopDataRequest.


        :param asc: The asc of this GetTopDataRequest.  # noqa: E501
        :type: bool
        """

        self._asc = asc

    @property
    def end_time(self):
        """Gets the end_time of this GetTopDataRequest.  # noqa: E501


        :return: The end_time of this GetTopDataRequest.  # noqa: E501
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this GetTopDataRequest.


        :param end_time: The end_time of this GetTopDataRequest.  # noqa: E501
        :type: int
        """

        self._end_time = end_time

    @property
    def group_by(self):
        """Gets the group_by of this GetTopDataRequest.  # noqa: E501


        :return: The group_by of this GetTopDataRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        """Sets the group_by of this GetTopDataRequest.


        :param group_by: The group_by of this GetTopDataRequest.  # noqa: E501
        :type: list[str]
        """

        self._group_by = group_by

    @property
    def instances(self):
        """Gets the instances of this GetTopDataRequest.  # noqa: E501


        :return: The instances of this GetTopDataRequest.  # noqa: E501
        :rtype: list[InstanceForGetTopDataInput]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this GetTopDataRequest.


        :param instances: The instances of this GetTopDataRequest.  # noqa: E501
        :type: list[InstanceForGetTopDataInput]
        """

        self._instances = instances

    @property
    def metric_names(self):
        """Gets the metric_names of this GetTopDataRequest.  # noqa: E501


        :return: The metric_names of this GetTopDataRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._metric_names

    @metric_names.setter
    def metric_names(self, metric_names):
        """Sets the metric_names of this GetTopDataRequest.


        :param metric_names: The metric_names of this GetTopDataRequest.  # noqa: E501
        :type: list[str]
        """

        self._metric_names = metric_names

    @property
    def namespace(self):
        """Gets the namespace of this GetTopDataRequest.  # noqa: E501


        :return: The namespace of this GetTopDataRequest.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this GetTopDataRequest.


        :param namespace: The namespace of this GetTopDataRequest.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def order_by_metric_name(self):
        """Gets the order_by_metric_name of this GetTopDataRequest.  # noqa: E501


        :return: The order_by_metric_name of this GetTopDataRequest.  # noqa: E501
        :rtype: str
        """
        return self._order_by_metric_name

    @order_by_metric_name.setter
    def order_by_metric_name(self, order_by_metric_name):
        """Sets the order_by_metric_name of this GetTopDataRequest.


        :param order_by_metric_name: The order_by_metric_name of this GetTopDataRequest.  # noqa: E501
        :type: str
        """

        self._order_by_metric_name = order_by_metric_name

    @property
    def start_time(self):
        """Gets the start_time of this GetTopDataRequest.  # noqa: E501


        :return: The start_time of this GetTopDataRequest.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this GetTopDataRequest.


        :param start_time: The start_time of this GetTopDataRequest.  # noqa: E501
        :type: int
        """

        self._start_time = start_time

    @property
    def sub_namespace(self):
        """Gets the sub_namespace of this GetTopDataRequest.  # noqa: E501


        :return: The sub_namespace of this GetTopDataRequest.  # noqa: E501
        :rtype: str
        """
        return self._sub_namespace

    @sub_namespace.setter
    def sub_namespace(self, sub_namespace):
        """Sets the sub_namespace of this GetTopDataRequest.


        :param sub_namespace: The sub_namespace of this GetTopDataRequest.  # noqa: E501
        :type: str
        """

        self._sub_namespace = sub_namespace

    @property
    def top_n(self):
        """Gets the top_n of this GetTopDataRequest.  # noqa: E501


        :return: The top_n of this GetTopDataRequest.  # noqa: E501
        :rtype: int
        """
        return self._top_n

    @top_n.setter
    def top_n(self, top_n):
        """Sets the top_n of this GetTopDataRequest.


        :param top_n: The top_n of this GetTopDataRequest.  # noqa: E501
        :type: int
        """

        self._top_n = top_n

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
        if issubclass(GetTopDataRequest, dict):
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
        if not isinstance(other, GetTopDataRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetTopDataRequest):
            return True

        return self.to_dict() != other.to_dict()
