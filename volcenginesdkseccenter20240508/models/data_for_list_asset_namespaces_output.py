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


class DataForListAssetNamespacesOutput(object):
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
        'cluster_id': 'str',
        'creation_time': 'int',
        'external_cluster_id': 'str',
        'has_audit_risk': 'bool',
        'id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'cluster_id': 'ClusterID',
        'creation_time': 'CreationTime',
        'external_cluster_id': 'ExternalClusterID',
        'has_audit_risk': 'HasAuditRisk',
        'id': 'ID',
        'name': 'Name'
    }

    def __init__(self, cluster_id=None, creation_time=None, external_cluster_id=None, has_audit_risk=None, id=None, name=None, _configuration=None):  # noqa: E501
        """DataForListAssetNamespacesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cluster_id = None
        self._creation_time = None
        self._external_cluster_id = None
        self._has_audit_risk = None
        self._id = None
        self._name = None
        self.discriminator = None

        if cluster_id is not None:
            self.cluster_id = cluster_id
        if creation_time is not None:
            self.creation_time = creation_time
        if external_cluster_id is not None:
            self.external_cluster_id = external_cluster_id
        if has_audit_risk is not None:
            self.has_audit_risk = has_audit_risk
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name

    @property
    def cluster_id(self):
        """Gets the cluster_id of this DataForListAssetNamespacesOutput.  # noqa: E501


        :return: The cluster_id of this DataForListAssetNamespacesOutput.  # noqa: E501
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this DataForListAssetNamespacesOutput.


        :param cluster_id: The cluster_id of this DataForListAssetNamespacesOutput.  # noqa: E501
        :type: str
        """

        self._cluster_id = cluster_id

    @property
    def creation_time(self):
        """Gets the creation_time of this DataForListAssetNamespacesOutput.  # noqa: E501


        :return: The creation_time of this DataForListAssetNamespacesOutput.  # noqa: E501
        :rtype: int
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this DataForListAssetNamespacesOutput.


        :param creation_time: The creation_time of this DataForListAssetNamespacesOutput.  # noqa: E501
        :type: int
        """

        self._creation_time = creation_time

    @property
    def external_cluster_id(self):
        """Gets the external_cluster_id of this DataForListAssetNamespacesOutput.  # noqa: E501


        :return: The external_cluster_id of this DataForListAssetNamespacesOutput.  # noqa: E501
        :rtype: str
        """
        return self._external_cluster_id

    @external_cluster_id.setter
    def external_cluster_id(self, external_cluster_id):
        """Sets the external_cluster_id of this DataForListAssetNamespacesOutput.


        :param external_cluster_id: The external_cluster_id of this DataForListAssetNamespacesOutput.  # noqa: E501
        :type: str
        """

        self._external_cluster_id = external_cluster_id

    @property
    def has_audit_risk(self):
        """Gets the has_audit_risk of this DataForListAssetNamespacesOutput.  # noqa: E501


        :return: The has_audit_risk of this DataForListAssetNamespacesOutput.  # noqa: E501
        :rtype: bool
        """
        return self._has_audit_risk

    @has_audit_risk.setter
    def has_audit_risk(self, has_audit_risk):
        """Sets the has_audit_risk of this DataForListAssetNamespacesOutput.


        :param has_audit_risk: The has_audit_risk of this DataForListAssetNamespacesOutput.  # noqa: E501
        :type: bool
        """

        self._has_audit_risk = has_audit_risk

    @property
    def id(self):
        """Gets the id of this DataForListAssetNamespacesOutput.  # noqa: E501


        :return: The id of this DataForListAssetNamespacesOutput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DataForListAssetNamespacesOutput.


        :param id: The id of this DataForListAssetNamespacesOutput.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this DataForListAssetNamespacesOutput.  # noqa: E501


        :return: The name of this DataForListAssetNamespacesOutput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DataForListAssetNamespacesOutput.


        :param name: The name of this DataForListAssetNamespacesOutput.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(DataForListAssetNamespacesOutput, dict):
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
        if not isinstance(other, DataForListAssetNamespacesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataForListAssetNamespacesOutput):
            return True

        return self.to_dict() != other.to_dict()
