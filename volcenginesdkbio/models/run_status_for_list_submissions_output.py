# coding: utf-8

"""
    bio

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class RunStatusForListSubmissionsOutput(object):
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
        'cancelled': 'int',
        'cancelling': 'str',
        'count': 'int',
        'failed': 'int',
        'pending': 'int',
        'running': 'int',
        'succeeded': 'int'
    }

    attribute_map = {
        'cancelled': 'Cancelled',
        'cancelling': 'Cancelling',
        'count': 'Count',
        'failed': 'Failed',
        'pending': 'Pending',
        'running': 'Running',
        'succeeded': 'Succeeded'
    }

    def __init__(self, cancelled=None, cancelling=None, count=None, failed=None, pending=None, running=None, succeeded=None, _configuration=None):  # noqa: E501
        """RunStatusForListSubmissionsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cancelled = None
        self._cancelling = None
        self._count = None
        self._failed = None
        self._pending = None
        self._running = None
        self._succeeded = None
        self.discriminator = None

        if cancelled is not None:
            self.cancelled = cancelled
        if cancelling is not None:
            self.cancelling = cancelling
        if count is not None:
            self.count = count
        if failed is not None:
            self.failed = failed
        if pending is not None:
            self.pending = pending
        if running is not None:
            self.running = running
        if succeeded is not None:
            self.succeeded = succeeded

    @property
    def cancelled(self):
        """Gets the cancelled of this RunStatusForListSubmissionsOutput.  # noqa: E501


        :return: The cancelled of this RunStatusForListSubmissionsOutput.  # noqa: E501
        :rtype: int
        """
        return self._cancelled

    @cancelled.setter
    def cancelled(self, cancelled):
        """Sets the cancelled of this RunStatusForListSubmissionsOutput.


        :param cancelled: The cancelled of this RunStatusForListSubmissionsOutput.  # noqa: E501
        :type: int
        """

        self._cancelled = cancelled

    @property
    def cancelling(self):
        """Gets the cancelling of this RunStatusForListSubmissionsOutput.  # noqa: E501


        :return: The cancelling of this RunStatusForListSubmissionsOutput.  # noqa: E501
        :rtype: str
        """
        return self._cancelling

    @cancelling.setter
    def cancelling(self, cancelling):
        """Sets the cancelling of this RunStatusForListSubmissionsOutput.


        :param cancelling: The cancelling of this RunStatusForListSubmissionsOutput.  # noqa: E501
        :type: str
        """

        self._cancelling = cancelling

    @property
    def count(self):
        """Gets the count of this RunStatusForListSubmissionsOutput.  # noqa: E501


        :return: The count of this RunStatusForListSubmissionsOutput.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this RunStatusForListSubmissionsOutput.


        :param count: The count of this RunStatusForListSubmissionsOutput.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def failed(self):
        """Gets the failed of this RunStatusForListSubmissionsOutput.  # noqa: E501


        :return: The failed of this RunStatusForListSubmissionsOutput.  # noqa: E501
        :rtype: int
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        """Sets the failed of this RunStatusForListSubmissionsOutput.


        :param failed: The failed of this RunStatusForListSubmissionsOutput.  # noqa: E501
        :type: int
        """

        self._failed = failed

    @property
    def pending(self):
        """Gets the pending of this RunStatusForListSubmissionsOutput.  # noqa: E501


        :return: The pending of this RunStatusForListSubmissionsOutput.  # noqa: E501
        :rtype: int
        """
        return self._pending

    @pending.setter
    def pending(self, pending):
        """Sets the pending of this RunStatusForListSubmissionsOutput.


        :param pending: The pending of this RunStatusForListSubmissionsOutput.  # noqa: E501
        :type: int
        """

        self._pending = pending

    @property
    def running(self):
        """Gets the running of this RunStatusForListSubmissionsOutput.  # noqa: E501


        :return: The running of this RunStatusForListSubmissionsOutput.  # noqa: E501
        :rtype: int
        """
        return self._running

    @running.setter
    def running(self, running):
        """Sets the running of this RunStatusForListSubmissionsOutput.


        :param running: The running of this RunStatusForListSubmissionsOutput.  # noqa: E501
        :type: int
        """

        self._running = running

    @property
    def succeeded(self):
        """Gets the succeeded of this RunStatusForListSubmissionsOutput.  # noqa: E501


        :return: The succeeded of this RunStatusForListSubmissionsOutput.  # noqa: E501
        :rtype: int
        """
        return self._succeeded

    @succeeded.setter
    def succeeded(self, succeeded):
        """Sets the succeeded of this RunStatusForListSubmissionsOutput.


        :param succeeded: The succeeded of this RunStatusForListSubmissionsOutput.  # noqa: E501
        :type: int
        """

        self._succeeded = succeeded

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
        if issubclass(RunStatusForListSubmissionsOutput, dict):
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
        if not isinstance(other, RunStatusForListSubmissionsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RunStatusForListSubmissionsOutput):
            return True

        return self.to_dict() != other.to_dict()
