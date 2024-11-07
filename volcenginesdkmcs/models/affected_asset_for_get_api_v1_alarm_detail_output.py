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


class AffectedAssetForGetApiV1AlarmDetailOutput(object):
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
        'resource_cloud_account_id': 'str',
        'resource_cloud_account_name': 'str',
        'resource_id': 'str',
        'resource_name': 'str',
        'resource_status': 'str',
        'resource_type': 'str',
        'resource_vendor': 'str'
    }

    attribute_map = {
        'resource_cloud_account_id': 'resource_cloud_account_id',
        'resource_cloud_account_name': 'resource_cloud_account_name',
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'resource_status': 'resource_status',
        'resource_type': 'resource_type',
        'resource_vendor': 'resource_vendor'
    }

    def __init__(self, resource_cloud_account_id=None, resource_cloud_account_name=None, resource_id=None, resource_name=None, resource_status=None, resource_type=None, resource_vendor=None, _configuration=None):  # noqa: E501
        """AffectedAssetForGetApiV1AlarmDetailOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._resource_cloud_account_id = None
        self._resource_cloud_account_name = None
        self._resource_id = None
        self._resource_name = None
        self._resource_status = None
        self._resource_type = None
        self._resource_vendor = None
        self.discriminator = None

        if resource_cloud_account_id is not None:
            self.resource_cloud_account_id = resource_cloud_account_id
        if resource_cloud_account_name is not None:
            self.resource_cloud_account_name = resource_cloud_account_name
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_name is not None:
            self.resource_name = resource_name
        if resource_status is not None:
            self.resource_status = resource_status
        if resource_type is not None:
            self.resource_type = resource_type
        if resource_vendor is not None:
            self.resource_vendor = resource_vendor

    @property
    def resource_cloud_account_id(self):
        """Gets the resource_cloud_account_id of this AffectedAssetForGetApiV1AlarmDetailOutput.  # noqa: E501


        :return: The resource_cloud_account_id of this AffectedAssetForGetApiV1AlarmDetailOutput.  # noqa: E501
        :rtype: str
        """
        return self._resource_cloud_account_id

    @resource_cloud_account_id.setter
    def resource_cloud_account_id(self, resource_cloud_account_id):
        """Sets the resource_cloud_account_id of this AffectedAssetForGetApiV1AlarmDetailOutput.


        :param resource_cloud_account_id: The resource_cloud_account_id of this AffectedAssetForGetApiV1AlarmDetailOutput.  # noqa: E501
        :type: str
        """

        self._resource_cloud_account_id = resource_cloud_account_id

    @property
    def resource_cloud_account_name(self):
        """Gets the resource_cloud_account_name of this AffectedAssetForGetApiV1AlarmDetailOutput.  # noqa: E501


        :return: The resource_cloud_account_name of this AffectedAssetForGetApiV1AlarmDetailOutput.  # noqa: E501
        :rtype: str
        """
        return self._resource_cloud_account_name

    @resource_cloud_account_name.setter
    def resource_cloud_account_name(self, resource_cloud_account_name):
        """Sets the resource_cloud_account_name of this AffectedAssetForGetApiV1AlarmDetailOutput.


        :param resource_cloud_account_name: The resource_cloud_account_name of this AffectedAssetForGetApiV1AlarmDetailOutput.  # noqa: E501
        :type: str
        """

        self._resource_cloud_account_name = resource_cloud_account_name

    @property
    def resource_id(self):
        """Gets the resource_id of this AffectedAssetForGetApiV1AlarmDetailOutput.  # noqa: E501


        :return: The resource_id of this AffectedAssetForGetApiV1AlarmDetailOutput.  # noqa: E501
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this AffectedAssetForGetApiV1AlarmDetailOutput.


        :param resource_id: The resource_id of this AffectedAssetForGetApiV1AlarmDetailOutput.  # noqa: E501
        :type: str
        """

        self._resource_id = resource_id

    @property
    def resource_name(self):
        """Gets the resource_name of this AffectedAssetForGetApiV1AlarmDetailOutput.  # noqa: E501


        :return: The resource_name of this AffectedAssetForGetApiV1AlarmDetailOutput.  # noqa: E501
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this AffectedAssetForGetApiV1AlarmDetailOutput.


        :param resource_name: The resource_name of this AffectedAssetForGetApiV1AlarmDetailOutput.  # noqa: E501
        :type: str
        """

        self._resource_name = resource_name

    @property
    def resource_status(self):
        """Gets the resource_status of this AffectedAssetForGetApiV1AlarmDetailOutput.  # noqa: E501


        :return: The resource_status of this AffectedAssetForGetApiV1AlarmDetailOutput.  # noqa: E501
        :rtype: str
        """
        return self._resource_status

    @resource_status.setter
    def resource_status(self, resource_status):
        """Sets the resource_status of this AffectedAssetForGetApiV1AlarmDetailOutput.


        :param resource_status: The resource_status of this AffectedAssetForGetApiV1AlarmDetailOutput.  # noqa: E501
        :type: str
        """

        self._resource_status = resource_status

    @property
    def resource_type(self):
        """Gets the resource_type of this AffectedAssetForGetApiV1AlarmDetailOutput.  # noqa: E501


        :return: The resource_type of this AffectedAssetForGetApiV1AlarmDetailOutput.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this AffectedAssetForGetApiV1AlarmDetailOutput.


        :param resource_type: The resource_type of this AffectedAssetForGetApiV1AlarmDetailOutput.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def resource_vendor(self):
        """Gets the resource_vendor of this AffectedAssetForGetApiV1AlarmDetailOutput.  # noqa: E501


        :return: The resource_vendor of this AffectedAssetForGetApiV1AlarmDetailOutput.  # noqa: E501
        :rtype: str
        """
        return self._resource_vendor

    @resource_vendor.setter
    def resource_vendor(self, resource_vendor):
        """Sets the resource_vendor of this AffectedAssetForGetApiV1AlarmDetailOutput.


        :param resource_vendor: The resource_vendor of this AffectedAssetForGetApiV1AlarmDetailOutput.  # noqa: E501
        :type: str
        """

        self._resource_vendor = resource_vendor

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
        if issubclass(AffectedAssetForGetApiV1AlarmDetailOutput, dict):
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
        if not isinstance(other, AffectedAssetForGetApiV1AlarmDetailOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AffectedAssetForGetApiV1AlarmDetailOutput):
            return True

        return self.to_dict() != other.to_dict()
