# coding: utf-8

"""
    livesaas20230801

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DepartmentForGetLarkSubAccountInfoOutput(object):
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
        'department_id': 'str',
        'name': 'str',
        'sub_department': 'SubDepartmentForGetLarkSubAccountInfoOutput'
    }

    attribute_map = {
        'department_id': 'DepartmentId',
        'name': 'Name',
        'sub_department': 'SubDepartment'
    }

    def __init__(self, department_id=None, name=None, sub_department=None, _configuration=None):  # noqa: E501
        """DepartmentForGetLarkSubAccountInfoOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._department_id = None
        self._name = None
        self._sub_department = None
        self.discriminator = None

        if department_id is not None:
            self.department_id = department_id
        if name is not None:
            self.name = name
        if sub_department is not None:
            self.sub_department = sub_department

    @property
    def department_id(self):
        """Gets the department_id of this DepartmentForGetLarkSubAccountInfoOutput.  # noqa: E501


        :return: The department_id of this DepartmentForGetLarkSubAccountInfoOutput.  # noqa: E501
        :rtype: str
        """
        return self._department_id

    @department_id.setter
    def department_id(self, department_id):
        """Sets the department_id of this DepartmentForGetLarkSubAccountInfoOutput.


        :param department_id: The department_id of this DepartmentForGetLarkSubAccountInfoOutput.  # noqa: E501
        :type: str
        """

        self._department_id = department_id

    @property
    def name(self):
        """Gets the name of this DepartmentForGetLarkSubAccountInfoOutput.  # noqa: E501


        :return: The name of this DepartmentForGetLarkSubAccountInfoOutput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DepartmentForGetLarkSubAccountInfoOutput.


        :param name: The name of this DepartmentForGetLarkSubAccountInfoOutput.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def sub_department(self):
        """Gets the sub_department of this DepartmentForGetLarkSubAccountInfoOutput.  # noqa: E501


        :return: The sub_department of this DepartmentForGetLarkSubAccountInfoOutput.  # noqa: E501
        :rtype: SubDepartmentForGetLarkSubAccountInfoOutput
        """
        return self._sub_department

    @sub_department.setter
    def sub_department(self, sub_department):
        """Sets the sub_department of this DepartmentForGetLarkSubAccountInfoOutput.


        :param sub_department: The sub_department of this DepartmentForGetLarkSubAccountInfoOutput.  # noqa: E501
        :type: SubDepartmentForGetLarkSubAccountInfoOutput
        """

        self._sub_department = sub_department

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
        if issubclass(DepartmentForGetLarkSubAccountInfoOutput, dict):
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
        if not isinstance(other, DepartmentForGetLarkSubAccountInfoOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DepartmentForGetLarkSubAccountInfoOutput):
            return True

        return self.to_dict() != other.to_dict()
