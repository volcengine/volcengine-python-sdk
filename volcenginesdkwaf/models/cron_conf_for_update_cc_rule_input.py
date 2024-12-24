# coding: utf-8

"""
    waf

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class CronConfForUpdateCCRuleInput(object):
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
        'crontab': 'str',
        'path_threshold': 'int',
        'single_threshold': 'int'
    }

    attribute_map = {
        'crontab': 'Crontab',
        'path_threshold': 'PathThreshold',
        'single_threshold': 'SingleThreshold'
    }

    def __init__(self, crontab=None, path_threshold=None, single_threshold=None, _configuration=None):  # noqa: E501
        """CronConfForUpdateCCRuleInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._crontab = None
        self._path_threshold = None
        self._single_threshold = None
        self.discriminator = None

        if crontab is not None:
            self.crontab = crontab
        if path_threshold is not None:
            self.path_threshold = path_threshold
        if single_threshold is not None:
            self.single_threshold = single_threshold

    @property
    def crontab(self):
        """Gets the crontab of this CronConfForUpdateCCRuleInput.  # noqa: E501


        :return: The crontab of this CronConfForUpdateCCRuleInput.  # noqa: E501
        :rtype: str
        """
        return self._crontab

    @crontab.setter
    def crontab(self, crontab):
        """Sets the crontab of this CronConfForUpdateCCRuleInput.


        :param crontab: The crontab of this CronConfForUpdateCCRuleInput.  # noqa: E501
        :type: str
        """

        self._crontab = crontab

    @property
    def path_threshold(self):
        """Gets the path_threshold of this CronConfForUpdateCCRuleInput.  # noqa: E501


        :return: The path_threshold of this CronConfForUpdateCCRuleInput.  # noqa: E501
        :rtype: int
        """
        return self._path_threshold

    @path_threshold.setter
    def path_threshold(self, path_threshold):
        """Sets the path_threshold of this CronConfForUpdateCCRuleInput.


        :param path_threshold: The path_threshold of this CronConfForUpdateCCRuleInput.  # noqa: E501
        :type: int
        """

        self._path_threshold = path_threshold

    @property
    def single_threshold(self):
        """Gets the single_threshold of this CronConfForUpdateCCRuleInput.  # noqa: E501


        :return: The single_threshold of this CronConfForUpdateCCRuleInput.  # noqa: E501
        :rtype: int
        """
        return self._single_threshold

    @single_threshold.setter
    def single_threshold(self, single_threshold):
        """Sets the single_threshold of this CronConfForUpdateCCRuleInput.


        :param single_threshold: The single_threshold of this CronConfForUpdateCCRuleInput.  # noqa: E501
        :type: int
        """

        self._single_threshold = single_threshold

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
        if issubclass(CronConfForUpdateCCRuleInput, dict):
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
        if not isinstance(other, CronConfForUpdateCCRuleInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CronConfForUpdateCCRuleInput):
            return True

        return self.to_dict() != other.to_dict()
