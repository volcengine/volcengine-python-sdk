# coding: utf-8

"""
    sqs

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class MessageForReceiveMessageOutput(object):
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
        'message_body': 'str',
        'message_id': 'str',
        'receipt_handle': 'str'
    }

    attribute_map = {
        'message_body': 'MessageBody',
        'message_id': 'MessageId',
        'receipt_handle': 'ReceiptHandle'
    }

    def __init__(self, message_body=None, message_id=None, receipt_handle=None, _configuration=None):  # noqa: E501
        """MessageForReceiveMessageOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._message_body = None
        self._message_id = None
        self._receipt_handle = None
        self.discriminator = None

        if message_body is not None:
            self.message_body = message_body
        if message_id is not None:
            self.message_id = message_id
        if receipt_handle is not None:
            self.receipt_handle = receipt_handle

    @property
    def message_body(self):
        """Gets the message_body of this MessageForReceiveMessageOutput.  # noqa: E501


        :return: The message_body of this MessageForReceiveMessageOutput.  # noqa: E501
        :rtype: str
        """
        return self._message_body

    @message_body.setter
    def message_body(self, message_body):
        """Sets the message_body of this MessageForReceiveMessageOutput.


        :param message_body: The message_body of this MessageForReceiveMessageOutput.  # noqa: E501
        :type: str
        """

        self._message_body = message_body

    @property
    def message_id(self):
        """Gets the message_id of this MessageForReceiveMessageOutput.  # noqa: E501


        :return: The message_id of this MessageForReceiveMessageOutput.  # noqa: E501
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        """Sets the message_id of this MessageForReceiveMessageOutput.


        :param message_id: The message_id of this MessageForReceiveMessageOutput.  # noqa: E501
        :type: str
        """

        self._message_id = message_id

    @property
    def receipt_handle(self):
        """Gets the receipt_handle of this MessageForReceiveMessageOutput.  # noqa: E501


        :return: The receipt_handle of this MessageForReceiveMessageOutput.  # noqa: E501
        :rtype: str
        """
        return self._receipt_handle

    @receipt_handle.setter
    def receipt_handle(self, receipt_handle):
        """Sets the receipt_handle of this MessageForReceiveMessageOutput.


        :param receipt_handle: The receipt_handle of this MessageForReceiveMessageOutput.  # noqa: E501
        :type: str
        """

        self._receipt_handle = receipt_handle

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
        if issubclass(MessageForReceiveMessageOutput, dict):
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
        if not isinstance(other, MessageForReceiveMessageOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MessageForReceiveMessageOutput):
            return True

        return self.to_dict() != other.to_dict()
