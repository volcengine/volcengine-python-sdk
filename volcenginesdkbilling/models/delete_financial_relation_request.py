# coding: utf-8

"""
    billing

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DeleteFinancialRelationRequest(object):
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
        'relation': 'int',
        'relation_id': 'str',
        'sub_account_id': 'int'
    }

    attribute_map = {
        'relation': 'Relation',
        'relation_id': 'RelationID',
        'sub_account_id': 'SubAccountID'
    }

    def __init__(self, relation=None, relation_id=None, sub_account_id=None, _configuration=None):  # noqa: E501
        """DeleteFinancialRelationRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._relation = None
        self._relation_id = None
        self._sub_account_id = None
        self.discriminator = None

        self.relation = relation
        self.relation_id = relation_id
        self.sub_account_id = sub_account_id

    @property
    def relation(self):
        """Gets the relation of this DeleteFinancialRelationRequest.  # noqa: E501


        :return: The relation of this DeleteFinancialRelationRequest.  # noqa: E501
        :rtype: int
        """
        return self._relation

    @relation.setter
    def relation(self, relation):
        """Sets the relation of this DeleteFinancialRelationRequest.


        :param relation: The relation of this DeleteFinancialRelationRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and relation is None:
            raise ValueError("Invalid value for `relation`, must not be `None`")  # noqa: E501

        self._relation = relation

    @property
    def relation_id(self):
        """Gets the relation_id of this DeleteFinancialRelationRequest.  # noqa: E501


        :return: The relation_id of this DeleteFinancialRelationRequest.  # noqa: E501
        :rtype: str
        """
        return self._relation_id

    @relation_id.setter
    def relation_id(self, relation_id):
        """Sets the relation_id of this DeleteFinancialRelationRequest.


        :param relation_id: The relation_id of this DeleteFinancialRelationRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and relation_id is None:
            raise ValueError("Invalid value for `relation_id`, must not be `None`")  # noqa: E501

        self._relation_id = relation_id

    @property
    def sub_account_id(self):
        """Gets the sub_account_id of this DeleteFinancialRelationRequest.  # noqa: E501


        :return: The sub_account_id of this DeleteFinancialRelationRequest.  # noqa: E501
        :rtype: int
        """
        return self._sub_account_id

    @sub_account_id.setter
    def sub_account_id(self, sub_account_id):
        """Sets the sub_account_id of this DeleteFinancialRelationRequest.


        :param sub_account_id: The sub_account_id of this DeleteFinancialRelationRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and sub_account_id is None:
            raise ValueError("Invalid value for `sub_account_id`, must not be `None`")  # noqa: E501

        self._sub_account_id = sub_account_id

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
        if issubclass(DeleteFinancialRelationRequest, dict):
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
        if not isinstance(other, DeleteFinancialRelationRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeleteFinancialRelationRequest):
            return True

        return self.to_dict() != other.to_dict()