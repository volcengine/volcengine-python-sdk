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


class BasicDetailForGetTaskResultOutput(object):
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
        'assertions': 'list[AssertionForGetTaskResultOutput]',
        'ch_uk': 'str',
        'client_info': 'ClientInfoForGetTaskResultOutput',
        'error_msg': 'str',
        'target_info': 'TargetInfoForGetTaskResultOutput',
        'timestamp': 'int',
        'usability_info': 'UsabilityInfoForGetTaskResultOutput'
    }

    attribute_map = {
        'assertions': 'Assertions',
        'ch_uk': 'ChUk',
        'client_info': 'ClientInfo',
        'error_msg': 'ErrorMsg',
        'target_info': 'TargetInfo',
        'timestamp': 'Timestamp',
        'usability_info': 'UsabilityInfo'
    }

    def __init__(self, assertions=None, ch_uk=None, client_info=None, error_msg=None, target_info=None, timestamp=None, usability_info=None, _configuration=None):  # noqa: E501
        """BasicDetailForGetTaskResultOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._assertions = None
        self._ch_uk = None
        self._client_info = None
        self._error_msg = None
        self._target_info = None
        self._timestamp = None
        self._usability_info = None
        self.discriminator = None

        if assertions is not None:
            self.assertions = assertions
        if ch_uk is not None:
            self.ch_uk = ch_uk
        if client_info is not None:
            self.client_info = client_info
        if error_msg is not None:
            self.error_msg = error_msg
        if target_info is not None:
            self.target_info = target_info
        if timestamp is not None:
            self.timestamp = timestamp
        if usability_info is not None:
            self.usability_info = usability_info

    @property
    def assertions(self):
        """Gets the assertions of this BasicDetailForGetTaskResultOutput.  # noqa: E501


        :return: The assertions of this BasicDetailForGetTaskResultOutput.  # noqa: E501
        :rtype: list[AssertionForGetTaskResultOutput]
        """
        return self._assertions

    @assertions.setter
    def assertions(self, assertions):
        """Sets the assertions of this BasicDetailForGetTaskResultOutput.


        :param assertions: The assertions of this BasicDetailForGetTaskResultOutput.  # noqa: E501
        :type: list[AssertionForGetTaskResultOutput]
        """

        self._assertions = assertions

    @property
    def ch_uk(self):
        """Gets the ch_uk of this BasicDetailForGetTaskResultOutput.  # noqa: E501


        :return: The ch_uk of this BasicDetailForGetTaskResultOutput.  # noqa: E501
        :rtype: str
        """
        return self._ch_uk

    @ch_uk.setter
    def ch_uk(self, ch_uk):
        """Sets the ch_uk of this BasicDetailForGetTaskResultOutput.


        :param ch_uk: The ch_uk of this BasicDetailForGetTaskResultOutput.  # noqa: E501
        :type: str
        """

        self._ch_uk = ch_uk

    @property
    def client_info(self):
        """Gets the client_info of this BasicDetailForGetTaskResultOutput.  # noqa: E501


        :return: The client_info of this BasicDetailForGetTaskResultOutput.  # noqa: E501
        :rtype: ClientInfoForGetTaskResultOutput
        """
        return self._client_info

    @client_info.setter
    def client_info(self, client_info):
        """Sets the client_info of this BasicDetailForGetTaskResultOutput.


        :param client_info: The client_info of this BasicDetailForGetTaskResultOutput.  # noqa: E501
        :type: ClientInfoForGetTaskResultOutput
        """

        self._client_info = client_info

    @property
    def error_msg(self):
        """Gets the error_msg of this BasicDetailForGetTaskResultOutput.  # noqa: E501


        :return: The error_msg of this BasicDetailForGetTaskResultOutput.  # noqa: E501
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this BasicDetailForGetTaskResultOutput.


        :param error_msg: The error_msg of this BasicDetailForGetTaskResultOutput.  # noqa: E501
        :type: str
        """

        self._error_msg = error_msg

    @property
    def target_info(self):
        """Gets the target_info of this BasicDetailForGetTaskResultOutput.  # noqa: E501


        :return: The target_info of this BasicDetailForGetTaskResultOutput.  # noqa: E501
        :rtype: TargetInfoForGetTaskResultOutput
        """
        return self._target_info

    @target_info.setter
    def target_info(self, target_info):
        """Sets the target_info of this BasicDetailForGetTaskResultOutput.


        :param target_info: The target_info of this BasicDetailForGetTaskResultOutput.  # noqa: E501
        :type: TargetInfoForGetTaskResultOutput
        """

        self._target_info = target_info

    @property
    def timestamp(self):
        """Gets the timestamp of this BasicDetailForGetTaskResultOutput.  # noqa: E501


        :return: The timestamp of this BasicDetailForGetTaskResultOutput.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this BasicDetailForGetTaskResultOutput.


        :param timestamp: The timestamp of this BasicDetailForGetTaskResultOutput.  # noqa: E501
        :type: int
        """

        self._timestamp = timestamp

    @property
    def usability_info(self):
        """Gets the usability_info of this BasicDetailForGetTaskResultOutput.  # noqa: E501


        :return: The usability_info of this BasicDetailForGetTaskResultOutput.  # noqa: E501
        :rtype: UsabilityInfoForGetTaskResultOutput
        """
        return self._usability_info

    @usability_info.setter
    def usability_info(self, usability_info):
        """Sets the usability_info of this BasicDetailForGetTaskResultOutput.


        :param usability_info: The usability_info of this BasicDetailForGetTaskResultOutput.  # noqa: E501
        :type: UsabilityInfoForGetTaskResultOutput
        """

        self._usability_info = usability_info

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
        if issubclass(BasicDetailForGetTaskResultOutput, dict):
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
        if not isinstance(other, BasicDetailForGetTaskResultOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BasicDetailForGetTaskResultOutput):
            return True

        return self.to_dict() != other.to_dict()
