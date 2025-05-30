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


class MultiLevelManagementForGetTenantQuotaOutput(object):
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
        'app_sec': 'AppSecForGetTenantQuotaOutput',
        'cluster_sec': 'ClusterSecForGetTenantQuotaOutput',
        'protect_host': 'ProtectHostForGetTenantQuotaOutput'
    }

    attribute_map = {
        'app_sec': 'AppSec',
        'cluster_sec': 'ClusterSec',
        'protect_host': 'ProtectHost'
    }

    def __init__(self, app_sec=None, cluster_sec=None, protect_host=None, _configuration=None):  # noqa: E501
        """MultiLevelManagementForGetTenantQuotaOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._app_sec = None
        self._cluster_sec = None
        self._protect_host = None
        self.discriminator = None

        if app_sec is not None:
            self.app_sec = app_sec
        if cluster_sec is not None:
            self.cluster_sec = cluster_sec
        if protect_host is not None:
            self.protect_host = protect_host

    @property
    def app_sec(self):
        """Gets the app_sec of this MultiLevelManagementForGetTenantQuotaOutput.  # noqa: E501


        :return: The app_sec of this MultiLevelManagementForGetTenantQuotaOutput.  # noqa: E501
        :rtype: AppSecForGetTenantQuotaOutput
        """
        return self._app_sec

    @app_sec.setter
    def app_sec(self, app_sec):
        """Sets the app_sec of this MultiLevelManagementForGetTenantQuotaOutput.


        :param app_sec: The app_sec of this MultiLevelManagementForGetTenantQuotaOutput.  # noqa: E501
        :type: AppSecForGetTenantQuotaOutput
        """

        self._app_sec = app_sec

    @property
    def cluster_sec(self):
        """Gets the cluster_sec of this MultiLevelManagementForGetTenantQuotaOutput.  # noqa: E501


        :return: The cluster_sec of this MultiLevelManagementForGetTenantQuotaOutput.  # noqa: E501
        :rtype: ClusterSecForGetTenantQuotaOutput
        """
        return self._cluster_sec

    @cluster_sec.setter
    def cluster_sec(self, cluster_sec):
        """Sets the cluster_sec of this MultiLevelManagementForGetTenantQuotaOutput.


        :param cluster_sec: The cluster_sec of this MultiLevelManagementForGetTenantQuotaOutput.  # noqa: E501
        :type: ClusterSecForGetTenantQuotaOutput
        """

        self._cluster_sec = cluster_sec

    @property
    def protect_host(self):
        """Gets the protect_host of this MultiLevelManagementForGetTenantQuotaOutput.  # noqa: E501


        :return: The protect_host of this MultiLevelManagementForGetTenantQuotaOutput.  # noqa: E501
        :rtype: ProtectHostForGetTenantQuotaOutput
        """
        return self._protect_host

    @protect_host.setter
    def protect_host(self, protect_host):
        """Sets the protect_host of this MultiLevelManagementForGetTenantQuotaOutput.


        :param protect_host: The protect_host of this MultiLevelManagementForGetTenantQuotaOutput.  # noqa: E501
        :type: ProtectHostForGetTenantQuotaOutput
        """

        self._protect_host = protect_host

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
        if issubclass(MultiLevelManagementForGetTenantQuotaOutput, dict):
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
        if not isinstance(other, MultiLevelManagementForGetTenantQuotaOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MultiLevelManagementForGetTenantQuotaOutput):
            return True

        return self.to_dict() != other.to_dict()
