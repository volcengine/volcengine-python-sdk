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


class VulnForGetRiskOutput(object):
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
        'affected_assets_cnt': 'int',
        'applicable_vendors': 'list[str]',
        'associated_cves': 'list[AssociatedCveForGetRiskOutput]',
        'attached_resource_risk_status': 'str',
        'vuln_category': 'str',
        'vuln_cvss': 'VulnCvssForGetRiskOutput',
        'vuln_desc': 'str',
        'vuln_solution': 'str',
        'vuln_title': 'str',
        'vuln_view_id': 'str',
        'vulnerable_soft_packages': 'list[VulnerableSoftPackageForGetRiskOutput]'
    }

    attribute_map = {
        'affected_assets_cnt': 'AffectedAssetsCnt',
        'applicable_vendors': 'ApplicableVendors',
        'associated_cves': 'AssociatedCves',
        'attached_resource_risk_status': 'AttachedResourceRiskStatus',
        'vuln_category': 'VulnCategory',
        'vuln_cvss': 'VulnCvss',
        'vuln_desc': 'VulnDesc',
        'vuln_solution': 'VulnSolution',
        'vuln_title': 'VulnTitle',
        'vuln_view_id': 'VulnViewID',
        'vulnerable_soft_packages': 'VulnerableSoftPackages'
    }

    def __init__(self, affected_assets_cnt=None, applicable_vendors=None, associated_cves=None, attached_resource_risk_status=None, vuln_category=None, vuln_cvss=None, vuln_desc=None, vuln_solution=None, vuln_title=None, vuln_view_id=None, vulnerable_soft_packages=None, _configuration=None):  # noqa: E501
        """VulnForGetRiskOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._affected_assets_cnt = None
        self._applicable_vendors = None
        self._associated_cves = None
        self._attached_resource_risk_status = None
        self._vuln_category = None
        self._vuln_cvss = None
        self._vuln_desc = None
        self._vuln_solution = None
        self._vuln_title = None
        self._vuln_view_id = None
        self._vulnerable_soft_packages = None
        self.discriminator = None

        if affected_assets_cnt is not None:
            self.affected_assets_cnt = affected_assets_cnt
        if applicable_vendors is not None:
            self.applicable_vendors = applicable_vendors
        if associated_cves is not None:
            self.associated_cves = associated_cves
        if attached_resource_risk_status is not None:
            self.attached_resource_risk_status = attached_resource_risk_status
        if vuln_category is not None:
            self.vuln_category = vuln_category
        if vuln_cvss is not None:
            self.vuln_cvss = vuln_cvss
        if vuln_desc is not None:
            self.vuln_desc = vuln_desc
        if vuln_solution is not None:
            self.vuln_solution = vuln_solution
        if vuln_title is not None:
            self.vuln_title = vuln_title
        if vuln_view_id is not None:
            self.vuln_view_id = vuln_view_id
        if vulnerable_soft_packages is not None:
            self.vulnerable_soft_packages = vulnerable_soft_packages

    @property
    def affected_assets_cnt(self):
        """Gets the affected_assets_cnt of this VulnForGetRiskOutput.  # noqa: E501


        :return: The affected_assets_cnt of this VulnForGetRiskOutput.  # noqa: E501
        :rtype: int
        """
        return self._affected_assets_cnt

    @affected_assets_cnt.setter
    def affected_assets_cnt(self, affected_assets_cnt):
        """Sets the affected_assets_cnt of this VulnForGetRiskOutput.


        :param affected_assets_cnt: The affected_assets_cnt of this VulnForGetRiskOutput.  # noqa: E501
        :type: int
        """

        self._affected_assets_cnt = affected_assets_cnt

    @property
    def applicable_vendors(self):
        """Gets the applicable_vendors of this VulnForGetRiskOutput.  # noqa: E501


        :return: The applicable_vendors of this VulnForGetRiskOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._applicable_vendors

    @applicable_vendors.setter
    def applicable_vendors(self, applicable_vendors):
        """Sets the applicable_vendors of this VulnForGetRiskOutput.


        :param applicable_vendors: The applicable_vendors of this VulnForGetRiskOutput.  # noqa: E501
        :type: list[str]
        """

        self._applicable_vendors = applicable_vendors

    @property
    def associated_cves(self):
        """Gets the associated_cves of this VulnForGetRiskOutput.  # noqa: E501


        :return: The associated_cves of this VulnForGetRiskOutput.  # noqa: E501
        :rtype: list[AssociatedCveForGetRiskOutput]
        """
        return self._associated_cves

    @associated_cves.setter
    def associated_cves(self, associated_cves):
        """Sets the associated_cves of this VulnForGetRiskOutput.


        :param associated_cves: The associated_cves of this VulnForGetRiskOutput.  # noqa: E501
        :type: list[AssociatedCveForGetRiskOutput]
        """

        self._associated_cves = associated_cves

    @property
    def attached_resource_risk_status(self):
        """Gets the attached_resource_risk_status of this VulnForGetRiskOutput.  # noqa: E501


        :return: The attached_resource_risk_status of this VulnForGetRiskOutput.  # noqa: E501
        :rtype: str
        """
        return self._attached_resource_risk_status

    @attached_resource_risk_status.setter
    def attached_resource_risk_status(self, attached_resource_risk_status):
        """Sets the attached_resource_risk_status of this VulnForGetRiskOutput.


        :param attached_resource_risk_status: The attached_resource_risk_status of this VulnForGetRiskOutput.  # noqa: E501
        :type: str
        """

        self._attached_resource_risk_status = attached_resource_risk_status

    @property
    def vuln_category(self):
        """Gets the vuln_category of this VulnForGetRiskOutput.  # noqa: E501


        :return: The vuln_category of this VulnForGetRiskOutput.  # noqa: E501
        :rtype: str
        """
        return self._vuln_category

    @vuln_category.setter
    def vuln_category(self, vuln_category):
        """Sets the vuln_category of this VulnForGetRiskOutput.


        :param vuln_category: The vuln_category of this VulnForGetRiskOutput.  # noqa: E501
        :type: str
        """

        self._vuln_category = vuln_category

    @property
    def vuln_cvss(self):
        """Gets the vuln_cvss of this VulnForGetRiskOutput.  # noqa: E501


        :return: The vuln_cvss of this VulnForGetRiskOutput.  # noqa: E501
        :rtype: VulnCvssForGetRiskOutput
        """
        return self._vuln_cvss

    @vuln_cvss.setter
    def vuln_cvss(self, vuln_cvss):
        """Sets the vuln_cvss of this VulnForGetRiskOutput.


        :param vuln_cvss: The vuln_cvss of this VulnForGetRiskOutput.  # noqa: E501
        :type: VulnCvssForGetRiskOutput
        """

        self._vuln_cvss = vuln_cvss

    @property
    def vuln_desc(self):
        """Gets the vuln_desc of this VulnForGetRiskOutput.  # noqa: E501


        :return: The vuln_desc of this VulnForGetRiskOutput.  # noqa: E501
        :rtype: str
        """
        return self._vuln_desc

    @vuln_desc.setter
    def vuln_desc(self, vuln_desc):
        """Sets the vuln_desc of this VulnForGetRiskOutput.


        :param vuln_desc: The vuln_desc of this VulnForGetRiskOutput.  # noqa: E501
        :type: str
        """

        self._vuln_desc = vuln_desc

    @property
    def vuln_solution(self):
        """Gets the vuln_solution of this VulnForGetRiskOutput.  # noqa: E501


        :return: The vuln_solution of this VulnForGetRiskOutput.  # noqa: E501
        :rtype: str
        """
        return self._vuln_solution

    @vuln_solution.setter
    def vuln_solution(self, vuln_solution):
        """Sets the vuln_solution of this VulnForGetRiskOutput.


        :param vuln_solution: The vuln_solution of this VulnForGetRiskOutput.  # noqa: E501
        :type: str
        """

        self._vuln_solution = vuln_solution

    @property
    def vuln_title(self):
        """Gets the vuln_title of this VulnForGetRiskOutput.  # noqa: E501


        :return: The vuln_title of this VulnForGetRiskOutput.  # noqa: E501
        :rtype: str
        """
        return self._vuln_title

    @vuln_title.setter
    def vuln_title(self, vuln_title):
        """Sets the vuln_title of this VulnForGetRiskOutput.


        :param vuln_title: The vuln_title of this VulnForGetRiskOutput.  # noqa: E501
        :type: str
        """

        self._vuln_title = vuln_title

    @property
    def vuln_view_id(self):
        """Gets the vuln_view_id of this VulnForGetRiskOutput.  # noqa: E501


        :return: The vuln_view_id of this VulnForGetRiskOutput.  # noqa: E501
        :rtype: str
        """
        return self._vuln_view_id

    @vuln_view_id.setter
    def vuln_view_id(self, vuln_view_id):
        """Sets the vuln_view_id of this VulnForGetRiskOutput.


        :param vuln_view_id: The vuln_view_id of this VulnForGetRiskOutput.  # noqa: E501
        :type: str
        """

        self._vuln_view_id = vuln_view_id

    @property
    def vulnerable_soft_packages(self):
        """Gets the vulnerable_soft_packages of this VulnForGetRiskOutput.  # noqa: E501


        :return: The vulnerable_soft_packages of this VulnForGetRiskOutput.  # noqa: E501
        :rtype: list[VulnerableSoftPackageForGetRiskOutput]
        """
        return self._vulnerable_soft_packages

    @vulnerable_soft_packages.setter
    def vulnerable_soft_packages(self, vulnerable_soft_packages):
        """Sets the vulnerable_soft_packages of this VulnForGetRiskOutput.


        :param vulnerable_soft_packages: The vulnerable_soft_packages of this VulnForGetRiskOutput.  # noqa: E501
        :type: list[VulnerableSoftPackageForGetRiskOutput]
        """

        self._vulnerable_soft_packages = vulnerable_soft_packages

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
        if issubclass(VulnForGetRiskOutput, dict):
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
        if not isinstance(other, VulnForGetRiskOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VulnForGetRiskOutput):
            return True

        return self.to_dict() != other.to_dict()
