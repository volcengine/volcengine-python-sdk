# coding: utf-8

"""
    rds_mysql_v2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DataForDescribeDeletedDBInstancesOutput(object):
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
        'backup_expiration_time': 'str',
        'create_time': 'str',
        'db_engine_version': 'str',
        'data_keep_days': 'int',
        'data_keep_policy': 'str',
        'deletion_time': 'str',
        'instance_id': 'str',
        'instance_name': 'str',
        'instance_status': 'str',
        'instance_type': 'str',
        'node_spec': 'str',
        'project_name': 'str',
        'storage_space': 'int',
        'storage_type': 'str'
    }

    attribute_map = {
        'backup_expiration_time': 'BackupExpirationTime',
        'create_time': 'CreateTime',
        'db_engine_version': 'DBEngineVersion',
        'data_keep_days': 'DataKeepDays',
        'data_keep_policy': 'DataKeepPolicy',
        'deletion_time': 'DeletionTime',
        'instance_id': 'InstanceId',
        'instance_name': 'InstanceName',
        'instance_status': 'InstanceStatus',
        'instance_type': 'InstanceType',
        'node_spec': 'NodeSpec',
        'project_name': 'ProjectName',
        'storage_space': 'StorageSpace',
        'storage_type': 'StorageType'
    }

    def __init__(self, backup_expiration_time=None, create_time=None, db_engine_version=None, data_keep_days=None, data_keep_policy=None, deletion_time=None, instance_id=None, instance_name=None, instance_status=None, instance_type=None, node_spec=None, project_name=None, storage_space=None, storage_type=None, _configuration=None):  # noqa: E501
        """DataForDescribeDeletedDBInstancesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._backup_expiration_time = None
        self._create_time = None
        self._db_engine_version = None
        self._data_keep_days = None
        self._data_keep_policy = None
        self._deletion_time = None
        self._instance_id = None
        self._instance_name = None
        self._instance_status = None
        self._instance_type = None
        self._node_spec = None
        self._project_name = None
        self._storage_space = None
        self._storage_type = None
        self.discriminator = None

        if backup_expiration_time is not None:
            self.backup_expiration_time = backup_expiration_time
        if create_time is not None:
            self.create_time = create_time
        if db_engine_version is not None:
            self.db_engine_version = db_engine_version
        if data_keep_days is not None:
            self.data_keep_days = data_keep_days
        if data_keep_policy is not None:
            self.data_keep_policy = data_keep_policy
        if deletion_time is not None:
            self.deletion_time = deletion_time
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if instance_status is not None:
            self.instance_status = instance_status
        if instance_type is not None:
            self.instance_type = instance_type
        if node_spec is not None:
            self.node_spec = node_spec
        if project_name is not None:
            self.project_name = project_name
        if storage_space is not None:
            self.storage_space = storage_space
        if storage_type is not None:
            self.storage_type = storage_type

    @property
    def backup_expiration_time(self):
        """Gets the backup_expiration_time of this DataForDescribeDeletedDBInstancesOutput.  # noqa: E501


        :return: The backup_expiration_time of this DataForDescribeDeletedDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._backup_expiration_time

    @backup_expiration_time.setter
    def backup_expiration_time(self, backup_expiration_time):
        """Sets the backup_expiration_time of this DataForDescribeDeletedDBInstancesOutput.


        :param backup_expiration_time: The backup_expiration_time of this DataForDescribeDeletedDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._backup_expiration_time = backup_expiration_time

    @property
    def create_time(self):
        """Gets the create_time of this DataForDescribeDeletedDBInstancesOutput.  # noqa: E501


        :return: The create_time of this DataForDescribeDeletedDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this DataForDescribeDeletedDBInstancesOutput.


        :param create_time: The create_time of this DataForDescribeDeletedDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._create_time = create_time

    @property
    def db_engine_version(self):
        """Gets the db_engine_version of this DataForDescribeDeletedDBInstancesOutput.  # noqa: E501


        :return: The db_engine_version of this DataForDescribeDeletedDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._db_engine_version

    @db_engine_version.setter
    def db_engine_version(self, db_engine_version):
        """Sets the db_engine_version of this DataForDescribeDeletedDBInstancesOutput.


        :param db_engine_version: The db_engine_version of this DataForDescribeDeletedDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._db_engine_version = db_engine_version

    @property
    def data_keep_days(self):
        """Gets the data_keep_days of this DataForDescribeDeletedDBInstancesOutput.  # noqa: E501


        :return: The data_keep_days of this DataForDescribeDeletedDBInstancesOutput.  # noqa: E501
        :rtype: int
        """
        return self._data_keep_days

    @data_keep_days.setter
    def data_keep_days(self, data_keep_days):
        """Sets the data_keep_days of this DataForDescribeDeletedDBInstancesOutput.


        :param data_keep_days: The data_keep_days of this DataForDescribeDeletedDBInstancesOutput.  # noqa: E501
        :type: int
        """

        self._data_keep_days = data_keep_days

    @property
    def data_keep_policy(self):
        """Gets the data_keep_policy of this DataForDescribeDeletedDBInstancesOutput.  # noqa: E501


        :return: The data_keep_policy of this DataForDescribeDeletedDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._data_keep_policy

    @data_keep_policy.setter
    def data_keep_policy(self, data_keep_policy):
        """Sets the data_keep_policy of this DataForDescribeDeletedDBInstancesOutput.


        :param data_keep_policy: The data_keep_policy of this DataForDescribeDeletedDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._data_keep_policy = data_keep_policy

    @property
    def deletion_time(self):
        """Gets the deletion_time of this DataForDescribeDeletedDBInstancesOutput.  # noqa: E501


        :return: The deletion_time of this DataForDescribeDeletedDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._deletion_time

    @deletion_time.setter
    def deletion_time(self, deletion_time):
        """Sets the deletion_time of this DataForDescribeDeletedDBInstancesOutput.


        :param deletion_time: The deletion_time of this DataForDescribeDeletedDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._deletion_time = deletion_time

    @property
    def instance_id(self):
        """Gets the instance_id of this DataForDescribeDeletedDBInstancesOutput.  # noqa: E501


        :return: The instance_id of this DataForDescribeDeletedDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this DataForDescribeDeletedDBInstancesOutput.


        :param instance_id: The instance_id of this DataForDescribeDeletedDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def instance_name(self):
        """Gets the instance_name of this DataForDescribeDeletedDBInstancesOutput.  # noqa: E501


        :return: The instance_name of this DataForDescribeDeletedDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this DataForDescribeDeletedDBInstancesOutput.


        :param instance_name: The instance_name of this DataForDescribeDeletedDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._instance_name = instance_name

    @property
    def instance_status(self):
        """Gets the instance_status of this DataForDescribeDeletedDBInstancesOutput.  # noqa: E501


        :return: The instance_status of this DataForDescribeDeletedDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_status

    @instance_status.setter
    def instance_status(self, instance_status):
        """Sets the instance_status of this DataForDescribeDeletedDBInstancesOutput.


        :param instance_status: The instance_status of this DataForDescribeDeletedDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._instance_status = instance_status

    @property
    def instance_type(self):
        """Gets the instance_type of this DataForDescribeDeletedDBInstancesOutput.  # noqa: E501


        :return: The instance_type of this DataForDescribeDeletedDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this DataForDescribeDeletedDBInstancesOutput.


        :param instance_type: The instance_type of this DataForDescribeDeletedDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._instance_type = instance_type

    @property
    def node_spec(self):
        """Gets the node_spec of this DataForDescribeDeletedDBInstancesOutput.  # noqa: E501


        :return: The node_spec of this DataForDescribeDeletedDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._node_spec

    @node_spec.setter
    def node_spec(self, node_spec):
        """Sets the node_spec of this DataForDescribeDeletedDBInstancesOutput.


        :param node_spec: The node_spec of this DataForDescribeDeletedDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._node_spec = node_spec

    @property
    def project_name(self):
        """Gets the project_name of this DataForDescribeDeletedDBInstancesOutput.  # noqa: E501


        :return: The project_name of this DataForDescribeDeletedDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this DataForDescribeDeletedDBInstancesOutput.


        :param project_name: The project_name of this DataForDescribeDeletedDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def storage_space(self):
        """Gets the storage_space of this DataForDescribeDeletedDBInstancesOutput.  # noqa: E501


        :return: The storage_space of this DataForDescribeDeletedDBInstancesOutput.  # noqa: E501
        :rtype: int
        """
        return self._storage_space

    @storage_space.setter
    def storage_space(self, storage_space):
        """Sets the storage_space of this DataForDescribeDeletedDBInstancesOutput.


        :param storage_space: The storage_space of this DataForDescribeDeletedDBInstancesOutput.  # noqa: E501
        :type: int
        """

        self._storage_space = storage_space

    @property
    def storage_type(self):
        """Gets the storage_type of this DataForDescribeDeletedDBInstancesOutput.  # noqa: E501


        :return: The storage_type of this DataForDescribeDeletedDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._storage_type

    @storage_type.setter
    def storage_type(self, storage_type):
        """Sets the storage_type of this DataForDescribeDeletedDBInstancesOutput.


        :param storage_type: The storage_type of this DataForDescribeDeletedDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._storage_type = storage_type

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
        if issubclass(DataForDescribeDeletedDBInstancesOutput, dict):
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
        if not isinstance(other, DataForDescribeDeletedDBInstancesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataForDescribeDeletedDBInstancesOutput):
            return True

        return self.to_dict() != other.to_dict()
