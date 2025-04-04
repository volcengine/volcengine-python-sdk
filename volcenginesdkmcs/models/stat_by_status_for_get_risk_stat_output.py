# coding: utf-8

"""
    mcs

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class StatByStatusForGetRiskStatOutput(object):
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
        'handled': 'int',
        'ignored': 'int',
        'total': 'int',
        'unhandled': 'int',
        'whitened': 'int'
    }

    attribute_map = {
        'handled': 'Handled',
        'ignored': 'Ignored',
        'total': 'Total',
        'unhandled': 'Unhandled',
        'whitened': 'Whitened'
    }

    def __init__(self, handled=None, ignored=None, total=None, unhandled=None, whitened=None, _configuration=None):  # noqa: E501
        """StatByStatusForGetRiskStatOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._handled = None
        self._ignored = None
        self._total = None
        self._unhandled = None
        self._whitened = None
        self.discriminator = None

        if handled is not None:
            self.handled = handled
        if ignored is not None:
            self.ignored = ignored
        if total is not None:
            self.total = total
        if unhandled is not None:
            self.unhandled = unhandled
        if whitened is not None:
            self.whitened = whitened

    @property
    def handled(self):
        """Gets the handled of this StatByStatusForGetRiskStatOutput.  # noqa: E501


        :return: The handled of this StatByStatusForGetRiskStatOutput.  # noqa: E501
        :rtype: int
        """
        return self._handled

    @handled.setter
    def handled(self, handled):
        """Sets the handled of this StatByStatusForGetRiskStatOutput.


        :param handled: The handled of this StatByStatusForGetRiskStatOutput.  # noqa: E501
        :type: int
        """

        self._handled = handled

    @property
    def ignored(self):
        """Gets the ignored of this StatByStatusForGetRiskStatOutput.  # noqa: E501


        :return: The ignored of this StatByStatusForGetRiskStatOutput.  # noqa: E501
        :rtype: int
        """
        return self._ignored

    @ignored.setter
    def ignored(self, ignored):
        """Sets the ignored of this StatByStatusForGetRiskStatOutput.


        :param ignored: The ignored of this StatByStatusForGetRiskStatOutput.  # noqa: E501
        :type: int
        """

        self._ignored = ignored

    @property
    def total(self):
        """Gets the total of this StatByStatusForGetRiskStatOutput.  # noqa: E501


        :return: The total of this StatByStatusForGetRiskStatOutput.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this StatByStatusForGetRiskStatOutput.


        :param total: The total of this StatByStatusForGetRiskStatOutput.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def unhandled(self):
        """Gets the unhandled of this StatByStatusForGetRiskStatOutput.  # noqa: E501


        :return: The unhandled of this StatByStatusForGetRiskStatOutput.  # noqa: E501
        :rtype: int
        """
        return self._unhandled

    @unhandled.setter
    def unhandled(self, unhandled):
        """Sets the unhandled of this StatByStatusForGetRiskStatOutput.


        :param unhandled: The unhandled of this StatByStatusForGetRiskStatOutput.  # noqa: E501
        :type: int
        """

        self._unhandled = unhandled

    @property
    def whitened(self):
        """Gets the whitened of this StatByStatusForGetRiskStatOutput.  # noqa: E501


        :return: The whitened of this StatByStatusForGetRiskStatOutput.  # noqa: E501
        :rtype: int
        """
        return self._whitened

    @whitened.setter
    def whitened(self, whitened):
        """Sets the whitened of this StatByStatusForGetRiskStatOutput.


        :param whitened: The whitened of this StatByStatusForGetRiskStatOutput.  # noqa: E501
        :type: int
        """

        self._whitened = whitened

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
        if issubclass(StatByStatusForGetRiskStatOutput, dict):
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
        if not isinstance(other, StatByStatusForGetRiskStatOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StatByStatusForGetRiskStatOutput):
            return True

        return self.to_dict() != other.to_dict()
