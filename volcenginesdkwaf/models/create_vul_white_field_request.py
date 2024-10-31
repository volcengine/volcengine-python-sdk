# coding: utf-8

"""
    waf

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class CreateVulWhiteFieldRequest(object):
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
        'enable': 'int',
        'field_area': 'str',
        'field_list': 'str',
        'host': 'str',
        'name': 'str',
        'project_name': 'str'
    }

    attribute_map = {
        'enable': 'Enable',
        'field_area': 'FieldArea',
        'field_list': 'FieldList',
        'host': 'Host',
        'name': 'Name',
        'project_name': 'ProjectName'
    }

    def __init__(self, enable=None, field_area=None, field_list=None, host=None, name=None, project_name=None, _configuration=None):  # noqa: E501
        """CreateVulWhiteFieldRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._enable = None
        self._field_area = None
        self._field_list = None
        self._host = None
        self._name = None
        self._project_name = None
        self.discriminator = None

        if enable is not None:
            self.enable = enable
        if field_area is not None:
            self.field_area = field_area
        if field_list is not None:
            self.field_list = field_list
        if host is not None:
            self.host = host
        if name is not None:
            self.name = name
        if project_name is not None:
            self.project_name = project_name

    @property
    def enable(self):
        """Gets the enable of this CreateVulWhiteFieldRequest.  # noqa: E501


        :return: The enable of this CreateVulWhiteFieldRequest.  # noqa: E501
        :rtype: int
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this CreateVulWhiteFieldRequest.


        :param enable: The enable of this CreateVulWhiteFieldRequest.  # noqa: E501
        :type: int
        """

        self._enable = enable

    @property
    def field_area(self):
        """Gets the field_area of this CreateVulWhiteFieldRequest.  # noqa: E501


        :return: The field_area of this CreateVulWhiteFieldRequest.  # noqa: E501
        :rtype: str
        """
        return self._field_area

    @field_area.setter
    def field_area(self, field_area):
        """Sets the field_area of this CreateVulWhiteFieldRequest.


        :param field_area: The field_area of this CreateVulWhiteFieldRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["args", "url", "cookies", "headers", "bodydetail"]  # noqa: E501
        if (self._configuration.client_side_validation and
                field_area not in allowed_values):
            raise ValueError(
                "Invalid value for `field_area` ({0}), must be one of {1}"  # noqa: E501
                .format(field_area, allowed_values)
            )

        self._field_area = field_area

    @property
    def field_list(self):
        """Gets the field_list of this CreateVulWhiteFieldRequest.  # noqa: E501


        :return: The field_list of this CreateVulWhiteFieldRequest.  # noqa: E501
        :rtype: str
        """
        return self._field_list

    @field_list.setter
    def field_list(self, field_list):
        """Sets the field_list of this CreateVulWhiteFieldRequest.


        :param field_list: The field_list of this CreateVulWhiteFieldRequest.  # noqa: E501
        :type: str
        """

        self._field_list = field_list

    @property
    def host(self):
        """Gets the host of this CreateVulWhiteFieldRequest.  # noqa: E501


        :return: The host of this CreateVulWhiteFieldRequest.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this CreateVulWhiteFieldRequest.


        :param host: The host of this CreateVulWhiteFieldRequest.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def name(self):
        """Gets the name of this CreateVulWhiteFieldRequest.  # noqa: E501


        :return: The name of this CreateVulWhiteFieldRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateVulWhiteFieldRequest.


        :param name: The name of this CreateVulWhiteFieldRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def project_name(self):
        """Gets the project_name of this CreateVulWhiteFieldRequest.  # noqa: E501


        :return: The project_name of this CreateVulWhiteFieldRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this CreateVulWhiteFieldRequest.


        :param project_name: The project_name of this CreateVulWhiteFieldRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

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
        if issubclass(CreateVulWhiteFieldRequest, dict):
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
        if not isinstance(other, CreateVulWhiteFieldRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateVulWhiteFieldRequest):
            return True

        return self.to_dict() != other.to_dict()
