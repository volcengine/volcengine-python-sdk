# coding: utf-8

"""
    cr

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ItemForListRegistriesOutput(object):
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
        'charge_type': 'str',
        'create_time': 'str',
        'status': 'StatusForListRegistriesOutput',
        'type': 'str'
    }

    attribute_map = {
        'charge_type': 'ChargeType',
        'create_time': 'CreateTime',
        'status': 'Status',
        'type': 'Type'
    }

    def __init__(self, charge_type=None, create_time=None, status=None, type=None, _configuration=None):  # noqa: E501
        """ItemForListRegistriesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._charge_type = None
        self._create_time = None
        self._status = None
        self._type = None
        self.discriminator = None

        if charge_type is not None:
            self.charge_type = charge_type
        if create_time is not None:
            self.create_time = create_time
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type

    @property
    def charge_type(self):
        """Gets the charge_type of this ItemForListRegistriesOutput.  # noqa: E501


        :return: The charge_type of this ItemForListRegistriesOutput.  # noqa: E501
        :rtype: str
        """
        return self._charge_type

    @charge_type.setter
    def charge_type(self, charge_type):
        """Sets the charge_type of this ItemForListRegistriesOutput.


        :param charge_type: The charge_type of this ItemForListRegistriesOutput.  # noqa: E501
        :type: str
        """

        self._charge_type = charge_type

    @property
    def create_time(self):
        """Gets the create_time of this ItemForListRegistriesOutput.  # noqa: E501


        :return: The create_time of this ItemForListRegistriesOutput.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ItemForListRegistriesOutput.


        :param create_time: The create_time of this ItemForListRegistriesOutput.  # noqa: E501
        :type: str
        """

        self._create_time = create_time

    @property
    def status(self):
        """Gets the status of this ItemForListRegistriesOutput.  # noqa: E501


        :return: The status of this ItemForListRegistriesOutput.  # noqa: E501
        :rtype: StatusForListRegistriesOutput
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ItemForListRegistriesOutput.


        :param status: The status of this ItemForListRegistriesOutput.  # noqa: E501
        :type: StatusForListRegistriesOutput
        """

        self._status = status

    @property
    def type(self):
        """Gets the type of this ItemForListRegistriesOutput.  # noqa: E501


        :return: The type of this ItemForListRegistriesOutput.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ItemForListRegistriesOutput.


        :param type: The type of this ItemForListRegistriesOutput.  # noqa: E501
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
        if issubclass(ItemForListRegistriesOutput, dict):
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
        if not isinstance(other, ItemForListRegistriesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ItemForListRegistriesOutput):
            return True

        return self.to_dict() != other.to_dict()
