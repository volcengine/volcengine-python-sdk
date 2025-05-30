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


class FilterForListRepoImageVulnInput(object):
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
        'fixed': 'bool',
        'pkg_name': 'str',
        'pkg_type': 'str',
        'severity': 'list[str]',
        'title': 'str',
        'vuln_id': 'str',
        'vuln_tags': 'list[str]'
    }

    attribute_map = {
        'fixed': 'Fixed',
        'pkg_name': 'PkgName',
        'pkg_type': 'PkgType',
        'severity': 'Severity',
        'title': 'Title',
        'vuln_id': 'VulnID',
        'vuln_tags': 'VulnTags'
    }

    def __init__(self, fixed=None, pkg_name=None, pkg_type=None, severity=None, title=None, vuln_id=None, vuln_tags=None, _configuration=None):  # noqa: E501
        """FilterForListRepoImageVulnInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._fixed = None
        self._pkg_name = None
        self._pkg_type = None
        self._severity = None
        self._title = None
        self._vuln_id = None
        self._vuln_tags = None
        self.discriminator = None

        if fixed is not None:
            self.fixed = fixed
        if pkg_name is not None:
            self.pkg_name = pkg_name
        if pkg_type is not None:
            self.pkg_type = pkg_type
        if severity is not None:
            self.severity = severity
        if title is not None:
            self.title = title
        if vuln_id is not None:
            self.vuln_id = vuln_id
        if vuln_tags is not None:
            self.vuln_tags = vuln_tags

    @property
    def fixed(self):
        """Gets the fixed of this FilterForListRepoImageVulnInput.  # noqa: E501


        :return: The fixed of this FilterForListRepoImageVulnInput.  # noqa: E501
        :rtype: bool
        """
        return self._fixed

    @fixed.setter
    def fixed(self, fixed):
        """Sets the fixed of this FilterForListRepoImageVulnInput.


        :param fixed: The fixed of this FilterForListRepoImageVulnInput.  # noqa: E501
        :type: bool
        """

        self._fixed = fixed

    @property
    def pkg_name(self):
        """Gets the pkg_name of this FilterForListRepoImageVulnInput.  # noqa: E501


        :return: The pkg_name of this FilterForListRepoImageVulnInput.  # noqa: E501
        :rtype: str
        """
        return self._pkg_name

    @pkg_name.setter
    def pkg_name(self, pkg_name):
        """Sets the pkg_name of this FilterForListRepoImageVulnInput.


        :param pkg_name: The pkg_name of this FilterForListRepoImageVulnInput.  # noqa: E501
        :type: str
        """

        self._pkg_name = pkg_name

    @property
    def pkg_type(self):
        """Gets the pkg_type of this FilterForListRepoImageVulnInput.  # noqa: E501


        :return: The pkg_type of this FilterForListRepoImageVulnInput.  # noqa: E501
        :rtype: str
        """
        return self._pkg_type

    @pkg_type.setter
    def pkg_type(self, pkg_type):
        """Sets the pkg_type of this FilterForListRepoImageVulnInput.


        :param pkg_type: The pkg_type of this FilterForListRepoImageVulnInput.  # noqa: E501
        :type: str
        """

        self._pkg_type = pkg_type

    @property
    def severity(self):
        """Gets the severity of this FilterForListRepoImageVulnInput.  # noqa: E501


        :return: The severity of this FilterForListRepoImageVulnInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this FilterForListRepoImageVulnInput.


        :param severity: The severity of this FilterForListRepoImageVulnInput.  # noqa: E501
        :type: list[str]
        """

        self._severity = severity

    @property
    def title(self):
        """Gets the title of this FilterForListRepoImageVulnInput.  # noqa: E501


        :return: The title of this FilterForListRepoImageVulnInput.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this FilterForListRepoImageVulnInput.


        :param title: The title of this FilterForListRepoImageVulnInput.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def vuln_id(self):
        """Gets the vuln_id of this FilterForListRepoImageVulnInput.  # noqa: E501


        :return: The vuln_id of this FilterForListRepoImageVulnInput.  # noqa: E501
        :rtype: str
        """
        return self._vuln_id

    @vuln_id.setter
    def vuln_id(self, vuln_id):
        """Sets the vuln_id of this FilterForListRepoImageVulnInput.


        :param vuln_id: The vuln_id of this FilterForListRepoImageVulnInput.  # noqa: E501
        :type: str
        """

        self._vuln_id = vuln_id

    @property
    def vuln_tags(self):
        """Gets the vuln_tags of this FilterForListRepoImageVulnInput.  # noqa: E501


        :return: The vuln_tags of this FilterForListRepoImageVulnInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._vuln_tags

    @vuln_tags.setter
    def vuln_tags(self, vuln_tags):
        """Sets the vuln_tags of this FilterForListRepoImageVulnInput.


        :param vuln_tags: The vuln_tags of this FilterForListRepoImageVulnInput.  # noqa: E501
        :type: list[str]
        """

        self._vuln_tags = vuln_tags

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
        if issubclass(FilterForListRepoImageVulnInput, dict):
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
        if not isinstance(other, FilterForListRepoImageVulnInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FilterForListRepoImageVulnInput):
            return True

        return self.to_dict() != other.to_dict()
