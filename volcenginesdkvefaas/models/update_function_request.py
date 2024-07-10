# coding: utf-8

"""
    vefaas

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class UpdateFunctionRequest(object):
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
        'description': 'str',
        'envs': 'list[EnvForUpdateFunctionInput]',
        'exclusive_mode': 'bool',
        'id': 'str',
        'initializer_sec': 'int',
        'max_concurrency': 'int',
        'memory_mb': 'int',
        'nas_storage': 'NasStorageForUpdateFunctionInput',
        'request_timeout': 'int',
        'runtime': 'str',
        'source': 'str',
        'source_access_config': 'SourceAccessConfigForUpdateFunctionInput',
        'source_type': 'str',
        'tls_config': 'TlsConfigForUpdateFunctionInput',
        'tos_mount_config': 'TosMountConfigForUpdateFunctionInput',
        'vpc_config': 'VpcConfigForUpdateFunctionInput'
    }

    attribute_map = {
        'description': 'Description',
        'envs': 'Envs',
        'exclusive_mode': 'ExclusiveMode',
        'id': 'Id',
        'initializer_sec': 'InitializerSec',
        'max_concurrency': 'MaxConcurrency',
        'memory_mb': 'MemoryMB',
        'nas_storage': 'NasStorage',
        'request_timeout': 'RequestTimeout',
        'runtime': 'Runtime',
        'source': 'Source',
        'source_access_config': 'SourceAccessConfig',
        'source_type': 'SourceType',
        'tls_config': 'TlsConfig',
        'tos_mount_config': 'TosMountConfig',
        'vpc_config': 'VpcConfig'
    }

    def __init__(self, description=None, envs=None, exclusive_mode=None, id=None, initializer_sec=None, max_concurrency=None, memory_mb=None, nas_storage=None, request_timeout=None, runtime=None, source=None, source_access_config=None, source_type=None, tls_config=None, tos_mount_config=None, vpc_config=None, _configuration=None):  # noqa: E501
        """UpdateFunctionRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._description = None
        self._envs = None
        self._exclusive_mode = None
        self._id = None
        self._initializer_sec = None
        self._max_concurrency = None
        self._memory_mb = None
        self._nas_storage = None
        self._request_timeout = None
        self._runtime = None
        self._source = None
        self._source_access_config = None
        self._source_type = None
        self._tls_config = None
        self._tos_mount_config = None
        self._vpc_config = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if envs is not None:
            self.envs = envs
        if exclusive_mode is not None:
            self.exclusive_mode = exclusive_mode
        self.id = id
        if initializer_sec is not None:
            self.initializer_sec = initializer_sec
        if max_concurrency is not None:
            self.max_concurrency = max_concurrency
        if memory_mb is not None:
            self.memory_mb = memory_mb
        if nas_storage is not None:
            self.nas_storage = nas_storage
        if request_timeout is not None:
            self.request_timeout = request_timeout
        if runtime is not None:
            self.runtime = runtime
        if source is not None:
            self.source = source
        if source_access_config is not None:
            self.source_access_config = source_access_config
        if source_type is not None:
            self.source_type = source_type
        if tls_config is not None:
            self.tls_config = tls_config
        if tos_mount_config is not None:
            self.tos_mount_config = tos_mount_config
        if vpc_config is not None:
            self.vpc_config = vpc_config

    @property
    def description(self):
        """Gets the description of this UpdateFunctionRequest.  # noqa: E501


        :return: The description of this UpdateFunctionRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateFunctionRequest.


        :param description: The description of this UpdateFunctionRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def envs(self):
        """Gets the envs of this UpdateFunctionRequest.  # noqa: E501


        :return: The envs of this UpdateFunctionRequest.  # noqa: E501
        :rtype: list[EnvForUpdateFunctionInput]
        """
        return self._envs

    @envs.setter
    def envs(self, envs):
        """Sets the envs of this UpdateFunctionRequest.


        :param envs: The envs of this UpdateFunctionRequest.  # noqa: E501
        :type: list[EnvForUpdateFunctionInput]
        """

        self._envs = envs

    @property
    def exclusive_mode(self):
        """Gets the exclusive_mode of this UpdateFunctionRequest.  # noqa: E501


        :return: The exclusive_mode of this UpdateFunctionRequest.  # noqa: E501
        :rtype: bool
        """
        return self._exclusive_mode

    @exclusive_mode.setter
    def exclusive_mode(self, exclusive_mode):
        """Sets the exclusive_mode of this UpdateFunctionRequest.


        :param exclusive_mode: The exclusive_mode of this UpdateFunctionRequest.  # noqa: E501
        :type: bool
        """

        self._exclusive_mode = exclusive_mode

    @property
    def id(self):
        """Gets the id of this UpdateFunctionRequest.  # noqa: E501


        :return: The id of this UpdateFunctionRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateFunctionRequest.


        :param id: The id of this UpdateFunctionRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def initializer_sec(self):
        """Gets the initializer_sec of this UpdateFunctionRequest.  # noqa: E501


        :return: The initializer_sec of this UpdateFunctionRequest.  # noqa: E501
        :rtype: int
        """
        return self._initializer_sec

    @initializer_sec.setter
    def initializer_sec(self, initializer_sec):
        """Sets the initializer_sec of this UpdateFunctionRequest.


        :param initializer_sec: The initializer_sec of this UpdateFunctionRequest.  # noqa: E501
        :type: int
        """

        self._initializer_sec = initializer_sec

    @property
    def max_concurrency(self):
        """Gets the max_concurrency of this UpdateFunctionRequest.  # noqa: E501


        :return: The max_concurrency of this UpdateFunctionRequest.  # noqa: E501
        :rtype: int
        """
        return self._max_concurrency

    @max_concurrency.setter
    def max_concurrency(self, max_concurrency):
        """Sets the max_concurrency of this UpdateFunctionRequest.


        :param max_concurrency: The max_concurrency of this UpdateFunctionRequest.  # noqa: E501
        :type: int
        """

        self._max_concurrency = max_concurrency

    @property
    def memory_mb(self):
        """Gets the memory_mb of this UpdateFunctionRequest.  # noqa: E501


        :return: The memory_mb of this UpdateFunctionRequest.  # noqa: E501
        :rtype: int
        """
        return self._memory_mb

    @memory_mb.setter
    def memory_mb(self, memory_mb):
        """Sets the memory_mb of this UpdateFunctionRequest.


        :param memory_mb: The memory_mb of this UpdateFunctionRequest.  # noqa: E501
        :type: int
        """

        self._memory_mb = memory_mb

    @property
    def nas_storage(self):
        """Gets the nas_storage of this UpdateFunctionRequest.  # noqa: E501


        :return: The nas_storage of this UpdateFunctionRequest.  # noqa: E501
        :rtype: NasStorageForUpdateFunctionInput
        """
        return self._nas_storage

    @nas_storage.setter
    def nas_storage(self, nas_storage):
        """Sets the nas_storage of this UpdateFunctionRequest.


        :param nas_storage: The nas_storage of this UpdateFunctionRequest.  # noqa: E501
        :type: NasStorageForUpdateFunctionInput
        """

        self._nas_storage = nas_storage

    @property
    def request_timeout(self):
        """Gets the request_timeout of this UpdateFunctionRequest.  # noqa: E501


        :return: The request_timeout of this UpdateFunctionRequest.  # noqa: E501
        :rtype: int
        """
        return self._request_timeout

    @request_timeout.setter
    def request_timeout(self, request_timeout):
        """Sets the request_timeout of this UpdateFunctionRequest.


        :param request_timeout: The request_timeout of this UpdateFunctionRequest.  # noqa: E501
        :type: int
        """

        self._request_timeout = request_timeout

    @property
    def runtime(self):
        """Gets the runtime of this UpdateFunctionRequest.  # noqa: E501


        :return: The runtime of this UpdateFunctionRequest.  # noqa: E501
        :rtype: str
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        """Sets the runtime of this UpdateFunctionRequest.


        :param runtime: The runtime of this UpdateFunctionRequest.  # noqa: E501
        :type: str
        """

        self._runtime = runtime

    @property
    def source(self):
        """Gets the source of this UpdateFunctionRequest.  # noqa: E501


        :return: The source of this UpdateFunctionRequest.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this UpdateFunctionRequest.


        :param source: The source of this UpdateFunctionRequest.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def source_access_config(self):
        """Gets the source_access_config of this UpdateFunctionRequest.  # noqa: E501


        :return: The source_access_config of this UpdateFunctionRequest.  # noqa: E501
        :rtype: SourceAccessConfigForUpdateFunctionInput
        """
        return self._source_access_config

    @source_access_config.setter
    def source_access_config(self, source_access_config):
        """Sets the source_access_config of this UpdateFunctionRequest.


        :param source_access_config: The source_access_config of this UpdateFunctionRequest.  # noqa: E501
        :type: SourceAccessConfigForUpdateFunctionInput
        """

        self._source_access_config = source_access_config

    @property
    def source_type(self):
        """Gets the source_type of this UpdateFunctionRequest.  # noqa: E501


        :return: The source_type of this UpdateFunctionRequest.  # noqa: E501
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this UpdateFunctionRequest.


        :param source_type: The source_type of this UpdateFunctionRequest.  # noqa: E501
        :type: str
        """

        self._source_type = source_type

    @property
    def tls_config(self):
        """Gets the tls_config of this UpdateFunctionRequest.  # noqa: E501


        :return: The tls_config of this UpdateFunctionRequest.  # noqa: E501
        :rtype: TlsConfigForUpdateFunctionInput
        """
        return self._tls_config

    @tls_config.setter
    def tls_config(self, tls_config):
        """Sets the tls_config of this UpdateFunctionRequest.


        :param tls_config: The tls_config of this UpdateFunctionRequest.  # noqa: E501
        :type: TlsConfigForUpdateFunctionInput
        """

        self._tls_config = tls_config

    @property
    def tos_mount_config(self):
        """Gets the tos_mount_config of this UpdateFunctionRequest.  # noqa: E501


        :return: The tos_mount_config of this UpdateFunctionRequest.  # noqa: E501
        :rtype: TosMountConfigForUpdateFunctionInput
        """
        return self._tos_mount_config

    @tos_mount_config.setter
    def tos_mount_config(self, tos_mount_config):
        """Sets the tos_mount_config of this UpdateFunctionRequest.


        :param tos_mount_config: The tos_mount_config of this UpdateFunctionRequest.  # noqa: E501
        :type: TosMountConfigForUpdateFunctionInput
        """

        self._tos_mount_config = tos_mount_config

    @property
    def vpc_config(self):
        """Gets the vpc_config of this UpdateFunctionRequest.  # noqa: E501


        :return: The vpc_config of this UpdateFunctionRequest.  # noqa: E501
        :rtype: VpcConfigForUpdateFunctionInput
        """
        return self._vpc_config

    @vpc_config.setter
    def vpc_config(self, vpc_config):
        """Sets the vpc_config of this UpdateFunctionRequest.


        :param vpc_config: The vpc_config of this UpdateFunctionRequest.  # noqa: E501
        :type: VpcConfigForUpdateFunctionInput
        """

        self._vpc_config = vpc_config

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
        if issubclass(UpdateFunctionRequest, dict):
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
        if not isinstance(other, UpdateFunctionRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateFunctionRequest):
            return True

        return self.to_dict() != other.to_dict()
