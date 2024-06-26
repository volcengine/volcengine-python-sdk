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


class DeleteTagsResponse(object):
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
        'failures': 'list[FailureForDeleteTagsOutput]',
        'successes': 'list[SuccessForDeleteTagsOutput]'
    }

    attribute_map = {
        'failures': 'Failures',
        'successes': 'Successes'
    }

    def __init__(self, failures=None, successes=None, _configuration=None):  # noqa: E501
        """DeleteTagsResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._failures = None
        self._successes = None
        self.discriminator = None

        if failures is not None:
            self.failures = failures
        if successes is not None:
            self.successes = successes

    @property
    def failures(self):
        """Gets the failures of this DeleteTagsResponse.  # noqa: E501


        :return: The failures of this DeleteTagsResponse.  # noqa: E501
        :rtype: list[FailureForDeleteTagsOutput]
        """
        return self._failures

    @failures.setter
    def failures(self, failures):
        """Sets the failures of this DeleteTagsResponse.


        :param failures: The failures of this DeleteTagsResponse.  # noqa: E501
        :type: list[FailureForDeleteTagsOutput]
        """

        self._failures = failures

    @property
    def successes(self):
        """Gets the successes of this DeleteTagsResponse.  # noqa: E501


        :return: The successes of this DeleteTagsResponse.  # noqa: E501
        :rtype: list[SuccessForDeleteTagsOutput]
        """
        return self._successes

    @successes.setter
    def successes(self, successes):
        """Sets the successes of this DeleteTagsResponse.


        :param successes: The successes of this DeleteTagsResponse.  # noqa: E501
        :type: list[SuccessForDeleteTagsOutput]
        """

        self._successes = successes

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
        if issubclass(DeleteTagsResponse, dict):
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
        if not isinstance(other, DeleteTagsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeleteTagsResponse):
            return True

        return self.to_dict() != other.to_dict()
