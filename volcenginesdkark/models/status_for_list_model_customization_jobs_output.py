# coding: utf-8

"""
    ark

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class StatusForListModelCustomizationJobsOutput(object):
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
        'billable_tokens': 'int',
        'message': 'str',
        'output_expired_time': 'str',
        'phase': 'str',
        'phase_time': 'str',
        'queue_position': 'int',
        'resumable': 'bool',
        'retry_count': 'int',
        'retry_limit': 'int',
        'training_tokens_per_epoch': 'int'
    }

    attribute_map = {
        'billable_tokens': 'BillableTokens',
        'message': 'Message',
        'output_expired_time': 'OutputExpiredTime',
        'phase': 'Phase',
        'phase_time': 'PhaseTime',
        'queue_position': 'QueuePosition',
        'resumable': 'Resumable',
        'retry_count': 'RetryCount',
        'retry_limit': 'RetryLimit',
        'training_tokens_per_epoch': 'TrainingTokensPerEpoch'
    }

    def __init__(self, billable_tokens=None, message=None, output_expired_time=None, phase=None, phase_time=None, queue_position=None, resumable=None, retry_count=None, retry_limit=None, training_tokens_per_epoch=None, _configuration=None):  # noqa: E501
        """StatusForListModelCustomizationJobsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._billable_tokens = None
        self._message = None
        self._output_expired_time = None
        self._phase = None
        self._phase_time = None
        self._queue_position = None
        self._resumable = None
        self._retry_count = None
        self._retry_limit = None
        self._training_tokens_per_epoch = None
        self.discriminator = None

        if billable_tokens is not None:
            self.billable_tokens = billable_tokens
        if message is not None:
            self.message = message
        if output_expired_time is not None:
            self.output_expired_time = output_expired_time
        if phase is not None:
            self.phase = phase
        if phase_time is not None:
            self.phase_time = phase_time
        if queue_position is not None:
            self.queue_position = queue_position
        if resumable is not None:
            self.resumable = resumable
        if retry_count is not None:
            self.retry_count = retry_count
        if retry_limit is not None:
            self.retry_limit = retry_limit
        if training_tokens_per_epoch is not None:
            self.training_tokens_per_epoch = training_tokens_per_epoch

    @property
    def billable_tokens(self):
        """Gets the billable_tokens of this StatusForListModelCustomizationJobsOutput.  # noqa: E501


        :return: The billable_tokens of this StatusForListModelCustomizationJobsOutput.  # noqa: E501
        :rtype: int
        """
        return self._billable_tokens

    @billable_tokens.setter
    def billable_tokens(self, billable_tokens):
        """Sets the billable_tokens of this StatusForListModelCustomizationJobsOutput.


        :param billable_tokens: The billable_tokens of this StatusForListModelCustomizationJobsOutput.  # noqa: E501
        :type: int
        """

        self._billable_tokens = billable_tokens

    @property
    def message(self):
        """Gets the message of this StatusForListModelCustomizationJobsOutput.  # noqa: E501


        :return: The message of this StatusForListModelCustomizationJobsOutput.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this StatusForListModelCustomizationJobsOutput.


        :param message: The message of this StatusForListModelCustomizationJobsOutput.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def output_expired_time(self):
        """Gets the output_expired_time of this StatusForListModelCustomizationJobsOutput.  # noqa: E501


        :return: The output_expired_time of this StatusForListModelCustomizationJobsOutput.  # noqa: E501
        :rtype: str
        """
        return self._output_expired_time

    @output_expired_time.setter
    def output_expired_time(self, output_expired_time):
        """Sets the output_expired_time of this StatusForListModelCustomizationJobsOutput.


        :param output_expired_time: The output_expired_time of this StatusForListModelCustomizationJobsOutput.  # noqa: E501
        :type: str
        """

        self._output_expired_time = output_expired_time

    @property
    def phase(self):
        """Gets the phase of this StatusForListModelCustomizationJobsOutput.  # noqa: E501


        :return: The phase of this StatusForListModelCustomizationJobsOutput.  # noqa: E501
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this StatusForListModelCustomizationJobsOutput.


        :param phase: The phase of this StatusForListModelCustomizationJobsOutput.  # noqa: E501
        :type: str
        """

        self._phase = phase

    @property
    def phase_time(self):
        """Gets the phase_time of this StatusForListModelCustomizationJobsOutput.  # noqa: E501


        :return: The phase_time of this StatusForListModelCustomizationJobsOutput.  # noqa: E501
        :rtype: str
        """
        return self._phase_time

    @phase_time.setter
    def phase_time(self, phase_time):
        """Sets the phase_time of this StatusForListModelCustomizationJobsOutput.


        :param phase_time: The phase_time of this StatusForListModelCustomizationJobsOutput.  # noqa: E501
        :type: str
        """

        self._phase_time = phase_time

    @property
    def queue_position(self):
        """Gets the queue_position of this StatusForListModelCustomizationJobsOutput.  # noqa: E501


        :return: The queue_position of this StatusForListModelCustomizationJobsOutput.  # noqa: E501
        :rtype: int
        """
        return self._queue_position

    @queue_position.setter
    def queue_position(self, queue_position):
        """Sets the queue_position of this StatusForListModelCustomizationJobsOutput.


        :param queue_position: The queue_position of this StatusForListModelCustomizationJobsOutput.  # noqa: E501
        :type: int
        """

        self._queue_position = queue_position

    @property
    def resumable(self):
        """Gets the resumable of this StatusForListModelCustomizationJobsOutput.  # noqa: E501


        :return: The resumable of this StatusForListModelCustomizationJobsOutput.  # noqa: E501
        :rtype: bool
        """
        return self._resumable

    @resumable.setter
    def resumable(self, resumable):
        """Sets the resumable of this StatusForListModelCustomizationJobsOutput.


        :param resumable: The resumable of this StatusForListModelCustomizationJobsOutput.  # noqa: E501
        :type: bool
        """

        self._resumable = resumable

    @property
    def retry_count(self):
        """Gets the retry_count of this StatusForListModelCustomizationJobsOutput.  # noqa: E501


        :return: The retry_count of this StatusForListModelCustomizationJobsOutput.  # noqa: E501
        :rtype: int
        """
        return self._retry_count

    @retry_count.setter
    def retry_count(self, retry_count):
        """Sets the retry_count of this StatusForListModelCustomizationJobsOutput.


        :param retry_count: The retry_count of this StatusForListModelCustomizationJobsOutput.  # noqa: E501
        :type: int
        """

        self._retry_count = retry_count

    @property
    def retry_limit(self):
        """Gets the retry_limit of this StatusForListModelCustomizationJobsOutput.  # noqa: E501


        :return: The retry_limit of this StatusForListModelCustomizationJobsOutput.  # noqa: E501
        :rtype: int
        """
        return self._retry_limit

    @retry_limit.setter
    def retry_limit(self, retry_limit):
        """Sets the retry_limit of this StatusForListModelCustomizationJobsOutput.


        :param retry_limit: The retry_limit of this StatusForListModelCustomizationJobsOutput.  # noqa: E501
        :type: int
        """

        self._retry_limit = retry_limit

    @property
    def training_tokens_per_epoch(self):
        """Gets the training_tokens_per_epoch of this StatusForListModelCustomizationJobsOutput.  # noqa: E501


        :return: The training_tokens_per_epoch of this StatusForListModelCustomizationJobsOutput.  # noqa: E501
        :rtype: int
        """
        return self._training_tokens_per_epoch

    @training_tokens_per_epoch.setter
    def training_tokens_per_epoch(self, training_tokens_per_epoch):
        """Sets the training_tokens_per_epoch of this StatusForListModelCustomizationJobsOutput.


        :param training_tokens_per_epoch: The training_tokens_per_epoch of this StatusForListModelCustomizationJobsOutput.  # noqa: E501
        :type: int
        """

        self._training_tokens_per_epoch = training_tokens_per_epoch

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
        if issubclass(StatusForListModelCustomizationJobsOutput, dict):
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
        if not isinstance(other, StatusForListModelCustomizationJobsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StatusForListModelCustomizationJobsOutput):
            return True

        return self.to_dict() != other.to_dict()
