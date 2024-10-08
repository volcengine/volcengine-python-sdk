# coding: utf-8

"""
    mcdn

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class CloudAccountForListCloudAccountsOutput(object):
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
        'cloud_account_vendor_permission': 'str',
        'content_settings': 'ContentSettingsForListCloudAccountsOutput',
        'created_at': 'int',
        'domain_settings': 'DomainSettingsForListCloudAccountsOutput',
        'extra': 'ExtraForListCloudAccountsOutput',
        'id': 'str',
        'last_sync_at': 'int',
        'name': 'str',
        'permission_state': 'PermissionStateForListCloudAccountsOutput',
        'read_only': 'bool',
        'self_host_proxy_endpoint': 'str',
        'stat_settings': 'StatSettingsForListCloudAccountsOutput',
        'sub_products': 'list[str]',
        'sync_status': 'str',
        'sync_status_state': 'SyncStatusStateForListCloudAccountsOutput',
        'top_account_id': 'str',
        'updated_at': 'int',
        'vendor': 'str'
    }

    attribute_map = {
        'cloud_account_vendor_permission': 'CloudAccountVendorPermission',
        'content_settings': 'ContentSettings',
        'created_at': 'CreatedAt',
        'domain_settings': 'DomainSettings',
        'extra': 'Extra',
        'id': 'Id',
        'last_sync_at': 'LastSyncAt',
        'name': 'Name',
        'permission_state': 'PermissionState',
        'read_only': 'ReadOnly',
        'self_host_proxy_endpoint': 'SelfHostProxyEndpoint',
        'stat_settings': 'StatSettings',
        'sub_products': 'SubProducts',
        'sync_status': 'SyncStatus',
        'sync_status_state': 'SyncStatusState',
        'top_account_id': 'TopAccountId',
        'updated_at': 'UpdatedAt',
        'vendor': 'Vendor'
    }

    def __init__(self, cloud_account_vendor_permission=None, content_settings=None, created_at=None, domain_settings=None, extra=None, id=None, last_sync_at=None, name=None, permission_state=None, read_only=None, self_host_proxy_endpoint=None, stat_settings=None, sub_products=None, sync_status=None, sync_status_state=None, top_account_id=None, updated_at=None, vendor=None, _configuration=None):  # noqa: E501
        """CloudAccountForListCloudAccountsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cloud_account_vendor_permission = None
        self._content_settings = None
        self._created_at = None
        self._domain_settings = None
        self._extra = None
        self._id = None
        self._last_sync_at = None
        self._name = None
        self._permission_state = None
        self._read_only = None
        self._self_host_proxy_endpoint = None
        self._stat_settings = None
        self._sub_products = None
        self._sync_status = None
        self._sync_status_state = None
        self._top_account_id = None
        self._updated_at = None
        self._vendor = None
        self.discriminator = None

        if cloud_account_vendor_permission is not None:
            self.cloud_account_vendor_permission = cloud_account_vendor_permission
        if content_settings is not None:
            self.content_settings = content_settings
        if created_at is not None:
            self.created_at = created_at
        if domain_settings is not None:
            self.domain_settings = domain_settings
        if extra is not None:
            self.extra = extra
        if id is not None:
            self.id = id
        if last_sync_at is not None:
            self.last_sync_at = last_sync_at
        if name is not None:
            self.name = name
        if permission_state is not None:
            self.permission_state = permission_state
        if read_only is not None:
            self.read_only = read_only
        if self_host_proxy_endpoint is not None:
            self.self_host_proxy_endpoint = self_host_proxy_endpoint
        if stat_settings is not None:
            self.stat_settings = stat_settings
        if sub_products is not None:
            self.sub_products = sub_products
        if sync_status is not None:
            self.sync_status = sync_status
        if sync_status_state is not None:
            self.sync_status_state = sync_status_state
        if top_account_id is not None:
            self.top_account_id = top_account_id
        if updated_at is not None:
            self.updated_at = updated_at
        if vendor is not None:
            self.vendor = vendor

    @property
    def cloud_account_vendor_permission(self):
        """Gets the cloud_account_vendor_permission of this CloudAccountForListCloudAccountsOutput.  # noqa: E501


        :return: The cloud_account_vendor_permission of this CloudAccountForListCloudAccountsOutput.  # noqa: E501
        :rtype: str
        """
        return self._cloud_account_vendor_permission

    @cloud_account_vendor_permission.setter
    def cloud_account_vendor_permission(self, cloud_account_vendor_permission):
        """Sets the cloud_account_vendor_permission of this CloudAccountForListCloudAccountsOutput.


        :param cloud_account_vendor_permission: The cloud_account_vendor_permission of this CloudAccountForListCloudAccountsOutput.  # noqa: E501
        :type: str
        """

        self._cloud_account_vendor_permission = cloud_account_vendor_permission

    @property
    def content_settings(self):
        """Gets the content_settings of this CloudAccountForListCloudAccountsOutput.  # noqa: E501


        :return: The content_settings of this CloudAccountForListCloudAccountsOutput.  # noqa: E501
        :rtype: ContentSettingsForListCloudAccountsOutput
        """
        return self._content_settings

    @content_settings.setter
    def content_settings(self, content_settings):
        """Sets the content_settings of this CloudAccountForListCloudAccountsOutput.


        :param content_settings: The content_settings of this CloudAccountForListCloudAccountsOutput.  # noqa: E501
        :type: ContentSettingsForListCloudAccountsOutput
        """

        self._content_settings = content_settings

    @property
    def created_at(self):
        """Gets the created_at of this CloudAccountForListCloudAccountsOutput.  # noqa: E501


        :return: The created_at of this CloudAccountForListCloudAccountsOutput.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this CloudAccountForListCloudAccountsOutput.


        :param created_at: The created_at of this CloudAccountForListCloudAccountsOutput.  # noqa: E501
        :type: int
        """

        self._created_at = created_at

    @property
    def domain_settings(self):
        """Gets the domain_settings of this CloudAccountForListCloudAccountsOutput.  # noqa: E501


        :return: The domain_settings of this CloudAccountForListCloudAccountsOutput.  # noqa: E501
        :rtype: DomainSettingsForListCloudAccountsOutput
        """
        return self._domain_settings

    @domain_settings.setter
    def domain_settings(self, domain_settings):
        """Sets the domain_settings of this CloudAccountForListCloudAccountsOutput.


        :param domain_settings: The domain_settings of this CloudAccountForListCloudAccountsOutput.  # noqa: E501
        :type: DomainSettingsForListCloudAccountsOutput
        """

        self._domain_settings = domain_settings

    @property
    def extra(self):
        """Gets the extra of this CloudAccountForListCloudAccountsOutput.  # noqa: E501


        :return: The extra of this CloudAccountForListCloudAccountsOutput.  # noqa: E501
        :rtype: ExtraForListCloudAccountsOutput
        """
        return self._extra

    @extra.setter
    def extra(self, extra):
        """Sets the extra of this CloudAccountForListCloudAccountsOutput.


        :param extra: The extra of this CloudAccountForListCloudAccountsOutput.  # noqa: E501
        :type: ExtraForListCloudAccountsOutput
        """

        self._extra = extra

    @property
    def id(self):
        """Gets the id of this CloudAccountForListCloudAccountsOutput.  # noqa: E501


        :return: The id of this CloudAccountForListCloudAccountsOutput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CloudAccountForListCloudAccountsOutput.


        :param id: The id of this CloudAccountForListCloudAccountsOutput.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def last_sync_at(self):
        """Gets the last_sync_at of this CloudAccountForListCloudAccountsOutput.  # noqa: E501


        :return: The last_sync_at of this CloudAccountForListCloudAccountsOutput.  # noqa: E501
        :rtype: int
        """
        return self._last_sync_at

    @last_sync_at.setter
    def last_sync_at(self, last_sync_at):
        """Sets the last_sync_at of this CloudAccountForListCloudAccountsOutput.


        :param last_sync_at: The last_sync_at of this CloudAccountForListCloudAccountsOutput.  # noqa: E501
        :type: int
        """

        self._last_sync_at = last_sync_at

    @property
    def name(self):
        """Gets the name of this CloudAccountForListCloudAccountsOutput.  # noqa: E501


        :return: The name of this CloudAccountForListCloudAccountsOutput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CloudAccountForListCloudAccountsOutput.


        :param name: The name of this CloudAccountForListCloudAccountsOutput.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def permission_state(self):
        """Gets the permission_state of this CloudAccountForListCloudAccountsOutput.  # noqa: E501


        :return: The permission_state of this CloudAccountForListCloudAccountsOutput.  # noqa: E501
        :rtype: PermissionStateForListCloudAccountsOutput
        """
        return self._permission_state

    @permission_state.setter
    def permission_state(self, permission_state):
        """Sets the permission_state of this CloudAccountForListCloudAccountsOutput.


        :param permission_state: The permission_state of this CloudAccountForListCloudAccountsOutput.  # noqa: E501
        :type: PermissionStateForListCloudAccountsOutput
        """

        self._permission_state = permission_state

    @property
    def read_only(self):
        """Gets the read_only of this CloudAccountForListCloudAccountsOutput.  # noqa: E501


        :return: The read_only of this CloudAccountForListCloudAccountsOutput.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this CloudAccountForListCloudAccountsOutput.


        :param read_only: The read_only of this CloudAccountForListCloudAccountsOutput.  # noqa: E501
        :type: bool
        """

        self._read_only = read_only

    @property
    def self_host_proxy_endpoint(self):
        """Gets the self_host_proxy_endpoint of this CloudAccountForListCloudAccountsOutput.  # noqa: E501


        :return: The self_host_proxy_endpoint of this CloudAccountForListCloudAccountsOutput.  # noqa: E501
        :rtype: str
        """
        return self._self_host_proxy_endpoint

    @self_host_proxy_endpoint.setter
    def self_host_proxy_endpoint(self, self_host_proxy_endpoint):
        """Sets the self_host_proxy_endpoint of this CloudAccountForListCloudAccountsOutput.


        :param self_host_proxy_endpoint: The self_host_proxy_endpoint of this CloudAccountForListCloudAccountsOutput.  # noqa: E501
        :type: str
        """

        self._self_host_proxy_endpoint = self_host_proxy_endpoint

    @property
    def stat_settings(self):
        """Gets the stat_settings of this CloudAccountForListCloudAccountsOutput.  # noqa: E501


        :return: The stat_settings of this CloudAccountForListCloudAccountsOutput.  # noqa: E501
        :rtype: StatSettingsForListCloudAccountsOutput
        """
        return self._stat_settings

    @stat_settings.setter
    def stat_settings(self, stat_settings):
        """Sets the stat_settings of this CloudAccountForListCloudAccountsOutput.


        :param stat_settings: The stat_settings of this CloudAccountForListCloudAccountsOutput.  # noqa: E501
        :type: StatSettingsForListCloudAccountsOutput
        """

        self._stat_settings = stat_settings

    @property
    def sub_products(self):
        """Gets the sub_products of this CloudAccountForListCloudAccountsOutput.  # noqa: E501


        :return: The sub_products of this CloudAccountForListCloudAccountsOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._sub_products

    @sub_products.setter
    def sub_products(self, sub_products):
        """Sets the sub_products of this CloudAccountForListCloudAccountsOutput.


        :param sub_products: The sub_products of this CloudAccountForListCloudAccountsOutput.  # noqa: E501
        :type: list[str]
        """

        self._sub_products = sub_products

    @property
    def sync_status(self):
        """Gets the sync_status of this CloudAccountForListCloudAccountsOutput.  # noqa: E501


        :return: The sync_status of this CloudAccountForListCloudAccountsOutput.  # noqa: E501
        :rtype: str
        """
        return self._sync_status

    @sync_status.setter
    def sync_status(self, sync_status):
        """Sets the sync_status of this CloudAccountForListCloudAccountsOutput.


        :param sync_status: The sync_status of this CloudAccountForListCloudAccountsOutput.  # noqa: E501
        :type: str
        """

        self._sync_status = sync_status

    @property
    def sync_status_state(self):
        """Gets the sync_status_state of this CloudAccountForListCloudAccountsOutput.  # noqa: E501


        :return: The sync_status_state of this CloudAccountForListCloudAccountsOutput.  # noqa: E501
        :rtype: SyncStatusStateForListCloudAccountsOutput
        """
        return self._sync_status_state

    @sync_status_state.setter
    def sync_status_state(self, sync_status_state):
        """Sets the sync_status_state of this CloudAccountForListCloudAccountsOutput.


        :param sync_status_state: The sync_status_state of this CloudAccountForListCloudAccountsOutput.  # noqa: E501
        :type: SyncStatusStateForListCloudAccountsOutput
        """

        self._sync_status_state = sync_status_state

    @property
    def top_account_id(self):
        """Gets the top_account_id of this CloudAccountForListCloudAccountsOutput.  # noqa: E501


        :return: The top_account_id of this CloudAccountForListCloudAccountsOutput.  # noqa: E501
        :rtype: str
        """
        return self._top_account_id

    @top_account_id.setter
    def top_account_id(self, top_account_id):
        """Sets the top_account_id of this CloudAccountForListCloudAccountsOutput.


        :param top_account_id: The top_account_id of this CloudAccountForListCloudAccountsOutput.  # noqa: E501
        :type: str
        """

        self._top_account_id = top_account_id

    @property
    def updated_at(self):
        """Gets the updated_at of this CloudAccountForListCloudAccountsOutput.  # noqa: E501


        :return: The updated_at of this CloudAccountForListCloudAccountsOutput.  # noqa: E501
        :rtype: int
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this CloudAccountForListCloudAccountsOutput.


        :param updated_at: The updated_at of this CloudAccountForListCloudAccountsOutput.  # noqa: E501
        :type: int
        """

        self._updated_at = updated_at

    @property
    def vendor(self):
        """Gets the vendor of this CloudAccountForListCloudAccountsOutput.  # noqa: E501


        :return: The vendor of this CloudAccountForListCloudAccountsOutput.  # noqa: E501
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this CloudAccountForListCloudAccountsOutput.


        :param vendor: The vendor of this CloudAccountForListCloudAccountsOutput.  # noqa: E501
        :type: str
        """

        self._vendor = vendor

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
        if issubclass(CloudAccountForListCloudAccountsOutput, dict):
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
        if not isinstance(other, CloudAccountForListCloudAccountsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CloudAccountForListCloudAccountsOutput):
            return True

        return self.to_dict() != other.to_dict()
