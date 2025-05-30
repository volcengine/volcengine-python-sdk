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


class DataForListMultiLevelInstitutionOutput(object):
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
        'account_id': 'str',
        'app_sec_open': 'bool',
        'cluster_sec_open': 'bool',
        'create_time': 'int',
        'expire_time': 'int',
        'host_total_count': 'int',
        'host_used_count': 'int',
        'id': 'str',
        'institution_id': 'str',
        'institution_name': 'str',
        'institution_status': 'str',
        'last_active_time': 'int',
        'remark': 'str',
        'report_switch_open': 'bool',
        'update_time': 'int'
    }

    attribute_map = {
        'account_id': 'AccountID',
        'app_sec_open': 'AppSecOpen',
        'cluster_sec_open': 'ClusterSecOpen',
        'create_time': 'CreateTime',
        'expire_time': 'ExpireTime',
        'host_total_count': 'HostTotalCount',
        'host_used_count': 'HostUsedCount',
        'id': 'ID',
        'institution_id': 'InstitutionID',
        'institution_name': 'InstitutionName',
        'institution_status': 'InstitutionStatus',
        'last_active_time': 'LastActiveTime',
        'remark': 'Remark',
        'report_switch_open': 'ReportSwitchOpen',
        'update_time': 'UpdateTime'
    }

    def __init__(self, account_id=None, app_sec_open=None, cluster_sec_open=None, create_time=None, expire_time=None, host_total_count=None, host_used_count=None, id=None, institution_id=None, institution_name=None, institution_status=None, last_active_time=None, remark=None, report_switch_open=None, update_time=None, _configuration=None):  # noqa: E501
        """DataForListMultiLevelInstitutionOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_id = None
        self._app_sec_open = None
        self._cluster_sec_open = None
        self._create_time = None
        self._expire_time = None
        self._host_total_count = None
        self._host_used_count = None
        self._id = None
        self._institution_id = None
        self._institution_name = None
        self._institution_status = None
        self._last_active_time = None
        self._remark = None
        self._report_switch_open = None
        self._update_time = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if app_sec_open is not None:
            self.app_sec_open = app_sec_open
        if cluster_sec_open is not None:
            self.cluster_sec_open = cluster_sec_open
        if create_time is not None:
            self.create_time = create_time
        if expire_time is not None:
            self.expire_time = expire_time
        if host_total_count is not None:
            self.host_total_count = host_total_count
        if host_used_count is not None:
            self.host_used_count = host_used_count
        if id is not None:
            self.id = id
        if institution_id is not None:
            self.institution_id = institution_id
        if institution_name is not None:
            self.institution_name = institution_name
        if institution_status is not None:
            self.institution_status = institution_status
        if last_active_time is not None:
            self.last_active_time = last_active_time
        if remark is not None:
            self.remark = remark
        if report_switch_open is not None:
            self.report_switch_open = report_switch_open
        if update_time is not None:
            self.update_time = update_time

    @property
    def account_id(self):
        """Gets the account_id of this DataForListMultiLevelInstitutionOutput.  # noqa: E501


        :return: The account_id of this DataForListMultiLevelInstitutionOutput.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this DataForListMultiLevelInstitutionOutput.


        :param account_id: The account_id of this DataForListMultiLevelInstitutionOutput.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def app_sec_open(self):
        """Gets the app_sec_open of this DataForListMultiLevelInstitutionOutput.  # noqa: E501


        :return: The app_sec_open of this DataForListMultiLevelInstitutionOutput.  # noqa: E501
        :rtype: bool
        """
        return self._app_sec_open

    @app_sec_open.setter
    def app_sec_open(self, app_sec_open):
        """Sets the app_sec_open of this DataForListMultiLevelInstitutionOutput.


        :param app_sec_open: The app_sec_open of this DataForListMultiLevelInstitutionOutput.  # noqa: E501
        :type: bool
        """

        self._app_sec_open = app_sec_open

    @property
    def cluster_sec_open(self):
        """Gets the cluster_sec_open of this DataForListMultiLevelInstitutionOutput.  # noqa: E501


        :return: The cluster_sec_open of this DataForListMultiLevelInstitutionOutput.  # noqa: E501
        :rtype: bool
        """
        return self._cluster_sec_open

    @cluster_sec_open.setter
    def cluster_sec_open(self, cluster_sec_open):
        """Sets the cluster_sec_open of this DataForListMultiLevelInstitutionOutput.


        :param cluster_sec_open: The cluster_sec_open of this DataForListMultiLevelInstitutionOutput.  # noqa: E501
        :type: bool
        """

        self._cluster_sec_open = cluster_sec_open

    @property
    def create_time(self):
        """Gets the create_time of this DataForListMultiLevelInstitutionOutput.  # noqa: E501


        :return: The create_time of this DataForListMultiLevelInstitutionOutput.  # noqa: E501
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this DataForListMultiLevelInstitutionOutput.


        :param create_time: The create_time of this DataForListMultiLevelInstitutionOutput.  # noqa: E501
        :type: int
        """

        self._create_time = create_time

    @property
    def expire_time(self):
        """Gets the expire_time of this DataForListMultiLevelInstitutionOutput.  # noqa: E501


        :return: The expire_time of this DataForListMultiLevelInstitutionOutput.  # noqa: E501
        :rtype: int
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this DataForListMultiLevelInstitutionOutput.


        :param expire_time: The expire_time of this DataForListMultiLevelInstitutionOutput.  # noqa: E501
        :type: int
        """

        self._expire_time = expire_time

    @property
    def host_total_count(self):
        """Gets the host_total_count of this DataForListMultiLevelInstitutionOutput.  # noqa: E501


        :return: The host_total_count of this DataForListMultiLevelInstitutionOutput.  # noqa: E501
        :rtype: int
        """
        return self._host_total_count

    @host_total_count.setter
    def host_total_count(self, host_total_count):
        """Sets the host_total_count of this DataForListMultiLevelInstitutionOutput.


        :param host_total_count: The host_total_count of this DataForListMultiLevelInstitutionOutput.  # noqa: E501
        :type: int
        """

        self._host_total_count = host_total_count

    @property
    def host_used_count(self):
        """Gets the host_used_count of this DataForListMultiLevelInstitutionOutput.  # noqa: E501


        :return: The host_used_count of this DataForListMultiLevelInstitutionOutput.  # noqa: E501
        :rtype: int
        """
        return self._host_used_count

    @host_used_count.setter
    def host_used_count(self, host_used_count):
        """Sets the host_used_count of this DataForListMultiLevelInstitutionOutput.


        :param host_used_count: The host_used_count of this DataForListMultiLevelInstitutionOutput.  # noqa: E501
        :type: int
        """

        self._host_used_count = host_used_count

    @property
    def id(self):
        """Gets the id of this DataForListMultiLevelInstitutionOutput.  # noqa: E501


        :return: The id of this DataForListMultiLevelInstitutionOutput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DataForListMultiLevelInstitutionOutput.


        :param id: The id of this DataForListMultiLevelInstitutionOutput.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def institution_id(self):
        """Gets the institution_id of this DataForListMultiLevelInstitutionOutput.  # noqa: E501


        :return: The institution_id of this DataForListMultiLevelInstitutionOutput.  # noqa: E501
        :rtype: str
        """
        return self._institution_id

    @institution_id.setter
    def institution_id(self, institution_id):
        """Sets the institution_id of this DataForListMultiLevelInstitutionOutput.


        :param institution_id: The institution_id of this DataForListMultiLevelInstitutionOutput.  # noqa: E501
        :type: str
        """

        self._institution_id = institution_id

    @property
    def institution_name(self):
        """Gets the institution_name of this DataForListMultiLevelInstitutionOutput.  # noqa: E501


        :return: The institution_name of this DataForListMultiLevelInstitutionOutput.  # noqa: E501
        :rtype: str
        """
        return self._institution_name

    @institution_name.setter
    def institution_name(self, institution_name):
        """Sets the institution_name of this DataForListMultiLevelInstitutionOutput.


        :param institution_name: The institution_name of this DataForListMultiLevelInstitutionOutput.  # noqa: E501
        :type: str
        """

        self._institution_name = institution_name

    @property
    def institution_status(self):
        """Gets the institution_status of this DataForListMultiLevelInstitutionOutput.  # noqa: E501


        :return: The institution_status of this DataForListMultiLevelInstitutionOutput.  # noqa: E501
        :rtype: str
        """
        return self._institution_status

    @institution_status.setter
    def institution_status(self, institution_status):
        """Sets the institution_status of this DataForListMultiLevelInstitutionOutput.


        :param institution_status: The institution_status of this DataForListMultiLevelInstitutionOutput.  # noqa: E501
        :type: str
        """

        self._institution_status = institution_status

    @property
    def last_active_time(self):
        """Gets the last_active_time of this DataForListMultiLevelInstitutionOutput.  # noqa: E501


        :return: The last_active_time of this DataForListMultiLevelInstitutionOutput.  # noqa: E501
        :rtype: int
        """
        return self._last_active_time

    @last_active_time.setter
    def last_active_time(self, last_active_time):
        """Sets the last_active_time of this DataForListMultiLevelInstitutionOutput.


        :param last_active_time: The last_active_time of this DataForListMultiLevelInstitutionOutput.  # noqa: E501
        :type: int
        """

        self._last_active_time = last_active_time

    @property
    def remark(self):
        """Gets the remark of this DataForListMultiLevelInstitutionOutput.  # noqa: E501


        :return: The remark of this DataForListMultiLevelInstitutionOutput.  # noqa: E501
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this DataForListMultiLevelInstitutionOutput.


        :param remark: The remark of this DataForListMultiLevelInstitutionOutput.  # noqa: E501
        :type: str
        """

        self._remark = remark

    @property
    def report_switch_open(self):
        """Gets the report_switch_open of this DataForListMultiLevelInstitutionOutput.  # noqa: E501


        :return: The report_switch_open of this DataForListMultiLevelInstitutionOutput.  # noqa: E501
        :rtype: bool
        """
        return self._report_switch_open

    @report_switch_open.setter
    def report_switch_open(self, report_switch_open):
        """Sets the report_switch_open of this DataForListMultiLevelInstitutionOutput.


        :param report_switch_open: The report_switch_open of this DataForListMultiLevelInstitutionOutput.  # noqa: E501
        :type: bool
        """

        self._report_switch_open = report_switch_open

    @property
    def update_time(self):
        """Gets the update_time of this DataForListMultiLevelInstitutionOutput.  # noqa: E501


        :return: The update_time of this DataForListMultiLevelInstitutionOutput.  # noqa: E501
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this DataForListMultiLevelInstitutionOutput.


        :param update_time: The update_time of this DataForListMultiLevelInstitutionOutput.  # noqa: E501
        :type: int
        """

        self._update_time = update_time

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
        if issubclass(DataForListMultiLevelInstitutionOutput, dict):
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
        if not isinstance(other, DataForListMultiLevelInstitutionOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataForListMultiLevelInstitutionOutput):
            return True

        return self.to_dict() != other.to_dict()
