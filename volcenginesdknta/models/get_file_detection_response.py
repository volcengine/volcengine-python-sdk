# coding: utf-8

"""
    nta

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class GetFileDetectionResponse(object):
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
        'file_md5': 'str',
        'file_sec_type': 'int',
        'file_size': 'int',
        'finish': 'int',
        'virus_desc': 'str'
    }

    attribute_map = {
        'file_md5': 'FileMd5',
        'file_sec_type': 'FileSecType',
        'file_size': 'FileSize',
        'finish': 'Finish',
        'virus_desc': 'VirusDesc'
    }

    def __init__(self, file_md5=None, file_sec_type=None, file_size=None, finish=None, virus_desc=None, _configuration=None):  # noqa: E501
        """GetFileDetectionResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._file_md5 = None
        self._file_sec_type = None
        self._file_size = None
        self._finish = None
        self._virus_desc = None
        self.discriminator = None

        if file_md5 is not None:
            self.file_md5 = file_md5
        if file_sec_type is not None:
            self.file_sec_type = file_sec_type
        if file_size is not None:
            self.file_size = file_size
        if finish is not None:
            self.finish = finish
        if virus_desc is not None:
            self.virus_desc = virus_desc

    @property
    def file_md5(self):
        """Gets the file_md5 of this GetFileDetectionResponse.  # noqa: E501


        :return: The file_md5 of this GetFileDetectionResponse.  # noqa: E501
        :rtype: str
        """
        return self._file_md5

    @file_md5.setter
    def file_md5(self, file_md5):
        """Sets the file_md5 of this GetFileDetectionResponse.


        :param file_md5: The file_md5 of this GetFileDetectionResponse.  # noqa: E501
        :type: str
        """

        self._file_md5 = file_md5

    @property
    def file_sec_type(self):
        """Gets the file_sec_type of this GetFileDetectionResponse.  # noqa: E501


        :return: The file_sec_type of this GetFileDetectionResponse.  # noqa: E501
        :rtype: int
        """
        return self._file_sec_type

    @file_sec_type.setter
    def file_sec_type(self, file_sec_type):
        """Sets the file_sec_type of this GetFileDetectionResponse.


        :param file_sec_type: The file_sec_type of this GetFileDetectionResponse.  # noqa: E501
        :type: int
        """

        self._file_sec_type = file_sec_type

    @property
    def file_size(self):
        """Gets the file_size of this GetFileDetectionResponse.  # noqa: E501


        :return: The file_size of this GetFileDetectionResponse.  # noqa: E501
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """Sets the file_size of this GetFileDetectionResponse.


        :param file_size: The file_size of this GetFileDetectionResponse.  # noqa: E501
        :type: int
        """

        self._file_size = file_size

    @property
    def finish(self):
        """Gets the finish of this GetFileDetectionResponse.  # noqa: E501


        :return: The finish of this GetFileDetectionResponse.  # noqa: E501
        :rtype: int
        """
        return self._finish

    @finish.setter
    def finish(self, finish):
        """Sets the finish of this GetFileDetectionResponse.


        :param finish: The finish of this GetFileDetectionResponse.  # noqa: E501
        :type: int
        """

        self._finish = finish

    @property
    def virus_desc(self):
        """Gets the virus_desc of this GetFileDetectionResponse.  # noqa: E501


        :return: The virus_desc of this GetFileDetectionResponse.  # noqa: E501
        :rtype: str
        """
        return self._virus_desc

    @virus_desc.setter
    def virus_desc(self, virus_desc):
        """Sets the virus_desc of this GetFileDetectionResponse.


        :param virus_desc: The virus_desc of this GetFileDetectionResponse.  # noqa: E501
        :type: str
        """

        self._virus_desc = virus_desc

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
        if issubclass(GetFileDetectionResponse, dict):
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
        if not isinstance(other, GetFileDetectionResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetFileDetectionResponse):
            return True

        return self.to_dict() != other.to_dict()