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


class DownloadBaselineCheckHostsRequest(object):
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
        'asset_id_list': 'list[str]',
        'asset_type': 'str',
        'baseline_id': 'int',
        'check_id': 'int',
        'conditions': 'ConditionsForDownloadBaselineCheckHostsInput',
        'id_list': 'list[str]'
    }

    attribute_map = {
        'asset_id_list': 'AssetIDList',
        'asset_type': 'AssetType',
        'baseline_id': 'BaselineID',
        'check_id': 'CheckID',
        'conditions': 'Conditions',
        'id_list': 'IDList'
    }

    def __init__(self, asset_id_list=None, asset_type=None, baseline_id=None, check_id=None, conditions=None, id_list=None, _configuration=None):  # noqa: E501
        """DownloadBaselineCheckHostsRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._asset_id_list = None
        self._asset_type = None
        self._baseline_id = None
        self._check_id = None
        self._conditions = None
        self._id_list = None
        self.discriminator = None

        if asset_id_list is not None:
            self.asset_id_list = asset_id_list
        if asset_type is not None:
            self.asset_type = asset_type
        if baseline_id is not None:
            self.baseline_id = baseline_id
        if check_id is not None:
            self.check_id = check_id
        if conditions is not None:
            self.conditions = conditions
        if id_list is not None:
            self.id_list = id_list

    @property
    def asset_id_list(self):
        """Gets the asset_id_list of this DownloadBaselineCheckHostsRequest.  # noqa: E501


        :return: The asset_id_list of this DownloadBaselineCheckHostsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._asset_id_list

    @asset_id_list.setter
    def asset_id_list(self, asset_id_list):
        """Sets the asset_id_list of this DownloadBaselineCheckHostsRequest.


        :param asset_id_list: The asset_id_list of this DownloadBaselineCheckHostsRequest.  # noqa: E501
        :type: list[str]
        """

        self._asset_id_list = asset_id_list

    @property
    def asset_type(self):
        """Gets the asset_type of this DownloadBaselineCheckHostsRequest.  # noqa: E501


        :return: The asset_type of this DownloadBaselineCheckHostsRequest.  # noqa: E501
        :rtype: str
        """
        return self._asset_type

    @asset_type.setter
    def asset_type(self, asset_type):
        """Sets the asset_type of this DownloadBaselineCheckHostsRequest.


        :param asset_type: The asset_type of this DownloadBaselineCheckHostsRequest.  # noqa: E501
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
    def baseline_id(self):
        """Gets the baseline_id of this DownloadBaselineCheckHostsRequest.  # noqa: E501


        :return: The baseline_id of this DownloadBaselineCheckHostsRequest.  # noqa: E501
        :rtype: int
        """
        return self._baseline_id

    @baseline_id.setter
    def baseline_id(self, baseline_id):
        """Sets the baseline_id of this DownloadBaselineCheckHostsRequest.


        :param baseline_id: The baseline_id of this DownloadBaselineCheckHostsRequest.  # noqa: E501
        :type: int
        """

        self._baseline_id = baseline_id

    @property
    def check_id(self):
        """Gets the check_id of this DownloadBaselineCheckHostsRequest.  # noqa: E501


        :return: The check_id of this DownloadBaselineCheckHostsRequest.  # noqa: E501
        :rtype: int
        """
        return self._check_id

    @check_id.setter
    def check_id(self, check_id):
        """Sets the check_id of this DownloadBaselineCheckHostsRequest.


        :param check_id: The check_id of this DownloadBaselineCheckHostsRequest.  # noqa: E501
        :type: int
        """

        self._check_id = check_id

    @property
    def conditions(self):
        """Gets the conditions of this DownloadBaselineCheckHostsRequest.  # noqa: E501


        :return: The conditions of this DownloadBaselineCheckHostsRequest.  # noqa: E501
        :rtype: ConditionsForDownloadBaselineCheckHostsInput
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this DownloadBaselineCheckHostsRequest.


        :param conditions: The conditions of this DownloadBaselineCheckHostsRequest.  # noqa: E501
        :type: ConditionsForDownloadBaselineCheckHostsInput
        """

        self._conditions = conditions

    @property
    def id_list(self):
        """Gets the id_list of this DownloadBaselineCheckHostsRequest.  # noqa: E501


        :return: The id_list of this DownloadBaselineCheckHostsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._id_list

    @id_list.setter
    def id_list(self, id_list):
        """Sets the id_list of this DownloadBaselineCheckHostsRequest.


        :param id_list: The id_list of this DownloadBaselineCheckHostsRequest.  # noqa: E501
        :type: list[str]
        """

        self._id_list = id_list

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
        if issubclass(DownloadBaselineCheckHostsRequest, dict):
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
        if not isinstance(other, DownloadBaselineCheckHostsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DownloadBaselineCheckHostsRequest):
            return True

        return self.to_dict() != other.to_dict()
