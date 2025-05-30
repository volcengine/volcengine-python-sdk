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


class EditVulnScanConfigRequest(object):
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
        'agent_id_list': 'list[str]',
        'asset_ids': 'list[str]',
        'asset_type': 'str',
        'if_all_host': 'bool',
        'leaf_group_ids': 'list[str]',
        'scan_type': 'ScanTypeForEditVulnScanConfigInput',
        'top_group_id': 'str'
    }

    attribute_map = {
        'agent_id_list': 'AgentIDList',
        'asset_ids': 'AssetIDs',
        'asset_type': 'AssetType',
        'if_all_host': 'IfAllHost',
        'leaf_group_ids': 'LeafGroupIDs',
        'scan_type': 'ScanType',
        'top_group_id': 'TopGroupID'
    }

    def __init__(self, agent_id_list=None, asset_ids=None, asset_type=None, if_all_host=None, leaf_group_ids=None, scan_type=None, top_group_id=None, _configuration=None):  # noqa: E501
        """EditVulnScanConfigRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._agent_id_list = None
        self._asset_ids = None
        self._asset_type = None
        self._if_all_host = None
        self._leaf_group_ids = None
        self._scan_type = None
        self._top_group_id = None
        self.discriminator = None

        if agent_id_list is not None:
            self.agent_id_list = agent_id_list
        if asset_ids is not None:
            self.asset_ids = asset_ids
        if asset_type is not None:
            self.asset_type = asset_type
        if if_all_host is not None:
            self.if_all_host = if_all_host
        if leaf_group_ids is not None:
            self.leaf_group_ids = leaf_group_ids
        if scan_type is not None:
            self.scan_type = scan_type
        if top_group_id is not None:
            self.top_group_id = top_group_id

    @property
    def agent_id_list(self):
        """Gets the agent_id_list of this EditVulnScanConfigRequest.  # noqa: E501


        :return: The agent_id_list of this EditVulnScanConfigRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._agent_id_list

    @agent_id_list.setter
    def agent_id_list(self, agent_id_list):
        """Sets the agent_id_list of this EditVulnScanConfigRequest.


        :param agent_id_list: The agent_id_list of this EditVulnScanConfigRequest.  # noqa: E501
        :type: list[str]
        """

        self._agent_id_list = agent_id_list

    @property
    def asset_ids(self):
        """Gets the asset_ids of this EditVulnScanConfigRequest.  # noqa: E501


        :return: The asset_ids of this EditVulnScanConfigRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._asset_ids

    @asset_ids.setter
    def asset_ids(self, asset_ids):
        """Sets the asset_ids of this EditVulnScanConfigRequest.


        :param asset_ids: The asset_ids of this EditVulnScanConfigRequest.  # noqa: E501
        :type: list[str]
        """

        self._asset_ids = asset_ids

    @property
    def asset_type(self):
        """Gets the asset_type of this EditVulnScanConfigRequest.  # noqa: E501


        :return: The asset_type of this EditVulnScanConfigRequest.  # noqa: E501
        :rtype: str
        """
        return self._asset_type

    @asset_type.setter
    def asset_type(self, asset_type):
        """Sets the asset_type of this EditVulnScanConfigRequest.


        :param asset_type: The asset_type of this EditVulnScanConfigRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["Host", "Dev"]  # noqa: E501
        if (self._configuration.client_side_validation and
                asset_type not in allowed_values):
            raise ValueError(
                "Invalid value for `asset_type` ({0}), must be one of {1}"  # noqa: E501
                .format(asset_type, allowed_values)
            )

        self._asset_type = asset_type

    @property
    def if_all_host(self):
        """Gets the if_all_host of this EditVulnScanConfigRequest.  # noqa: E501


        :return: The if_all_host of this EditVulnScanConfigRequest.  # noqa: E501
        :rtype: bool
        """
        return self._if_all_host

    @if_all_host.setter
    def if_all_host(self, if_all_host):
        """Sets the if_all_host of this EditVulnScanConfigRequest.


        :param if_all_host: The if_all_host of this EditVulnScanConfigRequest.  # noqa: E501
        :type: bool
        """

        self._if_all_host = if_all_host

    @property
    def leaf_group_ids(self):
        """Gets the leaf_group_ids of this EditVulnScanConfigRequest.  # noqa: E501


        :return: The leaf_group_ids of this EditVulnScanConfigRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._leaf_group_ids

    @leaf_group_ids.setter
    def leaf_group_ids(self, leaf_group_ids):
        """Sets the leaf_group_ids of this EditVulnScanConfigRequest.


        :param leaf_group_ids: The leaf_group_ids of this EditVulnScanConfigRequest.  # noqa: E501
        :type: list[str]
        """

        self._leaf_group_ids = leaf_group_ids

    @property
    def scan_type(self):
        """Gets the scan_type of this EditVulnScanConfigRequest.  # noqa: E501


        :return: The scan_type of this EditVulnScanConfigRequest.  # noqa: E501
        :rtype: ScanTypeForEditVulnScanConfigInput
        """
        return self._scan_type

    @scan_type.setter
    def scan_type(self, scan_type):
        """Sets the scan_type of this EditVulnScanConfigRequest.


        :param scan_type: The scan_type of this EditVulnScanConfigRequest.  # noqa: E501
        :type: ScanTypeForEditVulnScanConfigInput
        """

        self._scan_type = scan_type

    @property
    def top_group_id(self):
        """Gets the top_group_id of this EditVulnScanConfigRequest.  # noqa: E501


        :return: The top_group_id of this EditVulnScanConfigRequest.  # noqa: E501
        :rtype: str
        """
        return self._top_group_id

    @top_group_id.setter
    def top_group_id(self, top_group_id):
        """Sets the top_group_id of this EditVulnScanConfigRequest.


        :param top_group_id: The top_group_id of this EditVulnScanConfigRequest.  # noqa: E501
        :type: str
        """

        self._top_group_id = top_group_id

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
        if issubclass(EditVulnScanConfigRequest, dict):
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
        if not isinstance(other, EditVulnScanConfigRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EditVulnScanConfigRequest):
            return True

        return self.to_dict() != other.to_dict()
