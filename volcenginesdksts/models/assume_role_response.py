# coding: utf-8

"""
    sts

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class AssumeRoleResponse(object):
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
        'assumed_role_user': 'AssumedRoleUserForAssumeRoleOutput',
        'credentials': 'CredentialsForAssumeRoleOutput'
    }

    attribute_map = {
        'assumed_role_user': 'AssumedRoleUser',
        'credentials': 'Credentials'
    }

    def __init__(self, assumed_role_user=None, credentials=None, _configuration=None):  # noqa: E501
        """AssumeRoleResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._assumed_role_user = None
        self._credentials = None
        self.discriminator = None

        if assumed_role_user is not None:
            self.assumed_role_user = assumed_role_user
        if credentials is not None:
            self.credentials = credentials

    @property
    def assumed_role_user(self):
        """Gets the assumed_role_user of this AssumeRoleResponse.  # noqa: E501


        :return: The assumed_role_user of this AssumeRoleResponse.  # noqa: E501
        :rtype: AssumedRoleUserForAssumeRoleOutput
        """
        return self._assumed_role_user

    @assumed_role_user.setter
    def assumed_role_user(self, assumed_role_user):
        """Sets the assumed_role_user of this AssumeRoleResponse.


        :param assumed_role_user: The assumed_role_user of this AssumeRoleResponse.  # noqa: E501
        :type: AssumedRoleUserForAssumeRoleOutput
        """

        self._assumed_role_user = assumed_role_user

    @property
    def credentials(self):
        """Gets the credentials of this AssumeRoleResponse.  # noqa: E501


        :return: The credentials of this AssumeRoleResponse.  # noqa: E501
        :rtype: CredentialsForAssumeRoleOutput
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this AssumeRoleResponse.


        :param credentials: The credentials of this AssumeRoleResponse.  # noqa: E501
        :type: CredentialsForAssumeRoleOutput
        """

        self._credentials = credentials

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
        if issubclass(AssumeRoleResponse, dict):
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
        if not isinstance(other, AssumeRoleResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AssumeRoleResponse):
            return True

        return self.to_dict() != other.to_dict()
