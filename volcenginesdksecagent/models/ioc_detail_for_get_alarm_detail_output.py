# coding: utf-8

"""
    sec_agent

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class IOCDetailForGetAlarmDetailOutput(object):
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
        'id': 'str',
        'is_malicious': 'bool',
        'type': 'str'
    }

    attribute_map = {
        'id': 'ID',
        'is_malicious': 'IsMalicious',
        'type': 'Type'
    }

    def __init__(self, id=None, is_malicious=None, type=None, _configuration=None):  # noqa: E501
        """IOCDetailForGetAlarmDetailOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._is_malicious = None
        self._type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if is_malicious is not None:
            self.is_malicious = is_malicious
        if type is not None:
            self.type = type

    @property
    def id(self):
        """Gets the id of this IOCDetailForGetAlarmDetailOutput.  # noqa: E501


        :return: The id of this IOCDetailForGetAlarmDetailOutput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IOCDetailForGetAlarmDetailOutput.


        :param id: The id of this IOCDetailForGetAlarmDetailOutput.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def is_malicious(self):
        """Gets the is_malicious of this IOCDetailForGetAlarmDetailOutput.  # noqa: E501


        :return: The is_malicious of this IOCDetailForGetAlarmDetailOutput.  # noqa: E501
        :rtype: bool
        """
        return self._is_malicious

    @is_malicious.setter
    def is_malicious(self, is_malicious):
        """Sets the is_malicious of this IOCDetailForGetAlarmDetailOutput.


        :param is_malicious: The is_malicious of this IOCDetailForGetAlarmDetailOutput.  # noqa: E501
        :type: bool
        """

        self._is_malicious = is_malicious

    @property
    def type(self):
        """Gets the type of this IOCDetailForGetAlarmDetailOutput.  # noqa: E501


        :return: The type of this IOCDetailForGetAlarmDetailOutput.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IOCDetailForGetAlarmDetailOutput.


        :param type: The type of this IOCDetailForGetAlarmDetailOutput.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(IOCDetailForGetAlarmDetailOutput, dict):
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
        if not isinstance(other, IOCDetailForGetAlarmDetailOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IOCDetailForGetAlarmDetailOutput):
            return True

        return self.to_dict() != other.to_dict()
