# coding: utf-8

"""
    ecs

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ModifyInstanceSpecRequest(object):
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
        'client_token': 'str',
        'dry_run': 'bool',
        'instance_id': 'str',
        'instance_type': 'str',
        'instance_type_id': 'str'
    }

    attribute_map = {
        'client_token': 'ClientToken',
        'dry_run': 'DryRun',
        'instance_id': 'InstanceId',
        'instance_type': 'InstanceType',
        'instance_type_id': 'InstanceTypeId'
    }

    def __init__(self, client_token=None, dry_run=None, instance_id=None, instance_type=None, instance_type_id=None, _configuration=None):  # noqa: E501
        """ModifyInstanceSpecRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._client_token = None
        self._dry_run = None
        self._instance_id = None
        self._instance_type = None
        self._instance_type_id = None
        self.discriminator = None

        if client_token is not None:
            self.client_token = client_token
        if dry_run is not None:
            self.dry_run = dry_run
        self.instance_id = instance_id
        if instance_type is not None:
            self.instance_type = instance_type
        self.instance_type_id = instance_type_id

    @property
    def client_token(self):
        """Gets the client_token of this ModifyInstanceSpecRequest.  # noqa: E501


        :return: The client_token of this ModifyInstanceSpecRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_token

    @client_token.setter
    def client_token(self, client_token):
        """Sets the client_token of this ModifyInstanceSpecRequest.


        :param client_token: The client_token of this ModifyInstanceSpecRequest.  # noqa: E501
        :type: str
        """

        self._client_token = client_token

    @property
    def dry_run(self):
        """Gets the dry_run of this ModifyInstanceSpecRequest.  # noqa: E501


        :return: The dry_run of this ModifyInstanceSpecRequest.  # noqa: E501
        :rtype: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        """Sets the dry_run of this ModifyInstanceSpecRequest.


        :param dry_run: The dry_run of this ModifyInstanceSpecRequest.  # noqa: E501
        :type: bool
        """

        self._dry_run = dry_run

    @property
    def instance_id(self):
        """Gets the instance_id of this ModifyInstanceSpecRequest.  # noqa: E501


        :return: The instance_id of this ModifyInstanceSpecRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ModifyInstanceSpecRequest.


        :param instance_id: The instance_id of this ModifyInstanceSpecRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and instance_id is None:
            raise ValueError("Invalid value for `instance_id`, must not be `None`")  # noqa: E501

        self._instance_id = instance_id

    @property
    def instance_type(self):
        """Gets the instance_type of this ModifyInstanceSpecRequest.  # noqa: E501


        :return: The instance_type of this ModifyInstanceSpecRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this ModifyInstanceSpecRequest.


        :param instance_type: The instance_type of this ModifyInstanceSpecRequest.  # noqa: E501
        :type: str
        """

        self._instance_type = instance_type

    @property
    def instance_type_id(self):
        """Gets the instance_type_id of this ModifyInstanceSpecRequest.  # noqa: E501


        :return: The instance_type_id of this ModifyInstanceSpecRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_type_id

    @instance_type_id.setter
    def instance_type_id(self, instance_type_id):
        """Sets the instance_type_id of this ModifyInstanceSpecRequest.


        :param instance_type_id: The instance_type_id of this ModifyInstanceSpecRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and instance_type_id is None:
            raise ValueError("Invalid value for `instance_type_id`, must not be `None`")  # noqa: E501

        self._instance_type_id = instance_type_id

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
        if issubclass(ModifyInstanceSpecRequest, dict):
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
        if not isinstance(other, ModifyInstanceSpecRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModifyInstanceSpecRequest):
            return True

        return self.to_dict() != other.to_dict()
