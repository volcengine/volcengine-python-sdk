# coding: utf-8

"""
    vpc

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class Ipv6GatewayForDescribeIpv6GatewaysOutput(object):
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
        'creation_time': 'str',
        'description': 'str',
        'ipv6_gateway_id': 'str',
        'name': 'str',
        'status': 'str',
        'update_time': 'str',
        'vpc_id': 'str'
    }

    attribute_map = {
        'creation_time': 'CreationTime',
        'description': 'Description',
        'ipv6_gateway_id': 'Ipv6GatewayId',
        'name': 'Name',
        'status': 'Status',
        'update_time': 'UpdateTime',
        'vpc_id': 'VpcId'
    }

    def __init__(self, creation_time=None, description=None, ipv6_gateway_id=None, name=None, status=None, update_time=None, vpc_id=None, _configuration=None):  # noqa: E501
        """Ipv6GatewayForDescribeIpv6GatewaysOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._creation_time = None
        self._description = None
        self._ipv6_gateway_id = None
        self._name = None
        self._status = None
        self._update_time = None
        self._vpc_id = None
        self.discriminator = None

        if creation_time is not None:
            self.creation_time = creation_time
        if description is not None:
            self.description = description
        if ipv6_gateway_id is not None:
            self.ipv6_gateway_id = ipv6_gateway_id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if update_time is not None:
            self.update_time = update_time
        if vpc_id is not None:
            self.vpc_id = vpc_id

    @property
    def creation_time(self):
        """Gets the creation_time of this Ipv6GatewayForDescribeIpv6GatewaysOutput.  # noqa: E501


        :return: The creation_time of this Ipv6GatewayForDescribeIpv6GatewaysOutput.  # noqa: E501
        :rtype: str
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this Ipv6GatewayForDescribeIpv6GatewaysOutput.


        :param creation_time: The creation_time of this Ipv6GatewayForDescribeIpv6GatewaysOutput.  # noqa: E501
        :type: str
        """

        self._creation_time = creation_time

    @property
    def description(self):
        """Gets the description of this Ipv6GatewayForDescribeIpv6GatewaysOutput.  # noqa: E501


        :return: The description of this Ipv6GatewayForDescribeIpv6GatewaysOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Ipv6GatewayForDescribeIpv6GatewaysOutput.


        :param description: The description of this Ipv6GatewayForDescribeIpv6GatewaysOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def ipv6_gateway_id(self):
        """Gets the ipv6_gateway_id of this Ipv6GatewayForDescribeIpv6GatewaysOutput.  # noqa: E501


        :return: The ipv6_gateway_id of this Ipv6GatewayForDescribeIpv6GatewaysOutput.  # noqa: E501
        :rtype: str
        """
        return self._ipv6_gateway_id

    @ipv6_gateway_id.setter
    def ipv6_gateway_id(self, ipv6_gateway_id):
        """Sets the ipv6_gateway_id of this Ipv6GatewayForDescribeIpv6GatewaysOutput.


        :param ipv6_gateway_id: The ipv6_gateway_id of this Ipv6GatewayForDescribeIpv6GatewaysOutput.  # noqa: E501
        :type: str
        """

        self._ipv6_gateway_id = ipv6_gateway_id

    @property
    def name(self):
        """Gets the name of this Ipv6GatewayForDescribeIpv6GatewaysOutput.  # noqa: E501


        :return: The name of this Ipv6GatewayForDescribeIpv6GatewaysOutput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Ipv6GatewayForDescribeIpv6GatewaysOutput.


        :param name: The name of this Ipv6GatewayForDescribeIpv6GatewaysOutput.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def status(self):
        """Gets the status of this Ipv6GatewayForDescribeIpv6GatewaysOutput.  # noqa: E501


        :return: The status of this Ipv6GatewayForDescribeIpv6GatewaysOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Ipv6GatewayForDescribeIpv6GatewaysOutput.


        :param status: The status of this Ipv6GatewayForDescribeIpv6GatewaysOutput.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def update_time(self):
        """Gets the update_time of this Ipv6GatewayForDescribeIpv6GatewaysOutput.  # noqa: E501


        :return: The update_time of this Ipv6GatewayForDescribeIpv6GatewaysOutput.  # noqa: E501
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this Ipv6GatewayForDescribeIpv6GatewaysOutput.


        :param update_time: The update_time of this Ipv6GatewayForDescribeIpv6GatewaysOutput.  # noqa: E501
        :type: str
        """

        self._update_time = update_time

    @property
    def vpc_id(self):
        """Gets the vpc_id of this Ipv6GatewayForDescribeIpv6GatewaysOutput.  # noqa: E501


        :return: The vpc_id of this Ipv6GatewayForDescribeIpv6GatewaysOutput.  # noqa: E501
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this Ipv6GatewayForDescribeIpv6GatewaysOutput.


        :param vpc_id: The vpc_id of this Ipv6GatewayForDescribeIpv6GatewaysOutput.  # noqa: E501
        :type: str
        """

        self._vpc_id = vpc_id

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
        if issubclass(Ipv6GatewayForDescribeIpv6GatewaysOutput, dict):
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
        if not isinstance(other, Ipv6GatewayForDescribeIpv6GatewaysOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Ipv6GatewayForDescribeIpv6GatewaysOutput):
            return True

        return self.to_dict() != other.to_dict()