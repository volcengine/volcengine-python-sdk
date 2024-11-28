# coding: utf-8

"""
    escloud

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class TransferInfoForDescribeInstanceOutput(object):
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
        'forbid_stop': 'bool',
        'reduce_spec_config': 'ReduceSpecConfigForDescribeInstanceOutput',
        'transfer_progress': 'float',
        'transfer_status': 'str',
        'transfer_task_id': 'str'
    }

    attribute_map = {
        'forbid_stop': 'ForbidStop',
        'reduce_spec_config': 'ReduceSpecConfig',
        'transfer_progress': 'TransferProgress',
        'transfer_status': 'TransferStatus',
        'transfer_task_id': 'TransferTaskId'
    }

    def __init__(self, forbid_stop=None, reduce_spec_config=None, transfer_progress=None, transfer_status=None, transfer_task_id=None, _configuration=None):  # noqa: E501
        """TransferInfoForDescribeInstanceOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._forbid_stop = None
        self._reduce_spec_config = None
        self._transfer_progress = None
        self._transfer_status = None
        self._transfer_task_id = None
        self.discriminator = None

        if forbid_stop is not None:
            self.forbid_stop = forbid_stop
        if reduce_spec_config is not None:
            self.reduce_spec_config = reduce_spec_config
        if transfer_progress is not None:
            self.transfer_progress = transfer_progress
        if transfer_status is not None:
            self.transfer_status = transfer_status
        if transfer_task_id is not None:
            self.transfer_task_id = transfer_task_id

    @property
    def forbid_stop(self):
        """Gets the forbid_stop of this TransferInfoForDescribeInstanceOutput.  # noqa: E501


        :return: The forbid_stop of this TransferInfoForDescribeInstanceOutput.  # noqa: E501
        :rtype: bool
        """
        return self._forbid_stop

    @forbid_stop.setter
    def forbid_stop(self, forbid_stop):
        """Sets the forbid_stop of this TransferInfoForDescribeInstanceOutput.


        :param forbid_stop: The forbid_stop of this TransferInfoForDescribeInstanceOutput.  # noqa: E501
        :type: bool
        """

        self._forbid_stop = forbid_stop

    @property
    def reduce_spec_config(self):
        """Gets the reduce_spec_config of this TransferInfoForDescribeInstanceOutput.  # noqa: E501


        :return: The reduce_spec_config of this TransferInfoForDescribeInstanceOutput.  # noqa: E501
        :rtype: ReduceSpecConfigForDescribeInstanceOutput
        """
        return self._reduce_spec_config

    @reduce_spec_config.setter
    def reduce_spec_config(self, reduce_spec_config):
        """Sets the reduce_spec_config of this TransferInfoForDescribeInstanceOutput.


        :param reduce_spec_config: The reduce_spec_config of this TransferInfoForDescribeInstanceOutput.  # noqa: E501
        :type: ReduceSpecConfigForDescribeInstanceOutput
        """

        self._reduce_spec_config = reduce_spec_config

    @property
    def transfer_progress(self):
        """Gets the transfer_progress of this TransferInfoForDescribeInstanceOutput.  # noqa: E501


        :return: The transfer_progress of this TransferInfoForDescribeInstanceOutput.  # noqa: E501
        :rtype: float
        """
        return self._transfer_progress

    @transfer_progress.setter
    def transfer_progress(self, transfer_progress):
        """Sets the transfer_progress of this TransferInfoForDescribeInstanceOutput.


        :param transfer_progress: The transfer_progress of this TransferInfoForDescribeInstanceOutput.  # noqa: E501
        :type: float
        """

        self._transfer_progress = transfer_progress

    @property
    def transfer_status(self):
        """Gets the transfer_status of this TransferInfoForDescribeInstanceOutput.  # noqa: E501


        :return: The transfer_status of this TransferInfoForDescribeInstanceOutput.  # noqa: E501
        :rtype: str
        """
        return self._transfer_status

    @transfer_status.setter
    def transfer_status(self, transfer_status):
        """Sets the transfer_status of this TransferInfoForDescribeInstanceOutput.


        :param transfer_status: The transfer_status of this TransferInfoForDescribeInstanceOutput.  # noqa: E501
        :type: str
        """

        self._transfer_status = transfer_status

    @property
    def transfer_task_id(self):
        """Gets the transfer_task_id of this TransferInfoForDescribeInstanceOutput.  # noqa: E501


        :return: The transfer_task_id of this TransferInfoForDescribeInstanceOutput.  # noqa: E501
        :rtype: str
        """
        return self._transfer_task_id

    @transfer_task_id.setter
    def transfer_task_id(self, transfer_task_id):
        """Sets the transfer_task_id of this TransferInfoForDescribeInstanceOutput.


        :param transfer_task_id: The transfer_task_id of this TransferInfoForDescribeInstanceOutput.  # noqa: E501
        :type: str
        """

        self._transfer_task_id = transfer_task_id

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
        if issubclass(TransferInfoForDescribeInstanceOutput, dict):
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
        if not isinstance(other, TransferInfoForDescribeInstanceOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransferInfoForDescribeInstanceOutput):
            return True

        return self.to_dict() != other.to_dict()