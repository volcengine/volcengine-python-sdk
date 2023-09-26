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


class HaVipForDescribeHaVipsOutput(object):
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
        'account_id': 'str',
        'associated_eip_address': 'str',
        'associated_eip_id': 'str',
        'associated_instance_ids': 'list[str]',
        'associated_instance_type': 'str',
        'created_at': 'str',
        'description': 'str',
        'ha_vip_id': 'str',
        'ha_vip_name': 'str',
        'ip_address': 'str',
        'master_instance_id': 'str',
        'project_name': 'str',
        'status': 'str',
        'subnet_id': 'str',
        'updated_at': 'str',
        'vpc_id': 'str'
    }

    attribute_map = {
        'account_id': 'AccountId',
        'associated_eip_address': 'AssociatedEipAddress',
        'associated_eip_id': 'AssociatedEipId',
        'associated_instance_ids': 'AssociatedInstanceIds',
        'associated_instance_type': 'AssociatedInstanceType',
        'created_at': 'CreatedAt',
        'description': 'Description',
        'ha_vip_id': 'HaVipId',
        'ha_vip_name': 'HaVipName',
        'ip_address': 'IpAddress',
        'master_instance_id': 'MasterInstanceId',
        'project_name': 'ProjectName',
        'status': 'Status',
        'subnet_id': 'SubnetId',
        'updated_at': 'UpdatedAt',
        'vpc_id': 'VpcId'
    }

    def __init__(self, account_id=None, associated_eip_address=None, associated_eip_id=None, associated_instance_ids=None, associated_instance_type=None, created_at=None, description=None, ha_vip_id=None, ha_vip_name=None, ip_address=None, master_instance_id=None, project_name=None, status=None, subnet_id=None, updated_at=None, vpc_id=None, _configuration=None):  # noqa: E501
        """HaVipForDescribeHaVipsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_id = None
        self._associated_eip_address = None
        self._associated_eip_id = None
        self._associated_instance_ids = None
        self._associated_instance_type = None
        self._created_at = None
        self._description = None
        self._ha_vip_id = None
        self._ha_vip_name = None
        self._ip_address = None
        self._master_instance_id = None
        self._project_name = None
        self._status = None
        self._subnet_id = None
        self._updated_at = None
        self._vpc_id = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if associated_eip_address is not None:
            self.associated_eip_address = associated_eip_address
        if associated_eip_id is not None:
            self.associated_eip_id = associated_eip_id
        if associated_instance_ids is not None:
            self.associated_instance_ids = associated_instance_ids
        if associated_instance_type is not None:
            self.associated_instance_type = associated_instance_type
        if created_at is not None:
            self.created_at = created_at
        if description is not None:
            self.description = description
        if ha_vip_id is not None:
            self.ha_vip_id = ha_vip_id
        if ha_vip_name is not None:
            self.ha_vip_name = ha_vip_name
        if ip_address is not None:
            self.ip_address = ip_address
        if master_instance_id is not None:
            self.master_instance_id = master_instance_id
        if project_name is not None:
            self.project_name = project_name
        if status is not None:
            self.status = status
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if updated_at is not None:
            self.updated_at = updated_at
        if vpc_id is not None:
            self.vpc_id = vpc_id

    @property
    def account_id(self):
        """Gets the account_id of this HaVipForDescribeHaVipsOutput.  # noqa: E501


        :return: The account_id of this HaVipForDescribeHaVipsOutput.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this HaVipForDescribeHaVipsOutput.


        :param account_id: The account_id of this HaVipForDescribeHaVipsOutput.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def associated_eip_address(self):
        """Gets the associated_eip_address of this HaVipForDescribeHaVipsOutput.  # noqa: E501


        :return: The associated_eip_address of this HaVipForDescribeHaVipsOutput.  # noqa: E501
        :rtype: str
        """
        return self._associated_eip_address

    @associated_eip_address.setter
    def associated_eip_address(self, associated_eip_address):
        """Sets the associated_eip_address of this HaVipForDescribeHaVipsOutput.


        :param associated_eip_address: The associated_eip_address of this HaVipForDescribeHaVipsOutput.  # noqa: E501
        :type: str
        """

        self._associated_eip_address = associated_eip_address

    @property
    def associated_eip_id(self):
        """Gets the associated_eip_id of this HaVipForDescribeHaVipsOutput.  # noqa: E501


        :return: The associated_eip_id of this HaVipForDescribeHaVipsOutput.  # noqa: E501
        :rtype: str
        """
        return self._associated_eip_id

    @associated_eip_id.setter
    def associated_eip_id(self, associated_eip_id):
        """Sets the associated_eip_id of this HaVipForDescribeHaVipsOutput.


        :param associated_eip_id: The associated_eip_id of this HaVipForDescribeHaVipsOutput.  # noqa: E501
        :type: str
        """

        self._associated_eip_id = associated_eip_id

    @property
    def associated_instance_ids(self):
        """Gets the associated_instance_ids of this HaVipForDescribeHaVipsOutput.  # noqa: E501


        :return: The associated_instance_ids of this HaVipForDescribeHaVipsOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._associated_instance_ids

    @associated_instance_ids.setter
    def associated_instance_ids(self, associated_instance_ids):
        """Sets the associated_instance_ids of this HaVipForDescribeHaVipsOutput.


        :param associated_instance_ids: The associated_instance_ids of this HaVipForDescribeHaVipsOutput.  # noqa: E501
        :type: list[str]
        """

        self._associated_instance_ids = associated_instance_ids

    @property
    def associated_instance_type(self):
        """Gets the associated_instance_type of this HaVipForDescribeHaVipsOutput.  # noqa: E501


        :return: The associated_instance_type of this HaVipForDescribeHaVipsOutput.  # noqa: E501
        :rtype: str
        """
        return self._associated_instance_type

    @associated_instance_type.setter
    def associated_instance_type(self, associated_instance_type):
        """Sets the associated_instance_type of this HaVipForDescribeHaVipsOutput.


        :param associated_instance_type: The associated_instance_type of this HaVipForDescribeHaVipsOutput.  # noqa: E501
        :type: str
        """

        self._associated_instance_type = associated_instance_type

    @property
    def created_at(self):
        """Gets the created_at of this HaVipForDescribeHaVipsOutput.  # noqa: E501


        :return: The created_at of this HaVipForDescribeHaVipsOutput.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this HaVipForDescribeHaVipsOutput.


        :param created_at: The created_at of this HaVipForDescribeHaVipsOutput.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def description(self):
        """Gets the description of this HaVipForDescribeHaVipsOutput.  # noqa: E501


        :return: The description of this HaVipForDescribeHaVipsOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this HaVipForDescribeHaVipsOutput.


        :param description: The description of this HaVipForDescribeHaVipsOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def ha_vip_id(self):
        """Gets the ha_vip_id of this HaVipForDescribeHaVipsOutput.  # noqa: E501


        :return: The ha_vip_id of this HaVipForDescribeHaVipsOutput.  # noqa: E501
        :rtype: str
        """
        return self._ha_vip_id

    @ha_vip_id.setter
    def ha_vip_id(self, ha_vip_id):
        """Sets the ha_vip_id of this HaVipForDescribeHaVipsOutput.


        :param ha_vip_id: The ha_vip_id of this HaVipForDescribeHaVipsOutput.  # noqa: E501
        :type: str
        """

        self._ha_vip_id = ha_vip_id

    @property
    def ha_vip_name(self):
        """Gets the ha_vip_name of this HaVipForDescribeHaVipsOutput.  # noqa: E501


        :return: The ha_vip_name of this HaVipForDescribeHaVipsOutput.  # noqa: E501
        :rtype: str
        """
        return self._ha_vip_name

    @ha_vip_name.setter
    def ha_vip_name(self, ha_vip_name):
        """Sets the ha_vip_name of this HaVipForDescribeHaVipsOutput.


        :param ha_vip_name: The ha_vip_name of this HaVipForDescribeHaVipsOutput.  # noqa: E501
        :type: str
        """

        self._ha_vip_name = ha_vip_name

    @property
    def ip_address(self):
        """Gets the ip_address of this HaVipForDescribeHaVipsOutput.  # noqa: E501


        :return: The ip_address of this HaVipForDescribeHaVipsOutput.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this HaVipForDescribeHaVipsOutput.


        :param ip_address: The ip_address of this HaVipForDescribeHaVipsOutput.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

    @property
    def master_instance_id(self):
        """Gets the master_instance_id of this HaVipForDescribeHaVipsOutput.  # noqa: E501


        :return: The master_instance_id of this HaVipForDescribeHaVipsOutput.  # noqa: E501
        :rtype: str
        """
        return self._master_instance_id

    @master_instance_id.setter
    def master_instance_id(self, master_instance_id):
        """Sets the master_instance_id of this HaVipForDescribeHaVipsOutput.


        :param master_instance_id: The master_instance_id of this HaVipForDescribeHaVipsOutput.  # noqa: E501
        :type: str
        """

        self._master_instance_id = master_instance_id

    @property
    def project_name(self):
        """Gets the project_name of this HaVipForDescribeHaVipsOutput.  # noqa: E501


        :return: The project_name of this HaVipForDescribeHaVipsOutput.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this HaVipForDescribeHaVipsOutput.


        :param project_name: The project_name of this HaVipForDescribeHaVipsOutput.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def status(self):
        """Gets the status of this HaVipForDescribeHaVipsOutput.  # noqa: E501


        :return: The status of this HaVipForDescribeHaVipsOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this HaVipForDescribeHaVipsOutput.


        :param status: The status of this HaVipForDescribeHaVipsOutput.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def subnet_id(self):
        """Gets the subnet_id of this HaVipForDescribeHaVipsOutput.  # noqa: E501


        :return: The subnet_id of this HaVipForDescribeHaVipsOutput.  # noqa: E501
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this HaVipForDescribeHaVipsOutput.


        :param subnet_id: The subnet_id of this HaVipForDescribeHaVipsOutput.  # noqa: E501
        :type: str
        """

        self._subnet_id = subnet_id

    @property
    def updated_at(self):
        """Gets the updated_at of this HaVipForDescribeHaVipsOutput.  # noqa: E501


        :return: The updated_at of this HaVipForDescribeHaVipsOutput.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this HaVipForDescribeHaVipsOutput.


        :param updated_at: The updated_at of this HaVipForDescribeHaVipsOutput.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

    @property
    def vpc_id(self):
        """Gets the vpc_id of this HaVipForDescribeHaVipsOutput.  # noqa: E501


        :return: The vpc_id of this HaVipForDescribeHaVipsOutput.  # noqa: E501
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this HaVipForDescribeHaVipsOutput.


        :param vpc_id: The vpc_id of this HaVipForDescribeHaVipsOutput.  # noqa: E501
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
        if issubclass(HaVipForDescribeHaVipsOutput, dict):
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
        if not isinstance(other, HaVipForDescribeHaVipsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HaVipForDescribeHaVipsOutput):
            return True

        return self.to_dict() != other.to_dict()
