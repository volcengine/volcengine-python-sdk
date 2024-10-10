# coding: utf-8

"""
    vpc

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class FlowLogForDescribeFlowLogsOutput(object):
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
        'aggregation_interval': 'int',
        'business_status': 'str',
        'created_at': 'str',
        'description': 'str',
        'flow_log_id': 'str',
        'flow_log_name': 'str',
        'lock_reason': 'str',
        'log_project_id': 'str',
        'log_topic_id': 'str',
        'open_analyze_product_log': 'bool',
        'project_name': 'str',
        'resource_id': 'str',
        'resource_type': 'str',
        'status': 'str',
        'tags': 'list[TagForDescribeFlowLogsOutput]',
        'traffic_type': 'str',
        'updated_at': 'str',
        'vpc_id': 'str'
    }

    attribute_map = {
        'account_id': 'AccountId',
        'aggregation_interval': 'AggregationInterval',
        'business_status': 'BusinessStatus',
        'created_at': 'CreatedAt',
        'description': 'Description',
        'flow_log_id': 'FlowLogId',
        'flow_log_name': 'FlowLogName',
        'lock_reason': 'LockReason',
        'log_project_id': 'LogProjectId',
        'log_topic_id': 'LogTopicId',
        'open_analyze_product_log': 'OpenAnalyzeProductLog',
        'project_name': 'ProjectName',
        'resource_id': 'ResourceId',
        'resource_type': 'ResourceType',
        'status': 'Status',
        'tags': 'Tags',
        'traffic_type': 'TrafficType',
        'updated_at': 'UpdatedAt',
        'vpc_id': 'VpcId'
    }

    def __init__(self, account_id=None, aggregation_interval=None, business_status=None, created_at=None, description=None, flow_log_id=None, flow_log_name=None, lock_reason=None, log_project_id=None, log_topic_id=None, open_analyze_product_log=None, project_name=None, resource_id=None, resource_type=None, status=None, tags=None, traffic_type=None, updated_at=None, vpc_id=None, _configuration=None):  # noqa: E501
        """FlowLogForDescribeFlowLogsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_id = None
        self._aggregation_interval = None
        self._business_status = None
        self._created_at = None
        self._description = None
        self._flow_log_id = None
        self._flow_log_name = None
        self._lock_reason = None
        self._log_project_id = None
        self._log_topic_id = None
        self._open_analyze_product_log = None
        self._project_name = None
        self._resource_id = None
        self._resource_type = None
        self._status = None
        self._tags = None
        self._traffic_type = None
        self._updated_at = None
        self._vpc_id = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if aggregation_interval is not None:
            self.aggregation_interval = aggregation_interval
        if business_status is not None:
            self.business_status = business_status
        if created_at is not None:
            self.created_at = created_at
        if description is not None:
            self.description = description
        if flow_log_id is not None:
            self.flow_log_id = flow_log_id
        if flow_log_name is not None:
            self.flow_log_name = flow_log_name
        if lock_reason is not None:
            self.lock_reason = lock_reason
        if log_project_id is not None:
            self.log_project_id = log_project_id
        if log_topic_id is not None:
            self.log_topic_id = log_topic_id
        if open_analyze_product_log is not None:
            self.open_analyze_product_log = open_analyze_product_log
        if project_name is not None:
            self.project_name = project_name
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_type is not None:
            self.resource_type = resource_type
        if status is not None:
            self.status = status
        if tags is not None:
            self.tags = tags
        if traffic_type is not None:
            self.traffic_type = traffic_type
        if updated_at is not None:
            self.updated_at = updated_at
        if vpc_id is not None:
            self.vpc_id = vpc_id

    @property
    def account_id(self):
        """Gets the account_id of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501


        :return: The account_id of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this FlowLogForDescribeFlowLogsOutput.


        :param account_id: The account_id of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def aggregation_interval(self):
        """Gets the aggregation_interval of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501


        :return: The aggregation_interval of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501
        :rtype: int
        """
        return self._aggregation_interval

    @aggregation_interval.setter
    def aggregation_interval(self, aggregation_interval):
        """Sets the aggregation_interval of this FlowLogForDescribeFlowLogsOutput.


        :param aggregation_interval: The aggregation_interval of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501
        :type: int
        """

        self._aggregation_interval = aggregation_interval

    @property
    def business_status(self):
        """Gets the business_status of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501


        :return: The business_status of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501
        :rtype: str
        """
        return self._business_status

    @business_status.setter
    def business_status(self, business_status):
        """Sets the business_status of this FlowLogForDescribeFlowLogsOutput.


        :param business_status: The business_status of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501
        :type: str
        """

        self._business_status = business_status

    @property
    def created_at(self):
        """Gets the created_at of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501


        :return: The created_at of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this FlowLogForDescribeFlowLogsOutput.


        :param created_at: The created_at of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def description(self):
        """Gets the description of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501


        :return: The description of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FlowLogForDescribeFlowLogsOutput.


        :param description: The description of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def flow_log_id(self):
        """Gets the flow_log_id of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501


        :return: The flow_log_id of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501
        :rtype: str
        """
        return self._flow_log_id

    @flow_log_id.setter
    def flow_log_id(self, flow_log_id):
        """Sets the flow_log_id of this FlowLogForDescribeFlowLogsOutput.


        :param flow_log_id: The flow_log_id of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501
        :type: str
        """

        self._flow_log_id = flow_log_id

    @property
    def flow_log_name(self):
        """Gets the flow_log_name of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501


        :return: The flow_log_name of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501
        :rtype: str
        """
        return self._flow_log_name

    @flow_log_name.setter
    def flow_log_name(self, flow_log_name):
        """Sets the flow_log_name of this FlowLogForDescribeFlowLogsOutput.


        :param flow_log_name: The flow_log_name of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501
        :type: str
        """

        self._flow_log_name = flow_log_name

    @property
    def lock_reason(self):
        """Gets the lock_reason of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501


        :return: The lock_reason of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501
        :rtype: str
        """
        return self._lock_reason

    @lock_reason.setter
    def lock_reason(self, lock_reason):
        """Sets the lock_reason of this FlowLogForDescribeFlowLogsOutput.


        :param lock_reason: The lock_reason of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501
        :type: str
        """

        self._lock_reason = lock_reason

    @property
    def log_project_id(self):
        """Gets the log_project_id of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501


        :return: The log_project_id of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501
        :rtype: str
        """
        return self._log_project_id

    @log_project_id.setter
    def log_project_id(self, log_project_id):
        """Sets the log_project_id of this FlowLogForDescribeFlowLogsOutput.


        :param log_project_id: The log_project_id of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501
        :type: str
        """

        self._log_project_id = log_project_id

    @property
    def log_topic_id(self):
        """Gets the log_topic_id of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501


        :return: The log_topic_id of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501
        :rtype: str
        """
        return self._log_topic_id

    @log_topic_id.setter
    def log_topic_id(self, log_topic_id):
        """Sets the log_topic_id of this FlowLogForDescribeFlowLogsOutput.


        :param log_topic_id: The log_topic_id of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501
        :type: str
        """

        self._log_topic_id = log_topic_id

    @property
    def open_analyze_product_log(self):
        """Gets the open_analyze_product_log of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501


        :return: The open_analyze_product_log of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501
        :rtype: bool
        """
        return self._open_analyze_product_log

    @open_analyze_product_log.setter
    def open_analyze_product_log(self, open_analyze_product_log):
        """Sets the open_analyze_product_log of this FlowLogForDescribeFlowLogsOutput.


        :param open_analyze_product_log: The open_analyze_product_log of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501
        :type: bool
        """

        self._open_analyze_product_log = open_analyze_product_log

    @property
    def project_name(self):
        """Gets the project_name of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501


        :return: The project_name of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this FlowLogForDescribeFlowLogsOutput.


        :param project_name: The project_name of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def resource_id(self):
        """Gets the resource_id of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501


        :return: The resource_id of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this FlowLogForDescribeFlowLogsOutput.


        :param resource_id: The resource_id of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501
        :type: str
        """

        self._resource_id = resource_id

    @property
    def resource_type(self):
        """Gets the resource_type of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501


        :return: The resource_type of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this FlowLogForDescribeFlowLogsOutput.


        :param resource_type: The resource_type of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def status(self):
        """Gets the status of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501


        :return: The status of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this FlowLogForDescribeFlowLogsOutput.


        :param status: The status of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def tags(self):
        """Gets the tags of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501


        :return: The tags of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501
        :rtype: list[TagForDescribeFlowLogsOutput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this FlowLogForDescribeFlowLogsOutput.


        :param tags: The tags of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501
        :type: list[TagForDescribeFlowLogsOutput]
        """

        self._tags = tags

    @property
    def traffic_type(self):
        """Gets the traffic_type of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501


        :return: The traffic_type of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501
        :rtype: str
        """
        return self._traffic_type

    @traffic_type.setter
    def traffic_type(self, traffic_type):
        """Sets the traffic_type of this FlowLogForDescribeFlowLogsOutput.


        :param traffic_type: The traffic_type of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501
        :type: str
        """

        self._traffic_type = traffic_type

    @property
    def updated_at(self):
        """Gets the updated_at of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501


        :return: The updated_at of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this FlowLogForDescribeFlowLogsOutput.


        :param updated_at: The updated_at of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

    @property
    def vpc_id(self):
        """Gets the vpc_id of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501


        :return: The vpc_id of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this FlowLogForDescribeFlowLogsOutput.


        :param vpc_id: The vpc_id of this FlowLogForDescribeFlowLogsOutput.  # noqa: E501
        :type: str
        """

        self._vpc_id = vpc_id

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
        if issubclass(FlowLogForDescribeFlowLogsOutput, dict):
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
        if not isinstance(other, FlowLogForDescribeFlowLogsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FlowLogForDescribeFlowLogsOutput):
            return True

        return self.to_dict() != other.to_dict()