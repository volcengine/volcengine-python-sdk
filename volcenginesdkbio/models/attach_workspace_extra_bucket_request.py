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


class AttachWorkspaceExtraBucketRequest(object):
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
        'bucket': 'str',
        'id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'bucket': 'Bucket',
        'id': 'ID',
        'type': 'Type'
    }

    def __init__(self, bucket=None, id=None, type=None, _configuration=None):  # noqa: E501
        """AttachWorkspaceExtraBucketRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bucket = None
        self._id = None
        self._type = None
        self.discriminator = None

        self.bucket = bucket
        self.id = id
        self.type = type

    @property
    def bucket(self):
        """Gets the bucket of this AttachWorkspaceExtraBucketRequest.  # noqa: E501


        :return: The bucket of this AttachWorkspaceExtraBucketRequest.  # noqa: E501
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this AttachWorkspaceExtraBucketRequest.


        :param bucket: The bucket of this AttachWorkspaceExtraBucketRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and bucket is None:
            raise ValueError("Invalid value for `bucket`, must not be `None`")  # noqa: E501

        self._bucket = bucket

    @property
    def id(self):
        """Gets the id of this AttachWorkspaceExtraBucketRequest.  # noqa: E501


        :return: The id of this AttachWorkspaceExtraBucketRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AttachWorkspaceExtraBucketRequest.


        :param id: The id of this AttachWorkspaceExtraBucketRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def type(self):
        """Gets the type of this AttachWorkspaceExtraBucketRequest.  # noqa: E501


        :return: The type of this AttachWorkspaceExtraBucketRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AttachWorkspaceExtraBucketRequest.


        :param type: The type of this AttachWorkspaceExtraBucketRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["PublicCloud"]  # noqa: E501
        if (self._configuration.client_side_validation and
                type not in allowed_values):
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(AttachWorkspaceExtraBucketRequest, dict):
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
        if not isinstance(other, AttachWorkspaceExtraBucketRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AttachWorkspaceExtraBucketRequest):
            return True

        return self.to_dict() != other.to_dict()
