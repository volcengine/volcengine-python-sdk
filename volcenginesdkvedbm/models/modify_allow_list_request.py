# coding: utf-8

"""
    vedbm

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ModifyAllowListRequest(object):
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
        'allow_list': 'str',
        'allow_list_desc': 'str',
        'allow_list_id': 'str',
        'allow_list_name': 'str',
        'apply_instance_num': 'int',
        'modify_mode': 'int'
    }

    attribute_map = {
        'allow_list': 'AllowList',
        'allow_list_desc': 'AllowListDesc',
        'allow_list_id': 'AllowListId',
        'allow_list_name': 'AllowListName',
        'apply_instance_num': 'ApplyInstanceNum',
        'modify_mode': 'ModifyMode'
    }

    def __init__(self, allow_list=None, allow_list_desc=None, allow_list_id=None, allow_list_name=None, apply_instance_num=None, modify_mode=None, _configuration=None):  # noqa: E501
        """ModifyAllowListRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._allow_list = None
        self._allow_list_desc = None
        self._allow_list_id = None
        self._allow_list_name = None
        self._apply_instance_num = None
        self._modify_mode = None
        self.discriminator = None

        if allow_list is not None:
            self.allow_list = allow_list
        if allow_list_desc is not None:
            self.allow_list_desc = allow_list_desc
        self.allow_list_id = allow_list_id
        self.allow_list_name = allow_list_name
        if apply_instance_num is not None:
            self.apply_instance_num = apply_instance_num
        if modify_mode is not None:
            self.modify_mode = modify_mode

    @property
    def allow_list(self):
        """Gets the allow_list of this ModifyAllowListRequest.  # noqa: E501


        :return: The allow_list of this ModifyAllowListRequest.  # noqa: E501
        :rtype: str
        """
        return self._allow_list

    @allow_list.setter
    def allow_list(self, allow_list):
        """Sets the allow_list of this ModifyAllowListRequest.


        :param allow_list: The allow_list of this ModifyAllowListRequest.  # noqa: E501
        :type: str
        """

        self._allow_list = allow_list

    @property
    def allow_list_desc(self):
        """Gets the allow_list_desc of this ModifyAllowListRequest.  # noqa: E501


        :return: The allow_list_desc of this ModifyAllowListRequest.  # noqa: E501
        :rtype: str
        """
        return self._allow_list_desc

    @allow_list_desc.setter
    def allow_list_desc(self, allow_list_desc):
        """Sets the allow_list_desc of this ModifyAllowListRequest.


        :param allow_list_desc: The allow_list_desc of this ModifyAllowListRequest.  # noqa: E501
        :type: str
        """

        self._allow_list_desc = allow_list_desc

    @property
    def allow_list_id(self):
        """Gets the allow_list_id of this ModifyAllowListRequest.  # noqa: E501


        :return: The allow_list_id of this ModifyAllowListRequest.  # noqa: E501
        :rtype: str
        """
        return self._allow_list_id

    @allow_list_id.setter
    def allow_list_id(self, allow_list_id):
        """Sets the allow_list_id of this ModifyAllowListRequest.


        :param allow_list_id: The allow_list_id of this ModifyAllowListRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and allow_list_id is None:
            raise ValueError("Invalid value for `allow_list_id`, must not be `None`")  # noqa: E501

        self._allow_list_id = allow_list_id

    @property
    def allow_list_name(self):
        """Gets the allow_list_name of this ModifyAllowListRequest.  # noqa: E501


        :return: The allow_list_name of this ModifyAllowListRequest.  # noqa: E501
        :rtype: str
        """
        return self._allow_list_name

    @allow_list_name.setter
    def allow_list_name(self, allow_list_name):
        """Sets the allow_list_name of this ModifyAllowListRequest.


        :param allow_list_name: The allow_list_name of this ModifyAllowListRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and allow_list_name is None:
            raise ValueError("Invalid value for `allow_list_name`, must not be `None`")  # noqa: E501

        self._allow_list_name = allow_list_name

    @property
    def apply_instance_num(self):
        """Gets the apply_instance_num of this ModifyAllowListRequest.  # noqa: E501


        :return: The apply_instance_num of this ModifyAllowListRequest.  # noqa: E501
        :rtype: int
        """
        return self._apply_instance_num

    @apply_instance_num.setter
    def apply_instance_num(self, apply_instance_num):
        """Sets the apply_instance_num of this ModifyAllowListRequest.


        :param apply_instance_num: The apply_instance_num of this ModifyAllowListRequest.  # noqa: E501
        :type: int
        """

        self._apply_instance_num = apply_instance_num

    @property
    def modify_mode(self):
        """Gets the modify_mode of this ModifyAllowListRequest.  # noqa: E501


        :return: The modify_mode of this ModifyAllowListRequest.  # noqa: E501
        :rtype: int
        """
        return self._modify_mode

    @modify_mode.setter
    def modify_mode(self, modify_mode):
        """Sets the modify_mode of this ModifyAllowListRequest.


        :param modify_mode: The modify_mode of this ModifyAllowListRequest.  # noqa: E501
        :type: int
        """

        self._modify_mode = modify_mode

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
        if issubclass(ModifyAllowListRequest, dict):
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
        if not isinstance(other, ModifyAllowListRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModifyAllowListRequest):
            return True

        return self.to_dict() != other.to_dict()
