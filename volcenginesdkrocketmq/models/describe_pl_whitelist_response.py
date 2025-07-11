# coding: utf-8

"""
    rocketmq

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribePLWhitelistResponse(object):
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
        'account_ids': 'list[str]',
        'instance_id': 'str',
        'private_link_id': 'str'
    }

    attribute_map = {
        'account_ids': 'AccountIds',
        'instance_id': 'InstanceId',
        'private_link_id': 'PrivateLinkId'
    }

    def __init__(self, account_ids=None, instance_id=None, private_link_id=None, _configuration=None):  # noqa: E501
        """DescribePLWhitelistResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_ids = None
        self._instance_id = None
        self._private_link_id = None
        self.discriminator = None

        if account_ids is not None:
            self.account_ids = account_ids
        if instance_id is not None:
            self.instance_id = instance_id
        if private_link_id is not None:
            self.private_link_id = private_link_id

    @property
    def account_ids(self):
        """Gets the account_ids of this DescribePLWhitelistResponse.  # noqa: E501


        :return: The account_ids of this DescribePLWhitelistResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._account_ids

    @account_ids.setter
    def account_ids(self, account_ids):
        """Sets the account_ids of this DescribePLWhitelistResponse.


        :param account_ids: The account_ids of this DescribePLWhitelistResponse.  # noqa: E501
        :type: list[str]
        """

        self._account_ids = account_ids

    @property
    def instance_id(self):
        """Gets the instance_id of this DescribePLWhitelistResponse.  # noqa: E501


        :return: The instance_id of this DescribePLWhitelistResponse.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this DescribePLWhitelistResponse.


        :param instance_id: The instance_id of this DescribePLWhitelistResponse.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def private_link_id(self):
        """Gets the private_link_id of this DescribePLWhitelistResponse.  # noqa: E501


        :return: The private_link_id of this DescribePLWhitelistResponse.  # noqa: E501
        :rtype: str
        """
        return self._private_link_id

    @private_link_id.setter
    def private_link_id(self, private_link_id):
        """Sets the private_link_id of this DescribePLWhitelistResponse.


        :param private_link_id: The private_link_id of this DescribePLWhitelistResponse.  # noqa: E501
        :type: str
        """

        self._private_link_id = private_link_id

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
        if issubclass(DescribePLWhitelistResponse, dict):
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
        if not isinstance(other, DescribePLWhitelistResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribePLWhitelistResponse):
            return True

        return self.to_dict() != other.to_dict()
