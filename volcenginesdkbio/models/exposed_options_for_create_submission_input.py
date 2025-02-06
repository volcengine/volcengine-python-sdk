# coding: utf-8

"""
    bio

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ExposedOptionsForCreateSubmissionInput(object):
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
        'aai_passport': 'str',
        'execution_root_dir': 'str',
        'mount_tos': 'bool',
        'read_from_cache': 'bool'
    }

    attribute_map = {
        'aai_passport': 'AAIPassport',
        'execution_root_dir': 'ExecutionRootDir',
        'mount_tos': 'MountTOS',
        'read_from_cache': 'ReadFromCache'
    }

    def __init__(self, aai_passport=None, execution_root_dir=None, mount_tos=None, read_from_cache=None, _configuration=None):  # noqa: E501
        """ExposedOptionsForCreateSubmissionInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._aai_passport = None
        self._execution_root_dir = None
        self._mount_tos = None
        self._read_from_cache = None
        self.discriminator = None

        if aai_passport is not None:
            self.aai_passport = aai_passport
        if execution_root_dir is not None:
            self.execution_root_dir = execution_root_dir
        if mount_tos is not None:
            self.mount_tos = mount_tos
        if read_from_cache is not None:
            self.read_from_cache = read_from_cache

    @property
    def aai_passport(self):
        """Gets the aai_passport of this ExposedOptionsForCreateSubmissionInput.  # noqa: E501


        :return: The aai_passport of this ExposedOptionsForCreateSubmissionInput.  # noqa: E501
        :rtype: str
        """
        return self._aai_passport

    @aai_passport.setter
    def aai_passport(self, aai_passport):
        """Sets the aai_passport of this ExposedOptionsForCreateSubmissionInput.


        :param aai_passport: The aai_passport of this ExposedOptionsForCreateSubmissionInput.  # noqa: E501
        :type: str
        """

        self._aai_passport = aai_passport

    @property
    def execution_root_dir(self):
        """Gets the execution_root_dir of this ExposedOptionsForCreateSubmissionInput.  # noqa: E501


        :return: The execution_root_dir of this ExposedOptionsForCreateSubmissionInput.  # noqa: E501
        :rtype: str
        """
        return self._execution_root_dir

    @execution_root_dir.setter
    def execution_root_dir(self, execution_root_dir):
        """Sets the execution_root_dir of this ExposedOptionsForCreateSubmissionInput.


        :param execution_root_dir: The execution_root_dir of this ExposedOptionsForCreateSubmissionInput.  # noqa: E501
        :type: str
        """

        self._execution_root_dir = execution_root_dir

    @property
    def mount_tos(self):
        """Gets the mount_tos of this ExposedOptionsForCreateSubmissionInput.  # noqa: E501


        :return: The mount_tos of this ExposedOptionsForCreateSubmissionInput.  # noqa: E501
        :rtype: bool
        """
        return self._mount_tos

    @mount_tos.setter
    def mount_tos(self, mount_tos):
        """Sets the mount_tos of this ExposedOptionsForCreateSubmissionInput.


        :param mount_tos: The mount_tos of this ExposedOptionsForCreateSubmissionInput.  # noqa: E501
        :type: bool
        """

        self._mount_tos = mount_tos

    @property
    def read_from_cache(self):
        """Gets the read_from_cache of this ExposedOptionsForCreateSubmissionInput.  # noqa: E501


        :return: The read_from_cache of this ExposedOptionsForCreateSubmissionInput.  # noqa: E501
        :rtype: bool
        """
        return self._read_from_cache

    @read_from_cache.setter
    def read_from_cache(self, read_from_cache):
        """Sets the read_from_cache of this ExposedOptionsForCreateSubmissionInput.


        :param read_from_cache: The read_from_cache of this ExposedOptionsForCreateSubmissionInput.  # noqa: E501
        :type: bool
        """

        self._read_from_cache = read_from_cache

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
        if issubclass(ExposedOptionsForCreateSubmissionInput, dict):
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
        if not isinstance(other, ExposedOptionsForCreateSubmissionInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExposedOptionsForCreateSubmissionInput):
            return True

        return self.to_dict() != other.to_dict()
