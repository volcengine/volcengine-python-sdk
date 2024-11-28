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


class DirQuotaInfoForDescribeDirQuotasOutput(object):
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
        'dir_inode': 'int',
        'path': 'str',
        'status': 'str',
        'user_quota_infos': 'list[UserQuotaInfoForDescribeDirQuotasOutput]',
        'user_quota_infos_count': 'int'
    }

    attribute_map = {
        'dir_inode': 'DirInode',
        'path': 'Path',
        'status': 'Status',
        'user_quota_infos': 'UserQuotaInfos',
        'user_quota_infos_count': 'UserQuotaInfosCount'
    }

    def __init__(self, dir_inode=None, path=None, status=None, user_quota_infos=None, user_quota_infos_count=None, _configuration=None):  # noqa: E501
        """DirQuotaInfoForDescribeDirQuotasOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._dir_inode = None
        self._path = None
        self._status = None
        self._user_quota_infos = None
        self._user_quota_infos_count = None
        self.discriminator = None

        if dir_inode is not None:
            self.dir_inode = dir_inode
        if path is not None:
            self.path = path
        if status is not None:
            self.status = status
        if user_quota_infos is not None:
            self.user_quota_infos = user_quota_infos
        if user_quota_infos_count is not None:
            self.user_quota_infos_count = user_quota_infos_count

    @property
    def dir_inode(self):
        """Gets the dir_inode of this DirQuotaInfoForDescribeDirQuotasOutput.  # noqa: E501


        :return: The dir_inode of this DirQuotaInfoForDescribeDirQuotasOutput.  # noqa: E501
        :rtype: int
        """
        return self._dir_inode

    @dir_inode.setter
    def dir_inode(self, dir_inode):
        """Sets the dir_inode of this DirQuotaInfoForDescribeDirQuotasOutput.


        :param dir_inode: The dir_inode of this DirQuotaInfoForDescribeDirQuotasOutput.  # noqa: E501
        :type: int
        """

        self._dir_inode = dir_inode

    @property
    def path(self):
        """Gets the path of this DirQuotaInfoForDescribeDirQuotasOutput.  # noqa: E501


        :return: The path of this DirQuotaInfoForDescribeDirQuotasOutput.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this DirQuotaInfoForDescribeDirQuotasOutput.


        :param path: The path of this DirQuotaInfoForDescribeDirQuotasOutput.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def status(self):
        """Gets the status of this DirQuotaInfoForDescribeDirQuotasOutput.  # noqa: E501


        :return: The status of this DirQuotaInfoForDescribeDirQuotasOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DirQuotaInfoForDescribeDirQuotasOutput.


        :param status: The status of this DirQuotaInfoForDescribeDirQuotasOutput.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def user_quota_infos(self):
        """Gets the user_quota_infos of this DirQuotaInfoForDescribeDirQuotasOutput.  # noqa: E501


        :return: The user_quota_infos of this DirQuotaInfoForDescribeDirQuotasOutput.  # noqa: E501
        :rtype: list[UserQuotaInfoForDescribeDirQuotasOutput]
        """
        return self._user_quota_infos

    @user_quota_infos.setter
    def user_quota_infos(self, user_quota_infos):
        """Sets the user_quota_infos of this DirQuotaInfoForDescribeDirQuotasOutput.


        :param user_quota_infos: The user_quota_infos of this DirQuotaInfoForDescribeDirQuotasOutput.  # noqa: E501
        :type: list[UserQuotaInfoForDescribeDirQuotasOutput]
        """

        self._user_quota_infos = user_quota_infos

    @property
    def user_quota_infos_count(self):
        """Gets the user_quota_infos_count of this DirQuotaInfoForDescribeDirQuotasOutput.  # noqa: E501


        :return: The user_quota_infos_count of this DirQuotaInfoForDescribeDirQuotasOutput.  # noqa: E501
        :rtype: int
        """
        return self._user_quota_infos_count

    @user_quota_infos_count.setter
    def user_quota_infos_count(self, user_quota_infos_count):
        """Sets the user_quota_infos_count of this DirQuotaInfoForDescribeDirQuotasOutput.


        :param user_quota_infos_count: The user_quota_infos_count of this DirQuotaInfoForDescribeDirQuotasOutput.  # noqa: E501
        :type: int
        """

        self._user_quota_infos_count = user_quota_infos_count

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
        if issubclass(DirQuotaInfoForDescribeDirQuotasOutput, dict):
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
        if not isinstance(other, DirQuotaInfoForDescribeDirQuotasOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DirQuotaInfoForDescribeDirQuotasOutput):
            return True

        return self.to_dict() != other.to_dict()