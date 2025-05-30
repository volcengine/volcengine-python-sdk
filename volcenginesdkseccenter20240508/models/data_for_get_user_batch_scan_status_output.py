# coding: utf-8

"""
    seccenter20240508

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DataForGetUserBatchScanStatusOutput(object):
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
        'finish_time': 'int',
        'id': 'str',
        'process': 'int',
        'status': 'str'
    }

    attribute_map = {
        'finish_time': 'FinishTime',
        'id': 'ID',
        'process': 'Process',
        'status': 'Status'
    }

    def __init__(self, finish_time=None, id=None, process=None, status=None, _configuration=None):  # noqa: E501
        """DataForGetUserBatchScanStatusOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._finish_time = None
        self._id = None
        self._process = None
        self._status = None
        self.discriminator = None

        if finish_time is not None:
            self.finish_time = finish_time
        if id is not None:
            self.id = id
        if process is not None:
            self.process = process
        if status is not None:
            self.status = status

    @property
    def finish_time(self):
        """Gets the finish_time of this DataForGetUserBatchScanStatusOutput.  # noqa: E501


        :return: The finish_time of this DataForGetUserBatchScanStatusOutput.  # noqa: E501
        :rtype: int
        """
        return self._finish_time

    @finish_time.setter
    def finish_time(self, finish_time):
        """Sets the finish_time of this DataForGetUserBatchScanStatusOutput.


        :param finish_time: The finish_time of this DataForGetUserBatchScanStatusOutput.  # noqa: E501
        :type: int
        """

        self._finish_time = finish_time

    @property
    def id(self):
        """Gets the id of this DataForGetUserBatchScanStatusOutput.  # noqa: E501


        :return: The id of this DataForGetUserBatchScanStatusOutput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DataForGetUserBatchScanStatusOutput.


        :param id: The id of this DataForGetUserBatchScanStatusOutput.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def process(self):
        """Gets the process of this DataForGetUserBatchScanStatusOutput.  # noqa: E501


        :return: The process of this DataForGetUserBatchScanStatusOutput.  # noqa: E501
        :rtype: int
        """
        return self._process

    @process.setter
    def process(self, process):
        """Sets the process of this DataForGetUserBatchScanStatusOutput.


        :param process: The process of this DataForGetUserBatchScanStatusOutput.  # noqa: E501
        :type: int
        """

        self._process = process

    @property
    def status(self):
        """Gets the status of this DataForGetUserBatchScanStatusOutput.  # noqa: E501


        :return: The status of this DataForGetUserBatchScanStatusOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DataForGetUserBatchScanStatusOutput.


        :param status: The status of this DataForGetUserBatchScanStatusOutput.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(DataForGetUserBatchScanStatusOutput, dict):
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
        if not isinstance(other, DataForGetUserBatchScanStatusOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataForGetUserBatchScanStatusOutput):
            return True

        return self.to_dict() != other.to_dict()
