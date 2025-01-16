# coding: utf-8

"""
    alb

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ModifyCustomizedCfgAttributesRequest(object):
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
        'customized_cfg_content': 'str',
        'customized_cfg_id': 'str',
        'customized_cfg_name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'customized_cfg_content': 'CustomizedCfgContent',
        'customized_cfg_id': 'CustomizedCfgId',
        'customized_cfg_name': 'CustomizedCfgName',
        'description': 'Description'
    }

    def __init__(self, customized_cfg_content=None, customized_cfg_id=None, customized_cfg_name=None, description=None, _configuration=None):  # noqa: E501
        """ModifyCustomizedCfgAttributesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._customized_cfg_content = None
        self._customized_cfg_id = None
        self._customized_cfg_name = None
        self._description = None
        self.discriminator = None

        if customized_cfg_content is not None:
            self.customized_cfg_content = customized_cfg_content
        if customized_cfg_id is not None:
            self.customized_cfg_id = customized_cfg_id
        if customized_cfg_name is not None:
            self.customized_cfg_name = customized_cfg_name
        if description is not None:
            self.description = description

    @property
    def customized_cfg_content(self):
        """Gets the customized_cfg_content of this ModifyCustomizedCfgAttributesRequest.  # noqa: E501


        :return: The customized_cfg_content of this ModifyCustomizedCfgAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._customized_cfg_content

    @customized_cfg_content.setter
    def customized_cfg_content(self, customized_cfg_content):
        """Sets the customized_cfg_content of this ModifyCustomizedCfgAttributesRequest.


        :param customized_cfg_content: The customized_cfg_content of this ModifyCustomizedCfgAttributesRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                customized_cfg_content is not None and len(customized_cfg_content) > 4096):
            raise ValueError("Invalid value for `customized_cfg_content`, length must be less than or equal to `4096`")  # noqa: E501
        if (self._configuration.client_side_validation and
                customized_cfg_content is not None and len(customized_cfg_content) < 1):
            raise ValueError("Invalid value for `customized_cfg_content`, length must be greater than or equal to `1`")  # noqa: E501

        self._customized_cfg_content = customized_cfg_content

    @property
    def customized_cfg_id(self):
        """Gets the customized_cfg_id of this ModifyCustomizedCfgAttributesRequest.  # noqa: E501


        :return: The customized_cfg_id of this ModifyCustomizedCfgAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._customized_cfg_id

    @customized_cfg_id.setter
    def customized_cfg_id(self, customized_cfg_id):
        """Sets the customized_cfg_id of this ModifyCustomizedCfgAttributesRequest.


        :param customized_cfg_id: The customized_cfg_id of this ModifyCustomizedCfgAttributesRequest.  # noqa: E501
        :type: str
        """

        self._customized_cfg_id = customized_cfg_id

    @property
    def customized_cfg_name(self):
        """Gets the customized_cfg_name of this ModifyCustomizedCfgAttributesRequest.  # noqa: E501


        :return: The customized_cfg_name of this ModifyCustomizedCfgAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._customized_cfg_name

    @customized_cfg_name.setter
    def customized_cfg_name(self, customized_cfg_name):
        """Sets the customized_cfg_name of this ModifyCustomizedCfgAttributesRequest.


        :param customized_cfg_name: The customized_cfg_name of this ModifyCustomizedCfgAttributesRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                customized_cfg_name is not None and len(customized_cfg_name) > 128):
            raise ValueError("Invalid value for `customized_cfg_name`, length must be less than or equal to `128`")  # noqa: E501
        if (self._configuration.client_side_validation and
                customized_cfg_name is not None and len(customized_cfg_name) < 1):
            raise ValueError("Invalid value for `customized_cfg_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._customized_cfg_name = customized_cfg_name

    @property
    def description(self):
        """Gets the description of this ModifyCustomizedCfgAttributesRequest.  # noqa: E501


        :return: The description of this ModifyCustomizedCfgAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ModifyCustomizedCfgAttributesRequest.


        :param description: The description of this ModifyCustomizedCfgAttributesRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                description is not None and len(description) > 255):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                description is not None and len(description) < 1):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `1`")  # noqa: E501

        self._description = description

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
        if issubclass(ModifyCustomizedCfgAttributesRequest, dict):
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
        if not isinstance(other, ModifyCustomizedCfgAttributesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModifyCustomizedCfgAttributesRequest):
            return True

        return self.to_dict() != other.to_dict()
