# coding: utf-8

"""
    storage_ebs

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeAutoSnapshotPolicyRequest(object):
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
        'auto_snapshot_policy_ids': 'list[str]',
        'page_number': 'int',
        'page_size': 'int',
        'project_name': 'str'
    }

    attribute_map = {
        'auto_snapshot_policy_ids': 'AutoSnapshotPolicyIds',
        'page_number': 'PageNumber',
        'page_size': 'PageSize',
        'project_name': 'ProjectName'
    }

    def __init__(self, auto_snapshot_policy_ids=None, page_number=None, page_size=None, project_name=None, _configuration=None):  # noqa: E501
        """DescribeAutoSnapshotPolicyRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._auto_snapshot_policy_ids = None
        self._page_number = None
        self._page_size = None
        self._project_name = None
        self.discriminator = None

        if auto_snapshot_policy_ids is not None:
            self.auto_snapshot_policy_ids = auto_snapshot_policy_ids
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if project_name is not None:
            self.project_name = project_name

    @property
    def auto_snapshot_policy_ids(self):
        """Gets the auto_snapshot_policy_ids of this DescribeAutoSnapshotPolicyRequest.  # noqa: E501


        :return: The auto_snapshot_policy_ids of this DescribeAutoSnapshotPolicyRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._auto_snapshot_policy_ids

    @auto_snapshot_policy_ids.setter
    def auto_snapshot_policy_ids(self, auto_snapshot_policy_ids):
        """Sets the auto_snapshot_policy_ids of this DescribeAutoSnapshotPolicyRequest.


        :param auto_snapshot_policy_ids: The auto_snapshot_policy_ids of this DescribeAutoSnapshotPolicyRequest.  # noqa: E501
        :type: list[str]
        """

        self._auto_snapshot_policy_ids = auto_snapshot_policy_ids

    @property
    def page_number(self):
        """Gets the page_number of this DescribeAutoSnapshotPolicyRequest.  # noqa: E501


        :return: The page_number of this DescribeAutoSnapshotPolicyRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this DescribeAutoSnapshotPolicyRequest.


        :param page_number: The page_number of this DescribeAutoSnapshotPolicyRequest.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this DescribeAutoSnapshotPolicyRequest.  # noqa: E501


        :return: The page_size of this DescribeAutoSnapshotPolicyRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this DescribeAutoSnapshotPolicyRequest.


        :param page_size: The page_size of this DescribeAutoSnapshotPolicyRequest.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                page_size is not None and page_size > 100):  # noqa: E501
            raise ValueError("Invalid value for `page_size`, must be a value less than or equal to `100`")  # noqa: E501

        self._page_size = page_size

    @property
    def project_name(self):
        """Gets the project_name of this DescribeAutoSnapshotPolicyRequest.  # noqa: E501


        :return: The project_name of this DescribeAutoSnapshotPolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this DescribeAutoSnapshotPolicyRequest.


        :param project_name: The project_name of this DescribeAutoSnapshotPolicyRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

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
        if issubclass(DescribeAutoSnapshotPolicyRequest, dict):
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
        if not isinstance(other, DescribeAutoSnapshotPolicyRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeAutoSnapshotPolicyRequest):
            return True

        return self.to_dict() != other.to_dict()
