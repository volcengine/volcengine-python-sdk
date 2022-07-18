# coding: utf-8

"""
    cen

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class CenGrantRuleForDescribeGrantRulesToCenOutput(object):
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
        'cen_id': 'str',
        'creation_time': 'str',
        'instance_id': 'str',
        'instance_owner_id': 'str',
        'instance_region_id': 'str',
        'instance_type': 'str'
    }

    attribute_map = {
        'cen_id': 'CenId',
        'creation_time': 'CreationTime',
        'instance_id': 'InstanceId',
        'instance_owner_id': 'InstanceOwnerId',
        'instance_region_id': 'InstanceRegionId',
        'instance_type': 'InstanceType'
    }

    def __init__(self, cen_id=None, creation_time=None, instance_id=None, instance_owner_id=None, instance_region_id=None, instance_type=None, _configuration=None):  # noqa: E501
        """CenGrantRuleForDescribeGrantRulesToCenOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cen_id = None
        self._creation_time = None
        self._instance_id = None
        self._instance_owner_id = None
        self._instance_region_id = None
        self._instance_type = None
        self.discriminator = None

        if cen_id is not None:
            self.cen_id = cen_id
        if creation_time is not None:
            self.creation_time = creation_time
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_owner_id is not None:
            self.instance_owner_id = instance_owner_id
        if instance_region_id is not None:
            self.instance_region_id = instance_region_id
        if instance_type is not None:
            self.instance_type = instance_type

    @property
    def cen_id(self):
        """Gets the cen_id of this CenGrantRuleForDescribeGrantRulesToCenOutput.  # noqa: E501


        :return: The cen_id of this CenGrantRuleForDescribeGrantRulesToCenOutput.  # noqa: E501
        :rtype: str
        """
        return self._cen_id

    @cen_id.setter
    def cen_id(self, cen_id):
        """Sets the cen_id of this CenGrantRuleForDescribeGrantRulesToCenOutput.


        :param cen_id: The cen_id of this CenGrantRuleForDescribeGrantRulesToCenOutput.  # noqa: E501
        :type: str
        """

        self._cen_id = cen_id

    @property
    def creation_time(self):
        """Gets the creation_time of this CenGrantRuleForDescribeGrantRulesToCenOutput.  # noqa: E501


        :return: The creation_time of this CenGrantRuleForDescribeGrantRulesToCenOutput.  # noqa: E501
        :rtype: str
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this CenGrantRuleForDescribeGrantRulesToCenOutput.


        :param creation_time: The creation_time of this CenGrantRuleForDescribeGrantRulesToCenOutput.  # noqa: E501
        :type: str
        """

        self._creation_time = creation_time

    @property
    def instance_id(self):
        """Gets the instance_id of this CenGrantRuleForDescribeGrantRulesToCenOutput.  # noqa: E501


        :return: The instance_id of this CenGrantRuleForDescribeGrantRulesToCenOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this CenGrantRuleForDescribeGrantRulesToCenOutput.


        :param instance_id: The instance_id of this CenGrantRuleForDescribeGrantRulesToCenOutput.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def instance_owner_id(self):
        """Gets the instance_owner_id of this CenGrantRuleForDescribeGrantRulesToCenOutput.  # noqa: E501


        :return: The instance_owner_id of this CenGrantRuleForDescribeGrantRulesToCenOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_owner_id

    @instance_owner_id.setter
    def instance_owner_id(self, instance_owner_id):
        """Sets the instance_owner_id of this CenGrantRuleForDescribeGrantRulesToCenOutput.


        :param instance_owner_id: The instance_owner_id of this CenGrantRuleForDescribeGrantRulesToCenOutput.  # noqa: E501
        :type: str
        """

        self._instance_owner_id = instance_owner_id

    @property
    def instance_region_id(self):
        """Gets the instance_region_id of this CenGrantRuleForDescribeGrantRulesToCenOutput.  # noqa: E501


        :return: The instance_region_id of this CenGrantRuleForDescribeGrantRulesToCenOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_region_id

    @instance_region_id.setter
    def instance_region_id(self, instance_region_id):
        """Sets the instance_region_id of this CenGrantRuleForDescribeGrantRulesToCenOutput.


        :param instance_region_id: The instance_region_id of this CenGrantRuleForDescribeGrantRulesToCenOutput.  # noqa: E501
        :type: str
        """

        self._instance_region_id = instance_region_id

    @property
    def instance_type(self):
        """Gets the instance_type of this CenGrantRuleForDescribeGrantRulesToCenOutput.  # noqa: E501


        :return: The instance_type of this CenGrantRuleForDescribeGrantRulesToCenOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this CenGrantRuleForDescribeGrantRulesToCenOutput.


        :param instance_type: The instance_type of this CenGrantRuleForDescribeGrantRulesToCenOutput.  # noqa: E501
        :type: str
        """

        self._instance_type = instance_type

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
        if issubclass(CenGrantRuleForDescribeGrantRulesToCenOutput, dict):
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
        if not isinstance(other, CenGrantRuleForDescribeGrantRulesToCenOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CenGrantRuleForDescribeGrantRulesToCenOutput):
            return True

        return self.to_dict() != other.to_dict()
