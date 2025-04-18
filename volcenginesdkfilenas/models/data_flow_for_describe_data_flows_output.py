# coding: utf-8

"""
    filenas

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DataFlowForDescribeDataFlowsOutput(object):
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
        'bucket_name': 'str',
        'bucket_prefix': 'str',
        'create_time': 'str',
        'enable_bucket_versioning': 'bool',
        'evict_policy': 'EvictPolicyForDescribeDataFlowsOutput',
        'export_policy': 'ExportPolicyForDescribeDataFlowsOutput',
        'file_system_id': 'str',
        'file_system_path': 'str',
        'id': 'str',
        'import_policy': 'ImportPolicyForDescribeDataFlowsOutput',
        'name': 'str',
        'queue_exec': 'int',
        'queue_failed': 'int',
        'queue_len': 'int',
        'releasing': 'bool',
        'running_task_number': 'int',
        'same_name_file_policy': 'str',
        'status': 'str',
        'sync_status': 'str',
        'tls_info': 'TlsInfoForDescribeDataFlowsOutput',
        'update_time': 'str'
    }

    attribute_map = {
        'bucket_name': 'BucketName',
        'bucket_prefix': 'BucketPrefix',
        'create_time': 'CreateTime',
        'enable_bucket_versioning': 'EnableBucketVersioning',
        'evict_policy': 'EvictPolicy',
        'export_policy': 'ExportPolicy',
        'file_system_id': 'FileSystemId',
        'file_system_path': 'FileSystemPath',
        'id': 'Id',
        'import_policy': 'ImportPolicy',
        'name': 'Name',
        'queue_exec': 'QueueExec',
        'queue_failed': 'QueueFailed',
        'queue_len': 'QueueLen',
        'releasing': 'Releasing',
        'running_task_number': 'RunningTaskNumber',
        'same_name_file_policy': 'SameNameFilePolicy',
        'status': 'Status',
        'sync_status': 'SyncStatus',
        'tls_info': 'TlsInfo',
        'update_time': 'UpdateTime'
    }

    def __init__(self, bucket_name=None, bucket_prefix=None, create_time=None, enable_bucket_versioning=None, evict_policy=None, export_policy=None, file_system_id=None, file_system_path=None, id=None, import_policy=None, name=None, queue_exec=None, queue_failed=None, queue_len=None, releasing=None, running_task_number=None, same_name_file_policy=None, status=None, sync_status=None, tls_info=None, update_time=None, _configuration=None):  # noqa: E501
        """DataFlowForDescribeDataFlowsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bucket_name = None
        self._bucket_prefix = None
        self._create_time = None
        self._enable_bucket_versioning = None
        self._evict_policy = None
        self._export_policy = None
        self._file_system_id = None
        self._file_system_path = None
        self._id = None
        self._import_policy = None
        self._name = None
        self._queue_exec = None
        self._queue_failed = None
        self._queue_len = None
        self._releasing = None
        self._running_task_number = None
        self._same_name_file_policy = None
        self._status = None
        self._sync_status = None
        self._tls_info = None
        self._update_time = None
        self.discriminator = None

        if bucket_name is not None:
            self.bucket_name = bucket_name
        if bucket_prefix is not None:
            self.bucket_prefix = bucket_prefix
        if create_time is not None:
            self.create_time = create_time
        if enable_bucket_versioning is not None:
            self.enable_bucket_versioning = enable_bucket_versioning
        if evict_policy is not None:
            self.evict_policy = evict_policy
        if export_policy is not None:
            self.export_policy = export_policy
        if file_system_id is not None:
            self.file_system_id = file_system_id
        if file_system_path is not None:
            self.file_system_path = file_system_path
        if id is not None:
            self.id = id
        if import_policy is not None:
            self.import_policy = import_policy
        if name is not None:
            self.name = name
        if queue_exec is not None:
            self.queue_exec = queue_exec
        if queue_failed is not None:
            self.queue_failed = queue_failed
        if queue_len is not None:
            self.queue_len = queue_len
        if releasing is not None:
            self.releasing = releasing
        if running_task_number is not None:
            self.running_task_number = running_task_number
        if same_name_file_policy is not None:
            self.same_name_file_policy = same_name_file_policy
        if status is not None:
            self.status = status
        if sync_status is not None:
            self.sync_status = sync_status
        if tls_info is not None:
            self.tls_info = tls_info
        if update_time is not None:
            self.update_time = update_time

    @property
    def bucket_name(self):
        """Gets the bucket_name of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501


        :return: The bucket_name of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """Sets the bucket_name of this DataFlowForDescribeDataFlowsOutput.


        :param bucket_name: The bucket_name of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501
        :type: str
        """

        self._bucket_name = bucket_name

    @property
    def bucket_prefix(self):
        """Gets the bucket_prefix of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501


        :return: The bucket_prefix of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501
        :rtype: str
        """
        return self._bucket_prefix

    @bucket_prefix.setter
    def bucket_prefix(self, bucket_prefix):
        """Sets the bucket_prefix of this DataFlowForDescribeDataFlowsOutput.


        :param bucket_prefix: The bucket_prefix of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501
        :type: str
        """

        self._bucket_prefix = bucket_prefix

    @property
    def create_time(self):
        """Gets the create_time of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501


        :return: The create_time of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this DataFlowForDescribeDataFlowsOutput.


        :param create_time: The create_time of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501
        :type: str
        """

        self._create_time = create_time

    @property
    def enable_bucket_versioning(self):
        """Gets the enable_bucket_versioning of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501


        :return: The enable_bucket_versioning of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501
        :rtype: bool
        """
        return self._enable_bucket_versioning

    @enable_bucket_versioning.setter
    def enable_bucket_versioning(self, enable_bucket_versioning):
        """Sets the enable_bucket_versioning of this DataFlowForDescribeDataFlowsOutput.


        :param enable_bucket_versioning: The enable_bucket_versioning of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501
        :type: bool
        """

        self._enable_bucket_versioning = enable_bucket_versioning

    @property
    def evict_policy(self):
        """Gets the evict_policy of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501


        :return: The evict_policy of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501
        :rtype: EvictPolicyForDescribeDataFlowsOutput
        """
        return self._evict_policy

    @evict_policy.setter
    def evict_policy(self, evict_policy):
        """Sets the evict_policy of this DataFlowForDescribeDataFlowsOutput.


        :param evict_policy: The evict_policy of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501
        :type: EvictPolicyForDescribeDataFlowsOutput
        """

        self._evict_policy = evict_policy

    @property
    def export_policy(self):
        """Gets the export_policy of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501


        :return: The export_policy of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501
        :rtype: ExportPolicyForDescribeDataFlowsOutput
        """
        return self._export_policy

    @export_policy.setter
    def export_policy(self, export_policy):
        """Sets the export_policy of this DataFlowForDescribeDataFlowsOutput.


        :param export_policy: The export_policy of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501
        :type: ExportPolicyForDescribeDataFlowsOutput
        """

        self._export_policy = export_policy

    @property
    def file_system_id(self):
        """Gets the file_system_id of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501


        :return: The file_system_id of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501
        :rtype: str
        """
        return self._file_system_id

    @file_system_id.setter
    def file_system_id(self, file_system_id):
        """Sets the file_system_id of this DataFlowForDescribeDataFlowsOutput.


        :param file_system_id: The file_system_id of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501
        :type: str
        """

        self._file_system_id = file_system_id

    @property
    def file_system_path(self):
        """Gets the file_system_path of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501


        :return: The file_system_path of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501
        :rtype: str
        """
        return self._file_system_path

    @file_system_path.setter
    def file_system_path(self, file_system_path):
        """Sets the file_system_path of this DataFlowForDescribeDataFlowsOutput.


        :param file_system_path: The file_system_path of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501
        :type: str
        """

        self._file_system_path = file_system_path

    @property
    def id(self):
        """Gets the id of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501


        :return: The id of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DataFlowForDescribeDataFlowsOutput.


        :param id: The id of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def import_policy(self):
        """Gets the import_policy of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501


        :return: The import_policy of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501
        :rtype: ImportPolicyForDescribeDataFlowsOutput
        """
        return self._import_policy

    @import_policy.setter
    def import_policy(self, import_policy):
        """Sets the import_policy of this DataFlowForDescribeDataFlowsOutput.


        :param import_policy: The import_policy of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501
        :type: ImportPolicyForDescribeDataFlowsOutput
        """

        self._import_policy = import_policy

    @property
    def name(self):
        """Gets the name of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501


        :return: The name of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DataFlowForDescribeDataFlowsOutput.


        :param name: The name of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def queue_exec(self):
        """Gets the queue_exec of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501


        :return: The queue_exec of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501
        :rtype: int
        """
        return self._queue_exec

    @queue_exec.setter
    def queue_exec(self, queue_exec):
        """Sets the queue_exec of this DataFlowForDescribeDataFlowsOutput.


        :param queue_exec: The queue_exec of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501
        :type: int
        """

        self._queue_exec = queue_exec

    @property
    def queue_failed(self):
        """Gets the queue_failed of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501


        :return: The queue_failed of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501
        :rtype: int
        """
        return self._queue_failed

    @queue_failed.setter
    def queue_failed(self, queue_failed):
        """Sets the queue_failed of this DataFlowForDescribeDataFlowsOutput.


        :param queue_failed: The queue_failed of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501
        :type: int
        """

        self._queue_failed = queue_failed

    @property
    def queue_len(self):
        """Gets the queue_len of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501


        :return: The queue_len of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501
        :rtype: int
        """
        return self._queue_len

    @queue_len.setter
    def queue_len(self, queue_len):
        """Sets the queue_len of this DataFlowForDescribeDataFlowsOutput.


        :param queue_len: The queue_len of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501
        :type: int
        """

        self._queue_len = queue_len

    @property
    def releasing(self):
        """Gets the releasing of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501


        :return: The releasing of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501
        :rtype: bool
        """
        return self._releasing

    @releasing.setter
    def releasing(self, releasing):
        """Sets the releasing of this DataFlowForDescribeDataFlowsOutput.


        :param releasing: The releasing of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501
        :type: bool
        """

        self._releasing = releasing

    @property
    def running_task_number(self):
        """Gets the running_task_number of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501


        :return: The running_task_number of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501
        :rtype: int
        """
        return self._running_task_number

    @running_task_number.setter
    def running_task_number(self, running_task_number):
        """Sets the running_task_number of this DataFlowForDescribeDataFlowsOutput.


        :param running_task_number: The running_task_number of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501
        :type: int
        """

        self._running_task_number = running_task_number

    @property
    def same_name_file_policy(self):
        """Gets the same_name_file_policy of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501


        :return: The same_name_file_policy of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501
        :rtype: str
        """
        return self._same_name_file_policy

    @same_name_file_policy.setter
    def same_name_file_policy(self, same_name_file_policy):
        """Sets the same_name_file_policy of this DataFlowForDescribeDataFlowsOutput.


        :param same_name_file_policy: The same_name_file_policy of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501
        :type: str
        """

        self._same_name_file_policy = same_name_file_policy

    @property
    def status(self):
        """Gets the status of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501


        :return: The status of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DataFlowForDescribeDataFlowsOutput.


        :param status: The status of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def sync_status(self):
        """Gets the sync_status of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501


        :return: The sync_status of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501
        :rtype: str
        """
        return self._sync_status

    @sync_status.setter
    def sync_status(self, sync_status):
        """Sets the sync_status of this DataFlowForDescribeDataFlowsOutput.


        :param sync_status: The sync_status of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501
        :type: str
        """

        self._sync_status = sync_status

    @property
    def tls_info(self):
        """Gets the tls_info of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501


        :return: The tls_info of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501
        :rtype: TlsInfoForDescribeDataFlowsOutput
        """
        return self._tls_info

    @tls_info.setter
    def tls_info(self, tls_info):
        """Sets the tls_info of this DataFlowForDescribeDataFlowsOutput.


        :param tls_info: The tls_info of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501
        :type: TlsInfoForDescribeDataFlowsOutput
        """

        self._tls_info = tls_info

    @property
    def update_time(self):
        """Gets the update_time of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501


        :return: The update_time of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this DataFlowForDescribeDataFlowsOutput.


        :param update_time: The update_time of this DataFlowForDescribeDataFlowsOutput.  # noqa: E501
        :type: str
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
        if issubclass(DataFlowForDescribeDataFlowsOutput, dict):
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
        if not isinstance(other, DataFlowForDescribeDataFlowsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataFlowForDescribeDataFlowsOutput):
            return True

        return self.to_dict() != other.to_dict()
