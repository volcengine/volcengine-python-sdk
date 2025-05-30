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


class RiskForExportRepoImageAssetInput(object):
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
        'compl': 'list[str]',
        'senfile': 'list[str]',
        'virus': 'bool',
        'vuln': 'list[str]'
    }

    attribute_map = {
        'compl': 'Compl',
        'senfile': 'Senfile',
        'virus': 'Virus',
        'vuln': 'Vuln'
    }

    def __init__(self, compl=None, senfile=None, virus=None, vuln=None, _configuration=None):  # noqa: E501
        """RiskForExportRepoImageAssetInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._compl = None
        self._senfile = None
        self._virus = None
        self._vuln = None
        self.discriminator = None

        if compl is not None:
            self.compl = compl
        if senfile is not None:
            self.senfile = senfile
        if virus is not None:
            self.virus = virus
        if vuln is not None:
            self.vuln = vuln

    @property
    def compl(self):
        """Gets the compl of this RiskForExportRepoImageAssetInput.  # noqa: E501


        :return: The compl of this RiskForExportRepoImageAssetInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._compl

    @compl.setter
    def compl(self, compl):
        """Sets the compl of this RiskForExportRepoImageAssetInput.


        :param compl: The compl of this RiskForExportRepoImageAssetInput.  # noqa: E501
        :type: list[str]
        """

        self._compl = compl

    @property
    def senfile(self):
        """Gets the senfile of this RiskForExportRepoImageAssetInput.  # noqa: E501


        :return: The senfile of this RiskForExportRepoImageAssetInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._senfile

    @senfile.setter
    def senfile(self, senfile):
        """Sets the senfile of this RiskForExportRepoImageAssetInput.


        :param senfile: The senfile of this RiskForExportRepoImageAssetInput.  # noqa: E501
        :type: list[str]
        """

        self._senfile = senfile

    @property
    def virus(self):
        """Gets the virus of this RiskForExportRepoImageAssetInput.  # noqa: E501


        :return: The virus of this RiskForExportRepoImageAssetInput.  # noqa: E501
        :rtype: bool
        """
        return self._virus

    @virus.setter
    def virus(self, virus):
        """Sets the virus of this RiskForExportRepoImageAssetInput.


        :param virus: The virus of this RiskForExportRepoImageAssetInput.  # noqa: E501
        :type: bool
        """

        self._virus = virus

    @property
    def vuln(self):
        """Gets the vuln of this RiskForExportRepoImageAssetInput.  # noqa: E501


        :return: The vuln of this RiskForExportRepoImageAssetInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._vuln

    @vuln.setter
    def vuln(self, vuln):
        """Sets the vuln of this RiskForExportRepoImageAssetInput.


        :param vuln: The vuln of this RiskForExportRepoImageAssetInput.  # noqa: E501
        :type: list[str]
        """

        self._vuln = vuln

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
        if issubclass(RiskForExportRepoImageAssetInput, dict):
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
        if not isinstance(other, RiskForExportRepoImageAssetInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RiskForExportRepoImageAssetInput):
            return True

        return self.to_dict() != other.to_dict()
