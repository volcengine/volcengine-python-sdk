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


class CreateDataFlowRequest(object):
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
        'enable_tls_log': 'bool',
        'evict_policy': 'EvictPolicyForCreateDataFlowInput',
        'export_policy': 'ExportPolicyForCreateDataFlowInput',
        'file_system_id': 'str',
        'file_system_path': 'str',
        'import_policy': 'ImportPolicyForCreateDataFlowInput',
        'name': 'str',
        'same_name_file_policy': 'str'
    }

    attribute_map = {
        'bucket_name': 'BucketName',
        'bucket_prefix': 'BucketPrefix',
        'enable_tls_log': 'EnableTlsLog',
        'evict_policy': 'EvictPolicy',
        'export_policy': 'ExportPolicy',
        'file_system_id': 'FileSystemId',
        'file_system_path': 'FileSystemPath',
        'import_policy': 'ImportPolicy',
        'name': 'Name',
        'same_name_file_policy': 'SameNameFilePolicy'
    }

    def __init__(self, bucket_name=None, bucket_prefix=None, enable_tls_log=None, evict_policy=None, export_policy=None, file_system_id=None, file_system_path=None, import_policy=None, name=None, same_name_file_policy=None, _configuration=None):  # noqa: E501
        """CreateDataFlowRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bucket_name = None
        self._bucket_prefix = None
        self._enable_tls_log = None
        self._evict_policy = None
        self._export_policy = None
        self._file_system_id = None
        self._file_system_path = None
        self._import_policy = None
        self._name = None
        self._same_name_file_policy = None
        self.discriminator = None

        self.bucket_name = bucket_name
        if bucket_prefix is not None:
            self.bucket_prefix = bucket_prefix
        if enable_tls_log is not None:
            self.enable_tls_log = enable_tls_log
        if evict_policy is not None:
            self.evict_policy = evict_policy
        if export_policy is not None:
            self.export_policy = export_policy
        self.file_system_id = file_system_id
        self.file_system_path = file_system_path
        if import_policy is not None:
            self.import_policy = import_policy
        self.name = name
        self.same_name_file_policy = same_name_file_policy

    @property
    def bucket_name(self):
        """Gets the bucket_name of this CreateDataFlowRequest.  # noqa: E501


        :return: The bucket_name of this CreateDataFlowRequest.  # noqa: E501
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """Sets the bucket_name of this CreateDataFlowRequest.


        :param bucket_name: The bucket_name of this CreateDataFlowRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and bucket_name is None:
            raise ValueError("Invalid value for `bucket_name`, must not be `None`")  # noqa: E501

        self._bucket_name = bucket_name

    @property
    def bucket_prefix(self):
        """Gets the bucket_prefix of this CreateDataFlowRequest.  # noqa: E501


        :return: The bucket_prefix of this CreateDataFlowRequest.  # noqa: E501
        :rtype: str
        """
        return self._bucket_prefix

    @bucket_prefix.setter
    def bucket_prefix(self, bucket_prefix):
        """Sets the bucket_prefix of this CreateDataFlowRequest.


        :param bucket_prefix: The bucket_prefix of this CreateDataFlowRequest.  # noqa: E501
        :type: str
        """

        self._bucket_prefix = bucket_prefix

    @property
    def enable_tls_log(self):
        """Gets the enable_tls_log of this CreateDataFlowRequest.  # noqa: E501


        :return: The enable_tls_log of this CreateDataFlowRequest.  # noqa: E501
        :rtype: bool
        """
        return self._enable_tls_log

    @enable_tls_log.setter
    def enable_tls_log(self, enable_tls_log):
        """Sets the enable_tls_log of this CreateDataFlowRequest.


        :param enable_tls_log: The enable_tls_log of this CreateDataFlowRequest.  # noqa: E501
        :type: bool
        """

        self._enable_tls_log = enable_tls_log

    @property
    def evict_policy(self):
        """Gets the evict_policy of this CreateDataFlowRequest.  # noqa: E501


        :return: The evict_policy of this CreateDataFlowRequest.  # noqa: E501
        :rtype: EvictPolicyForCreateDataFlowInput
        """
        return self._evict_policy

    @evict_policy.setter
    def evict_policy(self, evict_policy):
        """Sets the evict_policy of this CreateDataFlowRequest.


        :param evict_policy: The evict_policy of this CreateDataFlowRequest.  # noqa: E501
        :type: EvictPolicyForCreateDataFlowInput
        """

        self._evict_policy = evict_policy

    @property
    def export_policy(self):
        """Gets the export_policy of this CreateDataFlowRequest.  # noqa: E501


        :return: The export_policy of this CreateDataFlowRequest.  # noqa: E501
        :rtype: ExportPolicyForCreateDataFlowInput
        """
        return self._export_policy

    @export_policy.setter
    def export_policy(self, export_policy):
        """Sets the export_policy of this CreateDataFlowRequest.


        :param export_policy: The export_policy of this CreateDataFlowRequest.  # noqa: E501
        :type: ExportPolicyForCreateDataFlowInput
        """

        self._export_policy = export_policy

    @property
    def file_system_id(self):
        """Gets the file_system_id of this CreateDataFlowRequest.  # noqa: E501


        :return: The file_system_id of this CreateDataFlowRequest.  # noqa: E501
        :rtype: str
        """
        return self._file_system_id

    @file_system_id.setter
    def file_system_id(self, file_system_id):
        """Sets the file_system_id of this CreateDataFlowRequest.


        :param file_system_id: The file_system_id of this CreateDataFlowRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and file_system_id is None:
            raise ValueError("Invalid value for `file_system_id`, must not be `None`")  # noqa: E501

        self._file_system_id = file_system_id

    @property
    def file_system_path(self):
        """Gets the file_system_path of this CreateDataFlowRequest.  # noqa: E501


        :return: The file_system_path of this CreateDataFlowRequest.  # noqa: E501
        :rtype: str
        """
        return self._file_system_path

    @file_system_path.setter
    def file_system_path(self, file_system_path):
        """Sets the file_system_path of this CreateDataFlowRequest.


        :param file_system_path: The file_system_path of this CreateDataFlowRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and file_system_path is None:
            raise ValueError("Invalid value for `file_system_path`, must not be `None`")  # noqa: E501

        self._file_system_path = file_system_path

    @property
    def import_policy(self):
        """Gets the import_policy of this CreateDataFlowRequest.  # noqa: E501


        :return: The import_policy of this CreateDataFlowRequest.  # noqa: E501
        :rtype: ImportPolicyForCreateDataFlowInput
        """
        return self._import_policy

    @import_policy.setter
    def import_policy(self, import_policy):
        """Sets the import_policy of this CreateDataFlowRequest.


        :param import_policy: The import_policy of this CreateDataFlowRequest.  # noqa: E501
        :type: ImportPolicyForCreateDataFlowInput
        """

        self._import_policy = import_policy

    @property
    def name(self):
        """Gets the name of this CreateDataFlowRequest.  # noqa: E501


        :return: The name of this CreateDataFlowRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateDataFlowRequest.


        :param name: The name of this CreateDataFlowRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def same_name_file_policy(self):
        """Gets the same_name_file_policy of this CreateDataFlowRequest.  # noqa: E501


        :return: The same_name_file_policy of this CreateDataFlowRequest.  # noqa: E501
        :rtype: str
        """
        return self._same_name_file_policy

    @same_name_file_policy.setter
    def same_name_file_policy(self, same_name_file_policy):
        """Sets the same_name_file_policy of this CreateDataFlowRequest.


        :param same_name_file_policy: The same_name_file_policy of this CreateDataFlowRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and same_name_file_policy is None:
            raise ValueError("Invalid value for `same_name_file_policy`, must not be `None`")  # noqa: E501
        allowed_values = ["Skip", "KeepLatest", "OverWrite"]  # noqa: E501
        if (self._configuration.client_side_validation and
                same_name_file_policy not in allowed_values):
            raise ValueError(
                "Invalid value for `same_name_file_policy` ({0}), must be one of {1}"  # noqa: E501
                .format(same_name_file_policy, allowed_values)
            )

        self._same_name_file_policy = same_name_file_policy

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
        if issubclass(CreateDataFlowRequest, dict):
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
        if not isinstance(other, CreateDataFlowRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateDataFlowRequest):
            return True

        return self.to_dict() != other.to_dict()
